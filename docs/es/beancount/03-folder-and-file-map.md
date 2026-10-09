---
lang: es
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mapa de Carpetas y Archivos
description: Mapea las carpetas importantes de contabilidad, archivos de libros mayores, paneles y archivos de ayuda.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:15+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:15+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mapa de Carpetas y Archivos

Esta página explica dónde se almacenan los archivos importantes de contabilidad.

## Carpeta principal de contabilidad

```text
1. Vereinsverwaltung/Buchhaltung
```

Esta carpeta contiene los libros mayores, los archivos del panel de control, los documentos de respaldo y las carpetas auxiliares.

## Archivos importantes de nivel superior

| Archivo | Propósito |
| --- | --- |
| `Buchhaltung Home.md` | Página de entrada de Obsidian con botones y una breve nota de flujo de trabajo. |
| `all.beancount` | Libro mayor combinado experimental que incluye tanto NICA como Tohuwabohu. |
| `dashboards.yaml` | Definición del panel de control para los paneles de control de Fava a nivel compartido. |

## Estructura de NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Ruta | Propósito |
| --- | --- |
| `2023/nica.beancount` | Libro mayor principal de NICA. Este es el archivo que se edita normalmente. |
| `2023/dashboards.yaml` | Configuración del panel de control para el libro mayor de NICA. |
| `2023/Buchhaltung NICA eV.md` | Nota auxiliar de Obsidian para abrir la contabilidad de NICA. |
| `2023/CSV/` | Exportaciones de CSV almacenadas. |
| `test/csv2bean.py` | Convierte CSV de Sparkasse a entradas temporales de Beancount. |
| `test/beancount_file.beancount` | Salida generada de la conversión de CSV. |
| `test/paypal2bean.py` | Ayuda para importaciones de CSV de PayPal. |
| `test/output_file_paypal.beancount` | Archivo de salida de PayPal generado. |
| `test/old files/` | CSV más antiguos y archivos generados. |

## Estructura de Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Ruta | Propósito |
| --- | --- |
| `2023/2023.beancount` | Libro mayor principal de Tohuwabohu. Este es el archivo que se edita normalmente. |
| `2021/2021.beancount` | Datos de libros mayores antiguos incluidos a través de `all.beancount`. |
| `all.beancount` | Archivo combinado de Tohuwabohu que incluye los archivos de los libros mayores de 2021 y 2023. |
| `2023/dashboards.yaml` | Configuración del panel de control para el libro mayor de Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Nota auxiliar de Obsidian. |
| `2023/Belege Ausgaben/` | Recibos y documentos de respaldo de los gastos. |
| `2023/Belege Ausgaben/Eingetragen/` | Recibos ya registrados en el libro mayor. |
| `test/csv2bean.py` | Convierte CSV de Sparkasse a entradas temporales de Beancount. |
| `test/beancount_file.beancount` | Salida generada de la conversión de CSV. |
| `test/paypal2bean.py` | Ayuda para importaciones de CSV de PayPal. |
| `test/output_file_paypal.beancount` | Archivo de salida de PayPal generado. |
| `test/CSV - old files/` | CSV más antiguos y archivos generados. |

## Principio de nomenclatura de archivos

Las carpetas todavía contienen nombres históricos como `2023`, incluso cuando también contienen actividad posterior de 2024, 2025 y 2026. Trate los archivos de libro mayor principales a los que se hace referencia actualmente como los libros mayores activos a menos que la estructura se cambie intencionalmente.

## Dónde editar

| Asociación | Edita este archivo |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

No edite los archivos de salida generados como registro permanente. Son archivos temporales de preparación.
