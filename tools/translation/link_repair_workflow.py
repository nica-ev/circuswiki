from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from dynamic.blocks import parse_dynamic_blocks
from translation.link_repair import LinkRepairResult, repair_link_targets
from translation.link_repair import repair_source_link_styles
from translation.markdown import join_markdown, split_markdown
from translation.metadata import read_scalar
from translation.workflow import DOCS, ROOT, rel


@dataclass(frozen=True)
class LinkRepairItem:
    path: str
    language: str
    translation_id: str
    status: str
    source: str
    source_exists: bool
    repair_count: int
    label_repair_count: int
    diagnostic_count: int
    safe_repair: bool
    reasons: list[str]


@dataclass(frozen=True)
class SourceLinkStyleItem:
    path: str
    language: str
    translation_id: str
    status: str
    repair_count: int
    diagnostic_count: int
    safe_repair: bool
    reasons: list[str]


def scan_link_repairs(language: str = "") -> dict[str, Any]:
    items = link_repair_items(language)
    return {
        "ok": True,
        "total": len(items),
        "safe_count": sum(1 for item in items if item.safe_repair),
        "repair_count": sum(item.repair_count for item in items),
        "label_repair_count": sum(item.label_repair_count for item in items),
        "items": [asdict(item) for item in items],
    }


def scan_source_link_styles(language: str = "") -> dict[str, Any]:
    items = source_link_style_items(language)
    return {
        "ok": True,
        "total": len(items),
        "safe_count": sum(1 for item in items if item.safe_repair),
        "repair_count": sum(item.repair_count for item in items),
        "items": [asdict(item) for item in items],
    }


def preview_source_link_style(path: str) -> dict[str, Any]:
    target = normalize_docs_markdown_path(path)
    document, result = source_link_style_context(target)
    return {
        "ok": True,
        "path": rel(target),
        "safe_repair": is_safe_source_style_repair(result),
        "repair_count": result.repair_count,
        "diagnostics": [asdict(item) for item in result.diagnostics],
        "current_body": document.body,
        "repaired_body": result.body,
    }


def repair_source_link_style_files(paths: list[str]) -> dict[str, Any]:
    repaired: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    for raw_path in paths:
        try:
            target = normalize_docs_markdown_path(raw_path)
            document, result = source_link_style_context(target)
        except Exception as exc:
            skipped.append({"path": str(raw_path), "reason": str(exc)})
            continue

        if not is_safe_source_style_repair(result):
            skipped.append(
                {
                    "path": rel(target),
                    "reason": "not_safe_repair",
                    "repair_count": result.repair_count,
                    "diagnostics": [asdict(item) for item in result.diagnostics],
                }
            )
            continue

        target.write_text(join_markdown(document.frontmatter, result.body), encoding="utf-8", newline="\n")
        repaired.append({"path": rel(target), "repair_count": result.repair_count})

    return {
        "ok": not skipped,
        "requested_count": len(paths),
        "repaired_count": len(repaired),
        "skipped_count": len(skipped),
        "repaired": repaired,
        "skipped": skipped,
    }


def repair_all_safe_source_link_styles(language: str = "") -> dict[str, Any]:
    paths = [item.path for item in source_link_style_items(language) if item.safe_repair]
    return repair_source_link_style_files(paths)


def preview_link_repair(path: str) -> dict[str, Any]:
    target = normalize_docs_markdown_path(path)
    source, document, result = repair_context(target)
    return {
        "ok": True,
        "path": rel(target),
        "source": rel(source),
        "safe_repair": is_safe_repair(result),
        "repair_count": result.repair_count,
        "label_repair_count": dynamic_label_repair_count(result),
        "diagnostics": [asdict(item) for item in result.diagnostics],
        "current_body": document.body,
        "repaired_body": result.body,
    }


def repair_link_files(paths: list[str]) -> dict[str, Any]:
    repaired: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    for raw_path in paths:
        try:
            target = normalize_docs_markdown_path(raw_path)
            source, document, result = repair_context(target)
        except Exception as exc:
            skipped.append({"path": str(raw_path), "reason": str(exc)})
            continue

        if not is_safe_repair(result):
            skipped.append(
                {
                    "path": rel(target),
                    "reason": "not_safe_repair",
                    "repair_count": result.repair_count,
                    "diagnostics": [asdict(item) for item in result.diagnostics],
                }
            )
            continue

        target.write_text(join_markdown(document.frontmatter, result.body), encoding="utf-8", newline="\n")
        repaired.append(
            {
                "path": rel(target),
                "source": rel(source),
                "repair_count": result.repair_count,
                "label_repair_count": dynamic_label_repair_count(result),
            }
        )

    return {
        "ok": not skipped,
        "requested_count": len(paths),
        "repaired_count": len(repaired),
        "skipped_count": len(skipped),
        "repaired": repaired,
        "skipped": skipped,
    }


