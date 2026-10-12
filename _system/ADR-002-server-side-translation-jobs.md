---
created: 2026-10-11 00:00:00
update: 2026-10-11 00:00:00
status: accepted
scope: tools/translation, tools/dev_console
---

# ADR-002: Run batch translations as persistent server-side jobs

**Status:** Accepted

**Date:** 2026-10-11

**Participants:** Marc Bielert, Codex

## Context

The translation console currently executes a batch in the browser by sending one
file request at a time. A batch containing several thousand target files can run
for days, stops being observable when the browser is closed, and cannot coordinate
concurrency or provider-wide backoff.

Every source note, including imported CircusFinder notes, is a first-class
Markdown document. Imported notes must use the same translation lifecycle as all
other notes because they may later be enriched and invalidated through the normal
source-hash mechanism.

The existing translation service is synchronous and network-bound. The local dev
console already runs a threaded HTTP server. Generated translations are durable
Markdown files, while batch execution state is local operational data that must
not be committed.

## Decision

We decided to move batch orchestration into a persistent server-side job manager.

- A SQLite database under the ignored `.cache/` directory stores job and item
  execution state. Markdown remains the content source of truth.
- The job manager uses a bounded Python thread pool because OpenRouter requests
  are network-bound.
- One batch job may be active at a time. Its concurrency is configurable from 1
  to 8 workers and defaults to 4.
- The existing plan-first workflow remains mandatory. Starting a job snapshots
  only the candidates in the reviewed plan.
- Each item records its planned source body and localized-metadata hashes. Workers
  verify the hashes before translation and before writing; changed sources become
  stale rather than publishing an obsolete translation.
- LLM rate-limit cooldown is shared across workers. A `429` pauses new requests
  globally and respects `Retry-After`.
- Target writes are atomic. An active target path cannot be processed twice.
- The frontend starts, observes, pauses, resumes, cancels, and retries jobs. It
  does not execute the translation loop.
- On server restart, interrupted items return to the queue. Before retrying, the
  manager recognizes target files that already contain the planned source hashes.
- All Markdown files use identical rules; there are no importer- or path-specific
  translation exceptions.

## Alternatives considered

### Browser-side bounded concurrency

This required less backend work, but the browser would still own a multi-day job,
global rate-limit coordination would be weak, and progress would disappear on
reload.

### Several independent CLI or browser workers

This reused existing entry points, but provided no shared throttling, made target
collisions possible, and increased operational mistakes.

### External queue infrastructure

Redis, Celery, or another service would provide mature distributed scheduling,
but would add installation and operational complexity that is not justified for a
single-user local tool. SQLite and in-process workers meet the current need.

### Special treatment for imported directory notes

Skipping or reducing translation for CircusFinder notes would lower API work, but
would create a second content lifecycle and obstruct future automated enrichment.
It was explicitly rejected.

## Consequences

- (+) Translation continues when the browser is closed or reloaded.
- (+) Jobs can recover after the dev-console server restarts.
- (+) Concurrency, cooldown, cancellation, and duplicate-target protection have a
  single owner.
- (+) Enriched notes invalidate translations through the existing hashes.
- (+) The design remains local and requires no additional service dependency.
- (-) The dev console gains persistent operational state and lifecycle logic.
- (-) Concurrent execution introduces synchronization and recovery cases that
  require dedicated tests.
- (-) Background work still stops when the dev-console process is not running.
- (neutral) Translation API usage and the number of generated Markdown files do
  not decrease; the decision improves throughput and operability.

## Implementation record

The resumable implementation checklist and progress log live in
`_system/translation-background-jobs-implementation-plan.md`.
