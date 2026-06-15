from __future__ import annotations

import json

from core.llm import chat_completion, chat_message_content, strip_code_fences

from .config import TRANSLATABLE_METADATA_FIELDS, language_name


def call_metadata_translation_model(
    metadata: dict[str, str],
    source_lang: str,
    target_lang: str,
    model: str,
) -> dict[str, str]:
    if not metadata:
        return {}

    data = chat_completion(
        model=model,
        messages=[
            {"role": "system", "content": metadata_prompt(source_lang, target_lang)},
            {"role": "user", "content": json.dumps(metadata, ensure_ascii=False, indent=2)},
        ],
        title="CircusWiki Translation Console",
    )
    content = chat_message_content(data, "metadata translation")
    raw = strip_code_fences(content).strip()
    try:
        translated = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Metadata translation response was not valid JSON: {raw}") from exc

    if not isinstance(translated, dict):
        raise RuntimeError(f"Metadata translation response must be a JSON object: {translated}")

    return {
        key: str(translated[key]).strip()
        for key in TRANSLATABLE_METADATA_FIELDS
        if key in metadata and key in translated
    }


def metadata_prompt(source_lang: str, target_lang: str) -> str:
    source_language = language_name(source_lang)
    target_language = language_name(target_lang)
    fields = ", ".join(TRANSLATABLE_METADATA_FIELDS)
    return f"""You are translating CircusWiki Markdown frontmatter metadata from {source_language} to {target_language}.

Translate only natural-language field values for these fields: {fields}.
Preserve meaning, keep titles concise, and make descriptions natural for metadata/search previews.
Do not add, remove, or rename fields.
Return only a valid JSON object with the same keys as the input.
Do not wrap the JSON in Markdown fences."""
