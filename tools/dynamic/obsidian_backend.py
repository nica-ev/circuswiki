from __future__ import annotations

import json
import re
from typing import Any
from pathlib import Path

from obsidian.cli import CommandResult, run_obsidian, status as obsidian_status
from base_labels import localize_base_text

ROOT = Path(__file__).resolve().parents[2]
GENERATED_BASE_ROOT = ROOT / "_bases"
LANGUAGE_FILTER_RE = re.compile(
    r"(?P<prefix>\blang\s*==\s*)(?P<quote>[\"']?)(?P<lang>[A-Za-z]{2,3}(?:-[A-Za-z0-9]+)?)(?P=quote)"
)


def status() -> dict[str, Any]:
    return obsidian_status()


def query_base(base_path: str, view: str, timeout_seconds: int = 60, language: str = "") -> dict[str, Any]:
    query_path = materialize_language_base(base_path, language) if language else base_path
    result = run_obsidian(
        [
            "base:query",
            f"path={query_path}",
            f"view={view}",
            "format=json",
        ],
        timeout_seconds=timeout_seconds,
    )
    parsed = parse_json_output(result)
    return {
        "ok": result.ok and parsed["ok"],
        "command": result.command,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "error": result.error or parsed["error"],
        "data": parsed["data"],
    }


def materialize_language_base(base_path: str, language: str) -> str:
    source = (ROOT / base_path).resolve()
    source.relative_to(ROOT)
    if not source.is_file():
        return base_path

    text = source.read_text(encoding="utf-8")
    updated, count = LANGUAGE_FILTER_RE.subn(
        lambda match: f"{match.group('prefix')}{match.group('quote')}{language}{match.group('quote')}",
        text,
    )
    if count == 0:
        updated = text
    updated = localize_base_text(updated, source, language)

    target = GENERATED_BASE_ROOT / f"{source.stem}.{language}.generated{source.suffix}"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(updated, encoding="utf-8", newline="\n")
    return target.relative_to(ROOT).as_posix()


def parse_json_output(result: CommandResult) -> dict[str, Any]:
    if not result.ok:
        return {"ok": False, "data": None, "error": result.error or result.stderr}

    text = result.stdout.strip()
    if not text:
        return {"ok": False, "data": None, "error": "Obsidian returned empty output."}
    if text.lower().startswith("error:"):
        return {"ok": False, "data": None, "error": text}

    for start_char in ("[", "{"):
        start = text.find(start_char)
        if start == -1:
            continue
        candidate = text[start:]
        try:
            return {"ok": True, "data": json.loads(candidate), "error": ""}
        except json.JSONDecodeError:
            continue

    return {"ok": False, "data": None, "error": f"Obsidian output was not valid JSON: {text[:500]}"}
