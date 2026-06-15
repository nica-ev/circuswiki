from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from dev_console.routes.registry import RouteRegistry  # noqa: E402


class FakeHandler:
    def __init__(self) -> None:
        self.responses: list[tuple[int, object]] = []

    def send_json(self, payload: object, status: int = 200) -> bool:
        self.responses.append((status, payload))
        return True

    def send_error_json(self, status: int, message: str) -> bool:
        return self.send_json({"error": message}, status=status)


class RouteRegistryTests(unittest.TestCase):
    def test_dispatch_returns_false_for_unknown_route(self) -> None:
        registry = RouteRegistry()
        handler = FakeHandler()
        self.assertFalse(registry.dispatch(method="GET", handler=handler, path="/missing"))
        self.assertEqual(handler.responses, [])

    def test_dispatch_sends_json_for_matched_route_result(self) -> None:
        registry = RouteRegistry()
        registry.get("/ok", lambda request: {"query": request.query_value("q")})
        handler = FakeHandler()
        self.assertTrue(registry.dispatch(method="GET", handler=handler, path="/ok", query_string="q=test"))
        self.assertEqual(handler.responses, [(200, {"query": "test"})])

    def test_dispatch_keeps_explicit_handler_response(self) -> None:
        registry = RouteRegistry()

        def route(request):
            return request.handler.send_error_json(400, "bad")

        registry.post("/bad", route)
        handler = FakeHandler()
        self.assertTrue(registry.dispatch(method="POST", handler=handler, path="/bad", payload={}))
        self.assertEqual(handler.responses, [(400, {"error": "bad"})])

    def test_dispatch_converts_exceptions_to_json_errors(self) -> None:
        registry = RouteRegistry()

        def route(_request):
            raise RuntimeError("boom")

        registry.get("/boom", route)
        handler = FakeHandler()
        self.assertTrue(registry.dispatch(method="GET", handler=handler, path="/boom"))
        self.assertEqual(handler.responses, [(500, {"error": "boom"})])

    def test_dispatch_converts_value_errors_to_bad_request(self) -> None:
        registry = RouteRegistry()

        def route(_request):
            raise ValueError("bad input")

        registry.get("/bad-input", route)
        handler = FakeHandler()
        self.assertTrue(registry.dispatch(method="GET", handler=handler, path="/bad-input"))
        self.assertEqual(handler.responses, [(400, {"error": "bad input"})])

    def test_required_query_value_reports_missing_value(self) -> None:
        registry = RouteRegistry()
        registry.get("/needs-query", lambda request: request.required_query_value("path") or True)
        handler = FakeHandler()

        self.assertTrue(registry.dispatch(method="GET", handler=handler, path="/needs-query"))
        self.assertEqual(handler.responses, [(400, {"error": "Missing path"})])

    def test_required_payload_value_reports_missing_value(self) -> None:
        registry = RouteRegistry()
        registry.post("/needs-payload", lambda request: request.required_payload_value("path") or True)
        handler = FakeHandler()

        self.assertTrue(registry.dispatch(method="POST", handler=handler, path="/needs-payload", payload={}))
        self.assertEqual(handler.responses, [(400, {"error": "Missing path"})])


if __name__ == "__main__":
    unittest.main()
