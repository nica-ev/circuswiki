from __future__ import annotations

from obsidian.cli import open_path as open_obsidian_path
from obsidian.cli import status


def register(registry) -> None:
    registry.get("/api/obsidian/status", obsidian_status)
    registry.post("/api/obsidian/open", open_path)


def obsidian_status(_request) -> dict[str, object]:
    return status()


def open_path(request) -> dict[str, object]:
    payload = request.payload or {}
    return open_obsidian_path(
        str(payload.get("path") or ""),
        newtab=bool(payload.get("newtab")),
    )
