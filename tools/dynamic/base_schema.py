from __future__ import annotations

from pathlib import Path
from typing import Any

from base_labels import extract_display_names, labels_for_language, unquote_yaml_scalar

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"


def base_view_columns(config: dict[str, str], page_path: Path, rows: list[dict[str, Any]]) -> list[str]:
    base = config.get("base", "").strip()
    view = config.get("view", "").strip()
    if not base or not view or not rows:
        return []
    base_path = (ROOT / base).resolve()
    try:
        base_path.relative_to(ROOT.resolve())
    except ValueError:
        return []
    if not base_path.is_file():
        return []

    order = base_view_order(base_path, view)
    if not order:
        return []

    language = page_language(page_path)
    try:
        localized_labels = labels_for_language(base_path, language) if language else {}
    except (OSError, ValueError, KeyError):
        localized_labels = {}
    try:
        source_labels = extract_display_names(base_path.read_text(encoding="utf-8"))
    except OSError:
        source_labels = {}

    columns: list[str] = []
    for property_name in order:
        column = resolve_base_property_column(property_name, rows, localized_labels, source_labels)
        if column and column not in columns:
            columns.append(column)
    return columns


def base_view_order(base_path: Path, view_name: str) -> list[str]:
    try:
        lines = base_path.read_text(encoding="utf-8-sig").splitlines()
    except OSError:
        return []
    for block in view_blocks(lines):
        if view_block_name(block) == view_name:
            return view_block_order(block)
    return []


def view_blocks(lines: list[str]) -> list[list[str]]:
    blocks: list[list[str]] = []
    in_views = False
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == "views:":
            in_views = True
            continue
        if not in_views:
            continue
        if stripped and not line.startswith((" ", "\t")):
            break
        if line.startswith("  - "):
            if current:
                blocks.append(current)
            current = [line]
            continue
        if current:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def view_block_name(block: list[str]) -> str:
    for line in block:
        stripped = line.strip()
        if stripped.startswith("name:"):
            return unquote_yaml_scalar(stripped.split(":", 1)[1])
    return ""


def view_block_order(block: list[str]) -> list[str]:
    order: list[str] = []
    order_indent: int | None = None
    for line in block:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if order_indent is None:
            if stripped == "order:":
                order_indent = indent
            continue
        if not stripped:
            continue
        if indent <= order_indent:
            break
        if stripped.startswith("- "):
            order.append(unquote_yaml_scalar(stripped[2:]))
    return order


def resolve_base_property_column(
    property_name: str,
    rows: list[dict[str, Any]],
    localized_labels: dict[str, str],
    source_labels: dict[str, str],
) -> str:
    property_key = base_property_key(property_name)
    candidates = [
        property_name,
        property_key,
        property_name.removeprefix("formula."),
        property_name.removeprefix("file."),
        localized_labels.get(property_key, ""),
        source_labels.get(property_key, ""),
    ]
    if property_name == "file.name":
        candidates.extend(["file", "path", "name", "basename"])
    for candidate in candidates:
        column = resolve_row_column(candidate, rows)
        if column:
            return column
    return ""


def base_property_key(property_name: str) -> str:
    if property_name.startswith(("formula.", "note.", "file.")):
        return property_name
    return f"note.{property_name}"


def resolve_row_column(candidate: str, rows: list[dict[str, Any]]) -> str:
    candidate = candidate.strip()
    if not candidate:
        return ""
    candidate_lower = candidate.lower()
    for row in rows:
        for key in row:
            if key.lower() == candidate_lower:
                return key
    return ""


def page_language(path: Path) -> str:
    try:
        relative = path.resolve().relative_to(DOCS.resolve()).as_posix()
    except ValueError:
        return ""
    parts = relative.split("/")
    return parts[0] if parts else ""
