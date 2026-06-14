---
lang: es
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: Traducción de Documentos PDF con Modelos de Lenguaje Grandes
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:33:46+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:33:46+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Tutorial: Traducir documentos PDF utilizando modelos de lenguaje grandes

## Introducción

Este tutorial describe un proceso para traducir el contenido de documentos PDF, especialmente aquellos que contienen texto basado en imágenes no seleccionable, utilizando modelos de lenguaje grandes (LLM). El flujo de trabajo implica optimizar el PDF, extraer texto mediante reconocimiento óptico de caracteres (OCR), traducir el texto y, finalmente, reformatear la traducción a un PDF.

**Requisitos previos:**

*   Una cuenta de Google (para acceder a Google AI Studio).
*   Opcional: Software de optimización de PDF (por ejemplo, pdf24 Creator).
*   Opcional: Un editor de texto o procesador de textos capaz de manejar Markdown y exportar a PDF (por ejemplo, Obsidian, Microsoft Word).

## Paso 1: Preparación del documento PDF

**Objetivo:** Reducir el tamaño del archivo PDF para optimizarlo para el procesamiento por parte del LLM, manteniendo al mismo tiempo la legibilidad del texto. Los LLM a menudo tienen límites de tamaño de entrada y los archivos más pequeños se procesan de manera más eficiente.

**Consideraciones:**

*   **PDF basados en texto:** Si el texto dentro del PDF se puede seleccionar (lo que significa que está incrustado electrónicamente), la reducción del tamaño del archivo es generalmente más fácil y puede lograr tamaños más pequeños sin pérdida de calidad.
*   **PDF basados en imágenes:** Si las páginas del PDF son imágenes de texto (el texto no se puede seleccionar individualmente), la reducción del tamaño implica la compresión de imágenes. Se debe tener cuidado de no reducir la calidad tanto como para que el texto se vuelva ilegible para el OCR.

**Procedimiento (Ejemplo con pdf24):**

1.  Abra su documento PDF en una herramienta como pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Utilice las funciones de compresión o reducción de tamaño. Las configuraciones efectivas comunes incluyen:
    *   Habilitar la optimización web.
    *   Convertir colores a escala de grises.
3.  Experimente con los niveles de compresión, apuntando a un tamaño de archivo inferior a **5 MB**, asegurándose de que el texto permanezca claro y legible.
4.  Guarde el archivo PDF optimizado.

## Paso 2: Extracción de texto utilizando Google AI Studio (Transcripción/OCR)

**Objetivo:** Utilizar las capacidades multimodales de un LLM para realizar OCR en el PDF preparado y extraer el contenido textual en un formato estructurado.

**Procedimiento:**

1.  Navegue a **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/)) e inicie sesión con su cuenta de Google. Nota: AI Studio es principalmente una herramienta para experimentar con modelos y prompts.
2.  Inicie una nueva sesión o chat.
3.  Adjunte el archivo PDF optimizado a su sesión (por ejemplo, utilizando el botón de adjuntar o arrastrando y soltando).
4.  Introduzca el siguiente prompt en el área de mensajes del usuario:
    ```
    Por favor, transcriba el PDF adjunto. Contiene imágenes con texto, lo que requiere OCR. Salga la transcripción en formato Markdown adecuado, utilizando encabezados y listas para crear una estructura que imite de cerca el diseño del documento original.
    ```
5.  Configure los ajustes del modelo:
    *   Mantenga la configuración predeterminada a menos que tenga requisitos específicos.
    *   Establezca la **Temperatura** en **0.1**. Una temperatura más baja fomenta una salida más determinista y menos creativa, lo que es adecuado para una transcripción precisa.
6.  Envíe el prompt. El proceso de transcripción puede tardar varios minutos (potencialmente 4-6 minutos o más, dependiendo del tamaño y la complejidad del PDF).
7.  Una vez completada la generación, copie el texto Markdown resultante.
    *   *Método 1:* Utilice la opción de copiar que a menudo se proporciona dentro de la interfaz (por ejemplo, a través de un menú asociado con la respuesta).
    *   *Método 2:* Seleccione manualmente todo el texto generado y cópielo (Ctrl+C o clic derecho -> Copiar).
