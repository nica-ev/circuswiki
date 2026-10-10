---
lang: pt
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projetos e Fundos Restritos
description: Explica como o dinheiro de projetos e fundos restritos são representados e verificados.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:22+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:22+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projetos e Fundos Restritos

Projetos são centrais neste sistema de contabilidade. Muitas subvenções e atividades precisam ser rastreadas separadamente do dinheiro de livre associação.

## O que um projeto significa no livro-razão

| Tipo de conta | Exemplo | Propósito |
| --- | --- | --- |
| Ativo do projeto | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Saldo interno do dinheiro do projeto. |
| Receita do projeto | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Financiamento do projeto ou receita do projeto. |
| Despesa do projeto | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Gastos do projeto. |

A conta bancária real pode ser uma única conta Sparkasse, mas o livro-razão separa os saldos internos dos projetos para que a equipe possa ver o que pertence a cada projeto.

## Projetos ativos e encerrados

Projetos ativos têm contas abertas e saldos relevantes. Projetos encerrados geralmente têm uma verificação final de saldo de `0,00 EUR` e diretivas de `close` para as contas de ativo, receita e despesa do projeto.

Não registre novas transações em projetos encerrados, a menos que você pretenda reabri-los ou corrigir dados históricos intencionalmente.

## Exemplos atuais na NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- projetos encerrados de 2024, como `24-AWO`, `24-HONY`, `24-Peter`

## Exemplos atuais na Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- projetos encerrados como `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Criação de um novo projeto

Um novo projeto normalmente precisa de contas abertas antes que as transações sejam inseridas.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Abra apenas as categorias que são realmente úteis para o projeto.

## Registro de financiamento de projeto

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Registro de despesas de projeto

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Compreensão dos saldos de projeto

Um saldo de ativo de projeto positivo significa que há dinheiro ainda alocado para esse projeto. Um saldo de ativo de projeto zero significa que o projeto não tem saldo bancário interno restante. Um saldo de ativo de projeto negativo geralmente significa que o projeto gastou mais do que seus fundos alocados ou que uma alocação está faltando.

## Encerramento de um projeto

Antes de encerrar um projeto, todas as receitas e despesas devem ser registradas, os recibos devem ser localizáveis, a conta de ativo do projeto deve estar exatamente em zero e qualquer dinheiro restante deve ser transferido ou devolvido corretamente.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Encerre também as subcontas se elas foram abertas separadamente.
