---
created: 2026-06-06 19:25:00
update: 2026-06-09 16:56:47
publish: false
tags:
  - translation
  - architecture
  - multilingual
title: Translation Architecture
description: Source-language and fallback rules for CircusWiki multilingual content.
authors:
  - Marc Bielert
---

# Translation Architecture

This note defines the intended multilingual content model for CircusWiki.

## Core Distinction

German is currently the default public site language, but German is not always the canonical source language of a page.

These concepts must remain separate:

- Default site language: the language shown at the root URL for the current project phase.
- Page language: the language of a specific Markdown file.
- Canonical source language: the original language in which a translation group was authored.

Current default presentation:

```text
/circuswiki/
/circuswiki/en/
/circuswiki/pl/
/circuswiki/hu/
/circuswiki/it/
/circuswiki/nl/
/circuswiki/el/
/circuswiki/es/
/circuswiki/uk/
/circuswiki/pt/
/circuswiki/cs/
/circuswiki/sk/
```

Current language folders:

```text
docs/de/example.md
docs/en/example.md
docs/pl/example.md
docs/hu/example.md
docs/it/example.md
docs/nl/example.md
docs/el/example.md
docs/es/example.md
docs/uk/example.md
docs/pt/example.md
docs/cs/example.md
docs/sk/example.md
```

The current configured language set is maintained in `tools/config/languages.json`.
Use that registry as the source of truth for tooling and docs.

The shared relative path and `translation_id` identify equivalent pages across languages. The folder determines the file's language for presentation, but metadata must identify the original source.

## Source Language Rule

CircusWiki has an international community. New original content may be authored in German, English, Italian, Polish, Greek, Hungarian, Spanish, Ukrainian, or other languages.

Automatic translation should always translate from the canonical original source into the requested target language whenever possible.

Do not translate from German merely because German is the current default site language.

Reason: translating from the original minimizes quality loss. Chained translation such as Italian -> German -> English should be avoided when Italian -> English is possible.

## Recommended Metadata

Original page:

```yaml
lang: de
translation_id: alaska-baseball
translation_status: original
translation_source_lang: de
```

Translated page:

```yaml
lang: en
translation_id: alaska-baseball
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Alaska Baseball.md
translation_source_hash: ...
translation_model: ...
translation_updated: ...
```

Original Italian page:

```yaml
lang: it
translation_id: some-italian-game
translation_status: original
translation_source_lang: it
```

German translation from the Italian original:

```yaml
lang: de
translation_id: some-italian-game
translation_status: machine-translated
translation_source_lang: it
translation_source: docs/it/Some Italian Game.md
translation_source_hash: ...
translation_model: ...
translation_updated: ...
```

## Field Semantics

`lang`

The language of the current file.

`translation_id`

Stable identifier shared by all language versions of the same page. Matching relative paths are still required for presentation, but `translation_id` is the safer semantic link for tooling.

`translation_status`

Suggested values:

- `original`
- `machine-translated`
- `human-translated`
- `human-reviewed`
- `needs-review`

`translation_source_lang`

The canonical source language for the translation group. This should match the `lang` value of the original page.

`translation_source`

Path to the exact source file used for translation. For translated pages this should point to the canonical original whenever possible.

`translation_source_body_hash`

Hash of the canonical source Markdown body used to determine whether the body
translation is outdated.

`translation_source_metadata_hash`

Hash of the translatable source metadata fields used to determine whether
localized frontmatter is outdated. The current translatable metadata fields are
`title` and `description`.

`translation_source_hash`

Legacy body-hash field kept for migration compatibility. New tooling should
write `translation_source_body_hash` and may update `translation_source_hash` as
a backward-compatible alias.

## Tags Are Not Enough

Do not model canonical source language as a tag.

Tags are content classification. Source language is structural translation metadata and should be a dedicated frontmatter field.

## Current Translation Tooling

The translation console and CLI require explicit source and target languages for
single-file operations. The UI may initialize selections from the registry, but
backend translation operations should not silently assume a fixed language pair.

Full page translation now has two explicit translation parts:

1. translate the Markdown body and repair local link targets
2. translate frontmatter `title` and `description`

Metadata-only translation is available separately for existing target files. It
updates only localized metadata and metadata provenance, preserving the target
body.

