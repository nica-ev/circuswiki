from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, urlunparse

import yaml

TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from translation.markdown import join_markdown, split_markdown


SOURCE_NAME = "Circus Gyms / Schools Around the World"
SOURCE_URL = (
    "https://datastudio.google.com/reporting/"
    "2ff68cae-8df4-46f2-b2e6-8ef6d0e328c1/page/Gj9BE"
)
TARGET_RELATIVE = Path("en/circusfinder/places/aerial-training-map")
SOURCE_TAG = "aerial-training-map"
SOURCE_ID_PREFIX = "aerial-map-"
SOCIAL_DOMAINS = {"facebook.com", "instagram.com", "linktr.ee", "wordpress.com"}

# The CSV has no stable record IDs and occasionally contains malformed map
# positions. Corrections are deliberately explicit instead of heuristic so a
# future dump cannot silently move an entry to an inferred location.
COORDINATE_CORRECTIONS = {
    "aradia fitness yeg edmonton": {
        "latitude": 53.49624,
        "longitude": -113.45434,
        "reason": "The source longitude -11345434 is missing its decimal point.",
    },
    "saskatoon pole dance studio": {
        "latitude": 52.1643,
        "longitude": -106.6644,
        "reason": "The source longitude has the wrong sign for Saskatoon, Canada.",
    },
}

URL_PATTERN = re.compile(
    r"(?i)(?:https?://[^\s]+|www\.[^\s]+|"
    r"(?<![@\w])(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,24}(?:/[^\s]*)?)"
)


@dataclass(frozen=True)
class SourceRecord:
    row_number: int
    raw_label: str
    name: str
    website: str
    raw_coordinates: str
    latitude: float | None
    longitude: float | None
    correction: str = ""


@dataclass(frozen=True)
class ExistingEntry:
    path: Path
    directory_id: str
    name: str
    normalized_name: str
    website: str
    domain: str
    latitude: float | None
    longitude: float | None
    owned: bool


def normalize_name(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.casefold()).strip()


def slugify(value: str) -> str:
    return normalize_name(value).replace(" ", "-") or "unnamed"


def normalize_website(value: str) -> str:
    website = value.strip().strip('"').rstrip(".,;:)")
    website = re.split(r"&(?:ved|usg)=", website, maxsplit=1, flags=re.IGNORECASE)[0]
    if not website:
        return ""
    if not website.lower().startswith(("http://", "https://")):
        website = "https://" + website
    parsed = urlparse(website)
    if not parsed.netloc:
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


def split_label(value: str) -> tuple[str, str]:
    label = value.strip().strip('"')
    if not label or label.casefold() == "null":
        return "", ""
    matches = list(URL_PATTERN.finditer(label))
    match = next(
        (
            candidate
            for candidate in matches
            if candidate.group(0).casefold().startswith(("http://", "https://"))
        ),
        matches[-1] if matches else None,
    )
    if not match:
        name = re.sub(r"\s+-\s+No direct website provided\s*$", "", label, flags=re.IGNORECASE)
        return name.strip(), ""
    website = normalize_website(match.group(0))
    name = re.sub(r"\s*[-–—:]\s*$", "", label[: match.start()]).strip()
    return name or label.strip(), website


def _parse_float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def parse_coordinates(raw: str, normalized_name: str) -> tuple[float | None, float | None, str]:
    correction = COORDINATE_CORRECTIONS.get(normalized_name)
    if correction:
        return float(correction["latitude"]), float(correction["longitude"]), str(correction["reason"])
    value = raw.strip()
    if not value or value.casefold() == "null":
        return None, None, ""
    parts = [part.strip() for part in value.split(",")]
    if len(parts) != 2:
        raise ValueError("coordinates must contain latitude and longitude")
    latitude = _parse_float(parts[0])
    longitude = _parse_float(parts[1])
    if latitude is None or longitude is None:
        raise ValueError("coordinates must be numeric")
    if not -90 <= latitude <= 90:
        raise ValueError("latitude must be between -90 and 90")
    if not -180 <= longitude <= 180:
        raise ValueError("longitude must be between -180 and 180")
    return latitude, longitude, ""


