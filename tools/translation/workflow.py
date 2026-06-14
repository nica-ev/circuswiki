from __future__ import annotations

import hashlib
import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from core.languages import (
    common_fallback_language,
    default_language,
    extra_docs_language_codes,
    language_codes,
    language_name as registry_language_name,
)
from dynamic.blocks import DynamicBlock, parse_dynamic_blocks
from dynamic.workflow import render_block
from .markdown import join_markdown, split_markdown
from .metadata import ensure_scalars, frontmatter_blocks, missing_scalars, read_scalar, remove_block, set_block, set_scalar
from . import link_repair


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DEFAULT_MODEL = "google/gemini-2.0-flash-001"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
TRANSLATION_METADATA_CONFIG = ROOT / "tools" / "config" / "translation_metadata.json"
LANGUAGES = language_codes()
DEFAULT_LANGUAGE = default_language()
COMMON_FALLBACK_LANGUAGE = common_fallback_language()
DEFAULT_CONTEXT_DESCRIPTION = (
    "CircusWiki pages about circus pedagogy, movement games, inclusive practice, "
    "organizational documentation, and related educational material."
)
LANGUAGE_NAMES = {language: registry_language_name(language) for language in LANGUAGES}
BATCH_TRANSLATION_EXCLUDED_RELATIVE_PATHS = {
    "sitemap.md",
}
MARKDOWN_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()(?P<target>[^)\s]+(?:\s+\"[^\"]*\")?)(\))")
WIKILINK_RE = re.compile(r"(!?\[\[)(?P<body>[^\]]+)(\]\])")
LOCAL_LINK_RE = re.compile(r"^(?![a-z][a-z0-9+.-]*:|#|/|mailto:)(?P<path>[^#?]+?\.md)(?P<suffix>[#?].*)?$", re.IGNORECASE)
BODY_HASH_FIELD = "translation_source_body_hash"
LOCALIZED_METADATA_HASH_FIELD = "translation_source_localized_metadata_hash"
STRUCTURAL_METADATA_HASH_FIELD = "translation_source_structural_metadata_hash"
METADATA_HASH_FIELD = "translation_source_metadata_hash"
LEGACY_HASH_FIELD = "translation_source_hash"
TRANSLATION_FIELD_PREFIXES = ("translation_",)


def language_name(language: str) -> str:
    return registry_language_name(language)


def load_translatable_metadata_fields() -> list[str]:
    if not TRANSLATION_METADATA_CONFIG.is_file():
        return ["title", "description"]

    data = json.loads(TRANSLATION_METADATA_CONFIG.read_text(encoding="utf-8"))
    fields = data.get("translatable_fields")
    if not isinstance(fields, list):
        raise ValueError("translation_metadata.json must contain a translatable_fields list")

    normalized: list[str] = []
    for field in fields:
        if not isinstance(field, str) or not field.strip():
            raise ValueError("translatable_fields entries must be non-empty strings")
        value = field.strip()
        if value not in normalized:
            normalized.append(value)
    return normalized


TRANSLATABLE_METADATA_FIELDS = tuple(load_translatable_metadata_fields())
TARGET_OWNED_METADATA_FIELDS = {
    "lang",
    *TRANSLATABLE_METADATA_FIELDS,
    BODY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    STRUCTURAL_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    LEGACY_HASH_FIELD,
    "translation_model",
    "translation_status",
    "translation_updated",
    "translation_metadata_model",
    "translation_metadata_status",
    "translation_metadata_updated",
}


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


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def language_path(path: str | Path, source_lang: str, target_lang: str) -> Path:
    source = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path)
    source_root = (DOCS / source_lang).resolve()
    target_root = (DOCS / target_lang).resolve()
    relative = source.resolve().relative_to(source_root)
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


