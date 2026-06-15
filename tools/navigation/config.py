from __future__ import annotations

from pathlib import Path

from core.languages import default_language, zensical_configs

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
MODEL_PATH = ROOT / "tools" / "navigation" / "nav.json"
DEFAULT_LANGUAGE = default_language()
CONFIGS = zensical_configs()
