---
created: 2026-10-11 00:00:00
update: 2026-10-11 00:00:00
status: implemented
scope: tools/translation, tools/core, tools/dev_console
---

# Server-side translation jobs: implementation plan

This is the durable execution plan for ADR-002. Update the checklist and progress
log after every completed milestone. If work is interrupted, resume from the first
unchecked milestone after reading the latest progress entry and running the
targeted tests listed there.

## Invariants

- Every Markdown source file follows the same translation rules. Do not add
  CircusFinder, importer, folder, or script-specific exceptions.
- Preserve the plan-first safeguard: planning performs no model calls, and a job
  contains only the reviewed plan candidates.
- Markdown and its translation provenance remain the content source of truth.
  SQLite contains disposable local execution state only.
- Use canonical original sources and the configured language registry.
- Never publish a translation when the source body or localized metadata changed
  after the item was planned.
- Unknown frontmatter fields and Obsidian Markdown constructs must remain intact.
- Keep backend business logic outside `tools/dev_console/routes/`.
- Keep `.cache/`, generated builds, API keys, and job databases out of Git.

## Target architecture

### Domain job manager

Add a focused module under `tools/translation/` that owns:

- SQLite schema creation and migrations for local job state;
- creation of a job from a reviewed batch plan;
- one-active-job enforcement;
- bounded `ThreadPoolExecutor` scheduling;
- item state transitions and attempt/error recording;
- pause, resume, cancel, failed-item retry, and shutdown;
- restart recovery of interrupted items;
- planned-source hash validation and completed-target reconciliation;
- aggregate status, throughput, ETA, worker, and error summaries.

Job states:

```text
queued -> running -> completed
                  -> failed
                  -> stale
queued/running -> cancelled
running on process exit -> queued on next start
```

Operational pause is stored separately from terminal job status so queued work is
not rewritten merely to pause dispatch.

### SQLite storage

Default database:

```text
.cache/dev_console/translation_jobs.sqlite3
```

Minimum tables:

- `translation_jobs`: identity, status, pause/cancel flags, model, prompt,
  configured/current concurrency, timestamps, and reviewed plan summary.
- `translation_job_items`: source/target identity, planned source hashes, reason,
  state, attempts, timings, result/error JSON, and actual/requested model data.

Use foreign keys, WAL mode, short transactions, per-operation connections, and
indexes for job/status lookup. Enforce target uniqueness within a job. The first
version permits one non-terminal job across the database.

### Worker and correctness flow

For each claimed item:

1. Check cancellation and pause state before dispatch.
2. Read the canonical source and compare body and localized-metadata hashes with
   the planned values.
3. If the target already records both planned hashes, mark the item completed as
   recovered without an API call.
4. Run the existing one-file translation service.
5. Immediately before the atomic replacement, re-read and verify the source
   hashes. If they changed, do not write and mark the item stale.
6. Persist the result or a bounded error message independently of other items.

The translation service will accept expected source hashes and use an atomic
temporary-file replacement. Single-file and CLI callers may omit the expectations
and retain their current behavior.

### Shared LLM cooldown

Extend `tools/core/llm.py` with a process-wide request gate:

- every attempt waits for any active cooldown before opening the request;
- `429` extends the shared cooldown using bounded `Retry-After` or exponential
  delay plus small jitter;
- expose a read-only snapshot for job status;
- keep existing bounded per-request retries for network and retryable HTTP errors.

Adaptive worker-count reduction is deferred unless real measurements show that a
shared cooldown and configurable fixed pool are insufficient. This keeps the first
implementation understandable while preventing retry storms.

### HTTP API

Add thin routes:

```text
POST /api/translation-jobs
GET  /api/translation-jobs/current
GET  /api/translation-jobs/{id}
GET  /api/translation-jobs/{id}/items
POST /api/translation-jobs/{id}/pause
POST /api/translation-jobs/{id}/resume
POST /api/translation-jobs/{id}/cancel
POST /api/translation-jobs/{id}/retry-failed
```

The route registry currently matches exact paths. Extend it with explicit dynamic
path matching or use a single action endpoint only if that produces a smaller,
well-tested interface. Invalid state transitions return `409`; validation errors
return `400`; missing jobs return `404`.

The server constructs and starts the manager, makes it available to route
adapters, and shuts it down gracefully.

### Frontend

Replace the per-file browser loop with:

