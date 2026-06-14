from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from dynamic.blocks import parse_dynamic_blocks, replace_block_contents, sync_block_markers  # noqa: E402
from dynamic.obsidian_backend import materialize_language_base  # noqa: E402
from dynamic.render import markdown_href, render_dynamic, render_table  # noqa: E402
from dynamic import workflow  # noqa: E402
from dynamic.workflow import frontmatter_tags  # noqa: E402


class DynamicWorkflowTests(unittest.TestCase):
    def test_parse_and_replace_dynamic_block_content_only(self) -> None:
        body = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/games.base
view: Fangspiele
-->
<!-- dynamic:content -->
old table
<!-- dynamic:end -->
Outro
"""
        blocks = parse_dynamic_blocks(body)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].config["engine"], "obsidian-base")
        self.assertEqual(blocks[0].config["base"], "_bases/games.base")
        self.assertEqual(blocks[0].config["view"], "Fangspiele")

        replaced = replace_block_contents(body, {0: "new table"})
        self.assertIn("Intro", replaced)
        self.assertIn("new table", replaced)
        self.assertNotIn("old table", replaced)
        self.assertIn("Outro", replaced)

    def test_frontmatter_tags_support_yaml_list_and_inline_list(self) -> None:
        self.assertIn("dynamic", frontmatter_tags("tags:\n  - spiele\n  - dynamic\n"))
        self.assertIn("dynamic", frontmatter_tags("tags: [spiele, #dynamic]\n"))

    def test_render_table_does_not_filter_language_by_default(self) -> None:
        page_path = ROOT / "docs" / "de" / "Fangspiele.md"
        markdown, warnings = render_table(
            [
                {"path": "docs/de/Alaska Baseball.md", "Link": "[[docs/de/Alaska Baseball.md|Alaska Baseball]]", "group-min": 30},
                {"path": "docs/en/Alaska Baseball.md", "Link": "[[docs/en/Alaska Baseball.md|Alaska Baseball]]", "group-min": 30},
            ],
            page_path,
            {},
        )
        self.assertIn("[Alaska Baseball](<Alaska%20Baseball.md>)", markdown)
        self.assertIn("[Alaska Baseball](<../en/Alaska%20Baseball.md>)", markdown)
        self.assertEqual(warnings, [])

    def test_render_table_filters_current_language_when_explicit(self) -> None:
        page_path = ROOT / "docs" / "de" / "Fangspiele.md"
        markdown, warnings = render_table(
            [
                {"path": "docs/de/Alaska Baseball.md", "Link": "[[docs/de/Alaska Baseball.md|Alaska Baseball]]", "group-min": 30},
                {"path": "docs/en/Alaska Baseball.md", "Link": "[[docs/en/Alaska Baseball.md|Alaska Baseball]]", "group-min": 30},
            ],
            page_path,
            {"language": "current"},
        )
        self.assertIn("[Alaska Baseball](<Alaska%20Baseball.md>)", markdown)
        self.assertNotIn("../en", markdown)
        self.assertEqual(warnings, ["language filter kept 1/2 rows for de"])

    def test_markdown_href_is_relative_to_current_page(self) -> None:
        page_path = ROOT / "docs" / "de" / "spiele" / "Index.md"
        href = markdown_href("docs/de/Alaska Baseball.md", page_path)
        self.assertEqual(href, "../Alaska%20Baseball.md")

    def test_markdown_href_does_not_start_with_percent_encoded_character(self) -> None:
        page_path = ROOT / "docs" / "de" / "Liste aller Spiele.md"
        href = markdown_href("docs/de/Ägyptisches Wurfspiel.md", page_path)
        self.assertEqual(href, "./%C3%84gyptisches%20Wurfspiel.md")

    def test_render_dynamic_supports_list_format(self) -> None:
        page_path = ROOT / "docs" / "de" / "Kaskade Workspace.md"
        markdown, warnings = render_dynamic(
            [
                {"file": "docs/de/Kaskade 001.md", "title": "Kaskade 001"},
                {"file": "docs/de/Kaskade 002.md", "title": "Kaskade 002"},
            ],
            page_path,
            {"format": "list"},
        )
        self.assertIn("edit the dynamic block config, not this list", markdown)
        self.assertIn("- [Kaskade 001](<Kaskade%20001.md>)", markdown)
        self.assertIn("- [Kaskade 002](<Kaskade%20002.md>)", markdown)
        self.assertEqual(warnings, [])

    def test_render_dynamic_warns_and_falls_back_to_table_for_unknown_format(self) -> None:
        page_path = ROOT / "docs" / "de" / "Fangspiele.md"
        markdown, warnings = render_dynamic(
            [{"file": "docs/de/Alaska Baseball.md", "group-min": 30}],
            page_path,
            {"format": "cards"},
        )
        self.assertIn("group-min |", markdown)
        self.assertNotIn("| file", markdown)
        self.assertEqual(warnings, ["unsupported format cards; rendered table"])

    def test_render_dynamic_pads_table_rows_consistently(self) -> None:
        page_path = ROOT / "docs" / "de" / "Fangspiele.md"
        markdown, _warnings = render_dynamic(
            [
                {"file": "docs/de/A.md", "Material": "x"},
                {"file": "docs/de/Long File Name.md", "Material": "longer value"},
            ],
            page_path,
            {"format": "table"},
        )
        lines = [line for line in markdown.splitlines() if line.startswith("|")]
        self.assertEqual(len(lines), 4)
        self.assertTrue(all(len(line) == len(lines[0]) for line in lines), lines)

    def test_render_dynamic_link_column_uses_obsidian_link_alias_case_insensitively(self) -> None:
        page_path = ROOT / "docs" / "cs" / "Fangspiele.md"
        markdown, warnings = render_dynamic(
            [
                {
                    "path": "docs/cs/Bombenspiel.md",
                    "Link": "[[docs/cs/Bombenspiel.md|Bombová hra]]",
                    "group-min": 8,
                }
            ],
            page_path,
            {"format": "table"},
        )
        self.assertIn("[Bombová hra](<Bombenspiel.md>)", markdown)
        self.assertNotIn("[[docs/cs/Bombenspiel.md|Bombová hra]]", markdown)
        self.assertEqual(warnings, [])

    def test_inferred_columns_hide_technical_identity_fields(self) -> None:
        page_path = ROOT / "docs" / "de" / "Aufwärmspiele MOC.md"
        markdown, warnings = render_dynamic(
            [
                {
                    "path": "docs/de/Alaska Baseball.md",
                    "file": "docs/de/Alaska Baseball.md",
                    "Link": "[[docs/de/Alaska Baseball.md|Alaska Baseball]]",
                    "Spieler Min": "30",
                }
            ],
            page_path,
            {"format": "table"},
        )
        header = next(line for line in markdown.splitlines() if line.startswith("|"))
        self.assertNotIn("file", header)
        self.assertNotIn("path", header)
        self.assertIn("Link", header)
        self.assertIn("Spieler Min", header)
        self.assertEqual(warnings, [])

    def test_inferred_localized_base_display_names_render_links_and_values(self) -> None:
        page_path = ROOT / "docs" / "it" / "convention-games.md"
        with patch(
            "dynamic.render.labels_for_language",
            return_value={
                "formula.link-title": "Collegamento",
                "note.group-min": "Giocatori Min",
                "note.group-max": "Giocatori Max",
                "note.Schwierigkeit": "Difficoltà",
                "note.Material": "Materiale",
                "note.Spieldauer": "Durata",
            },
        ):
            markdown, warnings = render_dynamic(
                [
                    {
                        "path": "docs/it/3-ball-piggyback-gladiators.md",
                        "Collegamento": "[[docs/it/3-ball-piggyback-gladiators.md|Gladiatori Piggyback a 3 Palle]]",
                        "category": "convention-games",
                        "Giocatori Min": "4",
                        "Giocatori Max": "30",
                        "Difficoltà": "difficile",
                        "Materiale": "Tre palle",
                        "Durata": "5-10",
                    }
                ],
                page_path,
                {
                    "format": "table",
                    "base": "_bases/Spiele-Base.base",
                    "view": "Convention-Games",
                },
            )
        header = next(line for line in markdown.splitlines() if line.startswith("|"))
        self.assertIn("Collegamento", header)
        self.assertIn("Giocatori Min", header)
        self.assertIn("category", header)
        self.assertIn("[Gladiatori Piggyback a 3 Palle](<3-ball-piggyback-gladiators.md>)", markdown)
        self.assertIn("Tre palle", markdown)
        self.assertEqual(warnings, [])

    def test_columns_config_is_invalid(self) -> None:
        body = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/games.base
view: Fangspiele
columns: file
-->
<!-- dynamic:content -->
table
<!-- dynamic:end -->
"""
        block = parse_dynamic_blocks(body)[0]
        self.assertIn("columns is not supported; configure columns in the Obsidian Base view", block.errors)

    def test_materialize_language_base_rewrites_only_language_filters(self) -> None:
        generated = ROOT / materialize_language_base("_bases/Resourcen.base", "es")
        text = generated.read_text(encoding="utf-8")
        self.assertIn('lang == "es"', text)
        self.assertIn("type == \"Tutorial\"", text)

    def test_sync_block_markers_copies_source_config_and_preserves_content(self) -> None:
        source = """Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/Spiele-Base.base
view: Fangspiele
format: table
-->
<!-- dynamic:content -->
source table
<!-- dynamic:end -->
"""
        target = source.replace("format: table", "format: table\ncolumns: file, group-min").replace("source table", "target table")

        synced, warnings = sync_block_markers(target, source)

        self.assertEqual(warnings, [])
        self.assertNotIn("columns: file, group-min", synced)
        self.assertNotIn("columns:", synced)
        self.assertIn("target table", synced)

    def test_refresh_dynamic_page_syncs_config_from_translation_source_before_rendering(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            docs = root / "docs"
            source = docs / "de" / "Fangspiele.md"
            target = docs / "cs" / "Fangspiele.md"
            source.parent.mkdir(parents=True)
            target.parent.mkdir(parents=True)
            source.write_text(
                "---\nlang: de\ntranslation_status: original\n---\n"
                + dynamic_body("source table"),
                encoding="utf-8",
            )
            target.write_text(
                "---\nlang: cs\ntranslation_status: machine-translated\ntranslation_source: docs/de/Fangspiele.md\n---\n"
                + dynamic_body("old target table", columns="file, group-min"),
                encoding="utf-8",
            )

            def fake_render(_path, block):
                self.assertNotIn("columns", block.config)
                return {"ok": True, "index": block.index, "config": block.config, "markdown": "new target table"}

            with (
                patch.object(workflow, "ROOT", root),
                patch.object(workflow, "DOCS", docs),
                patch.object(workflow, "render_block", side_effect=fake_render),
            ):
                result = workflow.refresh_dynamic_page(target, dry_run=False)

            text = target.read_text(encoding="utf-8")
            self.assertTrue(result["ok"])
            self.assertTrue(result["changed"])
            self.assertNotIn("columns:", text)
            self.assertIn("new target table", text)

def dynamic_body(content: str, columns: str = "") -> str:
    columns_line = f"columns: {columns}\n" if columns else ""
    return f"""Intro
<!-- dynamic:start
engine: obsidian-base
base: _bases/Spiele-Base.base
view: Fangspiele
format: table
{columns_line}\
-->
<!-- dynamic:content -->
{content}
<!-- dynamic:end -->
"""


if __name__ == "__main__":
    unittest.main()
