from __future__ import annotations

from pathlib import Path

from .config import (
    BODY_HASH_FIELD,
    LEGACY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    STRUCTURAL_METADATA_HASH_FIELD,
    language_name,
)
from .discovery import (
    derive_translation_id,
    discover_vault_pages,
    find_group_source_language,
    language_path,
    list_sources,
    primary_page,
    rel,
)
from .hashes import (
    body_hash_matches,
    legacy_source_hash,
    source_localized_metadata_hash,
    source_structural_metadata_hash,
    stored_body_hash,
    stored_localized_metadata_hash,
    translatable_body_hash,
)
from .markdown import split_markdown
from .metadata import missing_scalars, read_scalar
from .metadata_policy import source_owned_metadata_differences
from .models import PageStatus, VaultPage


def source_reference_hashes(source_page: VaultPage | None) -> dict[str, str]:
    if not source_page:
        return {
            "body": "",
            "legacy_body": "",
            "localized_metadata": "",
            "structural_metadata": "",
        }
    return {
        "body": translatable_body_hash(source_page.frontmatter, source_page.body),
        "legacy_body": legacy_source_hash(source_page.frontmatter, source_page.body),
        "localized_metadata": source_localized_metadata_hash(source_page.frontmatter),
        "structural_metadata": source_structural_metadata_hash(source_page.frontmatter),
    }


def common_page_issues(
    page: VaultPage,
    pages: list[VaultPage],
    language: str,
    relative_path: str,
) -> list[str]:
    issues: list[str] = []
    if len(pages) > 1:
        issues.append("duplicate_translation_id_in_language")
    if not page.has_frontmatter:
        issues.append("missing_frontmatter")
    if not read_scalar(page.frontmatter, "translation_id"):
        issues.append("missing_translation_id")
    if page.language != read_scalar(page.frontmatter, "lang"):
        issues.append("lang_mismatch")
    if page.relative_path != relative_path:
        issues.append("relative_path_mismatch")
    return issues


def source_page_issues(page: VaultPage, source_lang: str) -> list[str]:
    issues: list[str] = []
    if page.translation_status != "original":
        issues.append("source_status_not_original")
    if page.translation_source_lang and page.translation_source_lang != source_lang:
        issues.append("source_lang_mismatch")
    if not page.translation_source_lang:
        issues.append("source_missing_translation_source_lang")
    return issues


def translated_page_issues(
    page: VaultPage,
    source_page: VaultPage | None,
    source_lang: str,
    reference_hashes: dict[str, str],
) -> list[str]:
    issues: list[str] = []
    required = [
        "translation_source",
        "translation_source_lang",
        BODY_HASH_FIELD,
        "translation_model",
        "translation_status",
        "translation_updated",
    ]
    for key in missing_scalars(page.frontmatter, required):
        issues.append(f"missing_{key}")
    if page.translation_source_lang and page.translation_source_lang != source_lang:
        issues.append("translation_source_lang_mismatch")
    page_body_hash = stored_body_hash(page)
    if page_body_hash and not body_hash_matches(page_body_hash, reference_hashes["body"], reference_hashes["legacy_body"]):
        issues.append("source_body_hash_mismatch")
    if not page.translation_source_body_hash and page.translation_source_hash:
        issues.append("legacy_source_hash")
    page_localized_hash = stored_localized_metadata_hash(page)
    if page_localized_hash and page_localized_hash != reference_hashes["localized_metadata"]:
        issues.append("source_localized_metadata_hash_mismatch")
    if not page.translation_source_localized_metadata_hash and page.translation_source_metadata_hash:
        issues.append("legacy_metadata_hash")
    if not page_localized_hash:
        issues.append(f"missing_{LOCALIZED_METADATA_HASH_FIELD}")
    if page.translation_source_structural_metadata_hash and page.translation_source_structural_metadata_hash != reference_hashes["structural_metadata"]:
        issues.append("source_structural_metadata_hash_mismatch")
    if not page.translation_source_structural_metadata_hash:
        issues.append(f"missing_{STRUCTURAL_METADATA_HASH_FIELD}")
    source_owned_differences = source_owned_metadata_differences(source_page.frontmatter, page.frontmatter) if source_page else []
    if source_owned_differences:
        issues.append("source_owned_metadata_mismatch")
    if page.translation_status == "missing-translation":
        issues.append("fallback_page")
    return issues


