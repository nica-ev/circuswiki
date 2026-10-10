from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import stage_multilang  # noqa: E402


class StagingWorkflowTests(unittest.TestCase):
    def test_single_language_stage_discovers_other_languages_for_fallbacks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            build = Path(tmp)
            with (
                patch.object(sys, "argv", ["stage_multilang.py", "--language", "de"]),
                patch.object(stage_multilang, "BUILD", build),
                patch.object(stage_multilang, "discover_translation_groups", return_value={}) as discover,
                patch.object(stage_multilang, "copy_language"),
                patch.object(stage_multilang, "create_fallback_pages") as create_fallbacks,
                patch.object(stage_multilang, "write_translation_map"),
                patch.object(stage_multilang, "normalize_markdown_files", return_value=0),
                patch.object(stage_multilang, "export_datasets"),
            ):
                stage_multilang.main()

            discover.assert_called_once_with()
            create_fallbacks.assert_called_once_with({}, ("de",))

    def test_page_url_default_and_non_default_language(self) -> None:
        with patch.dict(os.environ, {"CIRCUSWIKI_SITE_BASE_PATH": "/example/"}):
            self.assertEqual(stage_multilang.page_url("de", "index.md"), "/example/")
            self.assertEqual(stage_multilang.page_url("en", "spiele/test.md"), "/example/en/spiele/test/")

    def test_choose_fallback_prefers_common_language_then_source(self) -> None:
        pages = {
            "de": {"relative_path": "x.md"},
            "en": {"relative_path": "x.md"},
        }
        self.assertEqual(stage_multilang.choose_fallback_language("pl", "de", pages), "en")
        self.assertEqual(stage_multilang.choose_fallback_language("en", "de", pages), "de")

    def test_translation_map_contains_registry_languages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            build = Path(tmp)
            groups = {
                "index": {
                    "translation_id": "index",
                    "source_lang": "de",
                    "title": "Index",
                    "relative_path": "index.md",
                    "pages": {
                        "de": {
                            "relative_path": "index.md",
                            "translation_status": "original",
                            "translation_model": "",
                            "translation_updated": "",
                            "path": "docs/de/index.md",
                            "translation_source": "",
                            "translation_source_lang": "de",
                            "authors": [],
                        }
                    },
                }
            }
            with patch.object(stage_multilang, "BUILD", build):
                stage_multilang.write_translation_map(groups)
            data = (build / "de" / "javascripts" / "translation-map.json").read_text(encoding="utf-8")
            self.assertIn('"languages"', data)
            self.assertIn('"sk"', data)

    def test_translation_map_can_be_written_for_one_staged_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            build = Path(tmp)
            groups = {
                "index": {
                    "translation_id": "index",
                    "source_lang": "de",
                    "title": "Index",
                    "relative_path": "index.md",
                    "pages": {
                        "de": {
                            "relative_path": "index.md",
                            "translation_status": "original",
                            "translation_model": "",
                            "translation_updated": "",
                            "path": "docs/de/index.md",
                            "translation_source": "",
                            "translation_source_lang": "de",
                            "authors": [],
                        }
                    },
                }
            }
            with patch.object(stage_multilang, "BUILD", build):
                stage_multilang.write_translation_map(groups, ("de",))

            self.assertTrue((build / "de" / "javascripts" / "translation-map.json").exists())
            self.assertFalse((build / "en").exists())

    def test_copy_language_inherits_default_blog_authors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            build = root / ".build"
            assets = root / "site-assets"
            (docs / "de" / "blog").mkdir(parents=True)
            (docs / "en" / "blog").mkdir(parents=True)
            assets.mkdir()
            authors = "authors:\n  editor:\n    name: Editor\n"
            (docs / "de" / "blog" / ".authors.yml").write_text(authors, encoding="utf-8")

            with (
                patch.object(stage_multilang, "DOCS", docs),
                patch.object(stage_multilang, "BUILD", build),
                patch.object(stage_multilang, "SITE_ASSETS", assets),
                patch.object(stage_multilang, "DEFAULT_LANGUAGE", "de"),
            ):
                stage_multilang.copy_language("en")

            inherited = build / "en" / "blog" / ".authors.yml"
            self.assertEqual(inherited.read_text(encoding="utf-8"), authors)

    def test_internal_doc_link_normalization_removes_language_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "page.md"
            page.write_text("[Target](docs/en/folder/target.md#section)\n", encoding="utf-8")
            stage_multilang.normalize_internal_doc_links(root)
            self.assertEqual(page.read_text(encoding="utf-8"), "[Target](folder/target.md#section)\n")

    def test_obsidian_callouts_convert_to_admonitions_outside_code_fences(self) -> None:
        source = (
            "> [!tip]- Hinweise\n"
            "> Erste Zeile\n"
            "> Zweite Zeile\n"
            "\n"
            "```\n"
            "> [!warning] not a callout\n"
            "```\n"
        )
        result = stage_multilang.convert_obsidian_callouts(source)
        self.assertIn('??? tip "Hinweise"', result)
        self.assertIn("    Erste Zeile", result)
        self.assertIn("> [!warning] not a callout", result)

    def test_combined_markdown_normalization_applies_all_rewrites(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "folder" / "page.md"
            page.parent.mkdir()
            page.write_text(
                "[Target](docs/en/target.md)\n"
                "![Image](../../img/example.png)\n"
                "> [!tip] Note\n"
                "> Body\n",
                encoding="utf-8",
            )

            processed = stage_multilang.normalize_markdown_files(root)

            result = page.read_text(encoding="utf-8")
            self.assertEqual(processed, 1)
            self.assertIn("[Target](target.md)", result)
            self.assertIn("![Image](../img/example.png)", result)
            self.assertIn('!!! tip "Note"', result)


if __name__ == "__main__":
    unittest.main()
