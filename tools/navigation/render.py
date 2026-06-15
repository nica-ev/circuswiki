from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from translation.workflow import list_languages

from .config import CONFIGS, DEFAULT_LANGUAGE, MODEL_PATH
from .discovery import PageInfo, discover_pages, rel
from .model import load_nav_model, normalized_model, save_nav_model

NAV_BLOCK_RE = re.compile(r"(?ms)^nav\s*=\s*\[.*?^\]")


def nav_label(item: dict[str, Any], language: str, pages: dict[str, dict[str, PageInfo]]) -> str:
    labels = item.get("labels") or {}
    if labels.get(language):
        return str(labels[language])
    page = item.get("page")
    if page:
        page_info = pages.get(language, {}).get(page)
        if page_info:
            return page_info.title
    if labels.get(DEFAULT_LANGUAGE):
        return str(labels[DEFAULT_LANGUAGE])
    if page:
        page_info = pages.get(DEFAULT_LANGUAGE, {}).get(page)
        if page_info:
            return page_info.title
        return Path(page).stem
    return str(item.get("id", "Navigation"))


def nav_for_language(items: list[dict[str, Any]], language: str, pages: dict[str, dict[str, PageInfo]]) -> list[dict[str, Any]]:
    nav: list[dict[str, Any]] = []
    for item in items:
        label = nav_label(item, language, pages)
        children = item.get("children") or []
        if children:
            nav.append({label: nav_for_language(children, language, pages)})
        elif item.get("page"):
            nav.append({label: item["page"]})
    return nav


def format_nav_block(nav: list[dict[str, Any]]) -> str:
    lines = ["nav = ["]
    lines.extend(format_nav_entries(nav, 2))
    lines.append("]")
    return "\n".join(lines)


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def format_nav_entries(entries: list[dict[str, Any]], indent: int) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent
    for entry in entries:
        for label, value in entry.items():
            if isinstance(value, str):
                lines.append(f"{prefix}{{ {toml_string(label)} = {toml_string(value)} }},")
            elif isinstance(value, list):
                lines.append(f"{prefix}{{ {toml_string(label)} = [")
                lines.extend(format_nav_entries(value, indent + 2))
                lines.append(f"{prefix}] }},")
    return lines


def render_model_navs(model: dict[str, Any] | None = None) -> dict[str, str]:
    model = normalized_model(model or load_nav_model())
    pages = discover_pages()
    rendered: dict[str, str] = {}
    for language in configured_languages():
        rendered[language] = format_nav_block(nav_for_language(model["items"], language, pages))
    return rendered


def configured_languages() -> list[str]:
    return [language for language in list_languages() if language in CONFIGS and CONFIGS[language].exists()]


def replace_nav_block(text: str, nav_block: str) -> str:
    if not NAV_BLOCK_RE.search(text):
        raise ValueError("Could not find nav block in config")
    return NAV_BLOCK_RE.sub(nav_block, text, count=1)


def apply_nav_model(model: dict[str, Any] | None = None, save_model: bool = True) -> dict[str, Any]:
    model = normalized_model(model or load_nav_model())
    if save_model:
        save_nav_model(model)
    rendered = render_model_navs(model)
    changed: list[str] = []
    for language, nav_block in rendered.items():
        path = CONFIGS[language]
        text = path.read_text(encoding="utf-8")
        updated = replace_nav_block(text, nav_block)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(rel(path))
    return {"changed": changed, "changed_count": len(changed), "model_path": rel(MODEL_PATH)}


def duplicate_values(values: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)


def model_page_set(items: list[dict[str, Any]]) -> set[str]:
    pages: set[str] = set()
    for item in items:
        if item.get("page"):
            pages.add(str(item["page"]))
        pages.update(model_page_set(item.get("children") or []))
    return pages


def model_missing_targets(model: dict[str, Any], pages: dict[str, dict[str, PageInfo]]) -> list[dict[str, str]]:
    missing: list[dict[str, str]] = []
    for page in sorted(model_page_set(model.get("items") or [])):
        for language in configured_languages():
            if page not in pages.get(language, {}):
                missing.append({"language": language, "page": page, "status": "will_use_fallback_if_source_exists"})
    return missing


def navigation_preview(model: dict[str, Any] | None = None) -> dict[str, Any]:
    model = normalized_model(model or load_nav_model())
    rendered = render_model_navs(model)
    current: dict[str, str] = {}
    changed: dict[str, bool] = {}
    for language, path in CONFIGS.items():
        if not path.exists() or language not in rendered:
            continue
        match = NAV_BLOCK_RE.search(path.read_text(encoding="utf-8"))
        current[language] = match.group(0) if match else ""
        changed[language] = current[language] != rendered[language]
    return {
        "model": model,
        "rendered": rendered,
        "changed": changed,
        "changed_count": sum(1 for value in changed.values() if value),
    }
