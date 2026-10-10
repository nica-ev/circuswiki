---
lang: cs
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktivní prototyp pro vyhledávání a prozkoumávání cirkusových míst a sítí z dat CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:43+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:43+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder se načítá…</p>
</div>

> [!info] Přesná místa a přibližné pozice v síti
> Modré značky vycházejí z publikovaných adres. Oranžové značky importovaných kontaktů ze sítě však ukazují pouze střed města nebo regionu. Časově závislé údaje, jako jsou časy kurzů a tréninků, si prosím před návštěvou ověřte na uvedeném webu.

<noscript>
CircusFinder vyžaduje JavaScript pro mapu a filtry. Jednotlivé záznamy zůstanou přístupné jako běžné wiki stránky.
</noscript>

## Co tento prototyp testuje

Data pocházejí z Markdown souborů s YAML metadaty. Při sestavení Zensical jsou zkontrolována a exportována jako JSON. Tato stránka načítá výhradně tento export a nezná původní Markdown soubory.

- Vyhledávání v celém textu podle názvu, popisu, místa a nabídek
- Filtrování podle typu záznamu
- Značky na mapě s informacemi v bublině
- modré značky pro publikované, přesné adresy
- oranžové značky pro přibližné pozice měst nebo regionů
- dobrovolné vyhledávání v okolí pomocí geolokace prohlížeče
- záznamy bez geografického bodu, například mezinárodní sítě
