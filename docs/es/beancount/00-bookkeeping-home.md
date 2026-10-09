---
lang: es
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Documentación del Sistema de Contabilidad
description: Visión general y punto de partida para la documentación de contabilidad Beancount de NICA e.V. y Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:43+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:43+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Documentación del Sistema de Contabilidad

Esta documentación explica cómo funciona el sistema de contabilidad para NICA e.V. y Tohuwabohu Halle e.V. desde la perspectiva de un usuario normal.

El sistema utiliza archivos de contabilidad en texto plano en Beancount y una interfaz de navegador llamada Fava. No necesitas entender de programación para usarlo, pero sí debes seguir cuidadosamente el flujo de trabajo de contabilidad: importar datos bancarios, clasificar transacciones, adjuntar recibos cuando sea necesario y verificar saldos.

## Empieza aquí

- [01 - Descripción general del sistema](01-system-overview.md)
- [02 - Abrir Fava](02-opening-fava.md)
- [03 - Mapa de carpetas y archivos](03-folder-and-file-map.md)
- [04 - Fundamentos de Beancount para usuarios](04-beancount-basics-for-users.md)
- [05 - Cuentas y categorías](05-accounts-and-categories.md)
- [06 - Ingresar y editar transacciones](06-entering-and-editing-transactions.md)
- [07 - Importación y conciliación de CSV bancarios](07-bank-csv-import-and-reconciliation.md)
- [08 - Proyectos y fondos restringidos](08-projects-and-restricted-funds.md)
- [09 - Recibos y documentos](09-receipts-and-documents.md)
- [10 - Paneles e informes de Fava](10-fava-dashboards-and-reports.md)
- [11 - Rutina de contabilidad regular](11-regular-bookkeeping-routine.md)
- [12 - Solución de problemas](12-troubleshooting.md)
- [13 - Glosario](13-glossary.md)

## La regla más importante

El archivo de contabilidad es la fuente de la verdad. Fava solo muestra lo que está escrito en los archivos `.beancount`. Si algo parece incorrecto en Fava, corrige la entrada de Beancount y recarga Fava.

## Libros mayores actuales

| Organización | Archivo principal | Dirección de Fava | Puerto |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Lo que esta documentación no es

Esto no es asesoramiento legal ni fiscal. Describe cómo está organizado este sistema de contabilidad local específico y cómo los usuarios deben trabajar con él de manera coherente.
