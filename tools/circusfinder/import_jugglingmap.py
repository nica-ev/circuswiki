from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from circusfinder.importing import (  # noqa: E402
    ImportRecord,
    distance_km,
    import_records,
    load_source_config,
    normalize_name,
    normalize_website,
    website_domain,
)


API_ROOT = "https://jugglingmap.org/api/v1"
SOURCE_CONFIG = load_source_config("jugglingmap")
ALLOWED_KINDS = {"openTraining", "circusSchool", "shop"}
KIND_ORDER = {"openTraining": 0, "circusSchool": 1, "shop": 2}
KIND_ENTRY_KINDS = {
    "openTraining": ("training_space",),
    "circusSchool": ("circus_school", "organization"),
    "shop": ("shop", "organization"),
}
KIND_LABELS = {
    "openTraining": "juggling training or juggling club",
    "circusSchool": "circus school or juggling workshop",
    "shop": "juggling shop",
}
DAY_LABELS = {
    "mon": "Mon",
    "tue": "Tue",
    "wed": "Wed",
    "thu": "Thu",
    "fri": "Fri",
    "sat": "Sat",
    "sun": "Sun",
}
URL_PATTERN = re.compile(r"(?i)(?:https?://|www\.)[^\s<>()]+")
EMAIL_PATTERN = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"(?<!\w)(\+?[0-9][0-9() ./-]{6,}[0-9])(?!\w)")

# Reviewed decisions can map a JugglingMap record ID to an existing
# CircusFinder directory_id, "new", or "skip". Keeping these decisions next to
# the adapter makes future rescans repeatable and reviewable.
MATCH_OVERRIDES: dict[str, str] = {}

# Exact-name candidates were reviewed against their full source records. Two
# sparse duplicate pins are omitted in favour of the more complete entry. The
# other pairs are intentionally separate seasonal or weekday venues.
REVIEWED_SOURCE_SKIPS = {
    "01M3373PE3EM8V7E36C3Y2CMQ4:openTraining": "duplicate VolaTutto training pin",
    "01KYYC89AC4MHENJYF9EF2CYGX:openTraining": "duplicate generic Circus Amersfoort pin",
}
REVIEWED_DISTINCT_PAIRS = {
    frozenset({"01KZ6XDDYQ7BPADSAXKHJ33J5Q:openTraining", "01KZ6XZ8W5YH2AD1HM77072KVT:openTraining"}),
    frozenset({"01KZ8CQCV7S9F930Z5HD3NT499:openTraining", "01KZ8CZSP9TQ996F53PMVVBA9Z:openTraining"}),
    frozenset({"01M1YMHQZ6JZ0N9GZ68YWA4DPG:openTraining", "01M1YHFRP0RBZBBCT7BNXCHWMV:openTraining"}),
}


