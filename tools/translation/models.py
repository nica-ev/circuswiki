from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PageStatus:
    source: str
    target: str
    translation_id: str
    source_hash: str
    target_exists: bool
    needs_translation: bool
    issues: list[str]


@dataclass(frozen=True)
class VaultPage:
    path: Path
    rel_path: str
    language: str
    relative_path: str
    frontmatter: str
    body: str
    has_frontmatter: bool
    translation_id: str
    translation_status: str
    translation_source_lang: str
    translation_source: str
    translation_source_hash: str
    title: str
    translation_source_body_hash: str = ""
    translation_source_metadata_hash: str = ""
    translation_source_localized_metadata_hash: str = ""
    translation_source_structural_metadata_hash: str = ""
    translation_model: str = ""
    translation_updated: str = ""
    authors: list[str] | None = None
