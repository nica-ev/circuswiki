---
lang: pt
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Solução de problemas
description: Problemas comuns do Fava e Beancount e como resolvê-los.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:46+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:46+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Resolução de Problemas

## O Fava não abre

Verifique:

- A janela do terminal ainda está aberta?
- O Fava foi iniciado na pasta correta?
- A porta correta está a ser utilizada?
- Já existe outra instância do Fava a correr na mesma porta?
- O Fava está instalado e disponível no terminal?

Comandos:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Execute cada comando apenas a partir da pasta do livro-razão correta.

## O Fava mostra um erro do Beancount

Causas comuns:

- Erro de digitação no nome de uma conta.
- Diretiva `open` de conta em falta.
- O montante utiliza vírgula em vez de ponto.
- Faltam aspas à volta do beneficiário ou da narração.
- Uma transação não está equilibrada.
- Uma verificação de saldo não corresponde.
- Uma transação utiliza uma conta após o seu encerramento.

Corrija o ficheiro de texto, guarde-o e, em seguida, recarregue o Fava.

## A verificação de saldo falha

Não elimine a verificação de saldo como solução alternativa. Investigue a diferença.

Lista de verificação:

- O intervalo de datas do CSV estava completo?
- O mesmo CSV foi importado duas vezes?
- Algumas transações foram coladas no livro-razão errado?
- Uma transação foi atribuída à subconta Sparkasse errada?
- Um sinal de montante foi alterado incorretamente?
- Uma transferência PayPal ou em dinheiro foi registada apenas num lado?
- Existem edições manuais mais antigas após a verificação de saldo anterior?

## A conversão de CSV falha

Verifique:

- O ficheiro CSV está na mesma pasta `test` que `csv2bean.py`.
- O nome do ficheiro no comando está exato.
- O ficheiro é a exportação Sparkasse `Excel (CSV-CAMT V2)`.
- O ficheiro é separado por ponto e vírgula.
- O CSV não foi aberto e guardado novamente de forma a alterar o seu formato.

## As entradas importadas parecem demasiado genéricas

Isto é esperado. O conversor utiliza categorias de reserva como:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

O utilizador deve rever e classificar as entradas importadas manualmente.

## O painel de controlo está em falta

Verifique:

- `fava-dashboards` está instalado.
- O livro-razão contém a diretiva `custom "fava-extension" "fava_dashboards"`.
- Existe um ficheiro `dashboards.yaml` ao lado do livro-razão.
- O Fava foi reiniciado após a instalação ou alterações de configuração.

## Um projeto não aparece nos painéis de controlo

Verifique:

- O projeto tem uma conta de ativo de projeto sob o prefixo Sparkasse ou PayPal esperado.
- A conta do projeto não está fechada.
- O saldo do projeto não é exatamente zero.
- O nome da conta corresponde ao padrão de consulta do painel de controlo.

## O link do documento não funciona

Verifique:

- O caminho do ficheiro é relativo à pasta do ficheiro do livro-razão.
- O nome do ficheiro está escrito exatamente.
- O documento não foi movido após a ligação.
- O caminho utiliza barras normais ou o estilo de caminho relativo normal.

## Não tem a certeza de como classificar uma transação

Use esta ordem:

1. Procure transações antigas semelhantes no Fava.
2. Verifique o contexto do projeto ou da fatura.
3. Verifique se pertence a uma linha de orçamento de financiador.
4. Adicione um comentário se tiver incertezas.
5. Utilize temporariamente `Sonstiges` apenas se não houver uma categoria melhor conhecida.
6. Pergunte à pessoa responsável pelo projeto ou finanças antes de finalizar.
