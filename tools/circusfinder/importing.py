from __future__ import annotations

import difflib
import hashlib
import json
import math
import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse, urlunparse

import yaml

from translation.markdown import split_markdown


SOURCE_REGISTRY = Path(__file__).resolve().parents[1] / "config" / "circusfinder_sources.json"
SOCIAL_DOMAINS = {
    "facebook.com",
    "instagram.com",
    "linktr.ee",
    "tiktok.com",
    "vk.com",
    "vk.ru",
    "x.com",
    "youtube.com",
}


@dataclass(frozen=True)
class SourceConfig:
    source_id: str
    name: str
    url: str
    dataset_url: str
    language: str
    target_relative: Path
    reuse_basis: str
    license: str = ""
    minimum_expected_records: int = 0


@dataclass(frozen=True)
class ImportRecord:
    record_id: str
    name: str
    description: str
    body: str
    entry_kinds: tuple[str, ...]
    tags: tuple[str, ...]
    latitude: float | None
    longitude: float | None
    location_precision: str
    record_url: str = ""
    organization: str = ""
    website: str = ""
    public_emails: tuple[str, ...] = ()
    public_phone: str = ""
    source_urls: tuple[str, ...] = ()
    offers: tuple[str, ...] = ()
    opening_hours: tuple[str, ...] = ()
    schedule_note: str = ""
    address: str = ""
    postal_code: str = ""
    city: str = ""
    region: str = ""
    country_code: str = ""
    verification_status: str = "imported_public_directory"
    extra_frontmatter: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ExistingEntry:
    path: Path
    directory_id: str
    translation_id: str
    name: str
    normalized_name: str
    website: str
    domain: str
    latitude: float | None
    longitude: float | None
    owned: bool
    sources: tuple[dict[str, str], ...]

    def source_record_id(self, source_name: str) -> str:
        for source in self.sources:
            if source.get("name") == source_name and source.get("record_id"):
                return source["record_id"]
        return ""


@dataclass(frozen=True)
class MatchResult:
    status: str
    entry: ExistingEntry | None = None
    candidates: tuple[ExistingEntry, ...] = ()
    reason: str = ""


def load_source_config(source_id: str) -> SourceConfig:
    payload = json.loads(SOURCE_REGISTRY.read_text(encoding="utf-8"))
    raw = payload.get("sources", {}).get(source_id)
    if not isinstance(raw, dict):
        raise KeyError(f"Unknown CircusFinder source: {source_id}")
    return SourceConfig(
        source_id=source_id,
        name=str(raw["name"]),
        url=str(raw["url"]),
        dataset_url=str(raw.get("dataset_url") or raw["url"]),
        language=str(raw["language"]),
        target_relative=Path(str(raw["target"])),
        reuse_basis=str(raw.get("reuse_basis") or ""),
        license=str(raw.get("license") or ""),
        minimum_expected_records=int(raw.get("minimum_expected_records") or 0),
    )


def normalize_name(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.casefold()).strip()


def slugify(value: str) -> str:
    return normalize_name(value).replace(" ", "-") or "unnamed"


def normalize_website(value: str) -> str:
    website = value.strip().strip('"').rstrip(".,;:)")
    if not website:
        return ""
    if not website.lower().startswith(("http://", "https://")):
        website = "https://" + website
    parsed = urlparse(website)
    if not parsed.netloc or "." not in parsed.netloc:
        return ""
    return urlunparse(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path or "",
            parsed.params,
            parsed.query,
            "",
        )
    )


def website_domain(value: str) -> str:
    if not value:
        return ""
    domain = urlparse(value).netloc.casefold().split(":", 1)[0]
    return domain[4:] if domain.startswith("www.") else domain


def distance_km(
    latitude_a: float | None,
    longitude_a: float | None,
    latitude_b: float | None,
    longitude_b: float | None,
) -> float | None:
    if None in {latitude_a, longitude_a, latitude_b, longitude_b}:
        return None
    radius = 6371.0088
    lat_a = math.radians(float(latitude_a))
    lat_b = math.radians(float(latitude_b))
    delta_lat = lat_b - lat_a
    delta_lon = math.radians(float(longitude_b) - float(longitude_a))
    value = math.sin(delta_lat / 2) ** 2 + math.cos(lat_a) * math.cos(lat_b) * math.sin(delta_lon / 2) ** 2
    return radius * 2 * math.atan2(math.sqrt(value), math.sqrt(1 - value))


