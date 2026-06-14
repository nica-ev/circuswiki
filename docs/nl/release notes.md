---
lang: nl
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
translation_updated: 2026-06-10T20:13:57+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:02+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Deze release notes geven slechts een globaal overzicht; kleine wijzigingen (zoals individuele nieuwe pagina's of aanpassingen aan bestaande content) worden niet allemaal vermeld. Deze kunnen echter nauwkeurig worden gevolgd in de geschiedenis van de repository.

>[!info]- **Versie:** v0.04 - **Releasedatum**: 9 juni 2026
>**Content**
>- Meertalige content sterk uitgebreid: content is nu gestructureerd onder `docs/<taal>`.
>- Nieuwe en bijgewerkte vertalingen toegevoegd voor veel spelbeschrijvingen en projectpagina's.
>- Poolse workshopmaterialen geïmporteerd en geïntegreerd in de meertalige contentstructuur.
>- Content- en metadata-structuur voor spellen verder geüniformeerd.
>
>**Technisch**
>- Websitegenerator omgeschakeld van MkDocs/MkDocs Material naar Zensical.
>- Nieuwe meertalige build- en stagingstructuur geïntroduceerd.
>- Duits blijft de standaardtáál zonder taalprefix; andere talen worden gepubliceerd onder taalcodes, bijv. `/en/`, `/pl/`, `/es/`.
>- Centrale taalconfiguratie geïntroduceerd via `tools/config/languages.json`.
>- GitHub Pages-deployment bijgewerkt voor de nieuwe Zensical-structuur.
>- Lokale vertaaltools en dev console sterk uitgebreid: health checks, batchplanning, vertaalstatus, graafweergaven, navigatietools, linkreparatie en cleanup-workflows.
>- Taalschakelaar, indicatoren voor vertaalstatus en fallback-pagina's voor ontbrekende vertalingen toegevoegd.
>- Tabellen in de uiteindelijke site-output verbeterd: sorteerbare tabellen, betere weergave van dichte tabellen en optioneel inklapbare paginagebieden.
>
>**Opgelost**
>- Interne links en Markdown-links op vertaalde pagina's worden betrouwbaarder behouden en gerepareerd.
>- Meertalige navigatie en URL-structuur zijn gestabiliseerd.
>- Responsief gedrag van de navigatie is verbeterd, met name in combinatie met het mobiele hamburger-menu van Zensical.

>[!info]- **Versie:** v0.03 - **Releasedatum**: 11 maart 2025
>**Content**
>- Ontbrekende spelbeschrijvingen toegevoegd.
>
>**Technisch**
>- Favicon + logo toegevoegd.
>- UI-redesign.
>- Navigatie van de eerste graad bevindt zich nu in de paginakop, terwijl de rechter navigatiebalk contextafhankelijk wordt aangepast.
>- Tabellen kunnen worden gesorteerd door op de headers te klikken.
>
>**Opgelost**
>- Tags werken weer.

>[!info]- **Versie:** v0.02 - **Releasedatum**: 26 februari 2025
>**Technisch**
>- Blogfunctie.
>- Analytics (Google).
>- Cookiebanner.
>- Feedbackwidget (onderaan elke pagina).

>[!info]- **Versie:** v0.01 - **Releasedatum**: 15 januari 2025
>**Content**
>- 150 spelbeschrijvingen toegevoegd.
>- Basale beschrijving van de documentatie.
>
>**Technisch**
>- Basisopzet voor Mkdocs en Mkdocs-materials.
>- Obsidian-ondersteuning met Mkdocs-publisher (maakt gebruik van Obsidian Markdown zoals Markdown-links, callout boxes mogelijk).
