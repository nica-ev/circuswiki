from __future__ import annotations

import re
from collections.abc import Iterable


SCALAR_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*):(?P<value>.*)$")


def read_scalar(frontmatter: str, key: str) -> str | None:
    for line in frontmatter.splitlines():
        match = SCALAR_RE.match(line)
        if match and match.group("key") == key:
            return match.group("value").strip().strip('"')
    return None


def set_scalar(frontmatter: str, key: str, value: str) -> str:
    lines = frontmatter.splitlines()
    replacement = f"{key}: {format_scalar(value)}"

    for index, line in enumerate(lines):
        match = SCALAR_RE.match(line)
        if match and match.group("key") == key:
            lines[index] = replacement
            return "\n".join(lines) + "\n"

    if lines and lines[-1].strip():
        lines.append(replacement)
    else:
        lines[-1:] = [replacement]
    return "\n".join(lines) + "\n"


def ensure_scalars(frontmatter: str, values: dict[str, str]) -> str:
    updated = frontmatter
    for key, value in values.items():
        updated = set_scalar(updated, key, value)
    return updated


def frontmatter_blocks(frontmatter: str) -> dict[str, str]:
    """Return top-level YAML blocks keyed by field name, preserving formatting."""
    lines = frontmatter.splitlines()
    blocks: dict[str, list[str]] = {}
    current_key: str | None = None

    for line in lines:
        match = SCALAR_RE.match(line)
        if match and not line.startswith((" ", "\t")):
            current_key = match.group("key")
            blocks[current_key] = [line]
            continue
        if current_key is not None:
            blocks[current_key].append(line)

    return {key: "\n".join(block_lines) for key, block_lines in blocks.items()}


def set_block(frontmatter: str, key: str, block: str) -> str:
    lines = frontmatter.splitlines()
    replacement = block.splitlines()
    output: list[str] = []
    index = 0
    replaced = False

    while index < len(lines):
        line = lines[index]
        match = SCALAR_RE.match(line)
        if match and not line.startswith((" ", "\t")) and match.group("key") == key:
            output.extend(replacement)
            replaced = True
            index += 1
            while index < len(lines):
                next_line = lines[index]
                next_match = SCALAR_RE.match(next_line)
                if next_match and not next_line.startswith((" ", "\t")):
                    break
                index += 1
            continue
        output.append(line)
        index += 1

    if not replaced:
        if output and output[-1].strip():
            output.extend(replacement)
        else:
            output[-1:] = replacement

    return "\n".join(output) + "\n"


def remove_block(frontmatter: str, key: str) -> str:
    lines = frontmatter.splitlines()
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        match = SCALAR_RE.match(line)
        if match and not line.startswith((" ", "\t")) and match.group("key") == key:
            index += 1
            while index < len(lines):
                next_line = lines[index]
                next_match = SCALAR_RE.match(next_line)
                if next_match and not next_line.startswith((" ", "\t")):
                    break
                index += 1
            continue
        output.append(line)
        index += 1

    return "\n".join(output) + ("\n" if output else "")


def missing_scalars(frontmatter: str, keys: Iterable[str]) -> list[str]:
    return [key for key in keys if read_scalar(frontmatter, key) in (None, "")]


def format_scalar(value: str) -> str:
    if value == "":
        return ""
    if any(char in value for char in ['"', "\n"]):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if value.lower() in {"true", "false", "null", "none"}:
        return f'"{value}"'
    if value.startswith((" ", "-", "@", "#")) or value.endswith(" "):
        return f'"{value}"'
    return value
