from __future__ import annotations

import json
from typing import Any

from core.llm import chat_completion, chat_message_content
from translation.workflow import default_model

from .discovery import PageInfo, discover_pages
from .model import load_nav_model, normalized_model
from .render import configured_languages, nav_label, navigation_preview
from .workflow_language import language_name


def flattened_model_labels(
    items: list[dict[str, Any]],
    source_lang: str,
    pages: dict[str, dict[str, PageInfo]],
) -> list[dict[str, str]]:
    labels: list[dict[str, str]] = []
    for item in items:
        labels.append(
            {
                "id": str(item["id"]),
                "source_label": nav_label(item, source_lang, pages),
                "page": str(item.get("page") or ""),
            }
        )
        labels.extend(flattened_model_labels(item.get("children") or [], source_lang, pages))
    return labels


def set_model_label(items: list[dict[str, Any]], item_id: str, language: str, label: str) -> bool:
    for item in items:
        if item.get("id") == item_id:
            labels = item.setdefault("labels", {})
            if not isinstance(labels, dict):
                labels = {}
                item["labels"] = labels
            labels[language] = label
            return True
        if set_model_label(item.get("children") or [], item_id, language, label):
            return True
    return False


def translate_nav_labels(
    target_lang: str,
    source_lang: str,
    model: dict[str, Any] | None = None,
    model_name: str | None = None,
) -> dict[str, Any]:
    if not source_lang:
        raise ValueError("Missing source language")
    if target_lang == source_lang:
        raise ValueError("Target language must differ from source language")
    if target_lang not in configured_languages():
        raise ValueError(f"Unknown target language: {target_lang}")

    model = normalized_model(model or load_nav_model())
    pages = discover_pages()
    label_items = flattened_model_labels(model["items"], source_lang, pages)
    prompt = {
        "task": "Translate website navigation labels only.",
        "source_language": language_name(source_lang),
        "target_language": language_name(target_lang),
        "rules": [
            "Return JSON only.",
            "Return exactly this schema: {\"translations\":{\"item-id\":\"translated label\"}}.",
            "Do not add, remove, reorder, rename, or restructure navigation items.",
            "Do not translate file paths, IDs, or page values.",
            "Translate labels naturally and concisely for website navigation.",
            "Preserve proper names and project names unless there is an established localized form.",
        ],
        "labels": label_items,
    }
    content = call_navigation_model(json.dumps(prompt, ensure_ascii=False), model_name or default_model())
    parsed = parse_json_response(content)
    translations = parsed.get("translations")
    if not isinstance(translations, dict):
        raise ValueError("LLM response must contain a translations object")

    applied: list[dict[str, str]] = []
    for item_id, label in translations.items():
        if not isinstance(label, str) or not label.strip():
            continue
        if set_model_label(model["items"], str(item_id), target_lang, label.strip()):
            applied.append({"id": str(item_id), "label": label.strip()})

    model["source"] = f"label translation {source_lang}->{target_lang} ({model_name or default_model()})"
    model = normalized_model(model)
    return {
        "model": model,
        "target_lang": target_lang,
        "target_language": language_name(target_lang),
        "translated_count": len(applied),
        "translations": applied,
        "raw": content,
        "preview": navigation_preview(model),
    }


def translate_all_nav_labels(
    source_lang: str,
    model: dict[str, Any] | None = None,
    target_langs: list[str] | None = None,
    model_name: str | None = None,
) -> dict[str, Any]:
    if not source_lang:
        raise ValueError("Missing source language")
    languages = configured_languages()
    if source_lang not in languages:
        raise ValueError(f"Unknown source language: {source_lang}")

    targets = target_langs or [language for language in languages if language != source_lang]
    targets = [language for language in targets if language != source_lang]
    unknown = [language for language in targets if language not in languages]
    if unknown:
        raise ValueError(f"Unknown target languages: {', '.join(unknown)}")

    current_model = normalized_model(model or load_nav_model())
    results: list[dict[str, Any]] = []
    for target_lang in targets:
        result = translate_nav_labels(
            target_lang=target_lang,
            model=current_model,
            source_lang=source_lang,
            model_name=model_name,
        )
        current_model = result["model"]
        results.append(
            {
                "target_lang": target_lang,
                "target_language": result["target_language"],
                "translated_count": result["translated_count"],
                "translations": result["translations"],
                "raw": result["raw"],
            }
        )

    current_model["source"] = f"label translation from {source_lang} to {len(results)} languages ({model_name or default_model()})"
    current_model = normalized_model(current_model)
    return {
        "model": current_model,
        "source_lang": source_lang,
        "source_language": language_name(source_lang),
        "target_count": len(results),
        "results": results,
        "preview": navigation_preview(current_model),
    }


def call_navigation_model(prompt: str, model: str) -> str:
    data = chat_completion(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an information architect for a multilingual Markdown knowledge commons. Return strict JSON only.",
            },
            {"role": "user", "content": prompt},
        ],
        title="CircusWiki Navigation Console",
    )
    return chat_message_content(data, "navigation")


def parse_json_response(content: str) -> dict[str, Any]:
    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1]).strip()
        if text.startswith("json"):
            text = text[4:].strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("LLM response did not contain a JSON object")
    return json.loads(text[start : end + 1])
