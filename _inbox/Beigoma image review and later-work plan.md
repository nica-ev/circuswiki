---
created: 2026-06-12 18:00:50
update: 2026-06-12 18:00:50
status: waiting-for-permission
project: beigoma-images
publish: false
---

# Beigoma image review and later-work plan

This note documents the June 2026 review of the English Beigoma source notes and where images would be useful. It is intentionally kept outside `docs/` because this is planning material, not public content.

## Current state

The English Beigoma notes are in good textual shape, but most of the cluster is visually under-supported. The strongest need is not decorative illustration, but practical images that reduce ambiguity:

- what a Beigoma top looks like
- how the string is prepared and wound
- what the playing floor / `yuka` looks like
- how a portable floor is built
- what decorated or modified tops look like
- what score cards, league tables, and tournament sheets look like

Only one existing image was found in the English source cluster:

- `docs/en/Wie spielt man Beigoma.md` currently embeds `../img/4691855_1005.jpg`

## Permission status

Marc has contacted Tokyo Beigoma by email to ask for permission to reuse images with credit.

Until permission is granted, Tokyo Beigoma images should be treated as `permission required`. Credit alone is not enough unless the source explicitly allows reuse.

No explicit open license was found during the review on the checked Tokyo Beigoma pages. Galiton also appears useful as a visual reference source, but no explicit open image license was identified there either.

## Recommended later image folder

The repository convention is shared public media under `docs/img/`. For the later download/compression step, use a dedicated subfolder so these images can be handled separately:

```text
docs/img/beigoma-source/
docs/img/beigoma-source/tokyo-beigoma/
docs/img/beigoma-source/galiton/
```

If these are only temporary raw downloads before compression, consider a non-public working folder first, then move compressed/approved images into `docs/img/beigoma-source/`.

## Source pages checked

Tokyo Beigoma:

- https://tokyo-beigoma.com/
- https://tokyo-beigoma.com/playground/
- https://tokyo-beigoma.com/category/game/
- https://tokyo-beigoma.com/category/goods/
- https://tokyo-beigoma.com/category/processing/
- https://tokyo-beigoma.com/category/decoration/
- https://tokyo-beigoma.com/score_sheet/
- https://tokyo-beigoma.com/minitoko/
- https://tokyo-beigoma.com/2min-processing/
- https://tokyo-beigoma.com/%E3%83%99%E3%83%BC%E3%82%B4%E3%83%9E%E5%B0%82%E9%96%80%E7%94%A8%E8%AA%9E%E3%81%AE%E3%81%94%E7%B4%B9%E4%BB%8B/
- https://tokyo-beigoma.com/%E3%83%99%E3%83%BC%E3%82%B4%E3%83%9E%E3%83%87%E3%82%B3%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E6%96%B9%E6%B3%95%E3%81%AE%E3%81%94%E7%B4%B9%E4%BB%8B/
- https://tokyo-beigoma.com/%E3%83%88%E3%83%BC%E3%83%8A%E3%83%A1%E3%83%B3%E3%83%88%E6%88%A6/
- https://tokyo-beigoma.com/%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E5%AF%BE%E6%88%A6/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c%e3%82%b9%e3%83%94%e3%83%bc%e3%83%89%e3%80%8d/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c%e3%83%96%e3%83%ad%e3%83%83%e3%82%af%e3%82%b2%e3%83%bc%e3%83%a0%e3%80%8d/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c%e3%83%aa%e3%83%bc%e3%82%b0%e6%88%a6%e3%80%8d/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c%e5%90%8d%e4%ba%ba%e3%81%ab%e6%8c%91%e6%88%A6%e3%80%8d/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c%e3%82%bf%e3%83%83%e3%82%b0%e3%83%9e%e3%83%83%e3%83%81%e3%83%88%e3%83%BC%e3%83%8A%e3%83%A1%e3%83%B3%e3%83%88%e3%80%8d/
- https://tokyo-beigoma.com/%e3%82%b2%e3%83%bc%e3%83%a0%e3%81%ae%e7%b4%b9%e4%bb%8b%e3%80%8c10%e5%88%86%e5%8a%A0%e5%B7%A5%e3%80%8d/

