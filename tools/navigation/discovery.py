from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from translation.markdown import split_markdown
from translation.metadata import read_scalar
from translation.workflow import list_languages

from .config import DOCS, ROOT


@dataclass(frozen=True)
class PageInfo:
    language: str
    relative_path: str
    title: str
    translation_id: str
    path: str


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read_page_info(path: Path, language: str) -> PageInfo:
    document = split_markdown(path.read_text(encoding="utf-8"))
    relative_path = path.relative_to(DOCS / language).as_posix()
    return PageInfo(
        language=language,
        relative_path=relative_path,
        title=read_scalar(document.frontmatter, "title") or path.stem,
        translation_id=read_scalar(document.frontmatter, "translation_id") or Path(relative_path).with_suffix("").as_posix(),
        path=rel(path),
    )


def discover_pages() -> dict[str, dict[str, PageInfo]]:
    pages: dict[str, dict[str, PageInfo]] = {}
    for language in list_languages():
        root = DOCS / language
        if not root.exists():
            continue
        for markdown_file in root.rglob("*.md"):
            page = read_page_info(markdown_file, language)
            pages.setdefault(language, {})[page.relative_path] = page
    return pages
