---
lang: hu
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projektek és elkülönített alapok
description: Elmagyarázza, hogyan jelennek meg és ellenőrizhetők a projektfinanszírozás és az elkülönített alapok.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:59+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:59+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projektek és elkülönített alapok

A projektek központi szerepet játszanak ebben a könyvelési rendszerben. Sok támogatást és tevékenységet külön kell kezelni a szabadon felhasználható pénzektől.

## Mit jelent egy projekt a főkönyvben

| Számlatípus | Példa | Cél |
| --- | --- | --- |
| Projekt eszköz | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | A projekt pénzének belső egyenlege. |
| Projekt bevétel | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Projektfinanszírozás vagy projektbevétel. |
| Projekt kiadás | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Projektkiadás. |

A tényleges bankszámla lehet egyetlen Sparkasse-számla, de a főkönyv elkülöníti a belső projektegyenlegeket, hogy a csapat láthassa, mi melyik projekthez tartozik.

## Aktív és lezárt projektek

Az aktív projekteknek nyitott számlái és releváns egyenlegei vannak. A lezárt projektek általában egy végső `0,00 EUR` egyenlegellenőrzéssel és `close` (lezárás) utasításokkal rendelkeznek a projekt eszköz-, bevételi és kiadási számláihoz.

Ne vezessen új tranzakciókat lezárt projektekbe, hacsak nem szándékosan nyitja meg újra vagy javítja a történelmi adatokat.

## Aktuális példák a NICÁ-ban

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- lezárt 2024-es projektek, mint például `24-AWO`, `24-HONY`, `24-Peter`

## Aktuális példák a Tohuwabohu-ban

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- lezárt projektek, mint például `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Új projekt létrehozása

Egy új projekthez általában számlákat kell nyitni a tranzakciók rögzítése előtt.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Csak azokat a kategóriákat nyissa meg, amelyek ténylegesen hasznosak a projekthez.

## Projektfinanszírozás rögzítése

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Projektkiadások rögzítése

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Projektmérlegek értelmezése

A pozitív projekt eszközmérleg azt jelenti, hogy továbbra is pénz van hozzárendelve a projekthez. A nulla projekt eszközmérleg azt jelenti, hogy a projektnek nincs belső banki egyenlege. A negatív projekt eszközmérleg általában azt jelenti, hogy a projekt többet költött, mint a hozzárendelt alapok, vagy hiányzik egy hozzárendelés.

## Projekt lezárása

A projekt lezárása előtt be kell vezetni az összes bevételt és kiadást, a bizonylatoknak megtalálhatónak kell lenniük, a projekt eszközszámlának pontosan nullának kell lennie, és a fennmaradó pénzt helyesen át kell utalni vagy vissza kell juttatni.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Zárja le az al-számlákat is, ha külön voltak nyitva.