def _number(value: Any) -> float | None:
    if value in (None, "") or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _source_dicts(value: Any) -> tuple[dict[str, str], ...]:
    if not isinstance(value, list):
        return ()
    return tuple(
        {str(key): str(item_value) for key, item_value in item.items() if item_value not in (None, "")}
        for item in value
        if isinstance(item, dict)
    )


def load_existing_entries(docs_root: Path, config: SourceConfig) -> list[ExistingEntry]:
    entries: list[ExistingEntry] = []
    target = (docs_root / config.target_relative).resolve()
    for path in docs_root.glob("*/circusfinder/places/**/*.md"):
        document = split_markdown(path.read_text(encoding="utf-8-sig"))
        if not document.has_frontmatter:
            continue
        data = yaml.safe_load(document.frontmatter) or {}
        if not isinstance(data, dict) or not data.get("publish", True):
            continue
        if str(data.get("translation_status") or "") != "original":
            continue
        name = str(data.get("organization") or data.get("title") or "").strip()
        directory_id = str(data.get("directory_id") or "").strip()
        translation_id = str(data.get("translation_id") or "").strip()
        if not name or not directory_id:
            continue
        website = normalize_website(str(data.get("website") or ""))
        domain = website_domain(website)
        if not domain:
            email_domains = {
                str(email).rsplit("@", 1)[1].casefold()
                for email in data.get("public_emails") or []
                if isinstance(email, str) and "@" in email
            }
            if len(email_domains) == 1:
                domain = email_domains.pop()
        entries.append(
            ExistingEntry(
                path=path,
                directory_id=directory_id,
                translation_id=translation_id,
                name=name,
                normalized_name=normalize_name(name),
                website=website,
                domain=domain,
                latitude=_number(data.get("latitude")),
                longitude=_number(data.get("longitude")),
                owned=path.resolve().is_relative_to(target),
                sources=_source_dicts(data.get("source")),
            )
        )
    return entries


def match_existing(record: ImportRecord, entries: Iterable[ExistingEntry], source_name: str) -> MatchResult:
    choices = list(entries)
    by_source_id = [entry for entry in choices if entry.source_record_id(source_name) == record.record_id]
    if len(by_source_id) == 1:
        return MatchResult("matched", by_source_id[0], reason="stable source record ID")
    if len(by_source_id) > 1:
        return MatchResult("ambiguous", candidates=tuple(by_source_id), reason="duplicate stable source record ID")

    normalized = normalize_name(record.name)
    domain = website_domain(record.website)
    exact = [entry for entry in choices if entry.normalized_name == normalized]
    compatible_exact = []
    for entry in exact:
        distance = distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude)
        same_domain = bool(domain) and domain == entry.domain and domain not in SOCIAL_DOMAINS
        if (distance is not None and distance <= 10) or same_domain:
            compatible_exact.append(entry)
    if len(compatible_exact) == 1:
        return MatchResult("matched", compatible_exact[0], reason="exact normalized name and compatible location")
    if len(compatible_exact) > 1:
        return MatchResult(
            "ambiguous",
            candidates=tuple(compatible_exact),
            reason="exact normalized name matches multiple compatible records",
        )

    domain_matches = [
        entry
        for entry in choices
        if domain and domain == entry.domain and domain not in SOCIAL_DOMAINS
    ]
    compatible_domains = []
    for entry in domain_matches:
        distance = distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude)
        if distance is None or distance <= 5:
            compatible_domains.append(entry)
    if len(compatible_domains) == 1:
        return MatchResult("matched", compatible_domains[0], reason="unique website domain and compatible location")
    if len(compatible_domains) > 1:
        return MatchResult(
            "ambiguous",
            candidates=tuple(compatible_domains),
            reason="website domain matches multiple compatible records",
        )

    fuzzy: list[ExistingEntry] = []
    for entry in choices:
        distance = distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude)
        similarity = difflib.SequenceMatcher(None, normalized, entry.normalized_name).ratio()
        if distance is not None and distance <= 1 and similarity >= 0.9:
            fuzzy.append(entry)
    if len(fuzzy) == 1:
        return MatchResult("matched", fuzzy[0], reason="similar name within one kilometre")
    if len(fuzzy) > 1:
        return MatchResult("ambiguous", candidates=tuple(fuzzy), reason="multiple similar nearby records")
    return MatchResult("unmatched")


