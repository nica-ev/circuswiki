---
lang: en
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Opening Fava
description: How to start and open the local Fava bookkeeping interface.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 02 - Opening Fava

Fava is the web interface used to inspect the bookkeeping. It runs locally on the computer and is opened in a browser or Obsidian web view.

## Requirements

The computer must have these programs installed and available:

- Python
- Beancount
- Fava
- `fava-dashboards` if the dashboard extension should be visible
- Obsidian, if using the Obsidian buttons

## Opening from Obsidian

The note `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` contains buttons for opening bookkeeping. The buttons start Fava through Obsidian Shell Commands and then open the local Fava URL.

| Button | Opens |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava on port `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava on port `4999` |

Do not close the terminal window that starts Fava. If the terminal is closed, Fava stops.

## Opening manually

### NICA e.V.

Open a terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Run:

```powershell
fava nica.beancount --port 4998
```

Then open `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Open a terminal in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Run:

```powershell
fava 2023.beancount --port 4999
```

Then open `http://127.0.0.1:4999/`.

## Startup batch files

| File | Purpose |
| --- | --- |
| `startup-nica.bat` | Starts NICA Fava on port `4998`. |
| `startup-tohu.bat` | Starts Tohuwabohu Fava on port `4999`. |
| `startup-all.bat` | Starts Obsidian, several tools, and both Fava instances. |

## Important URLs

| View | NICA | Tohuwabohu |
| --- | --- | --- |
| Home | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Income Statement | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## When Fava is already running

If Fava is already running, opening the URL is enough. If the port is already occupied and Fava refuses to start, another Fava instance may already be open. Use the existing browser page or close the old terminal window and start again.
