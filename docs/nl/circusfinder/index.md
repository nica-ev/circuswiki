---
lang: nl
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interactieve prototype om circuslocaties en netwerken uit CircusWiki-gegevens te zoeken en te verkennen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:34+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:34+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder wordt geladen …</p>
</div>

> [!info] Exacte locaties en globale netwerkposities
> Blauwe markeringen zijn gebaseerd op gepubliceerde adressen. Oranje markeringen van geïmporteerde netwerkcontacten tonen daarentegen alleen stads- of regio-centra. Controleer tijdsgebonden informatie zoals cursus- en trainingsuren op de gelinkte website voordat je een bezoek brengt.

<noscript>
CircusFinder vereist JavaScript voor de kaart en filters. De individuele vermeldingen blijven toegankelijk als normale wiki-pagina's.
</noscript>

## Wat deze prototype test

De gegevens komen uit Markdown-bestanden met YAML-metadata. Tijdens de Zensical-build worden ze gecontroleerd en als JSON geëxporteerd. Deze pagina laadt uitsluitend deze export en kent de oorspronkelijke Markdown-bestanden niet.

- Zoeken op trefwoorden in namen, beschrijvingen, locaties en aanbod
- Filteren op type vermelding
- Kaartmarkeringen met pop-up informatie
- Blauwe markeringen voor gepubliceerde, exacte adressen
- Oranje markeringen voor globale stads- of regio-posities
- Optionele zoekradius via de geolocatie van de browser
- Vermeldingen zonder geografisch punt, zoals internationale netwerken
