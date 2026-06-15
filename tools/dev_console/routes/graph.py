from __future__ import annotations

from translation.original_graph import original_graph


def register(registry) -> None:
    registry.get("/api/original-graph", graph)


def graph(request) -> dict[str, object]:
    return original_graph(exclude_sitemap=request.query_value("exclude_sitemap", "true") != "false")
