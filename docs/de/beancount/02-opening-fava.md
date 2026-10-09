---
lang: de
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Eröffnung
description: Wie man die lokale Fava Buchhaltungsoberfläche startet und öffnet.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:33:12+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:33:12+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Fava öffnen

Fava ist die Web-Oberfläche zur Einsicht in die Buchhaltung. Sie läuft lokal auf dem Computer und wird im Browser oder in der Obsidian-Webansicht geöffnet.

## Voraussetzungen

Auf dem Computer müssen folgende Programme installiert und verfügbar sein:

- Python
- Beancount
- Fava
- `fava-dashboards`, falls die Dashboard-Erweiterung sichtbar sein soll
- Obsidian, falls die Obsidian-Buttons verwendet werden

## Öffnen aus Obsidian

Die Notiz `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` enthält Buttons zum Öffnen der Buchhaltung. Die Buttons starten Fava über Obsidian Shell Commands und öffnen dann die lokale Fava-URL.

| Button | Öffnet |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava auf Port `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava auf Port `4999` |

Schließe das Terminalfenster, das Fava startet, nicht. Wenn das Terminal geschlossen wird, stoppt Fava.

## Manuelles Öffnen

### NICA e.V.

Öffne ein Terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Führe aus:

```powershell
fava nica.beancount --port 4998
```

Öffne dann `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Öffne ein Terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Führe aus:

```powershell
fava 2023.beancount --port 4999
```

Öffne dann `http://127.0.0.1:4999/`.

## Start-Batchdateien

| Datei | Zweck |
| --- | --- |
| `startup-nica.bat` | Startet NICA Fava auf Port `4998`. |
| `startup-tohu.bat` | Startet Tohuwabohu Fava auf Port `4999`. |
| `startup-all.bat` | Startet Obsidian, diverse Tools und beide Fava-Instanzen. |

## Wichtige URLs

| Ansicht | NICA | Tohuwabohu |
| --- | --- | --- |
| Home | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Gewinn- und Verlustrechnung | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Wenn Fava bereits läuft

Wenn Fava bereits läuft, genügt das Öffnen der URL. Wenn der Port bereits belegt ist und Fava sich nicht starten lässt, ist möglicherweise bereits eine andere Fava-Instanz geöffnet. Nutze die bestehende Browserseite oder schließe das alte Terminalfenster und starte neu.
