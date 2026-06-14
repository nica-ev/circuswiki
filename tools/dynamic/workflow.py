from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from core.languages import language_codes
from translation.markdown import join_markdown, split_markdown
from translation.metadata import read_scalar

from .blocks import DynamicBlock, parse_dynamic_blocks, replace_block_contents, sync_block_markers
from .obsidian_backend import query_base, status as obsidian_status
from .render import render_dynamic

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"


@dataclass(frozen=True)
class DynamicPage:
    path: str
    language: str
    title: str
    tags: list[str]
    block_count: int
    valid_block_count: int
    issues: list[str]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def abs_path(path: str | Path) -> Path:
    source = Path(path)
    if source.is_absolute():
        return source
    return (ROOT / source).resolve()


def scan_dynamic_pages(language: str = "") -> dict[str, Any]:
    pages = [page_summary(path) for path in dynamic_markdown_files(language=language)]
    return {
        "obsidian": obsidian_status(),
        "total": len(pages),
        "pages": [asdict(page) for page in pages],
    }


def check_dynamic_pages(path: str = "", language: str = "") -> dict[str, Any]:
    pages = [page_summary(item) for item in target_paths(path=path, language=language)]
    return {
        "ok": all(not page.issues for page in pages),
        "total": len(pages),
        "pages": [asdict(page) for page in pages],
    }


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
    body, sync_warnings = sync_dynamic_block_config(path, document.frontmatter, document.body)
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


def sync_dynamic_block_config(path: Path, frontmatter: str, body: str) -> tuple[str, list[str]]:
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


def page_summary(path: Path) -> DynamicPage:
    text = path.read_text(encoding="utf-8")
    document = split_markdown(text)
    tags = frontmatter_tags(document.frontmatter)
    blocks = parse_dynamic_blocks(document.body)
    issues: list[str] = []
    if "dynamic" not in tags:
        issues.append("missing dynamic tag")
    if not blocks:
        issues.append("no dynamic block")
    for block in blocks:
        issues.extend(f"block {block.index}: {error}" for error in block.errors)
    return DynamicPage(
        path=rel(path),
        language=page_language(path),
        title=read_scalar(document.frontmatter, "title") or path.stem,
        tags=tags,
        block_count=len(blocks),
        valid_block_count=sum(1 for block in blocks if not block.errors),
        issues=issues,
    )


def target_paths(path: str = "", language: str = "") -> list[Path]:
    if path:
        candidate = abs_path(path)
        if not candidate.exists():
            return []
        return [candidate]
    return dynamic_markdown_files(language=language)


def dynamic_markdown_files(language: str = "") -> list[Path]:
    if language == "all":
        language = ""
    root = DOCS / language if language else DOCS
    if not root.exists():
        return []
    allowed_roots = set(language_codes())
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        language_part = page_language(path)
        if not language and language_part not in allowed_roots:
            continue
        document = split_markdown(path.read_text(encoding="utf-8"))
        if "dynamic" in frontmatter_tags(document.frontmatter):
            files.append(path)
    return files


def frontmatter_tags(frontmatter: str) -> list[str]:
    tags: list[str] = []
    lines = frontmatter.splitlines()
    in_tags = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_tags:
                continue
            continue
        if stripped.startswith("tags:"):
            in_tags = True
            value = stripped.split(":", 1)[1].strip()
            if value.startswith("[") and value.endswith("]"):
                tags.extend(clean_tag(part) for part in value[1:-1].split(","))
            elif value and value not in {"[]", ""}:
                tags.append(clean_tag(value))
            continue
        if in_tags and (line.startswith(" ") or line.startswith("\t")) and stripped.startswith("-"):
            tags.append(clean_tag(stripped[1:]))
            continue
        if in_tags and not line.startswith((" ", "\t")):
            in_tags = False
    return sorted({tag for tag in tags if tag})


def clean_tag(value: str) -> str:
    return value.strip().strip('"\'').lstrip("#")


def page_language(path: Path) -> str:
    try:
        relative = path.resolve().relative_to(DOCS.resolve()).as_posix()
    except ValueError:
        return ""
    parts = relative.split("/")
    return parts[0] if parts else ""
