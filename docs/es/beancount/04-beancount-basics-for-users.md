---
lang: es
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Conceptos básicos de Beancount para usuarios
description: Introduce el formato de texto de Beancount y los patrones de transacciones utilizados en los libros de contabilidad.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:36:11+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:36:11+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Fundamentos de Beancount para Usuarios

Beancount almacena la contabilidad como texto legible. Cada transacción indica qué sucedió, en qué fecha, quién estuvo involucrado y qué cuentas cambiaron.

## Estructura básica de una transacción

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Parte | Significado |
| --- | --- |
| `2026-01-13` | Fecha de la transacción. |
| `!` | Marcador de estado. En este sistema se usa comúnmente para entradas importadas o que aún no han sido revisadas definitivamente. |
| Primera cita | Beneficiario o remitente. |
| Segunda cita | Descripción o texto de la operación bancaria. |
| Primera línea de cuenta | De dónde provino o a dónde fue el dinero. |
| Segunda línea de cuenta | La categoría opuesta. Si no se escribe importe, Beancount lo calcula automáticamente. |

## Nombres de cuentas

Los nombres de las cuentas están separados por dos puntos:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Léelo de izquierda a derecha: activo, cuenta bancaria, Sparkasse NICA, fondos disponibles libremente.

## Las cinco familias de cuentas

| Familia | Significado | Ejemplo |
| --- | --- | --- |
| `Vermoegen` | Activos: banco, PayPal, efectivo, inventario. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Pasivos: dinero adeudado a personas u otros. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Saldos iniciales y asientos de regularización. | `Equity:Opening-Balances` |
| `Einnahmen` | Ingresos. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Gastos. | `Ausgaben:Buero:Miete` |

## Signos de ingresos y gastos

En los informes de Beancount, los ingresos a menudo aparecen internamente con un signo negativo y los gastos con un signo positivo. Fava y los paneles de control a menudo presentan estos valores de una manera más amigable para el usuario. No modifiques las transacciones solo porque un número de ingresos parezca negativo en una consulta bruta.

## Verificaciones de saldo

Una verificación de saldo indica que una cuenta debe tener un saldo específico en una fecha determinada:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Si Beancount no puede igualar ese saldo con las transacciones anteriores a esa fecha, Fava mostrará un error. Las verificaciones de saldo son el principal mecanismo de control de calidad.

## Abrir y cerrar cuentas

Antes de que se utilice una cuenta, se abre:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Cuando un proyecto finaliza y la cuenta del proyecto está a cero, se puede cerrar:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Normalmente, las cuentas cerradas no deberían recibir nuevas transacciones.

## Comentarios y documentos

Las líneas que comienzan con `;` son comentarios. Explican decisiones o situaciones inciertas y no afectan a los números.

Los recibos se pueden vincular con líneas `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
