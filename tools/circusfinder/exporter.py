from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from core.languages import common_fallback_language, default_language, language_codes
from translation.markdown import split_markdown


ENTRY_GLOB = "circusfinder/places/**/*.md"
LOCATION_PRECISIONS = {"exact", "approximate", "city", "none"}


class DirectoryValidationError(ValueError):
    def __init__(self, issues: list[str]):
        self.issues = issues
        super().__init__("CircusFinder directory validation failed:\n- " + "\n- ".join(issues))


@dataclass(frozen=True)
class DirectoryEntry:
    path: Path
    relative_path: str
    language: str
    data: dict[str, Any]

    @property
    def directory_id(self) -> str:
        return str(self.data["directory_id"])

    @property
    def is_original(self) -> bool:
        return self.data.get("translation_status") == "original"


def _string(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value).strip()


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        return []
    return [_string(item) for item in value if _string(item)]


def _list_with_legacy_value(data: dict[str, Any], list_key: str, legacy_key: str) -> list[str]:
    values = _string_list(data.get(list_key))
    legacy_value = _string(data.get(legacy_key))
    if not values and legacy_value:
        values.append(legacy_value)
    return values


def _number(value: Any) -> float | None:
    if value in (None, ""):
        return None
    if isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _frontmatter(path: Path) -> dict[str, Any]:
    document = split_markdown(path.read_text(encoding="utf-8-sig"))
    if not document.has_frontmatter:
        raise DirectoryValidationError([f"{path.as_posix()}: missing YAML frontmatter"])
    try:
        loaded = yaml.safe_load(document.frontmatter) or {}
    except yaml.YAMLError as exc:
        raise DirectoryValidationError([f"{path.as_posix()}: invalid YAML ({exc})"]) from exc
    if not isinstance(loaded, dict):
        raise DirectoryValidationError([f"{path.as_posix()}: frontmatter must be a mapping"])
    return loaded


def _validate_entry(entry: DirectoryEntry, docs_root: Path) -> list[str]:
    data = entry.data
    label = entry.path.resolve().relative_to(docs_root.resolve()).as_posix()
    issues: list[str] = []

    for key in ("directory_id", "translation_id", "translation_status", "translation_source_lang", "title"):
        if not _string(data.get(key)):
            issues.append(f"{label}: missing {key}")

    if _string(data.get("lang")) != entry.language:
        issues.append(f"{label}: lang must match the '{entry.language}' folder")

    kinds = data.get("entry_kinds")
    if not isinstance(kinds, list) or not _string_list(kinds):
        issues.append(f"{label}: entry_kinds must be a non-empty list")

    for key in ("collective_statuses", "contact_people", "public_emails", "opening_hours", "source_urls"):
        value = data.get(key)
        if value is not None and (not isinstance(value, list) or not _string_list(value)):
            issues.append(f"{label}: {key} must be a non-empty list when provided")

    precision = _string(data.get("location_precision"))
    if precision not in LOCATION_PRECISIONS:
        allowed = ", ".join(sorted(LOCATION_PRECISIONS))
        issues.append(f"{label}: location_precision must be one of {allowed}")

    raw_latitude = data.get("latitude")
    raw_longitude = data.get("longitude")
    latitude = _number(raw_latitude)
    longitude = _number(raw_longitude)
    has_latitude = raw_latitude not in (None, "")
    has_longitude = raw_longitude not in (None, "")
    if has_latitude != has_longitude:
        issues.append(f"{label}: latitude and longitude must be provided together")
    if has_latitude and latitude is None:
        issues.append(f"{label}: latitude must be numeric")
    if has_longitude and longitude is None:
        issues.append(f"{label}: longitude must be numeric")
    if latitude is not None and not -90 <= latitude <= 90:
        issues.append(f"{label}: latitude must be between -90 and 90")
    if longitude is not None and not -180 <= longitude <= 180:
        issues.append(f"{label}: longitude must be between -180 and 180")
    if precision == "none" and (has_latitude or has_longitude):
        issues.append(f"{label}: location_precision 'none' cannot have coordinates")
    if precision in {"exact", "approximate", "city"} and not (has_latitude and has_longitude):
        issues.append(f"{label}: location_precision '{precision}' requires coordinates")

    cover_image = _string(data.get("cover_image"))
    if cover_image:
        normalized = cover_image.replace("\\", "/")
        if not normalized.startswith("docs/img/") or ".." in Path(normalized).parts:
            issues.append(f"{label}: cover_image must point inside docs/img/")
        elif not (docs_root.parent / normalized).is_file():
            issues.append(f"{label}: cover_image does not exist: {cover_image}")
        for key in ("cover_image_alt", "cover_image_credit", "cover_image_license"):
            if not _string(data.get(key)):
                issues.append(f"{label}: {key} is required when cover_image is set")

    return issues


