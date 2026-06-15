from __future__ import annotations

from translation.workflow import batch_translation_plan, translate_batch_item, translate_page


def register(registry) -> None:
    registry.post("/api/translate", translate)
    registry.post("/api/batch-plan", batch_plan)
    registry.post("/api/batch-translate-file", batch_translate_file)


def translate(request) -> dict[str, object] | bool:
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
        model=request.payload.get("model") or None,
        prompt=request.payload.get("prompt") or None,
        dry_run=bool(request.payload.get("dry_run")),
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
