from __future__ import annotations

from translation.workflow import (
    metadata_batch_item,
    metadata_batch_plan,
    repair_vault_metadata,
    translate_metadata_page,
)


def register(registry) -> None:
    registry.post("/api/translate-metadata", translate_metadata)
    registry.post("/api/repair-metadata", repair_metadata)
    registry.post("/api/metadata-batch-plan", batch_plan)
    registry.post("/api/metadata-batch-translate-file", batch_translate_file)


def translate_metadata(request) -> dict[str, object] | bool:
    payload = request.payload or {}
    source_path = request.payload_value("path")
    if not source_path:
        return request.handler.send_error_json(400, "Missing path")
    source_lang = request.required_payload_value("source_lang")
    target_lang = request.required_payload_value("target_lang")
    if not source_lang or not target_lang:
        return True
    return translate_metadata_page(
        source_path=source_path,
        source_lang=source_lang,
        target_lang=target_lang,
        model=payload.get("model") or None,
        dry_run=bool(payload.get("dry_run")),
    )


def repair_metadata(request) -> dict[str, object] | bool:
    source_path = request.payload_value("path")
    if not source_path:
        return request.handler.send_error_json(400, "Missing path")
    return repair_vault_metadata(source_path)


def batch_plan(request) -> dict[str, object]:
    payload = request.payload or {}
    return metadata_batch_plan(
        target_lang=str(payload.get("target_lang") or ""),
        max_files=int(payload.get("max_files") or 0),
        source_lang=str(payload.get("source_lang") or "all"),
        reason=str(payload.get("reason") or "all"),
        path_filter=str(payload.get("path_filter") or ""),
    )


def batch_translate_file(request) -> dict[str, object]:
    payload = request.payload or {}
    return metadata_batch_item(
        source_path=str(payload.get("source_path") or ""),
        source_lang=str(payload.get("source_lang") or ""),
        target_lang=str(payload.get("target_lang") or ""),
        model=payload.get("model") or None,
    )