Galiton:

- https://www.galiton.co.jp/special/progress/beigoma.html

## Priority recommendations

### 1. `docs/en/Wie spielt man Beigoma.md`

Highest priority. This is the beginner tutorial and should become visually instructional.

Recommended images:

- prepared Beigoma string with knots
- placing the top between knots
- winding sequence
- compact finished wrap
- hand position before release
- throw/release close to the floor

Best candidate source:

- Galiton beginner guide, because it has a clear step-by-step sequence

Fallback if permission is unclear:

- take our own staged photos with neutral background and a local Beigoma set

### 2. `docs/en/Making a Beigoma Floor.md`

High priority. The shallow cloth depression and floor construction are hard to understand text-only.

Recommended images:

- materials laid out
- cloth over bucket/frame
- fastening method
- finished floor from side angle showing depression
- top spinning on the floor

Best candidate sources:

- Tokyo Beigoma mini-floor article: `https://tokyo-beigoma.com/minitoko/`
- Galiton beginner guide floor images

Fallback if permission is unclear:

- produce our own build sequence when making/compressing images later

### 3. `docs/en/Beigoma Equipment and Setup.md`

High priority. This note should orient readers before they enter the detailed tutorial pages.

Recommended images:

- Beigoma tops
- strings
- playing floor / `yuka`
- workshop setup with multiple stations, if available

Best candidate sources:

- Galiton for basic objects and floor styles
- Tokyo Beigoma homepage/playground for event setup

Caution:

- avoid photos with identifiable children or public participants unless permission is very clear

### 4. `docs/en/Beigoma.md`

Medium-high priority. Needs one strong overview image near the top.

Recommended image:

- an attractive overview photo showing Beigoma tops, string, and playing floor

Best candidate source:

- Tokyo Beigoma homepage/topic images

Purpose:

- immediately answer “what is this?” for readers arriving from the index or search

### 5. `docs/en/Beigoma Terminologie.md`

Medium priority, but useful. Terminology benefits from comparison visuals.

Recommended images:

- normal vs modified/decorated top
- playing floor / `yuka`
- winding styles, if a clear image exists

Best candidate sources:

- Tokyo Beigoma terminology article
- Galiton top overview

Separate issue noticed:

- The Japanese terms in this file currently appear mojibaked, for example `å¥³å·»ã` instead of Japanese text. This should be fixed separately from the image pass.

### 6. `docs/en/Beigoma Modification Basics.md`

Medium-high priority. Modification is material/tactile and needs visual examples.

Recommended images:

- unmodified top
- filing/processing setup
- contact point or body being shaped
- polished/mirror-finished top
- before/after comparison

Best candidate sources:

- Tokyo Beigoma processing category
- `https://tokyo-beigoma.com/2min-processing/`
- mirror-polish article

Caution:

- if using tool-use photos, make safety context explicit in caption/nearby text

### 7. `docs/en/Beigoma Decoration and Personalization.md`

Medium-high priority. This note needs visual examples more than explanation.

Recommended images:

- decorated tops
- decoration method sheet
- plate-style top decoration
- colored/patterned Beigoma examples

Best candidate source:

- Tokyo Beigoma decoration method page

### 8. `docs/en/Beigoma 10-Minute Modification Game.md`

Medium priority. One or two images are enough.

Recommended images:

- timed modification setup
- tool/material table
- example modified result

Best candidate source:

- Tokyo Beigoma 10-minute modification article

### 9. `docs/en/Beigoma Point Match.md`

Medium priority. This needs a score/table visual more than general Beigoma photography.

Recommended images:

- point-match score sheet
- example team scoring card
- four-player/team setup if available

Best candidate sources:

- Tokyo Beigoma point-match article
- Tokyo Beigoma score-sheet page

### 10. `docs/en/Beigoma Tournament Match.md`

