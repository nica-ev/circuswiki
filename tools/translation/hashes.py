from __future__ import annotations

import hashlib
import json

from dynamic.blocks import parse_dynamic_blocks

from .body_segments import frontmatter_tags, static_body_segments
from .config import TRANSLATABLE_METADATA_FIELDS
from .metadata import read_scalar
from .metadata_policy import source_owned_metadata_blocks
from .models import VaultPage


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
