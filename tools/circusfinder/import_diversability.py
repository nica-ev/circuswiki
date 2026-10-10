from __future__ import annotations

import html
import re
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

import yaml


MAP_URL = "https://diversabilitycircus.org/map/"
KML_URL = "https://www.google.com/maps/d/kml?mid=1y-Kcn2lBvxyfpTKRxYjVg7o8eK9g1Po&forcekml=1"
IMPORT_DATE = date(2026, 10, 10)
BATCH_ID = "diversability-circus-map-2026-10-10"
TARGET_RELATIVE = Path("en/circusfinder/places/diversability")
KML_NAMESPACE = {"kml": "http://www.opengis.net/kml/2.2"}

# These organisations already have a CircusFinder record from the QuatProps or
# NICA batches. Keeping the source names here makes the import repeatable while
# preventing a second marker for the same organisation.
EXISTING_RECORDS = {
    "azirkarte gizarteratzeko elkartea": "es-vitoria-gasteiz-azirkarte",
    "circa asociacion artistas malabares modulares todozancos": "es-barcelona-circa-artistas",
    "circo despacio": "es-seville-circo-despacio-canton-y-prada",
    "cirqueon centrum pro novy cirkus": "cz-prague-cirqueon",
    "cirkus fuskabo": "si-ljubljana-cirkus-fuskabo",
    "cirkus in beweging": "be-leuven-cirkus-in-beweging",
    "cirkus legrando": "cz-brno-cirkus-legrando",
    "circus amersfoort": "nl-amersfoort-circus-amersfoort",
    "circus camino": "gr-crete-circus-camino",
    "circus eruption": "gb-swansea-circus-eruptions",
    "circus school carampa": "es-madrid-escuela-de-circo-carampa",
    "clown kiko circus kiko": "nl-nijmegen-circus-kiko",
    "ecole du cirque de bruxelles": "be-brussels-ecole-de-cirque",
    "inspiral circus space": "hu-budapest-inspiral-circus",
    "mini art fest": "bg-sofia-mini-art-festival",
    "monokyklo": "gr-thessaloniki-monokyklo",
    "network for inclusive circus arts": "de-halle-nica-tohuwabohu",
    "odskocznia studio": "pl-warsaw-odskocznia-studio",
    "riga circus": "lv-riga-nextdoor-circus-riga-cirks",
    "roundabout circus inc": "au-new-south-wales-roundabout-circus",
    "spazio ipotetico": "it-florence-spazio-ipotetico",
    "stiklings": "gb-manchester-stiklings",
    "tohuwabohu halle": "de-halle-nica-tohuwabohu",
    "trapiti": "sk-andovce-nove-zamky-trapiti",
    "woesh circusatelier": "be-brugge-circusatelier-woesh",
}


@dataclass(frozen=True)
class Placemark:
    name: str
    description: str
    longitude: float
    latitude: float


class _PlainTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"br", "p", "div", "li"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div", "li"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def _normalize_name(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.casefold()).strip()


def _slug(value: str) -> str:
    return _normalize_name(value).replace(" ", "-") or "unnamed"


def _plain_text(value: str) -> str:
    parser = _PlainTextParser()
    parser.feed(html.unescape(value))
    text = "".join(parser.parts).replace("\xa0", " ").replace("", "")
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n\n".join(line for line in lines if line)


def _summary(description: str, name: str) -> str:
    paragraph = description.split("\n\n", 1)[0].strip()
    if not paragraph:
        return f"Inclusive circus organisation listed by the DiversAbility Circus project."
    paragraph = re.sub(r"[*_`]", "", paragraph)
    sentence = re.split(r"(?<=[.!?])\s+", paragraph, maxsplit=1)[0]
    if len(sentence) < 80 and len(paragraph) > len(sentence):
        sentence = paragraph
    if len(sentence) <= 320:
        return sentence
    shortened = sentence[:317].rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "…"


def _emails(value: str) -> list[str]:
    found = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", value, flags=re.IGNORECASE)
    return list(dict.fromkeys(email.rstrip(".,;:") for email in found))


def _website(value: str) -> str:
    candidates = re.findall(r"(?i)(?:https?://|www\.)[^\s<>]+", value)
    for candidate in candidates:
        candidate = html.unescape(candidate).rstrip(".,;:)")
        if "mymaps.usercontent.google.com" in candidate:
            continue
        return candidate if candidate.startswith(("http://", "https://")) else "https://" + candidate
    return ""


def _phone(value: str) -> str:
    match = re.search(r"(?i)(?:tel(?:ephone)?|phone)\s*:\s*([+()0-9][+()0-9 ./-]{6,}[0-9])", value)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


