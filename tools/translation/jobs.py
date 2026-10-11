from __future__ import annotations

import json
import sqlite3
import threading
import time
import uuid
from collections.abc import Iterator
from concurrent.futures import Future, ThreadPoolExecutor
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Callable

from core.llm import capture_llm_calls, request_gate_status

from .config import (
    BODY_HASH_FIELD,
    LEGACY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    ROOT,
    STRUCTURAL_METADATA_HASH_FIELD,
)
from .markdown import split_markdown
from .metadata import read_scalar
from .service import (
    SourceChangedError,
    require_source_snapshot,
    source_snapshot,
    translate_batch_item,
)


ACTIVE_JOB_STATUSES = ("queued", "running")
TERMINAL_ITEM_STATUSES = ("completed", "failed", "stale", "cancelled")
MAX_CONCURRENCY = 8
DEFAULT_CONCURRENCY = 4


class TranslationJobError(RuntimeError):
    pass


class TranslationJobConflictError(TranslationJobError):
    pass


class TranslationJobNotFoundError(TranslationJobError):
    pass


class TranslationJobStateError(TranslationJobError):
    pass


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def compact_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)


def parse_json(value: str | None, default: object) -> object:
    if not value:
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


class TranslationJobStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=30.0)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 30000")
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as connection:
            connection.execute("PRAGMA journal_mode = WAL")
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS translation_jobs (
                    id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    paused INTEGER NOT NULL DEFAULT 0,
                    cancel_requested INTEGER NOT NULL DEFAULT 0,
                    model TEXT NOT NULL,
                    prompt TEXT,
                    concurrency INTEGER NOT NULL,
                    total_items INTEGER NOT NULL,
                    plan_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    started_at TEXT,
                    finished_at TEXT
                );

                CREATE TABLE IF NOT EXISTS translation_job_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT NOT NULL REFERENCES translation_jobs(id) ON DELETE CASCADE,
                    position INTEGER NOT NULL,
                    translation_id TEXT NOT NULL,
                    source_path TEXT NOT NULL,
                    target_path TEXT NOT NULL,
                    source_lang TEXT NOT NULL,
                    target_lang TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    source_chars INTEGER NOT NULL DEFAULT 0,
                    source_body_hash TEXT NOT NULL,
                    source_localized_metadata_hash TEXT NOT NULL,
                    source_structural_metadata_hash TEXT NOT NULL,
                    status TEXT NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0,
                    started_at TEXT,
                    finished_at TEXT,
                    duration_seconds REAL,
                    result_json TEXT,
                    error TEXT,
                    requested_model TEXT NOT NULL,
                    actual_model TEXT,
                    api_calls INTEGER NOT NULL DEFAULT 0,
                    prompt_tokens INTEGER NOT NULL DEFAULT 0,
                    completion_tokens INTEGER NOT NULL DEFAULT 0,
                    total_tokens INTEGER NOT NULL DEFAULT 0,
                    cost REAL NOT NULL DEFAULT 0,
                    recovered INTEGER NOT NULL DEFAULT 0,
                    UNIQUE(job_id, target_path)
                );

                CREATE INDEX IF NOT EXISTS idx_translation_jobs_status
                    ON translation_jobs(status, created_at);
                CREATE INDEX IF NOT EXISTS idx_translation_job_items_status
                    ON translation_job_items(job_id, status, position);
                """
            )
            existing_columns = {
                str(row["name"])
                for row in connection.execute("PRAGMA table_info(translation_job_items)").fetchall()
            }
            for name, declaration in {
                "api_calls": "INTEGER NOT NULL DEFAULT 0",
                "prompt_tokens": "INTEGER NOT NULL DEFAULT 0",
                "completion_tokens": "INTEGER NOT NULL DEFAULT 0",
                "total_tokens": "INTEGER NOT NULL DEFAULT 0",
                "cost": "REAL NOT NULL DEFAULT 0",
            }.items():
                if name not in existing_columns:
                    connection.execute(
                        f"ALTER TABLE translation_job_items ADD COLUMN {name} {declaration}"
                    )

    def recover_interrupted(self) -> None:
        now = utc_now()
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = 'queued', started_at = NULL, finished_at = NULL,
                    duration_seconds = NULL,
                    error = CASE
                        WHEN error IS NULL OR error = '' THEN 'Requeued after server restart.'
                        ELSE error
                    END
                WHERE status = 'running'
                """
            )
            connection.execute(
                """
                UPDATE translation_jobs
                SET status = 'queued', updated_at = ?, finished_at = NULL
                WHERE status = 'running' AND cancel_requested = 0
                """,
                (now,),
            )
            connection.execute(
                """
                UPDATE translation_jobs
                SET status = 'cancelled', updated_at = ?, finished_at = COALESCE(finished_at, ?)
                WHERE status IN ('queued', 'running') AND cancel_requested = 1
                """,
                (now, now),
            )
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = 'cancelled', finished_at = COALESCE(finished_at, ?)
                WHERE status = 'queued'
                  AND job_id IN (SELECT id FROM translation_jobs WHERE status = 'cancelled')
                """,
                (now,),
            )

    def create_job(
        self,
        *,
        plan: dict[str, object],
        model: str,
        prompt: str | None,
        concurrency: int,
    ) -> str:
        candidates = plan.get("candidates")
        if not isinstance(candidates, list) or not candidates:
            raise ValueError("A translation job requires a non-empty reviewed plan")
        if not 1 <= concurrency <= MAX_CONCURRENCY:
            raise ValueError(f"concurrency must be between 1 and {MAX_CONCURRENCY}")

        required = {
            "translation_id",
            "source_path",
            "target_path",
            "source_lang",
            "target_lang",
            "source_body_hash",
            "source_localized_metadata_hash",
            "source_structural_metadata_hash",
        }
        normalized_candidates: list[dict[str, object]] = []
        targets: set[str] = set()
        for position, raw_item in enumerate(candidates):
            if not isinstance(raw_item, dict):
                raise ValueError(f"Invalid candidate at position {position + 1}")
            missing = sorted(key for key in required if not raw_item.get(key))
            if missing:
                raise ValueError(
                    f"Candidate {position + 1} is missing required fields: {', '.join(missing)}"
                )
            target_path = str(raw_item["target_path"])
            if target_path in targets:
                raise ValueError(f"Reviewed plan contains duplicate target: {target_path}")
            targets.add(target_path)
            normalized_candidates.append(raw_item)

        job_id = uuid.uuid4().hex
        now = utc_now()
        plan_summary = {key: value for key, value in plan.items() if key not in {"candidates"}}

        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            active = connection.execute(
                "SELECT id FROM translation_jobs WHERE status IN ('queued', 'running') LIMIT 1"
            ).fetchone()
            if active is not None:
                raise TranslationJobConflictError(
                    f"Translation job {active['id']} is already active"
                )
            connection.execute(
                """
                INSERT INTO translation_jobs (
                    id, status, paused, cancel_requested, model, prompt, concurrency,
                    total_items, plan_json, created_at, updated_at
                ) VALUES (?, 'queued', 0, 0, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job_id,
                    model,
                    prompt,
                    concurrency,
                    len(normalized_candidates),
                    compact_json(plan_summary),
                    now,
                    now,
                ),
            )
            connection.executemany(
                """
                INSERT INTO translation_job_items (
                    job_id, position, translation_id, source_path, target_path,
                    source_lang, target_lang, reason, source_chars,
                    source_body_hash, source_localized_metadata_hash,
                    source_structural_metadata_hash, status, requested_model
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'queued', ?)
                """,
                [
                    (
                        job_id,
                        position,
                        str(item["translation_id"]),
                        str(item["source_path"]),
                        str(item["target_path"]),
                        str(item["source_lang"]),
                        str(item["target_lang"]),
                        str(item.get("reason") or ""),
                        int(item.get("source_chars") or 0),
                        str(item["source_body_hash"]),
                        str(item["source_localized_metadata_hash"]),
                        str(item["source_structural_metadata_hash"]),
                        model,
                    )
                    for position, item in enumerate(normalized_candidates)
                ],
            )
        return job_id

    def active_job(self) -> dict[str, object] | None:
        with self.connect() as connection:
            row = connection.execute(
                """
                SELECT * FROM translation_jobs
                WHERE status IN ('queued', 'running')
                ORDER BY created_at DESC LIMIT 1
                """
            ).fetchone()
        return dict(row) if row is not None else None

    def current_job_id(self) -> str | None:
        with self.connect() as connection:
            row = connection.execute(
                """
                SELECT id FROM translation_jobs
                ORDER BY CASE WHEN status IN ('queued', 'running') THEN 0 ELSE 1 END,
                         created_at DESC
                LIMIT 1
                """
            ).fetchone()
        return str(row["id"]) if row is not None else None

    def job_row(self, job_id: str) -> dict[str, object]:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT * FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
        if row is None:
            raise TranslationJobNotFoundError(f"Unknown translation job: {job_id}")
        return dict(row)

    def claim_next_item(self, job_id: str) -> dict[str, object] | None:
        now = utc_now()
        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            job = connection.execute(
                "SELECT status, paused, cancel_requested FROM translation_jobs WHERE id = ?",
                (job_id,),
            ).fetchone()
            if (
                job is None
                or job["status"] not in ACTIVE_JOB_STATUSES
                or job["paused"]
                or job["cancel_requested"]
            ):
                return None
            row = connection.execute(
                """
                SELECT * FROM translation_job_items
                WHERE job_id = ? AND status = 'queued'
                ORDER BY position LIMIT 1
                """,
                (job_id,),
            ).fetchone()
            if row is None:
                return None
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = 'running', attempts = attempts + 1, started_at = ?,
                    finished_at = NULL, duration_seconds = NULL, error = NULL
                WHERE id = ? AND status = 'queued'
                """,
                (now, row["id"]),
            )
            connection.execute(
                """
                UPDATE translation_jobs
                SET status = 'running', started_at = COALESCE(started_at, ?), updated_at = ?
                WHERE id = ?
                """,
                (now, now, job_id),
            )
            claimed = connection.execute(
                "SELECT * FROM translation_job_items WHERE id = ?", (row["id"],)
            ).fetchone()
        return dict(claimed) if claimed is not None else None

    def finish_item(
        self,
        item_id: int,
        *,
        status: str,
        result: dict[str, object] | None = None,
        error: str | None = None,
        recovered: bool = False,
        llm_calls: list[dict[str, object]] | None = None,
    ) -> None:
        if status not in TERMINAL_ITEM_STATUSES:
            raise ValueError(f"Invalid terminal item status: {status}")
        now = utc_now()
        with self.connect() as connection:
            row = connection.execute(
                "SELECT job_id, started_at FROM translation_job_items WHERE id = ?",
                (item_id,),
            ).fetchone()
            if row is None:
                return
            duration = None
            if row["started_at"]:
                try:
                    duration = max(
                        0.0,
                        (datetime.fromisoformat(now) - datetime.fromisoformat(row["started_at"])).total_seconds(),
                    )
                except ValueError:
                    duration = None
            llm_calls = llm_calls or []
            actual_models = sorted(
                {str(call.get("actual_model") or "") for call in llm_calls if call.get("actual_model")}
            )
            prompt_tokens = sum(int(call.get("prompt_tokens") or 0) for call in llm_calls)
            completion_tokens = sum(int(call.get("completion_tokens") or 0) for call in llm_calls)
            total_tokens = sum(int(call.get("total_tokens") or 0) for call in llm_calls)
            cost = sum(float(call.get("cost") or 0.0) for call in llm_calls)
            stored_result = dict(result or {})
            if llm_calls:
                stored_result["llm_calls"] = llm_calls
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = ?, finished_at = ?, duration_seconds = ?, result_json = ?,
                    error = ?, actual_model = ?, api_calls = ?, prompt_tokens = ?,
                    completion_tokens = ?, total_tokens = ?, cost = ?, recovered = ?
                WHERE id = ?
                """,
                (
                    status,
                    now,
                    duration,
                    compact_json(stored_result) if stored_result else None,
                    error[:8000] if error else None,
                    ", ".join(actual_models) or None,
                    len(llm_calls),
                    prompt_tokens,
                    completion_tokens,
                    total_tokens,
                    cost,
                    int(recovered),
                    item_id,
                ),
            )
            connection.execute(
                "UPDATE translation_jobs SET updated_at = ? WHERE id = ?",
                (now, row["job_id"]),
            )

    def pause(self, job_id: str) -> None:
        self._set_paused(job_id, True)

    def resume(self, job_id: str) -> None:
        self._set_paused(job_id, False)

    def _set_paused(self, job_id: str, paused: bool) -> None:
        now = utc_now()
        with self.connect() as connection:
            row = connection.execute(
                "SELECT status, cancel_requested FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
            if row is None:
                raise TranslationJobNotFoundError(f"Unknown translation job: {job_id}")
            if row["status"] not in ACTIVE_JOB_STATUSES or row["cancel_requested"]:
                raise TranslationJobStateError(
                    f"Translation job {job_id} cannot be {'paused' if paused else 'resumed'}"
                )
            connection.execute(
                "UPDATE translation_jobs SET paused = ?, updated_at = ? WHERE id = ?",
                (int(paused), now, job_id),
            )

    def request_cancel(self, job_id: str) -> None:
        now = utc_now()
        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            row = connection.execute(
                "SELECT status FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
            if row is None:
                raise TranslationJobNotFoundError(f"Unknown translation job: {job_id}")
            if row["status"] not in ACTIVE_JOB_STATUSES:
                raise TranslationJobStateError(f"Translation job {job_id} is already terminal")
            connection.execute(
                """
                UPDATE translation_jobs
                SET cancel_requested = 1, paused = 0, updated_at = ? WHERE id = ?
                """,
                (now, job_id),
            )
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = 'cancelled', finished_at = ?
                WHERE job_id = ? AND status = 'queued'
                """,
                (now, job_id),
            )

    def cancel_item_if_requested(self, job_id: str, item_id: int) -> bool:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT cancel_requested FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
        if row is not None and bool(row["cancel_requested"]):
            self.finish_item(item_id, status="cancelled", error="Cancelled before translation started.")
            return True
        return False

    def retry_failed(self, job_id: str) -> int:
        now = utc_now()
        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            job = connection.execute(
                "SELECT status FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
            if job is None:
                raise TranslationJobNotFoundError(f"Unknown translation job: {job_id}")
            if job["status"] in ACTIVE_JOB_STATUSES:
                raise TranslationJobStateError(f"Translation job {job_id} is still active")
            active = connection.execute(
                """
                SELECT id FROM translation_jobs
                WHERE status IN ('queued', 'running') AND id != ? LIMIT 1
                """,
                (job_id,),
            ).fetchone()
            if active is not None:
                raise TranslationJobConflictError(
                    f"Translation job {active['id']} is already active"
                )
            count = connection.execute(
                "SELECT COUNT(*) AS count FROM translation_job_items WHERE job_id = ? AND status = 'failed'",
                (job_id,),
            ).fetchone()["count"]
            if not count:
                raise TranslationJobStateError(f"Translation job {job_id} has no failed items")
            connection.execute(
                """
                UPDATE translation_job_items
                SET status = 'queued', started_at = NULL, finished_at = NULL,
                    duration_seconds = NULL, result_json = NULL, error = NULL,
                    actual_model = NULL, api_calls = 0, prompt_tokens = 0,
                    completion_tokens = 0, total_tokens = 0, cost = 0, recovered = 0
                WHERE job_id = ? AND status = 'failed'
                """,
                (job_id,),
            )
            connection.execute(
                """
                UPDATE translation_jobs
                SET status = 'queued', paused = 0, cancel_requested = 0,
                    finished_at = NULL, updated_at = ?
                WHERE id = ?
                """,
                (now, job_id),
            )
        return int(count)

    def finalize_if_idle(self, job_id: str) -> str | None:
        now = utc_now()
        with self.connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            job = connection.execute(
                "SELECT status, cancel_requested FROM translation_jobs WHERE id = ?", (job_id,)
            ).fetchone()
            if job is None or job["status"] not in ACTIVE_JOB_STATUSES:
                return None
            active_count = connection.execute(
                """
                SELECT COUNT(*) AS count FROM translation_job_items
                WHERE job_id = ? AND status IN ('queued', 'running')
                """,
                (job_id,),
            ).fetchone()["count"]
            if active_count:
                return None
            status = "cancelled" if job["cancel_requested"] else "completed"
            connection.execute(
                """
                UPDATE translation_jobs
                SET status = ?, paused = 0, updated_at = ?, finished_at = ?
                WHERE id = ?
                """,
                (status, now, now, job_id),
            )
        return status

    def job_summary(self, job_id: str) -> dict[str, object]:
        job = self.job_row(job_id)
        with self.connect() as connection:
            counts = {
                str(row["status"]): int(row["count"])
                for row in connection.execute(
                    """
                    SELECT status, COUNT(*) AS count
                    FROM translation_job_items WHERE job_id = ? GROUP BY status
                    """,
                    (job_id,),
                ).fetchall()
            }
            failures = [
                dict(row)
                for row in connection.execute(
                    """
                    SELECT id, position, translation_id, source_path, target_path,
                           source_lang, target_lang, status, attempts, error
                    FROM translation_job_items
                    WHERE job_id = ? AND status IN ('failed', 'stale')
                    ORDER BY finished_at DESC, position LIMIT 20
                    """,
                    (job_id,),
                ).fetchall()
            ]
            usage = connection.execute(
                """
                SELECT COALESCE(SUM(api_calls), 0) AS api_calls,
                       COALESCE(SUM(prompt_tokens), 0) AS prompt_tokens,
                       COALESCE(SUM(completion_tokens), 0) AS completion_tokens,
                       COALESCE(SUM(total_tokens), 0) AS total_tokens,
                       COALESCE(SUM(cost), 0) AS cost
                FROM translation_job_items WHERE job_id = ?
                """,
                (job_id,),
            ).fetchone()

        total = int(job["total_items"])
        terminal = sum(counts.get(status, 0) for status in TERMINAL_ITEM_STATUSES)
        remaining = max(0, total - terminal)
        elapsed_seconds = 0.0
        if job.get("started_at"):
            end = job.get("finished_at") or utc_now()
            try:
                elapsed_seconds = max(
                    0.0,
                    (datetime.fromisoformat(str(end)) - datetime.fromisoformat(str(job["started_at"]))).total_seconds(),
                )
            except ValueError:
                elapsed_seconds = 0.0
        throughput_per_minute = terminal / elapsed_seconds * 60.0 if terminal and elapsed_seconds else 0.0
        eta_seconds = remaining / throughput_per_minute * 60.0 if throughput_per_minute else None

        return {
            "id": job["id"],
            "status": job["status"],
            "paused": bool(job["paused"]),
            "cancel_requested": bool(job["cancel_requested"]),
            "model": job["model"],
            "concurrency": int(job["concurrency"]),
            "total_items": total,
            "counts": counts,
            "terminal_items": terminal,
            "remaining_items": remaining,
            "progress": terminal / total if total else 1.0,
            "throughput_per_minute": round(throughput_per_minute, 3),
            "eta_seconds": round(eta_seconds, 1) if eta_seconds is not None else None,
            "created_at": job["created_at"],
            "started_at": job["started_at"],
            "updated_at": job["updated_at"],
            "finished_at": job["finished_at"],
            "plan": parse_json(str(job["plan_json"]), {}),
            "recent_failures": failures,
            "usage": {
                "api_calls": int(usage["api_calls"]),
                "prompt_tokens": int(usage["prompt_tokens"]),
                "completion_tokens": int(usage["completion_tokens"]),
                "total_tokens": int(usage["total_tokens"]),
                "cost": float(usage["cost"]),
            },
        }

    def items(self, job_id: str, *, status: str = "", limit: int = 100) -> list[dict[str, object]]:
        self.job_row(job_id)
        limit = min(max(limit, 1), 1000)
        parameters: list[object] = [job_id]
        condition = "job_id = ?"
        if status:
            condition += " AND status = ?"
            parameters.append(status)
        parameters.append(limit)
        with self.connect() as connection:
            rows = connection.execute(
                f"""
                SELECT id, position, translation_id, source_path, target_path,
                       source_lang, target_lang, reason, source_chars, status,
                       attempts, started_at, finished_at, duration_seconds,
                       error, requested_model, actual_model, api_calls,
                       prompt_tokens, completion_tokens, total_tokens, cost, recovered
                FROM translation_job_items
                WHERE {condition}
                ORDER BY position LIMIT ?
                """,
                parameters,
            ).fetchall()
        return [dict(row) for row in rows]


class TranslationJobManager:
    def __init__(
        self,
        database_path: Path,
        *,
        root: Path = ROOT,
        translate_item: Callable[..., dict[str, object]] = translate_batch_item,
        scheduler_interval: float = 0.2,
    ) -> None:
        self.root = root
        self.store = TranslationJobStore(database_path)
        self.translate_item = translate_item
        self.scheduler_interval = scheduler_interval
        self._stop = threading.Event()
        self._wake = threading.Event()
        self._future_lock = threading.Lock()
        self._futures: dict[int, Future[None]] = {}
        self._executor: ThreadPoolExecutor | None = None
        self._scheduler: threading.Thread | None = None

    def start(self) -> None:
        if self._scheduler is not None and self._scheduler.is_alive():
            return
        self.store.initialize()
        self.store.recover_interrupted()
        self._stop.clear()
        self._executor = ThreadPoolExecutor(
            max_workers=MAX_CONCURRENCY,
            thread_name_prefix="translation-worker",
        )
        self._scheduler = threading.Thread(
            target=self._scheduler_loop,
            name="translation-job-scheduler",
            daemon=True,
        )
        self._scheduler.start()

    def shutdown(self, *, wait: bool = True) -> None:
        self._stop.set()
        self._wake.set()
        if self._scheduler is not None:
            self._scheduler.join(timeout=5.0 if wait else 0.5)
        if self._executor is not None:
            self._executor.shutdown(wait=wait, cancel_futures=False)
        self._scheduler = None
        self._executor = None

    def create_job(
        self,
        *,
        plan: dict[str, object],
        model: str,
        prompt: str | None,
        concurrency: int = DEFAULT_CONCURRENCY,
    ) -> dict[str, object]:
        job_id = self.store.create_job(
            plan=plan,
            model=model,
            prompt=prompt,
            concurrency=concurrency,
        )
        self._wake.set()
        return self.get_job(job_id)

    def get_current_job(self) -> dict[str, object] | None:
        job_id = self.store.current_job_id()
        return self.get_job(job_id) if job_id else None

    def get_job(self, job_id: str) -> dict[str, object]:
        summary = self.store.job_summary(job_id)
        summary["rate_limit"] = request_gate_status()
        return summary

    def get_items(self, job_id: str, *, status: str = "", limit: int = 100) -> list[dict[str, object]]:
        return self.store.items(job_id, status=status, limit=limit)

    def pause(self, job_id: str) -> dict[str, object]:
        self.store.pause(job_id)
        self._wake.set()
        return self.get_job(job_id)

    def resume(self, job_id: str) -> dict[str, object]:
        self.store.resume(job_id)
        self._wake.set()
        return self.get_job(job_id)

    def cancel(self, job_id: str) -> dict[str, object]:
        self.store.request_cancel(job_id)
        self._wake.set()
        return self.get_job(job_id)

    def retry_failed(self, job_id: str) -> dict[str, object]:
        retried = self.store.retry_failed(job_id)
        self._wake.set()
        result = self.get_job(job_id)
        result["retried_items"] = retried
        return result

    def wait_for_terminal(self, job_id: str, timeout: float = 10.0) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            job = self.get_job(job_id)
            if job["status"] not in ACTIVE_JOB_STATUSES:
                return job
            time.sleep(0.02)
        raise TimeoutError(f"Translation job {job_id} did not finish within {timeout} seconds")

    def _scheduler_loop(self) -> None:
        while not self._stop.is_set():
            self._remove_done_futures()
            active = self.store.active_job()
            if active is not None:
                job_id = str(active["id"])
                self.store.finalize_if_idle(job_id)
                active = self.store.active_job()
                if active is not None and not active["paused"] and not active["cancel_requested"]:
                    self._fill_worker_slots(active)
                if active is not None and active["cancel_requested"]:
                    self.store.finalize_if_idle(job_id)
            self._wake.wait(self.scheduler_interval)
            self._wake.clear()

    def _remove_done_futures(self) -> None:
        with self._future_lock:
            completed = [item_id for item_id, future in self._futures.items() if future.done()]
            for item_id in completed:
                future = self._futures.pop(item_id)
                try:
                    future.result()
                except Exception:
                    # Worker exceptions are converted to item failures. This is a
                    # final guard so the scheduler remains alive if that conversion
                    # itself unexpectedly fails.
                    pass

    def _fill_worker_slots(self, job: dict[str, object]) -> None:
        if self._executor is None:
            return
        with self._future_lock:
            active_count = sum(1 for future in self._futures.values() if not future.done())
        available = max(0, int(job["concurrency"]) - active_count)
        for _ in range(available):
            item = self.store.claim_next_item(str(job["id"]))
            if item is None:
                break
            future = self._executor.submit(self._run_item, item, job)
            with self._future_lock:
                self._futures[int(item["id"])] = future
            future.add_done_callback(lambda _future: self._wake.set())

    def _run_item(self, item: dict[str, object], job: dict[str, object]) -> None:
        item_id = int(item["id"])
        job_id = str(item["job_id"])
        llm_calls: list[dict[str, object]] = []
        try:
            if self.store.cancel_item_if_requested(job_id, item_id):
                return
            source = (self.root / str(item["source_path"])).resolve()
            _source_doc, snapshot = source_snapshot(source)
            require_source_snapshot(
                snapshot,
                expected_body_hash=str(item["source_body_hash"]),
                expected_localized_metadata_hash=str(item["source_localized_metadata_hash"]),
                expected_structural_metadata_hash=str(item["source_structural_metadata_hash"]),
            )
            if self._target_matches_planned_hashes(item):
                self.store.finish_item(
                    item_id,
                    status="completed",
                    result={"target": item["target_path"], "recovered": True},
                    recovered=True,
                )
                return
            with capture_llm_calls() as llm_calls:
                result = self.translate_item(
                    source_path=str(item["source_path"]),
                    source_lang=str(item["source_lang"]),
                    target_lang=str(item["target_lang"]),
                    model=str(job["model"]),
                    prompt=job.get("prompt") or None,
                    expected_source_body_hash=str(item["source_body_hash"]),
                    expected_source_localized_metadata_hash=str(item["source_localized_metadata_hash"]),
                    expected_source_structural_metadata_hash=str(item["source_structural_metadata_hash"]),
                )
            self.store.finish_item(item_id, status="completed", result=result, llm_calls=llm_calls)
        except SourceChangedError as exc:
            self.store.finish_item(item_id, status="stale", error=str(exc), llm_calls=llm_calls)
        except Exception as exc:
            self.store.finish_item(
                item_id,
                status="failed",
                error=f"{type(exc).__name__}: {exc}",
                llm_calls=llm_calls,
            )
        finally:
            self._wake.set()

    def _target_matches_planned_hashes(self, item: dict[str, object]) -> bool:
        target = (self.root / str(item["target_path"])).resolve()
        if not target.exists():
            return False
        try:
            document = split_markdown(target.read_text(encoding="utf-8"))
        except (OSError, UnicodeError):
            return False
        body_hash = read_scalar(document.frontmatter, BODY_HASH_FIELD) or read_scalar(
            document.frontmatter, LEGACY_HASH_FIELD
        )
        localized_hash = read_scalar(
            document.frontmatter, LOCALIZED_METADATA_HASH_FIELD
        ) or read_scalar(document.frontmatter, METADATA_HASH_FIELD)
        structural_hash = read_scalar(document.frontmatter, STRUCTURAL_METADATA_HASH_FIELD)
        return (
            body_hash == str(item["source_body_hash"])
            and localized_hash == str(item["source_localized_metadata_hash"])
            and structural_hash == str(item["source_structural_metadata_hash"])
        )