Batch translation works from translation groups:

```text
translation_id -> find canonical original -> translate original into selected target language
```

not a fixed folder pair such as:

```text
docs/de -> docs/en
```

## Translation Workflow

Expected behavior:

1. Collect all language versions by `translation_id`.
2. Identify the original page by `translation_status: original` and `translation_source_lang`.
3. For a requested target language, check whether a matching target file exists.
4. If the target is missing or outdated, translate from the original source page.
5. Write the translated file to the matching target language folder.
6. Preserve relative path parity where possible.
7. Record the source file, body hash, metadata hash, model, status, and update timestamps.

If more than one page claims to be the original for a `translation_id`, tooling should flag the group for manual review.

## Public Language Fallback Strategy

Current implementation:

- `tools/stage_multilang.py` discovers translation groups by `translation_id`.
- Missing language versions are generated as static fallback pages in `.build/<language>/`.
- Generated fallback pages use `translation_status: missing-translation`.
- Multilingual staging embeds a compact JSON translation context into each staged page. It contains only that page's language URLs and current translation provenance.
- `site-assets/javascripts/language-switcher.js` reads this page-local context and rewrites language links to known real or fallback pages without downloading a vault-wide manifest.
- This keeps GitHub Pages fully static while avoiding raw 404s for known untranslated pages.

Current public behavior:

- German remains the default public root.
- Other configured languages are available under their language code, for example `/en/`, `/it/`, and `/pl/`.
- Do not force automatic browser-language redirects.
- Do not surprise the current German-based community by changing the root language.

Long term:

- Keep explicit language URLs such as `/en/`, `/it/`, `/pl/`.
- Browser language detection may suggest a language, but should not silently redirect first-time users.
- If a user manually selects a language, store the preference locally.
- If a page is missing in the selected language, fall back visibly.

Suggested fallback order for a missing page:

1. selected language
2. English, if available as common bridge language
3. canonical original source language
4. German, while German remains the project default

Fallback should be visible to the user, for example:

```text
This page is shown in German because no English translation exists yet.
```

## Implementation Implications

Code changes must avoid hard-coding German as source. The configured site
languages live in `tools/config/languages.json`; read them through
`tools/core/languages.py` instead of duplicating lists. The current configured
languages are German (`de`), English (`en`), Polish (`pl`), Hungarian (`hu`),
Italian (`it`), Dutch (`nl`), Greek (`el`), Spanish (`es`), Ukrainian (`uk`),
Portuguese (`pt`), Czech (`cs`), and Slovak (`sk`). Use Dutch (`nl`) for the
Circusatelier Woesh / West Flanders context; Flemish is a regional variety, but
`nl` is the standard web language code.

When extending translation tooling:

- make source and target languages explicit parameters
- derive source candidates from metadata, not only folders
- validate `lang`, `translation_id`, `translation_status`, and `translation_source_lang`
- keep body translation and metadata translation separate internally
- translate only deliberate localized metadata fields, currently `title` and `description`
- preserve Obsidian syntax, links, image paths, code blocks, and unknown frontmatter fields

## Deterministic Repair

The translation console may offer automated metadata repair for yellow health cells.

Allowed deterministic repairs:

- set `lang` from the language folder
- set missing `translation_id` from the translation group / relative path
- mark the detected canonical source page as `translation_status: original`
- set `translation_source_lang` from the detected canonical source language
- set translated pages' `translation_source` to the detected source file
- set missing translated-page `translation_status` to `needs-review`

Do not auto-repair quality-sensitive provenance when it cannot be trusted:

- do not invent `translation_model`
- do not invent `translation_updated`
- do not update `translation_source_hash` merely to silence an outdated warning
- do not turn stale translations green without retranslating or human review

Unresolved or unsafe cases should stay yellow.

## Batch Translation Safeguards

Batch translation must use a plan-first workflow.

Planning must not call the translation API. It should only:

- select candidate files
- apply `max_files`
- count source characters
- exclude generated aggregate/index utility pages such as `sitemap.md`
- show source language, target language, source path, target path, and reason

Running a batch should process only the planned files and update progress after
each file. This keeps cost exposure explicit and bounded.

The first implementation uses one prompt template with `{source_lang}` and
`{target_lang}` placeholders. These placeholders are injected per translation
call, including batch translation.
