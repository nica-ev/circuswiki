---
lang: es
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Cuentas y Categorías
description: Explica la estructura de cuentas y las convenciones de categorías alemanas utilizadas en los libros de contabilidad.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:55+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:55+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Cuentas y Categorías

Esta página explica la estructura de cuentas utilizada en los libros de contabilidad.

## Idioma de los nombres

Los nombres de las cuentas están en alemán. Siga utilizando los nombres de cuenta existentes para mantener la coherencia de los informes.

| Alemán | Significado en inglés |
| --- | --- |
| `Vermoegen` | Activos |
| `Verbindlichkeiten` | Pasivos |
| `Einnahmen` | Ingresos |
| `Ausgaben` | Gastos |
| `Buero` | Oficina |
| `Verein` | Asociación/actividad general de la asociación |
| `Projekt` | Proyecto |
| `Barkasse` | Caja chica |
| `Freies-Geld` | Fondos libres/sin restricciones |

## Cuentas de activos

Ejemplos de NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Ejemplos de Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Cuentas generales de ingresos

| Cuenta | Uso para |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Cuotas de membresía. |
| `Einnahmen:Spende` | Donaciones. |
| `Einnahmen:Verleih` | Ingresos por alquiler o préstamo. |
| `Einnahmen:Sonstiges` | Otros ingresos que no encajan en otra parte. |

## Cuentas generales de gastos

| Cuenta | Uso para |
| --- | --- |
| `Ausgaben:Buero:Miete` | Alquiler de oficina o local. |
| `Ausgaben:Buero:Internet` | Internet y servicios digitales. |
| `Ausgaben:Buero:Sonstiges` | Otros gastos de oficina. |
| `Ausgaben:Verein:Versicherung` | Seguro de la asociación. |
| `Ausgaben:Verein:Ehrenamt` | Dietas de voluntarios o costes de voluntarios de la asociación. |
| `Ausgaben:Essen` | Gastos de comida fuera de un proyecto específico. |
| `Ausgaben:Sonstiges` | Recurso temporal para gastos no especificados. |

`Ausgaben:Sonstiges` y `Einnahmen:Sonstiges` son útiles durante la importación, pero no deben convertirse en la categoría final si existe una categoría más precisa.

## Cuentas de proyectos

Las cuentas de proyectos siguen este patrón:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Ejemplos:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Subcategorías típicas de proyectos

| Subcategoría | Significado |
| --- | --- |
| `Honorar` | Honorarios pagados a personas o recibidos por trabajo. |
| `Aufwand` | Gasto o asignación de gastos. |
| `Sachmittel` | Materiales y suministros. |
| `Sonstiges` | Otros costes o ingresos del proyecto. |
| `Pauschale` / `Pauschalen` | Presupuesto de proyecto a tanto alzado o tarifa fija. |

## Pasivos con personas

Las cuentas de pasivos rastrean el dinero adeudado a personas o devuelto a personas. Los ejemplos incluyen `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` y `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Elección de la cuenta correcta

1. ¿Es a nivel de asociación o a nivel de proyecto?
2. Si es a nivel de proyecto, ¿qué proyecto es el propietario del dinero?
3. ¿Se trata de ingresos, gastos, movimiento de activos o reembolso de pasivos?
4. ¿Ya existe una categoría precisa?
5. Si no hay una categoría adecuada, utilice `Sonstiges` temporalmente y añada un comentario.
