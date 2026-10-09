---
lang: hu
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava megnyitása
description: Hogyan indítsuk el és nyissuk meg a helyi Fava könyvelő felületet.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:33:24+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:33:24+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Fava megnyitása

A Fava az a webes felület, amelyet a könyvelés megtekintésére használunk. Helyileg fut a számítógépen, és böngészőben vagy az Obsidian webes nézetében nyílik meg.

## Követelmények

A számítógépen telepítve és elérhetőnek kell lennie a következő programoknak:

- Python
- Beancount
- Fava
- `fava-dashboards`, ha a műszerfal kiterjesztés látható legyen
- Obsidian, ha az Obsidian gombokat használjuk

## Megnyitás Obsidianból

Az `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` jegyzet tartalmaz gombokat a könyvelés megnyitásához. A gombok az Obsidian Shell Commands segítségével indítják el a Favát, majd megnyitják a helyi Fava URL-t.

| Gomb | Nyit meg |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava a `4998`-as porton |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava a `4999`-es porton |

Ne zárja be a Fava-t elindító terminálablakot. Ha a terminál bezárul, a Fava leáll.

## Manuális megnyitás

### NICA e.V.

Nyisson egy terminált itt:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Futtassa a következő parancsot:

```powershell
fava nica.beancount --port 4998
```

Ezután nyissa meg a `http://127.0.0.1:4998/` címet.

### Tohuwabohu Halle e.V.

Nyisson egy terminált itt:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Futtassa a következő parancsot:

```powershell
fava 2023.beancount --port 4999
```

Ezután nyissa meg a `http://127.0.0.1:4999/` címet.

## Indító batch fájlok

| Fájl | Cél |
| --- | --- |
| `startup-nica.bat` | Elindítja a NICA Fava-t a `4998`-as porton. |
| `startup-tohu.bat` | Elindítja a Tohuwabohu Fava-t a `4999`-es porton. |
| `startup-all.bat` | Elindítja az Obsidian-t, több eszközt és mindkét Fava példányt. |

## Fontos URL-ek

| Nézet | NICA | Tohuwabohu |
| --- | --- | --- |
| Kezdőlap | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Műszerfalak | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Eredménykimutatás | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Ha a Fava már fut

Ha a Fava már fut, elegendő az URL megnyitása. Ha a port már foglalt, és a Fava nem indul el, akkor lehetséges, hogy egy másik Fava példány már nyitva van. Használja a meglévő böngészőoldalt, vagy zárja be a régi terminálablakot, és indítsa újra.