def download_placemarks() -> list[Placemark]:
    request = urllib.request.Request(KML_URL, headers={"User-Agent": "CircusWiki/1.0 (public data import)"})
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    placemarks: list[Placemark] = []
    for node in root.findall(".//kml:Placemark", KML_NAMESPACE):
        name = (node.findtext("kml:name", default="", namespaces=KML_NAMESPACE) or "").strip()
        raw_description = node.findtext("kml:description", default="", namespaces=KML_NAMESPACE) or ""
        coordinates = (node.findtext(".//kml:coordinates", default="", namespaces=KML_NAMESPACE) or "").strip()
        if not name or not coordinates:
            continue
        longitude_text, latitude_text, *_ = coordinates.split(",")
        placemarks.append(
            Placemark(
                name=name,
                description=_plain_text(raw_description),
                longitude=float(longitude_text),
                latitude=float(latitude_text),
            )
        )
    return placemarks


def _deduplicate(placemarks: list[Placemark]) -> tuple[list[Placemark], list[str]]:
    by_coordinates: dict[tuple[float, float], Placemark] = {}
    duplicates: list[str] = []
    for placemark in placemarks:
        key = (placemark.latitude, placemark.longitude)
        current = by_coordinates.get(key)
        if current is None:
            by_coordinates[key] = placemark
            continue
        duplicates.append(placemark.name)
        if len(placemark.description) > len(current.description):
            by_coordinates[key] = placemark
    return list(by_coordinates.values()), duplicates


def _frontmatter(placemark: Placemark, slug: str) -> dict[str, object]:
    directory_id = f"diversability-{slug}"
    imported_on = IMPORT_DATE.isoformat()
    data: dict[str, object] = {
        "lang": "en",
        "translation_id": f"circusfinder/places/diversability/{slug}",
        "created": imported_on,
        "update": imported_on,
        "publish": True,
        "tags": ["circusfinder", "inclusive-circus", "diversability-circus"],
        "title": placemark.name,
        "description": _summary(placemark.description, placemark.name),
        "translation_status": "original",
        "translation_source_lang": "en",
        "directory_id": directory_id,
        "entry_kinds": ["organization"],
        "directory_status": "active",
        "latitude": placemark.latitude,
        "longitude": placemark.longitude,
        "location_precision": "approximate",
        "organization": placemark.name,
        "last_verified": imported_on,
        "verification_status": "imported_public_map",
        "source": [
            {
                "name": "DiversAbility Circus",
                "url": MAP_URL,
                "dataset_url": KML_URL,
                "record_name": placemark.name,
                "retrieved": imported_on,
                "batch_id": BATCH_ID,
            }
        ],
    }
    website = _website(placemark.description)
    emails = _emails(placemark.description)
    phone = _phone(placemark.description)
    if website:
        data["website"] = website
    if emails:
        data["public_emails"] = emails
    if phone:
        data["public_phone"] = phone
    return data


def _markdown(placemark: Placemark, slug: str) -> str:
    frontmatter = yaml.safe_dump(
        _frontmatter(placemark, slug),
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    description = placemark.description or "No description was provided in the source map."
    return (
        f"---\n{frontmatter}\n---\n\n"
        f"# {placemark.name}\n\n"
        f"{description}\n\n"
        "## Source\n\n"
        f"Imported from the [{'DiversAbility Circus Map'}]({MAP_URL}) on {IMPORT_DATE.isoformat()}. "
        "The map position is treated as approximate because the source does not provide a structured "
        "location-precision field.\n"
    )


def import_map(docs_root: Path) -> dict[str, object]:
    placemarks = download_placemarks()
    deduplicated, source_duplicates = _deduplicate(placemarks)
    target = docs_root / TARGET_RELATIVE
    target.mkdir(parents=True, exist_ok=True)

    imported: list[str] = []
    skipped: dict[str, str] = {}
    used_slugs: set[str] = set()
    for placemark in deduplicated:
        normalized_name = _normalize_name(placemark.name)
        if normalized_name in EXISTING_RECORDS:
            skipped[placemark.name] = EXISTING_RECORDS[normalized_name]
            continue
        slug = _slug(placemark.name)
        candidate = slug
        suffix = 2
        while candidate in used_slugs:
            candidate = f"{slug}-{suffix}"
            suffix += 1
        slug = candidate
        used_slugs.add(slug)
        (target / f"{slug}.md").write_text(_markdown(placemark, slug), encoding="utf-8")
        imported.append(placemark.name)

    return {
        "source_records": len(placemarks),
        "source_coordinate_duplicates": source_duplicates,
        "existing_records_skipped": skipped,
        "records_imported": len(imported),
        "target": target.as_posix(),
    }


if __name__ == "__main__":
    import json
    import sys

    repository_root = Path(__file__).resolve().parents[2]
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(import_map(repository_root / "docs"), ensure_ascii=False, indent=2))
