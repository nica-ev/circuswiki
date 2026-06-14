from __future__ import annotations

from dataclasses import dataclass

START_MARKER = "<!-- dynamic:start"
CONTENT_MARKER = "<!-- dynamic:content -->"
END_MARKER = "<!-- dynamic:end -->"


@dataclass(frozen=True)
class DynamicBlock:
    index: int
    start: int
    content_start: int
    content_end: int
    end: int
    marker_text: str
    config_text: str
    config: dict[str, str]

    @property
    def errors(self) -> list[str]:
        errors: list[str] = []
        if self.config.get("engine") != "obsidian-base":
            errors.append("engine must be obsidian-base")
        if not self.config.get("base"):
            errors.append("missing base")
        if not self.config.get("view"):
            errors.append("missing view")
        if self.config.get("columns"):
            errors.append("columns is not supported; configure columns in the Obsidian Base view")
        return errors


def parse_dynamic_blocks(text: str) -> list[DynamicBlock]:
    blocks: list[DynamicBlock] = []
    cursor = 0

    while True:
        start = text.find(START_MARKER, cursor)
        if start == -1:
            return blocks

        start_close = text.find("-->", start)
        if start_close == -1:
            return blocks

        content_marker_start = text.find(CONTENT_MARKER, start_close + 3)
        if content_marker_start == -1:
            cursor = start_close + 3
            continue

        content_start = content_marker_start + len(CONTENT_MARKER)
        if content_start < len(text) and text[content_start:content_start + 2] == "\r\n":
            content_start += 2
        elif content_start < len(text) and text[content_start] == "\n":
            content_start += 1

        end_marker_start = text.find(END_MARKER, content_start)
        if end_marker_start == -1:
            cursor = content_start
            continue

        marker_text = text[start:start_close + 3]
        config_text = marker_text[len(START_MARKER): -3].strip()
        block = DynamicBlock(
            index=len(blocks),
            start=start,
            content_start=content_start,
            content_end=end_marker_start,
            end=end_marker_start + len(END_MARKER),
            marker_text=marker_text,
            config_text=config_text,
            config=parse_block_config(config_text),
        )
        blocks.append(block)
        cursor = block.end


def parse_block_config(text: str) -> dict[str, str]:
    config: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().replace("_", "-")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        config[key] = value
    return config


def replace_block_contents(text: str, replacements: dict[int, str]) -> str:
    blocks = parse_dynamic_blocks(text)
    if not replacements:
        return text

    pieces: list[str] = []
    cursor = 0
    for block in blocks:
        pieces.append(text[cursor:block.content_start])
        if block.index in replacements:
            replacement = replacements[block.index].strip("\n")
            pieces.append(replacement)
            pieces.append("\n\n")
        else:
            pieces.append(text[block.content_start:block.content_end])
        cursor = block.content_end
    pieces.append(text[cursor:])
    return "".join(pieces)


def sync_block_markers(text: str, source_text: str) -> tuple[str, list[str]]:
    blocks = parse_dynamic_blocks(text)
    source_blocks = parse_dynamic_blocks(source_text)
    warnings: list[str] = []
    if not blocks or not source_blocks:
        return text, warnings
    if len(blocks) != len(source_blocks):
        warnings.append(f"dynamic block count differs from source: target {len(blocks)}, source {len(source_blocks)}")
        return text, warnings

    pieces: list[str] = []
    cursor = 0
    for block, source_block in zip(blocks, source_blocks):
        pieces.append(text[cursor:block.start])
        pieces.append(source_block.marker_text)
        pieces.append(text[block.start + len(block.marker_text):block.content_start])
        cursor = block.content_start
    pieces.append(text[cursor:])
    return "".join(pieces), warnings
