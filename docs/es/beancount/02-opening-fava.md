---
lang: es
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Apertura Fava
description: Cómo iniciar y abrir la interfaz local de contabilidad Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:01+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:01+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Abrir Fava

Fava es la interfaz web que se utiliza para inspeccionar la contabilidad. Se ejecuta localmente en el ordenador y se abre en un navegador o en la vista web de Obsidian.

## Requisitos

El ordenador debe tener instalados y disponibles los siguientes programas:

- Python
- Beancount
- Fava
- `fava-dashboards` si la extensión de panel de control debe ser visible
- Obsidian, si se utilizan los botones de Obsidian

## Abrir desde Obsidian

La nota `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` contiene botones para abrir la contabilidad. Los botones inician Fava a través de los Comandos de Shell de Obsidian y luego abren la URL local de Fava.

| Botón | Abre |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava en el puerto `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava en el puerto `4999` |

No cierres la ventana de terminal que inicia Fava. Si se cierra la terminal, Fava se detiene.

## Abrir manualmente

### NICA e.V.

Abre una terminal en:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Ejecuta:

```powershell
fava nica.beancount --port 4998
```

Luego abre `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Abre una terminal en:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Ejecuta:

```powershell
fava 2023.beancount --port 4999
```

Luego abre `http://127.0.0.1:4999/`.

## Archivos por lotes de inicio

| Archivo | Propósito |
| --- | --- |
| `startup-nica.bat` | Inicia NICA Fava en el puerto `4998`. |
| `startup-tohu.bat` | Inicia Tohuwabohu Fava en el puerto `4999`. |
| `startup-all.bat` | Inicia Obsidian, varias herramientas y ambas instancias de Fava. |

## URLs importantes

| Vista | NICA | Tohuwabohu |
| --- | --- | --- |
| Inicio | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Paneles de control | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Cuenta de resultados | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Cuando Fava ya está en ejecución

Si Fava ya se está ejecutando, basta con abrir la URL. Si el puerto ya está ocupado y Fava se niega a iniciarse, es posible que otra instancia de Fava ya esté abierta. Utiliza la página del navegador existente o cierra la ventana de terminal anterior y vuelve a empezar.