def repair_all_safe_link_files(language: str = "") -> dict[str, Any]:
    paths = [item.path for item in link_repair_items(language) if item.safe_repair]
    return repair_link_files(paths)


def link_repair_items(language: str = "") -> list[LinkRepairItem]:
    items: list[LinkRepairItem] = []
    if not DOCS.exists():
        return items

    roots = [DOCS / language] if language else [path for path in DOCS.iterdir() if path.is_dir()]
    for root in roots:
        if not root.exists() or root.name == "img":
            continue
        for path in sorted(root.rglob("*.md")):
            item = inspect_link_repair_file(path)
            if item:
                items.append(item)
    return items


def source_link_style_items(language: str = "") -> list[SourceLinkStyleItem]:
    items: list[SourceLinkStyleItem] = []
    if not DOCS.exists():
        return items

    roots = [DOCS / language] if language else [path for path in DOCS.iterdir() if path.is_dir()]
    for root in roots:
        if not root.exists() or root.name == "img":
            continue
        for path in sorted(root.rglob("*.md")):
            item = inspect_source_link_style_file(path)
            if item:
                items.append(item)
    return items


def inspect_source_link_style_file(path: Path) -> SourceLinkStyleItem | None:
    if not safe_docs_markdown_path(path):
        return None

    document = split_markdown(path.read_text(encoding="utf-8"))
    if not document.has_frontmatter:
        return None

    status = read_scalar(document.frontmatter, "translation_status") or ""
    if status != "original":
        return None

    result = repair_source_link_styles(document.body)
    reasons = sorted({item.kind for item in result.diagnostics})
    if not result.repair_count and not reasons:
        return None

    language = path.relative_to(DOCS).parts[0]
    return SourceLinkStyleItem(
        path=rel(path),
        language=language,
        translation_id=read_scalar(document.frontmatter, "translation_id") or "",
        status=status,
        repair_count=result.repair_count,
        diagnostic_count=len(result.diagnostics),
        safe_repair=is_safe_source_style_repair(result),
        reasons=reasons,
    )


def inspect_link_repair_file(path: Path) -> LinkRepairItem | None:
    if not safe_docs_markdown_path(path):
        return None

    document = split_markdown(path.read_text(encoding="utf-8"))
    if not document.has_frontmatter:
        return None

    status = read_scalar(document.frontmatter, "translation_status") or ""
    if status == "original":
        return None

    source = read_scalar(document.frontmatter, "translation_source") or ""
    if not source:
        return None

    language = path.relative_to(DOCS).parts[0]
    translation_id = read_scalar(document.frontmatter, "translation_id") or ""
    source_path = (ROOT / source).resolve()
    source_exists = source_path.is_file()
    if not source_exists:
        return LinkRepairItem(
            path=rel(path),
            language=language,
            translation_id=translation_id,
            status=status,
            source=source,
            source_exists=False,
            repair_count=0,
            label_repair_count=0,
            diagnostic_count=1,
            safe_repair=False,
            reasons=["missing_translation_source_file"],
        )

    if not safe_docs_markdown_path(source_path):
        return None

    source_document = split_markdown(source_path.read_text(encoding="utf-8"))
    result = combined_link_repair(path, document.frontmatter, source_document.body, document.body)
    reasons = sorted({item.kind for item in result.diagnostics})
    if not result.repair_count and not reasons:
        return None

    return LinkRepairItem(
        path=rel(path),
        language=language,
        translation_id=translation_id,
        status=status,
        source=source,
        source_exists=True,
        repair_count=result.repair_count,
        label_repair_count=dynamic_label_repair_count(result),
        diagnostic_count=len(result.diagnostics),
        safe_repair=is_safe_repair(result),
        reasons=reasons,
    )