- start reviewed plan as a server job;
- reconnect to the current job when the feature mounts;
- poll while a job is non-terminal and stop polling on unmount;
- display counts, progress, rolling throughput/ETA, concurrency, cooldown, and
  recent failures;
- provide pause, resume, cancel, and retry-failed controls;
- disable starting another job while one is non-terminal;
- refresh vault health once a job reaches a terminal state.

The job keeps running when the feature is unmounted or the browser closes.

## Implementation milestones

- [x] M0: Inspect current architecture and record ADR plus resumable plan.
- [x] M1: Add source-hash expectation checks and atomic translation writes.
- [x] M2: Add shared LLM cooldown with focused unit tests.
- [x] M3: Implement SQLite job store, manager, recovery, and unit tests.
- [x] M4: Integrate manager lifecycle and translation-job HTTP routes with route
  tests.
- [x] M5: Replace frontend batch loop with job controls, polling, progress, and
  error rendering.
- [x] M6: Update tooling documentation and architecture notes.
- [x] M7: Run targeted tests and full tooling checks.
- [ ] M8: Run the dev console and verify the batch workflow in the Playwright MCP,
  including reload/reconnect and pause/resume without making real model calls.
  **Blocked:** the required browser runtime reported that no browser instance was
  available in this frontend on 2026-10-11. Do not substitute another browser
  mechanism; rerun this milestone when Playwright MCP is available.
- [x] M9: Review the diff for unrelated changes and mark implementation complete.

## Verification strategy

### Unit tests

- Atomic write leaves the old target intact when source validation fails.
- A planned hash mismatch marks an item stale without invoking translation.
- Job creation persists exactly the reviewed candidates and rejects an overlapping
  active job.
- Multiple workers process distinct targets and never exceed configured
  concurrency.
- Item failure does not stop other items.
- Pause stops new claims; resume continues; cancel prevents new work.
- Restart recovery requeues interrupted items and recognizes already-written
  targets.
- Retry-failed resets only failed items.
- Shared `429` cooldown delays other workers and exposes status.
- Route validation and state-conflict responses are correct.

### Repository checks

```powershell
python -m unittest tools.tests.test_core_llm
python -m unittest tools.tests.test_translation_jobs
python -m unittest tools.tests.test_dev_console_routes
python tools/dev_console_static_check.py
python -m unittest discover -s tools/tests
python tools/dev_console_smoke.py
powershell -ExecutionPolicy Bypass -File tools/check.ps1
```

### Browser verification

Use the Playwright MCP against `http://127.0.0.1:8787` as required by
`AGENTS.md`. Use a test database and mocked/no-call job fixture or a completed
local job so verification cannot spend API credits. Confirm:

- an existing job appears after opening or reloading the batch tab;
- progress and job-state controls render correctly;
- pause/resume state survives reload;
- no legacy browser-side per-file requests are sent.

## Deferred work

- Distributed workers or external queue services.
- Concurrent independent batch jobs.
- Provider-specific batch APIs.
- Automatic model fallback or routing across different models.
- Automated concurrency tuning beyond the shared cooldown.
- Unifying metadata-only batch translation with this queue. The first delivery
  changes full-page batch translation only; the same manager can be generalized
  later after the primary workflow is proven.

## Progress log

### 2026-10-11 — M0 complete

- Confirmed the frontend currently executes full-page batches sequentially.
- Confirmed `ThreadingHTTPServer` can serve concurrent requests, while domain
  translation calls are synchronous and network-bound.
- Confirmed ordinary full-page translation performs body and localized-metadata
  calls before writing a target.
- Recorded ADR-002 and this implementation plan.
- Existing user changes were identified in CircusFinder content/import tooling and
  will be preserved.
- Next action: implement M1 in `tools/translation/service.py` with focused tests.

### 2026-10-11 — M1 complete

- Batch-plan candidates now snapshot body, localized-metadata, and structural
  metadata hashes.
- Full-page translation accepts expected hashes, rejects stale work before model
  calls, and revalidates the source immediately before writing.
- Full-page and metadata-only target writes now use same-directory temporary files
  and atomic replacement.
- Added `tools/tests/test_translation_service.py` covering atomic replacement,
  pre-call stale detection, and preservation of an existing target when the source
  changes during translation.
- Verification passed: `python -m unittest tools.tests.test_translation_service
  tools.tests.test_translation_workflow` (27 tests).
- Next action: implement M2 shared LLM cooldown and its focused tests.

### 2026-10-11 — M2 complete

