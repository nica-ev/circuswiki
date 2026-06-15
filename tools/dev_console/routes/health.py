from __future__ import annotations

from translation.workflow import health_summary, inspect_page, list_sources, vault_health_matrix


def register(registry) -> None:
    registry.get("/api/pages", pages)
    registry.get("/api/health", health)
    registry.get("/api/vault-health", vault_health)
    registry.get("/api/page", page)


def pages(request) -> dict[str, object] | bool:
    source_lang = request.query_value("source_lang")
    if not source_lang:
        return request.handler.send_error_json(400, "Missing source_lang")
    return {"pages": list_sources(source_lang)}


def health(request) -> dict[str, object] | bool:
    source_lang = request.query_value("source_lang")
    if not source_lang:
        return request.handler.send_error_json(400, "Missing source_lang")
    target_lang = request.query_value("target_lang")
    if not target_lang:
        return request.handler.send_error_json(400, "Missing target_lang")
    return health_summary(source_lang, target_lang)


def vault_health(_request) -> dict[str, object]:
    return vault_health_matrix()


def page(request) -> dict[str, object] | bool:
    source_path = request.query_value("path")
    if not source_path:
        return request.handler.send_error_json(400, "Missing path")
    source_lang = request.query_value("source_lang")
    if not source_lang:
        return request.handler.send_error_json(400, "Missing source_lang")
    target_lang = request.query_value("target_lang")
    if not target_lang:
        return request.handler.send_error_json(400, "Missing target_lang")
    return inspect_page(source_path, source_lang, target_lang).__dict__
