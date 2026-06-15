from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from translation.markdown import join_markdown, split_markdown  # noqa: E402
from translation.metadata import ensure_scalars, read_scalar  # noqa: E402
from translation.health import (  # noqa: E402
    common_page_issues,
    source_page_issues,
    source_reference_hashes,
    translated_page_issues,
)
from translation.workflow import (  # noqa: E402
    VaultPage,
    apply_translated_metadata,
    batch_translation_plan,
    find_group_source_language,
    merge_source_metadata,
    needs_localized_metadata_translation,
    restore_markdown_link_targets,
    restore_wikilink_targets,
    source_body_hash,
    source_metadata_hash,
    source_metadata_for_translation,
    source_owned_metadata_differences,
    source_structural_metadata_hash,
    translatable_body_hash,
    translate_body,
)
from unittest.mock import patch


class TranslationWorkflowTests(unittest.TestCase):
    def test_batch_plan_all_targets(self) -> None:
        plan = batch_translation_plan("all", 1)
        self.assertEqual(plan["target_lang"], "all")
        self.assertGreaterEqual(plan["planned_count"], 0)
        self.assertIn("target_langs", plan)
        self.assertIn("de", plan["target_langs"])

    def test_batch_plan_reason_filter(self) -> None:
        plan = batch_translation_plan("all", 5, reason="missing_file")
        self.assertTrue(
            all(item["reason"] == "missing_file" for item in plan["candidates"]),
            plan["candidates"],
        )
        self.assertEqual(plan["filters"]["reason"], "missing_file")

    def test_batch_plan_source_filter(self) -> None:
        plan = batch_translation_plan("all", 5, source_lang="de")
        self.assertTrue(
            all(item["source_lang"] == "de" for item in plan["candidates"]),
            plan["candidates"],
        )
        self.assertEqual(plan["filters"]["source_lang"], "de")

    def test_batch_plan_max_source_chars_filter(self) -> None:
        plan = batch_translation_plan("all", 5, max_source_chars=1)
        self.assertEqual(plan["total_candidates"], 0)
        self.assertEqual(plan["filters"]["max_source_chars"], 1)

    def test_source_language_uses_original_status(self) -> None:
        pages = {
            "en": [self.page("en", "machine-translated")],
            "pl": [self.page("pl", "original")],
            "de": [self.page("de", "")],
        }
        self.assertEqual(find_group_source_language(pages), "pl")

    def test_frontmatter_unknown_fields_are_preserved(self) -> None:
        source = "---\ntitle: Test\ncustom_field: keep me\n---\nBody\n"
        document = split_markdown(source)
        updated = ensure_scalars(document.frontmatter, {"lang": "en"})
        output = join_markdown(updated, document.body)
        result = split_markdown(output)
        self.assertEqual(read_scalar(result.frontmatter, "custom_field"), "keep me")
        self.assertEqual(read_scalar(result.frontmatter, "lang"), "en")

    def test_read_scalar_uses_yaml_for_quoted_and_folded_values(self) -> None:
        frontmatter = 'title: "A \\"quoted\\" title"\ndescription: >\n  first line\n  second line\n'
        self.assertEqual(read_scalar(frontmatter, "title"), 'A "quoted" title')
        self.assertEqual(read_scalar(frontmatter, "description"), "first line second line")

    def test_body_hash_ignores_metadata_changes(self) -> None:
        self.assertEqual(source_body_hash("Body\n"), source_body_hash("Body\n"))
        self.assertNotEqual(source_body_hash("Body\n"), source_body_hash("Changed\n"))

    def test_metadata_hash_tracks_configured_translatable_fields(self) -> None:
        first = "title: Test\ndescription: One\ncustom: ignored\n"
        second = "title: Test\ndescription: Two\ncustom: ignored\n"
        third = "title: Test\ndescription: One\ncustom: changed\n"
        fourth = "title: Test\ndescription: One\nSchwierigkeit: einfach\ncustom: ignored\n"
        self.assertNotEqual(source_metadata_hash(first), source_metadata_hash(second))
        self.assertEqual(source_metadata_hash(first), source_metadata_hash(third))
        self.assertNotEqual(source_metadata_hash(first), source_metadata_hash(fourth))

    def test_source_metadata_for_translation_uses_configured_fields(self) -> None:
        metadata = source_metadata_for_translation(
            "title: Test\ndescription: One\nSchwierigkeit: einfach\nMaterial: Bälle\ncustom: ignored\n"
        )
        self.assertEqual(
            metadata,
            {
                "title": "Test",
                "description": "One",
                "Schwierigkeit": "einfach",
                "Material": "Bälle",
            },
        )

    def test_localized_and_structural_metadata_hashes_are_independent(self) -> None:
        base = "title: Test\ndescription: One\nupdate: 2026-06-14\ncustom: source\n"
        structural_changed = "title: Test\ndescription: One\nupdate: 2026-06-15\ncustom: source\n"
        localized_changed = "title: Test\ndescription: Two\nupdate: 2026-06-14\ncustom: source\n"

        self.assertEqual(source_metadata_hash(base), source_metadata_hash(structural_changed))
        self.assertNotEqual(source_metadata_hash(base), source_metadata_hash(localized_changed))
        self.assertNotEqual(source_structural_metadata_hash(base), source_structural_metadata_hash(structural_changed))
        self.assertEqual(source_structural_metadata_hash(base), source_structural_metadata_hash(localized_changed))

    def test_metadata_merge_preserves_target_translated_fields(self) -> None:
        source = "title: Quelle\ndescription: Deutsch\ntags:\n  - spiel\nauthors:\n  - Marc\n"
        target = "title: Existing English\ndescription: Existing description\ntags:\n  - translated-tag\nlocal_note: remove\n"
        merged = merge_source_metadata(target, source)
        translated = apply_translated_metadata(
            merged,
            {"title": "Source", "description": "English description"},
        )
        self.assertEqual(read_scalar(translated, "title"), "Source")
        self.assertEqual(read_scalar(translated, "description"), "English description")
        self.assertIsNone(read_scalar(translated, "local_note"))
        self.assertIn("tags:\n  - spiel", translated)
        self.assertNotIn("translated-tag", translated)
        self.assertIn("authors:\n  - Marc", translated)

    def test_metadata_merge_removes_target_tags_when_source_has_none(self) -> None:
        source = "title: Quelle\ndescription: Deutsch\n"
        target = "title: Existing English\ntags:\n  - translated-tag\nlocal_note: keep\n"
        merged = merge_source_metadata(target, source)
        self.assertNotIn("tags:", merged)
        self.assertNotIn("local_note:", merged)

    def test_source_owned_metadata_differences_detect_unknown_and_update_drift(self) -> None:
        source = "title: Quelle\ndescription: Deutsch\nupdate: 2026-06-14\ntags:\n  - moc\ncustom: source\n"
        target = "title: Target\ndescription: English\nupdate: 2026-06-13\ntags:\n  - moc\n  - dynamic\ncustom: target\nextra: remove\n"
        self.assertEqual(
            source_owned_metadata_differences(source, target),
            ["custom", "extra", "tags", "update"],
        )

    def test_structural_only_metadata_drift_does_not_require_api_translation(self) -> None:
        source = "title: Quelle\ndescription: Deutsch\nupdate: 2026-06-14\n"
        target = (
            "title: Target\n"
            "description: English\n"
            "update: 2026-06-13\n"
            f"translation_source_metadata_hash: {source_metadata_hash(source)}\n"
        )
        self.assertFalse(needs_localized_metadata_translation(source, target))

    def test_markdown_link_targets_are_restored_without_touching_external_links(self) -> None:
        source = "See [Spiel](spiele/original.md#regeln) and [Site](https://example.org).\n"
        translated = "See [Game](games/translated.md#rules) and [Site](https://example.org).\n"
        result = restore_markdown_link_targets(source, translated)
        self.assertIn("[Game](spiele/original.md#regeln)", result)
        self.assertIn("[Site](https://example.org)", result)

    def test_wikilink_targets_are_restored_but_aliases_stay_translated(self) -> None:
        source = "Siehe [[Spiele/Fangen|Fangen]] und ![[img/original.png]].\n"
        translated = "See [[Games/Tag|Tag]] and ![[img/translated.png]].\n"
        result = restore_wikilink_targets(source, translated)
        self.assertIn("[[Spiele/Fangen|Tag]]", result)
        self.assertIn("![[img/original.png]]", result)

    def test_dynamic_body_hash_ignores_generated_content(self) -> None:
        frontmatter = "tags:\n  - dynamic\n"
        first = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/Spiele-Base.base
