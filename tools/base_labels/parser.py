from __future__ import annotations

import json
import re

TOP_LEVEL_RE = re.compile(r"^[A-Za-z0-9_.-]+:\s*(?:#.*)?$")
PROPERTY_KEY_RE = re.compile(r"^(?P<indent>\s{2})(?P<key>[^\s:#][^:#]*):\s*(?:#.*)?$")
DISPLAY_NAME_RE = re.compile(r"^(?P<indent>\s{4})displayName:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")
LANGUAGE_FILTER_RE = re.compile(
    r"(?P<prefix>\blang\s*==\s*)(?P<quote>[\"']?)(?P<lang>[A-Za-z]{2,3}(?:-[A-Za-z0-9]+)?)(?P=quote)"
)


def unquote_yaml_scalar(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value[0:1] == value[-1:] and value[0:1] in {'"', "'"}:
        inner = value[1:-1]
        if value[0] == '"':
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return inner
        return inner.replace("''", "'")
    comment = value.find(" #")
    if comment != -1:
        value = value[:comment].rstrip()
    return value


def quote_yaml_scalar(value: str) -> str:
    if value == "":
        return '""'
    needs_quotes = (
        value != value.strip()
        or any(char in value for char in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "!", "%", "@", "`", "\n", "\r"])
        or value.lower() in {"true", "false", "null", "~"}
        or value[0] in "-?"
    )
    if not needs_quotes:
        return value
    return json.dumps(value, ensure_ascii=False)


def properties_section_bounds(lines: list[str]) -> tuple[int, int] | None:
    start = None
    for index, line in enumerate(lines):
        if line.strip() == "properties:":
            start = index
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if line.strip() and not line.startswith((" ", "\t")) and TOP_LEVEL_RE.match(line.strip()):
            end = index
            break
    return start, end


def extract_display_names(text: str) -> dict[str, str]:
    lines = text.splitlines(keepends=True)
    bounds = properties_section_bounds(lines)
    if not bounds:
        return {}
    start, end = bounds
    labels: dict[str, str] = {}
    current_key = ""
    for line in lines[start + 1:end]:
        key_match = PROPERTY_KEY_RE.match(line.rstrip("\r\n"))
        if key_match:
            current_key = key_match.group("key").strip()
            continue
        display_match = DISPLAY_NAME_RE.match(line)
        if display_match and current_key:
            labels[current_key] = unquote_yaml_scalar(display_match.group("value"))
    return labels


def apply_display_names(text: str, labels: dict[str, str]) -> str:
    if not labels:
        return text
    lines = text.splitlines(keepends=True)
    bounds = properties_section_bounds(lines)
    if not bounds:
        return text
    start, end = bounds
    current_key = ""
    for index in range(start + 1, end):
        line = lines[index]
        key_match = PROPERTY_KEY_RE.match(line.rstrip("\r\n"))
        if key_match:
            current_key = key_match.group("key").strip()
            continue
        display_match = DISPLAY_NAME_RE.match(line)
        if display_match and current_key in labels:
            lines[index] = f"{display_match.group('indent')}displayName: {quote_yaml_scalar(labels[current_key])}{display_match.group('newline')}"
    return "".join(lines)
