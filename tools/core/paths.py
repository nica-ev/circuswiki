from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
TOOLS = ROOT / "tools"


def rel(path: str | Path, root: Path = ROOT) -> str:
    resolved = Path(path).resolve()
    return resolved.relative_to(root.resolve()).as_posix()


def resolve_under_root(path: str | Path, root: Path = ROOT) -> Path:
    """Resolve path and require it to stay under root.

    Relative paths are resolved against root. Absolute paths are accepted only
    when their resolved target is inside root; otherwise ValueError is raised.
    """
    candidate = Path(path)
    resolved = (root / candidate).resolve() if not candidate.is_absolute() else candidate.resolve()
    resolved_root = root.resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"Path resolves outside root {resolved_root}: {resolved}") from exc
    return resolved