Medium priority. A bracket image or score sheet would be useful.

Recommended images:

- tournament bracket
- tournament score sheet
- one-on-one match setup if clear

Best candidate sources:

- Tokyo Beigoma tournament article
- Tokyo Beigoma score-sheet page

### 11. `docs/en/Basic Beigoma Rules and Refereeing.md`

Medium-low priority for photos, higher priority for diagrams.

Recommended visuals:

- simple diagram of Riki win, Hajiki win, floor miss, Pakkan
- optional photo of tops on/outside the floor

Best approach:

- make our own simple diagrams later instead of relying on source-site photos

Reason:

- referee decisions need clarity, not atmosphere

### 12. Game-format notes translated from older German sources

Affected notes:

- `docs/en/Beigoma-Spiel-Speed.md`
- `docs/en/Blockspiel.md`
- `docs/en/Ligaspiel.md`
- `docs/en/Fordere den Meister heraus.md`
- `docs/en/Tag Match Tournament.md`

Recommended visuals:

- score cards
- block cards
- league tables
- challenge-master card
- team/tournament bracket sheets

Best candidate sources:

- Tokyo Beigoma game-format pages
- Tokyo Beigoma score-sheet page

Best long-term approach:

- use Tokyo Beigoma images as visual reference if permission allows
- consider making our own simplified English score-sheet diagrams/templates for consistency and translation-friendliness

### 13. `docs/en/Facilitating Beigoma for Mixed Groups.md`

Medium-low priority. One contextual photo could help, but privacy risk is higher.

Recommended image:

- non-identifying workshop setup photo
- group/floor arrangement without clearly identifiable faces

Best candidate source:

- Tokyo Beigoma playground page

Caution:

- avoid identifiable children or public participants unless permission is explicit and covers people shown in the photos

## Candidate image types found

Tokyo Beigoma candidates:

- homepage/category images for decoration, processing, rules
- terminology page image
- decoration method images, including a decoration handout/image
- processing images for Riki-goma and polishing
- point-match photos and score examples
- tournament image and bracket-related visual
- game-format screenshots for Speed, Block Game, League Game, Challenge the Master, Tag Match Tournament, and 10-minute modification
- mini-floor construction sequence
- score-sheet images for tournament/league/random/table formats
- playground/event photos

Galiton candidates:

- Beigoma top overview
- string/preparation sequence
- winding sequence
- floor setup sequence
- Kanto/Kansai floor examples
- Beigoma list/table image

## Later implementation workflow

When permission status is clear:

1. Create an image manifest before downloading anything.
2. Include target note, target section, source page, direct image URL, proposed filename, credit line, and permission status.
3. Download only approved or otherwise legally usable images.
4. Put raw source images into a dedicated subfolder for separate compression work.
5. Compress/resize consistently before embedding in notes.
6. Add captions/alt text that explain the pedagogical purpose, not only the object shown.
7. Add or update source/credit text near the image or in a page-level source section.
8. Verify site build and image paths after insertion.

Suggested manifest fields:

```text
target_note,target_section,image_purpose,source_page,image_url,filename,credit,permission_status,notes
```

Permission status values:

```text
needs-permission
approved
own-photo
own-diagram
not-used
```

## Recommended credit style

If Tokyo Beigoma grants permission, use consistent credit text, for example:

```text
Image: Tokyo Beigoma, used with permission. Source: <source page URL>
```

If Galiton grants permission, use:

```text
Image: Galiton, used with permission. Source: <source page URL>
```

For our own images:

```text
Image: CircusWiki / Nica e.V.
```

## Open decisions

- Wait for Tokyo Beigoma permission response before downloading their images.
- Decide whether to contact Galiton separately or use Galiton only as visual reference for our own photos.
- Decide whether game-format visuals should be source screenshots or newly made English templates/diagrams.
- Decide whether event photos with people are acceptable at all; safest option is to avoid identifiable people.
- Fix mojibake in `docs/en/Beigoma Terminologie.md` separately.
