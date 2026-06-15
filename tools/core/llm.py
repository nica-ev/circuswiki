from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

from core.env import env_value

DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"


def chat_completions_url(base_url: str) -> str:
    normalized = base_url.rstrip("/")
    if normalized.endswith("/chat/completions"):
        return normalized
    return normalized + "/chat/completions"


def default_base_url() -> str:
    return env_value("OPENROUTER_BASE_URL", "OPENAI_BASE_URL", default=DEFAULT_BASE_URL)


def api_key() -> str:
    value = env_value("OPENROUTER_API_KEY", "OPENAI_API_KEY")
    if not value:
        raise RuntimeError("Missing OPENROUTER_API_KEY or OPENAI_API_KEY")
    return value


def chat_completion(
    *,
    model: str,
    messages: list[dict[str, str]],
    title: str,
    base_url: str | None = None,
    temperature: float = 0.2,
    timeout: int = 180,
) -> dict[str, Any]:
    url = chat_completions_url(base_url or default_base_url())
    request = urllib.request.Request(
        url,
        data=json.dumps(
            {
                "model": model,
                "messages": messages,
                "temperature": temperature,
            }
        ).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/nica-ev/circuswiki",
            "X-Title": title,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{title} API request failed with HTTP {exc.code} for {url}: {details}") from exc


def chat_message_content(data: dict[str, Any], context: str) -> str:
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected {context} response: {data}") from exc


def strip_code_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        return "\n".join(lines[1:-1])
    return text
