---
lang: es
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
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
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:09:26+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:09:26+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>Cargando CircusFinder…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Ubicaciones exactas y posiciones aproximadas de la red
> Los marcadores azules se basan en direcciones publicadas. Los marcadores naranjas de contactos de red importados, en cambio, solo muestran centros urbanos o regionales. Por favor, comprueba la información temporal, como horarios de cursos y entrenamientos, en el sitio web enlazado antes de tu visita.

<noscript>
CircusFinder necesita JavaScript para el mapa y los filtros. Las entradas individuales seguirán siendo accesibles como páginas normales de Wiki.
</noscript>

## Qué prueba este prototipo

Los datos provienen de archivos Markdown con metadatos YAML. Durante la compilación de Zensical, se comprueban y exportan como JSON. Esta página carga exclusivamente esta exportación y no conoce los archivos Markdown originales.

- Búsqueda de texto libre por nombre, descripción, ubicación y ofertas
- Filtro por tipo de entrada
- Marcadores en el mapa con información emergente
- Marcadores azules para direcciones exactas publicadas
- Marcadores naranjas para posiciones urbanas o regionales aproximadas
- Búsqueda voluntaria por radio a través de la geolocalización del navegador
- Entradas sin punto geográfico, como redes internacionales
