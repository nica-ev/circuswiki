---
created: 2026-06-09 00:00:00
update: 2026-06-09 15:45:24
tags:
  - system
  - spiele
---

# Spiele Content Schema

This schema describes the target structure for canonical game notes tagged `#spiele` that are shown through `_bases/Spiele-Base.base`.

It is a review guide, not an automatic migration rule. Existing content should be changed minimally and only when the source note supports the edit.

## Scope

Applies to:

- canonical source game notes under `docs/<lang>/`
- German game notes under `docs/de/`
- notes with `tags` containing `spiele`
- notes queried by `_bases/Spiele-Base.base`
- ordinary game notes, not MOC/index notes

Does not apply to:

- notes tagged `moc`
- generated base/MOC pages
- non-game pedagogy articles unless they are intentionally modeled as games
- translated target files unless a separate translation review is being done

## Base Query Fields

The current German games base displays these fields:

```yaml
group-min:
group-max:
Schwierigkeit:
Material:
Spieldauer:
```

The current base filters use:

```yaml
lang: de
tags:
  - spiele
category:
```

These fields must be present and internally consistent for reviewed game notes whenever the information can be inferred from the note.

## Frontmatter

Target frontmatter shape. The example uses German because most existing game sources are German; for an English canonical source use `lang: en`, `translation_status: original`, and `translation_source_lang: en` while keeping the same metadata keys.

```yaml
---
lang: de
translation_id: stable-slug
publish: true
tags:
  - spiele
created: YYYY-MM-DD HH:mm:ss
update: YYYY-MM-DD HH:mm:ss
title: Human-readable title
description: One short sentence describing the game.
authors:
  - Marc Bielert
category:
  - warm-up
Schwierigkeit: einfach
Material: keines
Spieldauer: 5-10
source: unbekannt
group-min: 5
group-max: 30
translation_status: original
translation_source_lang: de
---
```

### Required Metadata

- `lang`: Language code. For German source notes this is `de`.
- `translation_id`: Stable cross-language identifier. Preserve existing values.
- `publish`: Usually `true` for public game notes. Preserve existing value unless explicitly reviewing publication status.
- `tags`: Must include `spiele`. Do not include `moc` for ordinary game notes.
- `created`: Preserve existing timestamp.
- `update`: Update when the note is materially edited.
- `title`: Human-readable title. Usually matches the page title, but may normalize underscores or filename quirks.
- `description`: Required after review. One concise sentence useful for search, previews, and metadata display.
- `authors`: Preserve existing authors unless the note explicitly says otherwise.
- `category`: Required for Base/MOC placement. Preserve existing controlled values unless a mismatch is clear.
- `Schwierigkeit`: Difficulty shown in the Base table.
- `Material`: Material shown in the Base table.
- `Spieldauer`: Duration shown in the Base table.
- `source`: Source attribution. Use `unbekannt` only when no source is available.
- `group-min`: Minimum useful group size shown in the Base table.
- `group-max`: Maximum useful group size shown in the Base table.
- `translation_status`: For original German source notes, use `original`.
- `translation_source_lang`: For original German source notes, use `de`.

### Category Values

Use the category values currently expected by `_bases/Spiele-Base.base`:

```yaml
warm-up
bewegung
cool-down
fangen
klatschspiel
Kooperation
kreisspiel
call-response
action
sonstiges
kennenlernen
Taktik
beigoma
```

Do not rename or normalize these values during ordinary content cleanup. If category naming is changed later, handle it as a separate metadata migration.

### Metadata Consistency Rules

- Frontmatter values and visible Markdown facts should agree.
- If a note says "ab 8 Personen", set `group-min: 8` if no better information exists.
- If no meaningful upper limit is stated, use the existing project convention if present in similar notes, otherwise flag the value as uncertain instead of inventing precision.
- Prefer plain numeric values for `group-min` and `group-max`.
- Prefer a compact duration format for `Spieldauer`, for example `5`, `5-10`, or `10-15`.
- Preserve unknown frontmatter fields.
- Do not delete `todo` fields unless the review explicitly resolves them.