def source_body_hash(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def translatable_body(frontmatter: str, body: str) -> str:
    blocks = parse_dynamic_blocks(body) if "dynamic" in frontmatter_tags(frontmatter) else []
    if not blocks:
        return body
    return json.dumps(static_body_segments(body, blocks), ensure_ascii=False, separators=(",", ":"))


def translatable_body_hash(frontmatter: str, body: str) -> str:
    return source_body_hash(translatable_body(frontmatter, body))


def legacy_source_hash(frontmatter: str, body: str) -> str:
    translation_id = read_scalar(frontmatter, "translation_id") or ""
    payload = f"translation_id={translation_id}\n\n{body}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_hash(frontmatter: str, body: str) -> str:
    return translatable_body_hash(frontmatter, body)


def source_localized_metadata_payload(frontmatter: str) -> dict[str, str]:
    return {
        key: read_scalar(frontmatter, key) or ""
        for key in TRANSLATABLE_METADATA_FIELDS
    }


def source_localized_metadata_hash(frontmatter: str) -> str:
    payload = json.dumps(
        source_localized_metadata_payload(frontmatter),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_structural_metadata_hash(frontmatter: str) -> str:
    payload = json.dumps(
        source_owned_metadata_blocks(frontmatter),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_metadata_hash(frontmatter: str) -> str:
    return source_localized_metadata_hash(frontmatter)


def stored_body_hash(page: VaultPage) -> str:
    return page.translation_source_body_hash or page.translation_source_hash


def stored_localized_metadata_hash(page: VaultPage) -> str:
    return page.translation_source_localized_metadata_hash or page.translation_source_metadata_hash


def body_hash_matches(stored_hash: str, current_hash: str, legacy_hash: str) -> bool:
    return bool(stored_hash) and stored_hash in {current_hash, legacy_hash}


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


def vault_health_matrix() -> dict[str, object]:
    languages, groups = discover_vault_pages()
    rows: list[dict[str, object]] = []
    totals = {"green": 0, "yellow": 0, "red": 0}

    for translation_id in sorted(groups):
        pages_by_language = groups[translation_id]
        source_lang = find_group_source_language(pages_by_language)
        source_pages = pages_by_language.get(source_lang) or []
        source_page = primary_page(source_pages) if source_pages else None
        source_hash_value = (
            translatable_body_hash(source_page.frontmatter, source_page.body)
            if source_page
            else ""
        )
        legacy_hash_value = (
            legacy_source_hash(source_page.frontmatter, source_page.body)
            if source_page
            else ""
        )
        localized_metadata_hash_value = source_localized_metadata_hash(source_page.frontmatter) if source_page else ""
        structural_metadata_hash_value = source_structural_metadata_hash(source_page.frontmatter) if source_page else ""

        title = (
            source_page.title
            if source_page
            else primary_page(next(iter(pages_by_language.values()))).title
        )
        relative_path = (
            source_page.relative_path
            if source_page
            else primary_page(next(iter(pages_by_language.values()))).relative_path
        )
        cells: dict[str, dict[str, object]] = {}

        for language in languages:
            pages = pages_by_language.get(language, [])
            issues: list[str] = []
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

            if language == source_lang:
                if page.translation_status != "original":
                    issues.append("source_status_not_original")
                if page.translation_source_lang and page.translation_source_lang != source_lang:
                    issues.append("source_lang_mismatch")
                if not page.translation_source_lang:
                    issues.append("source_missing_translation_source_lang")
            else:
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
                if page_body_hash and not body_hash_matches(page_body_hash, source_hash_value, legacy_hash_value):
                    issues.append("source_body_hash_mismatch")
                if not page.translation_source_body_hash and page.translation_source_hash:
                    issues.append("legacy_source_hash")
                page_localized_hash = stored_localized_metadata_hash(page)
                if page_localized_hash and page_localized_hash != localized_metadata_hash_value:
                    issues.append("source_localized_metadata_hash_mismatch")
                if not page.translation_source_localized_metadata_hash and page.translation_source_metadata_hash:
                    issues.append("legacy_metadata_hash")
                if not page_localized_hash:
                    issues.append(f"missing_{LOCALIZED_METADATA_HASH_FIELD}")
                if page.translation_source_structural_metadata_hash and page.translation_source_structural_metadata_hash != structural_metadata_hash_value:
                    issues.append("source_structural_metadata_hash_mismatch")
                if not page.translation_source_structural_metadata_hash:
                    issues.append(f"missing_{STRUCTURAL_METADATA_HASH_FIELD}")
                source_owned_differences = source_owned_metadata_differences(source_page.frontmatter, page.frontmatter) if source_page else []
                if source_owned_differences:
                    issues.append("source_owned_metadata_mismatch")
                if page.translation_status == "missing-translation":
                    issues.append("fallback_page")

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


def repair_vault_metadata(path: str | Path) -> dict[str, object]:
    target = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    target.relative_to(ROOT)
    if not target.is_file() or target.suffix.lower() != ".md":
        raise FileNotFoundError(f"Not a Markdown file: {path}")

    language = target.relative_to(DOCS).parts[0]
    page = read_vault_page(target, language)
    _languages, groups = discover_vault_pages()
    pages_by_language = groups.get(page.translation_id)
    if not pages_by_language:
        return {"path": rel(target), "changed": False, "changes": [], "remaining": ["group_not_found"]}

    source_lang = find_group_source_language(pages_by_language)
    source_pages = pages_by_language.get(source_lang) or []
    source_page = primary_page(source_pages) if source_pages else None
    changes: list[str] = []
    skipped: list[str] = []
    frontmatter = page.frontmatter

    def assign(key: str, value: str, reason: str) -> None:
        nonlocal frontmatter
        if read_scalar(frontmatter, key) != value:
            frontmatter = set_scalar(frontmatter, key, value)
            changes.append(reason)

    assign("lang", language, "set_lang_from_folder")
    assign("translation_id", page.translation_id, "set_translation_id")

    if language == source_lang:
        assign("translation_status", "original", "set_source_status_original")
        assign("translation_source_lang", source_lang, "set_source_language")
    else:
        assign("translation_source_lang", source_lang, "set_translation_source_language")
        if source_page:
            assign("translation_source", source_page.rel_path, "set_translation_source")
        if not read_scalar(frontmatter, "translation_status"):
            assign("translation_status", "needs-review", "set_missing_translation_status")

        # Do not fabricate quality-sensitive provenance. A missing or mismatched
        # source hash/model/timestamp should stay visible until translation is rerun
        # or manually reviewed.
        for key in (BODY_HASH_FIELD, LOCALIZED_METADATA_HASH_FIELD, STRUCTURAL_METADATA_HASH_FIELD, "translation_model", "translation_updated"):
            if not read_scalar(frontmatter, key):
                skipped.append(f"missing_{key}")

    if frontmatter != page.frontmatter:
        output = join_markdown(frontmatter, page.body)
        target.write_text(output, encoding="utf-8", newline="\n")

    updated = read_vault_page(target, language)
    remaining = deterministic_repair_remaining_issues(updated, source_lang, source_page)
    return {
        "path": rel(target),
        "changed": bool(changes),
        "changes": changes,
        "skipped": skipped,
        "remaining": remaining,
    }


def deterministic_repair_remaining_issues(
    page: VaultPage,
    source_lang: str,
    source_page: VaultPage | None,
) -> list[str]:
    issues: list[str] = []
    if read_scalar(page.frontmatter, "lang") != page.language:
        issues.append("lang_mismatch")
    if not read_scalar(page.frontmatter, "translation_id"):
        issues.append("missing_translation_id")

    if page.language == source_lang:
        if read_scalar(page.frontmatter, "translation_status") != "original":
            issues.append("source_status_not_original")
        if read_scalar(page.frontmatter, "translation_source_lang") != source_lang:
            issues.append("source_lang_mismatch")
        return issues

    if read_scalar(page.frontmatter, "translation_source_lang") != source_lang:
        issues.append("translation_source_lang_mismatch")
    if source_page and read_scalar(page.frontmatter, "translation_source") != source_page.rel_path:
        issues.append("translation_source_mismatch")
    for key in (BODY_HASH_FIELD, LOCALIZED_METADATA_HASH_FIELD, STRUCTURAL_METADATA_HASH_FIELD, "translation_model", "translation_updated"):
        if not read_scalar(page.frontmatter, key):
            issues.append(f"missing_{key}")
    return issues


def batch_translation_plan(
    target_lang: str,
    max_files: int,
    source_lang: str = "all",
    reason: str = "all",
    max_source_chars: int | None = None,
    path_filter: str = "",
) -> dict[str, object]:
    if max_files < 1:
        raise ValueError("max_files must be at least 1")
    if max_source_chars is not None and max_source_chars < 1:
        raise ValueError("max_source_chars must be at least 1")

    languages, groups = discover_vault_pages()
    target_langs = list(languages) if target_lang == "all" else [target_lang]
    unknown = [language for language in target_langs if language not in languages]
    if unknown:
        raise ValueError(f"Unknown target language: {', '.join(unknown)}")
    if not target_langs:
        raise ValueError(f"Unknown target language: {target_lang}")
    if source_lang != "all" and source_lang not in languages:
        raise ValueError(f"Unknown source language: {source_lang}")
    if reason not in batch_translation_candidate_reasons():
        raise ValueError(f"Unknown candidate reason: {reason}")

    candidates: list[dict[str, object]] = []
    skipped: list[dict[str, str]] = []
    normalized_path_filter = path_filter.strip().lower()

    for translation_id in sorted(groups):
        pages_by_language = groups[translation_id]
        group_source_lang = find_group_source_language(pages_by_language)
        if source_lang != "all" and group_source_lang != source_lang:
            skipped.append(
                {
                    "translation_id": translation_id,
                    "source_lang": group_source_lang,
                    "reason": "source_lang_filter",
                }
            )
            continue

        source_pages = pages_by_language.get(group_source_lang) or []
        if not source_pages:
            skipped.append({"translation_id": translation_id, "reason": "missing_source"})
            continue

        source_page = primary_page(source_pages)
        source_chars = len(translatable_body(source_page.frontmatter, source_page.body))
        if max_source_chars is not None and source_chars > max_source_chars:
            skipped.append(
                {
                    "translation_id": translation_id,
                    "source_lang": group_source_lang,
                    "reason": "max_source_chars_filter",
                }
            )
            continue
        if normalized_path_filter and not batch_path_filter_matches(source_page, normalized_path_filter):
            skipped.append(
                {
                    "translation_id": translation_id,
                    "source_lang": group_source_lang,
                    "reason": "path_filter",
                }
            )
            continue

        excluded_reason = batch_translation_exclusion_reason(source_page)
        if excluded_reason:
            skipped.append({"translation_id": translation_id, "reason": excluded_reason})
            continue

        for candidate_target_lang in target_langs:
            if group_source_lang == candidate_target_lang:
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "target_is_source",
                    }
                )
                continue

            target_pages = pages_by_language.get(candidate_target_lang) or []
            target_page = primary_page(target_pages) if target_pages else None
            candidate_reason = translation_candidate_reason(source_page, target_page, group_source_lang)
            if not candidate_reason:
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "not_translation_candidate",
                    }
                )
                continue
            if not metadata_reason_matches(reason, candidate_reason):
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "candidate_reason_filter",
                    }
                )
                continue

            candidates.append(
                {
                    "translation_id": translation_id,
                    "title": source_page.title,
                    "source_lang": group_source_lang,
                    "source_language": language_name(group_source_lang),
                    "target_lang": candidate_target_lang,
                    "target_language": language_name(candidate_target_lang),
                    "source_path": source_page.rel_path,
                    "target_path": rel(language_path(source_page.path, group_source_lang, candidate_target_lang)),
                    "source_chars": source_chars,
                    "reason": candidate_reason,
                }
            )

    limited = candidates[:max_files]
    target_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for item in candidates:
        target_language = str(item["target_lang"])
        source_language = str(item["source_lang"])
        target_counts[target_language] = target_counts.get(target_language, 0) + 1
        source_counts[source_language] = source_counts.get(source_language, 0) + 1

    return {
        "target_lang": target_lang,
        "target_language": "All target languages" if target_lang == "all" else language_name(target_lang),
        "target_langs": target_langs,
        "target_counts": target_counts,
        "source_counts": source_counts,
        "source_policy": "canonical_source_per_translation_group",
        "filters": {
            "source_lang": source_lang,
            "reason": reason,
            "max_source_chars": max_source_chars,
            "path_filter": path_filter,
        },
        "available_reasons": batch_translation_candidate_reasons(),
        "max_files": max_files,
        "total_candidates": len(candidates),
        "planned_count": len(limited),
        "total_source_chars": sum(int(item["source_chars"]) for item in limited),
        "candidates": limited,
        "skipped_count": len(skipped),
    }


