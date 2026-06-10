---
created: 2025-05-02 21:56:19
update: 2026-06-10 21:32:19
---

# CircusWiki

CircusWiki is a Markdown-based knowledge base for circus pedagogy, circus arts, movement games, education, and related topics.

The repository is a clean rebuild:

- content is authored as an Obsidian vault
- public site generation uses Zensical
- local tooling is maintained under `tools/`

## Structure

```text
.
|-- docs/          Published Markdown content and shared assets
|   |-- de/        German pages and default public root
|   |-- en/        English pages
|   |-- hu/        Hungarian pages
|   |-- it/        Italian pages
|   |-- nl/        Dutch pages
|   |-- el/        Greek pages
|   |-- es/        Spanish pages
|   |-- uk/        Ukrainian pages
|   |-- pt/        Portuguese pages
|   |-- cs/        Czech pages
|   |-- sk/        Slovak pages
|   `-- img/       Shared media assets
|-- site-assets/   Shared generated-site assets copied into each language build
|-- tools/         Local build/staging scripts
|-- .obsidian/     Obsidian vault configuration
|-- _templates/    Obsidian templates
|-- _dataview/     Dataview helper notes and queries
|-- _canvas/       Obsidian canvas files
|-- _inbox/        Drafts, raw notes, and working material
|-- _system/       Vault maintenance notes
|-- zensical.toml     Zensical German/default site configuration
|-- zensical.en.toml  Zensical English site configuration
|-- zensical.pl.toml  Zensical Polish site configuration
|-- zensical.hu.toml  Zensical Hungarian site configuration
|-- zensical.it.toml  Zensical Italian site configuration
|-- zensical.nl.toml  Zensical Dutch site configuration
|-- zensical.el.toml  Zensical Greek site configuration
|-- zensical.es.toml  Zensical Spanish site configuration
|-- zensical.uk.toml  Zensical Ukrainian site configuration
|-- zensical.pt.toml  Zensical Portuguese site configuration
|-- zensical.cs.toml  Zensical Czech site configuration
`-- zensical.sk.toml  Zensical Slovak site configuration
```

Language folders use matching relative paths so translations can preserve page context:

```text
docs/de/spiele/example.md
docs/en/spiele/example.md
docs/pl/spiele/example.md
docs/hu/spiele/example.md
docs/it/spiele/example.md
docs/nl/spiele/example.md
docs/el/spiele/example.md
docs/es/spiele/example.md
docs/uk/spiele/example.md
docs/pt/spiele/example.md
docs/cs/spiele/example.md
docs/sk/spiele/example.md
```

Public URLs do not expose German as a language layer. German is the default root, other languages use their language code:

```text
/circuswiki/spiele/example/
/circuswiki/en/spiele/example/
/circuswiki/pl/spiele/example/
/circuswiki/hu/spiele/example/
/circuswiki/it/spiele/example/
/circuswiki/nl/spiele/example/
/circuswiki/el/spiele/example/
/circuswiki/es/spiele/example/
/circuswiki/uk/spiele/example/
/circuswiki/pt/spiele/example/
/circuswiki/cs/spiele/example/
/circuswiki/sk/spiele/example/
```

Configured languages are German (`de`), English (`en`), Polish (`pl`),
Hungarian (`hu`), Italian (`it`), Dutch (`nl`), Greek (`el`), Spanish (`es`),
Ukrainian (`uk`), Portuguese (`pt`), Czech (`cs`), and Slovak (`sk`). Dutch is used for the Circusatelier Woesh / West Flanders
context; Flemish is a regional variety, but `nl` is the correct standard site
language code. Czech uses `cs` and Slovak uses `sk`; Czechoslovakia was the former country, while Czech and Slovak are separate languages today. Portuguese uses the general `pt` code unless a regional variant such as Brazilian Portuguese is needed later.

The build creates an ignored `.build/` staging directory so Zensical can see each language as its own root while source content stays organized in `docs/<lang>/`. Shared generated-site assets from `site-assets/` are copied into each staged language root.

