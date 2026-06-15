from __future__ import annotations

from .config import (
    LOCALIZED_METADATA_HASH_FIELD,
    METADATA_HASH_FIELD,
    TARGET_OWNED_METADATA_FIELDS,
    TRANSLATABLE_METADATA_FIELDS,
    TRANSLATION_FIELD_PREFIXES,
)
from .metadata import frontmatter_blocks, read_scalar, remove_block, set_block, set_scalar


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
    from .hashes import source_localized_metadata_hash

    source_metadata = source_metadata_for_translation(source_frontmatter)
    for key in TRANSLATABLE_METADATA_FIELDS:
        if key in source_metadata and not read_scalar(target_frontmatter, key):
            return True
    current_metadata_hash = source_localized_metadata_hash(source_frontmatter)
    stored_hash = read_scalar(target_frontmatter, LOCALIZED_METADATA_HASH_FIELD) or read_scalar(target_frontmatter, METADATA_HASH_FIELD)
    return stored_hash != current_metadata_hash