view: Liste aller Spiele
-->
<!-- dynamic:content -->
old generated table
<!-- dynamic:end -->
Outro
"""
        second = first.replace("old generated table", "new generated table")
        self.assertEqual(
            translatable_body_hash(frontmatter, first),
            translatable_body_hash(frontmatter, second),
        )

    def test_translate_body_renders_dynamic_blocks_without_sending_them_to_model(self) -> None:
        body = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/Spiele-Base.base
view: Liste aller Spiele
-->
<!-- dynamic:content -->
old generated table
<!-- dynamic:end -->
Outro
"""

        def fake_translate(body: str, **_kwargs: object) -> str:
            self.assertNotIn("old generated table", body)
            self.assertNotIn("dynamic:start", body)
            return body.replace("Intro", "Translated intro").replace("Outro", "Translated outro")

        with (
            patch("translation.body_translation.call_translation_model", side_effect=fake_translate) as translate,
            patch(
                "translation.body_translation.render_block",
                return_value={"ok": True, "index": 0, "markdown": "fresh generated table", "warnings": []},
            ) as render,
        ):
            translated, _link_result, dynamic_results = translate_body(
                source_body=body,
                target_path=ROOT / "docs" / "es" / "Liste aller Spiele.md",
                source_lang="de",
                target_lang="es",
                model="test-model",
                prompt=None,
            )

        self.assertEqual(translate.call_count, 2)
        render.assert_called_once()
        self.assertIn("Translated intro", translated)
        self.assertIn("fresh generated table", translated)
        self.assertIn("Translated outro", translated)
        self.assertIn("<!-- dynamic:end -->", translated)
        self.assertNotIn("old generated table", translated)
        self.assertEqual(len(dynamic_results), 1)

    def test_translate_body_does_not_count_dynamic_table_links_as_repairs(self) -> None:
        body = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/Spiele-Base.base
