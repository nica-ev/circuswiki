---
created: 2026-06-14 23:15:13
update: 2026-06-15 04:02:00
status: draft
scope: tools, tools/dev_console
---

# Dev Console And Tooling Refactor Plan

This is the working implementation note for the full tooling architecture refactor.
It is intended as the task tracker for a longer cleanup effort.

The goal is not only to make the dev-console UI nicer. The goal is to end with a stable, modular architecture across the local tooling codebase: Python services, API routes, frontend shell, feature modules, and layout system.

## Architecture Goals

- Keep domains separated: translation, metadata, health, dynamic content, links, navigation, graph, cleanup, Obsidian utilities.
- Keep adapters thin: CLI, dev-console routes, and frontend API clients should delegate to domain services.
- Keep business logic outside `tools/dev_console`.
- Keep UI shell, feature state, rendering, API clients, and layout concerns separated.
- Keep file writes explicit and isolated.
- Keep LLM/API calls centralized through one client.
- Keep code simple enough to maintain without introducing a frontend framework.
- Preserve behavior while changing structure incrementally.
- Support a fixed-size local app window and future Tauri packaging without another architectural rewrite.

## Target Python Shape

```text
tools/
  core/
    paths.py
    env.py
    llm.py
    json_api.py
    results.py
  translation/
    models.py
    discovery.py
    hashes.py
    metadata_policy.py
    health.py
    planning.py
    body_translation.py
    metadata_translation.py
    service.py
    workflow.py              # temporary compatibility facade during migration
    link_repair.py
    link_repair_workflow.py
    cleanup.py
    original_graph.py
  dynamic/
    models.py
    blocks.py
    base_schema.py
    render.py
    scanner.py
    refresh.py
    obsidian_backend.py
    workflow.py              # temporary compatibility facade during migration
  navigation/
    model.py
    discovery.py
    render.py
    labels.py
    service.py
    workflow.py              # compatibility facade
  base_labels/
    config.py
    parser.py
    planning.py
    translation.py
    materialize.py
    service.py
```

The compatibility facades keep existing CLI/dev-console imports stable while internals are split. They should shrink over time and eventually either disappear or become intentional public service entry points.

## Target Dev Console Backend Shape

```text
tools/dev_console/
  server.py
  routes/
    __init__.py
    registry.py
    config.py
    translation.py
    metadata.py
    health.py
    dynamic.py
    base_labels.py
    links.py
    navigation.py
    graph.py
    cleanup.py
    obsidian.py
```

Route modules stay thin. They parse request data, call Python service functions, and return JSON. They do not implement domain policy.

Target route style:

```python
def register(registry: RouteRegistry) -> None:
    registry.get("/api/dynamic/scan", scan)
    registry.get("/api/dynamic/check", check)
    registry.post("/api/dynamic/refresh", refresh)
```

## Target Frontend Shape

```text
tools/dev_console/static/
  index.html
  app.js
  api/
    client.js
    config.js
    translation.js
    metadata.js
    health.js
    dynamic.js
    baseLabels.js
    links.js
    navigation.js
    graph.js
    cleanup.js
    obsidian.js
  core/
    dom.js
    events.js
    html.js
    state.js
    toolModule.js
    shell.js
    layout.js
  features/
    translateSingle.js
    translateBatch.js
    metadataBatch.js
    healthMatrix.js
    dynamicPages.js
    baseLabels.js
    linkRepair.js
    sourceLinkStyle.js
    navigation.js
    originalGraph.js
    cleanup.js
  styles/
    tokens.css
    shell.css
    controls.css
    panes.css
    tables.css
    features.css
```

No frontend framework for this refactor. Plain JavaScript modules are enough if boundaries are strict.

## UI Model

The UI should use a persistent app shell:

- Fixed top bar for app title, global status, and active workspace context.
- Left navigation or compact rail for primary groups.
- Secondary navigation for tools inside the selected group.
- One active tool viewport at a time.
- Optional bottom/right output drawer for logs and raw JSON, scoped to the active tool.
- No full-page scrolling in normal desktop use.
- Scroll only inside explicit panes: lists, logs, tables, matrix panels, and code editors.

