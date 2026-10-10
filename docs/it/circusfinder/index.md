---
lang: it
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Prototipo interattivo per la ricerca ed esplorazione di luoghi e reti circensi dai dati di CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:32+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:32+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">Caricamento di CircusFinder in corso…</p>
</div>

> [!info] Posizioni precise e posizioni approssimative della rete
> I contrassegni blu si basano su indirizzi pubblicati. I contrassegni arancioni dei contatti di rete importati, invece, indicano solo centri cittadini o regionali. Si prega di verificare le informazioni dipendenti dal tempo, come orari di corsi e allenamenti, sul sito web collegato prima della visita.

<noscript>
CircusFinder richiede JavaScript per la mappa e i filtri. Le singole voci rimangono accessibili come normali pagine Wiki.
</noscript>

## Cosa testa questo prototipo

I dati provengono da file Markdown con metadati YAML. Durante la build di Zensical, vengono controllati ed esportati come JSON. Questa pagina carica esclusivamente questo export e non conosce i file Markdown originali.

- Ricerca testuale libera per nome, descrizione, luogo e offerte
- Filtro per tipo di voce
- Contrassegni sulla mappa con informazioni popup
- contrassegni blu per indirizzi pubblicati e precisi
- contrassegni arancioni per posizioni cittadine o regionali approssimative
- ricerca volontaria per raggio tramite geolocalizzazione del browser
- voci senza punto geografico, ad esempio reti internazionali
