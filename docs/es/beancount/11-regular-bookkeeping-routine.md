---
lang: es
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rutina Regular de Contabilidad
description: Una lista de verificación práctica y recurrente para mantener los libros al día.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:02+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:02+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Rutina de Contabilidad Regular

Esta página describe una rutina práctica para mantener los libros al día.

## Rutina semanal o quincenal

Úsala cuando haya movimientos bancarios regulares.

1. Abre la instancia correcta de Fava.
2. Comprueba si Fava muestra errores.
3. Busca la última conciliación de saldos.
4. Exporta los datos CSV de Sparkasse más recientes.
5. Convierte el CSV con `csv2bean.py`.
6. Pega las nuevas entradas en `Bank Dump`.
7. Clasifica las entradas en las cuentas correctas.
8. Adjunta o referencia los recibos donde sea necesario.
9. Añade una nueva conciliación de saldos.
10. Recarga Fava y resuelve los errores.
11. Revisa `Ausgaben:Sonstiges` y `Einnahmen:Sonstiges` para ver si hay entradas que deberían ser más específicas.

## Rutina mensual

Al final del mes:

1. Concilia Sparkasse.
2. Concilia PayPal si se usa.
3. Concilia la caja de efectivo si se usó efectivo.
4. Revisa las deudas pendientes con personas.
5. Revisa los saldos de los proyectos activos.
6. Revisa las entradas no clasificadas de `Sonstiges`.
7. Revisa los recibos faltantes.
8. Comprueba si algún proyecto finalizado debe prepararse para su cierre.

## Rutina de informes de proyectos

Antes de preparar un informe de proyecto o un *Verwendungsnachweis* (justificante de uso):

1. Abre las páginas de las cuentas del proyecto en Fava.
2. Exporta o revisa todos los ingresos y gastos del proyecto.
3. Confirma que las categorías coinciden con las líneas presupuestarias del financiador.
4. Confirma que existen todos los recibos y documentos de honorarios.
5. Comprueba si las devoluciones, cancelaciones y reembolsos se registran como correcciones en lugar de ingresos falsos.
6. Confirma que el saldo de activos del proyecto es explicable.
7. Si el proyecto ha finalizado, transfiere el dinero restante correctamente y cierra las cuentas del proyecto.

## Rutina de fin de año

Al final del año:

1. Concilia todas las cuentas bancarias.
2. Concilia PayPal.
3. Concilia las cajas de efectivo.
4. Revisa las deudas.
5. Revisa los saldos de los proyectos pendientes.
6. Asegúrate de que todos los recibos estén almacenados y enlazados o sean localizables.
7. Revisa las categorías de ingresos y gastos.
8. Añade las conciliaciones de saldos finales.
9. Prepara los informes desde Fava.
10. Archiva los CSV exportados y los documentos de apoyo.

## Comprobaciones de calidad

Un libro de contabilidad está en buen estado cuando:

- Fava se abre sin errores.
- La última conciliación de saldos de Sparkasse coincide con el banco.
- Los saldos de PayPal y efectivo se han comprobado donde sea relevante.
- Los saldos de los proyectos son intencionados y explicables.
- Los proyectos cerrados tienen un saldo de activos cero.
- Las cuentas `Sonstiges` no contienen entradas evitables sin categorizar.
- Se pueden encontrar los recibos de los gastos.
- Los comentarios explican correcciones o suposiciones inusuales.

## Lista de verificación para la entrega a otra persona

Antes de entregar la contabilidad a otra persona:

- Muéstrale el archivo de libro de contabilidad correcto para cada asociación.
- Muéstrale cómo iniciar Fava.
- Muéstrale la última conciliación de saldos.
- Muéstrale cómo se organizan las importaciones CSV en `Bank Dump`.
- Muéstrale dónde se almacenan los recibos.
- Muéstrale un ejemplo de proyecto, desde los ingresos de financiación hasta el cierre final.
- Señálale esta carpeta de documentación.
