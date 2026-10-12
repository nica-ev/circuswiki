---
lang: sk
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktívny prototyp na vyhľadávanie a prehliadanie cirkusových miest a sietí z dát CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:24:11+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:24:11+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>CircusFinder sa načíta …</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Presné miesta a približné sieťové pozície
> Modré značky vychádzajú z publikovaných adries. Oranžové značky importovaných sieťových kontaktov však ukazujú iba mestá alebo centrá regiónov. Časovo závislé informácie, ako sú časy kurzov a tréningov, si pred návštevou overte na prepojenej webovej stránke.

<noscript>
CircusFinder vyžaduje JavaScript pre mapu a filtre. Jednotlivé záznamy zostanú prístupné ako bežné wiki stránky.
</noscript>

## Čo tento prototyp testuje

Údaje pochádzajú z Markdown súborov s YAML metadátami. Pri zostavovaní pomocou Zensical sa kontrolujú a exportujú ako JSON. Táto stránka načíta výhradne tento export a nepozná pôvodné Markdown súbory.

- Vyhľadávanie voľného textu podľa názvu, popisu, miesta a ponúk
- Filtrovanie podľa typu záznamu
- Značky na mape s informáciami v kontextovom okne
- Modré značky pre publikované, presné adresy
- Oranžové značky pre približné pozície miest alebo regiónov
- Dobrovoľné vyhľadávanie v okruhu pomocou geolokácie prehliadača
- Záznamy bez geografického bodu, napríklad medzinárodné siete
