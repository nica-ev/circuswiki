from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
import re
from typing import Any
from urllib.parse import parse_qs

RouteHandler = Callable[["Request"], object]


@dataclass(frozen=True)
class Request:
    handler: Any
    path: str
    query_string: str = ""
    payload: dict[str, object] | None = None
    path_params: dict[str, str] | None = None

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

    def path_value(self, key: str, default: str = "") -> str:
        return str((self.path_params or {}).get(key) or default)


class HttpError(RuntimeError):
    def __init__(self, status: int, message: str) -> None:
        super().__init__(message)
        self.status = status


class RouteRegistry:
    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], RouteHandler] = {}
        self._pattern_routes: list[tuple[str, re.Pattern[str], RouteHandler]] = []

    def get(self, path: str, handler: RouteHandler) -> None:
        self._routes[("GET", path)] = handler

    def post(self, path: str, handler: RouteHandler) -> None:
        self._routes[("POST", path)] = handler

    def get_pattern(self, path: str, handler: RouteHandler) -> None:
        self._add_pattern("GET", path, handler)

    def post_pattern(self, path: str, handler: RouteHandler) -> None:
        self._add_pattern("POST", path, handler)

    def _add_pattern(self, method: str, path: str, handler: RouteHandler) -> None:
        parts: list[str] = []
        for segment in path.strip("/").split("/"):
            match = re.fullmatch(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}", segment)
            parts.append(f"(?P<{match.group(1)}>[^/]+)" if match else re.escape(segment))
        self._pattern_routes.append((method, re.compile(r"^/" + "/".join(parts) + r"$"), handler))

    def dispatch(
        self,
        *,
        method: str,
        handler: Any,
        path: str,
        query_string: str = "",
        payload: dict[str, object] | None = None,
    ) -> bool:
        normalized_method = method.upper()
        route = self._routes.get((normalized_method, path))
        path_params: dict[str, str] = {}
        if route is None:
            for pattern_method, pattern, pattern_handler in self._pattern_routes:
                if pattern_method != normalized_method:
                    continue
                match = pattern.fullmatch(path)
                if match:
                    route = pattern_handler
                    path_params = match.groupdict()
                    break
        if route is None:
            return False
        request = Request(
            handler=handler,
            path=path,
            query_string=query_string,
            payload=payload,
            path_params=path_params,
        )
        try:
            result = route(request)
        except HttpError as exc:
            return handler.send_error_json(exc.status, str(exc))
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
