---
lang: es
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Paneles e Informes de Fava
description: Descripción general de los informes de Fava y los paneles personalizados utilizados para la revisión de la contabilidad.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:25+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:25+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Paneles y Reportes de Fava

Fava proporciona reportes contables estándar. El sistema también utiliza `fava-dashboards` para páginas de resumen personalizadas.

## Vistas estándar de Fava

| Vista | Uso |
| --- | --- |
| Balance General | Para verificar activos, pasivos, fondos disponibles, saldos de PayPal, efectivo y proyectos. |
| Estado de Resultados | Para ver ingresos y gastos a lo largo del tiempo. |
| Página de Cuenta | Para inspeccionar todas las transacciones de una cuenta específica. |
| Diario | Para buscar el historial cronológico de transacciones. |
| Consulta | Para ejecutar consultas personalizadas de Beancount cuando sea necesario. |
| Documentos | Para encontrar recibos y archivos vinculados. |

## Extensión de Panel

Los ledgers incluyen esta directiva:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Esto activa la extensión de panel si `fava-dashboards` está instalado.

## Archivos de configuración de paneles

Los archivos de panel se nombran `dashboards.yaml`. Se almacenan cerca de los archivos del ledger y a nivel de contabilidad compartido.

## Secciones principales del panel

| Panel | Propósito |
| --- | --- |
| `Vorstand-Cockpit` | Resumen de gestión: dinero disponible, saldo total de Sparkasse, PayPal, efectivo, tendencia de liquidez, resultado mensual, saldos de proyectos activos. |
| `Details & Daten` | Gráficos detallados: gastos por categoría, ingresos por categoría, flujo de dinero, red de proyectos/personas. |

## Indicadores importantes del panel

### Freies Geld (Dinero Disponible)

Muestra el dinero disponible fuera de los fondos restringidos de proyectos. Las cuentas típicas son `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` y `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Total Sparkasse)

Muestra el saldo total de Sparkasse entre la cuenta bancaria principal y las subcuentas internas.

### PayPal

Muestra el saldo de PayPal. Un saldo negativo de PayPal indica que algo debe ser revisado.

### Barkasse (Caja de Efectivo)

Muestra el saldo de la caja de efectivo.

### Saldo Aktiver Projekte (Saldo de Proyectos Activos)

Muestra los saldos de proyectos distintos de cero. Esto es útil para ver qué proyectos aún tienen dinero o están sobregirados.

### Monatlicher Ueberschuss / Fehlbetrag (Superávit / Déficit Mensual)

Muestra el superávit u déficit operativo mensual, excluyendo las cuentas de proyectos en la consulta del panel.

## Cómo usar los paneles de forma responsable

Los paneles son resúmenes. Si un número parece sorprendente:

1. Haz clic en la cuenta o reporte de Fava vinculado.
2. Inspecciona las transacciones subyacentes.
3. Verifica si una transacción todavía está en `Sonstiges` (Otros) o `Bank Dump` (Volcado Bancario).
4. Comprueba si el nombre de la cuenta coincide con el patrón de consulta del panel.
5. Confirma las verificaciones de saldo antes de confiar en los números de gestión.

## Cuando los números del panel parecen incorrectos

Causas comunes:

- Una transacción se registró en la cuenta bancaria principal en lugar de la subcuenta del proyecto.
- Se cerró una cuenta de proyecto pero todavía tiene un saldo distinto de cero.
- Un nuevo proyecto utiliza un patrón de nomenclatura no incluido en la consulta del panel.
- Una transacción todavía está en una categoría general de reserva.
- El archivo del panel pertenece a un ledger diferente al que se está abriendo actualmente.
