---
lang: hu
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava irányítópultok és jelentések
description: A Fava jelentések és egyéni irányítópultok áttekintése a könyvelés felülvizsgálatához.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:11+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:11+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Fava irányítópultok és jelentések

A Fava alapértelmezett könyvelési jelentéseket kínál. A rendszer egyéni áttekintő oldalakhoz a `fava-dashboards` bővítményt is használja.

## Alapértelmezett Fava nézetek

| Nézet | Mire használható |
| --- | --- |
| Mérleg | Eszközök, kötelezettségek, szabad pénz, PayPal, készpénz és projektmérlegek ellenőrzésére. |
| Eredménykimutatás | Jövedelmek és kiadások időbeli alakulásának megtekintésére. |
| Számlaoldal | Egy adott számla összes tranzakciójának vizsgálatára. |
| Főkönyv | A tranzakciók időrendi előzményeinek keresésére. |
| Lekérdezés | Egyéni Beancount lekérdezések futtatására szükség esetén. |
| Dokumentumok | Hivatkozott bizonylatok és fájlok megtalálására. |

## Irányítópult bővítmény

A főkönyvi fájlok tartalmazzák ezt a direktívát:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Ez aktiválja az irányítópult bővítményt, ha a `fava-dashboards` telepítve van.

## Irányítópult konfigurációs fájlok

Az irányítópult fájlok neve `dashboards.yaml`. Ezek a főkönyvi fájlok közelében, illetve a megosztott könyvelési szinten tárolódnak.

## Fő irányítópult szekciók

| Irányítópult | Célja |
| --- | --- |
| `Vorstand-Cockpit` | Vezetőségi áttekintés: szabad pénz, teljes Sparkasse egyenleg, PayPal, készpénz, likviditási trend, havi eredmény, aktív projektmérlegek. |
| `Details & Daten` | Részletes grafikonok: kiadások kategóriák szerint, bevételek kategóriák szerint, pénzforgalom, projekt/személy hálózat. |

## Fontos irányítópult mutatók

### Freies Geld (Szabad pénz)

A korlátozott projektalapokon kívül rendelkezésre álló pénzt mutatja. Tipikus számlák: `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` és `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Teljes Sparkasse egyenleg)

A fő bankszámla és a belső alszámlák teljes Sparkasse egyenlegét mutatja.

### PayPal

A PayPal egyenleget mutatja. Negatív PayPal egyenleg esetén ellenőrzést igényel.

### Barkasse (Kassza)

A készpénztár egyenlegét mutatja.

### Saldo Aktiver Projekte (Aktív projektek egyenlege)

A nullától eltérő projektmérlegeket mutatja. Ez hasznos annak megtekintésére, hogy mely projektekben maradt pénz, vagy melyek lépték túl a keretet.

### Monatlicher Ueberschuss / Fehlbetrag (Havi többlet / Hiány)

A havi működési többletet vagy hiányt mutatja, a projekt számlák kivételével az irányítópult lekérdezéséből.

## Hogyan használjuk felelősségteljesen az irányítópultokat

Az irányítópultok összefoglalók. Ha egy szám meglepőnek tűnik:

1. Kattintson a hivatkozott Fava számlára vagy jelentésre.
2. Vizsgálja meg az alapjául szolgáló tranzakciókat.
3. Ellenőrizze, hogy egy tranzakció még mindig a `Sonstiges` (Egyéb) vagy `Bank Dump` (Banki mentés) kategóriában van-e.
4. Ellenőrizze, hogy a számla neve megegyezik-e az irányítópult lekérdezési mintájával.
5. Erősítse meg a mérlegellenőrzéseket, mielőtt megbízik a vezetőségi számokban.

## Ha az irányítópult számai hibásnak tűnnek

Gyakori okok:

- Egy tranzakciót a fő bankszámlára könyveltek a projekt alszámla helyett.
- Egy projekt számlát lezártak, de még mindig nullától eltérő egyenlege van.
- Egy új projekt olyan elnevezési mintát használ, amely nem szerepel az irányítópult lekérdezésében.
- Egy tranzakció még mindig egy általános tartalék kategóriában van.
- Az irányítópult fájl egy másik főkönyvhöz tartozik, mint a jelenleg megnyitott.
