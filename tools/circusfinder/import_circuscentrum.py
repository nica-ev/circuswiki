from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from circusfinder.importing import (  # noqa: E402
    ImportRecord,
    import_records,
    load_source_config,
    normalize_name,
    normalize_website,
)


SOURCE_CONFIG = load_source_config("circuscentrum")
SOURCE_URL = "https://circuscentrum.be/nl/landschap"
KNOWN_CATEGORIES = {"Atelier", "Festival", "Spreidingsbureau", "Werkplaats"}
EMAIL_PATTERN = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"(?<!\w)(\+?[0-9][0-9() ./-]{6,}[0-9])(?!\w)")
POSTAL_PATTERN = re.compile(r"\b([1-9][0-9]{3,4})\b")

# Circuscentrum mixes undifferentiated organizations and dated event listings
# in records without a category. These IDs were reviewed against the live
# directory on 2026-10-11. Unknown uncategorized records remain excluded until
# they receive an explicit decision here.
UNCATEGORIZED_ORGANIZATIONS: dict[str, tuple[str, ...]] = {
    "89": ("network", "organization"),  # Circuscentrum
    "170": ("circus_school", "organization"),  # ESAC
    "171": ("circus_school", "organization"),  # Codarts Circus Arts
    "172": ("circus_school", "organization"),  # Fontys ACAPA
    "173": ("circus_school", "organization"),  # CNAC
    "174": ("circus_school", "organization"),  # Ecole nationale de cirque de Chatellerault
    "175": ("circus_school", "organization"),  # Le Lido
    "582": ("organization",),  # Upswing
    "1180": ("organization",),  # Huis van Alijn
    "1181": ("organization",),  # House of Mysteries
    "1219": ("circus_school", "organization"),  # Ecole de Cirque de Bruxelles
}

# Reviewed cross-source decisions can map a Circuscentrum node ID to an
# existing CircusFinder directory_id, "new", or "skip".
MATCH_OVERRIDES: dict[str, str] = {}


@dataclass
class SourceNode:
    node_id: str
    title: str = ""
    category: str = ""
    description_parts: list[str] = field(default_factory=list)
    website: str = ""
    emails: list[str] = field(default_factory=list)

    @property
    def description(self) -> str:
        lines = []
        for raw_line in "".join(self.description_parts).splitlines():
            line = re.sub(r"\s+", " ", html.unescape(raw_line)).strip()
            if line and line not in lines:
                lines.append(line)
        return "\n".join(lines)


class LandscapeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.nodes: list[SourceNode] = []
        self.current: SourceNode | None = None
        self.node_div_depth = 0
        self.active_field = ""
        self.field_div_depth = 0
        self.settings_parts: list[str] = []
        self.in_settings = False

    @staticmethod
    def _attributes(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key: value or "" for key, value in attrs}

    @staticmethod
    def _field(classes: set[str]) -> str:
        if "field-name-node-title" in classes:
            return "title"
        if "field-name-field-organisation-category" in classes:
            return "category"
        if "field-name-field-short-description" in classes:
            return "description"
        if "field--name-organisation-link" in classes:
            return "website"
        return ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = self._attributes(attrs)
        classes = set(attributes.get("class", "").split())
        if tag == "script" and attributes.get("data-drupal-selector") == "drupal-settings-json":
            self.in_settings = True

        if self.current is None:
            if tag == "div" and {"node--type-organisation", "node--view-mode-teaser"}.issubset(classes):
                node_id = attributes.get("id", "").strip()
                if node_id:
                    self.current = SourceNode(node_id=node_id)
                    self.node_div_depth = 1
            return

        if tag == "div":
            self.node_div_depth += 1
            field_name = self._field(classes)
            if field_name and not self.active_field:
                self.active_field = field_name
                self.field_div_depth = self.node_div_depth

        if tag == "a":
            href = html.unescape(attributes.get("href", "")).strip()
            if self.active_field == "website" and href:
                self.current.website = normalize_website(href)
            if href.casefold().startswith("mailto:"):
                email = href[7:].split("?", 1)[0].strip()
                if email and email not in self.current.emails:
                    self.current.emails.append(email)
        if tag == "br" and self.active_field == "description":
            self.current.description_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.in_settings:
            self.settings_parts.append(data)
        if self.current is None or not data:
            return
        if self.active_field == "title":
            self.current.title += data
        elif self.active_field == "category":
            self.current.category += data
        elif self.active_field == "description":
            self.current.description_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.in_settings:
            self.in_settings = False
        if self.current is None:
            return
        if tag in {"p", "li"} and self.active_field == "description":
            self.current.description_parts.append("\n")
        if tag != "div":
            return
        if self.field_div_depth == self.node_div_depth:
            self.active_field = ""
            self.field_div_depth = 0
        if self.node_div_depth == 1:
            self.current.title = re.sub(r"\s+", " ", self.current.title).strip()
            self.current.category = re.sub(r"\s+", " ", self.current.category).strip()
            self.nodes.append(self.current)
            self.current = None
            self.node_div_depth = 0
            return
        self.node_div_depth -= 1


