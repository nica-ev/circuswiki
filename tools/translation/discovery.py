from __future__ import annotations

from pathlib import Path

from core.languages import extra_docs_language_codes

from .config import DOCS, ROOT, COMMON_FALLBACK_LANGUAGE, DEFAULT_LANGUAGE, LANGUAGES
from .markdown import split_markdown
from .metadata import read_scalar
from .models import VaultPage


def rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(ROOT).as_posix()
    except ValueError as exc:
        raise ValueError(f"Path is outside repository root {ROOT}: {resolved}") from exc


def language_path(path: str | Path, source_lang: str, target_lang: str) -> Path:
    source = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path)
    source_root = (DOCS / source_lang).resolve()
    target_root = (DOCS / target_lang).resolve()
    resolved_source = source.resolve()
    try:
        relative = resolved_source.relative_to(source_root)
    except ValueError as exc:
        raise ValueError(f"Source path is outside docs/{source_lang}: {resolved_source}") from exc
    return target_root / relative


def list_languages() -> list[str]:
    configured = [language for language in LANGUAGES if (DOCS / language).exists()]
    return configured + extra_docs_language_codes()


def list_sources(source_lang: str) -> list[str]:
    source_root = DOCS / source_lang
    return sorted(
        rel(path)
        for path in source_root.rglob("*.md")
        if path.is_file()
    )


def read_list(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    values: list[str] = []

    for index, line in enumerate(lines):
        if line.strip() != f"{key}:":
            continue

        for item in lines[index + 1 :]:
            if not item.startswith((" ", "\t")):
                break

            stripped = item.strip()
            if stripped.startswith("- "):
                values.append(stripped[2:].strip().strip("\"'"))

        break

    return values


def derive_translation_id(path: Path) -> str:
    stem = path.stem.lower()
    return (
        stem.replace(" ", "-")
        .replace("_", "-")
        .replace(".", "-")
        .strip("-")
    )


def derive_translation_id_from_relative(relative_path: str) -> str:
    return Path(relative_path).with_suffix("").as_posix()


def read_vault_page(path: Path, language: str) -> VaultPage:
    from .config import BODY_HASH_FIELD, LOCALIZED_METADATA_HASH_FIELD, METADATA_HASH_FIELD, STRUCTURAL_METADATA_HASH_FIELD

    document = split_markdown(path.read_text(encoding="utf-8"))
    relative_path = path.relative_to(DOCS / language).as_posix()
    translation_id = read_scalar(document.frontmatter, "translation_id")
    return VaultPage(
        path=path,
        rel_path=rel(path),
        language=language,
        relative_path=relative_path,
        frontmatter=document.frontmatter,
        body=document.body,
        has_frontmatter=document.has_frontmatter,
        translation_id=translation_id or derive_translation_id_from_relative(relative_path),
        translation_status=read_scalar(document.frontmatter, "translation_status") or "",
        translation_source_lang=read_scalar(document.frontmatter, "translation_source_lang") or "",
        translation_source=read_scalar(document.frontmatter, "translation_source") or "",
        translation_source_hash=read_scalar(document.frontmatter, "translation_source_hash") or "",
        title=read_scalar(document.frontmatter, "title") or path.stem,
        translation_source_body_hash=read_scalar(document.frontmatter, BODY_HASH_FIELD) or "",
        translation_source_metadata_hash=read_scalar(document.frontmatter, METADATA_HASH_FIELD) or "",
        translation_source_localized_metadata_hash=read_scalar(document.frontmatter, LOCALIZED_METADATA_HASH_FIELD) or "",
        translation_source_structural_metadata_hash=read_scalar(document.frontmatter, STRUCTURAL_METADATA_HASH_FIELD) or "",
        translation_model=read_scalar(document.frontmatter, "translation_model") or "",
        translation_updated=read_scalar(document.frontmatter, "translation_updated") or "",
        authors=read_list(document.frontmatter, "authors"),
    )


def discover_vault_pages() -> tuple[list[str], dict[str, dict[str, list[VaultPage]]]]:
    languages = list_languages()
    groups: dict[str, dict[str, list[VaultPage]]] = {}

    for language in languages:
        language_root = DOCS / language
        for markdown_file in language_root.rglob("*.md"):
            page = read_vault_page(markdown_file, language)
            groups.setdefault(page.translation_id, {}).setdefault(language, []).append(page)

    return languages, groups


def find_group_source_language(pages_by_language: dict[str, list[VaultPage]]) -> str:
    for language, pages in pages_by_language.items():
        if any(page.translation_status == "original" for page in pages):
            return language

    for pages in pages_by_language.values():
        for page in pages:
            if page.translation_source_lang and page.translation_source_lang in pages_by_language:
                return page.translation_source_lang

    for pages in pages_by_language.values():
        for page in pages:
            source = page.translation_source
            if source.startswith("docs/"):
                parts = source.split("/")
                if len(parts) > 2 and parts[1] in pages_by_language:
                    return parts[1]

    if DEFAULT_LANGUAGE in pages_by_language:
        return DEFAULT_LANGUAGE
    if COMMON_FALLBACK_LANGUAGE in pages_by_language:
        return COMMON_FALLBACK_LANGUAGE
    return next(iter(pages_by_language))


def primary_page(pages: list[VaultPage]) -> VaultPage:
    originals = [page for page in pages if page.translation_status == "original"]
    if originals:
        return originals[0]
    return pages[0]
