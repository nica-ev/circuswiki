from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any
from urllib.parse import parse_qs

RouteHandler = Callable[["Request"], object]


@dataclass(frozen=True)
class Request:
    handler: Any
    path: str
    query_string: str = ""
    payload: dict[str, object] | None = None

    @property
    def query(self) -> dict[str, list[str]]:
        return parse_qs(self.query_string)

    def query_value(self, key: str, default: str = "") -> str:
        return self.query.get(key, [default])[0] or default

    def required_query_value(self, key: str) -> str | None:
        value = self.query_value(key)
        if not value:
            self.handler.send_error_json(400, f"Missing {key}")
            return None
        return value

    def payload_value(self, key: str, default: str = "") -> str:
        if self.payload is None:
            return default
        return str(self.payload.get(key) or default)

    def required_payload_value(self, key: str) -> str | None:
        value = self.payload_value(key)
        if not value:
            self.handler.send_error_json(400, f"Missing {key}")
            return None
        return value


class RouteRegistry:
    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], RouteHandler] = {}

    def get(self, path: str, handler: RouteHandler) -> None:
        self._routes[("GET", path)] = handler

    def post(self, path: str, handler: RouteHandler) -> None:
        self._routes[("POST", path)] = handler

    def dispatch(
        self,
        *,
        method: str,
        handler: Any,
        path: str,
        query_string: str = "",
        payload: dict[str, object] | None = None,
    ) -> bool:
        route = self._routes.get((method.upper(), path))
        if route is None:
            return False
        request = Request(handler=handler, path=path, query_string=query_string, payload=payload)
        try:
            result = route(request)
        except ValueError as exc:
            return handler.send_error_json(400, str(exc))
        except FileNotFoundError as exc:
            return handler.send_error_json(404, str(exc))
        except Exception as exc:
            logging.exception("Unhandled dev-console route error for %s %s", method, path)
            return handler.send_error_json(500, str(exc))
        if result is True:
            return True
        return handler.send_json(result)


def register_all(registry: RouteRegistry, modules: list[Any]) -> None:
    for module in modules:
        module.register(registry)
