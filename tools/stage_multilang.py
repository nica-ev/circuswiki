from __future__ import annotations

import json
import re
import shutil
import os
from pathlib import Path
from urllib.parse import quote

from core.languages import (
    common_fallback_language,
    default_language,
    language_codes,
    language_codes_re,
    language_name,
)
from translation.discovery import discover_vault_pages, find_group_source_language, primary_page


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BUILD = ROOT / ".build"
SITE_ASSETS = ROOT / "site-assets"
LANGUAGES = language_codes()
DEFAULT_LANGUAGE = default_language()
COMMON_FALLBACK_LANGUAGE = common_fallback_language()
FALLBACK_STATUS = "missing-translation"


IMAGE_LINK_RE = re.compile(
    r"(?P<prefix>(?:\(|\[|=|:\s*|src=[\"']|href=[\"']))"
    r"(?P<path>(?:(?:\.\./)+)?img/)"
)
DOC_LINK_RE = re.compile(
    r"(?P<prefix>\]\(|href=[\"'])"
    rf"docs/(?!img/)(?:(?:{language_codes_re()})/)?(?P<path>[^)\"']+?\.md(?P<anchor>#[^)\"']*)?)"
)
OBSIDIAN_CALLOUT_RE = re.compile(
    r"^(?P<indent>[ \t]*)>\s*\[!(?P<type>[A-Za-z][\w-]*)\](?P<fold>[+-])?(?P<title>.*)$"
)
BLOCKQUOTE_LINE_RE = re.compile(r"^[ \t]*>\s?(?P<body>.*)$")
FENCE_RE = re.compile(r"^[ \t]*(```|~~~)")
CALLOUT_TYPE_ALIASES = {
    "summary": "abstract",
    "tldr": "abstract",
    "hint": "tip",
    "important": "tip",
    "todo": "note",
    "check": "success",
    "done": "success",
    "help": "question",
    "faq": "question",
    "caution": "warning",
    "attention": "warning",
    "fail": "failure",
    "missing": "failure",
    "error": "danger",
    "cite": "quote",
}
CALLOUT_TYPES = {
    "note",
    "abstract",
    "info",
    "tip",
    "success",
    "question",
    "warning",
    "failure",
    "danger",
    "bug",
    "example",
    "quote",
}


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def site_base_path() -> str:
    value = os.getenv("CIRCUSWIKI_SITE_BASE_PATH", "/circuswiki/").strip()
    if not value.startswith("/"):
        value = "/" + value
    if not value.endswith("/"):
        value += "/"
    return value


def derive_translation_id(path: Path, language: str) -> str:
    relative = path.relative_to(DOCS / language).with_suffix("")
    return relative.as_posix()


def page_url(language: str, relative_path: str) -> str:
    path = Path(relative_path)
    without_suffix = path.with_suffix("").as_posix()
    if without_suffix == "index":
        suffix = ""
    elif without_suffix.endswith("/index"):
        suffix = without_suffix[: -len("/index")] + "/"
    else:
        suffix = without_suffix + "/"

    encoded = quote(suffix, safe="/")
    base_path = site_base_path()
    if language == DEFAULT_LANGUAGE:
        return base_path + encoded
    return f"{base_path}{language}/" + encoded


def language_label(language: str) -> str:
    return language_name(language)


