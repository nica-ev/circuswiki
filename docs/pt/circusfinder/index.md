---
lang: pt
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Protótipo interativo para pesquisar e explorar locais e redes de circo a partir de dados do CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:12:20+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:12:20+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>A carregar o CircusFinder…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Localizações exatas e posições aproximadas de rede
> Os marcadores azuis baseiam-se em moradas publicadas. Os marcadores laranja de contactos de rede importados indicam apenas centros urbanos ou regionais. Por favor, verifique informações dependentes do tempo, como horários de cursos e treinos, no website associado antes de visitar.

<noscript>
O CircusFinder requer JavaScript para o mapa e os filtros. As entradas individuais permanecem acessíveis como páginas normais do Wiki.
</noscript>

## O que este protótipo testa

Os dados provêm de ficheiros Markdown com metadados YAML. Durante a compilação do Zensical, são verificados e exportados como JSON. Esta página carrega exclusivamente esta exportação e não conhece os ficheiros Markdown originais.

- Pesquisa de texto livre por nome, descrição, local e ofertas
- Filtro por tipo de entrada
- Marcadores de mapa com informações em pop-up
- Marcadores azuis para moradas exatas publicadas
- Marcadores laranja para posições urbanas ou regionais aproximadas
- Pesquisa voluntária por raio através da geolocalização do navegador
- Entradas sem ponto geográfico, como redes internacionais