## Markdown Body

Target body structure:

```markdown
> [!info] Kurzbeschreibung
> Eine kurze, konkrete Zusammenfassung des Spiels.

**Gruppengröße**: 5-30 Personen
**Schwierigkeit**: einfach
**Material**: keines
**Spieldauer**: 5-10 Minuten

## **Spielbeschreibung**:

Beschreibung von Aufbau, Ablauf, Regeln, Ende und Auswertung, soweit relevant.

## **Varianten**:

Optional. Nur verwenden, wenn Varianten vorhanden sind.

## **Hinweise**:

Optional. Für Sicherheit, Inklusion, Moderation, Gruppendynamik oder pädagogische Hinweise.

## **Quelle**:

Unbekannt

## **Querverweise**

Optional. Links zu verwandten Notizen.
```

### Body Section Rules

- Add a `Kurzbeschreibung` callout to reviewed game notes.
- The callout should usually match or closely mirror `description`.
- Keep the short fact block near the top.
- Use `## **Spielbeschreibung**:` as the main rules section.
- Use optional sections only when there is content for them.
- Preserve Obsidian links, callouts, embeds, and existing useful cross-links.
- Do not rewrite non-German source language content into German unless explicitly requested.
- Do not bulk-polish prose beyond what is needed for structure, clarity, and consistency.

## Review Reporting

For each reviewed batch, report:

- changed files
- metadata filled or changed
- structure changes made
- uncertain fields or assumptions
- notes that should be skipped or reviewed by a human before editing

Small batches are preferred until the workflow is stable.

## Base View Review Workflow

This workflow is the current reliable process for manually cleaning game notes that are shown through `_bases/Spiele-Base.base`.

### 1. Select One Base View

Work on one Base view at a time.

Use the view name from `_bases/Spiele-Base.base`, for example:

```yaml
base: _bases/Spiele-Base.base
view: Aufwärmspiele MOC
```

Map the view to its filter in `_bases/Spiele-Base.base`. Current view/category mappings include:

```text
Aufwärmspiele MOC              -> category contains warm-up
Bewegungsspiele                -> category contains bewegung
Cooldown Spiele MOC            -> category contains cool-down
Fangspiele                     -> category contains fangen
Klatschspiele MOC              -> category contains klatschspiel
Kooperationsspiele             -> category contains Kooperation
Kreisspiele MOC                -> category contains kreisspiel
Call and Response              -> category contains call-response
Schnelligkeit+Reaktionsspiele  -> category contains action
Spiele für Zwischendurch       -> category contains sonstiges
Spiele zum Kennenlernen        -> category contains kennenlernen
Taktik und Konzentrationsspiele -> category contains Taktik
Beigoma                       -> category contains beigoma
```

Do not process all game notes at once. The useful review unit is one Base view or one explicitly named file.

### 2. Build the Candidate List

Derive candidates from frontmatter, not filenames.

Selection rules:

- `lang: de`
- `tags` contains `spiele`
- `tags` does not contain `moc`
- `category` contains the category value used by the selected Base view

Use a script like this to list candidates and schema gaps:

```powershell
@'
from pathlib import Path
import yaml

category_name = "warm-up"  # change per Base view
rows = []

for path in sorted(Path("docs/de").glob("*.md")):
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception as exc:
        rows.append((path.name, "YAML_ERROR", str(exc)))
        continue

    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    categories = fm.get("category") or []
    if isinstance(categories, str):
        categories = [categories]

    if (
        fm.get("lang") == "de"
        and "spiele" in tags
        and "moc" not in tags
        and category_name in categories
    ):
        body = parts[2]
        issues = []
        if not fm.get("description"):
            issues.append("NO_DESC")
        if "[!info] Kurzbeschreibung" not in body:
            issues.append("NO_CALLOUT")
        if "## **Spielbeschreibung**:" not in body:
            issues.append("NO_SPIEL_HEADING")
        if not all(
            fm.get(k) not in (None, "")
            for k in ["group-min", "group-max", "Schwierigkeit", "Material", "Spieldauer"]
        ):
            issues.append("MISSING_BASE")
        rows.append((path.name, "OK" if not issues else ",".join(issues)))

for row in rows:
    print("\t".join(row))
print("COUNT", len(rows))
print("ISSUES", sum(1 for _, status in rows if status != "OK"))
'@ | python -
```

