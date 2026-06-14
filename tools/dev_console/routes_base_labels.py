from __future__ import annotations

from urllib.parse import parse_qs

from base_labels import (
    materialize_all_base_labels,
    plan_base_label_translation,
    scan_base_labels,
    translate_base_labels,
)


def query_value(query: dict[str, list[str]], key: str, default: str = "") -> str:
    return query.get(key, [default])[0] or default


def handle_get(handler, path: str, query_string: str) -> bool:
    query = parse_qs(query_string)

    if path == "/api/base-labels/scan":
        try:
            return handler.send_json(scan_base_labels())
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/base-labels/plan":
        try:
            return handler.send_json(
                plan_base_label_translation(
                    base_path=query_value(query, "base"),
                    target_lang=query_value(query, "target_lang", "all"),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False


def handle_post(handler, path: str, payload: dict[str, object]) -> bool:
    if path == "/api/base-labels/translate":
        try:
            return handler.send_json(
                translate_base_labels(
                    base_path=str(payload.get("base") or ""),
                    target_lang=str(payload.get("target_lang") or "all"),
                    model=str(payload.get("model") or "") or None,
                    dry_run=bool(payload.get("dry_run")),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    if path == "/api/base-labels/materialize":
        try:
            return handler.send_json(
                materialize_all_base_labels(
                    base_path=str(payload.get("base") or ""),
                    target_lang=str(payload.get("target_lang") or "all"),
                )
            )
        except Exception as exc:
            return handler.send_error_json(500, str(exc))

    return False
