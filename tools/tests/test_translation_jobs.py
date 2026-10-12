from __future__ import annotations

import os
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from translation.config import (  # noqa: E402
    BODY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    STRUCTURAL_METADATA_HASH_FIELD,
)
from translation.jobs import (  # noqa: E402
    TranslationJobConflictError,
    TranslationJobManager,
    TranslationJobStateError,
    TranslationJobStore,
)
from translation.service import source_snapshot  # noqa: E402
from core.llm import chat_completion  # noqa: E402


class FakeResponse:
    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def read(self) -> bytes:
        return (
            b'{"model":"actual/model","provider":"test-provider",'
            b'"usage":{"prompt_tokens":8,"completion_tokens":3,"total_tokens":11,"cost":0.002},'
            b'"choices":[{"message":{"content":"translated"}}]}'
        )


def source_text(translation_id: str, body: str = "Source body.") -> str:
    return f"""---
lang: de
translation_id: {translation_id}
translation_status: original
translation_source_lang: de
title: {translation_id}
description: Source description
---

{body}
"""


class TranslationJobTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.database = self.root / ".cache" / "translation_jobs.sqlite3"
        self.managers: list[TranslationJobManager] = []

    def tearDown(self) -> None:
        for manager in reversed(self.managers):
            manager.shutdown(wait=True)
        self.temporary_directory.cleanup()

    def manager(self, translate_item, *, interval: float = 0.01) -> TranslationJobManager:
        manager = TranslationJobManager(
            self.database,
            root=self.root,
            translate_item=translate_item,
            scheduler_interval=interval,
        )
        self.managers.append(manager)
        return manager

    def plan(self, names: list[str]) -> dict[str, object]:
        candidates: list[dict[str, object]] = []
        for name in names:
            source = self.root / "docs" / "de" / f"{name}.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(source_text(name), encoding="utf-8")
            _document, snapshot = source_snapshot(source)
            candidates.append(
                {
                    "translation_id": name,
                    "source_path": f"docs/de/{name}.md",
                    "target_path": f"docs/en/{name}.md",
                    "source_lang": "de",
                    "target_lang": "en",
                    "reason": "missing_file",
                    "source_chars": 12,
                    "source_body_hash": snapshot.body_hash,
                    "source_localized_metadata_hash": snapshot.localized_metadata_hash,
                    "source_structural_metadata_hash": snapshot.structural_metadata_hash,
                }
            )
        return {
            "target_lang": "en",
            "planned_count": len(candidates),
            "total_candidates": len(candidates),
            "candidates": candidates,
        }

    def test_workers_run_concurrently_with_configured_bound(self) -> None:
        lock = threading.Lock()
        two_started = threading.Event()
        active = 0
        maximum_active = 0

        def translate_item(**kwargs: object) -> dict[str, object]:
            nonlocal active, maximum_active
            with lock:
                active += 1
                maximum_active = max(maximum_active, active)
                if active == 2:
                    two_started.set()
            two_started.wait(timeout=1.0)
            time.sleep(0.02)
            with lock:
                active -= 1
            return {"target": kwargs["source_path"], "model": kwargs["model"]}

        manager = self.manager(translate_item)
        manager.start()
        job = manager.create_job(
            plan=self.plan(["one", "two", "three", "four"]),
            model="test-model",
            prompt=None,
            concurrency=2,
        )

        completed = manager.wait_for_terminal(str(job["id"]))

        self.assertEqual(completed["status"], "completed")
        self.assertEqual(completed["counts"].get("completed"), 4)
        self.assertEqual(maximum_active, 2)

    def test_source_change_marks_item_stale_without_translation(self) -> None:
        calls = 0

        def translate_item(**_kwargs: object) -> dict[str, object]:
            nonlocal calls
            calls += 1
            return {}

        plan = self.plan(["stale"])
        source = self.root / "docs" / "de" / "stale.md"
        source.write_text(source_text("stale", "Changed after planning."), encoding="utf-8")
        manager = self.manager(translate_item)
        manager.start()
        job = manager.create_job(plan=plan, model="test-model", prompt=None, concurrency=1)

        completed = manager.wait_for_terminal(str(job["id"]))

        self.assertEqual(calls, 0)
        self.assertEqual(completed["counts"].get("stale"), 1)
        self.assertIn("Source changed", completed["recent_failures"][0]["error"])

    def test_item_failure_does_not_stop_job_and_can_be_retried(self) -> None:
        failed_once = False

        def translate_item(**kwargs: object) -> dict[str, object]:
            nonlocal failed_once
            if str(kwargs["source_path"]).endswith("fail.md") and not failed_once:
                failed_once = True
                raise RuntimeError("temporary failure")
            return {"target": kwargs["source_path"], "model": kwargs["model"]}

        manager = self.manager(translate_item)
        manager.start()
        job = manager.create_job(
            plan=self.plan(["pass", "fail"]),
            model="test-model",
            prompt=None,
            concurrency=2,
        )
        first_run = manager.wait_for_terminal(str(job["id"]))

        self.assertEqual(first_run["counts"].get("completed"), 1)
        self.assertEqual(first_run["counts"].get("failed"), 1)

        retried = manager.retry_failed(str(job["id"]))
        self.assertEqual(retried["retried_items"], 1)
        second_run = manager.wait_for_terminal(str(job["id"]))
        self.assertEqual(second_run["counts"].get("completed"), 2)
        self.assertNotIn("failed", second_run["counts"])

    def test_paused_job_does_not_claim_items_until_resumed(self) -> None:
        calls = 0

        def translate_item(**_kwargs: object) -> dict[str, object]:
            nonlocal calls
            calls += 1
            return {"model": "test-model"}

        store = TranslationJobStore(self.database)
        store.initialize()
        job_id = store.create_job(
            plan=self.plan(["paused"]),
            model="test-model",
            prompt=None,
            concurrency=1,
        )
        store.pause(job_id)
        manager = self.manager(translate_item)
        manager.start()

        time.sleep(0.05)
        self.assertEqual(calls, 0)
        self.assertTrue(manager.get_job(job_id)["paused"])

        manager.resume(job_id)
        completed = manager.wait_for_terminal(job_id)
        self.assertEqual(completed["counts"].get("completed"), 1)

    def test_restart_requeues_running_item_and_recovers_written_target(self) -> None:
        plan = self.plan(["recover"])
        item = plan["candidates"][0]
        store = TranslationJobStore(self.database)
        store.initialize()
        job_id = store.create_job(
            plan=plan,
            model="test-model",
            prompt=None,
            concurrency=1,
        )
        claimed = store.claim_next_item(job_id)
        self.assertIsNotNone(claimed)

        target = self.root / str(item["target_path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            "---\n"
            f"{BODY_HASH_FIELD}: {item['source_body_hash']}\n"
            f"{LOCALIZED_METADATA_HASH_FIELD}: {item['source_localized_metadata_hash']}\n"
            f"{STRUCTURAL_METADATA_HASH_FIELD}: {item['source_structural_metadata_hash']}\n"
            "---\n\nTranslated.\n",
            encoding="utf-8",
        )

        def unexpected_translation(**_kwargs: object) -> dict[str, object]:
            raise AssertionError("Recovered targets must not call the model")

        manager = self.manager(unexpected_translation)
        manager.start()
        completed = manager.wait_for_terminal(job_id)

        self.assertEqual(completed["counts"].get("completed"), 1)
        recovered_items = manager.get_items(job_id, status="completed")
        self.assertEqual(recovered_items[0]["recovered"], 1)

    def test_cancel_stops_queued_items_and_allows_running_item_to_finish(self) -> None:
        started = threading.Event()
        release = threading.Event()

        def translate_item(**kwargs: object) -> dict[str, object]:
            started.set()
            release.wait(timeout=2.0)
            return {"target": kwargs["source_path"], "model": kwargs["model"]}

        manager = self.manager(translate_item)
        manager.start()
        job = manager.create_job(
            plan=self.plan(["running", "queued-one", "queued-two"]),
            model="test-model",
            prompt=None,
            concurrency=1,
        )
        self.assertTrue(started.wait(timeout=2.0))

        cancelling = manager.cancel(str(job["id"]))
        self.assertTrue(cancelling["cancel_requested"])
        release.set()
        cancelled = manager.wait_for_terminal(str(job["id"]))

        self.assertEqual(cancelled["status"], "cancelled")
        self.assertEqual(cancelled["counts"].get("completed"), 1)
        self.assertEqual(cancelled["counts"].get("cancelled"), 2)

    def test_job_aggregates_non_content_llm_usage(self) -> None:
        def translate_item(**kwargs: object) -> dict[str, object]:
            chat_completion(
                model=str(kwargs["model"]),
                messages=[{"role": "user", "content": "translate"}],
                title="Job telemetry test",
                base_url="https://example.test/api/v1",
            )
            return {"target": kwargs["source_path"], "model": kwargs["model"]}

        manager = self.manager(translate_item)
        manager.start()
        with (
            patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False),
            patch("urllib.request.urlopen", return_value=FakeResponse()),
        ):
            job = manager.create_job(
                plan=self.plan(["telemetry"]),
                model="requested/model",
                prompt=None,
                concurrency=1,
            )
            completed = manager.wait_for_terminal(str(job["id"]))

        self.assertEqual(completed["usage"]["api_calls"], 1)
        self.assertEqual(completed["usage"]["total_tokens"], 11)
        self.assertEqual(completed["usage"]["cost"], 0.002)
        item = manager.get_items(str(job["id"]), status="completed")[0]
        self.assertEqual(item["actual_model"], "actual/model")

    def test_only_one_job_can_be_active_and_retry_requires_failures(self) -> None:
        store = TranslationJobStore(self.database)
        store.initialize()
        job_id = store.create_job(
            plan=self.plan(["one"]), model="test-model", prompt=None, concurrency=1
        )

        with self.assertRaises(TranslationJobConflictError):
            store.create_job(
                plan=self.plan(["two"]), model="test-model", prompt=None, concurrency=1
            )
        store.request_cancel(job_id)
        store.finalize_if_idle(job_id)
        with self.assertRaises(TranslationJobStateError):
            store.retry_failed(job_id)


if __name__ == "__main__":
    unittest.main()
