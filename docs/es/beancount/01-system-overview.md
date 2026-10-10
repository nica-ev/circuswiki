---
lang: es
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Resumen del Sistema
description: Explica el propósito, los componentes y el flujo de trabajo normal del usuario del sistema de contabilidad.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:03:53+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:03:53+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Resumen del Sistema

## Propósito

El sistema de contabilidad registra toda la actividad financiera de las asociaciones de una manera estructurada y verificable. Está diseñado para responder a las preguntas contables habituales:

- ¿Cuánto dinero está disponible actualmente?
- ¿Qué ingresos y gastos pertenecen a la propia asociación?
- ¿Qué ingresos y gastos pertenecen a un proyecto específico?
- ¿Son correctos los saldos de Sparkasse, PayPal y efectivo?
- ¿Qué recibos y documentos pertenecen a qué transacciones?
- ¿Qué proyectos están activos, terminados o ya cerrados?

## Componentes principales

| Componente | Qué hace |
| --- | --- |
| Beancount | El formato de datos contables. Las transacciones se escriben en archivos de texto plano. |
| Fava | La interfaz del navegador para ver y filtrar los datos de Beancount. |
| Fava Dashboards | Páginas de panel personalizadas dentro de Fava para una visión general de la gestión y vistas de proyectos. |
| Obsidian | El sistema de notas desde el cual se puede abrir la contabilidad a través de botones. |
| Scripts de importación CSV | Scripts auxiliares que convierten las exportaciones CSV de Sparkasse en entradas de Beancount. |

## Cómo encajan las partes

1. Los datos bancarios o de PayPal se exportan como CSV.
2. El CSV se convierte en entradas temporales de Beancount.
3. Las nuevas entradas se copian al archivo de libro mayor correcto.
4. El usuario revisa, clasifica y corrige las entradas.
5. Las comprobaciones de saldo confirman que el libro mayor coincide con el saldo bancario o de PayPal.
6. Fava muestra informes, páginas de cuentas, estados de resultados, balances y paneles de control.

## Dos asociaciones separadas

| Asociación | Libro Mayor | Prefijo de cuenta típico |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

También existe un archivo combinado experimental: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. El trabajo diario normal debe realizarse en el libro mayor individual de la asociación correspondiente.

## Flujo de trabajo básico

1. Abrir la instancia de Fava correcta.
2. Buscar la última comprobación de saldo completada.
3. Exportar las nuevas transacciones bancarias de Sparkasse a partir de la última fecha comprobada.
4. Convertir el CSV al formato Beancount.
5. Pegar las entradas generadas primero en la sección `Bank Dump`.
6. Mover o clasificar las entradas en las secciones de asociación o proyecto correctas.
7. Añadir recibos, enlaces, comentarios o etiquetas cuando sea necesario.
8. Añadir una nueva comprobación de saldo.
9. Recargar Fava y verificar que no haya errores.

## Qué debe aprender primero un nuevo usuario

1. [Abrir Fava](02-opening-fava.md)
2. [Conceptos básicos de Beancount para usuarios](04-beancount-basics-for-users.md)
3. [Importación y conciliación de CSV bancarios](07-bank-csv-import-and-reconciliation.md)
4. [Cuentas y categorías](05-accounts-and-categories.md)
5. [Proyectos y fondos restringidos](08-projects-and-restricted-funds.md)
