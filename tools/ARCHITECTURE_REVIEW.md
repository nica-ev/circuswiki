---
created: 2026-06-07 21:04:37
update: 2026-06-07 23:37:20
---

# CircusWiki Tooling Architecture Review

Status: closed implementation review
Scope: `tools/`, `site-assets/`, multilingual Zensical configs, local dev console, translation/navigation tooling, and optional Obsidian integration.

## Summary

The original review identified duplicated language configuration, unclear tooling boundaries, implicit source/target language defaults, implicit API contracts, missing tests, and missing Obsidian integration boundaries.

Those issues have mostly been addressed. This file is now a status record, not the active architecture source. Use `tools/ARCHITECTURE.md` for current architecture and next refactor targets.

## Completed

- Added canonical language/site registry in `tools/config/languages.json`.
- Added shared registry access and validation in `tools/core/languages.py`.
- Replaced duplicated language lists in Python staging/build/navigation/translation helpers.
- Made runtime language switching derive available languages and fallback URLs from compact, build-generated per-page translation contexts.
- Added `tools/sync_configs.py` for dry-run/default Zensical config synchronization and explicit `--write` updates.
- Split dev-console backend routes by domain.
- Added optional Obsidian CLI adapter and status route.
- Made translation CLI source/target languages explicit.
- Made single-file dev-console translation endpoints reject missing language parameters instead of silently defaulting to a fixed language pair.
- Added batch translation source-language, reason, path/title/ID, and source-size filters.
- Added focused Python tests for registry behavior, staging behavior, translation helpers, navigation rendering, config sync, and Obsidian status.
- Added `tools/check.ps1` as the standard local quality gate.
- Updated GitHub Pages deployment to `actions/deploy-pages@v5`.
- Added tooling documentation in `tools/README.md`, `tools/ARCHITECTURE.md`, and `tools/AGENTS.md`.

## Current Decisions

- Keep Zensical as the static-site generator.
- Keep Python scripts and PowerShell wrappers for local tooling.
- Keep the dev console on Python `http.server` plus vanilla JS for now.
- Keep Zensical TOML files checked in and human-readable; use registry sync/validation rather than hiding config generation.
- Keep Obsidian integration optional. Browser mode must remain usable without Obsidian CLI.
- Do not introduce a schema framework yet. Current endpoint contracts plus targeted validation helpers are sufficient.
- Do not run full local tooling checks inside the Pages deploy workflow unless there is a concrete CI need. The deploy workflow's job is to build and deploy the static site.

## Remaining Risks

### Translation Group Logic Duplication

Staging and translation workflow still each contain translation-group discovery logic. This is the main remaining architecture cleanup target because fallback generation, vault health, and batch planning should agree exactly on canonical source detection.

### Metadata Repair Edge Cases

Deterministic repair intentionally avoids fabricating source hashes, model names, or timestamps. More tests should cover duplicate originals, missing originals, moved files, and conflicting `translation_id` values.

### Frontend Growth

The dev-console UI is still a large application. Generic helpers have been split out, but domain modules should be extracted only when they reduce coupling or make tests/manual review easier.

### Documentation Drift

`_inbox/` contains historical drafts with MkDocs-era information. They should remain available as project history but must not be used as current implementation guidance.

## Active Follow-Up

Use `tools/ARCHITECTURE.md` for the current follow-up list. At the time of this cleanup, the practical next architecture item is extracting shared translation-group discovery.
