---
lang: cs
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Zadávání a úprava transakcí
description: Popisuje, jak uživatelé kontrolují, klasifikují, opravují a zadávají účetní transakce.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:58+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:58+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Zadávání a úprava transakcí

Většina záznamů pochází z importovaných bankovních dat, ale uživatelé stále potřebují transakce kontrolovat, klasifikovat, opravovat a někdy je zadávat ručně.

## Stav transakce

V účetních knihách se u importovaných transakcí běžně používá znak `!`:

```beancount
2026-03-12 ! "Příjemce" "Text z banky"
```

Použijte tento znak jako standardní, pokud se tým nerozhodne pro přísnější konvenci stavů.

## Základní zadání příjmu

```beancount
2026-01-15 ! "Max Mustermann" "Členský příspěvek 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Základní zadání výdaje

```beancount
2026-01-20 ! "Název dodavatele" "Faktura 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Příjem z projektu

```beancount
2026-02-10 ! "Poskytovatel financování" "Platba grantu projekt 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Výdaj na projekt

```beancount
2026-02-15 ! "Jméno osoby" "Honorář projekt 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Interní přesun mezi projektem a volnými prostředky

Někdy je nutné transakcí alokovat bankovní prostředky mezi účet specifický pro projekt a volné prostředky. Skutečný bankovní účet je jeden fyzický účet Sparkasse, ale účetní kniha sleduje interní zůstatky projektů odděleně.

```beancount
2026-02-20 ! "Interní alokace" "Přesun zbývajících prostředků projektu na volné peníze"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Interní převody provádějte pouze tehdy, když rozumíte důvodu, proč se má interní zůstatek projektu změnit.

## Proplacení osobám

Pokud někdo zaplatil z vlastních prostředků a je mu později proplaceno, obvyklý čistý postup je zaúčtovat výdaj proti závazku a poté závazek vyrovnat bankovní platbou.

```beancount
2026-03-01 ! "Obchod" "Materiál zakoupený Marcem"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Proplacení materiálu"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Komentáře k nejasným rozhodnutím

```beancount
; Není jasné, zda to patří k CEDU-25 nebo k prostředkům volného sdružení. Zkontrolovat fakturu.
2026-03-10 ! "Dodavatel" "Faktura 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Bezpečné úpravy

Před úpravou zkontrolujte:

- Jste ve správné účetní knize sdružení.
- Neupravujete vygenerovaný výstup importu, jako by to byla finální účetní kniha.
- Datum transakce je správné.
- Částka používá jako desetinný oddělovač tečku, například `12.50 EUR`.
- Názvy účtů jsou napsány přesně jako existující účty.
- Transakce projektu používají konzistentně účet aktiv projektu a kategorii příjmů/výdajů projektu.

Po úpravě soubor uložte, znovu načtěte Favu, zkontrolujte chyby a prohlédněte si příslušnou stránku účtu.
