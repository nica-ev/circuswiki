---
lang: en
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interactive prototype for searching and exploring circus locations and networks from CircusWiki data.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:26+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:26+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder is loading…</p>
</div>

> [!info] Precise Locations and Approximate Network Positions
> Blue markers are based on published addresses. Orange markers for imported network contacts, however, only show city or regional centers. Please check time-sensitive information such as course and training times on the linked website before visiting.

<noscript>
CircusFinder requires JavaScript for the map and filters. Individual entries remain accessible as normal wiki pages.
</noscript>

## What This Prototype Tests

The data comes from Markdown files with YAML metadata. During the Zensical build, it is checked and exported as JSON. This page exclusively loads this export and does not know the original Markdown files.

- Free text search across names, descriptions, locations, and offerings
- Filter by entry type
- Map markers with popup information
- Blue markers for published, precise addresses
- Orange markers for approximate city or regional positions
- Optional radius search via browser geolocation
- Entries without a geographical point, such as international networks
