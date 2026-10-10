---
lang: cs
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Příjmy a dokumenty
description: Vysvětluje, kde jsou uloženy podpůrné dokumenty a jak transakce odkazují na příjmy.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:59+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:59+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Účtenky a dokumenty

Účtenky, faktury, smlouvy a další podpůrné dokumenty zajišťují auditovatelnost transakcí. Účetní kniha by měla umožnit dohledání dokumentu k danému výdaji.

## Kde jsou dokumenty uloženy

Tohuwabohu má v současnosti jasně definovanou složku pro účtenky:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Účtenky již zadané do účetní knihy se často nacházejí v:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA používá podpůrné soubory ve své účetní složce a projektových složkách. Pokud bude v budoucnu zavedena jednotná složka pro účtenky NICA, zdokumentujte ji zde a důsledně ji používejte.

## Položky `document`

Položka `document` propojuje soubor s účtem a datem:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Cesta k souboru je relativní ke složce obsahující soubor účetní knihy.

## Odkazy na dokumenty s tagy

Některé starší položky obsahují tagy dokumentů, například:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Část `^2023_001` je odkaz v Beancountu. Může propojit účtenku s příslušnou transakcí, pokud je stejný odkaz použit i tam.

## Význam `scanned`

Komentáře v účetních knihách definují konvenci pro naskenované účtenky. Pokud je použit tag `scanned`, znamená to:

- Účtenka byla naskenována nebo digitalizována.
- Obrázek byl zmenšen a optimalizován, například pomocí TinyPNG.
- Soubor byl uložen podle vzoru rok a číslo, například `2023_002.jpg`.
- Číslo je uvedeno v příslušné položce účetní knihy.

## Dobré názvy souborů

Dobré názvy souborů účtenek jsou stabilní a čitelné:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Vyhněte se názvům jako `scan.jpg`, `image1.jpg` nebo `download.pdf`.

## Pracovní postup pro novou účtenku

1. Uložte účtenku do správné složky pro účtenky.
2. Přejmenujte ji tak, aby byla později rozpoznatelná.
3. Zadejte nebo najděte příslušnou transakci.
4. Přidejte řádek `document` nebo metadata s odkazem, pokud je to užitečné.
5. Pokud byla účtenka zpracována, přesuňte ji do složky `Eingetragen`, pokud je to taková konvence.
6. Znovu načtěte Fava a zkontrolujte, zda odkaz na dokument funguje.

## Když účtenka chybí

Pokud účtenka chybí, přidejte komentář poblíž transakce:

```beancount
; Receipt missing. Ask responsible person.
```

Nepředstírejte, že dokument existuje, pokud není k dispozici.

## Smlouvy a faktury za honoráře

Smlouvy a faktury za honoráře by měly být uloženy poblíž příslušného projektu nebo účetní složky a jasně odkazovány. Pro audit projektů je důležitá nejen existence transakce, ale také rychlé dohledání dokumentu, který výdaj dokládá.
