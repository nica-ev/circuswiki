from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from circusfinder import DirectoryValidationError, load_entries, write_datasets  # noqa: E402


def entry_text(**overrides: object) -> str:
    values = {
        "lang": "de",
        "translation_id": "circusfinder/places/demo",
        "translation_status": "original",
        "translation_source_lang": "de",
        "directory_id": "demo",
        "title": "Demo Circus",
        "entry_kinds": ["training_space"],
        "location_precision": "exact",
        "latitude": 52.5,
        "longitude": 13.4,
        "source": [{"name": "Example source", "url": "https://example.org/data"}],
    }
    values.update(overrides)
    import yaml

    return "---\n" + yaml.safe_dump(values, allow_unicode=True, sort_keys=False) + "---\nDemo\n"


class CircusFinderExportTests(unittest.TestCase):
    def test_valid_entry_is_exported_for_each_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            source.parent.mkdir(parents=True)
            source.write_text(entry_text(), encoding="utf-8")

            with patch("circusfinder.exporter.language_codes", return_value=("de", "en")):
                entries = load_entries(root / "docs")
                counts = write_datasets(entries, root / ".build")

            self.assertEqual(counts, {"de": 1, "en": 1})
            payload = json.loads((root / ".build" / "en" / "data" / "circusfinder.v1.json").read_text(encoding="utf-8"))
            self.assertEqual(payload["records"][0]["id"], "demo")
            self.assertTrue(payload["records"][0]["translation_missing"])

    def test_dataset_export_can_target_one_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            source.parent.mkdir(parents=True)
            source.write_text(entry_text(), encoding="utf-8")

            entries = load_entries(root / "docs")
            counts = write_datasets(entries, root / ".build", target_languages=("de",))

            self.assertEqual(counts, {"de": 1})
            self.assertTrue((root / ".build" / "de" / "data" / "circusfinder.v1.json").exists())
            self.assertFalse((root / ".build" / "en").exists())

    def test_invalid_coordinates_fail_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            source.parent.mkdir(parents=True)
            source.write_text(entry_text(latitude=120), encoding="utf-8")

            with patch("circusfinder.exporter.language_codes", return_value=("de",)):
                with self.assertRaises(DirectoryValidationError) as error:
                    load_entries(root / "docs")

            self.assertIn("latitude must be between -90 and 90", str(error.exception))

    def test_missing_source_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            source.parent.mkdir(parents=True)
            source.write_text(entry_text(source=None), encoding="utf-8")

            with patch("circusfinder.exporter.language_codes", return_value=("de",)):
                with self.assertRaises(DirectoryValidationError) as error:
                    load_entries(root / "docs")

            self.assertIn("source must be a non-empty list of mappings", str(error.exception))

    def test_translation_localizes_text_but_not_structural_data(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            german = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            english = root / "docs" / "en" / "circusfinder" / "places" / "demo.md"
            german.parent.mkdir(parents=True)
            english.parent.mkdir(parents=True)
            german.write_text(entry_text(title="Deutscher Titel", latitude=52.5), encoding="utf-8")
            english.write_text(
                entry_text(
                    lang="en",
                    title="English title",
                    translation_status="human-translated",
                    latitude=40.0,
                ),
                encoding="utf-8",
            )

            with patch("circusfinder.exporter.language_codes", return_value=("de", "en")):
                entries = load_entries(root / "docs")
                write_datasets(entries, root / ".build")

            payload = json.loads((root / ".build" / "en" / "data" / "circusfinder.v1.json").read_text(encoding="utf-8"))
            record = payload["records"][0]
            self.assertEqual(record["title"], "English title")
            self.assertEqual(record["location"]["latitude"], 52.5)
            self.assertFalse(record["translation_missing"])

    def test_coordinates_are_forbidden_for_non_location(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "demo.md"
            source.parent.mkdir(parents=True)
            source.write_text(entry_text(location_precision="none"), encoding="utf-8")

            with patch("circusfinder.exporter.language_codes", return_value=("de",)):
                with self.assertRaises(DirectoryValidationError) as error:
                    load_entries(root / "docs")

            self.assertIn("location_precision 'none' cannot have coordinates", str(error.exception))

    def test_network_metadata_and_multiple_contacts_are_exported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "en" / "circusfinder" / "places" / "network.md"
            source.parent.mkdir(parents=True)
            source.write_text(
                entry_text(
                    lang="en",
                    translation_source_lang="en",
                    organization="Example Network",
                    collective_statuses=["regional_partner"],
                    contact_people=["Ada Example", "Team Contact"],
                    public_emails=["hello@example.org", "team@example.org"],
                ),
                encoding="utf-8",
            )

            with patch("circusfinder.exporter.language_codes", return_value=("en",)):
                entries = load_entries(root / "docs")
                write_datasets(entries, root / ".build")

            payload = json.loads((root / ".build" / "en" / "data" / "circusfinder.v1.json").read_text(encoding="utf-8"))
            record = payload["records"][0]
            self.assertEqual(record["organization"], "Example Network")
            self.assertEqual(record["collective_statuses"], ["regional_partner"])
            self.assertEqual(record["contact"]["people"], ["Ada Example", "Team Contact"])
            self.assertEqual(record["contact"]["emails"], ["hello@example.org", "team@example.org"])

    def test_exact_place_contact_schedule_and_sources_are_exported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs" / "de" / "circusfinder" / "places" / "studio.md"
            source.parent.mkdir(parents=True)
            source.write_text(
                entry_text(
                    address="Beispielstraße 23",
                    postal_code="06108",
                    public_phone="+49 345 123456",
                    opening_hours=["Sonntag 17:30–20:30 Uhr"],
                    schedule_note="Aktuelle Termine vor dem Besuch prüfen.",
                    schedule_url="https://example.org/schedule",
                    source_urls=["https://example.org/contact"],
                    source=[
                        {
                            "name": "Example directory",
                            "url": "https://example.org/directory",
                            "record_name": "Example studio",
                        }
                    ],
                ),
                encoding="utf-8",
            )

            with patch("circusfinder.exporter.language_codes", return_value=("de",)):
                entries = load_entries(root / "docs")
                write_datasets(entries, root / ".build")

            payload = json.loads((root / ".build" / "de" / "data" / "circusfinder.v1.json").read_text(encoding="utf-8"))
            record = payload["records"][0]
            self.assertEqual(record["location"]["address"], "Beispielstraße 23")
            self.assertEqual(record["location"]["postal_code"], "06108")
            self.assertEqual(record["contact"]["phone"], "+49 345 123456")
            self.assertEqual(record["opening_hours"], ["Sonntag 17:30–20:30 Uhr"])
            self.assertEqual(record["schedule_url"], "https://example.org/schedule")
            self.assertEqual(record["source"][0]["name"], "Example directory")
            self.assertEqual(record["source"][0]["record_name"], "Example studio")
            self.assertEqual(record["source_urls"], ["https://example.org/contact"])


if __name__ == "__main__":
    unittest.main()
