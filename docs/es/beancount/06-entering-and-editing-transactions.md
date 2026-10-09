---
lang: es
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Introducir y Editar Transacciones
description: Describe cómo los usuarios revisan, clasifican, corrigen e introducen transacciones contables.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:53:31+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:53:31+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Introducción y Edición de Transacciones

La mayoría de las entradas provienen de datos bancarios importados, pero los usuarios aún necesitan revisar, clasificar, corregir y, a veces, introducir transacciones manualmente.

## Estado de la transacción

Los libros contables suelen usar `!` en las transacciones importadas:

```beancount
2026-03-12 ! "Beneficiario" "Texto del banco"
```

Utiliza este como marcador normal a menos que el equipo decida una convención de estado más estricta.

## Entrada básica de ingresos

```beancount
2026-01-15 ! "Max Mustermann" "Cuota de socio 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Entrada básica de gastos

```beancount
2026-01-20 ! "Nombre del proveedor" "Factura 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Ingresos de proyectos

```beancount
2026-02-10 ! "Organismo financiador" "Pago de subvención proyecto 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Gastos de proyectos

```beancount
2026-02-15 ! "Nombre de la persona" "Honorarios proyecto 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Movimiento interno entre proyecto y fondos libres

A veces, una transacción debe asignar dinero bancario entre una cuenta de activo específica del proyecto y los fondos libres. La cuenta bancaria real es una cuenta física de Sparkasse, pero el libro contable rastrea los saldos internos del proyecto por separado.

```beancount
2026-02-20 ! "Asignación interna" "Mover fondos restantes del proyecto a dinero libre"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Solo realiza transferencias internas cuando entiendas por qué debe cambiar el saldo interno del proyecto.

## Reembolsos a personas

Si alguien pagó de forma privada y se le reembolsa más tarde, el patrón limpio suele ser registrar el gasto contra un pasivo y luego saldar el pasivo con el pago bancario.

```beancount
2026-03-01 ! "Tienda" "Material comprado por Marc"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Reembolso material"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Comentarios para decisiones poco claras

```beancount
; No está claro si esto pertenece a CEDU-25 o a los fondos de la asociación libre. Consultar factura.
2026-03-10 ! "Vendedor" "Factura 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Edición segura

Antes de editar, comprueba:

- Estás en el libro contable de la asociación correcta.
- No estás editando la salida generada de la importación como si fuera el libro contable final.
- La fecha de la transacción es correcta.
- El importe utiliza un punto como separador decimal, por ejemplo `12.50 EUR`.
- Los nombres de las cuentas están escritos exactamente como las cuentas existentes.
- Las transacciones de proyectos utilizan la cuenta de activo del proyecto y la categoría de ingresos/gastos del proyecto de forma coherente.

Después de editar, guarda el archivo, recarga Fava, comprueba si hay errores e inspecciona la página de la cuenta correspondiente.
