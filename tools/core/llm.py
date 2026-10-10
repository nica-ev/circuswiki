from __future__ import annotations

import http.client
import json
import logging
import ssl
import time
import urllib.error
import urllib.request
from typing import Any
from urllib.parse import urlparse

from core.env import env_value

DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
RETRYABLE_HTTP_STATUS_CODES = {429, 502, 503, 504}
MAX_RETRY_DELAY_SECONDS = 30.0


def _retry_after_seconds(headers: Any) -> float | None:
    if headers is None:
        return None

    retry_after = headers.get("Retry-After")
    if retry_after is None:
        return None

    try:
        return min(max(float(retry_after), 0.0), MAX_RETRY_DELAY_SECONDS)
    except (TypeError, ValueError):
        return None


def _retry_delay_seconds(attempt: int, headers: Any = None) -> float:
    retry_after = _retry_after_seconds(headers)
    if retry_after is not None:
        return retry_after
    return min(float(2 ** (attempt - 1)), MAX_RETRY_DELAY_SECONDS)


def _wait_before_retry(
    *,
    title: str,
    attempt: int,
    max_attempts: int,
    reason: str,
    headers: Any = None,
) -> None:
    delay = _retry_delay_seconds(attempt, headers)
    logging.warning(
        "%s API request attempt %d/%d failed (%s); retrying in %.1f seconds",
        title,
        attempt,
        max_attempts,
        reason,
        delay,
    )
    time.sleep(delay)


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
    max_attempts: int = 3,
) -> dict[str, Any]:
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    url = chat_completions_url(base_url or default_base_url())
    scheme = urlparse(url).scheme.lower()
    if scheme not in {"http", "https"}:
        raise ValueError(f"Unsupported chat completions URL scheme: {scheme or '<missing>'}")
    request_data = json.dumps(
        {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
    ).encode("utf-8")
    request_headers = {
        "Authorization": f"Bearer {api_key()}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/nica-ev/circuswiki",
        "X-Title": title,
    }

    for attempt in range(1, max_attempts + 1):
        request = urllib.request.Request(
            url,
            data=request_data,
            headers=request_headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            if exc.code in RETRYABLE_HTTP_STATUS_CODES and attempt < max_attempts:
                _wait_before_retry(
                    title=title,
                    attempt=attempt,
                    max_attempts=max_attempts,
                    reason=f"HTTP {exc.code}",
                    headers=exc.headers,
                )
                continue
            raise RuntimeError(
                f"{title} API request failed with HTTP {exc.code} for {url}: {details}"
            ) from exc
        except (
            http.client.IncompleteRead,
            ssl.SSLError,
            TimeoutError,
            ConnectionError,
            urllib.error.URLError,
        ) as exc:
            if attempt < max_attempts:
                _wait_before_retry(
                    title=title,
                    attempt=attempt,
                    max_attempts=max_attempts,
                    reason=str(exc),
                )
                continue
            raise RuntimeError(
                f"{title} API request failed after {max_attempts} attempts for {url}: {exc}"
            ) from exc

    raise AssertionError("unreachable")


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
