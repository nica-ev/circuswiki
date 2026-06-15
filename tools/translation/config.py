from __future__ import annotations

import json
from pathlib import Path

from core.languages import (
    common_fallback_language,
    default_language,
    language_codes,
    language_name as registry_language_name,
)

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DEFAULT_MODEL = "google/gemini-2.0-flash-001"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
TRANSLATION_METADATA_CONFIG = ROOT / "tools" / "config" / "translation_metadata.json"
LANGUAGES = language_codes()
DEFAULT_LANGUAGE = default_language()
COMMON_FALLBACK_LANGUAGE = common_fallback_language()
DEFAULT_CONTEXT_DESCRIPTION = (
    "CircusWiki pages about circus pedagogy, movement games, inclusive practice, "
    "organizational documentation, and related educational material."
)
LANGUAGE_NAMES = {language: registry_language_name(language) for language in LANGUAGES}
BATCH_TRANSLATION_EXCLUDED_RELATIVE_PATHS = {
    "sitemap.md",
}
BODY_HASH_FIELD = "translation_source_body_hash"
LOCALIZED_METADATA_HASH_FIELD = "translation_source_localized_metadata_hash"
STRUCTURAL_METADATA_HASH_FIELD = "translation_source_structural_metadata_hash"
METADATA_HASH_FIELD = "translation_source_metadata_hash"
LEGACY_HASH_FIELD = "translation_source_hash"
TRANSLATION_FIELD_PREFIXES = ("translation_",)


def language_name(language: str) -> str:
    return registry_language_name(language)


def load_translatable_metadata_fields() -> list[str]:
    if not TRANSLATION_METADATA_CONFIG.is_file():
        return ["title", "description"]

    data = json.loads(TRANSLATION_METADATA_CONFIG.read_text(encoding="utf-8"))
    fields = data.get("translatable_fields")
    if not isinstance(fields, list):
        raise ValueError("translation_metadata.json must contain a translatable_fields list")

    normalized: list[str] = []
    for field in fields:
        if not isinstance(field, str) or not field.strip():
            raise ValueError("translatable_fields entries must be non-empty strings")
        value = field.strip()
        if value not in normalized:
            normalized.append(value)
    return normalized


TRANSLATABLE_METADATA_FIELDS = tuple(load_translatable_metadata_fields())
TARGET_OWNED_METADATA_FIELDS = {
    "lang",
    *TRANSLATABLE_METADATA_FIELDS,
    BODY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    STRUCTURAL_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    LEGACY_HASH_FIELD,
    "translation_model",
    "translation_status",
    "translation_updated",
    "translation_metadata_model",
    "translation_metadata_status",
    "translation_metadata_updated",
}
