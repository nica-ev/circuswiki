---
lang: nl
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interactieve prototype om circuslocaties en -netwerken uit CircusWiki-gegevens te zoeken en te verkennen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:06:33+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:06:33+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>CircusFinder wordt geladen …</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Exacte locaties en geschatte netwerkposities
> Blauwe markeringen zijn gebaseerd op gepubliceerde adressen. Oranje markeringen van geïmporteerde netwerkcontacten tonen daarentegen alleen stads- of regio-centra. Controleer tijdsgebonden informatie zoals cursus- en trainingstijden op de gelinkte website voordat je een bezoek brengt.

<noscript>
CircusFinder heeft JavaScript nodig voor de kaart en filters. De individuele vermeldingen blijven toegankelijk als normale wiki-pagina's.
</noscript>

## Wat dit prototype test

De gegevens komen uit Markdown-bestanden met YAML-metadata. Tijdens de Zensical-build worden ze gecontroleerd en als JSON geëxporteerd. Deze pagina laadt uitsluitend deze export en kent de oorspronkelijke Markdown-bestanden niet.

- Zoeken op trefwoorden in namen, beschrijvingen, locaties en aanbod
- Filteren op type vermelding
- Kaartmarkeringen met pop-upinformatie
- blauwe markeringen voor gepubliceerde, exacte adressen
- oranje markeringen voor geschatte stads- of regio-posities
- optionele zoekradius via de geolocatie van de browser
- vermeldingen zonder geografisch punt, zoals internationale netwerken
