---
lang: en
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Release Notes
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:13:38+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:16:59+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
[!info]
These release notes provide only a general overview; minor changes (such as individual new pages or modifications to existing content) are not all listed. However, these can be precisely tracked in the repository's history.

[!info]- **Version:** v0.04 - **Release Date**: June 9, 2026
>**Content**
- Multilingual content significantly expanded: Content is now structured under `docs/<language>`.
- New and updated translations added for many game descriptions and project pages.
- Polish workshop materials imported and integrated into the multilingual content structure.
- Content and metadata structure for games further unified.

>**Technical**
- Website generator switched from MkDocs/MkDocs Material to Zensical.
- New multilingual build and staging structure introduced.
- German remains the default language without a language prefix; other languages will be published under language codes, e.g., `/en/`, `/pl/`, `/es/`.
- Central language configuration introduced via `tools/config/languages.json`.
- GitHub Pages deployment updated for the new Zensical structure.
- Local translation tools and Dev Console significantly expanded: health checks, batch scheduling, translation status, graph views, navigation tools, link repair, and cleanup workflows.
- Language switcher, translation status indicators, and fallback pages for missing translations added.
- Tables in the final site output improved: sortable tables, better display of dense tables, and optionally collapsible page sections.

>**Fixed**
- Internal links and Markdown links on translated pages are more reliably preserved and repaired.
- Multilingual navigation and URL structure have been stabilized.
- Responsive behavior of the navigation has been improved, especially in conjunction with Zensical's mobile hamburger menu.

[!info]- **Version:** v0.03 - **Release Date**: March 11, 2025
>**Content**
- Missing game descriptions added.

>**Technical**
- Favicon + logo added.
- UI Redesign.
- Top-level navigation is now in the page header, while the right-hand navigation bar is adjusted contextually.
- Tables can be sorted by clicking on the headers.

>**Fixed**
- Tags are working again.

[!info]- **Version:** v0.02 - **Release Date**: February 26, 2025
>**Technical**
- Blog feature.
- Analytics (Google).
- Cookie banner.
- Feedback widget (bottom of each page).

[!info]- **Version:** v0.01 - **Release Date**: January 15, 2025
>**Content**
- 150 game descriptions added.
- Basic documentation description.

>**Technical**
- Base setup for MkDocs and MkDocs Materials.
- Obsidian support with MkDocs publisher (allows the use of Obsidian Markdown such as Markdown links, Callout Boxes).