Primary groups:

- Translate
- Dynamic Content
- Links
- Structure
- Maintenance

Initial tool mapping:

- Translate
  - Single File
  - Batch Body
  - Batch Metadata
  - Translation Health
- Dynamic Content
  - Dynamic Pages
  - Base Labels
- Links
  - Translation Link Repair
  - Source Link Style
- Structure
  - Navigation
  - Original Graph
- Maintenance
  - Cleanup
  - Obsidian

## Frontend Module Contract

Each feature module should expose one object:

```js
export const feature = {
  id: "dynamic-pages",
  label: "Dynamic Pages",
  group: "dynamic-content",
  mount(root, context) {},
  unmount() {},
  refresh() {},
};
```

Feature modules own:

- Their own local state.
- Their own DOM under `root`.
- Their own event listeners.
- Their own render functions.
- Their own busy state.
- Their own logs/output.

Feature modules must not:

- Query DOM outside their root, except through shell services.
- Mutate another feature's state.
- Register global event listeners without cleanup behavior.
- Depend on another feature's internal DOM IDs.
- Add IDs that need to be known by global busy logic.

Shared frontend context:

```js
{
  api,
  config,
  shell,
  openInObsidian,
  notify,
}
```

## Refactor Tasks

- [x] Phase 0: Stabilize Current Branch
  - [x] Keep the existing `server.py` JSON helper fix.
  - [x] Keep the existing root refactor plan note updated as decisions change.
  - [x] Preserve `.obsidian/workspace.json` because it is an accepted local workspace change.
  - [x] Run a quick dev-console smoke test after each structural step.
  - [x] Avoid behavior changes unless needed for architecture.
  - [x] Keep commits small enough to review.
  - [x] Dependency: none.

- [x] Phase 1: Establish Core Python Infrastructure
  - [x] Create `tools/core/paths.py` for `ROOT`, `DOCS`, config paths, and safe relative path helpers.
  - [x] Create `tools/core/env.py` for `.env` loading and environment value lookup.
  - [x] Create `tools/core/llm.py` for OpenAI-compatible chat calls.
  - [x] Move shared chat URL normalization into `core.llm`.
  - [x] Move shared code-fence stripping into `core.llm` or a focused text utility.
  - [x] Create a small typed result/error pattern only if it simplifies call sites. Not needed yet; skipped intentionally.
  - [x] Add unit tests for env loading, chat URL normalization, and JSON-response parsing.
  - [x] Dependency: Phase 0.

- [x] Phase 2: Replace Duplicated LLM Clients
  - [x] Update `translation.workflow` model calls to use `core.llm`.
  - [x] Update `navigation.workflow` model calls to use `core.llm`.
  - [x] Update `base_labels.py` model calls to use `core.llm`.
  - [x] Preserve model names, prompts, headers, timeouts, and error messages where practical.
  - [x] Remove duplicated `.env` loaders from domain modules.
  - [x] Remove duplicated `chat_completions_url()` helpers from domain modules.
  - [x] Dependency: Phase 1.

- [x] Phase 3: Establish Backend Route Registry
  - [x] Create `tools/dev_console/routes/`.
  - [x] Create `tools/dev_console/routes/registry.py`.
  - [x] Define `RouteRegistry` with `get()`, `post()`, and `dispatch()` methods.
  - [x] Centralize route exception handling.
  - [x] Centralize query and JSON payload helpers.
  - [x] Add route registry tests for matched route, unknown route, route exception, and invalid method.
  - [x] Dependency: Phase 0.

- [x] Phase 4: Split Dev Console Routes By API Domain
  - [x] Create `routes/config.py` for `/api/config`.
  - [x] Create `routes/translation.py` for single-file body translation endpoints.
  - [x] Create `routes/metadata.py` for metadata translation and metadata batch endpoints.
  - [x] Create `routes/health.py` for translation health, vault health, pages, and page inspection.
  - [x] Create `routes/dynamic.py` for dynamic page endpoints.
  - [x] Create `routes/base_labels.py` for base-label endpoints.
  - [x] Create `routes/links.py` for link repair and source link style endpoints.
  - [x] Create `routes/navigation.py` for navigation endpoints.
  - [x] Create `routes/graph.py` for original graph endpoints.
  - [x] Create `routes/cleanup.py` for cleanup endpoints.
  - [x] Create `routes/obsidian.py` for Obsidian open endpoint.
  - [x] Update `server.py` to register route modules.
  - [x] Keep old route modules only until all endpoints are migrated.
  - [x] Delete old route modules after migration.
  - [x] Dependency: Phase 3.

