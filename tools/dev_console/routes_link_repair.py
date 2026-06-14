from __future__ import annotations

from urllib.parse import parse_qs

from translation.link_repair_workflow import (
    preview_link_repair,
    preview_source_link_style,
    repair_all_safe_source_link_styles,
    repair_all_safe_link_files,
    repair_link_files,
    repair_source_link_style_files,
    scan_link_repairs,
    scan_source_link_styles,
)


def handle_get(handler, path: str, query_string: str) -> bool:
    if path == "/api/link-repair/scan":
        try:
            query = parse_qs(query_string)
            language = (query.get("language") or [""])[0]
            return handler.send_json(scan_link_repairs(language=language))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/link-repair/preview":
        try:
            query = parse_qs(query_string)
            item_path = (query.get("path") or [""])[0]
            if not item_path:
                return handler.send_error_json(400, "Missing path")
            return handler.send_json(preview_link_repair(item_path))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/source-link-style/scan":
        try:
            query = parse_qs(query_string)
            language = (query.get("language") or [""])[0]
            return handler.send_json(scan_source_link_styles(language=language))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/source-link-style/preview":
        try:
            query = parse_qs(query_string)
            item_path = (query.get("path") or [""])[0]
            if not item_path:
                return handler.send_error_json(400, "Missing path")
            return handler.send_json(preview_source_link_style(item_path))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False


def handle_post(handler, path: str, payload: dict[str, object]) -> bool:
    if path == "/api/link-repair/repair":
        try:
            paths = payload.get("paths")
            if not isinstance(paths, list):
                return handler.send_error_json(400, "Missing paths list")
            return handler.send_json(repair_link_files([str(path) for path in paths]))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/link-repair/repair-all":
        try:
            language = payload.get("language") or ""
            return handler.send_json(repair_all_safe_link_files(str(language)))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/source-link-style/repair":
        try:
            paths = payload.get("paths")
            if not isinstance(paths, list):
                return handler.send_error_json(400, "Missing paths list")
            return handler.send_json(repair_source_link_style_files([str(path) for path in paths]))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/source-link-style/repair-all":
        try:
            language = payload.get("language") or ""
            return handler.send_json(repair_all_safe_source_link_styles(str(language)))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False
