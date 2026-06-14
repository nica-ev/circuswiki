from __future__ import annotations

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from translation import link_repair_workflow as workflow  # noqa: E402


def note(frontmatter: str, body: str) -> str:
    return f"---\n{textwrap.dedent(frontmatter).strip()}\n---\n{body}"


class LinkRepairWorkflowTests(unittest.TestCase):
    def run_with_vault(self, callback) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            docs = root / "docs"
            docs.mkdir()

            def local_rel(path: Path) -> str:
                return Path(path).resolve().relative_to(root).as_posix()

            with (
                patch.object(workflow, "ROOT", root),
                patch.object(workflow, "DOCS", docs),
                patch.object(workflow, "rel", local_rel),
            ):
                callback(root, docs)

    def test_scan_finds_safe_translated_link_target_repair(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Spiel.md"
            target = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: spiel
                    translation_status: original
                    """,
                    "| Link |\n| --- |\n| [Ziel](<Ziel%20Datei.md>) |\n",
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    translation_source: docs/de/Spiel.md
                    """,
                    "| Link |\n| --- |\n| [Target](<Target%20File.md>) |\n",
                ),
                encoding="utf-8",
            )

            result = workflow.scan_link_repairs("en")

            self.assertEqual(result["total"], 1)
            self.assertEqual(result["safe_count"], 1)
            self.assertEqual(result["items"][0]["path"], "docs/en/Spiel.md")

        self.run_with_vault(scenario)

    def test_repair_link_files_writes_only_body_targets(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Spiel.md"
            target = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: spiel
                    translation_status: original
                    """,
                    "> Siehe [Ziel](Ziel.md)\n",
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    translation_source: docs/de/Spiel.md
                    custom: keep
                    """,
                    "> See [Target](Target.md)\n",
                ),
                encoding="utf-8",
            )

            result = workflow.repair_link_files(["docs/en/Spiel.md"])
            text = target.read_text(encoding="utf-8")

            self.assertEqual(result["repaired_count"], 1)
            self.assertIn("custom: keep", text)
            self.assertIn("> See [Target](Ziel.md)", text)

        self.run_with_vault(scenario)

    def test_count_mismatch_is_reported_but_not_repaired(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Spiel.md"
            target = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: spiel
                    translation_status: original
                    """,
                    "[A](A.md) [B](B.md)\n",
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    translation_source: docs/de/Spiel.md
                    """,
                    "[A](Wrong.md)\n",
                ),
                encoding="utf-8",
            )

            scan = workflow.scan_link_repairs("en")
            result = workflow.repair_link_files(["docs/en/Spiel.md"])

            self.assertEqual(scan["total"], 1)
            self.assertEqual(scan["safe_count"], 0)
            self.assertEqual(result["repaired_count"], 0)
            self.assertIn("[A](Wrong.md)", target.read_text(encoding="utf-8"))

        self.run_with_vault(scenario)

    def test_dynamic_link_labels_are_not_repaired_by_link_workflow(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Liste.md"
            target = docs / "en" / "Liste.md"
            linked = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: liste
                    translation_status: original
                    tags:
                      - dynamic
                    """,
                    dynamic_body("[Spiel](Spiel.md)"),
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: liste
                    translation_status: machine-translated
                    translation_source: docs/de/Liste.md
                    tags:
                      - dynamic
                    """,
                    dynamic_body("[Spiel](Spiel.md)"),
                ),
                encoding="utf-8",
            )
            linked.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    title: Translated Game
                    """,
                    "Body\n",
                ),
                encoding="utf-8",
            )

            scan = workflow.scan_link_repairs("en")
            result = workflow.repair_link_files(["docs/en/Liste.md"])
            text = target.read_text(encoding="utf-8")

            self.assertEqual(scan["total"], 0)
            self.assertEqual(scan["safe_count"], 0)
            self.assertEqual(scan["label_repair_count"], 0)
            self.assertEqual(result["repaired_count"], 0)
            self.assertIn("[Spiel](Spiel.md)", text)

        self.run_with_vault(scenario)

    def test_dynamic_link_label_repair_requires_dynamic_tag(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Liste.md"
            target = docs / "en" / "Liste.md"
            linked = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: liste
                    translation_status: original
                    """,
                    dynamic_body("[Spiel](Spiel.md)"),
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: liste
                    translation_status: machine-translated
                    translation_source: docs/de/Liste.md
                    """,
                    dynamic_body("[Spiel](Spiel.md)"),
                ),
                encoding="utf-8",
            )
            linked.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    title: Translated Game
                    """,
                    "Body\n",
                ),
                encoding="utf-8",
            )

            scan = workflow.scan_link_repairs("en")

            self.assertEqual(scan["total"], 0)

        self.run_with_vault(scenario)

    def test_regenerated_dynamic_links_are_ignored_by_sequence_repair(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Liste.md"
            target = docs / "en" / "Liste.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: liste
                    translation_status: original
                    tags:
                      - dynamic
                    """,
                    dynamic_body("[Spiel A](Spiel%20A.md)\n| [Spiel B](Spiel%20B.md)"),
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: liste
                    translation_status: machine-translated
                    translation_source: docs/de/Liste.md
                    tags:
                      - dynamic
                    """,
                    dynamic_body("[Game A](Game%20A.md)"),
                ),
                encoding="utf-8",
            )

            scan = workflow.scan_link_repairs("en")

            self.assertEqual(scan["total"], 0)

        self.run_with_vault(scenario)

    def test_static_links_are_repaired_while_dynamic_blocks_are_preserved(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Liste.md"
            target = docs / "en" / "Liste.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: liste
                    translation_status: original
                    tags:
                      - dynamic
                    """,
                    "[Intro](Intro.md)\n" + dynamic_body("[Spiel](Spiel.md)"),
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: liste
                    translation_status: machine-translated
                    translation_source: docs/de/Liste.md
                    tags:
                      - dynamic
                    """,
                    "[Intro](Wrong.md)\n" + dynamic_body("[Generated](Generated.md)"),
                ),
                encoding="utf-8",
            )

            result = workflow.repair_link_files(["docs/en/Liste.md"])
            text = target.read_text(encoding="utf-8")

            self.assertEqual(result["repaired_count"], 1)
            self.assertIn("[Intro](Intro.md)", text)
            self.assertIn("[Generated](Generated.md)", text)
            self.assertNotIn("[Spiel](Spiel.md)", text)

        self.run_with_vault(scenario)

    def test_source_link_style_scan_finds_original_image_syntax_repairs(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Spiel.md"
            target = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: spiel
                    translation_status: original
                    """,
                    "![[../img/game-photo.jpg|300]]\n![Other|200](../img/other.jpg)\n",
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    translation_source: docs/de/Spiel.md
                    """,
                    "![[../img/game-photo.jpg|300]]\n",
                ),
                encoding="utf-8",
            )

            scan = workflow.scan_source_link_styles("de")

            self.assertEqual(scan["total"], 1)
            self.assertEqual(scan["safe_count"], 1)
            self.assertEqual(scan["repair_count"], 2)
            self.assertEqual(scan["items"][0]["path"], "docs/de/Spiel.md")

        self.run_with_vault(scenario)

    def test_source_link_style_repair_writes_original_only(self) -> None:
        def scenario(_root: Path, docs: Path) -> None:
            source = docs / "de" / "Spiel.md"
            target = docs / "en" / "Spiel.md"
            source.parent.mkdir()
            target.parent.mkdir()
            source.write_text(
                note(
                    """
                    lang: de
                    translation_id: spiel
                    translation_status: original
                    """,
                    "![[../img/game-photo.jpg|300]]\n",
                ),
                encoding="utf-8",
            )
            target.write_text(
                note(
                    """
                    lang: en
                    translation_id: spiel
                    translation_status: machine-translated
                    translation_source: docs/de/Spiel.md
                    """,
                    "![[../img/game-photo.jpg|300]]\n",
                ),
                encoding="utf-8",
            )

            result = workflow.repair_source_link_style_files(["docs/de/Spiel.md", "docs/en/Spiel.md"])

            self.assertEqual(result["repaired_count"], 1)
            self.assertEqual(result["skipped_count"], 1)
            self.assertIn("![game-photo](../img/game-photo.jpg){ width=300 }", source.read_text(encoding="utf-8"))
            self.assertIn("![[../img/game-photo.jpg|300]]", target.read_text(encoding="utf-8"))

        self.run_with_vault(scenario)


def dynamic_body(link: str) -> str:
    return textwrap.dedent(
        f"""
        <!-- dynamic:start
        engine: obsidian-base
        base: _bases/Test.base
        view: Test
        -->
        <!-- dynamic:content -->
        | file |
        | --- |
        | {link} |

        <!-- dynamic:end -->
        """
    ).lstrip()


if __name__ == "__main__":
    unittest.main()
