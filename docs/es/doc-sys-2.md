---
lang: es
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Sistema de documentación
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:02:21+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:10+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifiesto](doc-sys-manifest.md){ .md-button }
[Configuración de Obsidian](Obsidian%20Setup.md){ .md-button }
## Arquitectura del Sistema

La idea general
> [!info] Resumen de la arquitectura
>
> Aquí hay una representación gráfica de la arquitectura del sistema:
>```mermaid
>flowchart LR
>A(Contenidos) --> B(Control de versiones)
>C(Software de edición) --> A
>A --> D(Hacer accesible en línea)
>```

En detalle:

> [!info] Resumen de la arquitectura
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Archivos}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Tema: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Un editor de texto opcional, pero recomendado por mí, para editar archivos Markdown.
> *   **Archivos:** Los archivos Markdown que contienen el contenido de mi documentación.
> *   **Github Desktop:** Una herramienta para gestionar fácilmente mis repositorios de Git.
> *   **Github:** Un servicio en línea para control de versiones y colaboración.
> *   **Github Pages:** Un servicio gratuito para publicar mi sitio web.
> *   **MkDocs:** Una herramienta para generar automáticamente el sitio web a partir de mis archivos Markdown.
> *   **MkDocs-Material:** Un tema para MkDocs que ofrece un diseño moderno y atractivo.
> *   **MkDocs-Publisher:** Una colección de plugins que facilita la colaboración con Obsidian y ofrece funcionalidad adicional.

## Componentes en detalle

### 1. Markdown

> [!info] Markdown como base
> Utilizo el [formato Markdown](Markdown.md) para mi documentación. Markdown es un lenguaje de marcado sencillo que me permite dar formato de texto simple (por ejemplo, encabezados, listas, enlaces).

**Ventajas:**

*   Es fácil de aprender y usar, lo que me permite centrarme en el contenido.
*   Es independiente de la plataforma, por lo que puedo continuar mi trabajo en cualquier dispositivo.
*   Es ideal para el control de versiones, lo que me permite rastrear y gestionar los cambios.
*   Es a prueba de futuro y no propietario, lo que me da la seguridad de que mi trabajo seguirá siendo accesible a largo plazo.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian como editor de texto
> [Obsidian](Obsidian%20Setup.md) es un editor de texto opcional, pero recomendado por mí. Me ofrece las siguientes ventajas:

*   Puedo almacenar mis datos localmente y editarlos sin conexión, lo que me da flexibilidad y control.
*   Puedo enlazar y conectar archivos fácilmente entre sí, lo que me ayuda a organizar información compleja.
*   Puedo etiquetar y gestionar archivos fácilmente, lo que me proporciona una dimensión adicional de organización.
*   Puedo visualizar mis datos gráficamente, lo que me ayuda a reconocer patrones y relaciones.
*   Puedo ampliar la funcionalidad de Obsidian mediante plugins, lo que me permite adaptar la herramienta a mis necesidades específicas.

### 3. Git y Github

> [!info] Git para control de versiones
> [Git](https://git-scm.com/) es un sistema de control de versiones que me permite rastrear y gestionar los cambios en la documentación. [Github](https://github.com/) es un servicio en línea que me permite almacenar mis repositorios de Git y colaborar con otros.

**Ventajas:**

*   Control de versiones: Cada cambio se documenta y se puede rastrear en cualquier momento, lo que me ayuda a evitar errores y a mantener una visión general.
*   Colaboración: Varias personas pueden trabajar en la documentación al mismo tiempo, lo que me da la oportunidad de integrar comentarios y contribuciones de otros.
*   Copia de seguridad: Mi documentación está segura y se copia de seguridad regularmente, lo que me da la seguridad de que mi trabajo no se perderá.

### 4. Github Desktop

> [!info] Github Desktop como herramienta
> [Github Desktop](../_inbox/Github%20Desktop.md) es una interfaz gráfica para Git que me permite usar Git de forma sencilla y sin línea de comandos.

**Ventajas:**

*   Fácil de usar, lo que me facilita el uso de Git.
*   No se requieren conocimientos de línea de comandos, lo que me ahorra tiempo y esfuerzo.
*   Simplifica mi flujo de trabajo, lo que me permite centrarme en la creación de contenido.

### 5. MkDocs

> [!info] MkDocs como generador de sitios web
> [MkDocs](https://mkdocs.org) es un generador de sitios estáticos que convierte mis archivos Markdown en un sitio web estático.

**Ventajas:**

*   Creación sencilla de sitios web, lo que me permite publicar mi documentación de forma rápida y sencilla.
*   Actualización rápida, lo que me permite ver los cambios en tiempo real.
*   Diseño coherente, lo que garantiza una presentación profesional y uniforme de mi documentación.
*   Vista previa sin conexión, lo que me permite revisar mi documentación antes de publicarla.

### 6. Github Pages

> [!info] Github Pages para alojamiento
> [Github Pages](../_inbox/Github%20Pages.md) es un servicio de alojamiento gratuito de Github que me permite publicar mi sitio web fácilmente en línea.

**Ventajas:**

*   Alojamiento gratuito, lo que me permite publicar mi documentación sin costes adicionales.
*   Publicación sencilla, lo que me libera de la implementación técnica de la publicación.
*   Fiable, lo que me da la seguridad de que mi documentación estará disponible en todo momento.

### 7. MkDocs-Material

> [!info] MkDocs-Material como tema
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) es un tema para MkDocs que ofrece un diseño moderno y atractivo.

**Ventajas:**

*   Diseño moderno, lo que hace que mi documentación parezca profesional y actual.
*   Personalizable, lo que me permite adaptar el diseño a mis necesidades específicas.
*   Fácil de usar, lo que me facilita el uso de la documentación.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher como colección de plugins
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) es una colección de plugins de MkDocs que simplifican la colaboración con Obsidian y ofrecen funciones adicionales.

**Ventajas:**

-   **Integración simplificada con Obsidian:** Adaptación automática de la sintaxis Markdown de Obsidian (callouts, wikilinks, etc.).
-   **Metadatos ampliados:** Integración de etiquetas y categorías del frontmatter de Obsidian.

## Flujo de trabajo

> [!info] Mi flujo de trabajo
> Aquí está mi flujo de trabajo típico:

1.  Creo y edito archivos Markdown con un editor de texto (opcionalmente Obsidian).
2.  Guardo los archivos Markdown localmente.
3.  Subo mis cambios al repositorio de Git con Github Desktop.
4.  Genero automáticamente el sitio web con MkDocs.
5.  Publico el sitio web con Github Pages.

## Sistema de archivos

> [!info] Estructura de directorios
> Aquí está la estructura de directorios de mi sistema:
>
> ```
>/docs/     (Aquí están mis archivos Markdown)
>/site/     (Aquí se genera el sitio web)
>license    (Información de licencia)
>mkdocs.yml (Archivo de configuración para MkDocs)
>readme.md  (Archivo para describir el repositorio)
>```

## Alternativas para la creación de contenido

> [!info] Alternativas para la creación de contenido
> Soy consciente de que no todo el mundo está familiarizado con Markdown y Git. Por lo tanto, ofrezco las siguientes alternativas:

1.  **Wordpress:** El contenido se puede crear en Wordpress como una página.
2.  **Archivo de texto, archivo de Word:** El contenido se puede crear como un archivo de texto, un archivo de Word (o en otros formatos típicos).

En estos casos, puedo incorporar el contenido al sistema.
