---
lang: es
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Recibos y Documentos
description: Explica dónde se almacenan los documentos de soporte y cómo las transacciones hacen referencia a los recibos.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:50+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:50+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Recibos y Documentos

Los recibos, facturas, contratos y otros documentos de respaldo hacen que las transacciones sean auditables. El libro mayor debe permitir encontrar el documento detrás de un gasto.

## Dónde se almacenan los documentos

Tohuwabohu tiene actualmente una carpeta de recibos clara:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Los recibos que ya se han introducido en el libro mayor se encuentran a menudo en:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA utiliza archivos de soporte en su carpeta de contabilidad y carpetas de proyectos. Si más adelante se introduce una carpeta de recibos coherente para NICA, documéntelo aquí y utilícela de forma consistente.

## Entradas de `document`

Una entrada de `document` vincula un archivo a una cuenta y fecha:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

La ruta del archivo es relativa a la carpeta que contiene el archivo del libro mayor.

## Enlaces de documentos con etiquetas

Algunas entradas antiguas incluyen etiquetas de documentos como:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

La parte `^2023_001` es un enlace de Beancount. Puede conectar un recibo a la transacción relacionada si se utiliza el mismo enlace allí.

## Significado de `scanned`

Los comentarios en los libros mayores definen la convención para los recibos escaneados. Cuando se utiliza la etiqueta `scanned`, significa:

- El recibo fue escaneado o digitalizado.
- La imagen se redujo y optimizó, por ejemplo, con TinyPNG.
- El archivo se guardó utilizando un patrón de año y número, por ejemplo, `2023_002.jpg`.
- El número se referencia en la entrada del libro mayor relacionada.

## Buenos nombres de archivo

Los buenos nombres de archivo de recibos son estables y legibles:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Evite nombres como `scan.jpg`, `image1.jpg` o `download.pdf`.

## Flujo de trabajo para un nuevo recibo

1. Guarde el recibo en la carpeta de recibos correcta.
2. Renómbrelo para que pueda ser reconocido más tarde.
3. Introduzca o encuentre la transacción relacionada.
4. Añada una línea de `document` o metadatos de enlace si es útil.
5. Si el recibo ha sido procesado, muévalo a `Eingetragen` si esa es la convención de la carpeta.
6. Recargue Fava y compruebe que el enlace del documento funciona.

## Cuando falta un recibo

Si falta un recibo, añada un comentario cerca de la transacción:

```beancount
; Receipt missing. Ask responsible person.
```

No finja que hay un documento si no está disponible.

## Contratos y documentos de honorarios

Los contratos y las facturas de honorarios deben almacenarse cerca del proyecto relacionado o de la carpeta de contabilidad y referenciarse claramente. Para las auditorías de proyectos, la pregunta importante no es solo que exista la transacción, sino que el documento que prueba el gasto se pueda encontrar rápidamente.