def batch_translation_candidate_reasons() -> list[str]:
    return [
        "all",
        "missing_file",
        "fallback_page",
        "source_body_hash_mismatch",
        "missing_body_hash",
        "translation_source_lang_mismatch",
    ]


def metadata_batch_plan(
    target_lang: str,
    max_files: int,
    source_lang: str = "all",
    reason: str = "all",
    path_filter: str = "",
) -> dict[str, object]:
    if max_files < 1:
        raise ValueError("max_files must be at least 1")

    languages, groups = discover_vault_pages()
    target_langs = list(languages) if target_lang == "all" else [target_lang]
    unknown = [language for language in target_langs if language not in languages]
    if unknown:
        raise ValueError(f"Unknown target language: {', '.join(unknown)}")
    if source_lang != "all" and source_lang not in languages:
        raise ValueError(f"Unknown source language: {source_lang}")
    if reason not in metadata_batch_candidate_reasons():
        raise ValueError(f"Unknown candidate reason: {reason}")

    candidates: list[dict[str, object]] = []
    skipped: list[dict[str, str]] = []
    normalized_path_filter = path_filter.strip().lower()

    for translation_id in sorted(groups):
        pages_by_language = groups[translation_id]
        group_source_lang = find_group_source_language(pages_by_language)
        if source_lang != "all" and group_source_lang != source_lang:
            skipped.append({"translation_id": translation_id, "reason": "source_lang_filter"})
            continue

        source_pages = pages_by_language.get(group_source_lang) or []
        if not source_pages:
            skipped.append({"translation_id": translation_id, "reason": "missing_source"})
            continue
        source_page = primary_page(source_pages)
        if normalized_path_filter and not batch_path_filter_matches(source_page, normalized_path_filter):
            skipped.append({"translation_id": translation_id, "reason": "path_filter"})
            continue

        source_metadata = source_metadata_for_translation(source_page.frontmatter)
        source_metadata_chars = sum(len(value) for value in source_metadata.values())

        for candidate_target_lang in target_langs:
            if group_source_lang == candidate_target_lang:
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "target_is_source",
                    }
                )
                continue

            target_pages = pages_by_language.get(candidate_target_lang) or []
            target_page = primary_page(target_pages) if target_pages else None
            candidate_reason = metadata_candidate_reason(source_page, target_page)
            if not candidate_reason:
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "not_metadata_candidate",
                    }
                )
                continue
            if reason != "all" and candidate_reason != reason:
                skipped.append(
                    {
                        "translation_id": translation_id,
                        "target_lang": candidate_target_lang,
                        "reason": "candidate_reason_filter",
                    }
                )
                continue

            candidates.append(
                {
                    "translation_id": translation_id,
                    "title": source_page.title,
                    "source_lang": group_source_lang,
                    "source_language": language_name(group_source_lang),
                    "target_lang": candidate_target_lang,
                    "target_language": language_name(candidate_target_lang),
                    "source_path": source_page.rel_path,
                    "target_path": rel(language_path(source_page.path, group_source_lang, candidate_target_lang)),
                    "source_title": read_scalar(source_page.frontmatter, "title") or source_page.path.stem,
                    "target_title": read_scalar(target_page.frontmatter, "title") if target_page else "",
                    "source_has_description": bool(read_scalar(source_page.frontmatter, "description")),
                    "target_has_description": bool(read_scalar(target_page.frontmatter, "description")) if target_page else False,
                    "source_owned_metadata_differences": (
                        source_owned_metadata_differences(source_page.frontmatter, target_page.frontmatter)
                        if target_page
                        else []
                    ),
                    "metadata_chars": source_metadata_chars,
                    "reason": candidate_reason,
                }
            )

    limited = candidates[:max_files]
    target_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for item in candidates:
        target_language = str(item["target_lang"])
        source_language = str(item["source_lang"])
        target_counts[target_language] = target_counts.get(target_language, 0) + 1
        source_counts[source_language] = source_counts.get(source_language, 0) + 1

    return {
        "target_lang": target_lang,
        "target_language": "All target languages" if target_lang == "all" else language_name(target_lang),
        "target_langs": target_langs,
        "target_counts": target_counts,
        "source_counts": source_counts,
        "source_policy": "canonical_source_per_translation_group",
        "filters": {
            "source_lang": source_lang,
            "reason": reason,
            "path_filter": path_filter,
        },
        "available_reasons": metadata_batch_candidate_reasons(),
        "max_files": max_files,
        "total_candidates": len(candidates),
        "planned_count": len(limited),
        "total_metadata_chars": sum(int(item["metadata_chars"]) for item in limited),
        "candidates": limited,
        "skipped_count": len(skipped),
    }


