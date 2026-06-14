from __future__ import annotations

from urllib.parse import parse_qs

from dynamic.workflow import check_dynamic_pages, refresh_dynamic_pages, scan_dynamic_pages


def query_value(query: dict[str, list[str]], key: str, default: str = "") -> str:
    return query.get(key, [default])[0] or default


def handle_get(handler, path: str, query_string: str) -> bool:
    query = parse_qs(query_string)

    if path == "/api/dynamic/scan":
        try:
            return handler.send_json(scan_dynamic_pages(language=query_value(query, "language")))
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/dynamic/check":
        try:
            return handler.send_json(
                check_dynamic_pages(
                    path=query_value(query, "path"),
                    language=query_value(query, "language"),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False


def handle_post(handler, path: str, payload: dict[str, object]) -> bool:
    if path == "/api/dynamic/preview":
        try:
            return handler.send_json(
                refresh_dynamic_pages(
                    path=str(payload.get("path") or ""),
                    language=str(payload.get("language") or ""),
                    dry_run=True,
                    all_languages=bool(payload.get("all_languages")),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/dynamic/refresh":
        try:
            return handler.send_json(
                refresh_dynamic_pages(
                    path=str(payload.get("path") or ""),
                    language=str(payload.get("language") or ""),
                    dry_run=False,
                    all_languages=bool(payload.get("all_languages")),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False