def source_item(config: SourceConfig, record: ImportRecord, imported_on: date) -> dict[str, str]:
    item = {
        "name": config.name,
        "url": record.record_url or config.url,
        "dataset_url": config.dataset_url,
        "record_id": record.record_id,
        "record_name": record.name,
        "retrieved": imported_on.isoformat(),
        "batch_id": f"{config.source_id}-{imported_on.isoformat()}",
    }
    if config.reuse_basis:
        item["reuse_basis"] = config.reuse_basis
    if config.license:
        item["license"] = config.license
    return item


def _source_block(data: list[dict[str, Any]]) -> list[str]:
    dumped = yaml.safe_dump({"source": data}, allow_unicode=True, sort_keys=False, width=1000).strip()
    return dumped.splitlines()


def update_existing_source(path: Path, new_source: dict[str, str], apply: bool) -> bool:
    text = path.read_text(encoding="utf-8-sig")
    document = split_markdown(text)
    data = yaml.safe_load(document.frontmatter) or {}
    sources = list(data.get("source") or [])
    changed = False
    matched_index: int | None = None
    for index, current in enumerate(sources):
        if not isinstance(current, dict):
            continue
        same_source = current.get("name") == new_source["name"]
        same_record = current.get("record_id") == new_source["record_id"]
        legacy_same_name = not current.get("record_id") and current.get("record_name") == new_source["record_name"]
        if same_source and (same_record or legacy_same_name):
            matched_index = index
            if current != new_source:
                sources[index] = new_source
                changed = True
            break
    else:
        sources.append(new_source)
        changed = True

    lines = document.frontmatter.splitlines()
    start = next((index for index, line in enumerate(lines) if line == "source:"), None)
    needs_body_separator = not document.body.startswith("\n")
    if not changed and not needs_body_separator:
        return False
    if not apply:
        return True

    if start is None:
        lines.extend(_source_block(sources))
    else:
        end = start + 1
        while end < len(lines) and (lines[end].startswith("-") or lines[end].startswith(" ") or not lines[end].strip()):
            end += 1
        item_starts = [
            index
            for index in range(start + 1, end)
            if re.match(r"^\s*-\s+", lines[index])
        ]
        indent = re.match(r"^(\s*)", lines[item_starts[0]]).group(1) if item_starts else "  "
        rendered_item = [indent + line for line in yaml.safe_dump([new_source], allow_unicode=True, sort_keys=False, width=1000).strip().splitlines()]
        if matched_index is not None and matched_index < len(item_starts):
            item_start = item_starts[matched_index]
            item_end = item_starts[matched_index + 1] if matched_index + 1 < len(item_starts) else end
            lines[item_start:item_end] = rendered_item
        else:
            lines[end:end] = rendered_item
    body = document.body if document.body.startswith("\n") else "\n" + document.body
    path.write_text(f"---\n{'\n'.join(lines).rstrip()}\n---\n{body}", encoding="utf-8", newline="\n")
    return True


def _stable_slug(record: ImportRecord, used: set[str]) -> str:
    base = slugify(record.name)
    if base not in used:
        used.add(base)
        return base
    suffix = hashlib.sha1(record.record_id.encode("utf-8")).hexdigest()[:8]
    candidate = f"{base}-{suffix}"
    counter = 2
    while candidate in used:
        candidate = f"{base}-{suffix}-{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def _existing_identity(path: Path) -> tuple[str | None, str | None, str | None]:
    if not path.is_file():
        return None, None, None
    document = split_markdown(path.read_text(encoding="utf-8-sig"))
    data = yaml.safe_load(document.frontmatter) or {}
    return (
        str(data.get("created") or "") or None,
        str(data.get("directory_id") or "") or None,
        str(data.get("translation_id") or "") or None,
    )


