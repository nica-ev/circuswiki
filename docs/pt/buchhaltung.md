---
lang: pt
translation_id: buchhaltung
publish: true
tags:
  - moc
created: 2025-01-19 16:47:55
update: 2026-06-07 00:06:48
title: Visão Geral da Contabilidade
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/buchhaltung.md
translation_source_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:31:00+00:00
translation_source_body_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_source_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:45+00:00
translation_source_localized_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_source_structural_metadata_hash: 50f1f18cad2c4ebdd8284c2c85de7dd1c5fa87e6d1a499f8cdd300ec1a798d96
---
# Visão Geral da Contabilidade

A nossa contabilidade baseia-se na chamada "contabilidade em texto simples" (Plaintext Accounting).
Todos os dados / transações são escritos num ficheiro de texto num formato facilmente legível por humanos.

Uma transação neste formato tem o seguinte aspeto:
```
2023-01-09 document Despesas:Escritório:Outros "Recibos Despesas/Registados/2023_004.jpg" ^2023_004

2023-01-09 ! "Hornbach" "Lâmpada de escritório" #aberto #digitalizado ^2023_004

    Despesas:Escritório:Outros              64.95 EUR

    Passivos:Pessoa:Marc-Bielert
```

# A Fazer

As doações devem ser sempre rastreadas claramente, seja através de uma conta separada ou de etiquetas (tags).
Isto é importante para os [Relatórios de Atividades](../_inbox/Tätigkeitsberichte.md) que temos de elaborar anualmente. #aFazer
