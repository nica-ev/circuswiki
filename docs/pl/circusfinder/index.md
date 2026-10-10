---
lang: pl
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktywny prototyp do wyszukiwania i eksploracji miejsc i sieci cyrkowych z danych CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:28+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:28+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder się ładuje…</p>
</div>

> [!info] Dokładne lokalizacje i przybliżone pozycje sieciowe
> Niebieskie znaczniki opierają się na opublikowanych adresach. Pomarańczowe znaczniki importowanych kontaktów sieciowych wskazują jedynie centra miast lub regionów. Prosimy o sprawdzenie aktualnych informacji, takich jak godziny kursów i treningów, na powiązanej stronie internetowej przed wizytą.

<noscript>
CircusFinder wymaga JavaScript do działania mapy i filtrów. Poszczególne wpisy pozostają dostępne jako zwykłe strony Wiki.
</noscript>

## Co testuje ten prototyp

Dane pochodzą z plików Markdown z metadanymi YAML. Podczas budowania Zensical są one sprawdzane i eksportowane jako JSON. Ta strona ładuje wyłącznie ten eksport i nie zna oryginalnych plików Markdown.

- Wyszukiwanie pełnotekstowe według nazw, opisów, lokalizacji i ofert
- Filtrowanie według typu wpisu
- Znaczniki na mapie z informacjami w wyskakujących okienkach
- Niebieskie znaczniki dla opublikowanych, dokładnych adresów
- Pomarańczowe znaczniki dla przybliżonych pozycji w miastach lub regionach
- Opcjonalne wyszukiwanie w promieniu za pomocą geolokalizacji przeglądarki
- Wpisy bez punktu geograficznego, np. sieci międzynarodowe
