---
lang: cs
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
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
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:22:44+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:22:44+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>CircusFinder se načítá…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Přesná místa a přibližné pozice v síti
> Modré značky vycházejí z publikovaných adres. Oranžové značky importovaných kontaktů ze sítě však ukazují pouze střed města nebo regionu. Časově závislé údaje, jako jsou časy kurzů a tréninků, si prosím před návštěvou ověřte na uvedených webových stránkách.

<noscript>
CircusFinder vyžaduje JavaScript pro mapu a filtry. Jednotlivé záznamy zůstanou přístupné jako běžné stránky wiki.
</noscript>

## Co tento prototyp testuje

Data pocházejí ze souborů Markdown s metadaty YAML. Během sestavení Zensical jsou kontrolována a exportována jako JSON. Tato stránka načítá výhradně tento export a nezná původní soubory Markdown.

- Vyhledávání v plném textu podle názvu, popisu, místa a nabídek
- Filtrování podle typu záznamu
- Značky na mapě s informacemi v kontextovém okně
- modré značky pro publikované, přesné adresy
- oranžové značky pro přibližné pozice měst nebo regionů
- dobrovolné vyhledávání v okolí pomocí geolokace prohlížeče
- záznamy bez geografického bodu, například mezinárodní sítě