def load_source(csv_path: Path) -> tuple[list[SourceRecord], dict[str, Any]]:
    records: list[SourceRecord] = []
    status_counts: Counter[str] = Counter()
    skipped: list[dict[str, Any]] = []
    corrections: list[dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"Latitude_Longitude", "Status", "Location_Name_&_Website"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing))}")
        for row_number, row in enumerate(reader, start=2):
            status = (row.get("Status") or "").strip()
            status_counts[status or "(blank)"] += 1
            if status != "Open":
                continue
            raw_label = (row.get("Location_Name_&_Website") or "").strip()
            name, website = split_label(raw_label)
            if not name:
                skipped.append({"row": row_number, "reason": "open record has no name"})
                continue
            raw_coordinates = (row.get("Latitude_Longitude") or "").strip()
            normalized_name = normalize_name(name)
            try:
                latitude, longitude, correction = parse_coordinates(raw_coordinates, normalized_name)
            except ValueError as exc:
                skipped.append(
                    {
                        "row": row_number,
                        "name": name,
                        "coordinates": raw_coordinates,
                        "reason": str(exc),
                    }
                )
                continue
            if correction:
                corrections.append(
                    {
                        "row": row_number,
                        "name": name,
                        "source_coordinates": raw_coordinates,
                        "latitude": latitude,
                        "longitude": longitude,
                        "reason": correction,
                    }
                )
            records.append(
                SourceRecord(
                    row_number=row_number,
                    raw_label=raw_label,
                    name=name,
                    website=website,
                    raw_coordinates=raw_coordinates,
                    latitude=latitude,
                    longitude=longitude,
                    correction=correction,
                )
            )
    return records, {
        "source_rows": sum(status_counts.values()),
        "source_status_counts": dict(sorted(status_counts.items())),
        "open_named_records": len(records),
        "skipped_open_records": skipped,
        "coordinate_corrections": corrections,
    }


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


def _same_source_place(left: SourceRecord, right: SourceRecord) -> bool:
    left_name = normalize_name(left.name)
    right_name = normalize_name(right.name)
    left_branch = normalize_name(" ".join(re.findall(r"\(([^)]+)\)", left.name)))
    right_branch = normalize_name(" ".join(re.findall(r"\(([^)]+)\)", right.name)))
    if left_branch and right_branch and left_branch != right_branch:
        return False
    left_domain = website_domain(left.website)
    right_domain = website_domain(right.website)
    distance = distance_km(left.latitude, left.longitude, right.latitude, right.longitude)
    if left_name == right_name:
        if distance is None:
            return bool(left_domain and left_domain == right_domain)
        return distance <= 0.25
    same_domain = (
        bool(left_domain)
        and left_domain == right_domain
        and left_domain not in SOCIAL_DOMAINS
    )
    if same_domain and distance is not None and distance <= 0.25:
        return True
    similarity = difflib.SequenceMatcher(None, left_name, right_name).ratio()
    return distance is not None and distance <= 0.25 and similarity >= 0.9


def _record_quality(record: SourceRecord) -> tuple[int, int, int, int]:
    return (
        int(bool(record.website)),
        -record.name.count("("),
        -len(record.name),
        -record.row_number,
    )


def deduplicate_source(records: list[SourceRecord]) -> tuple[list[SourceRecord], list[dict[str, Any]]]:
    parent = list(range(len(records)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for left in range(len(records)):
        for right in range(left + 1, len(records)):
            if _same_source_place(records[left], records[right]):
                union(left, right)

    groups: dict[int, list[SourceRecord]] = {}
    for index, record in enumerate(records):
        groups.setdefault(find(index), []).append(record)

    selected: list[SourceRecord] = []
    duplicate_groups: list[dict[str, Any]] = []
    for group in groups.values():
        chosen = max(group, key=_record_quality)
        selected.append(chosen)
        if len(group) > 1:
            duplicate_groups.append(
                {
                    "selected": chosen.name,
                    "source_rows": [
                        {"row": record.row_number, "name": record.name, "coordinates": record.raw_coordinates}
                        for record in group
                    ],
                }
            )
    selected.sort(key=lambda record: record.row_number)
    duplicate_groups.sort(key=lambda item: item["source_rows"][0]["row"])
    return selected, duplicate_groups


def _number(value: Any) -> float | None:
    if value in (None, "") or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def load_existing_entries(docs_root: Path) -> list[ExistingEntry]:
    entries: list[ExistingEntry] = []
    target = (docs_root / TARGET_RELATIVE).resolve()
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
                name=name,
                normalized_name=normalize_name(name),
                website=website,
                domain=domain,
                latitude=_number(data.get("latitude")),
                longitude=_number(data.get("longitude")),
                owned=path.resolve().is_relative_to(target),
            )
        )
    return entries


