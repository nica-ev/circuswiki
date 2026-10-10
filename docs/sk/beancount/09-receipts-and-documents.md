---
lang: sk
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Príjmy a dokumenty
description: Vysvetľuje, kde sú uložené podporné dokumenty a ako transakcie odkazujú na príjmy.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:03+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Príjmy a dokumenty

Príjmy, faktúry, zmluvy a iné podporné dokumenty umožňujú auditovať transakcie. Účtovná kniha by mala umožniť nájsť dokument súvisiaci s výdavkom.

## Kde sú dokumenty uložené

Tohuwabohu má momentálne jasne definovaný priečinok na príjmy:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Príjmy, ktoré už boli zadané do účtovnej knihy, sa často nachádzajú v:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA používa podporné súbory vo svojom priečinku účtovníctva a projektových priečinkoch. Ak bude neskôr zavedený jednotný priečinok pre príjmy NICA, zdokumentujte to tu a používajte ho konzistentne.

## Záznamy `document`

Záznam `document` spája súbor s účtom a dátumom:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Cesta k súboru je relatívna k priečinku obsahujúcemu súbor účtovnej knihy.

## Odkazy na dokumenty s tagmi

Niektoré staršie záznamy obsahujú tagy dokumentov, ako napríklad:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Časť `^2023_001` je odkaz Beancount. Môže spojiť príjem s príslušnou transakciou, ak sa tam použije rovnaký odkaz.

## Význam `scanned`

Komentáre v účtovných knihách definujú konvenciu pre skenované príjmy. Keď sa použije tag `scanned`, znamená to:

- Príjem bol naskenovaný alebo digitalizovaný.
- Obrázok bol zmenšený a optimalizovaný, napríklad pomocou TinyPNG.
- Súbor bol uložený pomocou vzoru roka a čísla, napríklad `2023_002.jpg`.
- Číslo je uvedené v príslušnom zázname účtovnej knihy.

## Dobré názvy súborov

Dobré názvy súborov príjmov sú stabilné a čitateľné:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Vyhnite sa názvom ako `scan.jpg`, `image1.jpg` alebo `download.pdf`.

## Pracovný postup pre nový príjem

1. Uložte príjem do správneho priečinka na príjmy.
2. Premenujte ho tak, aby sa dal neskôr rozpoznať.
3. Zadajte alebo vyhľadajte príslušnú transakciu.
4. Pridajte riadok `document` alebo metaúdaj odkazu, ak je to užitočné.
5. Ak bol príjem spracovaný, presuňte ho do priečinka `Eingetragen`, ak je to takáto konvencia.
6. Znova načítajte Fava a skontrolujte, či odkaz na dokument funguje.

## Keď príjem chýba

Ak príjem chýba, pridajte komentár k transakcii:

```beancount
; Receipt missing. Ask responsible person.
```

Nepredstierajte, že dokument existuje, ak nie je k dispozícii.

## Zmluvy a faktúry za honoráre

Zmluvy a faktúry za honoráre by mali byť uložené v blízkosti príslušného projektu alebo priečinka účtovníctva a jasne odkázané. Pri projektových auditoch je dôležitou otázkou nielen existencia transakcie, ale aj to, či sa dá rýchlo nájsť dokument potvrdzujúci výdavok.
