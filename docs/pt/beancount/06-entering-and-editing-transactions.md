---
lang: pt
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Inserir e Editar Transações
description: Descreve como os usuários revisam, classificam, corrigem e inserem transações contábeis.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:53:48+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:53:48+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Inserir e Editar Transações

A maioria das entradas provém de dados bancários importados, mas os utilizadores ainda precisam de rever, classificar, corrigir e, por vezes, inserir transações manualmente.

## Estado da transação

Os livros de contabilidade utilizam comummente `!` em transações importadas:

```beancount
2026-03-12 ! "Payee" "Bank text"
```

Utilize este marcador como normal, a menos que a equipa decida uma convenção de estado mais rigorosa.

## Entrada básica de rendimento

```beancount
2026-01-15 ! "Max Mustermann" "Mitgliedsbeitrag 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Entrada básica de despesa

```beancount
2026-01-20 ! "Provider Name" "Invoice 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Rendimento de projeto

```beancount
2026-02-10 ! "Funding Body" "Grant payment project 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Despesa de projeto

```beancount
2026-02-15 ! "Person Name" "Honorar project 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Movimento interno entre projeto e fundos livres

Por vezes, uma transação deve alocar dinheiro bancário entre uma conta de ativo específica do projeto e fundos livres. A conta bancária real é uma conta física da Sparkasse, mas o livro de contabilidade acompanha os saldos internos do projeto separadamente.

```beancount
2026-02-20 ! "Internal allocation" "Move remaining project funds to free money"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Faça transferências internas apenas quando compreender porque é que o saldo interno do projeto deve ser alterado.

## Reembolsos a pessoas

Se alguém pagou privadamente e for reembolsado mais tarde, o padrão limpo é geralmente registar a despesa contra um passivo e, em seguida, liquidar o passivo com o pagamento bancário.

```beancount
2026-03-01 ! "Shop" "Material bought by Marc"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Reimbursement material"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Comentários para decisões pouco claras

```beancount
; Unclear whether this belongs to CEDU-25 or free association funds. Check invoice.
2026-03-10 ! "Vendor" "Invoice 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Edição segura

Antes de editar, verifique:

- Está no livro de contabilidade correto da associação.
- Não está a editar a saída de importação gerada como se fosse o livro de contabilidade final.
- A data da transação está correta.
- O montante utiliza um ponto como separador decimal, por exemplo `12.50 EUR`.
- Os nomes das contas estão escritos exatamente como as contas existentes.
- As transações de projeto utilizam a conta de ativo do projeto e a categoria de rendimento/despesa do projeto de forma consistente.

Após editar, guarde o ficheiro, recarregue o Fava, verifique se há erros e inspecione a página da conta relevante.
