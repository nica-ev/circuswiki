---
lang: hu
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktív prototípus cirkuszi helyszínek és hálózatok kereséséhez és felfedezéséhez a CircusWiki adataiból.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:30+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:30+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">A CircusFinder betöltése folyamatban…</p>
</div>

> [!info] Pontos helyszínek és hozzávetőleges hálózati pozíciók
> A kék jelölők közzétett címeken alapulnak. Ezzel szemben az importált hálózati kapcsolatok narancssárga jelölői csak városi vagy regionális központokat mutatnak. Kérjük, ellenőrizd az időhöz kötött információkat, mint például a tanfolyamok és edzések időpontjait, a látogatás előtt a hivatkozott weboldalon.

<noscript>
A CircusFinder térképhez és szűrőkhöz JavaScriptet igényel. Az egyes bejegyzések normál Wiki-oldalként továbbra is elérhetők.
</noscript>

## Mit tesztel ez a prototípus

Az adatok YAML metaadatokkal ellátott Markdown fájlokból származnak. A Zensical build során ezeket ellenőrzik és JSON formátumban exportálják. Ez az oldal kizárólag ezt az exportot tölti be, és nem ismeri az eredeti Markdown fájlokat.

- Szabad szöveges keresés név, leírás, helyszín és kínálat alapján
- Szűrés bejegyzés típusa szerint
- Térképi jelölők felugró információkkal
- kék jelölők közzétett, pontos címekhez
- narancssárga jelölők hozzávetőleges városi vagy regionális pozíciókhoz
- önkéntes körsugár keresés a böngésző helymeghatározásán keresztül
- földrajzi pont nélküli bejegyzések, például nemzetközi hálózatok
