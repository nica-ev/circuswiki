---
lang: sk
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Dashboardy a reporty
description: Prehľad reportov Fava a vlastných dashboardov na kontrolu účtovníctva.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:39+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:39+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 – Fava dashboardy a prehľady

Fava poskytuje štandardné účtovné prehľady. Systém tiež používa `fava-dashboards` na vlastné prehľadové stránky.

## Štandardné pohľady Favy

| Pohľad | Použitie na |
| --- | --- |
| Súvaha | Kontrolu aktív, pasív, voľných prostriedkov, PayPal, hotovosti a zostatkov projektov. |
| Výkaz ziskov a strát | Zobrazenie príjmov a výdavkov v čase. |
| Stránka účtu | Kontrolu všetkých transakcií pre jeden účet. |
| Denník | Vyhľadávanie chronologickej histórie transakcií. |
| Dopyt | Spustenie vlastných Beancount dopytov podľa potreby. |
| Dokumenty | Vyhľadanie prepojených potvrdeniek a súborov. |

## Rozšírenie dashboardu

Ledger obsahuje túto direktívu:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Toto aktivuje rozšírenie dashboardu, ak je nainštalovaný balík `fava-dashboards`.

## Konfiguračné súbory dashboardu

Súbory dashboardu sa nazývajú `dashboards.yaml`. Sú uložené v blízkosti súborov ledgeru a na zdieľanej úrovni účtovníctva.

## Hlavné sekcie dashboardu

| Dashboard | Účel |
| --- | --- |
| `Vorstand-Cockpit` | Prehľad pre manažment: voľné peniaze, celkový zostatok Sparkasse, PayPal, hotovosť, trend likvidity, mesačný výsledok, zostatky aktívnych projektov. |
| `Details & Daten` | Detailné grafy: výdavky podľa kategórie, príjmy podľa kategórie, peňažný tok, sieť projektov/osôb. |

## Dôležité ukazovatele dashboardu

### Voľné peniaze (Freies Geld)

Zobrazuje peniaze dostupné mimo obmedzených projektových fondov. Typické účty sú `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` a `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Celkovo Sparkasse (Sparkasse Gesamt)

Zobrazuje celkový zostatok na účtoch Sparkasse naprieč hlavným bankovým účtom a internými podúčetmi.

### PayPal

Zobrazuje zostatok na PayPal účte. Záporný zostatok na PayPale naznačuje, že je potrebné niečo skontrolovať.

### Hotovosť (Barkasse)

Zobrazuje zostatok v pokladnici.

### Zostatok aktívnych projektov (Saldo Aktiver Projekte)

Zobrazuje nenulové zostatky projektov. Toto je užitočné na zistenie, ktoré projekty stále držia peniaze alebo sú prekročené.

### Mesačný prebytok / deficit (Monatlicher Ueberschuss / Fehlbetrag)

Zobrazuje mesačný prevádzkový prebytok alebo deficit, pričom do dopytu dashboardu nie sú zahrnuté projektové účty.

## Ako zodpovedne používať dashboardy

Dashboardy sú súhrny. Ak sa nejaké číslo zdá byť prekvapivé:

1. Kliknite na prepojený účet alebo prehľad Favy.
2. Skontrolujte podkladové transakcie.
3. Skontrolujte, či transakcia stále nie je v sekcii `Sonstiges` (Rôzne) alebo `Bank Dump`.
4. Skontrolujte, či názov účtu zodpovedá vzoru dopytu dashboardu.
5. Pred dôverou v manažérske čísla potvrďte kontroly zostatkov.

## Keď sa čísla na dashboarde zdajú byť nesprávne

Bežné príčiny:

- Transakcia bola zaúčtovaná na hlavný bankový účet namiesto projektového podúctu.
- Projektový účet bol uzavretý, ale stále má nenulový zostatok.
- Nový projekt používa vzor pomenovania, ktorý nie je zahrnutý v dopyte dashboardu.
- Transakcia je stále v širokej záložnej kategórii.
- Súbor dashboardu patrí k inému ledgeru, než je aktuálne otvorený.