def metadata_reason_matches(filter_reason: str, candidate_reason: str) -> bool:
    if filter_reason == "all" or filter_reason == candidate_reason:
        return True
    aliases = {
        "missing_metadata_hash": {"missing_localized_metadata_hash"},
        "metadata_hash_mismatch": {"localized_metadata_hash_mismatch"},
    }
    return candidate_reason in aliases.get(filter_reason, set())


def metadata_batch_candidate_reasons() -> list[str]:
    return [
        "all",
        "missing_localized_metadata_hash",
        "localized_metadata_hash_mismatch",
        "missing_translatable_metadata",
        "missing_structural_metadata_hash",
        "structural_metadata_hash_mismatch",
        "source_owned_metadata_mismatch",
        "missing_metadata_hash",
        "metadata_hash_mismatch",
        "missing_title",
        "missing_description",
    ]


def metadata_candidate_reason(
    source_page: VaultPage,
    target_page: VaultPage | None,
) -> str | None:
    if target_page is None:
        return None

    source_metadata = source_metadata_for_translation(source_page.frontmatter)
    for field in TRANSLATABLE_METADATA_FIELDS:
        if field in source_metadata and not read_scalar(target_page.frontmatter, field):
            if field == "title":
                return "missing_title"
            if field == "description":
                return "missing_description"
            return "missing_translatable_metadata"

    current_localized_hash = source_localized_metadata_hash(source_page.frontmatter)
    page_localized_hash = stored_localized_metadata_hash(target_page)
    if not page_localized_hash:
        return "missing_localized_metadata_hash"
    if page_localized_hash != current_localized_hash:
        return "localized_metadata_hash_mismatch"

    current_structural_hash = source_structural_metadata_hash(source_page.frontmatter)
    if not target_page.translation_source_structural_metadata_hash:
        return "missing_structural_metadata_hash"
    if target_page.translation_source_structural_metadata_hash != current_structural_hash:
        return "structural_metadata_hash_mismatch"
    if source_owned_metadata_differences(source_page.frontmatter, target_page.frontmatter):
        return "source_owned_metadata_mismatch"
    return None


