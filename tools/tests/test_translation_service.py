from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from translation.link_repair import LinkRepairResult  # noqa: E402
from translation.service import SourceChangedError, atomic_write_text, translate_page  # noqa: E402


SOURCE = """---
lang: de
translation_id: example
translation_status: original
translation_source_lang: de
title: Beispiel
description: Beschreibung
---

Quelltext.
"""


class TranslationServiceTests(unittest.TestCase):
    def test_atomic_write_replaces_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "target.md"
            target.write_text("old", encoding="utf-8")

            atomic_write_text(target, "new\n")

            self.assertEqual(target.read_text(encoding="utf-8"), "new\n")
            self.assertEqual(list(target.parent.glob(f".{target.name}.*.tmp")), [])

    def test_planned_hash_mismatch_stops_before_model_calls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "docs" / "de" / "example.md"
            target = root / "docs" / "en" / "example.md"
            source.parent.mkdir(parents=True)
            source.write_text(SOURCE, encoding="utf-8")

            with (
                patch("translation.service.ROOT", root),
                patch("translation.service.language_path", return_value=target),
                patch("translation.service.translate_body") as translate_body,
                patch("translation.service.call_metadata_translation_model") as translate_metadata,
            ):
                with self.assertRaisesRegex(SourceChangedError, "body"):
                    translate_page(
                        source_path="docs/de/example.md",
                        source_lang="de",
                        target_lang="en",
                        model="test-model",
                        expected_source_body_hash="outdated",
                    )

            translate_body.assert_not_called()
            translate_metadata.assert_not_called()
            self.assertFalse(target.exists())

    def test_source_change_during_translation_preserves_existing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "docs" / "de" / "example.md"
            target = root / "docs" / "en" / "example.md"
            source.parent.mkdir(parents=True)
            target.parent.mkdir(parents=True)
            source.write_text(SOURCE, encoding="utf-8")
            target.write_text("existing target\n", encoding="utf-8")

            def translate_and_change_source(**_kwargs: object):
                source.write_text(SOURCE.replace("Quelltext.", "Geändert."), encoding="utf-8")
                return "Translated.\n", LinkRepairResult("Translated.\n", False, 0, []), []

            with (
                patch("translation.service.ROOT", root),
                patch("translation.service.language_path", return_value=target),
                patch("translation.service.rel", side_effect=lambda path: Path(path).name),
                patch("translation.service.translate_body", side_effect=translate_and_change_source),
                patch("translation.service.call_metadata_translation_model", return_value={"title": "Example"}),
            ):
                with self.assertRaisesRegex(SourceChangedError, "body"):
                    translate_page(
                        source_path="docs/de/example.md",
                        source_lang="de",
                        target_lang="en",
                        model="test-model",
                    )

            self.assertEqual(target.read_text(encoding="utf-8"), "existing target\n")


if __name__ == "__main__":
    unittest.main()