def _merged_sources(
    existing_path: Path | None,
    config: SourceConfig,
    record: ImportRecord,
    imported_on: date,
) -> list[dict[str, Any]]:
    own_source: dict[str, Any] = source_item(config, record, imported_on)
    if existing_path is None or not existing_path.is_file():
        return [own_source]
    document = split_markdown(existing_path.read_text(encoding="utf-8-sig"))
    data = yaml.safe_load(document.frontmatter) or {}
    existing_sources = [item for item in data.get("source") or [] if isinstance(item, dict)]
    merged: list[dict[str, Any]] = []
    replaced = False
    for item in existing_sources:
        if item.get("name") == config.name and not replaced:
            merged.append(own_source)
            replaced = True
        else:
            merged.append(dict(item))
    if not replaced:
        merged.insert(0, own_source)
    return merged


def render_markdown(
    config: SourceConfig,
    record: ImportRecord,
    slug: str,
    imported_on: date,
    existing_path: Path | None = None,
) -> str:
    created, existing_directory_id, existing_translation_id = _existing_identity(existing_path or Path())
    imported = imported_on.isoformat()
    translation_id = existing_translation_id or f"circusfinder/places/{config.source_id}/{slug}"
    directory_id = existing_directory_id or f"{config.source_id}-{slug}"
    data: dict[str, Any] = {
        "lang": config.language,
        "translation_id": translation_id,
        "created": created or imported,
        "update": imported,
        "publish": True,
        "tags": list(dict.fromkeys(("circusfinder", *record.tags, config.source_id))),
        "title": record.name,
        "description": record.description,
        "translation_status": "original",
        "translation_source_lang": config.language,
        "directory_id": directory_id,
        "entry_kinds": list(record.entry_kinds),
        "directory_status": "active",
        "location_precision": record.location_precision,
        "organization": record.organization or record.name,
        "last_verified": imported,
        "verification_status": record.verification_status,
        "source": _merged_sources(existing_path, config, record, imported_on),
    }
    if record.latitude is not None and record.longitude is not None:
        data["latitude"] = record.latitude
        data["longitude"] = record.longitude
    optional: tuple[tuple[str, Any], ...] = (
        ("country_code", record.country_code),
        ("region", record.region),
        ("city", record.city),
        ("address", record.address),
        ("postal_code", record.postal_code),
        ("website", record.website),
        ("public_emails", list(record.public_emails)),
        ("public_phone", record.public_phone),
        ("source_urls", list(record.source_urls)),
        ("offers", list(record.offers)),
        ("opening_hours", list(record.opening_hours)),
        ("schedule_note", record.schedule_note),
    )
    for key, value in optional:
        if value:
            data[key] = value
    data.update(record.extra_frontmatter)
    frontmatter = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000).strip()
    body = "\n".join(line.rstrip() for line in record.body.strip().splitlines())
    return f"---\n{frontmatter}\n---\n\n{body}\n"


