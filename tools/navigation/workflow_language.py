from __future__ import annotations

from core.languages import language_name as registry_language_name


def language_name(language: str) -> str:
    return registry_language_name(language)
