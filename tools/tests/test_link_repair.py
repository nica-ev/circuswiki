from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from translation.link_repair import repair_link_targets, repair_source_link_styles  # noqa: E402


class LinkRepairTests(unittest.TestCase):
    def test_repairs_markdown_link_targets_inside_tables(self) -> None:
        source = "| Spiel |\n| --- |\n| [Ägyptisches Wurfspiel](<./%C3%84gyptisches%20Wurfspiel.md>) |\n"
        translated = "| Game |\n| --- |\n| [Egyptian Throwing Game](<./Egyptian%20Throwing%20Game.md>) |\n"

        result = repair_link_targets(source, translated)

        self.assertTrue(result.changed)
        self.assertEqual(result.repair_count, 1)
        self.assertIn("[Egyptian Throwing Game](<./%C3%84gyptisches%20Wurfspiel.md>)", result.body)

    def test_repairs_markdown_image_targets_but_keeps_translated_alt_text(self) -> None:
        source = "![Diabolo](../img/diabolo.png)\n"
        translated = "![Diabolo illustration](../images/diabolo-translated.png)\n"

        result = repair_link_targets(source, translated)

        self.assertTrue(result.changed)
        self.assertEqual(result.repair_count, 1)
        self.assertIn("![Diabolo illustration](../img/diabolo.png)", result.body)

    def test_repairs_angle_wrapped_markdown_image_targets(self) -> None:
        source = "![Tuch](<../img/Tuch Jonglage.webp>)\n"
        translated = "![Scarf](<../images/scarf juggling.webp>)\n"

        result = repair_link_targets(source, translated)

        self.assertIn("![Scarf](<../img/Tuch Jonglage.webp>)", result.body)

    def test_does_not_repair_external_image_targets(self) -> None:
        source = "![Logo](https://example.org/source.png)\n"
        translated = "![Logo](https://example.org/translated.png)\n"

        result = repair_link_targets(source, translated)

        self.assertFalse(result.changed)
        self.assertEqual(result.repair_count, 0)
        self.assertIn("https://example.org/translated.png", result.body)

    def test_repairs_markdown_link_targets_inside_callouts(self) -> None:
        source = "> [!tip]\n> Siehe [Fangen](spiele/Fangen.md#regeln).\n"
        translated = "> [!tip]\n> See [Tag](games/Tag.md#rules).\n"

        result = repair_link_targets(source, translated)

        self.assertIn("[Tag](spiele/Fangen.md#regeln)", result.body)

    def test_repairs_loose_obsidian_markdown_link_targets_with_spaces(self) -> None:
        source = "[Nadelöhr](Nadelöhr.md)\n"
        translated = "[Needle's Eye](Needle's Eye.md)\n"

        result = repair_link_targets(source, translated)

        self.assertTrue(result.changed)
        self.assertEqual(result.repair_count, 1)
        self.assertIn("[Needle's Eye](Nadelöhr.md)", result.body)
        self.assertEqual([item.kind for item in result.diagnostics], ["target_repaired"])

    def test_repairs_markdown_link_targets_without_dropping_titles(self) -> None:
        source = '[Nadelöhr](Nadelöhr.md "Quelle")\n'
        translated = '[Needle](Needle.md "Translated title")\n'

        result = repair_link_targets(source, translated)

        self.assertIn('[Needle](Nadelöhr.md "Translated title")', result.body)

    def test_repairs_wikilink_targets_but_keeps_translated_aliases(self) -> None:
        source = "Siehe [[Spiele/Fangen|Fangen]] und ![[img/original.png]].\n"
        translated = "See [[Games/Tag|Tag]] and ![[img/translated.png]].\n"

        result = repair_link_targets(source, translated)

        self.assertIn("[[Spiele/Fangen|Tag]]", result.body)
        self.assertIn("![[img/original.png]]", result.body)

    def test_does_not_repair_links_inside_fenced_code_blocks(self) -> None:
        source = "```md\n[Spiel](original.md)\n```\n[Spiel](real.md)\n"
        translated = "```md\n[Game](translated.md)\n```\n[Game](wrong.md)\n"

        result = repair_link_targets(source, translated)

        self.assertIn("[Game](translated.md)", result.body)
        self.assertIn("[Game](real.md)", result.body)
        self.assertNotIn("[Game](original.md)", result.body)
        self.assertNotIn("[Game](wrong.md)", result.body)

    def test_reports_count_mismatch_without_positional_repair(self) -> None:
        source = "[A](a.md) and [B](b.md)\n"
        translated = "[A](wrong-a.md)\n"

        result = repair_link_targets(source, translated)

        self.assertFalse(result.changed)
        self.assertEqual(result.repair_count, 0)
        self.assertIn("[A](wrong-a.md)", result.body)
        self.assertEqual(result.diagnostics[0].kind, "link_count_mismatch")

    def test_repairs_obsidian_image_embed_to_attr_list_markdown_image(self) -> None:
        source = "Intro\n![[../img/game-photo.jpg|300]]\n"

        result = repair_source_link_styles(source)

        self.assertTrue(result.changed)
        self.assertEqual(result.repair_count, 1)
        self.assertIn("![game-photo](../img/game-photo.jpg){ width=300 }", result.body)
        self.assertEqual(result.diagnostics[0].kind, "obsidian_image_embed")

    def test_repairs_markdown_image_alt_width_to_attr_list_width(self) -> None:
        source = "![Game photo|300](../img/game-photo.jpg)\n"

        result = repair_source_link_styles(source)

        self.assertTrue(result.changed)
        self.assertIn("![Game photo](../img/game-photo.jpg){ width=300 }", result.body)
        self.assertEqual(result.diagnostics[0].kind, "markdown_image_alt_width")

    def test_repairs_markdown_image_alt_width_and_preserves_existing_attrs(self) -> None:
        source = "![Game photo|300](../img/game-photo.jpg){ align=left }\n"

        result = repair_source_link_styles(source)

        self.assertIn("![Game photo](../img/game-photo.jpg){ align=left width=300 }", result.body)

    def test_does_not_repair_source_image_styles_inside_fenced_code(self) -> None:
        source = "```md\n![[../img/game-photo.jpg|300]]\n```\n"

        result = repair_source_link_styles(source)

        self.assertFalse(result.changed)


if __name__ == "__main__":
    unittest.main()
