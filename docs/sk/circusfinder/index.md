---
lang: sk
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktívny prototyp na vyhľadávanie a objavovanie cirkusových miest a sietí z dát CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:45+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:45+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder sa načíta …</p>
</div>

> [!info] Presné miesta a približné pozície v sieti
> Modré značky vychádzajú z publikovaných adries. Oranžové značky importovaných kontaktov zo siete však ukazujú iba centrá miest alebo regiónov. Časovo závislé informácie, ako sú časy kurzov a tréningov, si pred návštevou overte na prelinkovanej webovej stránke.

<noscript>
CircusFinder vyžaduje JavaScript pre mapu a filtre. Jednotlivé záznamy zostanú prístupné ako bežné wiki stránky.
</noscript>

## Čo tento prototyp testuje

Údaje pochádzajú z Markdown súborov s YAML metadátami. Počas Zensical-buildu sa kontrolujú a exportujú ako JSON. Táto stránka načíta výhradne tento export a nepozná pôvodné Markdown súbory.

- Vyhľadávanie voľného textu podľa názvu, popisu, miesta a ponúk
- Filtrovanie podľa typu záznamu
- Značky na mape s informáciami v kontextovom okne
- modré značky pre publikované, presné adresy
- oranžové značky pre približné pozície miest alebo regiónov
- dobrovoľné vyhľadávanie v okruhu pomocou geolokácie prehliadača
- záznamy bez geografického bodu, napríklad medzinárodné siete
