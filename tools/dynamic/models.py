from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DynamicPage:
    path: str
    language: str
    title: str
    tags: list[str]
    block_count: int
    valid_block_count: int
    issues: list[str]