- [x] Phase 5: Split Translation Domain Models And Discovery
  - [x] Create `tools/translation/models.py` for `PageStatus`, `VaultPage`, and future typed result objects.
  - [x] Create `tools/translation/discovery.py` for listing languages, sources, reading vault pages, grouping pages, source-language selection, and primary-page selection.
  - [x] Move `derive_translation_id()` and `derive_translation_id_from_relative()` to discovery or a focused identity module.
  - [x] Keep `workflow.py` as a facade exporting old function names.
  - [x] Update tests to import new modules where useful, but preserve old imports during migration.
  - [x] Dependency: Phase 1.

- [x] Phase 6: Split Translation Hash And Metadata Policy
  - [x] Create `tools/translation/hashes.py` for body, metadata, legacy, localized, and structural hash functions.
  - [x] Create `tools/translation/metadata_policy.py` for translatable fields, source-owned fields, target-owned fields, merge policy, difference detection, and metadata translation need detection.
  - [x] Keep `tools/translation/metadata.py` as low-level frontmatter text manipulation only.
  - [x] Move `translation_metadata.json` loading into translation config used by metadata policy.
  - [x] Add focused tests for source-owned vs target-owned metadata behavior.
  - [x] Dependency: Phase 5.

- [x] Phase 7: Split Translation Health And Repair
  - [x] Create `tools/translation/health.py` for `vault_health_matrix()`, `health_summary()`, and `inspect_page()`.
  - [x] Extract validation rules from `vault_health_matrix()` into small named functions.
  - [x] Move deterministic metadata repair into a focused repair module or service function.
  - [x] Keep issue names stable unless intentionally changed.
  - [x] Add tests for rule outputs on representative source/original/translated pages.
  - [x] Dependency: Phases 5 and 6.

- [x] Phase 8: Split Translation Planning
  - [x] Create `tools/translation/planning.py`.
  - [x] Extract shared candidate filtering: source language, target language, reason, path filter, max files.
  - [x] Keep body-translation and metadata-translation reason policies separate but powered by shared planning mechanics.
  - [x] Preserve existing plan response shapes for UI compatibility.
  - [x] Dependency: Phases 5, 6, and 7.

- [x] Phase 9: Split Translation Execution Services
  - [x] Create `tools/translation/body_translation.py` for static body segments, dynamic-block-aware body translation, link repair after model output, and prompt rendering.
  - [x] Create `tools/translation/metadata_translation.py` for metadata prompt and metadata model response parsing.
  - [x] Create `tools/translation/service.py` for orchestration: translate file, translate metadata only, batch item execution.
  - [x] Separate transform from persistence enough for service boundaries; deeper pure transform split remains optional.
  - [x] Preserve dry-run semantics.
  - [x] Preserve existing CLI and dev-console response fields.
  - [x] Dependency: Phases 2, 5, 6, 8.

- [x] Phase 10: Refactor Dynamic Domain Internals
  - [x] Create `tools/dynamic/models.py` for dynamic page result structures if useful.
  - [x] Create `tools/dynamic/base_schema.py` for Base view order and display-label resolution.
  - [x] Move Base schema parsing out of `dynamic.render`.
  - [x] Create `tools/dynamic/scanner.py` for finding and summarizing dynamic pages.
  - [x] Create `tools/dynamic/refresh.py` for sync and render/write orchestration.
  - [x] Keep `dynamic.workflow` as compatibility facade during migration.
  - [x] Dependency: Phase 1.