def import_records(
    records: list[ImportRecord],
    docs_root: Path,
    config: SourceConfig,
    *,
    apply: bool = False,
    prune: bool = False,
    imported_on: date | None = None,
    source_report: dict[str, Any] | None = None,
    match_overrides: dict[str, str] | None = None,
) -> dict[str, Any]:
    imported_on = imported_on or date.today()
    match_overrides = match_overrides or {}
    if prune and not apply:
        raise ValueError("prune requires apply")
    record_ids = [record.record_id for record in records]
    duplicate_ids = sorted({record_id for record_id in record_ids if record_ids.count(record_id) > 1})
    if duplicate_ids:
        raise ValueError(f"duplicate source record IDs: {', '.join(duplicate_ids)}")
    if len(records) < config.minimum_expected_records:
        raise ValueError(
            f"{config.name} returned {len(records)} records; expected at least {config.minimum_expected_records}"
        )

    entries = load_existing_entries(docs_root, config)
    owned_entries = [entry for entry in entries if entry.owned]
    non_owned_entries = [entry for entry in entries if not entry.owned]
    entries_by_directory_id = {entry.directory_id: entry for entry in entries}
    target = docs_root / config.target_relative
    used_slugs = {entry.path.stem for entry in owned_entries}

    planned: list[tuple[str, ImportRecord, ExistingEntry | None, str]] = []
    ambiguous: list[dict[str, Any]] = []
    matched_existing: list[dict[str, str]] = []
    skipped_by_override: list[str] = []
    matched_owned: set[Path] = set()

    for record in records:
        override = match_overrides.get(record.record_id, "")
        if override == "skip":
            skipped_by_override.append(record.record_id)
            continue
        if override and override != "new":
            entry = entries_by_directory_id.get(override)
            if entry is None:
                raise ValueError(f"match override for {record.record_id} names unknown directory_id {override}")
            action = "update_owned" if entry.owned else "match_existing"
            planned.append((action, record, entry, "reviewed override"))
            if entry.owned:
                matched_owned.add(entry.path.resolve())
            continue

        owned_match = match_existing(record, owned_entries, config.name)
        if owned_match.status == "matched" and owned_match.entry:
            planned.append(("update_owned", record, owned_match.entry, owned_match.reason))
            matched_owned.add(owned_match.entry.path.resolve())
            continue
        if owned_match.status == "ambiguous":
            ambiguous.append(
                {
                    "source_record_id": record.record_id,
                    "source_record": record.name,
                    "reason": owned_match.reason,
                    "candidates": [entry.directory_id for entry in owned_match.candidates],
                }
            )
            continue

        if override == "new":
            planned.append(("create", record, None, "reviewed new-record override"))
            continue

        existing_match = match_existing(record, non_owned_entries, config.name)
        if existing_match.status == "matched" and existing_match.entry:
            planned.append(("match_existing", record, existing_match.entry, existing_match.reason))
            continue
        if existing_match.status == "ambiguous":
            ambiguous.append(
                {
                    "source_record_id": record.record_id,
                    "source_record": record.name,
                    "reason": existing_match.reason,
                    "candidates": [entry.directory_id for entry in existing_match.candidates],
                }
            )
            continue
        planned.append(("create", record, None, "no existing match"))

    created: list[str] = []
    updated: list[str] = []
    existing_source_updates: list[str] = []
    write_allowed = apply and not ambiguous

    for action, record, entry, reason in planned:
        if action == "match_existing" and entry:
            new_source = source_item(config, record, imported_on)
            if update_existing_source(entry.path, new_source, write_allowed):
                existing_source_updates.append(entry.path.as_posix())
            matched_existing.append(
                {
                    "source_record_id": record.record_id,
                    "source_record": record.name,
                    "directory_id": entry.directory_id,
                    "path": entry.path.as_posix(),
                    "reason": reason,
                }
            )
            continue
        if action == "update_owned" and entry:
            path = entry.path
            content = render_markdown(config, record, path.stem, imported_on, path)
            if path.read_text(encoding="utf-8-sig") != content:
                updated.append(path.as_posix())
                if write_allowed:
                    path.write_text(content, encoding="utf-8", newline="\n")
            continue
        slug = _stable_slug(record, used_slugs)
        path = target / f"{slug}.md"
        created.append(path.as_posix())
        if write_allowed:
            target.mkdir(parents=True, exist_ok=True)
            path.write_text(render_markdown(config, record, slug, imported_on), encoding="utf-8", newline="\n")

    stale = [entry.path.as_posix() for entry in owned_entries if entry.path.resolve() not in matched_owned]
    pruned: list[str] = []
    if write_allowed and prune:
        for value in stale:
            path = Path(value)
            path.unlink()
            pruned.append(path.as_posix())

    report: dict[str, Any] = dict(source_report or {})
    report.update(
        {
            "source": config.name,
            "source_records_after_filtering": len(records),
            "matched_existing_records": matched_existing,
            "ambiguous_matches": ambiguous,
            "skipped_by_override": skipped_by_override,
            "existing_source_updates": existing_source_updates,
            "records_created": created,
            "records_updated": updated,
            "stale_owned_records": stale,
            "records_pruned": pruned,
            "target": target.as_posix(),
            "apply": apply,
            "apply_blocked": bool(apply and ambiguous),
            "prune": prune,
            "import_date": imported_on.isoformat(),
        }
    )
    return report
