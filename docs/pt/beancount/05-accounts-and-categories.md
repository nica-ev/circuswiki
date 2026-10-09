---
lang: pt
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Contas e Categorias
description: Explica a estrutura de contas alemã e as convenções de categoria usadas nos livros razão.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:30+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:30+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Contas e Categorias

Esta página explica a estrutura de contas utilizada nos livros-razão.

## Idioma dos Nomes

Os nomes das contas são em alemão. Continue a usar os nomes de contas existentes para manter a consistência dos relatórios.

| Alemão | Significado em Inglês |
| --- | --- |
| `Vermoegen` | Ativos |
| `Verbindlichkeiten` | Passivos |
| `Einnahmen` | Receitas |
| `Ausgaben` | Despesas |
| `Buero` | Escritório |
| `Verein` | Associação/atividade geral da associação |
| `Projekt` | Projeto |
| `Barkasse` | Caixa |
| `Freies-Geld` | Fundos livres/irrestritos |

## Contas de Ativos

Exemplos NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Exemplos Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Contas Gerais de Receitas

| Conta | Uso para |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Taxas de adesão. |
| `Einnahmen:Spende` | Doações. |
| `Einnahmen:Verleih` | Receita de aluguel ou empréstimo. |
| `Einnahmen:Sonstiges` | Outras receitas que não se encaixam em outro lugar. |

## Contas Gerais de Despesas

| Conta | Uso para |
| --- | --- |
| `Ausgaben:Buero:Miete` | Aluguel de escritório ou sala. |
| `Ausgaben:Buero:Internet` | Internet e serviços digitais. |
| `Ausgaben:Buero:Sonstiges` | Outras despesas de escritório. |
| `Ausgaben:Verein:Versicherung` | Seguro da associação. |
| `Ausgaben:Verein:Ehrenamt` | Subsídios para voluntários ou custos de voluntariado da associação. |
| `Ausgaben:Essen` | Despesas com alimentação fora de um projeto específico. |
| `Ausgaben:Sonstiges` | Opção temporária para despesas não claras. |

`Ausgaben:Sonstiges` e `Einnahmen:Sonstiges` são úteis durante a importação, mas não devem se tornar a categoria final se existir uma categoria mais precisa.

## Contas de Projetos

As contas de projetos seguem este padrão:

```text
Vermoegen:Bank:Sparkasse-ASSOCIACAO:PROJETO
Ausgaben:Projekt:PROJETO
Einnahmen:Projekt:PROJETO
```

Exemplos:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Subcategorias Típicas de Projetos

| Subcategoria | Significado |
| --- | --- |
| `Honorar` | Taxas pagas a pessoas ou recebidas por trabalho. |
| `Aufwand` | Subsídio de esforço ou despesa. |
| `Sachmittel` | Materiais e suprimentos. |
| `Sonstiges` | Outros custos ou receitas do projeto. |
| `Pauschale` / `Pauschalen` | Orçamento de projeto em valor fixo ou global. |

## Passivos com Pessoas

As contas de passivos rastreiam dinheiro devido a pessoas ou pago de volta a pessoas. Exemplos incluem `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` e `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Escolhendo a Conta Correta

1. É a nível da associação ou a nível do projeto?
2. Se for a nível do projeto, qual projeto é o dono do dinheiro?
3. É receita, despesa, movimento de ativo ou reembolso de passivo?
4. Existe uma categoria precisa já aberta?
5. Se não houver uma boa categoria, use `Sonstiges` temporariamente e adicione um comentário.