### 3. Read Before Editing

Read the unresolved files before changing them.

Prioritize:

- files with explicit fact blocks first
- files where only `description` or heading structure is missing
- sparse or stub notes last

Do not infer gameplay from a title alone. If a note is a stub, keep it as a stub and make that visible in `description` and the body.

### 4. Edit Conservatively

Allowed normal cleanup:

- fill `description`
- add or normalize `> [!info] Kurzbeschreibung`
- add the short visible fact block
- normalize `## **Spielbeschreibung**:`
- move visible source text into `## **Quelle**:`
- move related links into `## **Querverweise**`
- move variants into `## **Varianten**:`
- move facilitation, safety, inclusion, uncertainty, or todo notes into `## **Hinweise**:`
- remove duplicate top-level `# Title` headings when the generated page already uses the frontmatter title

Avoid:

- translating content
- merging duplicate notes unless explicitly requested
- deleting `todo` fields or incomplete content
- changing category values as part of ordinary cleanup
- normalizing all wording just for style
- changing source attribution without evidence

### 5. Metadata Inference Rules

Prefer values that are directly stated in the note.

Examples:

- Body says `Ab 8 Mitspieler` -> `group-min: 8`
- Body says `5 bis 10 Minuten` -> `Spieldauer: 5-10`
- Body says `keins` -> `Material: keines`
- Body says `Tasifan Spielebuch` -> `source: Tasifan Spielebuch`

When a note gives no upper group limit, use a conservative value based on existing project convention and report it:

- `99` for genuinely open-ended games or "jede Gruppengröße"
- `30` for common medium/large active group games
- `40` or `60` only for games that explicitly work better with large groups
- smaller limits when the mechanics require small groups or pairs

When a note is incomplete:

- use a description such as `Ein Spiel-Stub zu ..., dessen Inhalt noch ergänzt oder gelöscht werden muss.`
- keep or add a visible `#todo`
- fill minimal Base fields only so the note renders predictably
- report the note as needing human review

### 6. Validate the View

After editing, rerun the candidate check for the same category. The target result is:

```text
ISSUES 0
```

Also run:

```powershell
git diff --check -- docs/de
```

If this reports only CRLF warnings on MOC/index files, note that in the summary. Fix real whitespace errors in edited files.

For a single explicitly named file, validate only that file:

```powershell
@'
from pathlib import Path
import yaml

path = Path("docs/de/Example.md")
text = path.read_text(encoding="utf-8-sig")
parts = text.split("---", 2)
fm = yaml.safe_load(parts[1]) or {}
body = parts[2]
checks = {
    "description": bool(fm.get("description")),
    "callout": "[!info] Kurzbeschreibung" in body,
    "spielbeschreibung": "## **Spielbeschreibung**:" in body,
    "base_fields": all(
        fm.get(k) not in (None, "")
        for k in ["group-min", "group-max", "Schwierigkeit", "Material", "Spieldauer"]
    ),
}
print(checks)
'@ | python -
```

### 7. Report the Batch

For each completed Base view, report:

- view name
- changed files
- what was changed structurally
- inferred metadata that deserves review
- stub/incomplete notes preserved
- validation result
- any non-actionable CRLF warnings from generated/MOC/index pages

Do not hide uncertain values. The point of the workflow is to make human review fast and targeted.
