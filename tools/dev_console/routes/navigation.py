from __future__ import annotations

from navigation.workflow import (
    apply_nav_model,
    model_from_current_nav,
    nav_scan,
    navigation_preview,
    save_nav_model,
    translate_all_nav_labels,
    translate_nav_labels,
)


def register(registry) -> None:
    registry.get("/api/navigation/scan", scan)
    registry.post("/api/navigation/init", init)
    registry.post("/api/navigation/preview", preview)
    registry.post("/api/navigation/apply", apply)
    registry.post("/api/navigation/translate-labels", translate_labels)
    registry.post("/api/navigation/translate-all-labels", translate_all_labels)


def scan(_request) -> dict[str, object]:
    return nav_scan()


def init(request) -> dict[str, object] | bool:
    language = str((request.payload or {}).get("language") or "")
    if not language:
        return request.handler.send_error_json(400, "Missing language")
    model = save_nav_model(model_from_current_nav(language))
    return {"model": model, "preview": navigation_preview(model)}


def preview(request) -> dict[str, object] | bool:
    model = (request.payload or {}).get("model")
    if not isinstance(model, dict):
        return request.handler.send_error_json(400, "Missing model object")
    return navigation_preview(model)


def apply(request) -> dict[str, object] | bool:
    model = (request.payload or {}).get("model")
    if not isinstance(model, dict):
        return request.handler.send_error_json(400, "Missing model object")
    return apply_nav_model(model, save_model=True)


def translate_labels(request) -> dict[str, object] | bool:
    payload = request.payload or {}
    model = payload.get("model")
    if not isinstance(model, dict):
        return request.handler.send_error_json(400, "Missing model object")
    source_lang = str(payload.get("source_lang") or "")
    target_lang = str(payload.get("target_lang") or "")
    if not source_lang:
        return request.handler.send_error_json(400, "Missing source_lang")
    if not target_lang:
        return request.handler.send_error_json(400, "Missing target_lang")
    llm_model = payload.get("llm_model") or None
    return translate_nav_labels(
        target_lang=target_lang,
        model=model,
        source_lang=source_lang,
        model_name=str(llm_model) if llm_model else None,
    )


def translate_all_labels(request) -> dict[str, object] | bool:
    payload = request.payload or {}
    model = payload.get("model")
    if not isinstance(model, dict):
        return request.handler.send_error_json(400, "Missing model object")
    source_lang = str(payload.get("source_lang") or "")
    if not source_lang:
        return request.handler.send_error_json(400, "Missing source_lang")
    llm_model = payload.get("llm_model") or None
    return translate_all_nav_labels(
        model=model,
        source_lang=source_lang,
        model_name=str(llm_model) if llm_model else None,
    )