8.  Pegue el texto Markdown copiado en un editor de texto plano (como Bloc de notas, VS Code, Obsidian, etc.).
9.  Guarde este contenido como un archivo de texto plano. Se recomienda utilizar extensiones `.txt` o `.md` (Markdown). El formato Markdown ayuda a preservar la estructura del documento (encabezados, listas).

![Google AI Studio - Captura de pantalla de transcripción](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Paso 3: Traducción del texto extraído utilizando Google AI Studio

**Objetivo:** Traducir el texto Markdown extraído al idioma de destino deseado, preservando la estructura y el formato originales.

**Procedimiento:**

1.  En **Google AI Studio**, inicie un **nuevo chat** para asegurar un contexto fresco para la tarea de traducción.
2.  Adjunte el archivo `.txt` o `.md` guardado que contiene el texto Markdown extraído.
3.  Introduzca un prompt de traducción, especificando los idiomas de origen y destino. Ejemplo de inglés a italiano:
    ```
    Por favor, traduzca el archivo Markdown adjunto (inglés) al italiano. Mantenga la estructura original, el formato, el tono y el estilo del habla con precisión.
    ```
    *   **Modifique el prompt** según sus idiomas de origen y destino específicos (por ejemplo, "...traduzca el archivo Markdown adjunto (alemán) al español..."). La calidad de la traducción puede variar según el par de idiomas.
4.  Configure los ajustes del modelo:
    *   Asegúrese de que la configuración predeterminada sea apropiada.
    *   Establezca la **Temperatura** en **0.1** para promover la fidelidad al texto y la estructura de origen durante la traducción.
5.  Envíe el prompt. La traducción también puede tardar varios minutos, comparable al tiempo de transcripción.
6.  Una vez generado, copie el texto Markdown traducido utilizando los métodos descritos en el Paso 2 (botón de copiar de la interfaz o selección manual).

![Google AI Studio - Captura de pantalla de traducción](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Paso 4: Reformateo del texto traducido a un documento PDF

**Objetivo:** Convertir el texto Markdown traducido de nuevo a un documento PDF para compartirlo o archivarlo.

**Procedimiento:**

1.  Pegue el texto Markdown traducido copiado en una aplicación adecuada.
2.  **Recomendado:** Utilice un editor de texto o un procesador de documentos que entienda el formato Markdown para preservar la estructura (encabezados, listas, etc.).
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) es una herramienta gratuita que funciona bien con archivos Markdown y a menudo tiene capacidades de exportación a PDF (directamente o a través de complementos).
    *   Los procesadores de textos modernos (como Microsoft Word) también pueden importar o pegar Markdown y permitir guardar/exportar como PDF, aunque la fidelidad del formato puede variar.
    *   También hay disponibles convertidores dedicados de Markdown a PDF en línea o como software instalable.
3.  Utilice la función "Exportar a PDF" o "Guardar como PDF" de la aplicación.
4.  Revise el PDF resultante para asegurarse de que el formato y el contenido aparezcan como se espera.

## Conclusión

Este tutorial demostró un flujo de trabajo para aprovechar Google AI Studio para transcribir y traducir documentos PDF, incluidos aquellos que requieren OCR. Al preparar el PDF, extraer texto utilizando un LLM configurado, traducir el resultado y reformatearlo, los usuarios pueden obtener versiones traducidas de sus documentos. Si bien este método ofrece una solución gratuita o de bajo costo, los usuarios deben tener en cuenta las posibles variaciones en la precisión del OCR y la calidad de la traducción, especialmente para diseños complejos o idiomas menos comunes. Los tiempos de procesamiento dependen significativamente del tamaño del documento y de la carga del servidor.
