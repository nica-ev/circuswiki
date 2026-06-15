from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASES = ROOT / "_bases"
CONFIG_PATH = ROOT / "tools" / "config" / "base_display_names.json"
DEFAULT_MODEL = "google/gemini-2.0-flash-001"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def source_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_base_files() -> list[Path]:
    if not BASES.exists():
        return []
    return sorted(
        path for path in BASES.glob("*.base")
        if path.is_file() and ".generated" not in path.name
    )


def resolve_base(path: str | Path) -> Path:
    base = Path(path)
    resolved = (ROOT / base).resolve() if not base.is_absolute() else base.resolve()
    resolved.relative_to(ROOT)
    return resolved