The language selector is configured with root links, then adjusted in the browser to preserve the current path across languages.

## Local Setup

Create a Python environment and install Zensical:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Preview the default/German site only:

```powershell
python tools/stage_multilang.py
zensical serve
```

This is useful for quick checks, but it serves only `zensical.toml` and does not
run the multilingual post-build steps. Do not use plain `zensical serve` to test
language switching, fallback pages, or hover previews; hover previews depend on
the augmented generated sitemap.

Preview the compiled multilingual site:

```powershell
powershell -ExecutionPolicy Bypass -File tools/serve_multilang.ps1
```

Open:

```text
http://127.0.0.1:8000/circuswiki/
```

Use this command when checking the language switcher, translated pages, fallback
pages, hover previews, or the same URL shape used on GitHub Pages. It builds all
language configs first, augments the generated sitemaps, then serves the generated
`site/` directory with `/circuswiki/` mapped locally.

Available options:

```powershell
# Use another port if 8000 is busy
powershell -ExecutionPolicy Bypass -File tools/serve_multilang.ps1 -Port 8765

# Serve the existing site/ output without rebuilding
powershell -ExecutionPolicy Bypass -File tools/serve_multilang.ps1 -NoBuild

# Bind to all network interfaces for device testing on the local network
powershell -ExecutionPolicy Bypass -File tools/serve_multilang.ps1 -HostAddress 0.0.0.0
```

Expected local URLs:

```text
http://127.0.0.1:8000/circuswiki/
http://127.0.0.1:8000/circuswiki/en/
http://127.0.0.1:8000/circuswiki/pl/
http://127.0.0.1:8000/circuswiki/hu/
http://127.0.0.1:8000/circuswiki/it/
http://127.0.0.1:8000/circuswiki/nl/
http://127.0.0.1:8000/circuswiki/el/
http://127.0.0.1:8000/circuswiki/es/
http://127.0.0.1:8000/circuswiki/uk/
http://127.0.0.1:8000/circuswiki/pt/
http://127.0.0.1:8000/circuswiki/cs/
http://127.0.0.1:8000/circuswiki/sk/
```

Build all language sites:

```powershell
powershell -ExecutionPolicy Bypass -File tools/build_multilang.ps1
```

## GitHub Pages

The repository includes an Actions-based Pages workflow in `.github/workflows/pages.yml`.
It builds the ignored `site/` directory and uploads it as a GitHub Pages artifact.

The build base path is environment driven:

```powershell
$env:CIRCUSWIKI_SITE_BASE_PATH = "/circuswiki/"
$env:CIRCUSWIKI_SITE_URL = "https://nica-ev.github.io/circuswiki/"
powershell -ExecutionPolicy Bypass -File tools/build_multilang.ps1
```

If these variables are not set, the build defaults to the main public URL shape:

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

The Pages workflow uses the public repository URL shape:

```text
https://nica-ev.github.io/circuswiki/
https://nica-ev.github.io/circuswiki/en/
https://nica-ev.github.io/circuswiki/pl/
https://nica-ev.github.io/circuswiki/hu/
https://nica-ev.github.io/circuswiki/it/
https://nica-ev.github.io/circuswiki/nl/
https://nica-ev.github.io/circuswiki/el/
https://nica-ev.github.io/circuswiki/es/
https://nica-ev.github.io/circuswiki/uk/
https://nica-ev.github.io/circuswiki/pt/
https://nica-ev.github.io/circuswiki/cs/
https://nica-ev.github.io/circuswiki/sk/
```

GitHub Pages must be enabled for the repository with "GitHub Actions" as the
Pages source. After that, pushes to `main` or manual workflow runs deploy the
compiled multilingual site.

## Translation Console

The repo includes a local web console for translation workflow experiments and health checks:

Translation architecture notes, including canonical source-language rules and
future fallback behavior, live in `_system/translation-architecture.md`.

```powershell
powershell -ExecutionPolicy Bypass -File tools/dev_console.ps1
```

Open:

```text
http://127.0.0.1:8787
```

The local console can:

