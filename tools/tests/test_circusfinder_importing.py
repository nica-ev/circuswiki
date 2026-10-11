from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from circusfinder.import_circuscentrum import (  # noqa: E402
    LandscapeParser,
    _address,
    _coordinates,
    _entry_kinds,
)
from circusfinder.import_jugglingmap import (  # noqa: E402
    CategoryRecord,
    _merged_groups,
    _to_import_record,
)
from circusfinder.importing import (  # noqa: E402
    ImportRecord,
    SourceConfig,
    import_records,
)
from translation.markdown import split_markdown  # noqa: E402


def existing_entry(directory_id: str, name: str, latitude: float | None = None) -> str:
    data: dict[str, object] = {
        "lang": "en",
        "translation_id": f"circusfinder/places/network/{directory_id}",
        "translation_status": "original",
        "translation_source_lang": "en",
        "directory_id": directory_id,
        "title": name,
        "organization": name,
        "entry_kinds": ["organization"],
        "directory_status": "active",
        "location_precision": "approximate" if latitude is not None else "none",
        "source": [{"name": "Existing source", "url": "https://example.org"}],
    }
    if latitude is not None:
        data.update({"latitude": latitude, "longitude": 4.0})
    return "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + "---\n\nExisting body.\n"


def record(record_id: str, name: str, latitude: float | None = None) -> ImportRecord:
    return ImportRecord(
        record_id=record_id,
        name=name,
        description=f"{name} description",
        body=f"# {name}\n\nImported body.",
        entry_kinds=("organization",),
        tags=("test-source",),
        latitude=latitude,
        longitude=4.0 if latitude is not None else None,
        location_precision="approximate" if latitude is not None else "none",
        record_url=f"https://source.example/record/{record_id}",
    )


class SharedImportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = SourceConfig(
            source_id="test-source",
            name="Test source",
            url="https://source.example/",
            dataset_url="https://source.example/data",
            language="en",
            target_relative=Path("en/circusfinder/places/test-source"),
            reuse_basis="Direct permission",
            minimum_expected_records=1,
        )

    def test_import_is_dry_by_default_and_idempotent_after_apply(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            imported_on = date(2026, 10, 11)

            dry_run = import_records([record("42", "New Circus", 50.0)], docs, self.config, imported_on=imported_on)
            self.assertEqual(len(dry_run["records_created"]), 1)
            self.assertFalse(dry_run["apply"])
            self.assertFalse((docs / self.config.target_relative).exists())

            applied = import_records(
                [record("42", "New Circus", 50.0)],
                docs,
                self.config,
                apply=True,
                imported_on=imported_on,
            )
            self.assertEqual(len(applied["records_created"]), 1)
            generated = next((docs / self.config.target_relative).glob("*.md"))
            data = yaml.safe_load(split_markdown(generated.read_text(encoding="utf-8")).frontmatter)
            self.assertEqual(data["source"][0]["record_id"], "42")
            self.assertEqual(data["source"][0]["reuse_basis"], "Direct permission")

            second = import_records(
                [record("42", "New Circus", 50.0)],
                docs,
                self.config,
                apply=True,
                imported_on=imported_on,
            )
            self.assertEqual(second["records_created"], [])
            self.assertEqual(second["records_updated"], [])

    def test_source_owned_refresh_preserves_provenance_from_other_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            imported_on = date(2026, 10, 11)
            item = record("42", "Shared Circus", 50.0)
            import_records([item], docs, self.config, apply=True, imported_on=imported_on)
            generated = next((docs / self.config.target_relative).glob("*.md"))
            document = split_markdown(generated.read_text(encoding="utf-8"))
            data = yaml.safe_load(document.frontmatter)
            data["source"].append(
                {"name": "Second source", "url": "https://second.example/", "record_id": "other-7"}
            )
            frontmatter = yaml.safe_dump(data, allow_unicode=True, sort_keys=False).strip()
            generated.write_text(f"---\n{frontmatter}\n---\n\n{document.body.lstrip()}", encoding="utf-8")

            renamed = record("42", "Shared Circus Renamed", 50.0)
            refreshed = import_records([renamed], docs, self.config, apply=True, imported_on=imported_on)

            self.assertEqual(len(refreshed["records_updated"]), 1)
            refreshed_data = yaml.safe_load(
                split_markdown(generated.read_text(encoding="utf-8")).frontmatter
            )
            self.assertEqual([source["name"] for source in refreshed_data["source"]], ["Test source", "Second source"])

    def test_ambiguous_match_blocks_every_write(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            network = docs / "en" / "circusfinder" / "places" / "network"
            network.mkdir(parents=True)
            (network / "one.md").write_text(existing_entry("one", "Same Circus", 50.0), encoding="utf-8")
            (network / "two.md").write_text(existing_entry("two", "Same Circus", 50.01), encoding="utf-8")

            result = import_records(
                [record("ambiguous", "Same Circus", 50.005), record("new", "Other Circus", 49.0)],
                docs,
                self.config,
                apply=True,
                imported_on=date(2026, 10, 11),
            )

            self.assertTrue(result["apply_blocked"])
            self.assertEqual(len(result["ambiguous_matches"]), 1)
            self.assertFalse((docs / self.config.target_relative).exists())

    def test_missing_coordinates_do_not_match_on_name_alone(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            network = docs / "en" / "circusfinder" / "places" / "network"
            network.mkdir(parents=True)
            (network / "existing.md").write_text(existing_entry("existing", "Generic Circus"), encoding="utf-8")

            result = import_records(
                [record("new", "Generic Circus")],
                docs,
                self.config,
                imported_on=date(2026, 10, 11),
            )

            self.assertEqual(result["matched_existing_records"], [])
            self.assertEqual(len(result["records_created"]), 1)


class SourceAdapterTests(unittest.TestCase):
    def test_circuscentrum_parser_extracts_fields_and_drupal_coordinates(self) -> None:
        settings = {
            "geofield_google_map": {
                "geofield-map-node-organisation-104-field-geolocation": {
                    "data": {
                        "features": [
                            {
                                "geometry": {"coordinates": [5.066147, 51.254343]},
                                "properties": {"entity_id": "104"},
                            }
                        ]
                    }
                }
            }
        }
        source = f"""
        <div class="node node--type-organisation node--view-mode-teaser" id="104">
          <div class="field field-name-node-title"><h2>'t Sirk</h2></div>
          <div class="field field-name-field-organisation-category">Atelier</div>
          <div class="field field-name-field-short-description"><p>Street 13 2470 Retie<br>
          0497 48 69 11<br><a href="mailto:info@example.be">info@example.be</a></p></div>
          <div class="field field--name-organisation-link field__item"><a href="https://example.be/">Website</a></div>
        </div>
        <script type="application/json" data-drupal-selector="drupal-settings-json">{json.dumps(settings)}</script>
        """
        parser = LandscapeParser()
        parser.feed(source)

        self.assertEqual(len(parser.nodes), 1)
        node = parser.nodes[0]
        self.assertEqual((node.node_id, node.title, node.category), ("104", "'t Sirk", "Atelier"))
        self.assertEqual(node.website, "https://example.be/")
        self.assertEqual(node.emails, ["info@example.be"])
        self.assertEqual(_entry_kinds(node), ("youth_circus", "circus_school", "organization"))
        self.assertEqual(_coordinates(["".join(parser.settings_parts)])["104"], (51.254343, 5.066147))
        self.assertEqual(
            _address(node.description, ("info@example.be",), "0497 48 69 11"),
            ("Street 13", "2470", "Retie"),
        )

    def test_jugglingmap_merges_same_name_categories_at_one_pin(self) -> None:
        pin = "01TEST"
        common = {"lat": 50.0, "lng": 4.0, "place_name": "Example place"}
        categories = [
            CategoryRecord(pin, common["lat"], common["lng"], common["place_name"], {"name": "Example", "kind": "openTraining"}),
            CategoryRecord(pin, common["lat"], common["lng"], common["place_name"], {"name": "Example", "kind": "circusSchool"}),
            CategoryRecord(pin, common["lat"], common["lng"], common["place_name"], {"name": "Separate shop", "kind": "shop"}),
        ]

        groups = _merged_groups(categories)
        self.assertEqual(sorted(len(group) for group in groups), [1, 2])
        merged = _to_import_record(next(group for group in groups if len(group) == 2), date(2026, 10, 11))
        self.assertEqual(merged.entry_kinds, ("training_space", "circus_school", "organization"))
        self.assertEqual(merged.extra_frontmatter["jugglingmap_categories"], ["openTraining", "circusSchool"])

    def test_jugglingmap_normalizes_multiline_names_for_frontmatter(self) -> None:
        category = CategoryRecord(
            "01TEST",
            50.0,
            4.0,
            "Example place",
            {"name": "First line\n\nSecond line", "kind": "openTraining"},
        )

        imported = _to_import_record([category], date(2026, 10, 11))

        self.assertEqual(imported.name, "First line Second line")
        self.assertNotIn("\n", imported.description)


if __name__ == "__main__":
    unittest.main()
