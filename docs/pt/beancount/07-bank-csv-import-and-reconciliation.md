---
lang: pt
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Importação e Conciliação de CSV Bancário
description: Fluxo de trabalho para importar dados CSV do Sparkasse e conciliar saldos bancários.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:40+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:40+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Importação e Conciliação de CSV Bancário

Este fluxo de trabalho traz novas transações da Sparkasse para o Beancount e confirma que o livro-razão ainda corresponde à conta bancária real.

## Onde ocorrem as importações

| Associação | Pasta de importação | Script | Arquivo de saída |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Antes de exportar da Sparkasse

1. Abra o arquivo do livro-razão correto.
2. Encontre a seção `Balance Checks` (Verificações de Saldo).
3. Encontre a data do último saldo para a conta Sparkasse.
4. Verifique também a seção `Bank Dump` (Depósito Bancário) na parte inferior para a última data importada.
5. Use a data posterior dessas como seu ponto de partida.

Isso evita a perda de transações ou a importação do mesmo período duas vezes.

## Exportando da Sparkasse

1. Abra a visão geral da conta.
2. Filtre por intervalo de datas.
3. Comece a partir da última data verificada ou importada.
4. Termine com hoje ou a data de conciliação desejada.
5. Exporte como `Excel (CSV-CAMT V2)`.
6. Copie o CSV baixado para a pasta `test` correta.

Os scripts esperam o formato Sparkasse CSV-CAMT-V2 com colunas separadas por ponto e vírgula.

## Convertendo o CSV

Abra um terminal na pasta `test` correta e execute:

```powershell
python csv2bean.py "NOME-DO-ARQUIVO-BAIXADO.CSV"
```

Exemplo:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Se funcionar, o script imprimirá `Process finished.` (Processo concluído) e criará ou substituirá `beancount_file.beancount`.

## O que o conversor faz

O conversor cria entradas básicas do Beancount:

- Valores recebidos vão para a conta de ativo Sparkasse e `Einnahmen:Sonstiges` (Receitas: Outros) por padrão.
- Valores enviados vão para `Ausgaben:Sonstiges` (Despesas: Outras) e a conta de ativo Sparkasse por padrão.
- Algumas descrições de receita são automaticamente classificadas como `Einnahmen:Vereinsbeitrag` (Receitas: Contribuição da Associação).
- Alguns textos relacionados ao Tohuwabohu podem ser classificados como uma conta de receita de projeto.

O conversor é apenas uma primeira passagem. Ele não conhece o significado contábil final de cada transação.

## Copiando para o livro-razão principal

1. Abra `test/beancount_file.beancount`.
2. Ignore o cabeçalho de opções gerado.
3. Copie apenas as transações.
4. Cole-as no livro-razão principal, primeiro sob `Bank Dump`.
5. Adicione um separador datado para a data de importação, se necessário.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

O `Bank Dump` é uma área de preparação. As transações importadas podem ser movidas posteriormente para a seção temática ou de projeto correta.

## Classificando entradas importadas

Para cada transação importada, decida:

- É em nível de associação ou de projeto?
- É receita ou despesa?
- É um reembolso ou pagamento de responsabilidade?
- Pertence ao `Freies-Geld` (Dinheiro Livre) ou a uma conta de ativo específica do projeto?
- Existe um recibo ou fatura para anexar?

Substitua contas genéricas de fallback, como `Ausgaben:Sonstiges`, quando existir uma conta mais precisa.

## Adicionando uma verificação de saldo

Exemplo NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Exemplo Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Use o saldo exibido pela Sparkasse para essa data exata.

## Validando no Fava

1. Salve o arquivo do livro-razão.
2. Recarregue o Fava.
3. Verifique se há erros na parte superior da página do Fava.
4. Abra a página da conta Sparkasse.
5. Confirme o saldo corrente e as últimas transações.
6. Verifique o Balanço Patrimonial.
7. Verifique os painéis de projetos se as contas de projeto foram afetadas.

## Se a verificação de saldo falhar

Causas comuns:

- A exportação CSV perdeu um dia no início ou no fim.
- Uma transação foi importada duas vezes.
- Uma transação foi colada no livro-razão da associação errada.
- Um número foi editado incorretamente.
- Uma divisão de projeto usou o sinal errado.
- Movimentações do PayPal ou em dinheiro não foram registradas também.

Não remova a verificação de saldo apenas para fazer o erro desaparecer. Corrija a diferença subjacente da transação.