def match_existing(record: SourceRecord, entries: list[ExistingEntry]) -> ExistingEntry | None:
    normalized = normalize_name(record.name)
    domain = website_domain(record.website)
    exact = [entry for entry in entries if entry.normalized_name == normalized]
    if exact:
        ranked = sorted(
            exact,
            key=lambda entry: (
                distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude) is None,
                distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude) or 0,
            ),
        )
        nearest = ranked[0]
        distance = distance_km(record.latitude, record.longitude, nearest.latitude, nearest.longitude)
        if distance is None or distance <= 10:
            return nearest

    domain_matches = [
        entry
        for entry in entries
        if domain
        and domain == entry.domain
        and domain not in SOCIAL_DOMAINS
    ]
    if len(domain_matches) == 1:
        domain_match = domain_matches[0]
        distance = distance_km(
            record.latitude,
            record.longitude,
            domain_match.latitude,
            domain_match.longitude,
        )
        if distance is None:
            return domain_match

    best: tuple[float, ExistingEntry] | None = None
    for entry in entries:
        distance = distance_km(record.latitude, record.longitude, entry.latitude, entry.longitude)
        same_domain = (
            bool(domain)
            and domain == entry.domain
            and domain not in SOCIAL_DOMAINS
        )
        similarity = difflib.SequenceMatcher(None, normalized, entry.normalized_name).ratio()
        score = 0.0
        if same_domain and distance is not None and distance <= 5:
            score = 2.0 - min(distance, 5) / 10
        elif distance is not None and distance <= 1 and similarity >= 0.9:
            score = similarity
        if score and (best is None or score > best[0]):
            best = (score, entry)
    return best[1] if best else None


def source_item(record: SourceRecord, imported_on: date) -> dict[str, str]:
    return {
        "name": SOURCE_NAME,
        "url": SOURCE_URL,
        "record_name": record.name,
        "retrieved": imported_on.isoformat(),
        "batch_id": f"aerial-training-map-{imported_on.isoformat()}",
    }


