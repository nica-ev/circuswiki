---
lang: pt
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Glossário
description: Definições de termos de contabilidade, Beancount, Fava e contabilidade de projetos usados nesta documentação.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:17+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 - Glossário

## Conta

Um local nomeado onde o Beancount registra dinheiro ou valor. Exemplo: `Ausgaben:Buero:Miete`.

## Ativo

Algo que a associação possui ou controla, como dinheiro em banco, saldo do PayPal, dinheiro em espécie ou inventário. Neste sistema, os ativos estão sob `Vermoegen`.

## Verificação de saldo

Uma linha que confirma que uma conta tem um saldo específico em uma data específica. As verificações de saldo são usadas para verificar se o livro-razão corresponde aos registros bancários, do PayPal ou em dinheiro.

## Dump Bancário

Uma seção de preparação perto do final do livro-razão onde as transações bancárias importadas são coladas pela primeira vez antes de serem totalmente classificadas.

## Beancount

O formato de contabilidade em texto simples usado como fonte da verdade do sistema.

## CSV

Um arquivo de exportação semelhante a uma planilha. O Sparkasse exporta arquivos CSV que são convertidos em transações Beancount.

## Patrimônio Líquido

Família de contas Beancount usada para saldos iniciais e para equilibrar pontos de partida históricos.

## Fava

A interface do navegador para visualizar e trabalhar com livros-razão Beancount.

## Dashboards Fava

Uma extensão que adiciona páginas de dashboard personalizadas ao Fava.

## Freies-Geld

Dinheiro livre ou irrestrito que não é atribuído a um orçamento de projeto restrito.

## Receita

Dinheiro recebido. Neste sistema, as contas de receita começam com `Einnahmen`.

## Livro-razão

O arquivo de contabilidade contendo contas, transações, verificações de saldo e documentos. Os livros-razão principais são `nica.beancount` e `2023.beancount`.

## Passivo

Dinheiro devido a outra pessoa. Neste sistema, os passivos estão sob `Verbindlichkeiten`.

## Beneficiário

A pessoa ou organização nomeada em uma transação.

## Conta de projeto

Uma conta usada para rastrear dinheiro para um projeto específico separadamente do dinheiro geral da associação.

## Conciliação

O processo de verificar se o Beancount e o saldo real do banco ou PayPal correspondem.

## Recibo

Um documento que comprova uma despesa, como uma fatura, contrato ou recibo em dinheiro.

## Sonstiges

Alemão para "diversos" ou "outros". Útil como um fallback temporário, mas categorias específicas são melhores para a contabilidade final.

## Transação

Uma entrada contábil datada descrevendo um evento financeiro.

## Verwendungsnachweis

Um relatório do financiador do projeto explicando como o dinheiro concedido foi usado.