def load_entries(docs_root: Path) -> list[DirectoryEntry]:
    entries: list[DirectoryEntry] = []
    issues: list[str] = []
    seen_language_ids: dict[tuple[str, str], Path] = {}

    for language in language_codes():
        language_root = docs_root / language
        for path in sorted(language_root.glob(ENTRY_GLOB)):
            try:
                data = _frontmatter(path)
            except DirectoryValidationError as exc:
                issues.extend(exc.issues)
                continue
            if data.get("publish") is False:
                continue
            relative_path = path.relative_to(language_root).as_posix()
            entry = DirectoryEntry(path=path, relative_path=relative_path, language=language, data=data)
            issues.extend(_validate_entry(entry, docs_root))

            directory_id = _string(data.get("directory_id"))
            if directory_id:
                key = (language, directory_id)
                if key in seen_language_ids:
                    first = seen_language_ids[key].relative_to(docs_root).as_posix()
                    second = path.relative_to(docs_root).as_posix()
                    issues.append(f"duplicate directory_id '{directory_id}' for {language}: {first}, {second}")
                seen_language_ids[key] = path
            entries.append(entry)

    grouped = _group_entries(entries)
    for directory_id, versions in grouped.items():
        originals = [entry for entry in versions if entry.is_original]
        if len(originals) != 1:
            issues.append(f"directory_id '{directory_id}' must have exactly one original; found {len(originals)}")
        translation_ids = {_string(entry.data.get("translation_id")) for entry in versions}
        if len(translation_ids) > 1:
            issues.append(f"directory_id '{directory_id}' uses multiple translation_id values")

    if issues:
        raise DirectoryValidationError(issues)
    return entries


def _group_entries(entries: list[DirectoryEntry]) -> dict[str, list[DirectoryEntry]]:
    groups: dict[str, list[DirectoryEntry]] = {}
    for entry in entries:
        groups.setdefault(entry.directory_id, []).append(entry)
    return groups


def _preferred_entry(versions: list[DirectoryEntry], language: str) -> DirectoryEntry:
    by_language = {entry.language: entry for entry in versions}
    if language in by_language:
        return by_language[language]
    fallback = common_fallback_language()
    if fallback in by_language:
        return by_language[fallback]
    originals = [entry for entry in versions if entry.is_original]
    return originals[0]


def _detail_url(relative_path: str) -> str:
    path = Path(relative_path)
    without_suffix = path.with_suffix("").as_posix()
    if without_suffix.endswith("/index"):
        without_suffix = without_suffix[:-6]
    return f"../{without_suffix.strip('/')}/"


def _record(
    localized_entry: DirectoryEntry,
    canonical_entry: DirectoryEntry,
    requested_language: str,
) -> dict[str, Any]:
    data = canonical_entry.data
    localized = localized_entry.data
    latitude = _number(data.get("latitude"))
    longitude = _number(data.get("longitude"))
    cover_image = _string(data.get("cover_image"))
    contact_people = _string_list(data.get("contact_people"))
    public_emails = _list_with_legacy_value(data, "public_emails", "public_email")
    image: dict[str, Any] | None = None
    if cover_image:
        image = {
            "url": "../img/" + cover_image.replace("\\", "/").removeprefix("docs/img/"),
            "alt": _string(localized.get("cover_image_alt")) or _string(data.get("cover_image_alt")),
            "credit": _string(data.get("cover_image_credit")),
            "license": _string(data.get("cover_image_license")),
            "source_url": _string(data.get("cover_image_source")),
        }

    return {
        "id": canonical_entry.directory_id,
        "title": _string(localized.get("title")),
        "description": _string(localized.get("description")),
        "organization": _string(data.get("organization")) or _string(localized.get("title")),
        "entry_kinds": _string_list(data.get("entry_kinds")),
        "collective_statuses": _string_list(data.get("collective_statuses")),
        "status": _string(data.get("directory_status")) or "active",
        "location": {
            "country_code": _string(data.get("country_code")),
            "region": _string(data.get("region")),
            "city": _string(data.get("city")),
            "address": _string(data.get("address")),
            "postal_code": _string(data.get("postal_code")),
            "latitude": latitude,
            "longitude": longitude,
            "precision": _string(data.get("location_precision")),
        },
        "contact": {
            "website": _string(data.get("website")),
            "phone": _string(data.get("public_phone")),
            "email": public_emails[0] if public_emails else "",
            "emails": public_emails,
            "people": contact_people,
        },
        "offers": _string_list(data.get("offers")),
        "opening_hours": _string_list(data.get("opening_hours")),
        "schedule_note": _string(data.get("schedule_note")),
        "schedule_url": _string(data.get("schedule_url")),
        "source_urls": _string_list(data.get("source_urls")),
        "last_verified": _string(data.get("last_verified")),
        "verification_status": _string(data.get("verification_status")),
        "detail_url": _detail_url(localized_entry.relative_path),
        "image": image,
        "is_demo": bool(data.get("demo")),
        "content_language": localized_entry.language,
        "translation_missing": localized_entry.language != requested_language,
    }


def write_datasets(entries: list[DirectoryEntry], build_root: Path) -> dict[str, int]:
    groups = _group_entries(entries)
    counts: dict[str, int] = {}
    for language in language_codes():
        records = []
        for versions in groups.values():
            canonical = next(entry for entry in versions if entry.is_original)
            localized = _preferred_entry(versions, language)
            records.append(_record(localized, canonical, language))
        records.sort(key=lambda item: (item["title"].casefold(), item["id"]))
        payload = {
            "schema_version": 1,
            "language": language,
            "default_language": default_language(),
            "record_count": len(records),
            "records": records,
        }
        target = build_root / language / "data" / "circusfinder.v1.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        counts[language] = len(records)
    return counts


def export_datasets(docs_root: Path, build_root: Path) -> dict[str, int]:
    return write_datasets(load_entries(docs_root), build_root)
