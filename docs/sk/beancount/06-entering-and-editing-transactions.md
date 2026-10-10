---
lang: sk
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Zadanie a úprava transakcií
description: Opisuje, ako používatelia kontrolujú, klasifikujú, opravujú a zadávajú účtovné transakcie.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:03+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Zadanie a úprava transakcií

Väčšina záznamov pochádza z importovaných bankových údajov, ale používatelia stále potrebujú transakcie skontrolovať, klasifikovať, opraviť a niekedy zadať manuálne.

## Stav transakcie

V účtovných knihách sa pri importovaných transakciách bežne používa znak `!`:

```beancount
2026-03-12 ! "Odberateľ" "Banka text"
```

Použite tento znak ako bežný označovač, pokiaľ sa tím nerozhodne pre prísnejšiu konvenciu stavu.

## Základný príjem

```beancount
2026-01-15 ! "Max Mustermann" "Členský príspevok 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Základný výdavok

```beancount
2026-01-20 ! "Názov dodávateľa" "Faktúra 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Príjem z projektu

```beancount
2026-02-10 ! "Poskytovateľ financovania" "Platba grantu projekt 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Výdavok na projekt

```beancount
2026-02-15 ! "Meno osoby" "Honorár projekt 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Interný presun medzi projektom a voľnými prostriedkami

Niekedy je potrebné transakciou alokovať bankové peniaze medzi účet špecifický pre projekt a voľné prostriedky. Skutočný bankový účet je jeden fyzický účet Sparkasse, ale účtovná kniha sleduje interné zostatky projektov oddelene.

```beancount
2026-02-20 ! "Interná alokácia" "Presun zvyšných projektových prostriedkov na voľné peniaze"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Interné prevody vykonávajte iba vtedy, keď rozumiete dôvodu, prečo sa musí zmeniť interný zostatok projektu.

## Preplatenie osobám

Ak niekto zaplatil z vlastných prostriedkov a neskôr mu boli peniaze preplatené, bežným postupom je zaúčtovanie výdavku voči záväzku a následné vyrovnanie záväzku bankovou platbou.

```beancount
2026-03-01 ! "Obchod" "Materiál zakúpený Marcom"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Preplatenie materiálu"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Komentáre k nejasným rozhodnutiam

```beancount
; Nie je jasné, či to patrí k CEDU-25 alebo k fondom slobodného združenia. Skontrolujte faktúru.
2026-03-10 ! "Predajca" "Faktúra 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Bezpečné úpravy

Pred úpravou skontrolujte:

- Ste v správnej účtovnej knihe združenia.
- Neupravujete vygenerovaný výstup importu, akoby to bola konečná účtovná kniha.
- Dátum transakcie je správny.
- Suma používa bodku ako desatinnú čiarku, napríklad `12.50 EUR`.
- Názvy účtov sú napísané presne ako existujúce účty.
- Projektové transakcie používajú konzistentne projektový účet aktív a kategóriu príjmov/výdavkov projektu.

Po úprave uložte súbor, znova načítajte Fava, skontrolujte chyby a prezrite si príslušnú stránku účtu.
