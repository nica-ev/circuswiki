---
lang: pt
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
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
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:41+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:41+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">A carregar o CircusFinder…</p>
</div>

> [!info] Localizações exatas e posições aproximadas de rede
> Marcadores azuis baseiam-se em moradas publicadas. Marcadores laranja de contactos de rede importados indicam apenas centros urbanos ou regionais. Por favor, verifique informações dependentes do tempo, como horários de cursos e treinos, no website associado antes de visitar.

<noscript>
O CircusFinder requer JavaScript para o mapa e os filtros. As entradas individuais permanecem acessíveis como páginas Wiki normais.
</noscript>

## O que este protótipo testa

Os dados provêm de ficheiros Markdown com metadados YAML. Durante o processo de compilação do Zensical, são verificados e exportados como JSON. Esta página carrega exclusivamente esta exportação e não tem conhecimento dos ficheiros Markdown originais.

- Pesquisa de texto livre por nomes, descrições, locais e ofertas
- Filtro por tipo de entrada
- Marcadores de mapa com informações em pop-up
- Marcadores azuis para moradas exatas publicadas
- Marcadores laranja para posições aproximadas de cidades ou regiões
- Pesquisa voluntária por raio através da geolocalização do navegador
- Entradas sem ponto geográfico, como redes internacionais
