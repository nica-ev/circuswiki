---
lang: es
translation_id: obsidian-setup
publish: true
tags: 
title: Configuración de Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:09:26+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:22+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian es extremadamente personalizable, lo que puede ser un problema para los recién llegados.
Proporcionamos una configuración base que se puede usar tal cual, incluyendo plugins y temas, así como sus ajustes finos.
Esta es una configuración base y se puede ajustar aún más a las preferencias personales de cada uno.
Proporcionamos una solución funcional, que documentaremos y explicaremos aquí.

## Términos utilizados
**Vault** (Bóveda): una colección de archivos markdown e imágenes que forman la base de conocimiento.

## Plugins

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Proporciona acceso a muchas funciones nuevas y opciones de estilo para Canvas.

### BRAT
Necesario para instalar plugins no oficiales / plugins no registrados en el ecosistema de Obsidian, a saber:
- Dataview Serializer
- Sortable

### Better Word Count
Se utiliza principalmente por su capacidad para mostrar el número de palabras/caracteres en el texto resaltado.
Es visible en la barra de estado.

### Beautitab
Puramente cosmético, proporciona una página personalizable de "nueva pestaña vacía".

### Clear unused Images
Como su nombre indica, ayuda a organizar la bóveda identificando imágenes no utilizadas.

❗He excluido la subcarpeta ```/site/``` para que no elimine siempre las imágenes del sitio web generado (lo cual no es un problema, sino una molestia).

❗Tenga cuidado al usar el comando de limpieza de adjuntos, ya que esto siempre eliminará ```mkdocs.yml``` y ```license.``` --> si esto sucede, los archivos estarán en la carpeta .trash y se podrán recuperar. Pero es fácil pasarlo por alto.

### Dataview
Permite consultas tipo SQL en la bóveda.

### Dataview Serializer
Convierte los resultados de Dataview en markdown.
Ayuda a reutilizar los resultados de las consultas de Dataview en las notas reales.

### Emoji Toolbar
Bueno, proporciona acceso fácil a los emojis.
**Atajo de teclado configurado en: ALT-E**
😍

### Linter
Limpia archivos markdown y datos de frontmatter.
Ayuda a mantener un formato consistente.

### Note Toolbar
Permite barras de herramientas personalizables en la parte superior de una nota que se pueden definir a nivel de carpeta/archivo.

### Tag Wrangler
Proporciona opciones adicionales para trabajar con etiquetas.
- Renombrar etiquetas
Ayuda a organizar la bóveda.

### Templater
Permite plantillas personalizables que se pueden insertar manualmente o basándose en condiciones (como la creación de una nota).

### Status Bar Organizer
Permite ocultar elementos de la barra de estado.

### Sortable
Permite ordenar tablas (tanto de markdown como de dataview) haciendo clic en sus encabezados.

### Workspaces Plus
Permite un cambio rápido y fácil desde la barra de estado.

## Sistema de Archivos de la Bóveda

[Sistema de Archivos de la Bóveda](Vault%20File%20System.md){ .md-button }
