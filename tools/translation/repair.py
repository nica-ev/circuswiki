from __future__ import annotations

from pathlib import Path

from .config import BODY_HASH_FIELD, DOCS, LOCALIZED_METADATA_HASH_FIELD, ROOT, STRUCTURAL_METADATA_HASH_FIELD
from .discovery import discover_vault_pages, find_group_source_language, primary_page, read_vault_page, rel
from .markdown import join_markdown
from .metadata import read_scalar, set_scalar
from .models import VaultPage


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
