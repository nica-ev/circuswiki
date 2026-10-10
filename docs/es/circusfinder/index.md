---
lang: es
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Prototipo interactivo para buscar y explorar lugares y redes de circo a partir de datos de CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:37+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:37+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">Cargando CircusFinder…</p>
</div>

> [!info] Ubicaciones exactas y posiciones aproximadas de la red
> Los marcadores azules se basan en direcciones publicadas. Los marcadores naranjas de los contactos de red importados, en cambio, solo muestran centros de ciudades o regiones. Por favor, comprueba la información dependiente del tiempo, como horarios de cursos y entrenamientos, en el sitio web enlazado antes de tu visita.

<noscript>
CircusFinder necesita JavaScript para el mapa y los filtros. Las entradas individuales seguirán siendo accesibles como páginas normales de Wiki.
</noscript>

## Qué prueba este prototipo

Los datos provienen de archivos Markdown con metadatos YAML. Durante la compilación de Zensical, se comprueban y exportan como JSON. Esta página carga exclusivamente esta exportación y no conoce los archivos Markdown originales.

- Búsqueda de texto libre por nombre, descripción, ubicación y ofertas
- Filtro por tipo de entrada
- Marcadores en el mapa con información emergente
- Marcadores azules para direcciones exactas publicadas
- Marcadores naranjas para posiciones aproximadas de ciudades o regiones
- Búsqueda voluntaria por radio a través de la geolocalización del navegador
- Entradas sin punto geográfico, como redes internacionales