def _request_page(page_number: int) -> str:
    query = "" if page_number == 0 else "?" + urlencode({"page": page_number})
    url = SOURCE_URL + query
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            request = Request(
                url,
                headers={"Accept": "text/html", "User-Agent": "CircusWiki/1.0 (public data import)"},
            )
            with urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except Exception as exc:  # pragma: no cover - network failures vary
            last_error = exc
            if attempt < 2:
                time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def _coordinates(settings_documents: list[str]) -> dict[str, tuple[float, float]]:
    result: dict[str, tuple[float, float]] = {}
    for document in settings_documents:
        if not document.strip():
            continue
        settings = json.loads(document)
        maps = settings.get("geofield_google_map") or {}
        if not isinstance(maps, dict):
            continue
        for value in maps.values():
            if not isinstance(value, dict):
                continue
            features = (value.get("data") or {}).get("features") or []
            for feature in features:
                if not isinstance(feature, dict):
                    continue
                properties = feature.get("properties") or {}
                coordinates = (feature.get("geometry") or {}).get("coordinates") or []
                node_id = str(properties.get("entity_id") or "").strip()
                if len(coordinates) != 2 or not node_id:
                    continue
                longitude, latitude = coordinates
                if isinstance(latitude, (int, float)) and isinstance(longitude, (int, float)):
                    if -90 <= float(latitude) <= 90 and -180 <= float(longitude) <= 180:
                        result[node_id] = (float(latitude), float(longitude))
    return result


def _phone(value: str) -> str:
    normalized = re.sub(r"\+\s+(?=\d)", "+", value)
    for candidate in PHONE_PATTERN.findall(normalized):
        digits = re.sub(r"\D", "", candidate)
        if 7 <= len(digits) <= 16:
            return re.sub(r"\s+", " ", candidate).strip()
    return ""


def _emails(node: SourceNode) -> tuple[str, ...]:
    found = list(node.emails)
    for email in EMAIL_PATTERN.findall(node.description):
        cleaned = email.rstrip(".,;:")
        if cleaned not in found:
            found.append(cleaned)
    return tuple(found)


def _address(value: str, emails: tuple[str, ...], phone: str) -> tuple[str, str, str]:
    lines: list[str] = []
    for line in value.splitlines():
        cleaned = EMAIL_PATTERN.sub("", line)
        cleaned = PHONE_PATTERN.sub("", re.sub(r"\+\s+(?=\d)", "+", cleaned))
        cleaned = re.sub(r"\s+", " ", cleaned).strip(" ,-;")
        if cleaned and not cleaned.casefold().startswith(("http://", "https://", "www.")):
            lines.append(cleaned)
    for index, line in enumerate(lines):
        postal_match = POSTAL_PATTERN.search(line)
        if not postal_match:
            continue
        street_part = line[: postal_match.start()].strip(" ,-;")
        city = line[postal_match.end() :].strip(" ,-;")
        address_parts = [*lines[:index], *([street_part] if street_part else [])]
        return ", ".join(address_parts), postal_match.group(1), city
    return ", ".join(lines), "", ""


def _entry_kinds(node: SourceNode) -> tuple[str, ...] | None:
    if node.category == "Atelier":
        return ("youth_circus", "circus_school", "organization")
    if node.category == "Festival":
        return ("organization",)
    if node.category == "Werkplaats":
        return ("training_space", "organization")
    if node.category == "Spreidingsbureau":
        return ("distributor", "organization")
    if not node.category:
        return UNCATEGORIZED_ORGANIZATIONS.get(node.node_id)
    return None


def _tags(node: SourceNode) -> tuple[str, ...]:
    category_tags = {
        "Atelier": "circus-atelier",
        "Festival": "circus-festival",
        "Werkplaats": "circus-workspace",
        "Spreidingsbureau": "circus-distributor",
    }
    values = ["belgian-circus-landscape"]
    if node.category in category_tags:
        values.append(category_tags[node.category])
    return tuple(values)


def _offers(node: SourceNode) -> tuple[str, ...]:
    values = {
        "Atelier": ("Circuslessen en training",),
        "Festival": ("Circusfestival",),
        "Werkplaats": ("Werkruimte en ondersteuning",),
        "Spreidingsbureau": ("Spreiding en boekingen",),
    }
    return values.get(node.category, ())


def _summary(node: SourceNode) -> str:
    labels = {
        "Atelier": "circusatelier",
        "Festival": "circusfestival",
        "Werkplaats": "circuswerkplaats",
        "Spreidingsbureau": "spreidingsbureau",
    }
    label = labels.get(node.category, "circusorganisatie")
    return f"{node.title} staat in het Landschap van Circuscentrum vermeld als {label}."


