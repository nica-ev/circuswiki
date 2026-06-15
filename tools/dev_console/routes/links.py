from __future__ import annotations

from translation.link_repair_workflow import (
    preview_link_repair,
    preview_source_link_style,
    repair_all_safe_link_files,
    repair_all_safe_source_link_styles,
    repair_link_files,
    repair_source_link_style_files,
    scan_link_repairs,
    scan_source_link_styles,
)


def register(registry) -> None:
    registry.get("/api/link-repair/scan", scan_link_repair)
    registry.get("/api/link-repair/preview", preview_link)
    registry.post("/api/link-repair/repair", repair_link)
    registry.post("/api/link-repair/repair-all", repair_all_links)
    registry.get("/api/source-link-style/scan", scan_source_style)
    registry.get("/api/source-link-style/preview", preview_source_style)
    registry.post("/api/source-link-style/repair", repair_source_style)
    registry.post("/api/source-link-style/repair-all", repair_all_source_styles)


def scan_link_repair(request) -> dict[str, object]:
    return scan_link_repairs(language=request.query_value("language"))


def preview_link(request) -> dict[str, object] | bool:
    item_path = request.query_value("path")
    if not item_path:
        return request.handler.send_error_json(400, "Missing path")
    return preview_link_repair(item_path)


def repair_link(request) -> dict[str, object] | bool:
    paths = (request.payload or {}).get("paths")
    if not isinstance(paths, list):
        return request.handler.send_error_json(400, "Missing paths list")
    return repair_link_files([str(path) for path in paths])


def repair_all_links(request) -> dict[str, object]:
    return repair_all_safe_link_files(str((request.payload or {}).get("language") or ""))


def scan_source_style(request) -> dict[str, object]:
    return scan_source_link_styles(language=request.query_value("language"))


def preview_source_style(request) -> dict[str, object] | bool:
    item_path = request.query_value("path")
    if not item_path:
        return request.handler.send_error_json(400, "Missing path")
    return preview_source_link_style(item_path)


def repair_source_style(request) -> dict[str, object] | bool:
    paths = (request.payload or {}).get("paths")
    if not isinstance(paths, list):
        return request.handler.send_error_json(400, "Missing paths list")
    return repair_source_link_style_files([str(path) for path in paths])


def repair_all_source_styles(request) -> dict[str, object]:
    return repair_all_safe_source_link_styles(str((request.payload or {}).get("language") or ""))
