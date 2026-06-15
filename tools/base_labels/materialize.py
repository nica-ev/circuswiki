from __future__ import annotations

from pathlib import Path
from typing import Any

from core.languages import language_codes

from . import config as cfg
from .parser import LANGUAGE_FILTER_RE, apply_display_names
from .service import labels_for_language


def localize_base_text(text: str, base_path: str | Path, language: str) -> str:
    return apply_display_names(text, labels_for_language(base_path, language))


def materialize_base_labels(base_path: str | Path, language: str, target_path: Path | None = None) -> dict[str, Any]:
    source = cfg.resolve_base(base_path)
    text = source.read_text(encoding="utf-8")
    updated, replacements = LANGUAGE_FILTER_RE.subn(
        lambda match: f"{match.group('prefix')}{match.group('quote')}{language}{match.group('quote')}",
        text,
    )
    if replacements == 0:
        updated = text
    updated = localize_base_text(updated, source, language)
    if target_path is not None:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(updated, encoding="utf-8", newline="\n")
    return {
        "base": cfg.rel(source),
        "language": language,
        "language_replacements": replacements,
        "display_names": labels_for_language(source, language),
        "text": updated,
    }


def materialize_all_base_labels(base_path: str = "", target_lang: str = "all") -> dict[str, Any]:
    targets = [target_lang] if target_lang != "all" else language_codes()
    results = []
    for base in cfg.canonical_base_files():
        if base_path and cfg.rel(base) != base_path:
            continue
        for language in targets:
            target = cfg.BASES / f"{base.stem}.{language}.generated{base.suffix}"
            result = materialize_base_labels(base, language, target)
            result.pop("text", None)
            result["target"] = cfg.rel(target)
            results.append(result)
    return {"materialized_count": len(results), "results": results}
