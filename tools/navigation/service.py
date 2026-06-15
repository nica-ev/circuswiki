from __future__ import annotations

import json
import tomllib
from pathlib import Path
from typing import Any

from core.languages import language_name

from .config import CONFIGS, DEFAULT_LANGUAGE, MODEL_PATH
from .discovery import PageInfo, discover_pages, rel
from .model import (
    default_empty_model,
    load_nav_model,
    nav_model_exists,
    normalize_page,
    normalized_model,
    slug,
)
from .render import (
    configured_languages,
    duplicate_values,
    model_missing_targets,
    model_page_set,
)


def read_config_nav(language: str) -> list[dict[str, Any]]:
    path = CONFIGS[language]
    if not path.exists():
        return []
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return data.get("project", {}).get("nav", []) or []


def flatten_config_nav(nav: list[dict[str, Any]], prefix: str = "") -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for entry in nav:
        for label, value in entry.items():
            label_path = f"{prefix} / {label}" if prefix else str(label)
            if isinstance(value, str):
                items.append({"label": str(label), "label_path": label_path, "page": value})
            elif isinstance(value, list):
                items.extend(flatten_config_nav(value, label_path))
    return items


def nav_fingerprint(nav: list[dict[str, Any]]) -> str:
    flattened = flatten_config_nav(nav)
    return json.dumps(
        [{"label": item["label_path"], "page": item["page"]} for item in flattened],
        ensure_ascii=False,
        sort_keys=True,
    )


def model_from_current_nav(language: str) -> dict[str, Any]:
    nav = read_config_nav(language)
    pages = discover_pages()
    model = default_empty_model()
    model["source"] = f"current zensical nav ({language})"
    model["items"] = items_from_config_nav(nav, language, pages)
    return normalized_model(model)


def items_from_config_nav(
    nav: list[dict[str, Any]],
    language: str,
    pages: dict[str, dict[str, PageInfo]],
) -> list[dict[str, Any]]:
    used: set[str] = set()

    def unique_id(label: str, page: str | None) -> str:
        base = slug(Path(page).with_suffix("").as_posix() if page else label)
        candidate = base
        index = 2
        while candidate in used:
            candidate = f"{base}-{index}"
            index += 1
        used.add(candidate)
        return candidate

    def convert(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for entry in entries:
            for label, value in entry.items():
                if isinstance(value, str):
                    page = normalize_page(value)
                    item: dict[str, Any] = {
                        "id": unique_id(str(label), page),
                        "page": page,
                        "labels": {language: str(label)},
                    }
                    page_info = pages.get(language, {}).get(page)
                    if page_info and page_info.title and page_info.title != label:
                        item["title"] = page_info.title
                    result.append(item)
                elif isinstance(value, list):
                    result.append(
                        {
                            "id": unique_id(str(label), None),
                            "labels": {language: str(label)},
                            "children": convert(value),
                        }
                    )
        return result

    return convert(nav)


def nav_scan() -> dict[str, Any]:
    languages = configured_languages()
    pages = discover_pages()
    config_navs: dict[str, Any] = {}
    fingerprints: dict[str, list[str]] = {}

    for language in languages:
        nav = read_config_nav(language)
        flattened = flatten_config_nav(nav)
        fingerprint = nav_fingerprint(nav)
        fingerprints.setdefault(fingerprint, []).append(language)
        config_navs[language] = {
            "config": rel(CONFIGS[language]),
            "count": len(flattened),
            "items": flattened,
            "duplicate_pages": duplicate_values([item["page"] for item in flattened]),
            "duplicate_labels": duplicate_values([item["label_path"] for item in flattened]),
            "missing_files": [
                item for item in flattened if normalize_page(item["page"]) not in pages.get(language, {})
            ],
        }

    model = load_nav_model()
    model_pages = model_page_set(model.get("items") or [])
    default_pages = pages.get(DEFAULT_LANGUAGE, {})
    orphan_candidates = [
        {
            "page": page.relative_path,
            "title": page.title,
            "translation_id": page.translation_id,
        }
        for page in sorted(default_pages.values(), key=lambda item: item.relative_path.lower())
        if page.relative_path not in model_pages and not is_low_value_nav_candidate(page.relative_path)
    ]

    return {
        "languages": languages,
        "language_names": {language: language_name(language) for language in languages},
        "model_exists": nav_model_exists(),
        "model_path": rel(MODEL_PATH),
        "model": model,
        "configs": config_navs,
        "nav_variants": [
            {"languages": langs, "count": len(langs)} for langs in fingerprints.values()
        ],
        "has_multiple_navs": len(fingerprints) > 1,
        "model_missing_targets": model_missing_targets(model, pages),
        "orphan_candidate_count": len(orphan_candidates),
        "orphan_candidates": orphan_candidates[:80],
        "page_count_by_language": {language: len(pages.get(language, {})) for language in languages},
    }


def is_low_value_nav_candidate(relative_path: str) -> bool:
    path = relative_path.lower()
    return (
        path == "sitemap.md"
        or path == "tags.md"
        or path.startswith("blog/posts/")
        or path in {"test.md", "release notes.md"}
    )
