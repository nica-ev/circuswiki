from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from core.languages import default_language, language_codes, language_name

ROOT = Path(__file__).resolve().parents[1]
BASES = ROOT / "_bases"
CONFIG_PATH = ROOT / "tools" / "config" / "base_display_names.json"
DEFAULT_MODEL = "google/gemini-2.0-flash-001"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
TOP_LEVEL_RE = re.compile(r"^[A-Za-z0-9_.-]+:\s*(?:#.*)?$")
PROPERTY_KEY_RE = re.compile(r"^(?P<indent>\s{2})(?P<key>[^\s:#][^:#]*):\s*(?:#.*)?$")
DISPLAY_NAME_RE = re.compile(r"^(?P<indent>\s{4})displayName:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")
LANGUAGE_FILTER_RE = re.compile(
    r"(?P<prefix>\blang\s*==\s*)(?P<quote>[\"']?)(?P<lang>[A-Za-z]{2,3}(?:-[A-Za-z0-9]+)?)(?P=quote)"
)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def source_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_base_files() -> list[Path]:
    if not BASES.exists():
        return []
    return sorted(
        path for path in BASES.glob("*.base")
        if path.is_file() and ".generated" not in path.name
    )


def resolve_base(path: str | Path) -> Path:
    base = Path(path)
    resolved = (ROOT / base).resolve() if not base.is_absolute() else base.resolve()
    resolved.relative_to(ROOT)
    return resolved


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


def load_config(path: Path | None = None) -> dict[str, Any]:
    path = path or CONFIG_PATH
    if not path.is_file():
        return {"version": 1, "bases": {}}
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("base_display_names.json must contain a JSON object")
    data.setdefault("version", 1)
    data.setdefault("bases", {})
    return data


def save_config(config: dict[str, Any], path: Path | None = None) -> None:
    path = path or CONFIG_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def update_config_sources(config: dict[str, Any], base_path: Path) -> dict[str, Any]:
    base_rel = rel(base_path)
    labels = extract_display_names(base_path.read_text(encoding="utf-8"))
    base_entry = config.setdefault("bases", {}).setdefault(
        base_rel,
        {"source_lang": default_language(), "properties": {}},
    )
    base_entry.setdefault("source_lang", default_language())
    properties = base_entry.setdefault("properties", {})
    for key, value in labels.items():
        entry = properties.setdefault(key, {"translations": {}})
        old_hash = entry.get("source_hash")
        new_hash = source_hash(value)
        entry["source"] = value
        entry["source_hash"] = new_hash
        entry.setdefault("translations", {})
        if old_hash and old_hash != new_hash:
            for translation in entry["translations"].values():
                if isinstance(translation, dict):
                    translation["stale"] = True
    for key in list(properties):
        if key not in labels:
            properties[key]["missing_in_base"] = True
    return config


def scan_base_labels() -> dict[str, Any]:
    config = load_config()
    bases = []
    languages = language_codes()
    for base_path in canonical_base_files():
        labels = extract_display_names(base_path.read_text(encoding="utf-8"))
        config_entry = config.get("bases", {}).get(rel(base_path), {})
        properties = config_entry.get("properties", {}) if isinstance(config_entry, dict) else {}
        property_rows = []
        missing_count = 0
        stale_count = 0
        for key, value in labels.items():
            entry = properties.get(key, {}) if isinstance(properties, dict) else {}
            translations = entry.get("translations", {}) if isinstance(entry, dict) else {}
            current_hash = source_hash(value)
            missing_languages = []
            stale_languages = []
            source_lang = (
                config_entry.get("source_lang", default_language())
                if isinstance(config_entry, dict)
                else default_language()
            )
            for language in languages:
                if language == source_lang:
                    continue
                translation = translations.get(language)
                if not isinstance(translation, dict) or not str(translation.get("value") or "").strip():
                    missing_languages.append(language)
                    continue
                if translation.get("source_hash") != current_hash or translation.get("stale"):
                    stale_languages.append(language)
            missing_count += len(missing_languages)
            stale_count += len(stale_languages)
            property_rows.append(
                {
                    "key": key,
                    "source": value,
                    "source_hash": current_hash,
                    "missing_languages": missing_languages,
                    "stale_languages": stale_languages,
                    "translation_count": sum(1 for item in translations.values() if isinstance(item, dict) and item.get("value")),
                }
            )
        bases.append(
            {
                "path": rel(base_path),
                "source_lang": config_entry.get("source_lang", default_language()) if isinstance(config_entry, dict) else default_language(),
                "property_count": len(labels),
                "missing_count": missing_count,
                "stale_count": stale_count,
                "properties": property_rows,
            }
        )
    return {
        "languages": languages,
        "language_names": {language: language_name(language) for language in languages},
        "config_path": rel(CONFIG_PATH),
        "bases": bases,
    }


