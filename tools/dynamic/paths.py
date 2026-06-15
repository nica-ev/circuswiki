from __future__ import annotations

from pathlib import Path

from core.paths import DOCS, ROOT


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def abs_path(path: str | Path) -> Path:
    source = Path(path)
    if source.is_absolute():
        return source
    return (ROOT / source).resolve()


def page_language(path: Path) -> str:
    try:
        relative = path.resolve().relative_to(DOCS.resolve()).as_posix()
    except ValueError:
        return ""
    parts = relative.split("/")
    return parts[0] if parts else ""
