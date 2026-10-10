---
created: 2026-10-10
update: 2026-10-10
---

# CircusFinder source imports

## Purpose

CircusFinder should present the best available snapshot of currently usable circus and aerial training places. It is not intended to become a historical directory of closed venues. Imported records remain ordinary Markdown/YAML entries so they can be reviewed, corrected, translated, and used independently of the original presentation system.

Every imported record must retain machine-readable provenance. A source-specific folder, source URL, retrieval date, original record name, and batch ID make a batch identifiable and removable if the upstream source or its reuse conditions change.

## Circus Gyms / Schools Around the World

The public report is a crowdsourced aerial and circus training map maintained in Google Looker Studio:

<https://datastudio.google.com/reporting/2ff68cae-8df4-46f2-b2e6-8ef6d0e328c1/page/Gj9BE>

Looker Studio currently offers a manual chart-data export. It does not provide this report through a documented, stable public dataset API. The supported workflow is therefore:

1. Open the public report while signed in.
2. Export the full map data as CSV with **Keep value formatting** disabled.
3. Run a dry import and review its JSON report.
4. Resolve new invalid coordinates and ambiguous duplicate matches explicitly.
5. Apply the import only after the report looks plausible.
6. Validate CircusFinder and review the generated diff before committing.

Dry run:

```powershell
python tools/circusfinder/import_aerial_map.py "path/to/export.csv"
```

Apply reviewed additions and updates:

```powershell
python tools/circusfinder/import_aerial_map.py "path/to/export.csv" --apply
```

Removing source-owned entries that are no longer present in the current open snapshot is intentionally separate:

```powershell
python tools/circusfinder/import_aerial_map.py "path/to/export.csv" --apply --prune
```

Never use `--prune` without reviewing `stale_owned_records` from a dry run. A missing row could reflect a partial export or upstream editing mistake rather than a confirmed closure.

## Current import policy

- Only rows whose source status is exactly `Open` are eligible for publication.
- A record must have a usable name.
- `Unknown` and `Shut Down` rows are reported but not imported.
- Named open records without coordinates remain searchable directory entries with `location_precision: none`.
- Crowdsourced coordinates use `location_precision: approximate`, even when the source pin looks building-level.
- Invalid coordinates are rejected unless the importer contains an explicit, reviewed correction for that named record.
- Source duplicates are collapsed only when their names or non-generic website domains agree and their coordinates are very close.
- Existing CircusFinder records are preferred over creating duplicate records. A matched existing record receives this report as an additional source, while its stronger metadata and coordinates remain unchanged.
- Imported entries use `verification_status: imported_public_map`. “Open” means the upstream community map considers the place open; it is not an independent CircusWiki verification.

## Repeatability and update detection

The importer is dry-run by default and emits an audit report containing:

- source status counts;
- skipped open rows and reasons;
- explicit coordinate corrections;
- source duplicate groups;
- matches against existing CircusFinder entries;
- planned source-provenance updates;
- created and updated source-owned files; and
- stale files eligible for a reviewed prune.

Source-owned entries live under `docs/en/circusfinder/places/aerial-training-map/`. Their IDs and filenames are derived from normalized names, with a coordinate/domain fingerprint only when names collide. Repeated imports update those files instead of creating a new dated copy. Existing non-source records are not overwritten; only their matching provenance item is added or refreshed.

The CSV does not expose a durable upstream record ID. Name, website domain, and geographic proximity are therefore matching evidence rather than guaranteed identity. Ambiguous cases must remain visible in the audit output and be decided by a person.

## Recurring imports and scheduling

Initially, run a manual refresh every three months, or sooner after a known upstream update. The manual step is appropriate while export requires an authenticated Looker Studio session and while the matching rules are still being exercised against real changes.

A scheduled GitHub workflow must not contain a personal Google login, browser cookies, or another private credential. Before direct scheduled ingestion is enabled, the source needs one of the following:

- a stable public CSV, Google Sheet, API, or other documented data endpoint; or
- explicit cooperation from the map maintainer on a machine-readable export.

Until then, automation can safely provide a recurring reminder or open a maintenance issue, but the CSV export and dry-run review remain manual. Once a stable endpoint exists, the importer can run on a schedule and open a pull request containing its audit summary and Markdown changes. Automatic merging or automatic pruning is not a goal.

## Future improvements

- Keep a small reviewed registry of source-specific coordinate corrections and duplicate decisions.
- Add country/city enrichment without treating inferred geography as source-provided data.
- Surface verification date and source status more clearly in the CircusFinder interface.
- Produce a compact machine-readable import report suitable for pull-request summaries.
- Detect large source regressions, such as a partial export or an unexpected drop in open records, and refuse to apply them.
- Track records that change from `Open` to another status and require review before removal.
- Contact the map maintainer about reciprocal links, attribution preferences, and a stable open-data feed.
