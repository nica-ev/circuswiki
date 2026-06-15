from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from translation.workflow import list_languages

from .config import DEFAULT_LANGUAGE, MODEL_PATH, ROOT

ID_RE = re.compile(r"[^a-z0-9]+")


def nav_model_exists() -> bool:
    return MODEL_PATH.exists()


def default_empty_model() -> dict[str, Any]:
    return {
        "version": 1,
        "updated": datetime.now(UTC).isoformat(timespec="seconds"),
        "description": "Canonical CircusWiki navigation model. Edit items, then preview/apply from the dev console.",
        "items": [],
    }


def load_nav_model() -> dict[str, Any]:
    if not MODEL_PATH.exists():
        return default_empty_model()
    return json.loads(MODEL_PATH.read_text(encoding="utf-8"))


def save_nav_model(model: dict[str, Any]) -> dict[str, Any]:
    validate_model(model)
    model = normalized_model(model)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    MODEL_PATH.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return model


def validate_model(model: dict[str, Any]) -> None:
    if not isinstance(model, dict):
        raise ValueError("Navigation model must be a JSON object")
    items = model.get("items")
    if not isinstance(items, list):
        raise ValueError("Navigation model requires an items array")
    validate_items(items)


def validate_items(items: list[Any]) -> None:
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Navigation item must be an object")
        if not item.get("id"):
            raise ValueError("Navigation item is missing id")
        if not item.get("page") and not item.get("children"):
            raise ValueError(f"Navigation item {item.get('id')} needs page or children")
        children = item.get("children", [])
        if children:
            if not isinstance(children, list):
                raise ValueError(f"Navigation item {item.get('id')} children must be an array")
            validate_items(children)


def normalized_model(model: dict[str, Any]) -> dict[str, Any]:
    result = dict(model)
    result["version"] = int(result.get("version") or 1)
    result["updated"] = datetime.now(UTC).isoformat(timespec="seconds")
    result["items"] = normalize_items(result.get("items") or [])
    return result


def normalize_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for item in items:
        entry: dict[str, Any] = {"id": str(item["id"])}
        if item.get("page"):
            entry["page"] = normalize_page(str(item["page"]))
        labels = item.get("labels") or {}
        if isinstance(labels, dict) and labels:
            entry["labels"] = {str(key): str(value) for key, value in labels.items() if value}
        elif item.get("label"):
            entry["labels"] = {DEFAULT_LANGUAGE: str(item["label"])}
        children = item.get("children") or []
        if children:
            entry["children"] = normalize_items(children)
        normalized.append(entry)
    return normalized


def normalize_page(page: str) -> str:
    page = page.replace("\\", "/").strip()
    for language in list_languages():
        prefix = f"docs/{language}/"
        if page.startswith(prefix):
            page = page[len(prefix) :]
            break
    return page


def slug(value: str) -> str:
    value = value.lower().strip()
    value = ID_RE.sub("-", value).strip("-")
    return value or "nav-item"