def frontmatter_value(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def admonition_title(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        return ""
    escaped = stripped.replace("\\", "\\\\").replace('"', '\\"')
    return f' "{escaped}"'


def admonition_type(value: str) -> str:
    normalized = value.lower()
    normalized = CALLOUT_TYPE_ALIASES.get(normalized, normalized)
    if normalized in CALLOUT_TYPES:
        return normalized
    return "note"


def page_metadata(page) -> dict[str, object]:
    return {
        "path": page.rel_path,
        "relative_path": page.relative_path,
        "lang": page.language,
        "translation_id": page.translation_id,
        "translation_status": page.translation_status,
        "translation_source_lang": page.translation_source_lang,
        "translation_source": page.translation_source,
        "translation_model": page.translation_model,
        "translation_updated": page.translation_updated,
        "title": page.title,
        "authors": page.authors or [],
    }


def discover_translation_groups() -> dict[str, dict[str, object]]:
    groups: dict[str, dict[str, object]] = {}
    _languages, discovered = discover_vault_pages()

    for translation_id, pages_by_language in discovered.items():
        source_lang = find_group_source_language(pages_by_language)
        source_pages = pages_by_language.get(source_lang) or []
        source_page = primary_page(source_pages) if source_pages else primary_page(next(iter(pages_by_language.values())))
        pages = {
            language: page_metadata(primary_page(pages))
            for language, pages in pages_by_language.items()
            if language in LANGUAGES and pages
        }
        if not pages:
            continue
        groups[translation_id] = {
            "translation_id": translation_id,
            "relative_path": source_page.relative_path,
            "title": source_page.title,
            "source_lang": source_lang,
            "pages": pages,
        }

    return groups


def find_source_language(pages: dict[str, dict[str, str]]) -> str:
    for language, page in pages.items():
        if page["translation_status"] == "original":
            return language

    for page in pages.values():
        if page["translation_source_lang"] and page["translation_source_lang"] in pages:
            return page["translation_source_lang"]

    for page in pages.values():
        source = page["translation_source"]
        if source.startswith("docs/"):
            parts = source.split("/")
            if len(parts) > 2 and parts[1] in pages:
                return parts[1]

    for language, page in pages.items():
        if not page["translation_source"] and page["translation_status"] != "machine-translated":
            return language

    if DEFAULT_LANGUAGE in pages:
        return DEFAULT_LANGUAGE
    if COMMON_FALLBACK_LANGUAGE in pages:
        return COMMON_FALLBACK_LANGUAGE
    return next(iter(pages))


def choose_fallback_language(
    target_language: str,
    source_language: str,
    pages: dict[str, dict[str, str]],
) -> str | None:
    candidates = [
        COMMON_FALLBACK_LANGUAGE,
        source_language,
        DEFAULT_LANGUAGE,
        *pages.keys(),
    ]

    for candidate in candidates:
        if candidate != target_language and candidate in pages:
            return candidate
    return None


def fallback_body(
    target_language: str,
    fallback_language: str,
    title: str,
    fallback_url: str,
) -> str:
    target_label = language_label(target_language)
    fallback_label = language_label(fallback_language)

    if target_language == "de":
        return f"""# {title}

!!! info "Uebersetzung fehlt"

    Diese Seite ist noch nicht auf {target_label} verfuegbar.
    Sie sehen stattdessen die verfuegbare Version auf {fallback_label}.

[Zur verfuegbaren Version wechseln]({fallback_url})
"""

    return f"""# {title}

!!! info "Translation missing"

    This page is not available in {target_label} yet.
    The available {fallback_label} version is linked below.

[Open the available version]({fallback_url})
"""


def create_fallback_pages(groups: dict[str, dict[str, object]]) -> None:
    for group in groups.values():
        pages = group["pages"]
        source_language = group["source_lang"]
        relative_path = group["relative_path"]
        title = group["title"]

        for language in LANGUAGES:
            if language in pages:
                continue

            fallback_language = choose_fallback_language(language, source_language, pages)
            if not fallback_language:
                continue

            fallback_page = pages[fallback_language]
            target = BUILD / language / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            fallback_url = page_url(fallback_language, fallback_page["relative_path"])
            body = fallback_body(language, fallback_language, title, fallback_url)
            frontmatter = "\n".join(
                [
                    f"lang: {language}",
                    f"translation_id: {frontmatter_value(group['translation_id'])}",
                    f"translation_status: {FALLBACK_STATUS}",
                    f"translation_source_lang: {source_language}",
                    f"translation_source: {fallback_page['path']}",
                    f"title: {frontmatter_value(title)}",
                    "publish: true",
                ]
            )
            target.write_text(f"---\n{frontmatter}\n---\n{body}", encoding="utf-8", newline="\n")


def write_translation_map(groups: dict[str, dict[str, object]]) -> None:
    manifest = {
        "default_language": DEFAULT_LANGUAGE,
        "common_fallback_language": COMMON_FALLBACK_LANGUAGE,
        "languages": list(LANGUAGES),
        "groups": {},
        "paths": {},
    }

    for group in groups.values():
        pages = group["pages"]
        source_language = group["source_lang"]
        translation_id = group["translation_id"]
        group_entry = {
            "translation_id": translation_id,
            "source_lang": source_language,
            "title": group["title"],
            "languages": {},
        }

        for language in LANGUAGES:
            page = pages.get(language)
            if page:
                relative_path = page["relative_path"]
                status = page["translation_status"] or (
                    "original" if language == source_language else ""
                )
                fallback = False
                model = page["translation_model"]
                updated = page["translation_updated"]
                path = page["path"]
                source = page["translation_source"]
                source_lang = page["translation_source_lang"]
                authors = page["authors"]
            else:
                relative_path = group["relative_path"]
                status = FALLBACK_STATUS
                fallback = True
                model = ""
                updated = ""
                path = ""
                source = ""
                source_lang = source_language
                authors = []

            url = page_url(language, relative_path)
            group_entry["languages"][language] = {
                "url": url,
                "path": path,
                "relative_path": relative_path,
                "status": status,
                "fallback": fallback,
                "model": model,
                "updated": updated,
                "authors": authors,
                "source": source,
                "source_lang": source_lang,
            }
            manifest["paths"][f"{language}:{relative_path}"] = translation_id

        manifest["groups"][translation_id] = group_entry

    data = json.dumps(manifest, ensure_ascii=False, indent=2)
    for language in LANGUAGES:
        target = BUILD / language / "javascripts" / "translation-map.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data + "\n", encoding="utf-8")


def copy_language(language: str) -> Path:
    source = DOCS / language
    target = BUILD / language

    if not source.exists():
        raise FileNotFoundError(f"Missing language source directory: {source}")

    shutil.copytree(source, target)

    shared_img = DOCS / "img"
    if shared_img.exists():
        shutil.copytree(shared_img, target / "img")

    if SITE_ASSETS.exists():
        for item in SITE_ASSETS.iterdir():
            destination = target / item.name
            if item.is_dir():
                shutil.copytree(item, destination)
            else:
                shutil.copy2(item, destination)

    return target


def normalize_image_links(language_root: Path) -> None:
    for markdown_file in language_root.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        replacement_path = os.path.relpath(
            language_root / "img", markdown_file.parent
        ).replace("\\", "/").rstrip("/") + "/"

        def replace(match: re.Match[str]) -> str:
            return f"{match.group('prefix')}{replacement_path}"

        updated = IMAGE_LINK_RE.sub(replace, text)
        if updated != text:
            markdown_file.write_text(updated, encoding="utf-8", newline="")


def normalize_internal_doc_links(language_root: Path) -> None:
    for markdown_file in language_root.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")

        def replace(match: re.Match[str]) -> str:
            return f"{match.group('prefix')}{match.group('path')}"

        updated = DOC_LINK_RE.sub(replace, text)
        if updated != text:
            markdown_file.write_text(updated, encoding="utf-8", newline="")


def convert_obsidian_callouts(text: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    in_fence = False

    while index < len(lines):
        line = lines[index]
        line_text = line.rstrip("\r\n")

        if FENCE_RE.match(line_text):
            in_fence = not in_fence
            output.append(line)
            index += 1
            continue

        match = None if in_fence else OBSIDIAN_CALLOUT_RE.match(line_text)
        if not match:
            output.append(line)
            index += 1
            continue

        callout_type = admonition_type(match.group("type"))
        fold = match.group("fold") or ""
        title = admonition_title(match.group("title"))
        marker = "!!!"
        if fold == "+":
            marker = "???+"
        elif fold == "-":
            marker = "???"

        indent = match.group("indent")
        output.append(f"{indent}{marker} {callout_type}{title}\n")

        content: list[str] = []
        index += 1
        while index < len(lines):
            body_line = lines[index]
            body_text = body_line.rstrip("\r\n")
            body_match = BLOCKQUOTE_LINE_RE.match(body_text)
            if not body_match:
                break
            content.append(body_match.group("body"))
            index += 1

        if content:
            output.append("\n")
            for body in content:
                output.append(f"{indent}    {body}\n" if body else f"{indent}    \n")

        continue

    return "".join(output)


def convert_obsidian_callouts_in_markdown(language_root: Path) -> None:
    for markdown_file in language_root.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        updated = convert_obsidian_callouts(text)
        if updated != text:
            markdown_file.write_text(updated, encoding="utf-8", newline="")


def main() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)

    groups = discover_translation_groups()

    for language in LANGUAGES:
        language_root = copy_language(language)

    create_fallback_pages(groups)
    write_translation_map(groups)

    for language in LANGUAGES:
        language_root = BUILD / language
        normalize_internal_doc_links(language_root)
        normalize_image_links(language_root)
        convert_obsidian_callouts_in_markdown(language_root)


if __name__ == "__main__":
    main()
