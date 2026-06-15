from __future__ import annotations

from translation.cleanup import (
    delete_all_deletable_orphan_translations,
    delete_orphan_translations,
    scan_orphan_translations,
)


def register(registry) -> None:
    registry.get("/api/cleanup/orphans", scan)
    registry.post("/api/cleanup/delete-orphans", delete_selected)
    registry.post("/api/cleanup/delete-all-orphans", delete_all)


def scan(_request) -> dict[str, object]:
    return scan_orphan_translations()


def delete_selected(request) -> dict[str, object] | bool:
    paths = (request.payload or {}).get("paths")
    if not isinstance(paths, list):
        return request.handler.send_error_json(400, "Missing paths list")
    return delete_orphan_translations([str(path) for path in paths])


def delete_all(_request) -> dict[str, object]:
    return delete_all_deletable_orphan_translations()