- Added a process-wide request gate in `tools/core/llm.py`.
- Every model-request attempt observes the gate; `429` responses extend a shared
  cooldown using `Retry-After`/exponential delay plus bounded jitter.
- Exposed a read-only cooldown snapshot for job status and a controlled reset for
  tests.
- Preserved existing per-request retry bounds for HTTP and network failures.
- Verification passed: `python -m unittest tools.tests.test_core_llm
  tools.tests.test_translation_service` (13 tests).
- Next action: implement M3 SQLite persistence and the background worker manager.

### 2026-10-11 — M3 complete

- Added `tools/translation/jobs.py` with a WAL-mode SQLite store and bounded
  `ThreadPoolExecutor` manager.
- Implemented one-active-job enforcement, per-item state transitions, pause,
  resume, cancellation, failed-item retry, summaries, recent errors, and bounded
  item listing.
- Interrupted `running` items are requeued at startup. Existing targets whose
  provenance matches the planned hashes are reconciled as recovered without a
  model call.
- Worker failures are isolated; stale sources are classified separately; queued
  cancellation does not discard a currently running translation.
- Added seven focused tests for concurrency, stale detection, failure isolation,
  retry, pause/resume, cancellation, and restart reconciliation.
- Verification passed: `python -m unittest tools.tests.test_translation_jobs
  tools.tests.test_core_llm tools.tests.test_translation_service` (20 tests).
- Next action: implement M4 manager lifecycle and HTTP routes.

### 2026-10-11 — M4 complete

- The dev-console server now starts and shuts down one persistent translation job
  manager. The default database is `.cache/dev_console/translation_jobs.sqlite3`;
  a CLI override supports isolated tests.
- Extended the route registry with anchored named path parameters and explicit
  HTTP errors.
- Added create/current/detail/items and pause/resume/cancel/retry-failed routes.
- Added route tests for dynamic paths, manager delegation, and `409` state
  conflicts. The live smoke server returned `200` for the new current-job route.
- Verification passed: 17 route/job tests. The general smoke script's
  `/api/vault-health` request timed out while scanning the enlarged working vault;
  this occurred independently of the new endpoint, which passed.
- Next action: implement M5 frontend job controls, reconnection, and polling.

### 2026-10-11 — M5 and M6 complete

- Replaced the frontend per-file loop with server-job creation, current-job
  reconnection, one-second polling, and pause/resume/cancel/retry controls.
- The UI now reports worker state, item counts, throughput, ETA, shared cooldown,
  successful API calls, returned token usage/cost when supplied, and recent
  failures. Closing or switching away from the feature stops only polling.
- Increased the explicit plan ceiling in the UI to 10,000 files while preserving
  the required plan step.
- Added thread-local non-content LLM telemetry capture; prompts and response text
  are not persisted in telemetry.
- Updated `README.md`, `tools/README.md`, translation architecture, and dev-console
  architecture. The legacy single-item batch endpoint remains for compatibility,
  but the frontend no longer uses it.
- Verification passed: 21 focused backend tests and the frontend static check.
- Next action: run M7 repository-level checks, then browser verification.

### 2026-10-11 — M7 and M9 complete; M8 environment-blocked

- Full unit discovery passed: 156 tests.
- `tools/check.ps1` passed, including Python compilation, language-registry
  validation, the full test suite, and multilingual staging of 1,423 Markdown
  files in each of 12 languages.
- `tools/dev_console_static_check.py` passed.
- Updated the smoke test's request timeout for the enlarged vault; every smoke
  endpoint passed, including `/api/vault-health` and
  `/api/translation-jobs/current`.
- Live API verification with an isolated database returned no current job and a
  correct `400` response for an invalid/empty plan. No model call was possible.
- The required browser skill was initialized, but browser discovery returned an
  empty list. Interactive Playwright verification therefore remains explicitly
  blocked rather than being replaced by another browser tool.
- Reviewed the scoped diff and preserved the pre-existing CircusFinder/content
  worktree changes. No generated `.build/`, `site/`, `.cache/`, or job-database
  files are tracked.
- Final focused verification after telemetry and lifecycle refinements passed:
  45 test executions plus the frontend static check.
- Added an end-to-end job telemetry aggregation test after review; the final
  job/core subset passed 19 tests and `git diff --check` remained clean.
- Resume action: when Playwright MCP exposes a browser, start the dev console with
  an isolated `--translation-jobs-db`, seed or mock a no-call job, and complete M8.