def batch_path_filter_matches(source_page: VaultPage, path_filter: str) -> bool:
    haystack = " ".join(
        [
            source_page.rel_path,
            source_page.relative_path,
            source_page.translation_id,
            source_page.title,
        ]
    ).lower()
    return path_filter in haystack


def batch_translation_exclusion_reason(source_page: VaultPage) -> str | None:
    if source_page.relative_path in BATCH_TRANSLATION_EXCLUDED_RELATIVE_PATHS:
        return "excluded_generated_index_page"
    return None


def translation_candidate_reason(
    source_page: VaultPage,
    target_page: VaultPage | None,
    source_lang: str,
) -> str | None:
    if target_page is None:
        return "missing_file"

    if target_page.translation_status == "missing-translation":
        return "fallback_page"

    current_hash = translatable_body_hash(source_page.frontmatter, source_page.body)
    legacy_hash = legacy_source_hash(source_page.frontmatter, source_page.body)
    page_body_hash = stored_body_hash(target_page)
    if page_body_hash and not body_hash_matches(page_body_hash, current_hash, legacy_hash):
        return "source_body_hash_mismatch"

    if not page_body_hash:
        return "missing_body_hash"

    if target_page.translation_source_lang and target_page.translation_source_lang != source_lang:
        return "translation_source_lang_mismatch"

    return None


def translate_batch_item(
    source_path: str,
    source_lang: str,
    target_lang: str,
    model: str | None = None,
    prompt: str | None = None,
) -> dict[str, object]:
    return translate_page(
        source_path=source_path,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
        dry_run=False,
    )


def metadata_batch_item(
    source_path: str,
    source_lang: str,
    target_lang: str,
    model: str | None = None,
) -> dict[str, object]:
    return translate_metadata_page(
        source_path=source_path,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        dry_run=False,
    )


def inspect_page(
    source_path: str | Path,
    source_lang: str,
    target_lang: str,
) -> PageStatus:
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


def source_metadata_for_translation(frontmatter: str) -> dict[str, str]:
    return {
        key: value
        for key in TRANSLATABLE_METADATA_FIELDS
        if (value := read_scalar(frontmatter, key) or "")
    }


def is_target_owned_metadata_field(key: str) -> bool:
    return key in TARGET_OWNED_METADATA_FIELDS or key.startswith(TRANSLATION_FIELD_PREFIXES)


def source_owned_metadata_blocks(frontmatter: str) -> dict[str, str]:
    return {
        key: block
        for key, block in frontmatter_blocks(frontmatter).items()
        if not is_target_owned_metadata_field(key)
    }


def source_owned_metadata_differences(source_frontmatter: str, target_frontmatter: str) -> list[str]:
    source_blocks = source_owned_metadata_blocks(source_frontmatter)
    target_blocks = source_owned_metadata_blocks(target_frontmatter)
    return sorted(
        key
        for key in set(source_blocks) | set(target_blocks)
        if source_blocks.get(key, "").strip() != target_blocks.get(key, "").strip()
    )


def merge_source_metadata(target_frontmatter: str, source_frontmatter: str) -> str:
    updated = target_frontmatter
    source_blocks = source_owned_metadata_blocks(source_frontmatter)
    target_blocks = source_owned_metadata_blocks(target_frontmatter)

    for key in target_blocks:
        if key not in source_blocks:
            updated = remove_block(updated, key)

    for key, block in source_blocks.items():
        updated = set_block(updated, key, block)

    return updated


def apply_translated_metadata(frontmatter: str, values: dict[str, str]) -> str:
    updated = frontmatter
    for key in TRANSLATABLE_METADATA_FIELDS:
        if key in values:
            updated = set_scalar(updated, key, values[key])
    return updated


def needs_localized_metadata_translation(source_frontmatter: str, target_frontmatter: str) -> bool:
    source_metadata = source_metadata_for_translation(source_frontmatter)
    for key in TRANSLATABLE_METADATA_FIELDS:
        if key in source_metadata and not read_scalar(target_frontmatter, key):
            return True
    current_metadata_hash = source_localized_metadata_hash(source_frontmatter)
    stored_hash = read_scalar(target_frontmatter, LOCALIZED_METADATA_HASH_FIELD) or read_scalar(target_frontmatter, METADATA_HASH_FIELD)
    return stored_hash != current_metadata_hash


def frontmatter_tags(frontmatter: str) -> list[str]:
    tags: list[str] = []
    lines = frontmatter.splitlines()
    in_tags = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("tags:"):
            in_tags = True
            value = stripped.split(":", 1)[1].strip()
            if value.startswith("[") and value.endswith("]"):
                tags.extend(clean_tag(part) for part in value[1:-1].split(","))
            elif value and value != "[]":
                tags.append(clean_tag(value))
            continue
        if in_tags and line.startswith((" ", "\t")) and stripped.startswith("-"):
            tags.append(clean_tag(stripped[1:]))
            continue
        if in_tags and stripped and not line.startswith((" ", "\t")):
            in_tags = False
    return sorted({tag for tag in tags if tag})


def clean_tag(value: str) -> str:
    return value.strip().strip('"\'').lstrip("#")


