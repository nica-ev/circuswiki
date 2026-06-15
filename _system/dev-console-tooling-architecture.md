---
created: 2026-06-15 00:00:00
update: 2026-06-15 00:00:00
status: draft
scope: tools, tools/dev_console
---

# Dev Console Tooling Architecture

This note records the current target architecture for the local tooling refactor.
It complements `DEV_CONSOLE_REFACTOR_PLAN.md`, which remains the active task tracker until the refactor is complete.

## Boundaries

- `tools/core/` contains shared infrastructure only: paths, environment loading, language registry access, and OpenAI-compatible LLM calls.
- Domain packages contain business logic: `tools/translation/`, `tools/dynamic/`, `tools/navigation/`, and `tools/base_labels/`.
- `tools/dev_console/routes/` contains HTTP adapters only. Route modules parse request data, call domain services, and return JSON.
- `tools/dev_console/static/api/` contains frontend endpoint clients.
- `tools/dev_console/static/features/` contains feature-specific UI state, rendering, actions, and logs.
- `tools/dev_console/static/core/` contains shell helpers, event scopes, HTML escaping, DOM helpers, and layout helpers.
- `tools/dev_console/static/app.js` is the bootstrap and app-shell entry point. It should not contain domain behavior.

## Compatibility Facades

Some historic import paths remain as compatibility facades:

- `tools/translation/workflow.py`
- `tools/dynamic/workflow.py`
- `tools/navigation/workflow.py`

These files should stay thin. New behavior should go into focused domain modules or service modules first, then be re-exported only when an existing caller still depends on the old path.

## Dev Console UI

The console uses plain JavaScript modules, not a frontend framework.

The UI model is:

- one fixed app shell
- primary sidebar groups
- secondary tool navigation inside the selected group
- one active tool viewport
- explicit scroll regions for lists, logs, matrices, editors, and tables
- feature modules own their own state and busy handling

Avoid adding cross-feature DOM queries or global state. If a feature needs shared information, pass it through `features/lifecycle.js` or a small core service.

## Graph View

The original graph is intentionally an ECharts force graph. The force layout is part of the tool's value because it reveals structure and hub relationships. Do not replace it with a static or deterministic layout to work around rendering bugs.

The graph chart needs a concrete viewport-sized rendering contract. ECharts can fail or blank out when initialized inside ambiguous nested-grid `height: 100%` containers during panel mount. Keep the graph chart container explicitly sized, currently `68vh` with a minimum height, and let ECharts resize against that concrete box.

The graph feature may have cached data across tab switches, but the chart instance itself is disposable UI state. It should be recreated when the feature mounts and disposed when it unmounts.

## Validation

Run these checks after architecture changes:

```powershell
python tools/dev_console_static_check.py
python -m unittest discover -s tools/tests
python tools/dev_console_smoke.py
```

Use the browser-based manual smoke checklist in `DEV_CONSOLE_REFACTOR_PLAN.md` for layout and interaction validation.

## Rules

- Keep backend business logic outside `tools/dev_console`.
- Keep route modules thin.
- Keep feature modules independent.
- Keep LLM calls centralized through `tools/core/llm.py`.
- Do not reintroduce old MkDocs, Cursor, or Task Master tooling.
- Do not introduce Tauri or a frontend framework during this refactor.