- list source pages for the selected source language
- inspect the matching target path for the selected target language
- report missing, outdated, or inconsistent translations
- translate one selected Markdown file through an OpenAI-compatible API

German is the current default site language, but not a permanent source-language
rule. Translation tooling should translate from each page's canonical original
language as defined by metadata whenever possible.

During multilingual staging, missing language versions are generated as static
fallback pages. For example, if a German page has no English translation yet,
`/circuswiki/en/example/` should still resolve and show a visible "translation
missing" message with a link to the available source/fallback version.

The console's Vault Health tab includes a deterministic metadata repair tool.
It only fixes values that can be inferred safely, such as `lang`,
`translation_id`, `translation_status`, `translation_source_lang`, and
`translation_source`. It intentionally leaves stale hashes, missing model names,
and missing timestamps visible until translation or review happens.

The Batch Translate tab uses a required plan-first workflow. Planning does not
call the translation API; it only selects candidate files, applies `max_files`,
counts source characters, and shows the candidate list. Generated aggregate
pages such as `sitemap.md` are excluded from batch translation plans because
they duplicate links to real pages and can be disproportionately expensive.
Running the plan then processes only those planned files and shows progress file
by file.

The Original Graph tab visualizes explicit Markdown links and Obsidian wikilinks
between canonical original pages. Links may resolve through translated files,
but edges are normalized back to each target page's canonical original
translation group. `sitemap.md` is excluded by default because it links to many
pages and pollutes the graph. The tab includes controls for label visibility,
zoom, repulsion, gravity, and edge length.

API credentials are read from local environment variables and are not stored in the repo:

```powershell
$env:OPENROUTER_API_KEY = "..."
$env:OPENROUTER_MODEL = "google/gemini-2.0-flash-001"
```

Optional:

```powershell
$env:OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
```

The same workflow is available from the command line:

```powershell
python tools/translation_cli.py health --source-lang de --target-lang en
python tools/translation_cli.py inspect "docs/de/index.md" --source-lang de --target-lang en
python tools/translation_cli.py translate "docs/de/index.md" --source-lang de --target-lang en --dry-run
python tools/translation_cli.py translate "docs/de/index.md" --source-lang de --target-lang en
python tools/translation_cli.py translate-metadata "docs/de/index.md" --source-lang de --target-lang en --dry-run
python tools/translation_cli.py metadata-plan --target-lang en --source-lang all --reason metadata_hash_mismatch --max-files 25
```

Translation writes only target files. It splits Markdown into frontmatter and body. Full translation translates the Markdown body, repairs local link targets, translates frontmatter `title` and `description`, copies non-translation source metadata, and preserves target-local fields where possible.

Body and metadata freshness are tracked separately:

```yaml
lang: en
title: Translated title
description: Translated description
translation_id: ...
translation_source: docs/de/example.md
translation_source_body_hash: ...
translation_source_metadata_hash: ...
translation_source_hash: ... # legacy body-hash alias during migration
translation_model: ...
translation_status: machine-translated
translation_updated: ...
translation_metadata_model: ...
translation_metadata_status: machine-translated
translation_metadata_updated: ...
```

Unknown frontmatter fields are preserved instead of re-dumped.

## Tooling Maintenance

Tooling architecture and local API contracts are documented under `tools/`:

- `tools/README.md`: commands and dev-console endpoint contracts
- `tools/ARCHITECTURE.md`: current tooling boundaries and next refactor targets
- `tools/ARCHITECTURE_REVIEW.md`: closed review status and remaining risks
- `tools/AGENTS.md`: additional rules for tooling changes

Use the registry sync dry-run after changing languages or site URL settings:

```powershell
python tools/sync_configs.py
```

## Notes

- Obsidian setup is part of the repository and should not be removed during site cleanup.
- Site pages live in language folders below `docs/`.
- Shared images live in `docs/img/`.
- Generated staging and output belong in `.build/` and `site/`; both are ignored by Git.
- API keys belong in local environment variables or `.env`, never in committed files.

## License

Content is licensed under CC BY-SA 4.0 unless stated otherwise.
