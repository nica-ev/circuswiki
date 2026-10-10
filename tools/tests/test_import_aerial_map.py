from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from circusfinder.import_aerial_map import (  # noqa: E402
    ExistingEntry,
    SOURCE_URL,
    SourceRecord,
    deduplicate_source,
    import_csv,
    load_source,
    match_existing,
    split_label,
)
from translation.markdown import split_markdown  # noqa: E402


HEADERS = ["Latitude_Longitude", "Status", "Location_Name_&_Website"]


def write_csv(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(HEADERS)
        writer.writerows(rows)


def existing_entry() -> str:
    data = {
        "lang": "en",
        "translation_id": "circusfinder/places/network/circus-harmony",
        "translation_status": "original",
        "translation_source_lang": "en",
        "directory_id": "us-st-louis-circus-harmony",
        "title": "Circus Harmony",
        "organization": "Circus Harmony",
        "entry_kinds": ["organization"],
        "directory_status": "active",
        "location_precision": "approximate",
        "latitude": 38.6337,
        "longitude": -90.2001,
        "source": [{"name": "Existing source", "url": "https://example.org"}],
    }
    return "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + "---\n\nExisting body.\n"


class AerialMapImportTests(unittest.TestCase):
    def test_label_parser_splits_full_and_bare_urls(self) -> None:
        self.assertEqual(
            split_label("Example Studio - https://example.org/classes"),
            ("Example Studio", "https://example.org/classes"),
        )
        self.assertEqual(
            split_label("Example Studio - example.org"),
            ("Example Studio", "https://example.org"),
        )
        self.assertEqual(
            split_label("AirGym.Family - https://airgym.family/"),
            ("AirGym.Family", "https://airgym.family/"),
        )
        self.assertEqual(split_label("Example Studio - No direct website provided"), ("Example Studio", ""))

    def test_load_source_keeps_only_named_open_records_and_applies_explicit_corrections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "source.csv"
            write_csv(
                csv_path,
                [
                    ["53.49624,-11345434", "Open", "Aradia Fitness YEG (Edmonton) - example.org"],
                    ["52.1643,106.6644", "Open", "Saskatoon Pole & Dance Studio - example.ca"],
                    ["1,2", "Unknown", "Unknown Studio - unknown.example"],
                    ["3,4", "Open", "null"],
                    ["200,4", "Open", "Broken Studio - broken.example"],
                ],
            )

            records, report = load_source(csv_path)

            self.assertEqual(len(records), 2)
            self.assertEqual((records[0].latitude, records[0].longitude), (53.49624, -113.45434))
            self.assertEqual((records[1].latitude, records[1].longitude), (52.1643, -106.6644))
            self.assertEqual(report["source_status_counts"], {"Open": 4, "Unknown": 1})
            self.assertEqual(len(report["coordinate_corrections"]), 2)
            self.assertEqual(len(report["skipped_open_records"]), 2)

    def test_near_duplicate_with_same_domain_is_collapsed_but_distant_branch_is_kept(self) -> None:
        records = [
            SourceRecord(2, "Alpha", "Alpha Circus", "https://alpha.example", "1,1", 1.0, 1.0),
            SourceRecord(3, "Alpha duplicate", "Circus Alpha", "https://alpha.example", "1.0001,1", 1.0001, 1.0),
            SourceRecord(4, "Alpha branch", "Alpha Circus", "https://alpha.example", "2,2", 2.0, 2.0),
        ]

        selected, groups = deduplicate_source(records)

        self.assertEqual(len(selected), 2)
        self.assertEqual(len(groups), 1)
        self.assertEqual(len(groups[0]["source_rows"]), 2)

    def test_nearby_named_branches_are_not_collapsed(self) -> None:
        records = [
            SourceRecord(2, "North", "Example Studio (North)", "https://example.org", "1,1", 1.0, 1.0),
            SourceRecord(3, "South", "Example Studio (South)", "https://example.org", "1.0001,1", 1.0001, 1.0),
        ]

        selected, groups = deduplicate_source(records)

        self.assertEqual(len(selected), 2)
        self.assertEqual(groups, [])

    def test_unique_domain_matches_existing_entry_when_coordinates_are_missing(self) -> None:
        source = SourceRecord(
            2,
            "Prescott Circus Theatre",
            "Prescott Circus Theatre",
            "https://prescottcircus.org/",
            "",
            None,
            None,
        )
        existing = ExistingEntry(
            path=Path("prescott-circus.md"),
            directory_id="us-oakland-prescott-circus",
            name="Prescott Circus",
            normalized_name="prescott circus",
            website="https://www.prescottcircus.org/",
            domain="prescottcircus.org",
            latitude=37.8044,
            longitude=-122.2712,
            owned=False,
        )

        self.assertEqual(match_existing(source, [existing]), existing)

    def test_import_is_dry_run_by_default_and_updates_existing_provenance_idempotently(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            existing = docs / "en" / "circusfinder" / "places" / "network" / "circus-harmony.md"
            existing.parent.mkdir(parents=True)
            existing.write_text(existing_entry(), encoding="utf-8")
            csv_path = root / "source.csv"
            write_csv(
                csv_path,
                [
                    ["38.63372,-90.20005", "Open", "Circus Harmony - https://circusharmony.org/"],
                    ["10,20", "Open", "New Aerial Studio - newaerial.example"],
                    ["null", "Open", "No Coordinates Studio - nocoordinates.example"],
                    ["11,21", "Shut Down", "Closed Studio - closed.example"],
                ],
            )
            imported_on = date(2026, 10, 10)

            dry_run = import_csv(csv_path, docs, imported_on=imported_on)

            self.assertFalse(dry_run["apply"])
            self.assertEqual(len(dry_run["matched_existing_records"]), 1)
            self.assertEqual(len(dry_run["records_created"]), 2)
            self.assertFalse((docs / "en" / "circusfinder" / "places" / "aerial-training-map").exists())

            applied = import_csv(csv_path, docs, apply=True, imported_on=imported_on)
            self.assertEqual(len(applied["records_created"]), 2)
            generated = list((docs / "en" / "circusfinder" / "places" / "aerial-training-map").glob("*.md"))
            self.assertEqual(len(generated), 2)

            existing_data = yaml.safe_load(split_markdown(existing.read_text(encoding="utf-8")).frontmatter)
            aerial_sources = [source for source in existing_data["source"] if source.get("url") == SOURCE_URL]
            self.assertEqual(len(aerial_sources), 1)
            self.assertEqual(aerial_sources[0]["record_name"], "Circus Harmony")

            second_run = import_csv(csv_path, docs, apply=True, imported_on=imported_on)
            self.assertEqual(second_run["records_created"], [])
            self.assertEqual(second_run["existing_source_updates"], [])
            self.assertEqual(second_run["records_updated"], [])

    def test_source_owned_record_is_updated_in_place_after_upstream_rename(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            csv_path = root / "source.csv"
            imported_on = date(2026, 10, 10)
            write_csv(
                csv_path,
                [["10,20", "Open", "Original Studio - https://studio.example/"]],
            )
            import_csv(csv_path, docs, apply=True, imported_on=imported_on)

            write_csv(
                csv_path,
                [["10.0001,20", "Open", "Renamed Studio - https://studio.example/"]],
            )
            result = import_csv(csv_path, docs, imported_on=imported_on)

            self.assertEqual(result["records_created"], [])
            self.assertEqual(len(result["records_updated"]), 1)
            self.assertEqual(result["stale_owned_records"], [])


if __name__ == "__main__":
    unittest.main()