def labels_for_language(base_path: str | Path, language: str, config: dict[str, Any] | None = None) -> dict[str, str]:
    config = config or load_config()
    base_rel = rel(resolve_base(base_path))
    base_entry = config.get("bases", {}).get(base_rel, {})
    source_lang = base_entry.get("source_lang", default_language()) if isinstance(base_entry, dict) else default_language()
    properties = base_entry.get("properties", {}) if isinstance(base_entry, dict) else {}
    labels: dict[str, str] = {}
    for key, entry in properties.items():
        if not isinstance(entry, dict):
            continue
        if language == source_lang:
            value = entry.get("source")
        else:
            translations = entry.get("translations", {})
            translation = translations.get(language) if isinstance(translations, dict) else None
            value = translation.get("value") if isinstance(translation, dict) else None
        if isinstance(value, str) and value.strip():
            labels[str(key)] = value.strip()
    return labels


def localize_base_text(text: str, base_path: str | Path, language: str) -> str:
    return apply_display_names(text, labels_for_language(base_path, language))


def materialize_base_labels(base_path: str | Path, language: str, target_path: Path | None = None) -> dict[str, Any]:
    source = resolve_base(base_path)
    text = source.read_text(encoding="utf-8")
    updated, replacements = LANGUAGE_FILTER_RE.subn(
        lambda match: f"{match.group('prefix')}{match.group('quote')}{language}{match.group('quote')}",
        text,
    )
    if replacements == 0:
        updated = text
    updated = localize_base_text(updated, source, language)
    if target_path is not None:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(updated, encoding="utf-8", newline="\n")
    return {
        "base": rel(source),
        "language": language,
        "language_replacements": replacements,
        "display_names": labels_for_language(source, language),
        "text": updated,
    }


def plan_base_label_translation(base_path: str = "", target_lang: str = "all") -> dict[str, Any]:
    config = load_config()
    targets = [target_lang] if target_lang != "all" else language_codes()
    candidates = []
    for base in canonical_base_files():
        if base_path and rel(base) != base_path:
            continue
        update_config_sources(config, base)
        base_entry = config["bases"][rel(base)]
        source_lang = base_entry.get("source_lang", default_language())
        for key, entry in base_entry.get("properties", {}).items():
            for language in targets:
                if language == source_lang:
                    continue
                translation = entry.get("translations", {}).get(language)
                current_hash = entry.get("source_hash")
                missing = not isinstance(translation, dict) or not str(translation.get("value") or "").strip()
                stale = isinstance(translation, dict) and (translation.get("source_hash") != current_hash or translation.get("stale"))
                if missing or stale:
                    candidates.append(
                        {
                            "base": rel(base),
                            "property": key,
                            "source": entry.get("source", ""),
                            "source_lang": source_lang,
                            "target_lang": language,
                            "reason": "missing" if missing else "stale",
                        }
                    )
    return {
        "target_lang": target_lang,
        "base": base_path,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }


def translate_base_labels(base_path: str = "", target_lang: str = "all", model: str | None = None, dry_run: bool = False) -> dict[str, Any]:
    config = load_config()
    targets = [target_lang] if target_lang != "all" else language_codes()
    model = model or default_model()
    results = []
    for base in canonical_base_files():
        if base_path and rel(base) != base_path:
            continue
        update_config_sources(config, base)
        base_rel = rel(base)
        base_entry = config["bases"][base_rel]
        source_lang = base_entry.get("source_lang", default_language())
        properties = base_entry.get("properties", {})
        for language in targets:
            if language == source_lang:
                continue
            pending = {}
            for key, entry in properties.items():
                translation = entry.get("translations", {}).get(language)
                current_hash = entry.get("source_hash")
                missing = not isinstance(translation, dict) or not str(translation.get("value") or "").strip()
                stale = isinstance(translation, dict) and (translation.get("source_hash") != current_hash or translation.get("stale"))
                if missing or stale:
                    pending[key] = entry.get("source", "")
            if not pending:
                continue
            translated = pending if dry_run else call_label_translation_model(pending, source_lang, language, model)
            for key, value in translated.items():
                if key not in properties:
                    continue
                if not dry_run:
                    translations = properties[key].setdefault("translations", {})
                    translations[language] = {
                        "value": str(value).strip(),
                        "source_hash": properties[key].get("source_hash", ""),
                        "model": model,
                        "updated": datetime.now(UTC).isoformat(timespec="seconds"),
                    }
                results.append(
                    {
                        "base": base_rel,
                        "property": key,
                        "source": pending[key],
                        "target_lang": language,
                        "value": str(value).strip(),
                        "dry_run": dry_run,
                    }
                )
    if not dry_run:
        save_config(config)
    return {"model": model, "dry_run": dry_run, "translated_count": len(results), "results": results}


