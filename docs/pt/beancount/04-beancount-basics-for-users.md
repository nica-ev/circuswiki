---
lang: pt
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Noções Básicas do Beancount para Usuários
description: Apresenta o formato de texto do Beancount e os padrões de transação usados nos livros-razão.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:36+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:36+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Noções Básicas de Beancount para Utilizadores

O Beancount armazena a contabilidade como texto legível. Cada transação indica o que aconteceu, em que data, quem esteve envolvido e quais contas foram alteradas.

## Estrutura básica de uma transação

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Parte | Significado |
| --- | --- |
| `2026-01-13` | Data da transação. |
| `!` | Marcador de estado. Neste sistema, é comummente usado para entradas importadas ou que ainda não foram totalmente revistas. |
| Primeiro texto entre aspas | Beneficiário ou remetente. |
| Segundo texto entre aspas | Descrição ou texto de lançamento do banco. |
| Primeira linha de conta | Para onde o dinheiro foi ou de onde veio. |
| Segunda linha de conta | A categoria oposta. Se nenhum montante for escrito, o Beancount calcula-o automaticamente. |

## Nomes de contas

Os nomes das contas são separados por dois pontos:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Lê-se da esquerda para a direita: ativo, conta bancária, Sparkasse NICA, fundos livremente disponíveis.

## As cinco famílias de contas

| Família | Significado | Exemplo |
| --- | --- | --- |
| `Vermoegen` | Ativos: banco, PayPal, dinheiro, inventário. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Passivos: dinheiro devido a pessoas ou a terceiros. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Saldos iniciais e lançamentos de regularização. | `Equity:Opening-Balances` |
| `Einnahmen` | Receitas. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Despesas. | `Ausgaben:Buero:Miete` |

## Sinais de receitas e despesas

Nos relatórios do Beancount, as receitas aparecem frequentemente com um sinal negativo internamente e as despesas com um sinal positivo. O Fava e os painéis de controlo apresentam muitas vezes estes valores de forma mais amigável para o utilizador. Não altere transações apenas porque um número de receita parece negativo numa consulta bruta.

## Verificações de saldo

Uma verificação de saldo afirma que uma conta deve ter um saldo específico numa determinada data:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Se o Beancount não conseguir corresponder a esse saldo com as transações anteriores a essa data, o Fava apresentará um erro. As verificações de saldo são o principal mecanismo de controlo de qualidade.

## Abrir e fechar contas

Antes de uma conta ser utilizada, ela é aberta:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Quando um projeto é concluído e a conta do projeto está zerada, ela pode ser fechada:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Normalmente, contas fechadas não devem receber novas transações.

## Comentários e documentos

Linhas que começam com `;` são comentários. Elas explicam decisões ou situações incertas e não afetam os números.

Recibos podem ser ligados com linhas `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
