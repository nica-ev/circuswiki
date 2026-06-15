from __future__ import annotations

import argparse
import os
from pathlib import Path

from core.languages import (
    DEFAULT_BASE_URL,
    normalize_base_path,
    normalize_base_url,
    zensical_configs,
)
from sync_configs import rel, sync_config_text

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = zensical_configs()
DEFAULT_OUTPUT_DIR = ROOT


def materialize_config(
    path: Path,
    target: Path,
    language: str,
    base_path: str,
    base_url: str,
) -> None:
    text = path.read_text(encoding="utf-8")
    text = sync_config_text(text, language, base_path, base_url)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


def materialize_configs(
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    base_path: str | None = None,
    base_url: str | None = None,
) -> dict[str, object]:
    normalized_base_path = normalize_base_path(base_path)
    normalized_base_url = normalize_base_url(base_url)
    generated: dict[str, str] = {}
    for language, path in CONFIGS.items():
        target = output_dir / f".zensical-build.{path.name}"
        materialize_config(path, target, language, normalized_base_path, normalized_base_url)
        generated[language] = rel(target)
    return {
        "base_path": normalized_base_path,
        "base_url": normalized_base_url,
        "output_dir": rel(output_dir),
        "configs": generated,
    }


def configure_file(path: Path, language: str, base_path: str, base_url: str) -> None:
    """Backward-compatible explicit mutator. Prefer sync_configs.py --write."""
    text = sync_config_text(path.read_text(encoding="utf-8"), language, base_path, base_url)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize build-local Zensical configs.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--base-path", default=os.getenv("CIRCUSWIKI_SITE_BASE_PATH"))
    parser.add_argument("--base-url", default=os.getenv("CIRCUSWIKI_SITE_URL") or DEFAULT_BASE_URL)
    args = parser.parse_args()

    output_path = Path(args.output_dir)
    result = materialize_configs(
        output_dir=output_path if output_path.is_absolute() else (ROOT / output_path).resolve(),
        base_path=args.base_path,
        base_url=args.base_url,
    )
    print(f"Materialized Zensical configs: {result['output_dir']}")
    print(f"Configured site base path: {result['base_path']}")
    print(f"Configured site URL: {result['base_url']}")


if __name__ == "__main__":
    main()