def static_body_segments(body: str, blocks: list[DynamicBlock] | None = None) -> list[str]:
    blocks = parse_dynamic_blocks(body) if blocks is None else blocks
    if not blocks:
        return [body]

    segments: list[str] = []
    cursor = 0
    for block in blocks:
        segments.append(body[cursor:block.start])
        cursor = block.end
    segments.append(body[cursor:])
    return segments


def translate_markdown_segment(
    segment: str,
    source_lang: str,
    target_lang: str,
    model: str,
    prompt: str | None,
) -> tuple[str, link_repair.LinkRepairResult]:
    if not segment.strip():
        return segment, link_repair.LinkRepairResult(body=segment, changed=False, repair_count=0, diagnostics=[])

    translated = call_translation_model(
        body=segment,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
    )
    repair_result = link_repair.repair_link_targets(segment, translated)
    return repair_result.body, repair_result


def translate_body(
    source_body: str,
    target_path: Path,
    source_lang: str,
    target_lang: str,
    model: str,
    prompt: str | None,
) -> tuple[str, link_repair.LinkRepairResult, list[dict[str, object]]]:
    blocks = parse_dynamic_blocks(source_body)
    if not blocks:
        translated_body, link_result = translate_markdown_segment(
            source_body,
            source_lang=source_lang,
            target_lang=target_lang,
            model=model,
            prompt=prompt,
        )
        return translated_body, link_result, []

    pieces: list[str] = []
    cursor = 0
    repair_count = 0
    diagnostics: list[link_repair.LinkRepairDiagnostic] = []
    dynamic_results: list[dict[str, object]] = []

    for block in blocks:
        translated_segment, segment_result = translate_markdown_segment(
            source_body[cursor:block.start],
            source_lang=source_lang,
            target_lang=target_lang,
            model=model,
            prompt=prompt,
        )
        pieces.append(translated_segment)
        repair_count += segment_result.repair_count
        diagnostics.extend(segment_result.diagnostics)

        pieces.append(source_body[block.start:block.content_start])
        block_result = render_block(target_path, block)
        dynamic_results.append(block_result)
        if not block_result.get("ok"):
            errors = ", ".join(str(error) for error in block_result.get("errors", []))
            raise RuntimeError(f"Dynamic block {block.index} render failed for {target_path}: {errors}")
        pieces.append(str(block_result["markdown"]).strip("\n"))
        pieces.append("\n\n")
        pieces.append(source_body[block.content_end:block.end])
        cursor = block.end

    translated_tail, tail_result = translate_markdown_segment(
        source_body[cursor:],
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
    )
    pieces.append(translated_tail)
    repair_count += tail_result.repair_count
    diagnostics.extend(tail_result.diagnostics)

    translated_body = "".join(pieces)
    return (
        translated_body,
        link_repair.LinkRepairResult(
            body=translated_body,
            changed=repair_count > 0,
            repair_count=repair_count,
            diagnostics=diagnostics,
        ),
        dynamic_results,
    )


def target_starting_frontmatter(source_doc, target: Path) -> str:
    if target.exists():
        target_doc = split_markdown(target.read_text(encoding="utf-8"))
        if target_doc.has_frontmatter:
            return target_doc.frontmatter
    return source_doc.frontmatter


def build_target_frontmatter(
    source_doc,
    target: Path,
    source: Path,
    source_lang: str,
    target_lang: str,
    model: str,
    translated_metadata: dict[str, str],
    update_body_provenance: bool,
    update_metadata_provenance: bool,
) -> str:
    translation_id = read_scalar(source_doc.frontmatter, "translation_id") or derive_translation_id(source)
    current_body_hash = translatable_body_hash(source_doc.frontmatter, source_doc.body)
    current_localized_metadata_hash = source_localized_metadata_hash(source_doc.frontmatter)
    current_structural_metadata_hash = source_structural_metadata_hash(source_doc.frontmatter)
    frontmatter = target_starting_frontmatter(source_doc, target)
    frontmatter = merge_source_metadata(frontmatter, source_doc.frontmatter)
    frontmatter = apply_translated_metadata(frontmatter, translated_metadata)

    values = {
        "lang": target_lang,
        "translation_id": translation_id,
        "translation_source": rel(source),
        "translation_source_lang": source_lang,
        "translation_status": "machine-translated",
    }
    if update_body_provenance:
        values.update(
            {
                BODY_HASH_FIELD: current_body_hash,
                LEGACY_HASH_FIELD: current_body_hash,
                "translation_model": model,
                "translation_updated": datetime.now(UTC).isoformat(timespec="seconds"),
            }
        )
    elif not read_scalar(frontmatter, BODY_HASH_FIELD):
        existing_hash = read_scalar(frontmatter, LEGACY_HASH_FIELD) or ""
        if body_hash_matches(existing_hash, current_body_hash, legacy_source_hash(source_doc.frontmatter, source_doc.body)):
            values[BODY_HASH_FIELD] = current_body_hash
            values[LEGACY_HASH_FIELD] = current_body_hash
    if update_metadata_provenance:
        values.update(
            {
                LOCALIZED_METADATA_HASH_FIELD: current_localized_metadata_hash,
                METADATA_HASH_FIELD: current_localized_metadata_hash,
                "translation_metadata_model": model,
                "translation_metadata_status": "machine-translated",
                "translation_metadata_updated": datetime.now(UTC).isoformat(timespec="seconds"),
            }
        )
    else:
        existing_hash = read_scalar(frontmatter, METADATA_HASH_FIELD) or ""
        if not read_scalar(frontmatter, LOCALIZED_METADATA_HASH_FIELD) and existing_hash == current_localized_metadata_hash:
            values[LOCALIZED_METADATA_HASH_FIELD] = current_localized_metadata_hash
    values[STRUCTURAL_METADATA_HASH_FIELD] = current_structural_metadata_hash
    return ensure_scalars(frontmatter, values)


