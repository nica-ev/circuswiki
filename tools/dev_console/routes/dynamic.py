from __future__ import annotations

from dynamic.workflow import check_dynamic_pages, refresh_dynamic_pages, scan_dynamic_pages


def register(registry) -> None:
    registry.get("/api/dynamic/scan", scan)
    registry.get("/api/dynamic/check", check)
    registry.post("/api/dynamic/preview", preview)
    registry.post("/api/dynamic/refresh", refresh)


def scan(request) -> dict[str, object]:
    return scan_dynamic_pages(language=request.query_value("language"))


def check(request) -> dict[str, object]:
    return check_dynamic_pages(
        path=request.query_value("path"),
        language=request.query_value("language"),
    )


def preview(request) -> dict[str, object]:
    payload = request.payload or {}
    return refresh_dynamic_pages(
        path=str(payload.get("path") or ""),
        language=str(payload.get("language") or ""),
        dry_run=True,
        all_languages=bool(payload.get("all_languages")),
    )


def refresh(request) -> dict[str, object]:
    payload = request.payload or {}
    return refresh_dynamic_pages(
        path=str(payload.get("path") or ""),
        language=str(payload.get("language") or ""),
        dry_run=False,
        all_languages=bool(payload.get("all_languages")),
    )
