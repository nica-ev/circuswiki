from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from core.env import env_value

from . import link_repair
from .body_translation import translate_body
from .config import (
    BODY_HASH_FIELD,
    DEFAULT_MODEL,
    LEGACY_HASH_FIELD,
    LOCALIZED_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    ROOT,
    STRUCTURAL_METADATA_HASH_FIELD,
)
from .discovery import derive_translation_id, language_path, rel
from .hashes import (
    body_hash_matches,
    legacy_source_hash,
    source_localized_metadata_hash,
    source_structural_metadata_hash,
    translatable_body_hash,
)
from .markdown import join_markdown, split_markdown
from .metadata import ensure_scalars, read_scalar
from .metadata_policy import (
    apply_translated_metadata,
    merge_source_metadata,
    needs_localized_metadata_translation,
    source_metadata_for_translation,
    source_owned_metadata_differences,
)
from .metadata_translation import call_metadata_translation_model


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
        "wrote_file": not dry_run,
        "api_calls_performed": True,
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
        "wrote_file": not dry_run,
        "api_calls_performed": bool(translated_metadata),
        "source_metadata_hash": source_localized_metadata_hash(source_doc.frontmatter),
        "source_localized_metadata_hash": source_localized_metadata_hash(source_doc.frontmatter),
        "source_structural_metadata_hash": source_structural_metadata_hash(source_doc.frontmatter),
        "translated_metadata_fields": sorted(translated_metadata),
        "localized_metadata_translated": translate_localized_metadata,
        "source_owned_metadata_differences": source_owned_differences,
        "metadata_chars": sum(len(value) for value in source_metadata_for_translation(source_doc.frontmatter).values()),
    }


def default_model() -> str:
    return env_value("OPENROUTER_MODEL", default=DEFAULT_MODEL)
