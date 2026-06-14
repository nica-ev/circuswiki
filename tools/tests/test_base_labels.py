from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import base_labels  # noqa: E402
from dynamic.obsidian_backend import materialize_language_base  # noqa: E402


BASE_TEXT = """formulas:
  link-title: file.aslink(title)
properties:
  formula.link-title:
    displayName: Link
  note.group-min:
    displayName: Spieler Min
  note.Material:
    displayName: \"Material\"
views:
  - type: table
    name: Test
    filters:
      and:
        - lang == "de"
    order:
      - formula.link-title
      - group-min
"""


class BaseLabelTests(unittest.TestCase):
    def test_extract_display_names_from_properties_section(self) -> None:
        labels = base_labels.extract_display_names(BASE_TEXT)
        self.assertEqual(
            labels,
            {
                "formula.link-title": "Link",
                "note.group-min": "Spieler Min",
                "note.Material": "Material",
            },
        )

    def test_apply_display_names_preserves_other_base_content(self) -> None:
        updated = base_labels.apply_display_names(
            BASE_TEXT,
            {"note.group-min": "Players Min", "note.Material": "Required material"},
        )
        self.assertIn("displayName: Players Min", updated)
        self.assertIn("displayName: Required material", updated)
        self.assertIn("lang == \"de\"", updated)
        self.assertIn("name: Test", updated)

    def test_plan_detects_missing_and_stale_translations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            bases = root / "_bases"
            config = root / "tools" / "config" / "base_display_names.json"
            bases.mkdir(parents=True)
            (bases / "Test.base").write_text(BASE_TEXT, encoding="utf-8")
            config.parent.mkdir(parents=True)
            config.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "bases": {
                            "_bases/Test.base": {
                                "source_lang": "de",
                                "properties": {
                                    "formula.link-title": {
                                        "source": "Link",
                                        "source_hash": base_labels.source_hash("Link"),
                                        "translations": {"en": {"value": "Link", "source_hash": "old"}},
                                    }
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            with (
                patch.object(base_labels, "ROOT", root),
                patch.object(base_labels, "BASES", bases),
                patch.object(base_labels, "CONFIG_PATH", config),
                patch.object(base_labels, "language_codes", return_value=["de", "en"]),
            ):
                plan = base_labels.plan_base_label_translation("_bases/Test.base", "en")

        reasons = {(item["property"], item["reason"]) for item in plan["candidates"]}
        self.assertIn(("formula.link-title", "stale"), reasons)
        self.assertIn(("note.group-min", "missing"), reasons)

    def test_materialize_language_base_applies_stored_display_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            bases = root / "_bases"
            config = root / "tools" / "config" / "base_display_names.json"
            bases.mkdir(parents=True)
            (bases / "Test.base").write_text(BASE_TEXT, encoding="utf-8")
            config.parent.mkdir(parents=True)
            config.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "bases": {
                            "_bases/Test.base": {
                                "source_lang": "de",
                                "properties": {
                                    "note.group-min": {
                                        "source": "Spieler Min",
                                        "source_hash": base_labels.source_hash("Spieler Min"),
                                        "translations": {
                                            "en": {
                                                "value": "Players Min",
                                                "source_hash": base_labels.source_hash("Spieler Min"),
                                            }
                                        },
                                    }
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            with (
                patch.object(base_labels, "ROOT", root),
                patch.object(base_labels, "BASES", bases),
                patch.object(base_labels, "CONFIG_PATH", config),
                patch("dynamic.obsidian_backend.ROOT", root),
                patch("dynamic.obsidian_backend.GENERATED_BASE_ROOT", bases),
            ):
                generated = root / materialize_language_base("_bases/Test.base", "en")

            text = generated.read_text(encoding="utf-8")
            self.assertIn('lang == "en"', text)
            self.assertIn("displayName: Players Min", text)


if __name__ == "__main__":
    unittest.main()
