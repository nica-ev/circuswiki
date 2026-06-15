from __future__ import annotations

from dynamic.blocks import DynamicBlock, parse_dynamic_blocks


def frontmatter_tags(frontmatter: str) -> list[str]:
    tags: list[str] = []
    lines = frontmatter.splitlines()
    in_tags = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("tags:"):
            in_tags = True
            value = stripped.split(":", 1)[1].strip()
            if value.startswith("[") and value.endswith("]"):
                tags.extend(clean_tag(part) for part in value[1:-1].split(","))
            elif value and value != "[]":
                tags.append(clean_tag(value))
            continue
        if in_tags and line.startswith((" ", "\t")) and stripped.startswith("-"):
            tags.append(clean_tag(stripped[1:]))
            continue
        if in_tags and stripped and not line.startswith((" ", "\t")):
            in_tags = False
    return sorted({tag for tag in tags if tag})


def clean_tag(value: str) -> str:
    return value.strip().strip('"\'').lstrip("#")


def static_body_segments(body: str, blocks: list[DynamicBlock] | None = None) -> list[str]:
    blocks = parse_dynamic_blocks(body) if blocks is None else blocks
    if not blocks:
        return [body]

    segments: list[str] = []
    cursor = 0
    for block in blocks:
        segments.append(body[cursor:block.start])
        cursor = block.end
    segments.append(body[cursor:])
    return segments