def _body(node: SourceNode, imported_on: date) -> str:
    parts = [f"# {node.title}", "", _summary(node)]
    if node.description:
        parts.extend(["", "## Gegevens uit de bron", "", node.description])
    parts.extend(
        [
            "",
            "## Bron",
            "",
            f"Geïmporteerd uit [Circuscentrum Landschap](https://circuscentrum.be/nl/node/{node.node_id}) "
            f"op {imported_on.isoformat()}. Controleer actuele contact- en bezoekinformatie bij "
            "Circuscentrum of de organisatie zelf.",
        ]
    )
    return "\n".join(parts)


def _to_record(
    node: SourceNode,
    coordinates: dict[str, tuple[float, float]],
    imported_on: date,
) -> ImportRecord:
    entry_kinds = _entry_kinds(node)
    if entry_kinds is None:
        raise ValueError(f"unreviewed Circuscentrum category for node {node.node_id}: {node.category!r}")
    latitude, longitude = coordinates.get(node.node_id, (None, None))
    emails = _emails(node)
    phone = _phone(node.description)
    address, postal_code, city = _address(node.description, emails, phone)
    source_urls = (node.website,) if node.website else ()
    return ImportRecord(
        record_id=node.node_id,
        name=node.title,
        description=_summary(node),
        body=_body(node, imported_on),
        entry_kinds=entry_kinds,
        tags=_tags(node),
        latitude=latitude,
        longitude=longitude,
        location_precision="approximate" if latitude is not None else "none",
        record_url=f"https://circuscentrum.be/nl/node/{node.node_id}",
        website=node.website,
        public_emails=emails,
        public_phone=phone,
        source_urls=source_urls,
        offers=_offers(node),
        address=address,
        postal_code=postal_code,
        city=city,
        verification_status="imported_public_directory",
        extra_frontmatter={
            "circuscentrum_node_id": node.node_id,
            **({"circuscentrum_category": node.category} if node.category else {}),
        },
    )


def load_source(imported_on: date) -> tuple[list[ImportRecord], dict[str, Any]]:
    by_id: dict[str, SourceNode] = {}
    settings_documents: list[str] = []
    page_counts: list[int] = []
    for page_number in range(20):
        parser = LandscapeParser()
        parser.feed(_request_page(page_number))
        page_counts.append(len(parser.nodes))
        settings_documents.append("".join(parser.settings_parts))
        if not parser.nodes:
            break
        previous_count = len(by_id)
        for node in parser.nodes:
            if node.node_id in by_id and by_id[node.node_id].title != node.title:
                raise ValueError(f"Circuscentrum node {node.node_id} has conflicting titles")
            by_id[node.node_id] = node
        if len(by_id) == previous_count:
            break
    coordinates = _coordinates(settings_documents)

    categories: Counter[str] = Counter()
    skipped: list[dict[str, str]] = []
    records: list[ImportRecord] = []
    for node in by_id.values():
        categories[node.category or "(blank)"] += 1
        if not node.title:
            skipped.append({"record_id": node.node_id, "reason": "missing title"})
            continue
        if node.category and node.category not in KNOWN_CATEGORIES:
            skipped.append({"record_id": node.node_id, "name": node.title, "reason": "unknown category"})
            continue
        if not node.category and node.node_id not in UNCATEGORIZED_ORGANIZATIONS:
            skipped.append(
                {
                    "record_id": node.node_id,
                    "name": node.title,
                    "reason": "uncategorized record not reviewed as a persistent organization",
                }
            )
            continue
        records.append(_to_record(node, coordinates, imported_on))

    repeated: dict[str, list[ImportRecord]] = defaultdict(list)
    for record in records:
        repeated[normalize_name(record.name)].append(record)
    duplicate_candidates = [
        {"normalized_name": name, "record_ids": [record.record_id for record in group]}
        for name, group in sorted(repeated.items())
        if name and len(group) > 1
    ]
    records.sort(key=lambda record: int(record.record_id))
    return records, {
        "source_pages_with_records": sum(1 for count in page_counts if count),
        "source_page_record_counts": page_counts,
        "source_records": len(by_id),
        "source_category_counts": dict(sorted(categories.items())),
        "source_coordinate_count": len(coordinates),
        "records_without_coordinates": [record.record_id for record in records if record.latitude is None],
        "skipped_source_records": skipped,
        "source_duplicate_candidates": duplicate_candidates,
    }


def import_landscape(
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
    parser = argparse.ArgumentParser(description="Import Circuscentrum Landschap records into CircusFinder")
    parser.add_argument("--docs-root", type=Path, default=repository_root / "docs")
    parser.add_argument("--apply", action="store_true", help="Write reviewed additions and provenance updates")
    parser.add_argument("--prune", action="store_true", help="With --apply, remove stale source-owned records")
    args = parser.parse_args()
    if args.prune and not args.apply:
        parser.error("--prune requires --apply")
    sys.stdout.reconfigure(encoding="utf-8")
    result = import_landscape(args.docs_root.resolve(), apply=args.apply, prune=args.prune)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["apply_blocked"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
