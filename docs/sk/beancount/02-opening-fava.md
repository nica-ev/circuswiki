---
lang: sk
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Otvorenie Fava
description: Ako spustiť a otvoriť lokálne rozhranie účtovníctva Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:15+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:15+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Spustenie Favya

Fava je webové rozhranie používané na kontrolu účtovníctva. Beží lokálne na počítači a otvára sa v prehliadači alebo v prehliadači Obsidian.

## Požiadavky

Na počítači musia byť nainštalované a dostupné tieto programy:

- Python
- Beancount
- Fava
- `fava-dashboards`, ak má byť rozšírenie dashboardu viditeľné
- Obsidian, ak používate tlačidlá Obsidian

## Otvorenie z Obsidianu

Poznámka `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` obsahuje tlačidlá na otvorenie účtovníctva. Tlačidlá spúšťajú Fava cez Obsidian Shell Commands a následne otvárajú lokálnu URL Favya.

| Tlačidlo | Otvorí |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava na porte `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava na porte `4999` |

Nezatvárajte okno terminálu, ktoré spúšťa Fava. Ak terminál zatvoríte, Fava sa zastaví.

## Manuálne otvorenie

### NICA e.V.

Otvorte terminál v adresári:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Spustite príkaz:

```powershell
fava nica.beancount --port 4998
```

Potom otvorte `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Otvorte terminál v adresári:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Spustite príkaz:

```powershell
fava 2023.beancount --port 4999
```

Potom otvorte `http://127.0.0.1:4999/`.

## Dávkové súbory na spustenie

| Súbor | Účel |
| --- | --- |
| `startup-nica.bat` | Spustí NICA Fava na porte `4998`. |
| `startup-tohu.bat` | Spustí Tohuwabohu Fava na porte `4999`. |
| `startup-all.bat` | Spustí Obsidian, niekoľko nástrojov a obe inštancie Favya. |

## Dôležité URL adresy

| Zobrazenie | NICA | Tohuwabohu |
| --- | --- | --- |
| Domov | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Výkaz ziskov a strát | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Keď Fava už beží

Ak Fava už beží, stačí otvoriť URL. Ak je port už obsadený a Fava sa odmieta spustiť, je možné, že je už otvorená iná inštancia Favya. Použite existujúcu stránku v prehliadači alebo zatvorte staré okno terminálu a spustite znova.