def translate_page(
    source_path: str | Path,
    source_lang: str,
    target_lang: str,
    model: str | None = None,
    prompt: str | None = None,
    dry_run: bool = False,
) -> dict[str, object]:
    model = model or default_model()
    source = (ROOT / source_path).resolve()
    target = language_path(source, source_lang, target_lang)
    source_doc = split_markdown(source.read_text(encoding="utf-8"))
    current_body_hash = translatable_body_hash(source_doc.frontmatter, source_doc.body)
    current_localized_metadata_hash = source_localized_metadata_hash(source_doc.frontmatter)
    current_structural_metadata_hash = source_structural_metadata_hash(source_doc.frontmatter)

    translated_body, link_result, dynamic_results = translate_body(
        source_body=source_doc.body,
        target_path=target,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
    )
    translated_metadata = call_metadata_translation_model(
        metadata=source_metadata_for_translation(source_doc.frontmatter),
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
    )

    target_frontmatter = build_target_frontmatter(
        source_doc=source_doc,
        target=target,
        source=source,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        translated_metadata=translated_metadata,
        update_body_provenance=True,
        update_metadata_provenance=True,
    )
    label_result = link_repair.LinkRepairResult(body=translated_body, changed=False, repair_count=0, diagnostics=[])

    output = join_markdown(target_frontmatter, translated_body)
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8", newline="\n")

    return {
        "source": rel(source),
        "target": rel(target),
        "model": model,
        "dry_run": dry_run,
        "source_body_hash": current_body_hash,
        "source_metadata_hash": current_localized_metadata_hash,
        "source_localized_metadata_hash": current_localized_metadata_hash,
        "source_structural_metadata_hash": current_structural_metadata_hash,
        "translated_chars": len(translated_body),
        "translated_metadata_fields": sorted(translated_metadata),
        "link_repairs": link_result.repair_count,
        "dynamic_label_repairs": label_result.repair_count,
        "dynamic_blocks": len(dynamic_results),
        "dynamic_block_results": dynamic_results,
        "link_diagnostics": [item.__dict__ for item in link_result.diagnostics],
        "dynamic_label_diagnostics": [item.__dict__ for item in label_result.diagnostics],
    }


def translate_metadata_page(
    source_path: str | Path,
    source_lang: str,
    target_lang: str,
    model: str | None = None,
    dry_run: bool = False,
) -> dict[str, object]:
    model = model or default_model()
    source = (ROOT / source_path).resolve()
    target = language_path(source, source_lang, target_lang)
    if not target.exists():
        raise FileNotFoundError(f"Target file does not exist for metadata-only translation: {rel(target)}")

    source_doc = split_markdown(source.read_text(encoding="utf-8"))
    target_doc = split_markdown(target.read_text(encoding="utf-8"))
    source_owned_differences = source_owned_metadata_differences(source_doc.frontmatter, target_doc.frontmatter)
    translate_localized_metadata = needs_localized_metadata_translation(source_doc.frontmatter, target_doc.frontmatter)
    translated_metadata = (
        call_metadata_translation_model(
            metadata=source_metadata_for_translation(source_doc.frontmatter),
            source_lang=source_lang,
            target_lang=target_lang,
            model=model,
        )
        if translate_localized_metadata
        else {}
    )
    target_frontmatter = build_target_frontmatter(
        source_doc=source_doc,
        target=target,
        source=source,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        translated_metadata=translated_metadata,
        update_body_provenance=False,
        update_metadata_provenance=translate_localized_metadata,
    )
    output = join_markdown(target_frontmatter, target_doc.body)
    if not dry_run:
        target.write_text(output, encoding="utf-8", newline="\n")

    return {
        "source": rel(source),
        "target": rel(target),
        "model": model,
        "dry_run": dry_run,
        "source_metadata_hash": source_localized_metadata_hash(source_doc.frontmatter),
        "source_localized_metadata_hash": source_localized_metadata_hash(source_doc.frontmatter),
        "source_structural_metadata_hash": source_structural_metadata_hash(source_doc.frontmatter),
        "translated_metadata_fields": sorted(translated_metadata),
        "localized_metadata_translated": translate_localized_metadata,
        "source_owned_metadata_differences": source_owned_differences,
        "metadata_chars": sum(len(value) for value in source_metadata_for_translation(source_doc.frontmatter).values()),
    }


def restore_internal_link_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_internal_link_targets(source_body, translated_body)


def restore_markdown_link_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_markdown_link_targets(source_body, translated_body)


def restore_wikilink_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_wikilink_targets(source_body, translated_body)


def is_local_markdown_target(target: str) -> bool:
    return link_repair.is_local_markdown_target(target)


def wikilink_target(body: str) -> str:
    return link_repair.wikilink_target(body)


def wikilink_alias(body: str) -> str:
    return link_repair.wikilink_alias(body)


def call_translation_model(
    body: str,
    source_lang: str,
    target_lang: str,
    model: str,
    prompt: str | None = None,
) -> str:
    load_local_env()
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY or OPENAI_API_KEY")

    base_url = os.getenv("OPENROUTER_BASE_URL") or os.getenv("OPENAI_BASE_URL") or DEFAULT_BASE_URL
    url = chat_completions_url(base_url)
    system_prompt = render_prompt(prompt, source_lang, target_lang)
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": body},
        ],
        "temperature": 0.2,
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/nica-ev/circuswiki",
            "X-Title": "CircusWiki Translation Console",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Translation API request failed with HTTP {exc.code} for {url}: {details}"
        ) from exc

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected translation response: {data}") from exc

    return strip_code_fences(content).strip() + "\n"