def vault_health_matrix() -> dict[str, object]:
    languages, groups = discover_vault_pages()
    rows: list[dict[str, object]] = []
    totals = {"green": 0, "yellow": 0, "red": 0}

    for translation_id in sorted(groups):
        pages_by_language = groups[translation_id]
        source_lang = find_group_source_language(pages_by_language)
        source_pages = pages_by_language.get(source_lang) or []
        source_page = primary_page(source_pages) if source_pages else None
        reference_hashes = source_reference_hashes(source_page)

        title = source_page.title if source_page else primary_page(next(iter(pages_by_language.values()))).title
        relative_path = source_page.relative_path if source_page else primary_page(next(iter(pages_by_language.values()))).relative_path
        cells: dict[str, dict[str, object]] = {}

        for language in languages:
            pages = pages_by_language.get(language, [])
            page = primary_page(pages) if pages else None

            if not page:
                cells[language] = {
                    "status": "red",
                    "exists": False,
                    "path": "",
                    "relative_path": relative_path,
                    "issues": ["missing_file"],
                }
                totals["red"] += 1
                continue

            issues = common_page_issues(page, pages, language, relative_path)

            if language == source_lang:
                issues.extend(source_page_issues(page, source_lang))
            else:
                issues.extend(translated_page_issues(page, source_page, source_lang, reference_hashes))

            status = "green" if not issues else "yellow"
            totals[status] += 1
            cells[language] = {
                "status": status,
                "exists": True,
                "path": page.rel_path,
                "relative_path": page.relative_path,
                "issues": issues,
            }

        row_issues = sum(len(cell["issues"]) for cell in cells.values())
        missing = sum(1 for cell in cells.values() if cell["status"] == "red")
        rows.append(
            {
                "translation_id": translation_id,
                "title": title,
                "relative_path": relative_path,
                "source_lang": source_lang,
                "issues": row_issues,
                "missing": missing,
                "cells": cells,
            }
        )

    return {
        "languages": languages,
        "language_names": {language: language_name(language) for language in languages},
        "total_notes": len(rows),
        "totals": totals,
        "rows": rows,
    }


def inspect_page(source_path: str | Path, source_lang: str, target_lang: str) -> PageStatus:
    from .config import ROOT

    source = (ROOT / source_path).resolve()
    target = language_path(source, source_lang, target_lang)
    source_doc = split_markdown(source.read_text(encoding="utf-8"))
    issues: list[str] = []

    if not source_doc.has_frontmatter:
        issues.append("source_missing_frontmatter")

    translation_id = read_scalar(source_doc.frontmatter, "translation_id")
    if not translation_id:
        translation_id = derive_translation_id(source)
        issues.append("source_missing_translation_id")

    if read_scalar(source_doc.frontmatter, "lang") != source_lang:
        issues.append("source_lang_mismatch")

    current_hash = translatable_body_hash(source_doc.frontmatter, source_doc.body)
    current_legacy_hash = legacy_source_hash(source_doc.frontmatter, source_doc.body)
    current_localized_metadata_hash = source_localized_metadata_hash(source_doc.frontmatter)
    current_structural_metadata_hash = source_structural_metadata_hash(source_doc.frontmatter)
    target_exists = target.exists()
    needs_translation = not target_exists

    if target_exists:
        target_doc = split_markdown(target.read_text(encoding="utf-8"))
        if not target_doc.has_frontmatter:
            issues.append("target_missing_frontmatter")
            needs_translation = True
        else:
            if read_scalar(target_doc.frontmatter, "lang") != target_lang:
                issues.append("target_lang_mismatch")
            if read_scalar(target_doc.frontmatter, "translation_id") != translation_id:
                issues.append("translation_id_mismatch")
            target_body_hash = (
                read_scalar(target_doc.frontmatter, BODY_HASH_FIELD)
                or read_scalar(target_doc.frontmatter, LEGACY_HASH_FIELD)
                or ""
            )
            if not body_hash_matches(target_body_hash, current_hash, current_legacy_hash):
                issues.append("target_body_outdated")
                needs_translation = True
            target_localized_hash = (
                read_scalar(target_doc.frontmatter, LOCALIZED_METADATA_HASH_FIELD)
                or read_scalar(target_doc.frontmatter, METADATA_HASH_FIELD)
                or ""
            )
            if target_localized_hash != current_localized_metadata_hash:
                issues.append("target_localized_metadata_outdated")
                needs_translation = True
            if read_scalar(target_doc.frontmatter, STRUCTURAL_METADATA_HASH_FIELD) != current_structural_metadata_hash:
                issues.append("target_structural_metadata_outdated")
                needs_translation = True
            if source_owned_metadata_differences(source_doc.frontmatter, target_doc.frontmatter):
                issues.append("target_source_owned_metadata_mismatch")
                needs_translation = True
            missing = missing_scalars(
                target_doc.frontmatter,
                [
                    "translation_source",
                    "translation_source_lang",
                    BODY_HASH_FIELD,
                    "translation_model",
                    "translation_status",
                    "translation_updated",
                ],
            )
            for key in missing:
                issues.append(f"target_missing_{key}")

    return PageStatus(
        source=rel(source),
        target=rel(target),
        translation_id=translation_id,
        source_hash=current_hash,
        target_exists=target_exists,
        needs_translation=needs_translation,
        issues=issues,
    )


def health_summary(source_lang: str, target_lang: str) -> dict[str, object]:
    pages = [inspect_page(path, source_lang, target_lang) for path in list_sources(source_lang)]
    return {
        "source_lang": source_lang,
        "target_lang": target_lang,
        "total": len(pages),
        "translated": sum(1 for page in pages if page.target_exists),
        "needs_translation": sum(1 for page in pages if page.needs_translation),
        "with_issues": sum(1 for page in pages if page.issues),
        "pages": [page.__dict__ for page in pages],
    }
