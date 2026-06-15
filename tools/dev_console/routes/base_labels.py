from __future__ import annotations

from base_labels import (
    materialize_all_base_labels,
    plan_base_label_translation,
    scan_base_labels,
    translate_base_labels,
)


def register(registry) -> None:
    registry.get("/api/base-labels/scan", scan)
    registry.get("/api/base-labels/plan", plan)
    registry.post("/api/base-labels/translate", translate)
    registry.post("/api/base-labels/materialize", materialize)


def scan(_request) -> dict[str, object]:
    return scan_base_labels()


def plan(request) -> dict[str, object]:
    return plan_base_label_translation(
        base_path=request.query_value("base"),
        target_lang=request.query_value("target_lang", "all"),
    )


def translate(request) -> dict[str, object]:
    payload = request.payload or {}
    return translate_base_labels(
        base_path=str(payload.get("base") or ""),
        target_lang=str(payload.get("target_lang") or "all"),
        model=str(payload.get("model") or "") or None,
        dry_run=bool(payload.get("dry_run")),
    )


def materialize(request) -> dict[str, object]:
    payload = request.payload or {}
    return materialize_all_base_labels(
        base_path=str(payload.get("base") or ""),
        target_lang=str(payload.get("target_lang") or "all"),
    )