- [x] Phase 11: Refactor Base Label Domain
  - [x] Decide whether `base_labels.py` becomes a package or remains as facade over package modules.
  - [x] Create parser/config/planning/translation/materialize modules if moving to a package.
  - [x] Keep display-name parsing independent from LLM translation.
  - [x] Keep config persistence independent from materializing generated base files.
  - [x] Keep CLI behavior stable through `base_labels.cli`.
  - [x] Dependency: Phase 2.

- [x] Phase 12: Refactor Navigation Domain
  - [x] Extract nav model validation and normalization to `navigation/model.py`.
  - [x] Extract page discovery and title lookup to `navigation/discovery.py`.
  - [x] Extract TOML nav rendering/application to `navigation/render.py`.
  - [x] Extract label translation to `navigation/labels.py`.
  - [x] Keep `navigation/workflow.py` as compatibility facade during migration.
  - [x] Move nav scan and model-from-current-config orchestration to `navigation/service.py`.
  - [x] Dependency: Phase 2.

- [x] Phase 13: Define Frontend Shell Skeleton
  - [x] Create `static/core/shell.js`.
  - [x] Create `static/core/toolModule.js`.
  - [x] Create `static/core/state.js` only for app-level shared state.
  - [x] Create `static/core/dom.js` and move existing DOM helpers there.
  - [x] Create `static/core/html.js` for safe HTML/log text helpers.
  - [x] Create `static/core/events.js` for scoped listener registration and cleanup.
  - [x] Create `static/core/layout.js` for layout helpers.
  - [x] Make `static/app.js` only bootstrap config, create shell, register features, and start app.
  - [x] Dependency: Phase 4 can be parallel, but frontend route names should remain stable.

- [x] Phase 14: Replace Flat Tabs With App Navigation Model
  - [x] Define primary groups in a data structure.
  - [x] Define feature metadata in a registry.
  - [x] Render primary navigation from registry data.
  - [x] Render secondary navigation from active group.
  - [x] Keep only the active existing tool panel visible while feature-module mounting is prepared.
  - [x] Preserve current tool names during first migration.
  - [x] Dependency: Phase 13.

- [x] Phase 15: Create Fixed-Window Layout System
  - [x] Rewrite shell HTML to use an app viewport instead of full-page sections.
  - [x] Introduce `app-sidebar`, `app-shell`, `app-header`, `app-main`, `tool-header`, `tool-body`, and `tool-output`.
  - [x] Remove default body/page scrolling for normal desktop layout.
  - [x] Define explicit scroll regions for panes, lists, logs, matrices, and editors.
  - [x] Define minimum practical window size in the shell CSS.
  - [x] Preserve responsive fallback for narrow screens.
  - [x] Dependency: Phase 14.

- [x] Phase 16: Split Frontend API Clients
  - [x] Keep `static/api/client.js` as the low-level fetch wrapper.
  - [x] Create feature API modules for endpoint groups.
  - [x] Move endpoint strings and payload shaping out of feature render code.
  - [x] Make API modules return backend payloads directly without hiding important fields.
  - [x] Dependency: Phase 13.

- [x] Phase 17: Migrate Feature: Single File Translation
  - [x] Create `features/translateSingle.js`.
  - [x] Move page list loading, details rendering, body translation, metadata translation, and language selectors into the module.
  - [x] Keep local state private to the module.
  - [x] Scope lifecycle ownership through active feature panels; full root-local query migration is no longer required for duplicate-listener safety.
  - [x] Remove related code from old `app.js`.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 18: Migrate Feature: Translation Health
  - [x] Create `features/healthMatrix.js`.
  - [x] Move vault health state, matrix rendering, matrix window controls, and repair action into the module.
  - [x] Make pointer listeners removable when the future shell supports real feature unmounting.
  - [x] Keep matrix layout based on pane dimensions.
  - [x] Dependency: Phases 13, 14, 15, 16.

