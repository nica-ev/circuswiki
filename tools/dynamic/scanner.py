from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from core.languages import language_codes
from translation.markdown import split_markdown
from translation.metadata import read_scalar

from .blocks import parse_dynamic_blocks
from .body_tags import frontmatter_tags
from .models import DynamicPage
from .obsidian_backend import status as obsidian_status
from .paths import DOCS, abs_path, page_language, rel


def scan_dynamic_pages(language: str = "") -> dict[str, Any]:
    pages = [page_summary(path) for path in dynamic_markdown_files(language=language)]
    return {
        "obsidian": obsidian_status(),
        "total": len(pages),
        "pages": [asdict(page) for page in pages],
    }


def check_dynamic_pages(path: str = "", language: str = "") -> dict[str, Any]:
    pages = [page_summary(item) for item in target_paths(path=path, language=language)]
    return {
        "ok": all(not page.issues for page in pages),
        "total": len(pages),
        "pages": [asdict(page) for page in pages],
    }


def page_summary(path: Path) -> DynamicPage:
    text = path.read_text(encoding="utf-8")
    document = split_markdown(text)
    tags = frontmatter_tags(document.frontmatter)
    blocks = parse_dynamic_blocks(document.body)
    issues: list[str] = []
    if "dynamic" not in tags:
        issues.append("missing dynamic tag")
    if not blocks:
        issues.append("no dynamic block")
    for block in blocks:
        issues.extend(f"block {block.index}: {error}" for error in block.errors)
    return DynamicPage(
        path=rel(path),
        language=page_language(path),
        title=read_scalar(document.frontmatter, "title") or path.stem,
        tags=tags,
        block_count=len(blocks),
        valid_block_count=sum(1 for block in blocks if not block.errors),
        issues=issues,
    )


def target_paths(path: str = "", language: str = "") -> list[Path]:
    if path:
        candidate = abs_path(path)
        if not candidate.exists():
            return []
        return [candidate]
    return dynamic_markdown_files(language=language)


def dynamic_markdown_files(language: str = "") -> list[Path]:
    if language == "all":
        language = ""
    root = DOCS / language if language else DOCS
    if not root.exists():
        return []
    allowed_roots = set(language_codes())
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        language_part = page_language(path)
        if not language and language_part not in allowed_roots:
            continue
        document = split_markdown(path.read_text(encoding="utf-8"))
        if "dynamic" in frontmatter_tags(document.frontmatter):
            files.append(path)
    return files
