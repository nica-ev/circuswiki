---
lang: sk
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Riešenie problémov
description: Bežné problémy s Fava a Beancount a ich riešenia.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:53+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:53+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 – Riešenie problémov

## Fava sa neotvorí

Skontrolujte:

- Je okno terminálu stále otvorené?
- Spustila sa Fava v správnom priečinku?
- Používa sa správny port?
- Beží už na rovnakom porte iná inštancia Favy?
- Je Fava nainštalovaná a dostupná v termináli?

Príkazy:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Každý príkaz spustite iba zo správneho priečinka účtovnej knihy.

## Fava zobrazuje chybu Beancountu

Bežné príčiny:

- Preklep v názve účtu.
- Chýbajúci príkaz `open` pre účet.
- Suma používa čiarku namiesto bodky.
- Chýbajú úvodzovky okolo príjemcu alebo popisu.
- Transakcia nie je vyrovnaná.
- Kontrola zostatku sa nezhoduje.
- Transakcia používa účet po jeho zatvorení.

Opravte textový súbor, uložte ho a potom obnovte Favu.

## Kontrola zostatku zlyháva

Ako riešenie neodstraňujte kontrolu zostatku. Preskúmajte rozdiel.

Kontrolný zoznam:

- Bol rozsah dátumov CSV úplný?
- Bol rovnaký CSV importovaný dvakrát?
- Boli niektoré transakcie vložené do nesprávnej účtovnej knihy?
- Bol transakcii priradený nesprávny podúčet Sparkasse?
- Bol nesprávne zmenený znak sumy?
- Bol prevod PayPal alebo hotovosti zadaný iba na jednej strane?
- Existujú staršie manuálne úpravy po predchádzajúcej kontrole zostatku?

## Konverzia CSV zlyháva

Skontrolujte:

- Súbor CSV je v rovnakom priečinku `test` ako `csv2bean.py`.
- Názov súboru v príkaze je presný.
- Súbor je export Sparkasse `Excel (CSV-CAMT V2)`.
- Súbor je oddelený bodkočiarkou.
- CSV nebol otvorený a znova uložený spôsobom, ktorý zmenil jeho formát.

## Importované položky vyzerajú príliš všeobecne

Toto je očakávané. Konvertor používa záložné kategórie ako napríklad:

- `Výdavky:Rôzne`
- `Príjmy:Rôzne`

Používateľ musí importované položky manuálne skontrolovať a klasifikovať.

## Chýba Dashboard

Skontrolujte:

- Je nainštalovaný `fava-dashboards`.
- Účtovná kniha obsahuje direktívu `custom "fava-extension" "fava_dashboards"`.
- Súbor `dashboards.yaml` existuje vedľa účtovnej knihy.
- Fava bola reštartovaná po inštalácii alebo zmenách konfigurácie.

## Projekt sa nezobrazuje v Dashboardoch

Skontrolujte:

- Projekt má účet aktív projektu pod očakávaným prefixom Sparkasse alebo PayPal.
- Účet projektu nie je zatvorený.
- Zostatok projektu nie je presne nula.
- Názov účtu zodpovedá vzoru dopytu v Dashboarde.

## Odkaz na dokument nefunguje

Skontrolujte:

- Cesta k súboru je relatívna voči priečinku súboru účtovnej knihy.
- Názov súboru je presne napísaný.
- Dokument nebol presunutý po prepojení.
- Cesta používa lomky dopredu alebo bežný štýl relatívnej cesty.

## Neviem klasifikovať transakciu

Použite toto poradie:

1. Vyhľadajte podobné staršie transakcie vo Fave.
2. Skontrolujte kontext projektu alebo faktúry.
3. Skontrolujte, či patrí do riadku rozpočtu financovateľa.
4. Ak si nie ste istí, pridajte komentár.
5. Dočasne použite `Rôzne` iba v prípade, že nie je známa lepšia kategória.
6. Pred finalizáciou sa opýtajte zodpovednej osoby pre projekt alebo financie.
