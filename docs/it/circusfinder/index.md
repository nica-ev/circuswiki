---
lang: it
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Prototipo interattivo per cercare ed esplorare luoghi e reti di circo dai dati di CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:05:06+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:05:06+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>Caricamento di CircusFinder…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Posizioni precise e posizioni approssimative della rete
> I contrassegni blu si basano su indirizzi pubblicati. I contrassegni arancioni dei contatti di rete importati, invece, indicano solo centri urbani o regionali. Si prega di verificare le informazioni dipendenti dal tempo, come orari di corsi e allenamenti, sul sito web collegato prima della visita.

<noscript>
CircusFinder richiede JavaScript per la mappa e i filtri. Le singole voci rimangono accessibili come normali pagine Wiki.
</noscript>

## Cosa testa questo prototipo

I dati provengono da file Markdown con metadati YAML. Durante la build di Zensical, vengono controllati ed esportati come JSON. Questa pagina carica esclusivamente tale esportazione e non conosce i file Markdown originali.

- Ricerca testuale libera per nome, descrizione, luogo e offerte
- Filtro per tipo di voce
- Marcatori sulla mappa con informazioni popup
- Marcatori blu per indirizzi precisi e pubblicati
- Marcatori arancioni per posizioni urbane o regionali approssimative
- Ricerca opzionale per raggio tramite geolocalizzazione del browser
- Voci senza punto geografico, ad esempio reti internazionali
