---
lang: es
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Notas de lanzamiento
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:14:06+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:03+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Estas notas de lanzamiento solo ofrecen una visión general aproximada; no se enumeran todos los cambios menores (como páginas individuales nuevas o modificaciones de contenido existente). Sin embargo, estos se pueden seguir en detalle en el historial del repositorio.

>[!info]- **Versión:** v0.04 - **Fecha de lanzamiento**: 9 de junio de 2026
>**Contenido**
>- Contenidos multilingües ampliados considerablemente: los contenidos ahora se encuentran estructurados bajo `docs/<idioma>`.
>- Añadidas traducciones nuevas y actualizadas para muchas descripciones de juegos y páginas de proyectos.
>- Importados materiales de taller en polaco e integrados en la estructura de contenido multilingüe.
>- Estructura de metadatos y contenido para juegos unificada aún más.
>
>**Técnico**
>- Generador de sitio web cambiado de MkDocs/MkDocs Material a Zensical.
>- Introducida nueva estructura multilingüe de compilación y staging.
>- El alemán sigue siendo el idioma predeterminado sin prefijo de idioma; otros idiomas se publicarán bajo códigos de idioma, por ejemplo, `/en/`, `/pl/`, `/es/`.
>- Introducida configuración central de idiomas a través de `tools/config/languages.json`.
>- Actualizado el despliegue de GitHub Pages para la nueva estructura de Zensical.
>- Herramientas de traducción locales y consola de desarrollo ampliadas considerablemente: comprobaciones de estado, planificación por lotes, estado de traducción, vistas de gráfico, herramientas de navegación, reparación de enlaces y flujos de trabajo de limpieza.
>- Añadidos selector de idiomas, indicadores de estado de traducción y páginas de respaldo para traducciones faltantes.
>- Mejoradas las tablas en la salida final del sitio: tablas ordenables, mejor representación de tablas densas y áreas de página plegables opcionales.
>
>**Corregido**
>- Los enlaces internos y los enlaces de Markdown en páginas traducidas se conservan y reparan de manera más fiable.
>- La navegación multilingüe y la estructura de URL se han estabilizado.
>- Mejorado el comportamiento responsivo de la navegación, especialmente en combinación con el menú hamburguesa móvil de Zensical.

>[!info]- **Versión:** v0.03 - **Fecha de lanzamiento**: 11 de marzo de 2025
>**Contenido**
>- Añadidas descripciones de juegos faltantes
>
>**Técnico**
>- Añadido favicon + logo
>- Rediseño de la interfaz de usuario
>- La navegación de primer nivel ahora está en la cabecera de la página, mientras que la barra de navegación derecha se adapta según el contexto
>- Las tablas se pueden ordenar haciendo clic en las cabeceras
>
>**Corregido**
>- Las etiquetas funcionan de nuevo

>[!info]- **Versión:** v0.02 - **Fecha de lanzamiento**: 26 de febrero de 2025
>**Técnico**
>- Función de blog
>- Analíticas (Google)
>- Banner de cookies
>- Widget de comentarios (parte inferior de cada página)

>[!info]- **Versión:** v0.01 - **Fecha de lanzamiento** 15 de enero de 2025
>**Contenido**
>- Añadidas 150 descripciones de juegos
>- Descripción básica de la documentación
>
>**Técnico**
>- Configuración base para Mkdocs y Mkdocs-materials
>- Soporte de Obsidian con Mkdocs-publisher (permite el uso de Markdown de Obsidian como enlaces de Markdown, cuadros de llamada)
