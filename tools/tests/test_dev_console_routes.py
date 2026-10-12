from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from dev_console.routes.registry import RouteRegistry  # noqa: E402
from dev_console.routes import translation  # noqa: E402
from translation.jobs import TranslationJobStateError  # noqa: E402


class FakeHandler:
    def __init__(self) -> None:
        self.responses: list[tuple[int, object]] = []
        self.server = SimpleNamespace(translation_job_manager=None)

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

    def test_pattern_route_exposes_named_path_parameter(self) -> None:
        registry = RouteRegistry()
        registry.get_pattern(
            "/jobs/{job_id}/items",
            lambda request: {"job_id": request.path_value("job_id")},
        )
        handler = FakeHandler()

        self.assertTrue(registry.dispatch(method="GET", handler=handler, path="/jobs/abc123/items"))
        self.assertEqual(handler.responses, [(200, {"job_id": "abc123"})])

    def test_translation_job_routes_delegate_to_server_manager(self) -> None:
        class FakeJobManager:
            def __init__(self) -> None:
                self.created = None

            def create_job(self, **kwargs):
                self.created = kwargs
                return {"id": "job-1", "status": "queued"}

            def get_current_job(self):
                return {"id": "job-1", "status": "running"}

            def get_job(self, job_id):
                return {"id": job_id, "status": "running"}

            def get_items(self, job_id, *, status, limit):
                return [{"job_id": job_id, "status": status, "limit": limit}]

            def pause(self, job_id):
                return {"id": job_id, "paused": True}

            resume = pause
            cancel = pause
            retry_failed = pause

        registry = RouteRegistry()
        translation.register(registry)
        manager = FakeJobManager()
        handler = FakeHandler()
        handler.server.translation_job_manager = manager
        plan = {"candidates": [{"translation_id": "example"}]}

        self.assertTrue(
            registry.dispatch(
                method="POST",
                handler=handler,
                path="/api/translation-jobs",
                payload={"plan": plan, "model": "test-model", "concurrency": 3},
            )
        )
        self.assertEqual(manager.created["plan"], plan)
        self.assertEqual(manager.created["concurrency"], 3)
        self.assertEqual(handler.responses[-1], (200, {"id": "job-1", "status": "queued"}))

        registry.dispatch(method="GET", handler=handler, path="/api/translation-jobs/current")
        self.assertEqual(handler.responses[-1][1]["job"]["id"], "job-1")

        registry.dispatch(method="GET", handler=handler, path="/api/translation-jobs/job-1")
        self.assertEqual(handler.responses[-1][1]["id"], "job-1")

        registry.dispatch(
            method="GET",
            handler=handler,
            path="/api/translation-jobs/job-1/items",
            query_string="status=failed&limit=25",
        )
        self.assertEqual(handler.responses[-1][1]["items"][0]["limit"], 25)

        registry.dispatch(
            method="POST",
            handler=handler,
            path="/api/translation-jobs/job-1/pause",
            payload={},
        )
        self.assertTrue(handler.responses[-1][1]["paused"])

    def test_translation_job_state_conflict_returns_409(self) -> None:
        class ConflictManager:
            def pause(self, _job_id):
                raise TranslationJobStateError("cannot pause")

            resume = pause
            cancel = pause
            retry_failed = pause

        registry = RouteRegistry()
        translation.register(registry)
        handler = FakeHandler()
        handler.server.translation_job_manager = ConflictManager()

        registry.dispatch(
            method="POST",
            handler=handler,
            path="/api/translation-jobs/job-1/pause",
            payload={},
        )

        self.assertEqual(handler.responses[-1], (409, {"error": "cannot pause"}))


if __name__ == "__main__":
    unittest.main()