def _single_line(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


@dataclass(frozen=True)
class CategoryRecord:
    pin_id: str
    latitude: float
    longitude: float
    place_name: str
    category: dict[str, Any]

    @property
    def kind(self) -> str:
        return str(self.category.get("kind") or "")

    @property
    def name(self) -> str:
        return _single_line(self.category.get("name"))


def _json_request(url: str) -> Any:
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            request = Request(
                url,
                headers={"Accept": "application/json", "User-Agent": "CircusWiki/1.0 (public data import)"},
            )
            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # pragma: no cover - network failures vary
            last_error = exc
            if attempt < 2:
                time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def _full_pin(pin_id: str) -> dict[str, Any]:
    value = _json_request(f"{API_ROOT}/pins/{pin_id}")
    if not isinstance(value, dict):
        raise ValueError(f"pin {pin_id} did not return an object")
    return value


def _urls(*values: str) -> tuple[str, ...]:
    found: list[str] = []
    for value in values:
        for match in URL_PATTERN.findall(value or ""):
            normalized = normalize_website(match)
            if normalized and normalized not in found:
                found.append(normalized)
    return tuple(found)


def _emails(*values: str) -> tuple[str, ...]:
    found: list[str] = []
    for value in values:
        for email in EMAIL_PATTERN.findall(value or ""):
            cleaned = email.rstrip(".,;:")
            if cleaned not in found:
                found.append(cleaned)
    return tuple(found)


def _phone(value: str) -> str:
    for match in PHONE_PATTERN.findall(value or ""):
        digits = re.sub(r"\D", "", match)
        if 7 <= len(digits) <= 16:
            return re.sub(r"\s+", " ", match).strip()
    return ""


def _website(urls: tuple[str, ...]) -> str:
    non_social = [
        url
        for url in urls
        if website_domain(url)
        not in {"facebook.com", "instagram.com", "tiktok.com", "vk.com", "vk.ru", "youtube.com"}
    ]
    return (non_social or list(urls) or [""])[0]


def _time(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    hour = value.get("hour")
    minute = value.get("minute")
    if not isinstance(hour, int) or not isinstance(minute, int):
        return ""
    return f"{hour:02d}:{minute:02d}"


def _opening_hours(category: dict[str, Any]) -> tuple[str, ...]:
    result: list[str] = []
    for item in category.get("schedule") or []:
        if not isinstance(item, dict):
            continue
        day = DAY_LABELS.get(str(item.get("day") or ""), str(item.get("day") or "").title())
        start = _time(item.get("start"))
        end = _time(item.get("end"))
        if day and start and end:
            result.append(f"{day} {start}–{end}")
    return tuple(result)


def _summary(name: str, kinds: tuple[str, ...]) -> str:
    labels = [KIND_LABELS[kind] for kind in kinds]
    if len(labels) == 1:
        kind_text = labels[0]
    else:
        kind_text = ", ".join(labels[:-1]) + f" and {labels[-1]}"
    return f"{name} is listed on the community-maintained JugglingMap as a {kind_text}."


def _body(
    name: str,
    pin_id: str,
    place_name: str,
    categories: list[dict[str, Any]],
    imported_on: date,
) -> str:
    kinds = tuple(str(category["kind"]) for category in categories)
    parts = [f"# {name}", "", _summary(name, kinds)]
    if place_name:
        parts.extend(["", f"Location as provided by the source: {place_name}"])
    for category in categories:
        description = str(category.get("description") or "").strip()
        contacts = str(category.get("contacts") or "").strip()
        social = str(category.get("social") or "").strip()
        hours = _opening_hours(category)
        access = category.get("accessMode") or {}
        parts.extend(["", f"## {KIND_LABELS[str(category['kind'])].title()}"])
        if description:
            parts.extend(["", description])
        if hours:
            parts.extend(["", "Schedule supplied by the source: " + ", ".join(hours)])
        if isinstance(access, dict) and access.get("mode"):
            access_text = str(access["mode"])
            if access.get("text"):
                access_text += f": {access['text']}"
            parts.extend(["", f"Access: {access_text}"])
        if category.get("ageFrom") is not None or category.get("ageTo") is not None:
            low = category.get("ageFrom")
            high = category.get("ageTo")
            if low is not None and high is not None:
                parts.extend(["", f"Ages: {low}–{high}"])
        if contacts:
            parts.extend(["", "Contact as provided by the source:", "", contacts])
        if social:
            parts.extend(["", "Links or social accounts as provided by the source:", "", social])
    record_url = f"https://jugglingmap.org/pin/{pin_id}"
    parts.extend(
        [
            "",
            "## Source",
            "",
            f"Imported from [JugglingMap]({record_url}) on {imported_on.isoformat()}. "
            "The position is treated as approximate because the community map does not provide a "
            "structured location-precision field. Current details should be checked on JugglingMap before visiting.",
        ]
    )
    return "\n".join(parts)


def _merged_groups(categories: list[CategoryRecord]) -> list[list[CategoryRecord]]:
    by_pin: dict[str, list[CategoryRecord]] = defaultdict(list)
    for record in categories:
        by_pin[record.pin_id].append(record)
    groups: list[list[CategoryRecord]] = []
    for pin_records in by_pin.values():
        by_name: dict[str, list[CategoryRecord]] = defaultdict(list)
        for record in pin_records:
            by_name[normalize_name(record.name)].append(record)
        groups.extend(by_name.values())
    return groups


def _to_import_record(group: list[CategoryRecord], imported_on: date) -> ImportRecord:
    group = sorted(group, key=lambda item: KIND_ORDER[item.kind])
    primary = group[0]
    categories = [item.category for item in group]
    kinds = tuple(item.kind for item in group)
    entry_kinds = tuple(dict.fromkeys(kind for source_kind in kinds for kind in KIND_ENTRY_KINDS[source_kind]))
    contacts = "\n".join(str(item.get("contacts") or "") for item in categories)
    social = "\n".join(str(item.get("social") or "") for item in categories)
    urls = _urls(contacts, social)
    hours = tuple(dict.fromkeys(hour for item in categories for hour in _opening_hours(item)))
    access_notes: list[str] = []
    indoor_outdoor: list[str] = []
    age_from: list[int] = []
    age_to: list[int] = []
    for item in categories:
        access = item.get("accessMode") or {}
        if isinstance(access, dict) and access.get("mode"):
            value = _single_line(access["mode"])
            if access.get("text"):
                value += f": {_single_line(access['text'])}"
            access_notes.append(value)
        indoor_outdoor.extend(str(value) for value in item.get("indoorOutdoor") or [])
        if isinstance(item.get("ageFrom"), int):
            age_from.append(int(item["ageFrom"]))
        if isinstance(item.get("ageTo"), int):
            age_to.append(int(item["ageTo"]))
    record_id = f"{primary.pin_id}:{primary.kind}"
    extra: dict[str, Any] = {
        "source_content_language": "und",
        "jugglingmap_pin_id": primary.pin_id,
        "jugglingmap_categories": list(kinds),
    }
    if indoor_outdoor:
        extra["indoor_outdoor"] = list(dict.fromkeys(indoor_outdoor))
    if age_from:
        extra["minimum_age"] = min(age_from)
    if age_to:
        extra["maximum_age"] = max(age_to)
    return ImportRecord(
        record_id=record_id,
        name=primary.name,
        description=_summary(primary.name, kinds),
        body=_body(primary.name, primary.pin_id, primary.place_name, categories, imported_on),
        entry_kinds=entry_kinds,
        tags=tuple(
            dict.fromkeys(
                (
                    "juggling",
                    *(("shop",) if "shop" in kinds else ()),
                    *(("training-space",) if any(kind != "shop" for kind in kinds) else ()),
                )
            )
        ),
        latitude=primary.latitude,
        longitude=primary.longitude,
        location_precision="approximate",
        record_url=f"https://jugglingmap.org/pin/{primary.pin_id}",
        website=_website(urls),
        public_emails=_emails(contacts, social),
        public_phone=_phone(contacts),
        source_urls=urls,
        opening_hours=hours,
        schedule_note="; ".join(dict.fromkeys(access_notes)),
        address=primary.place_name,
        verification_status="imported_public_map",
        extra_frontmatter=extra,
    )


def load_source(imported_on: date) -> tuple[list[ImportRecord], dict[str, Any]]:
    summaries = _json_request(f"{API_ROOT}/pins")
    if not isinstance(summaries, list):
        raise ValueError("JugglingMap pin list is not an array")
    summary_ids = [str(item.get("id") or "") for item in summaries if isinstance(item, dict)]
    if not summary_ids or any(not value for value in summary_ids):
        raise ValueError("JugglingMap pin list contains missing IDs")

    pins: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(_full_pin, pin_id): pin_id for pin_id in summary_ids}
        for future in as_completed(futures):
            pin_id = futures[future]
            try:
                pins.append(future.result())
            except Exception as exc:  # pragma: no cover - network failures vary
                errors.append({"pin_id": pin_id, "error": str(exc)})
    if errors:
        raise ValueError(f"failed to fetch {len(errors)} JugglingMap pin details: {errors[:3]}")

    category_counts: Counter[str] = Counter()
    skipped: list[dict[str, str]] = []
    categories: list[CategoryRecord] = []
    for pin in pins:
        pin_id = str(pin.get("id") or "")
        latitude = pin.get("lat")
        longitude = pin.get("lng")
        if not isinstance(latitude, (int, float)) or not -90 <= float(latitude) <= 90:
            skipped.append({"record_id": pin_id, "reason": "invalid latitude"})
            continue
        if not isinstance(longitude, (int, float)) or not -180 <= float(longitude) <= 180:
            skipped.append({"record_id": pin_id, "reason": "invalid longitude"})
            continue
        for category in pin.get("categories") or []:
            if not isinstance(category, dict):
                continue
            kind = str(category.get("kind") or "")
            category_counts[kind or "(blank)"] += 1
            name = _single_line(category.get("name"))
            if kind not in ALLOWED_KINDS:
                skipped.append({"record_id": f"{pin_id}:{kind}", "reason": "unknown category"})
                continue
            if not name:
                skipped.append({"record_id": f"{pin_id}:{kind}", "reason": "missing name"})
                continue
            source_record_id = f"{pin_id}:{kind}"
            if source_record_id in REVIEWED_SOURCE_SKIPS:
                skipped.append({"record_id": source_record_id, "reason": REVIEWED_SOURCE_SKIPS[source_record_id]})
                continue
            categories.append(
                CategoryRecord(
                    pin_id=pin_id,
                    latitude=float(latitude),
                    longitude=float(longitude),
                    place_name=_single_line(pin.get("placeName")),
                    category=category,
                )
            )

    records = [_to_import_record(group, imported_on) for group in _merged_groups(categories)]
    repeated: dict[str, list[ImportRecord]] = defaultdict(list)
    for record in records:
        repeated[normalize_name(record.name)].append(record)
    duplicate_candidates: list[dict[str, Any]] = []
    for normalized, group in repeated.items():
        if not normalized or len(group) < 2:
            continue
        pairs = []
        for left_index, left in enumerate(group):
            for right in group[left_index + 1 :]:
                distance = distance_km(left.latitude, left.longitude, right.latitude, right.longitude)
                same_domain = bool(website_domain(left.website)) and website_domain(left.website) == website_domain(right.website)
                pair = frozenset({left.record_id, right.record_id})
                if ((distance is not None and distance <= 5) or same_domain) and pair not in REVIEWED_DISTINCT_PAIRS:
                    pairs.append(
                        {
                            "left": left.record_id,
                            "right": right.record_id,
                            "distance_km": round(distance, 3) if distance is not None else None,
                            "same_domain": same_domain,
                        }
                    )
        if pairs:
            duplicate_candidates.append({"normalized_name": normalized, "pairs": pairs})
    records.sort(key=lambda record: record.record_id)
    return records, {
        "source_pins": len(pins),
        "source_categories": sum(category_counts.values()),
        "source_category_counts": dict(sorted(category_counts.items())),
        "merged_same_name_categories": len(categories) - len(records),
        "skipped_source_records": skipped,
        "source_duplicate_candidates": duplicate_candidates,
    }


def import_map(
    docs_root: Path,
    *,
    apply: bool = False,
    prune: bool = False,
    imported_on: date | None = None,
) -> dict[str, Any]:
    imported_on = imported_on or date.today()
    records, source_report = load_source(imported_on)
    return import_records(
        records,
        docs_root,
        SOURCE_CONFIG,
        apply=apply,
        prune=prune,
        imported_on=imported_on,
        source_report=source_report,
        match_overrides=MATCH_OVERRIDES,
    )


def main() -> None:
    repository_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Import public JugglingMap locations into CircusFinder")
    parser.add_argument("--docs-root", type=Path, default=repository_root / "docs")
    parser.add_argument("--apply", action="store_true", help="Write reviewed additions and provenance updates")
    parser.add_argument("--prune", action="store_true", help="With --apply, remove stale source-owned records")
    args = parser.parse_args()
    if args.prune and not args.apply:
        parser.error("--prune requires --apply")
    sys.stdout.reconfigure(encoding="utf-8")
    result = import_map(args.docs_root.resolve(), apply=args.apply, prune=args.prune)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["apply_blocked"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