def call_metadata_translation_model(
    metadata: dict[str, str],
    source_lang: str,
    target_lang: str,
    model: str,
) -> dict[str, str]:
    if not metadata:
        return {}

    load_local_env()
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY or OPENAI_API_KEY")

    base_url = os.getenv("OPENROUTER_BASE_URL") or os.getenv("OPENAI_BASE_URL") or DEFAULT_BASE_URL
    url = chat_completions_url(base_url)
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": metadata_prompt(source_lang, target_lang)},
            {"role": "user", "content": json.dumps(metadata, ensure_ascii=False, indent=2)},
        ],
        "temperature": 0.2,
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/nica-ev/circuswiki",
            "X-Title": "CircusWiki Translation Console",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Translation API request failed with HTTP {exc.code} for {url}: {details}"
        ) from exc

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected translation response: {data}") from exc

    raw = strip_code_fences(content).strip()
    try:
        translated = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Metadata translation response was not valid JSON: {raw}") from exc

    if not isinstance(translated, dict):
        raise RuntimeError(f"Metadata translation response must be a JSON object: {translated}")

    return {
        key: str(translated[key]).strip()
        for key in TRANSLATABLE_METADATA_FIELDS
        if key in metadata and key in translated
    }


def metadata_prompt(source_lang: str, target_lang: str) -> str:
    source_language = language_name(source_lang)
    target_language = language_name(target_lang)
    fields = ", ".join(TRANSLATABLE_METADATA_FIELDS)
    return f"""You are translating CircusWiki Markdown frontmatter metadata from {source_language} to {target_language}.

Translate only natural-language field values for these fields: {fields}.
Preserve meaning, keep titles concise, and make descriptions natural for metadata/search previews.
Do not add, remove, or rename fields.
Return only a valid JSON object with the same keys as the input.
Do not wrap the JSON in Markdown fences."""


def chat_completions_url(base_url: str) -> str:
    normalized = base_url.rstrip("/")
    if normalized.endswith("/chat/completions"):
        return normalized
    return normalized + "/chat/completions"


def load_local_env() -> None:
    env_file = ROOT / ".env"
    if not env_file.exists():
        return

    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def default_model() -> str:
    load_local_env()
    return os.getenv("OPENROUTER_MODEL") or DEFAULT_MODEL


def default_prompt(source_lang: str, target_lang: str) -> str:
    return render_prompt(None, source_lang, target_lang)


def default_prompt_template() -> str:
    return """You are an expert {source_language}-to-{target_language} translator and localization specialist. Your mission is to translate {source_language} text into {target_language} that is not just grammatically correct, but also completely natural, idiomatic, and clear, as if it were originally written by a native {target_language} speaker for a {target_language} audience.

Guiding Principles:
1. **Clarity is paramount.** The reader must understand the text's meaning and intent without any confusion.
2. **Natural flow over literal accuracy.** You must restructure sentences and choose different words to make the text sound natural in {target_language}.
3. **Context is key.** You must understand the purpose of the text (e.g., game rules, marketing copy, technical description) and adapt your translation accordingly. The context for this text is: {context_description}

Strict Translation Rules:
1. **AVOID "SOURCE-ISMS":** You must actively identify and eliminate calques (word-for-word translations of {source_language} structures). Do not mirror {source_language} sentence structure, word order, or unique grammatical features. Rephrase the entire idea using natural {target_language} syntax.
2. **LOGICAL INFERENCE FOR INSTRUCTIONS:** When translating instructions, rules, or procedures, you must validate their logic. If a literal translation results in a nonsensical or illogical instruction in {target_language}, you are required to infer the true, logical intent and translate that intent instead.
3. **USE ACTIVE & IDIOMATIC VERBS:** Prefer natural {target_language} verbal constructions over awkward noun phrases common in literal translations. For example, a direct translation might produce a clunky noun phrase, but the goal is to find the fluid, verb-centric equivalent in {target_language}.
4. **ADAPT IDIOMS:** Never translate {source_language} idioms or colloquialisms literally. Find the closest functional equivalent in {target_language} or rephrase the meaning plainly if no direct equivalent exists.

Markdown and Structure Rules:
1. Return only translated Markdown body content.
2. Preserve Markdown structure, headings, tables, admonitions, comments, code blocks, links, image links, and Obsidian wikilinks.
3. Translate natural language text only.
4. Do not translate file names, URLs, anchors, image paths, YAML, HTML attributes, IDs, placeholders, or code.
5. Keep formatting intact.

Output Format Constraint:
Your response MUST contain ONLY the final, translated {target_language} text. Do not include any titles, headers, notes, explanations, or any other text before or after the translation. Your entire output is the translation itself."""


def render_prompt(prompt: str | None, source_lang: str, target_lang: str) -> str:
    template = prompt or default_prompt_template()
    source_language = language_name(source_lang)
    target_language = language_name(target_lang)
    replacements = {
        "{source_lang}": source_lang,
        "{target_lang}": target_lang,
        "{source_language}": source_language,
        "{target_language}": target_language,
        "{SOURCE_LANGUAGE}": source_language,
        "{TARGET_LANGUAGE}": target_language,
        "{{SOURCE_LANGUAGE}}": source_language,
        "{{TARGET_LANGUAGE}}": target_language,
        "{context_description}": DEFAULT_CONTEXT_DESCRIPTION,
        "{CONTEXT_DESCRIPTION}": DEFAULT_CONTEXT_DESCRIPTION,
        "{{CONTEXT_DESCRIPTION}}": DEFAULT_CONTEXT_DESCRIPTION,
    }
    rendered = template
    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, value)
    return rendered


def strip_code_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        return "\n".join(lines[1:-1])
    return text
