---
lang: es
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Solución de problemas
description: Problemas comunes de Fava y Beancount y cómo resolverlos.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:39+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:39+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Solución de problemas

## Fava no se abre

Comprueba:

- ¿Sigue abierta la ventana de la terminal?
- ¿Se inició Fava en la carpeta correcta?
- ¿Se está utilizando el puerto correcto?
- ¿Ya se está ejecutando otra instancia de Fava en el mismo puerto?
- ¿Está Fava instalado y disponible en la terminal?

Comandos:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Ejecuta cada comando solo desde la carpeta del libro mayor correcta.

## Fava muestra un error de Beancount

Causas comunes:

- Error tipográfico en el nombre de una cuenta.
- Directiva `open` de cuenta faltante.
- La cantidad utiliza una coma en lugar de un punto.
- Faltan comillas alrededor del beneficiario o la narración.
- Una transacción no está equilibrada.
- Una comprobación de saldo no coincide.
- Una transacción utiliza una cuenta después de que se haya cerrado.

Corrige el archivo de texto, guárdalo y luego recarga Fava.

## La comprobación de saldo falla

No elimines la comprobación de saldo como solución provisional. Investiga la diferencia.

Lista de verificación:

- ¿El rango de fechas del CSV estaba completo?
- ¿Se importó el mismo CSV dos veces?
- ¿Se pegaron algunas transacciones en el libro mayor incorrecto?
- ¿Se asignó una transacción a la subcuenta incorrecta de Sparkasse?
- ¿Se cambió incorrectamente el signo de una cantidad?
- ¿Se introdujo una transferencia de PayPal o en efectivo solo en un lado?
- ¿Hay ediciones manuales anteriores después de la comprobación de saldo anterior?

## La conversión de CSV falla

Comprueba:

- El archivo CSV está en la misma carpeta `test` que `csv2bean.py`.
- El nombre del archivo en el comando es exacto.
- El archivo es la exportación de Sparkasse `Excel (CSV-CAMT V2)`.
- El archivo está separado por punto y coma.
- El CSV no se abrió y se volvió a guardar de una manera que cambiara su formato.

## Las entradas importadas parecen demasiado genéricas

Esto es esperado. El convertidor utiliza categorías de respaldo como:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

El usuario debe revisar y clasificar las entradas importadas manualmente.

## El panel de control falta

Comprueba:

- `fava-dashboards` está instalado.
- El libro mayor contiene la directiva `custom "fava-extension" "fava_dashboards"`.
- Existe un archivo `dashboards.yaml` junto al libro mayor.
- Fava se reinició después de la instalación o los cambios de configuración.

## Un proyecto no aparece en los paneles de control

Comprueba:

- El proyecto tiene una cuenta de activos del proyecto bajo el prefijo esperado de Sparkasse o PayPal.
- La cuenta del proyecto no está cerrada.
- El saldo del proyecto no es exactamente cero.
- El nombre de la cuenta coincide con el patrón de consulta del panel de control.

## El enlace del documento no funciona

Comprueba:

- La ruta del archivo es relativa a la carpeta del archivo del libro mayor.
- El nombre del archivo está escrito exactamente.
- El documento no se movió después de vincularlo.
- La ruta utiliza barras inclinadas hacia adelante o un estilo de ruta relativa normal.

## No estoy seguro de cómo clasificar una transacción

Utiliza este orden:

1. Busca transacciones antiguas similares en Fava.
2. Comprueba el contexto del proyecto o la factura.
3. Comprueba si pertenece a una línea presupuestaria de un financiador.
4. Añade un comentario si no estás seguro.
5. Utiliza temporalmente `Sonstiges` solo si no se conoce una mejor categoría.
6. Pregunta a la persona responsable del proyecto o de finanzas antes de finalizar.
