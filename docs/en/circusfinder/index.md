---
lang: en
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
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
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:00:45+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:00:45+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>CircusFinder is loading…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Precise Locations and Approximate Network Positions
> Blue markers are based on published addresses. Orange markers for imported network contacts, however, only indicate city or regional centers. Please check time-dependent information such as course and training times on the linked website before visiting.

<noscript>
CircusFinder requires JavaScript for the map and filters. Individual entries remain accessible as regular wiki pages.
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
