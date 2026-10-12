---
created: 2026-10-10
update: 2026-10-11
---

# CircusFinder source imports

## Purpose

CircusFinder should present the best available snapshot of currently usable circus and aerial training places. It is not intended to become a historical directory of closed venues. Imported records remain ordinary Markdown/YAML entries so they can be reviewed, corrected, translated, and used independently of the original presentation system.

Every imported record must retain machine-readable provenance. A source-specific folder, source URL, stable source record ID where available, retrieval date, original record name, batch ID, and reuse basis make a batch identifiable and removable if the upstream source or its reuse conditions change. The source registry is `tools/config/circusfinder_sources.json`.

Direct permission from the people or organization responsible for a community resource is a valid reuse basis even when that community has not published a formal data license. Record that permission as provenance; do not invent a license identifier.

## Shared importer behavior

The JugglingMap and Circuscentrum adapters use `tools/circusfinder/importing.py`. The shared layer:

- validates a source-specific minimum record count to catch truncated responses;
- treats upstream IDs as the primary identity on later scans;
- checks existing originals across languages before creating a record;
- matches conservatively by exact normalized name plus nearby coordinates, unique non-social website domain, or a very similar name within one kilometre;
- reports ambiguous matches and blocks the entire apply operation until they receive an explicit adapter-level decision;
- updates source-owned files in place and only adds or refreshes provenance on matched non-source records;
- is dry-run by default; and
- only removes stale source-owned files when `--apply --prune` is explicitly used.

Always review `ambiguous_matches`, `skipped_source_records`, source duplicate candidates, `records_created`, `records_updated`, provenance updates, and `stale_owned_records` before applying a rescan. Never prune from a partial or unexpectedly small source response.

## JugglingMap

JugglingMap exposes a public list endpoint at `https://jugglingmap.org/api/v1/pins` and a detail endpoint for each stable pin ID. The importer retrieves all details and maps open training, circus school, and shop categories into CircusFinder metadata.

```powershell
python tools/circusfinder/import_jugglingmap.py
python tools/circusfinder/import_jugglingmap.py --apply
python tools/circusfinder/import_jugglingmap.py --apply --prune
```

Source-owned files live below `docs/en/circusfinder/places/jugglingmap/`. The generated framing text is English, while source-provided descriptions and contact details are preserved verbatim and marked with `source_content_language: und` because individual records use many languages. Community map positions are stored as `location_precision: approximate`.

Categories at one pin are merged only when their normalized names agree. Reviewed duplicate-pin omissions and reviewed distinct multi-venue pairs are explicit constants in the adapter. New suspicious same-name/domain or nearby pairs remain visible in the dry-run report.

## Circuscentrum Landschap

Circuscentrum publishes a server-rendered, paginated directory at `https://circuscentrum.be/nl/landschap`. Its Drupal settings embed source-provided map coordinates. The importer scans every result page, keys records by stable Drupal node ID, and cross-checks details against the embedded coordinate collection.

```powershell
python tools/circusfinder/import_circuscentrum.py
python tools/circusfinder/import_circuscentrum.py --apply
python tools/circusfinder/import_circuscentrum.py --apply --prune
```

Source-owned files live below `docs/nl/circusfinder/places/circuscentrum/` because the source content is Dutch. Atelier, festival, workspace, and distribution-office records are imported. Circuscentrum also mixes persistent organizations and dated event announcements in uncategorized records; only the explicitly reviewed organization IDs in the adapter are eligible. New uncategorized records are reported and skipped pending review. Records without a source coordinate remain searchable with `location_precision: none`.

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

Run a reviewed refresh every three months, or sooner after a known upstream update. JugglingMap and Circuscentrum can be fetched directly by their importers, but their dry-run reports still require review. The aerial map remains manual because its export requires an authenticated Looker Studio session.

A scheduled GitHub workflow must not contain a personal Google login, browser cookies, or another private credential. Before direct scheduled ingestion is enabled, the source needs one of the following:

- a stable public CSV, Google Sheet, API, or other documented data endpoint; or
- explicit cooperation from the map maintainer on a machine-readable export.

Until then, automation can safely provide a recurring reminder or open a maintenance issue, but the CSV export and dry-run review remain manual. Once a stable endpoint exists, the importer can run on a schedule and open a pull request containing its audit summary and Markdown changes. Automatic merging or automatic pruning is not a goal.

## Future improvements

- Add country/city enrichment without treating inferred geography as source-provided data.
- Surface verification date and source status more clearly in the CircusFinder interface.
- Produce a compact machine-readable import report suitable for pull-request summaries.
- Track records that change from `Open` to another status and require review before removal.
- Replace the aerial map's authenticated CSV export with a stable feed if its maintainers provide one.