view: Liste aller Spiele
-->
<!-- dynamic:content -->
| file |
| --- |
| [Spiel A](Spiel%20A.md) |
| [Spiel B](Spiel%20B.md) |
<!-- dynamic:end -->
Outro
"""

        with (
            patch("translation.body_translation.call_translation_model", side_effect=lambda body, **_kwargs: body),
            patch(
                "translation.body_translation.render_block",
                return_value={
                    "ok": True,
                    "index": 0,
                    "markdown": "| file |\n| --- |\n| [Game A](Game%20A.md) |",
                    "warnings": [],
                },
            ),
        ):
            _translated, link_result, _dynamic_results = translate_body(
                source_body=body,
                target_path=ROOT / "docs" / "en" / "Liste aller Spiele.md",
                source_lang="de",
                target_lang="en",
                model="test-model",
                prompt=None,
            )

        self.assertEqual(link_result.repair_count, 0)
        self.assertEqual(link_result.diagnostics, [])

    def test_health_common_page_rules_report_identity_issues(self) -> None:
        page = self.page("en", "machine-translated")
        duplicate = [page, page]
        issues = common_page_issues(page, duplicate, "source.md")

        self.assertEqual(
            issues,
            [
                "duplicate_translation_id_in_language",
                "missing_translation_id",
                "relative_path_mismatch",
            ],
        )

    def test_health_source_page_rules_report_original_metadata_issues(self) -> None:
        page = self.page("de", "machine-translated")

        self.assertEqual(
            source_page_issues(page, "de"),
            ["source_status_not_original", "source_missing_translation_source_lang"],
        )

    def test_health_translated_page_rules_report_hash_and_metadata_issues(self) -> None:
        source = VaultPage(
            path=ROOT / "docs" / "de" / "example.md",
            rel_path="docs/de/example.md",
            language="de",
            relative_path="example.md",
            frontmatter=(
                "lang: de\n"
                "title: Quelle\n"
                "description: Deutsch\n"
                "update: 2026-06-14\n"
                "tags:\n"
                "  - spiel\n"
                "translation_id: example\n"
                "translation_status: original\n"
                "translation_source_lang: de\n"
            ),
            body="Source body",
            has_frontmatter=True,
            translation_id="example",
            translation_status="original",
            translation_source_lang="de",
            translation_source="",
            translation_source_hash="",
            title="Quelle",
        )
        target = VaultPage(
            path=ROOT / "docs" / "en" / "example.md",
            rel_path="docs/en/example.md",
            language="en",
            relative_path="example.md",
            frontmatter=(
                "lang: en\n"
                "title: Source\n"
                "description: English\n"
                "update: 2026-06-13\n"
                "translation_id: example\n"
                "translation_source_lang: pl\n"
                "translation_source_hash: legacy\n"
                "translation_source_metadata_hash: legacy\n"
                "translation_status: missing-translation\n"
            ),
            body="Target body",
            has_frontmatter=True,
            translation_id="example",
            translation_status="missing-translation",
            translation_source_lang="pl",
            translation_source="",
            translation_source_hash="legacy",
            title="Source",
            translation_source_metadata_hash="legacy",
        )

        issues = translated_page_issues(target, source, "de", source_reference_hashes(source))

        self.assertEqual(
            issues,
            [
                "missing_translation_source",
                "missing_translation_source_body_hash",
                "missing_translation_model",
                "missing_translation_updated",
                "translation_source_lang_mismatch",
                "source_body_hash_mismatch",
                "legacy_source_hash",
                "source_localized_metadata_hash_mismatch",
                "legacy_metadata_hash",
                "missing_translation_source_structural_metadata_hash",
                "source_owned_metadata_mismatch",
                "fallback_page",
            ],
        )

    def page(self, language: str, status: str) -> VaultPage:
        return VaultPage(
            path=ROOT / "docs" / language / "example.md",
            rel_path=f"docs/{language}/example.md",
            language=language,
            relative_path="example.md",
            frontmatter=f"lang: {language}\ntranslation_status: {status}\n",
            body="Body",
            has_frontmatter=True,
            translation_id="example",
            translation_status=status,
            translation_source_lang="",
            translation_source="",
            translation_source_hash="",
            title="Example",
        )


if __name__ == "__main__":
    unittest.main()

