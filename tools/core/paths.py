from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
TOOLS = ROOT / "tools"


def rel(path: str | Path, root: Path = ROOT) -> str:
    resolved = Path(path).resolve()
    return resolved.relative_to(root.resolve()).as_posix()


def resolve_under_root(path: str | Path, root: Path = ROOT) -> Path:
    candidate = Path(path)
    resolved = (root / candidate).resolve() if not candidate.is_absolute() else candidate.resolve()
    resolved.relative_to(root.resolve())
    return resolved
