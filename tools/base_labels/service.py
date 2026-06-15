from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from core.languages import default_language, language_codes, language_name

from . import config as cfg
from .parser import extract_display_names
from .translation import call_label_translation_model, default_model


def load_config(path: Path | None = None) -> dict[str, Any]:
    path = path or cfg.CONFIG_PATH
    if not path.is_file():
        return {"version": 1, "bases": {}}
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("base_display_names.json must contain a JSON object")
    data.setdefault("version", 1)
    data.setdefault("bases", {})
    return data


def save_config(config: dict[str, Any], path: Path | None = None) -> None:
    path = path or cfg.CONFIG_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def update_config_sources(config: dict[str, Any], base_path: Path) -> dict[str, Any]:
    base_rel = cfg.rel(base_path)
    labels = extract_display_names(base_path.read_text(encoding="utf-8"))
    base_entry = config.setdefault("bases", {}).setdefault(
        base_rel,
        {"source_lang": default_language(), "properties": {}},
    )
    base_entry.setdefault("source_lang", default_language())
    properties = base_entry.setdefault("properties", {})
    for key, value in labels.items():
        entry = properties.setdefault(key, {"translations": {}})
        old_hash = entry.get("source_hash")
        new_hash = cfg.source_hash(value)
        entry["source"] = value
        entry["source_hash"] = new_hash
        entry.setdefault("translations", {})
        if old_hash and old_hash != new_hash:
            for translation in entry["translations"].values():
                if isinstance(translation, dict):
                    translation["stale"] = True
    for key in list(properties):
        if key not in labels:
            properties[key]["missing_in_base"] = True
    return config


def scan_base_labels() -> dict[str, Any]:
    config = load_config()
    bases = []
    languages = language_codes()
    for base_path in cfg.canonical_base_files():
        labels = extract_display_names(base_path.read_text(encoding="utf-8"))
        config_entry = config.get("bases", {}).get(cfg.rel(base_path), {})
        properties = config_entry.get("properties", {}) if isinstance(config_entry, dict) else {}
        property_rows = []
        missing_count = 0
        stale_count = 0
        for key, value in labels.items():
            entry = properties.get(key, {}) if isinstance(properties, dict) else {}
            translations = entry.get("translations", {}) if isinstance(entry, dict) else {}
            current_hash = cfg.source_hash(value)
            missing_languages = []
            stale_languages = []
            source_lang = (
                config_entry.get("source_lang", default_language())
                if isinstance(config_entry, dict)
                else default_language()
            )
            for language in languages:
                if language == source_lang:
                    continue
                translation = translations.get(language)
                if not isinstance(translation, dict) or not str(translation.get("value") or "").strip():
                    missing_languages.append(language)
                    continue
                if translation.get("source_hash") != current_hash or translation.get("stale"):
                    stale_languages.append(language)
            missing_count += len(missing_languages)
            stale_count += len(stale_languages)
            property_rows.append(
                {
                    "key": key,
                    "source": value,
                    "source_hash": current_hash,
                    "missing_languages": missing_languages,
                    "stale_languages": stale_languages,
                    "translation_count": sum(1 for item in translations.values() if isinstance(item, dict) and item.get("value")),
                }
            )
        bases.append(
            {
                "path": cfg.rel(base_path),
                "source_lang": config_entry.get("source_lang", default_language()) if isinstance(config_entry, dict) else default_language(),
                "property_count": len(labels),
                "missing_count": missing_count,
                "stale_count": stale_count,
                "properties": property_rows,
            }
        )
    return {
        "languages": languages,
        "language_names": {language: language_name(language) for language in languages},
        "config_path": cfg.rel(cfg.CONFIG_PATH),
        "bases": bases,
    }


def labels_for_language(base_path: str | Path, language: str, config: dict[str, Any] | None = None) -> dict[str, str]:
    config = config or load_config()
    base_rel = cfg.rel(cfg.resolve_base(base_path))
    base_entry = config.get("bases", {}).get(base_rel, {})
    source_lang = base_entry.get("source_lang", default_language()) if isinstance(base_entry, dict) else default_language()
    properties = base_entry.get("properties", {}) if isinstance(base_entry, dict) else {}
    labels: dict[str, str] = {}
    for key, entry in properties.items():
        if not isinstance(entry, dict):
            continue
        if language == source_lang:
            value = entry.get("source")
        else:
            translations = entry.get("translations", {})
            translation = translations.get(language) if isinstance(translations, dict) else None
            value = translation.get("value") if isinstance(translation, dict) else None
        if isinstance(value, str) and value.strip():
            labels[str(key)] = value.strip()
    return labels


def plan_base_label_translation(base_path: str = "", target_lang: str = "all") -> dict[str, Any]:
    config = load_config()
    targets = [target_lang] if target_lang != "all" else language_codes()
    candidates = []
    for base in cfg.canonical_base_files():
        if base_path and cfg.rel(base) != base_path:
            continue
        update_config_sources(config, base)
        base_entry = config["bases"][cfg.rel(base)]
        source_lang = base_entry.get("source_lang", default_language())
        for key, entry in base_entry.get("properties", {}).items():
            for language in targets:
                if language == source_lang:
                    continue
                translation = entry.get("translations", {}).get(language)
                current_hash = entry.get("source_hash")
                missing = not isinstance(translation, dict) or not str(translation.get("value") or "").strip()
                stale = isinstance(translation, dict) and (translation.get("source_hash") != current_hash or translation.get("stale"))
                if missing or stale:
                    candidates.append(
                        {
                            "base": cfg.rel(base),
                            "property": key,
                            "source": entry.get("source", ""),
                            "source_lang": source_lang,
                            "target_lang": language,
                            "reason": "missing" if missing else "stale",
                        }
                    )
    return {
        "target_lang": target_lang,
        "base": base_path,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }


def translate_base_labels(base_path: str = "", target_lang: str = "all", model: str | None = None, dry_run: bool = False) -> dict[str, Any]:
    config = load_config()
    targets = [target_lang] if target_lang != "all" else language_codes()
    model = model or default_model()
    results = []
    for base in cfg.canonical_base_files():
        if base_path and cfg.rel(base) != base_path:
            continue
        update_config_sources(config, base)
        base_rel = cfg.rel(base)
        base_entry = config["bases"][base_rel]
        source_lang = base_entry.get("source_lang", default_language())
        properties = base_entry.get("properties", {})
        for language in targets:
            if language == source_lang:
                continue
            pending = {}
            for key, entry in properties.items():
                translation = entry.get("translations", {}).get(language)
                current_hash = entry.get("source_hash")
                missing = not isinstance(translation, dict) or not str(translation.get("value") or "").strip()
                stale = isinstance(translation, dict) and (translation.get("source_hash") != current_hash or translation.get("stale"))
                if missing or stale:
                    pending[key] = entry.get("source", "")
            if not pending:
                continue
            translated = pending if dry_run else call_label_translation_model(pending, source_lang, language, model)
            for key, value in translated.items():
                if key not in properties:
                    continue
                if not dry_run:
                    translations = properties[key].setdefault("translations", {})
                    translations[language] = {
                        "value": str(value).strip(),
                        "source_hash": properties[key].get("source_hash", ""),
                        "model": model,
                        "updated": datetime.now(UTC).isoformat(timespec="seconds"),
                    }
                results.append(
                    {
                        "base": base_rel,
                        "property": key,
                        "source": pending[key],
                        "target_lang": language,
                        "value": str(value).strip(),
                        "dry_run": dry_run,
                    }
                )
    if not dry_run:
        save_config(config)
    return {"model": model, "dry_run": dry_run, "translated_count": len(results), "results": results}
