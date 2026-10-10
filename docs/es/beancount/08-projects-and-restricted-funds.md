---
lang: es
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Proyectos y Fondos Restringidos
description: Explica cómo se representan y verifican el dinero de proyectos y los fondos restringidos.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:14+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:14+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Proyectos y Fondos Restringidos

Los proyectos son fundamentales en este sistema de contabilidad. Muchas subvenciones y actividades deben registrarse por separado del dinero de libre disposición.

## Qué significa un proyecto en el libro mayor

| Tipo de cuenta | Ejemplo | Propósito |
| --- | --- | --- |
| Activo de proyecto | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Saldo interno del dinero del proyecto. |
| Ingresos de proyecto | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Financiación del proyecto o ingresos del proyecto. |
| Gasto de proyecto | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Gasto del proyecto. |

La cuenta bancaria real puede ser una única cuenta de Sparkasse, pero el libro mayor separa los saldos internos de los proyectos para que el equipo pueda ver a qué pertenece cada proyecto.

## Proyectos activos y cerrados

Los proyectos activos tienen cuentas abiertas y saldos relevantes. Los proyectos cerrados suelen tener una comprobación final del saldo de `0.00 EUR` y directivas de `close` para las cuentas de activo, ingresos y gastos del proyecto.

No registres nuevas transacciones en proyectos cerrados a menos que reabras o corrijas intencionadamente datos históricos.

## Ejemplos actuales en NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- proyectos cerrados de 2024 como `24-AWO`, `24-HONY`, `24-Peter`

## Ejemplos actuales en Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- proyectos cerrados como `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Creación de un nuevo proyecto

Normalmente, un nuevo proyecto necesita que se abran las cuentas antes de introducir las transacciones.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Solo abre las categorías que sean realmente útiles para el proyecto.

## Registro de la financiación del proyecto

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Registro de los gastos del proyecto

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Comprensión de los saldos de los proyectos

Un saldo de activo de proyecto positivo significa que todavía hay dinero asignado a ese proyecto. Un saldo de activo de proyecto cero significa que el proyecto no tiene saldo bancario interno restante. Un saldo de activo de proyecto negativo suele significar que el proyecto ha gastado más de los fondos asignados o que falta una asignación.

## Cierre de un proyecto

Antes de cerrar un proyecto, se deben registrar todos los ingresos y gastos, los recibos deben ser localizables, la cuenta de activo del proyecto debe ser exactamente cero y cualquier dinero restante debe ser transferido o devuelto correctamente.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Cierra también las subcuentas si se abrieron por separado.
