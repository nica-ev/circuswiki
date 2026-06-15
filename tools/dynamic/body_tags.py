from __future__ import annotations


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