def repair_context(path: Path) -> tuple[Path, Any, LinkRepairResult]:
    if not safe_docs_markdown_path(path):
        raise ValueError("Path is not a Markdown file under docs/<lang>/")

    document = split_markdown(path.read_text(encoding="utf-8"))
    if not document.has_frontmatter:
        raise ValueError("File has no frontmatter")
    if read_scalar(document.frontmatter, "translation_status") == "original":
        raise ValueError("Original files are not repaired by this tool")

    source = read_scalar(document.frontmatter, "translation_source") or ""
    if not source:
        raise ValueError("File has no translation_source")

    source_path = (ROOT / source).resolve()
    if not source_path.is_file():
        raise ValueError("translation_source points to a missing file")
    if not safe_docs_markdown_path(source_path):
        raise ValueError("translation_source is not under docs/<lang>/")

    source_document = split_markdown(source_path.read_text(encoding="utf-8"))
    return source_path, document, combined_link_repair(path, document.frontmatter, source_document.body, document.body)


def source_link_style_context(path: Path) -> tuple[Any, LinkRepairResult]:
    if not safe_docs_markdown_path(path):
        raise ValueError("Path is not a Markdown file under docs/<lang>/")

    document = split_markdown(path.read_text(encoding="utf-8"))
    if not document.has_frontmatter:
        raise ValueError("File has no frontmatter")
    if read_scalar(document.frontmatter, "translation_status") != "original":
        raise ValueError("Only original source files are repaired by source link style repair")

    return document, repair_source_link_styles(document.body)


def combined_link_repair(
    target_path: Path,
    target_frontmatter: str,
    source_body: str,
    target_body: str,
) -> LinkRepairResult:
    return repair_link_targets_preserving_dynamic(source_body, target_body)


def repair_link_targets_preserving_dynamic(source_body: str, target_body: str) -> LinkRepairResult:
    source_blocks = parse_dynamic_blocks(source_body)
    target_blocks = parse_dynamic_blocks(target_body)
    if not source_blocks and not target_blocks:
        return repair_link_targets(source_body, target_body)
    if len(source_blocks) != len(target_blocks):
        return repair_link_targets(body_without_dynamic_content(source_body), body_without_dynamic_content(target_body))

    pieces: list[str] = []
    source_cursor = 0
    target_cursor = 0
    diagnostics = []
    repair_count = 0

    for source_block, target_block in zip(source_blocks, target_blocks):
        segment_result = repair_link_targets(
            source_body[source_cursor:source_block.start],
            target_body[target_cursor:target_block.start],
        )
        pieces.append(segment_result.body)
        pieces.append(target_body[target_block.start:target_block.end])
        diagnostics.extend(segment_result.diagnostics)
        repair_count += segment_result.repair_count
        source_cursor = source_block.end
        target_cursor = target_block.end

    tail_result = repair_link_targets(source_body[source_cursor:], target_body[target_cursor:])
    pieces.append(tail_result.body)
    diagnostics.extend(tail_result.diagnostics)
    repair_count += tail_result.repair_count

    repaired = "".join(pieces)
    return LinkRepairResult(
        body=repaired,
        changed=repaired != target_body,
        repair_count=repair_count,
        diagnostics=diagnostics,
    )


def body_without_dynamic_content(body: str) -> str:
    blocks = parse_dynamic_blocks(body)
    if not blocks:
        return body

    pieces: list[str] = []
    cursor = 0
    for block in blocks:
        pieces.append(body[cursor:block.content_start])
        pieces.append("\n")
        pieces.append(body[block.content_end:block.end])
        cursor = block.end
    pieces.append(body[cursor:])
    return "".join(pieces)


def dynamic_label_repair_count(result: LinkRepairResult) -> int:
    return sum(1 for item in result.diagnostics if item.kind == "dynamic_label_repaired")


def is_safe_repair(result: LinkRepairResult) -> bool:
    return result.repair_count > 0 and not any(item.kind == "link_count_mismatch" for item in result.diagnostics)


def is_safe_source_style_repair(result: LinkRepairResult) -> bool:
    return result.repair_count > 0 and all(
        item.link_type == "source_image_style" for item in result.diagnostics
    )


def normalize_docs_markdown_path(path: str) -> Path:
    target = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    if not safe_docs_markdown_path(target):
        raise ValueError("Path is not a Markdown file under docs/<lang>/")
    return target


def safe_docs_markdown_path(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(DOCS.resolve())
    except ValueError:
        return False
    return len(relative.parts) >= 2 and path.suffix.lower() == ".md"
