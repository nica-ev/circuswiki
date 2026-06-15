from __future__ import annotations

from pathlib import Path
from typing import Any

from translation.markdown import join_markdown, split_markdown
from translation.metadata import read_scalar

from .blocks import DynamicBlock, parse_dynamic_blocks, replace_block_contents, sync_block_markers
from .obsidian_backend import query_base
from .paths import DOCS, ROOT, page_language, rel
from .render import render_dynamic
from .scanner import target_paths


def refresh_dynamic_pages(
    path: str = "",
    language: str = "",
    dry_run: bool = True,
    all_languages: bool = False,
) -> dict[str, Any]:
    if all_languages and path:
        raise ValueError("all_languages cannot be combined with a single path")
    if all_languages:
        language = ""
    targets = target_paths(path=path, language=language)
    results = [refresh_dynamic_page(item, dry_run=dry_run) for item in targets]
    return {
        "ok": all(result.get("ok") for result in results),
        "dry_run": dry_run,
        "all_languages": all_languages,
        "total": len(results),
        "changed_count": sum(1 for result in results if result.get("changed")),
        "results": results,
    }


def refresh_dynamic_page(path: Path, dry_run: bool = True) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    document = split_markdown(text)
    body, sync_warnings = sync_dynamic_block_config(document.frontmatter, document.body)
    blocks = parse_dynamic_blocks(document.body)
    if body != document.body:
        document = type(document)(frontmatter=document.frontmatter, body=body, has_frontmatter=document.has_frontmatter)
        blocks = parse_dynamic_blocks(document.body)
    if not blocks:
        return {
            "ok": False,
            "path": rel(path),
            "changed": False,
            "errors": ["No dynamic block found."],
            "blocks": [],
        }

    replacements: dict[int, str] = {}
    block_results: list[dict[str, Any]] = []
    errors: list[str] = []

    for block in blocks:
        block_result = render_block(path, block)
        block_results.append(block_result)
        if block_result["ok"]:
            replacements[block.index] = str(block_result["markdown"])
        else:
            errors.extend(str(error) for error in block_result.get("errors", []))

    if errors:
        return {
            "ok": False,
            "path": rel(path),
            "changed": False,
            "errors": errors,
            "blocks": block_results,
        }

    updated_body = replace_block_contents(document.body, replacements)
    updated_text = join_markdown(document.frontmatter, updated_body) if document.has_frontmatter else updated_body
    changed = updated_text != text.replace("\r\n", "\n")

    if changed and not dry_run:
        path.write_text(updated_text, encoding="utf-8")

    return {
        "ok": True,
        "path": rel(path),
        "changed": changed,
        "dry_run": dry_run,
        "errors": [],
        "warnings": sync_warnings,
        "blocks": block_results,
    }


def sync_dynamic_block_config(frontmatter: str, body: str) -> tuple[str, list[str]]:
    source = read_scalar(frontmatter, "translation_source") or ""
    status = read_scalar(frontmatter, "translation_status") or ""
    if not source or status == "original":
        return body, []

    source_path = (ROOT / source).resolve()
    if not source_path.is_file():
        return body, [f"translation_source not found: {source}"]
    try:
        source_path.relative_to(DOCS.resolve())
    except ValueError:
        return body, [f"translation_source is outside docs: {source}"]

    source_document = split_markdown(source_path.read_text(encoding="utf-8"))
    return sync_block_markers(body, source_document.body)


def render_block(page_path: Path, block: DynamicBlock) -> dict[str, Any]:
    errors = list(block.errors)
    if errors:
        return {
            "ok": False,
            "index": block.index,
            "config": block.config,
            "errors": errors,
        }

    query = query_base(block.config["base"], block.config["view"], language=page_language(page_path))
    if not query["ok"]:
        return {
            "ok": False,
            "index": block.index,
            "config": block.config,
            "command": query.get("command"),
            "stdout": query.get("stdout"),
            "stderr": query.get("stderr"),
            "errors": [query.get("error") or "Obsidian query failed."],
        }

    markdown, warnings = render_dynamic(query["data"], page_path, block.config)
    return {
        "ok": True,
        "index": block.index,
        "config": block.config,
        "command": query.get("command"),
        "warnings": warnings,
        "markdown": markdown,
    }