def _source_block(data: list[dict[str, Any]]) -> list[str]:
    dumped = yaml.safe_dump(
        {"source": data},
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    return dumped.splitlines()


def update_existing_source(path: Path, new_source: dict[str, str], apply: bool) -> bool:
    text = path.read_text(encoding="utf-8-sig")
    document = split_markdown(text)
    data = yaml.safe_load(document.frontmatter) or {}
    sources = list(data.get("source") or [])
    changed = False
    for index, current in enumerate(sources):
        if not isinstance(current, dict):
            continue
        if current.get("url") == SOURCE_URL or current.get("name") == SOURCE_NAME:
            if current != new_source:
                sources[index] = new_source
                changed = True
            break
    else:
        sources.append(new_source)
        changed = True
    if not changed or not apply:
        return changed

    lines = document.frontmatter.splitlines()
    start = next((index for index, line in enumerate(lines) if line == "source:"), None)
    replacement = _source_block(sources)
    if start is None:
        lines.extend(replacement)
    else:
        end = start + 1
        while end < len(lines) and (lines[end].startswith((" ", "-")) or not lines[end].strip()):
            end += 1
        lines[start:end] = replacement
    path.write_text(join_markdown("\n".join(lines), document.body), encoding="utf-8", newline="\n")
    return True


def _description(record: SourceRecord) -> str:
    return (
        f"{record.name} is listed as an open aerial or circus training location in the "
        f"crowdsourced {SOURCE_NAME} map."
    )


def _frontmatter(record: SourceRecord, slug: str, imported_on: date, created: str | None = None) -> dict[str, Any]:
    data: dict[str, Any] = {
        "lang": "en",
        "translation_id": f"circusfinder/places/aerial-training-map/{slug}",
        "created": created or imported_on.isoformat(),
        "update": imported_on.isoformat(),
        "publish": True,
        "tags": ["circusfinder", "aerial-arts", "training-space", SOURCE_TAG],
        "title": record.name,
        "description": _description(record),
        "translation_status": "original",
        "translation_source_lang": "en",
        "directory_id": f"{SOURCE_ID_PREFIX}{slug}",
        "entry_kinds": ["training_space"],
        "directory_status": "active",
        "location_precision": "approximate" if record.latitude is not None else "none",
        "organization": record.name,
        "last_verified": imported_on.isoformat(),
        "verification_status": "imported_public_map",
        "source": [source_item(record, imported_on)],
    }
    if record.latitude is not None and record.longitude is not None:
        data["latitude"] = record.latitude
        data["longitude"] = record.longitude
    if record.website:
        data["website"] = record.website
    return data


def render_markdown(record: SourceRecord, slug: str, imported_on: date, created: str | None = None) -> str:
    frontmatter = yaml.safe_dump(
        _frontmatter(record, slug, imported_on, created),
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    website = f"\n\nWebsite: [{record.website}]({record.website})" if record.website else ""
    location_note = (
        "The map position is treated as approximate because the coordinates come from a crowdsourced map."
        if record.latitude is not None
        else "The source marks this record as open but does not provide coordinates."
    )
    return (
        f"---\n{frontmatter}\n---\n\n"
        f"# {record.name}\n\n"
        f"{_description(record)}{website}\n\n"
        "## Source\n\n"
        f"Imported from the [{SOURCE_NAME}]({SOURCE_URL}) report on {imported_on.isoformat()}. "
        "Only source records marked as open are published in this batch. "
        f"{location_note}\n"
    )


def _existing_created(path: Path) -> str | None:
    document = split_markdown(path.read_text(encoding="utf-8-sig"))
    data = yaml.safe_load(document.frontmatter) or {}
    value = data.get("created")
    return str(value) if value not in (None, "") else None


def _stable_slug(record: SourceRecord, used: set[str]) -> str:
    base = slugify(record.name)
    if base not in used:
        used.add(base)
        return base
    fingerprint = f"{normalize_name(record.name)}|{record.latitude}|{record.longitude}|{website_domain(record.website)}"
    suffix = hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()[:8]
    candidate = f"{base}-{suffix}"
    counter = 2
    while candidate in used:
        candidate = f"{base}-{suffix}-{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def import_csv(
    csv_path: Path,
    docs_root: Path,
    *,
    apply: bool = False,
    prune: bool = False,
    imported_on: date | None = None,
) -> dict[str, Any]:
    imported_on = imported_on or date.today()
    source_records, report = load_source(csv_path)
    records, duplicate_groups = deduplicate_source(source_records)
    existing_entries = load_existing_entries(docs_root)
    owned_entries = [entry for entry in existing_entries if entry.owned]
    non_owned_entries = [entry for entry in existing_entries if not entry.owned]
    target = docs_root / TARGET_RELATIVE
    if apply:
        target.mkdir(parents=True, exist_ok=True)

    used_slugs = {entry.path.stem for entry in owned_entries}
    matched_owned: set[Path] = set()
    matched_existing: list[dict[str, str]] = []
    existing_source_updates: list[str] = []
    created: list[str] = []
    updated: list[str] = []

    for record in records:
        owned_match = match_existing(record, owned_entries)
        if owned_match:
            path = owned_match.path
            slug = path.stem
            matched_owned.add(path.resolve())
            content = render_markdown(record, slug, imported_on, _existing_created(path))
            if path.read_text(encoding="utf-8-sig") != content:
                updated.append(path.as_posix())
                if apply:
                    path.write_text(content, encoding="utf-8", newline="\n")
            continue

        existing_match = match_existing(record, non_owned_entries)
        if existing_match:
            new_source = source_item(record, imported_on)
            if update_existing_source(existing_match.path, new_source, apply):
                existing_source_updates.append(existing_match.path.as_posix())
            matched_existing.append(
                {
                    "source_record": record.name,
                    "directory_id": existing_match.directory_id,
                    "path": existing_match.path.as_posix(),
                }
            )
            continue

        slug = _stable_slug(record, used_slugs)
        path = target / f"{slug}.md"
        created.append(path.as_posix())
        if apply:
            path.write_text(render_markdown(record, slug, imported_on), encoding="utf-8", newline="\n")

    stale = [
        entry.path.as_posix()
        for entry in owned_entries
        if entry.path.resolve() not in matched_owned
    ]
    pruned: list[str] = []
    if apply and prune:
        expected_created = {Path(value).resolve() for value in created}
        for value in stale:
            path = Path(value)
            if path.resolve() in expected_created:
                continue
            path.unlink()
            pruned.append(path.as_posix())

    report.update(
        {
            "source_records_after_deduplication": len(records),
            "source_duplicate_groups": duplicate_groups,
            "matched_existing_records": matched_existing,
            "existing_source_updates": existing_source_updates,
            "records_created": created,
            "records_updated": updated,
            "stale_owned_records": stale,
            "records_pruned": pruned,
            "target": target.as_posix(),
            "apply": apply,
            "prune": prune,
            "import_date": imported_on.isoformat(),
        }
    )
    return report


def main() -> None:
    repository_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Import open locations from the Circus Gyms / Schools Around the World CSV export"
    )
    parser.add_argument("csv_path", type=Path, help="CSV exported from the public Looker Studio map")
    parser.add_argument("--docs-root", type=Path, default=repository_root / "docs")
    parser.add_argument("--apply", action="store_true", help="Write new records and update source provenance")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="With --apply, delete source-owned records absent from the current open snapshot",
    )
    args = parser.parse_args()
    if args.prune and not args.apply:
        parser.error("--prune requires --apply")
    sys.stdout.reconfigure(encoding="utf-8")
    result = import_csv(
        args.csv_path.resolve(),
        args.docs_root.resolve(),
        apply=args.apply,
        prune=args.prune,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
