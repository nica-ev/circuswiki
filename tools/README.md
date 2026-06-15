---
created: 2026-06-07 21:33:20
update: 2026-06-08 16:40:56
---

# CircusWiki Tools

Local tooling supports multilingual staging, translation workflow experiments, navigation management, and static site builds.

## Main Commands

```powershell
python tools/stage_multilang.py
powershell -ExecutionPolicy Bypass -File tools/build_multilang.ps1
powershell -ExecutionPolicy Bypass -File tools/serve_multilang.ps1
powershell -ExecutionPolicy Bypass -File tools/dev_console.ps1
powershell -ExecutionPolicy Bypass -File tools/check.ps1
python tools/sync_configs.py
```

Translation CLI:

```powershell
python tools/translation_cli.py health --source-lang de --target-lang en
python tools/translation_cli.py inspect "docs/de/index.md" --source-lang de --target-lang en
python tools/translation_cli.py translate "docs/de/index.md" --source-lang de --target-lang en --dry-run
```

Registry validation:

```powershell
python -m tools.core.languages
```

Tests:

```powershell
python -m unittest discover tools/tests
```

Combined checks:

```powershell
powershell -ExecutionPolicy Bypass -File tools/check.ps1
powershell -ExecutionPolicy Bypass -File tools/check.ps1 -FullBuild
```

Zensical config sync is dry-run by default:

```powershell
python tools/sync_configs.py
python tools/sync_configs.py --write
```

The sync command derives `site_url`, `docs_dir`, `site_dir`, theme language, and
alternate language entries from `tools/config/languages.json`. It respects
`CIRCUSWIKI_SITE_BASE_PATH` and `CIRCUSWIKI_SITE_URL`, or explicit `--base-path`
and `--base-url` arguments.

## Language Registry

The configured language list lives in `tools/config/languages.json`. Python tools should access it through `tools/core/languages.py` instead of duplicating language codes, names, fallback behavior, or Zensical config paths.

The registry currently owns:

- default language
- common fallback language
- language code order
- English and native language names
- Zensical config file per language
- root/default language marker

## Dev Console API Summary

The local console is served by `tools/dev_console/server.py`.

Current endpoint contracts:

- `GET /api/config`: returns registry languages, UI initial source/target selections, default model, default prompt template, and rendered default prompt.
- `GET /api/pages?source_lang=<code>`: returns source Markdown paths for the explicit source language. Missing `source_lang` returns `400`.
- `GET /api/health?source_lang=<code>&target_lang=<code>`: returns the file-pair health summary for the explicit language pair. Missing language parameters return `400`.
- `GET /api/page?path=<repo-path>&source_lang=<code>&target_lang=<code>`: inspects one explicit source/target pair. Missing `path`, `source_lang`, or `target_lang` returns `400`.
- `GET /api/vault-health`: returns the multilingual translation matrix using canonical source detection per translation group.
- `POST /api/translate`: translates one full file body plus localized metadata. JSON body requires `path`, `source_lang`, and `target_lang`; optional fields are `model`, `prompt`, and `dry_run`. `dry_run` still calls the translation API; it only skips writing the target file.
- `POST /api/translate-metadata`: translates only target frontmatter `title` and `description` for an existing target file. JSON body requires `path`, `source_lang`, and `target_lang`; optional fields are `model` and `dry_run`. `dry_run` still calls the metadata translation API when metadata is stale or missing; it only skips writing the target file.
- `POST /api/repair-metadata`: deterministic metadata repair for one file. JSON body requires `path`.
- `POST /api/batch-plan`: plans batch candidates without API calls. JSON body uses `target_lang`, `max_files`, optional `source_lang` (`all` allowed), optional `reason`, optional `max_source_chars`, and optional `path_filter`.
- `POST /api/batch-translate-file`: translates one planned batch item. JSON body uses `source_path`, `source_lang`, `target_lang`, and optional `model`/`prompt`.
- `POST /api/metadata-batch-plan`: plans metadata-only candidates without API calls. JSON body uses `target_lang`, `max_files`, optional `source_lang` (`all` allowed), optional `reason`, and optional `path_filter`.
- `POST /api/metadata-batch-translate-file`: translates metadata for one planned metadata batch item. JSON body uses `source_path`, `source_lang`, `target_lang`, and optional `model`.
- `GET /api/original-graph?exclude_sitemap=true|false`: returns canonical original nodes and explicit content-link edges normalized through translation groups for the Original Graph tab. `sitemap.md` is excluded by default.
- `GET /api/navigation/scan`: inspects Zensical navigation and canonical navigation model state.
- `POST /api/navigation/init`: creates the canonical navigation model from an explicit source language. JSON body requires `language`.
- `POST /api/navigation/preview`: renders the supplied model without writing files. JSON body requires `model`.
- `POST /api/navigation/apply`: writes the supplied model and regenerates Zensical nav blocks. JSON body requires `model`.
- `POST /api/navigation/translate-labels`: translates navigation labels for one target language. JSON body requires `model`, `source_lang`, and `target_lang`.
- `POST /api/navigation/translate-all-labels`: translates navigation labels from an explicit source language to all other configured languages. JSON body requires `model` and `source_lang`.
- `GET /api/obsidian/status`: reports optional Obsidian CLI availability.

The Link Repair workflow restores local Markdown/wikilink targets and, for
translated notes tagged `dynamic`, also rewrites Markdown link labels inside
generated dynamic block content to the linked target-language page title.

The console currently uses lightweight explicit endpoint contracts rather than
a dedicated schema framework. Add a schema layer only when request/response
objects become large enough that duplicated validation is causing bugs.

The server should remain thin. Translation, navigation, build, and Obsidian behavior should stay in domain modules.

The dev console serves `index.html` with mtime-based query strings for `styles.css`
and `app.js`, so normal refreshes should pick up local UI changes.

## Original Graph

The Original Graph tab is an experiment for understanding the semantic structure
of the multilingual vault.

Graph construction rules:

- nodes are canonical original translation groups, keyed by `translation_id`
- translated files are not shown as nodes
- explicit Markdown links and Obsidian wikilinks are parsed from original pages
- a link may resolve to a translated file, but the edge is normalized to that target file's canonical original group
- image links, embeds, external URLs, and links inside fenced code blocks are ignored
- `sitemap.md` is excluded by default because it links to many pages and distorts the structure

Graph controls:

- `Exclude sitemap.md`: reloads graph data with or without `sitemap.md`
- `Show labels`: toggles visible node titles
- `Zoom +` / `Zoom -` / `Fit`: deterministic viewport controls when mouse-wheel zoom is awkward
- `Repulsion`: increases spacing between nodes
- `Gravity`: controls how strongly the layout pulls toward the center
- `Edge Length`: increases spacing between connected nodes

The visualization uses Apache ECharts loaded from jsDelivr:

```html
https://cdn.jsdelivr.net/npm/echarts@6/dist/echarts.min.js
```

If the dev console needs to work offline, vendor `echarts.min.js` into
`tools/dev_console/static/` and update `index.html`.