def materialize_all_base_labels(base_path: str = "", target_lang: str = "all") -> dict[str, Any]:
    targets = [target_lang] if target_lang != "all" else language_codes()
    results = []
    for base in canonical_base_files():
        if base_path and rel(base) != base_path:
            continue
        for language in targets:
            target = BASES / f"{base.stem}.{language}.generated{base.suffix}"
            result = materialize_base_labels(base, language, target)
            result.pop("text", None)
            result["target"] = rel(target)
            results.append(result)
    return {"materialized_count": len(results), "results": results}


def call_label_translation_model(labels: dict[str, str], source_lang: str, target_lang: str, model: str) -> dict[str, str]:
    if not labels:
        return {}
    load_local_env()
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY or OPENAI_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL") or os.getenv("OPENAI_BASE_URL") or DEFAULT_BASE_URL
    request = urllib.request.Request(
        chat_completions_url(base_url),
        data=json.dumps(
            {
                "model": model,
                "messages": [
                    {"role": "system", "content": label_prompt(source_lang, target_lang)},
                    {"role": "user", "content": json.dumps(labels, ensure_ascii=False, indent=2)},
                ],
                "temperature": 0.2,
            }
        ).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/nica-ev/circuswiki",
            "X-Title": "CircusWiki Base Label Localization",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Translation API request failed with HTTP {exc.code}: {details}") from exc
    try:
        raw = strip_code_fences(data["choices"][0]["message"]["content"]).strip()
        translated = json.loads(raw)
    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Base label translation response was not valid JSON: {data}") from exc
    if not isinstance(translated, dict):
        raise RuntimeError(f"Base label translation response must be a JSON object: {translated}")
    return {key: str(translated[key]).strip() for key in labels if key in translated}


def label_prompt(source_lang: str, target_lang: str) -> str:
    return f"""You are translating short table column labels for CircusWiki Obsidian Bases from {language_name(source_lang)} to {language_name(target_lang)}.

Translate only the label values. Keep them concise table headers.
Do not translate or rename the JSON keys.
Return only a valid JSON object with the same keys as the input.
Do not wrap the JSON in Markdown fences."""


def chat_completions_url(base_url: str) -> str:
    normalized = base_url.rstrip("/")
    if normalized.endswith("/chat/completions"):
        return normalized
    return normalized + "/chat/completions"


def load_local_env() -> None:
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def default_model() -> str:
    load_local_env()
    return os.getenv("OPENROUTER_MODEL") or DEFAULT_MODEL


def strip_code_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        return "\n".join(lines[1:-1])
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate Obsidian Base displayName labels")
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("scan", help="Scan base displayName labels")
    plan_parser = subcommands.add_parser("plan", help="Plan missing/stale label translations")
    plan_parser.add_argument("--base", default="")
    plan_parser.add_argument("--target-lang", default="all")
    translate_parser = subcommands.add_parser("translate", help="Translate missing/stale labels")
    translate_parser.add_argument("--base", default="")
    translate_parser.add_argument("--target-lang", default="all")
    translate_parser.add_argument("--model")
    translate_parser.add_argument("--dry-run", action="store_true")
    materialize_parser = subcommands.add_parser("materialize", help="Regenerate localized generated base files")
    materialize_parser.add_argument("--base", default="")
    materialize_parser.add_argument("--target-lang", default="all")
    args = parser.parse_args()

    if args.command == "scan":
        print(json.dumps(scan_base_labels(), ensure_ascii=False, indent=2))
    elif args.command == "plan":
        print(json.dumps(plan_base_label_translation(args.base, args.target_lang), ensure_ascii=False, indent=2))
    elif args.command == "translate":
        print(json.dumps(translate_base_labels(args.base, args.target_lang, args.model, args.dry_run), ensure_ascii=False, indent=2))
    elif args.command == "materialize":
        print(json.dumps(materialize_all_base_labels(args.base, args.target_lang), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
