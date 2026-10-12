from __future__ import annotations

from translation.jobs import (
    DEFAULT_CONCURRENCY,
    TranslationJobConflictError,
    TranslationJobNotFoundError,
    TranslationJobStateError,
)
from translation.workflow import batch_translation_plan, default_model, translate_batch_item, translate_page

from .registry import HttpError


def register(registry) -> None:
    registry.post("/api/translate", translate)
    registry.post("/api/batch-plan", batch_plan)
    registry.post("/api/batch-translate-file", batch_translate_file)
    registry.post("/api/translation-jobs", create_translation_job)
    registry.get("/api/translation-jobs/current", current_translation_job)
    registry.get_pattern("/api/translation-jobs/{job_id}", translation_job)
    registry.get_pattern("/api/translation-jobs/{job_id}/items", translation_job_items)
    registry.post_pattern("/api/translation-jobs/{job_id}/{action}", translation_job_action)


def translate(request) -> dict[str, object] | bool:
    payload = request.payload or {}
    source_path = request.payload_value("path")
    if not source_path:
        return request.handler.send_error_json(400, "Missing path")
    source_lang = request.required_payload_value("source_lang")
    target_lang = request.required_payload_value("target_lang")
    if not source_lang or not target_lang:
        return True
    return translate_page(
        source_path=source_path,
        source_lang=source_lang,
        target_lang=target_lang,
        model=payload.get("model") or None,
        prompt=payload.get("prompt") or None,
        dry_run=bool(payload.get("dry_run")),
    )


def batch_plan(request) -> dict[str, object]:
    payload = request.payload or {}
    raw_max_source_chars = payload.get("max_source_chars")
    max_source_chars = (
        int(raw_max_source_chars)
        if raw_max_source_chars not in (None, "", 0, "0")
        else None
    )
    return batch_translation_plan(
        target_lang=str(payload.get("target_lang") or ""),
        max_files=int(payload.get("max_files") or 0),
        source_lang=str(payload.get("source_lang") or "all"),
        reason=str(payload.get("reason") or "all"),
        max_source_chars=max_source_chars,
        path_filter=str(payload.get("path_filter") or ""),
    )


def batch_translate_file(request) -> dict[str, object]:
    payload = request.payload or {}
    return translate_batch_item(
        source_path=str(payload.get("source_path") or ""),
        source_lang=str(payload.get("source_lang") or ""),
        target_lang=str(payload.get("target_lang") or ""),
        model=payload.get("model") or None,
        prompt=payload.get("prompt") or None,
    )


def job_manager(request):
    manager = getattr(request.handler.server, "translation_job_manager", None)
    if manager is None:
        raise HttpError(503, "Translation job manager is unavailable")
    return manager


def create_translation_job(request) -> dict[str, object]:
    payload = request.payload or {}
    plan = payload.get("plan")
    if not isinstance(plan, dict):
        raise ValueError("Missing reviewed translation plan")
    try:
        concurrency = int(payload.get("concurrency") or DEFAULT_CONCURRENCY)
    except (TypeError, ValueError) as exc:
        raise ValueError("concurrency must be an integer") from exc
    try:
        return job_manager(request).create_job(
            plan=plan,
            model=str(payload.get("model") or default_model()),
            prompt=str(payload.get("prompt") or "") or None,
            concurrency=concurrency,
        )
    except TranslationJobConflictError as exc:
        raise HttpError(409, str(exc)) from exc


def current_translation_job(request) -> dict[str, object]:
    return {"job": job_manager(request).get_current_job()}


def translation_job(request) -> dict[str, object]:
    try:
        return job_manager(request).get_job(request.path_value("job_id"))
    except TranslationJobNotFoundError as exc:
        raise HttpError(404, str(exc)) from exc


def translation_job_items(request) -> dict[str, object]:
    raw_limit = request.query_value("limit", "100")
    try:
        limit = int(raw_limit)
    except ValueError as exc:
        raise ValueError("limit must be an integer") from exc
    try:
        items = job_manager(request).get_items(
            request.path_value("job_id"),
            status=request.query_value("status"),
            limit=limit,
        )
    except TranslationJobNotFoundError as exc:
        raise HttpError(404, str(exc)) from exc
    return {"items": items}


def translation_job_action(request) -> dict[str, object]:
    manager = job_manager(request)
    job_id = request.path_value("job_id")
    action = request.path_value("action")
    operations = {
        "pause": manager.pause,
        "resume": manager.resume,
        "cancel": manager.cancel,
        "retry-failed": manager.retry_failed,
    }
    operation = operations.get(action)
    if operation is None:
        raise HttpError(404, f"Unknown translation job action: {action}")
    try:
        return operation(job_id)
    except TranslationJobNotFoundError as exc:
        raise HttpError(404, str(exc)) from exc
    except (TranslationJobConflictError, TranslationJobStateError) as exc:
        raise HttpError(409, str(exc)) from exc