- [x] Phase 19: Migrate Feature: Batch Translation
  - [x] Create `features/translateBatch.js`.
  - [x] Move batch plan, batch run, progress display, filters, and result log.
  - [x] Keep batch run state local; cancellable-ready remains a later enhancement.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 20: Migrate Feature: Batch Metadata
  - [x] Create `features/metadataBatch.js`.
  - [x] Move metadata plan, metadata run, progress display, filters, and result log.
  - [x] Preserve metadata batch configuration display behavior.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 21: Migrate Feature: Dynamic Pages
  - [x] Create `features/dynamicPages.js`.
  - [x] Move dynamic scan, check, preview, selected refresh, all-language refresh, details, and log.
  - [x] Keep Obsidian dependency status visible in the output pane.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 22: Migrate Feature: Base Labels
  - [x] Create `features/baseLabels.js`.
  - [x] Move scan, plan, translate, materialize, base filter, language filter, details, and log.
  - [x] Keep persisted label config path visible in the summary.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 23: Migrate Feature: Link Repair
  - [x] Create `features/linkRepair.js`.
  - [x] Move translated-file link repair scan, preview, selected repair, all-safe repair, selection state, and log.
  - [x] Keep selection state local.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 24: Migrate Feature: Source Link Style
  - [x] Create `features/sourceLinkStyle.js`.
  - [x] Move source style scan, preview, selected repair, all-safe repair, selection state, and details.
  - [x] Keep it under the Links group but separate from translation link repair.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 25: Migrate Feature: Navigation
  - [x] Create `features/navigation.js`.
  - [x] Move canonical model editor, scan, init, translate labels, preview, apply, diagnostics, and log.
  - [x] Use a split-pane editor/preview layout inside the fixed tool viewport after Phase 15.
  - [x] Dependency: Phases 13, 14, 15, 16.

- [x] Phase 26: Migrate Feature: Original Graph
  - [x] Create `features/originalGraph.js`.
  - [x] Move graph loading, chart lifecycle, force controls, zoom, drag, resize, details, and diagnostics.
  - [x] Ensure chart cleanup happens when the future shell supports real feature unmounting.
  - [x] Avoid persistent global chart references outside the feature.
  - [x] Dependency: Phases 13, 14, 15, 16.

- [x] Phase 27: Migrate Feature: Cleanup
  - [x] Create `features/cleanup.js`.
  - [x] Move orphan scan, delete selected, delete all-safe, details, selection state, and log.
  - [x] Keep destructive actions confirmable.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 28: Migrate Feature: Obsidian Utility
  - [x] Create `features/obsidian.js` only if a visible tool panel is useful.
  - [x] Keep Obsidian path button rendering available as a shared core helper.
  - [x] Dependency: Phases 13, 14, 16.

- [x] Phase 29: Remove Old Frontend Monolith
  - [x] Delete obsolete code from old `app.js`.
  - [x] Ensure no feature code depends on global DOM IDs outside its root after shell roots exist.
  - [x] Ensure no global busy function remains.
  - [x] Ensure all global pointer, resize, and keyboard listeners are owned and cleaned up when unmount support lands.
  - [x] Move feature mount, activation, resize, logging, and teardown orchestration out of `app.js`.
  - [x] Dependency: Phases 17 through 28.

- [x] Phase 30: CSS Cleanup
  - [x] Split CSS into token, shell, controls, pane, table, and feature files.
  - [x] Keep new shared layout selectors class-based; remaining feature selectors stay scoped to feature CSS.
  - [x] Remove viewport-height hacks where pane sizing should be managed by shell layout.
  - [x] Define a compact density scale for tool controls.
  - [x] Define visual patterns for safe, primary, destructive, and disabled actions.
  - [x] Dependency: Phase 15 and after each migrated feature has stable markup.

- [x] Phase 31: UX Pass For Fixed Tool Window
  - [x] Define target desktop window size.
  - [x] Test all tools at target size.
  - [x] Ensure no page-level scrolling in normal workflows.
  - [x] Ensure logs do not crowd out primary task panes.
  - [x] Ensure batch/progress workflows remain visible while running.
  - [x] Ensure destructive operations are harder to trigger accidentally.
  - [x] Dependency: Phases 15, 17 through 28, 30.

- [x] Phase 32: Tests And Smoke Scripts
  - [x] Add backend route registry unit tests.
  - [x] Add focused tests for split translation modules.
  - [x] Add focused tests for shared LLM client with mocked HTTP.
  - [x] Add lightweight frontend smoke checks if practical.
  - [x] Add a dev-console smoke command that starts the server and hits key API endpoints.
  - [x] Add a checklist for manual UI smoke tests.
  - [x] Dependency: Phases 1 through 30.

