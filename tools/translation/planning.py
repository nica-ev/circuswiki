from __future__ import annotations

from .config import BATCH_TRANSLATION_EXCLUDED_RELATIVE_PATHS, TRANSLATABLE_METADATA_FIELDS, language_name
from .discovery import discover_vault_pages, find_group_source_language, language_path, primary_page, rel
from .hashes import (
    body_hash_matches,
    legacy_source_hash,
    source_localized_metadata_hash,
    source_structural_metadata_hash,
    stored_body_hash,
    stored_localized_metadata_hash,
    translatable_body,
    translatable_body_hash,
)
from .metadata import read_scalar
from .metadata_policy import source_metadata_for_translation, source_owned_metadata_differences
from .models import VaultPage


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
            skipped.append({"translation_id": translation_id, "source_lang": group_source_lang, "reason": "source_lang_filter"})
            continue

        source_pages = pages_by_language.get(group_source_lang) or []
        if not source_pages:
            skipped.append({"translation_id": translation_id, "reason": "missing_source"})
            continue

        source_page = primary_page(source_pages)
        source_chars = len(translatable_body(source_page.frontmatter, source_page.body))
        if max_source_chars is not None and source_chars > max_source_chars:
            skipped.append({"translation_id": translation_id, "source_lang": group_source_lang, "reason": "max_source_chars_filter"})
            continue
        if normalized_path_filter and not batch_path_filter_matches(source_page, normalized_path_filter):
            skipped.append({"translation_id": translation_id, "source_lang": group_source_lang, "reason": "path_filter"})
            continue

        excluded_reason = batch_translation_exclusion_reason(source_page)
        if excluded_reason:
            skipped.append({"translation_id": translation_id, "reason": excluded_reason})
            continue

        for candidate_target_lang in target_langs:
            if group_source_lang == candidate_target_lang:
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "target_is_source"})
                continue

            target_pages = pages_by_language.get(candidate_target_lang) or []
            target_page = primary_page(target_pages) if target_pages else None
            candidate_reason = translation_candidate_reason(source_page, target_page, group_source_lang)
            if not candidate_reason:
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "not_translation_candidate"})
                continue
            if not metadata_reason_matches(reason, candidate_reason):
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "candidate_reason_filter"})
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
        "filters": {"source_lang": source_lang, "reason": reason, "max_source_chars": max_source_chars, "path_filter": path_filter},
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
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "target_is_source"})
                continue

            target_pages = pages_by_language.get(candidate_target_lang) or []
            target_page = primary_page(target_pages) if target_pages else None
            candidate_reason = metadata_candidate_reason(source_page, target_page)
            if not candidate_reason:
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "not_metadata_candidate"})
                continue
            if reason != "all" and candidate_reason != reason:
                skipped.append({"translation_id": translation_id, "target_lang": candidate_target_lang, "reason": "candidate_reason_filter"})
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
                    "source_owned_metadata_differences": source_owned_metadata_differences(source_page.frontmatter, target_page.frontmatter) if target_page else [],
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
        "filters": {"source_lang": source_lang, "reason": reason, "path_filter": path_filter},
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


def metadata_candidate_reason(source_page: VaultPage, target_page: VaultPage | None) -> str | None:
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
    haystack = " ".join([source_page.rel_path, source_page.relative_path, source_page.translation_id, source_page.title]).lower()
    return path_filter in haystack


def batch_translation_exclusion_reason(source_page: VaultPage) -> str | None:
    if source_page.relative_path in BATCH_TRANSLATION_EXCLUDED_RELATIVE_PATHS:
        return "excluded_generated_index_page"
    return None


def translation_candidate_reason(source_page: VaultPage, target_page: VaultPage | None, source_lang: str) -> str | None:
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
