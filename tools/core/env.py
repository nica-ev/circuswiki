from __future__ import annotations

import os
from pathlib import Path

from core.paths import ROOT


def load_local_env(env_file: Path | None = None) -> None:
    path = env_file or ROOT / ".env"
    if not path.is_file():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def env_value(*names: str, default: str = "") -> str:
    load_local_env()
    for name in names:
        value = os.getenv(name)
        if value:
            return value
    return default
