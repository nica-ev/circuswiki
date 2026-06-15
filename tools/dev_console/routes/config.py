from __future__ import annotations

from core.languages import common_fallback_language, default_language, language_entries
from translation.workflow import default_model, default_prompt, default_prompt_template


def register(registry) -> None:
    registry.get("/api/config", config)


def config(_request) -> dict[str, object]:
    source_lang = default_language()
    target_lang = common_fallback_language()
    return {
        "default_model": default_model(),
        "default_source_lang": source_lang,
        "default_target_lang": target_lang,
        "languages": language_entries(),
        "default_prompt": default_prompt_template(),
        "default_rendered_prompt": default_prompt(source_lang, target_lang),
    }
