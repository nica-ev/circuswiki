---
lang: nl
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Openen
description: Hoe de lokale Fava boekhoudinterface te starten en te openen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:06+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:06+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Fava openen

Fava is de webinterface die wordt gebruikt om de boekhouding te inspecteren. Het draait lokaal op de computer en wordt geopend in een browser of Obsidian webview.

## Vereisten

De computer moet de volgende programma's geïnstalleerd en beschikbaar hebben:

- Python
- Beancount
- Fava
- `fava-dashboards` als de dashboard-extensie zichtbaar moet zijn
- Obsidian, indien gebruik wordt gemaakt van de Obsidian-knoppen

## Openen vanuit Obsidian

De notitie `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` bevat knoppen om de boekhouding te openen. De knoppen starten Fava via Obsidian Shell Commands en openen vervolgens de lokale Fava URL.

| Knop | Opent |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava op poort `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava op poort `4999` |

Sluit het terminalvenster dat Fava start niet af. Als de terminal wordt gesloten, stopt Fava.

## Handmatig openen

### NICA e.V.

Open een terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Voer uit:

```powershell
fava nica.beancount --port 4998
```

Open vervolgens `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Open een terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Voer uit:

```powershell
fava 2023.beancount --port 4999
```

Open vervolgens `http://127.0.0.1:4999/`.

## Opstart batchbestanden

| Bestand | Doel |
| --- | --- |
| `startup-nica.bat` | Start NICA Fava op poort `4998`. |
| `startup-tohu.bat` | Start Tohuwabohu Fava op poort `4999`. |
| `startup-all.bat` | Start Obsidian, diverse tools en beide Fava-instanties. |

## Belangrijke URL's

| Weergave | NICA | Tohuwabohu |
| --- | --- | --- |
| Home | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Resultatenrekening | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Als Fava al draait

Als Fava al draait, is het openen van de URL voldoende. Als de poort al bezet is en Fava weigert te starten, is er mogelijk al een andere Fava-instantie geopend. Gebruik de bestaande browservenster of sluit het oude terminalvenster en start opnieuw.
