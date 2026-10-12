from __future__ import annotations

import os
import sys
import tempfile
import unittest
import urllib.error
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from core.env import env_value, load_local_env  # noqa: E402
from core.llm import (  # noqa: E402
    SharedRequestGate,
    capture_llm_calls,
    chat_completion,
    chat_completions_url,
    chat_message_content,
    request_gate_status,
    reset_request_gate,
    strip_code_fences,
)


class FakeResponse:
    def __init__(self, payload: bytes) -> None:
        self.payload = payload

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def read(self) -> bytes:
        return self.payload


class CoreLlmTests(unittest.TestCase):
    def tearDown(self) -> None:
        reset_request_gate()

    def test_chat_completions_url_accepts_base_or_endpoint(self) -> None:
        self.assertEqual(
            chat_completions_url("https://example.test/api/v1"),
            "https://example.test/api/v1/chat/completions",
        )
        self.assertEqual(
            chat_completions_url("https://example.test/api/v1/chat/completions"),
            "https://example.test/api/v1/chat/completions",
        )

    def test_strip_code_fences_removes_outer_fence(self) -> None:
        self.assertEqual(strip_code_fences("```json\n{\"ok\": true}\n```"), "{\"ok\": true}")

    def test_chat_message_content_extracts_first_choice(self) -> None:
        data = {"choices": [{"message": {"content": "hello"}}]}
        self.assertEqual(chat_message_content(data, "test"), "hello")

    def test_chat_completion_posts_openai_compatible_payload(self) -> None:
        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["timeout"] = timeout
            captured["headers"] = dict(request.header_items())
            captured["body"] = request.data.decode("utf-8")
            return FakeResponse(b'{"choices":[{"message":{"content":"ok"}}]}')

        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with patch("urllib.request.urlopen", side_effect=fake_urlopen):
                result = chat_completion(
                    model="test-model",
                    messages=[{"role": "user", "content": "Hello"}],
                    title="Test Client",
                    base_url="https://example.test/api/v1",
                    temperature=0.4,
                    timeout=12,
                )

        self.assertEqual(result["choices"][0]["message"]["content"], "ok")
        self.assertEqual(captured["url"], "https://example.test/api/v1/chat/completions")
        self.assertEqual(captured["timeout"], 12)
        self.assertEqual(captured["headers"]["Authorization"], "Bearer test-key")
        self.assertIn('"model": "test-model"', captured["body"])
        self.assertIn('"temperature": 0.4', captured["body"])

    def test_chat_completion_captures_usage_without_response_content(self) -> None:
        response = FakeResponse(
            b'{"model":"provider/model","provider":"test-provider",'
            b'"usage":{"prompt_tokens":10,"completion_tokens":4,"total_tokens":14,"cost":0.001},'
            b'"choices":[{"message":{"content":"secret translation"}}]}'
        )
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with patch("urllib.request.urlopen", return_value=response):
                with capture_llm_calls() as calls:
                    chat_completion(
                        model="requested/model",
                        messages=[{"role": "user", "content": "Hello"}],
                        title="Test Client",
                        base_url="https://example.test/api/v1",
                    )

        self.assertEqual(calls[0]["actual_model"], "provider/model")
        self.assertEqual(calls[0]["total_tokens"], 14)
        self.assertEqual(calls[0]["cost"], 0.001)
        self.assertNotIn("content", calls[0])

    def test_chat_completion_reports_http_error_body(self) -> None:
        error = urllib.error.HTTPError(
            url="https://example.test/api/v1/chat/completions",
            code=400,
            msg="Bad Request",
            hdrs={},
            fp=BytesIO(b"bad request details"),
        )

        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with patch("urllib.request.urlopen", side_effect=error):
                with self.assertRaisesRegex(RuntimeError, "HTTP 400.*bad request details"):
                    chat_completion(
                        model="test-model",
                        messages=[{"role": "user", "content": "Hello"}],
                        title="Test Client",
                        base_url="https://example.test/api/v1",
                    )

    def test_chat_completion_retries_connection_reset(self) -> None:
        response = FakeResponse(b'{"choices":[]}')

        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with (
                patch(
                    "urllib.request.urlopen",
                    side_effect=[ConnectionResetError(10054, "connection reset"), response],
                ) as urlopen,
                patch("core.llm.time.sleep") as sleep,
            ):
                result = chat_completion(
                    model="test-model",
                    messages=[{"role": "user", "content": "Hello"}],
                    title="Test Client",
                    base_url="https://example.test/api/v1",
                )

        self.assertEqual(result, {"choices": []})
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1.0)

    def test_chat_completion_retries_429_and_respects_retry_after(self) -> None:
        error = urllib.error.HTTPError(
            url="https://example.test/api/v1/chat/completions",
            code=429,
            msg="Too Many Requests",
            hdrs={"Retry-After": "0.25"},
            fp=BytesIO(b"rate limited"),
        )
        response = FakeResponse(b'{"choices":[]}')

        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with (
                patch("urllib.request.urlopen", side_effect=[error, response]) as urlopen,
                patch("core.llm.time.sleep") as sleep,
                patch("core.llm._REQUEST_GATE.wait"),
            ):
                result = chat_completion(
                    model="test-model",
                    messages=[{"role": "user", "content": "Hello"}],
                    title="Test Client",
                    base_url="https://example.test/api/v1",
                )

        self.assertEqual(result, {"choices": []})
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(0.25)
        self.assertTrue(request_gate_status()["active"])

    def test_shared_request_gate_reports_and_waits_for_cooldown(self) -> None:
        gate = SharedRequestGate()
        gate.defer(0.01, "test cooldown")

        active = gate.snapshot()
        self.assertTrue(active["active"])
        self.assertEqual(active["reason"], "test cooldown")

        gate.wait()

        self.assertFalse(gate.snapshot()["active"])

    def test_chat_completion_stops_after_bounded_connection_retries(self) -> None:
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False):
            with (
                patch(
                    "urllib.request.urlopen",
                    side_effect=ConnectionResetError(10054, "connection reset"),
                ) as urlopen,
                patch("core.llm.time.sleep") as sleep,
            ):
                with self.assertRaisesRegex(RuntimeError, "after 3 attempts"):
                    chat_completion(
                        model="test-model",
                        messages=[{"role": "user", "content": "Hello"}],
                        title="Test Client",
                        base_url="https://example.test/api/v1",
                    )

        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual([call.args for call in sleep.call_args_list], [(1.0,), (2.0,)])

    def test_load_local_env_does_not_overwrite_existing_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ".env"
            path.write_text("TEST_CORE_ENV=from-file\nEXISTING_CORE_ENV=from-file\n", encoding="utf-8")
            os.environ.pop("TEST_CORE_ENV", None)
            os.environ["EXISTING_CORE_ENV"] = "existing"
            load_local_env(path)
            self.assertEqual(env_value("TEST_CORE_ENV"), "from-file")
            self.assertEqual(os.environ["EXISTING_CORE_ENV"], "existing")
            os.environ.pop("TEST_CORE_ENV", None)
            os.environ.pop("EXISTING_CORE_ENV", None)


if __name__ == "__main__":
    unittest.main()
