from __future__ import annotations

import json

from core.env import env_value, load_local_env as core_load_local_env
from core.languages import language_name
from core.llm import chat_completion, chat_completions_url, chat_message_content, strip_code_fences

from .config import DEFAULT_MODEL


def call_label_translation_model(labels: dict[str, str], source_lang: str, target_lang: str, model: str) -> dict[str, str]:
    if not labels:
        return {}
    data = chat_completion(
        model=model,
        messages=[
            {"role": "system", "content": label_prompt(source_lang, target_lang)},
            {"role": "user", "content": json.dumps(labels, ensure_ascii=False, indent=2)},
        ],
        title="CircusWiki Base Label Localization",
    )
    try:
        raw = strip_code_fences(chat_message_content(data, "base label translation")).strip()
        translated = json.loads(raw)
    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Base label translation response was not valid JSON: {data}") from exc
    if not isinstance(translated, dict):
        raise TypeError(f"Base label translation response must be a JSON object: {translated}")
    missing = [key for key in labels if key not in translated]
    if missing:
        raise RuntimeError(f"Base label translation response missing keys: {', '.join(missing)}")
    return {key: str(translated[key]).strip() for key in labels if key in translated}


def label_prompt(source_lang: str, target_lang: str) -> str:
    return f"""You are translating short table column labels for CircusWiki Obsidian Bases from {language_name(source_lang)} to {language_name(target_lang)}.

Translate only the label values. Keep them concise table headers.
Do not translate or rename the JSON keys.
Return only a valid JSON object with the same keys as the input.
Do not wrap the JSON in Markdown fences."""


def load_local_env() -> None:
    core_load_local_env()


def default_model() -> str:
    return env_value("OPENROUTER_MODEL", default=DEFAULT_MODEL)