Manual UI smoke checklist:

- [x] Start `powershell -ExecutionPolicy Bypass -File tools/dev_console.ps1`.
- [x] Confirm the app opens without duplicate `/api/config` or `/api/health` 404s.
- [x] Confirm primary sidebar groups switch correctly.
- [x] Confirm secondary tool navigation switches within each group.
- [x] Confirm no page-level scrolling at the target desktop size.
- [x] Confirm each tool panel scrolls only inside its intended list, table, log, or editor panes.
- [x] Confirm single-file translation page list, details, dry-run, metadata translation, and body translation controls still respond.
- [x] Confirm vault health matrix loads, range handles drag, and metadata repair progress remains visible.
- [x] Confirm batch body and batch metadata plan/run controls still enable and disable correctly.
- [x] Confirm dynamic pages scan, preview, and refresh controls still show output.
- [x] Confirm base labels scan, plan, translate, and materialize controls still show output.
- [x] Confirm link repair and source link style selection, preview, and repair actions still work.
- [x] Confirm navigation scan, preview, apply, and model editor panes remain usable.
- [x] Confirm original graph loads, resizes, zooms, drags, and shows diagnostics.
- [x] Confirm cleanup deletion buttons are visually destructive and still require confirmation.

- [x] Phase 33: Documentation Cleanup
  - [x] Update README dev-console section if commands or behavior change.
  - [x] Add short architecture note under `_system/` after the refactor stabilizes.
  - [x] Keep this root planning file until the refactor is complete.
  - [x] Dependency: Refactor substantially complete.

## Migration Rules

- [x] Preserve working behavior at each phase.
- [x] Do not combine architectural migration with unrelated feature changes.
- [x] Prefer compatibility facades while migrating large Python modules.
- [x] Delete old code immediately after each migrated area is stable.
- [x] Keep route names stable unless there is a clear reason to rename.
- [x] Keep backend business logic outside `dev_console`.
- [x] Keep feature modules independent.
- [x] Do not introduce a frontend framework during this refactor.
- [x] Do not introduce Tauri during this refactor.
- [x] Keep generated outputs out of commits unless the task explicitly requires them.

## Completion Criteria

- [x] `tools/translation/workflow.py` is no longer a large mixed-responsibility module.
- [x] Translation discovery, hashes, metadata policy, health, planning, and execution are separate modules.
- [x] Dynamic Base schema resolution is separate from Markdown rendering.
- [x] Navigation model/render/label translation concerns are separated.
- [x] Base-label parsing/config/planning/translation/materialization concerns are separated.
- [x] All LLM calls use one shared core client.
- [x] Dev-console routes are registered through a registry and split by API domain.
- [x] `static/app.js` is a small bootstrap file.
- [x] Each frontend feature is independently mounted and unmounted.
- [x] App navigation is grouped and data-driven.
- [x] The UI has a fixed-window shell with explicit scroll regions.
- [x] No global busy function knows about every button.
- [x] No global state object contains every feature's state.
- [x] No hidden full-page tab panels are permanently rendered as the primary structure.
- [x] Existing CLI workflows still work.
- [x] Existing dev-console workflows still work.
- [x] Tests pass.

## Post-Refactor Stabilization Notes

- [x] Fixed feature log functions so async work that completes after a tab unmount does not write into missing DOM nodes.
- [x] Fixed the graph tab to use a dedicated layout instead of the generic vault-health grid.
- [x] Kept the original graph as an ECharts force graph. The force layout is required to make the structure useful; do not replace it with a deterministic/static layout as a workaround.
- [x] Restored the graph chart's concrete viewport sizing contract (`68vh`, minimum height, internal canvas fill). ECharts is sensitive to ambiguous nested-grid `height: 100%` sizing during mount.
- [x] Confirmed the validation commands pass after stabilization:
  - [x] `python tools/dev_console_static_check.py`
  - [x] `python -m unittest discover -s tools/tests`
  - [x] `python tools/dev_console_smoke.py`

















