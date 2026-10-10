---
lang: es
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Glosario
description: Definiciones de términos de contabilidad, Beancount, Fava y contabilidad de proyectos utilizados en esta documentación.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:12+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:12+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 - Glosario

## Cuenta

Un lugar con nombre donde Beancount registra dinero o valor. Ejemplo: `Ausgaben:Buero:Miete`.

## Activo

Algo que la asociación posee o controla, como dinero en el banco, saldo de PayPal, efectivo o inventario. En este sistema, los activos están bajo `Vermoegen`.

## Comprobación de saldo

Una línea que confirma que una cuenta tiene un saldo específico en una fecha específica. Las comprobaciones de saldo se utilizan para verificar que el libro mayor coincide con los registros bancarios, de PayPal o en efectivo.

## Volcado bancario

Una sección provisional cerca de la parte inferior del libro mayor donde se pegan por primera vez las transacciones bancarias importadas antes de que se clasifiquen por completo.

## Beancount

El formato de contabilidad en texto plano que se utiliza como fuente de verdad del sistema.

## CSV

Un archivo de exportación similar a una hoja de cálculo. Sparkasse exporta archivos CSV que se convierten en transacciones de Beancount.

## Patrimonio neto

Familia de cuentas de Beancount utilizada para saldos de apertura y puntos de partida históricos de equilibrio.

## Fava

La interfaz del navegador para ver y trabajar con libros mayores de Beancount.

## Paneles de Fava

Una extensión que añade páginas de panel personalizadas a Fava.

## Freies-Geld

Dinero libre o sin restricciones que no se asigna a un presupuesto de proyecto restringido.

## Ingresos

Dinero recibido. En este sistema, las cuentas de ingresos comienzan con `Einnahmen`.

## Libro mayor

El archivo de contabilidad que contiene cuentas, transacciones, comprobaciones de saldo y documentos. Los libros mayores principales son `nica.beancount` y `2023.beancount`.

## Pasivo

Dinero adeudado a otra persona. En este sistema, los pasivos están bajo `Verbindlichkeiten`.

## Beneficiario

La persona u organización nombrada en una transacción.

## Cuenta de proyecto

Una cuenta utilizada para rastrear dinero para un proyecto específico por separado del dinero general de la asociación.

## Conciliación

El proceso de comprobar que Beancount y el saldo real del banco o de PayPal coinciden.

## Recibo

Un documento que prueba un gasto, como una factura, un contrato o un recibo de efectivo.

## Sonstiges

Alemán para misceláneo u otro. Útil como solución provisional temporal, pero las categorías específicas son mejores para la contabilidad final.

## Transacción

Una entrada contable fechada que describe un evento financiero.

## Verwendungsnachweis

Un informe del financiador del proyecto que explica cómo se utilizó el dinero concedido.
