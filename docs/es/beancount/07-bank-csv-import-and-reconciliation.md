---
lang: es
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Importación y Conciliación de CSV Bancario
description: Flujo de trabajo para importar datos CSV de Sparkasse y conciliar saldos bancarios.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:31+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:31+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Importación y conciliación de CSV bancario

Este flujo de trabajo introduce las nuevas transacciones de Sparkasse en Beancount y confirma que el libro mayor sigue coincidiendo con la cuenta bancaria real.

## Dónde se realizan las importaciones

| Asociación | Carpeta de importación | Script | Archivo de salida |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Antes de exportar desde Sparkasse

1. Abre el archivo del libro mayor correcto.
2. Busca la sección `Balance Checks` (Comprobaciones de saldo).
3. Busca la fecha del último saldo de la cuenta Sparkasse.
4. Comprueba también la sección `Bank Dump` (Volcado bancario) en la parte inferior para ver la última fecha de importación.
5. Utiliza la más reciente de esas fechas como punto de partida.

Esto evita perder transacciones o importar el mismo período dos veces.

## Exportación desde Sparkasse

1. Abre la vista general de la cuenta.
2. Filtra por rango de fechas.
3. Empieza desde la última fecha comprobada o importada.
4. Termina con hoy o la fecha de conciliación deseada.
5. Exporta como `Excel (CSV-CAMT V2)`.
6. Copia el CSV descargado en la carpeta `test` correcta.

Los scripts esperan el formato CSV-CAMT-V2 de Sparkasse con columnas separadas por punto y coma.

## Conversión del CSV

Abre una terminal en la carpeta `test` correcta y ejecuta:

```powershell
python csv2bean.py "NOMBRE-DEL-ARCHIVO-DESCARGADO.CSV"
```

Ejemplo:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Si funciona, el script imprime `Process finished.` (Proceso finalizado) y crea o sobrescribe `beancount_file.beancount`.

## Qué hace el conversor

El conversor crea entradas básicas de Beancount:

- Los importes entrantes van a la cuenta de activo de Sparkasse y a `Einnahmen:Sonstiges` (Ingresos: Varios) por defecto.
- Los importes salientes van a `Ausgaben:Sonstiges` (Gastos: Varios) y a la cuenta de activo de Sparkasse por defecto.
- Algunas descripciones de ingresos se clasifican automáticamente como `Einnahmen:Vereinsbeitrag` (Ingresos: Cuota de asociación).
- Algunos textos relacionados con Tohuwabohu pueden clasificarse como una cuenta de ingresos de proyecto.

El conversor es solo un primer paso. No conoce el significado contable final de cada transacción.

## Copiar al libro mayor principal

1. Abre `test/beancount_file.beancount`.
2. Ignora la cabecera de opciones generada.
3. Copia solo las transacciones.
4. Pégalas primero en el libro mayor principal, bajo `Bank Dump` (Volcado bancario).
5. Añade un separador con fecha para la fecha de importación si es necesario.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

El `Bank Dump` es un área de preparación. Las transacciones importadas pueden moverse más tarde a la sección temática o de proyecto correcta.

## Clasificación de las entradas importadas

Para cada transacción importada, decide:

- ¿Es a nivel de asociación o de proyecto?
- ¿Es un ingreso o un gasto?
- ¿Es un reembolso o un pago de deuda?
- ¿Pertenece a `Freies-Geld` (Dinero libre) o a una cuenta de activo específica del proyecto?
- ¿Hay un recibo o factura que adjuntar?

Reemplaza las cuentas genéricas de respaldo como `Ausgaben:Sonstiges` cuando exista una cuenta más precisa.

## Añadir una comprobación de saldo

Ejemplo NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Ejemplo Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Utiliza el saldo que muestra Sparkasse para esa fecha exacta.

## Validación en Fava

1. Guarda el archivo del libro mayor.
2. Recarga Fava.
3. Comprueba si hay errores en la parte superior de la página de Fava.
4. Abre la página de la cuenta de Sparkasse.
5. Confirma el saldo acumulado y las últimas transacciones.
6. Revisa el Balance General.
7. Revisa los paneles de proyectos si se vieron afectadas cuentas de proyecto.

## Si la comprobación de saldo falla

Causas comunes:

- La exportación CSV omitió un día al principio o al final.
- Se importó una transacción dos veces.
- Se pegó una transacción en el libro mayor de la asociación incorrecta.
- Se editó incorrectamente un número.
- Una división de proyecto utilizó el signo incorrecto.
- No se registraron movimientos de PayPal o en efectivo.

No elimines la comprobación de saldo solo para que desaparezca el error. Corrige la diferencia de transacción subyacente.
