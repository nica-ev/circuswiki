---
lang: es
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Juegos - El Lado de los Datos
description: Cómo se estandarizaron las descripciones de los juegos y se hicieron más dinámicas utilizando metadatos y plugins de Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:00:57+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:57+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Juegos - El Lado de los Datos**
**Cómo se estandarizaron y dinamizaron las descripciones de juegos utilizando metadatos y plugins de Obsidian.**

Cuando se trata de gestionar contenido, la coherencia es clave. Para la primera sección principal de este proyecto, me ocupé de los juegos, alrededor de 170, cada uno con su propio formato, estilo y accesibilidad únicos. ¿El problema? Muchas de estas descripciones dependían de enlaces estáticos codificados, lo que hacía una pesadilla añadir juegos nuevos o ajustar la estructura.

Así que me arremangué y me puse a trabajar.
<!-- more -->
## Paso 1: Un Formato Unificado
Lo primero fue establecer un formato coherente para todas las descripciones de juegos. Me inspiré en el "Tasifan Spielebuch" (Libro de Juegos Tasifan), un recurso bien organizado para descripciones de juegos. Para hacerlo aún más fácil de usar, añadí resúmenes cortos para que todos los detalles esenciales fueran visibles de un vistazo, incluso en una vista previa.

Pero, ¿el verdadero cambio de juego? Los metadatos.

## Paso 2: Magia de Metadatos
Ahora, toda la información clave —tamaño del grupo, materiales, duración y más— se almacena como metadatos en la parte superior de cada archivo Markdown en un formato llamado YAML (o *frontmatter*). Esto no solo mantiene las cosas organizadas, sino que también hace que los datos sean reutilizables en todo el sistema.

Para facilitar la búsqueda del juego adecuado, implementé una lógica simple pero efectiva:
1. **Elige una categoría**: ¿Qué tipo de juego buscas? ¿Un juego para calmarse? ¿Un juego de persecución? ¿Algo para crear equipo? He creado un conjunto de categorías para empezar, pero estas se pueden ajustar o ampliar según sea necesario.
2. **Explora la tabla**: Una vez que hayas elegido una categoría, verás una tabla que enumera todos los juegos que encajan. La tabla es ordenable: solo haz clic en los encabezados para organizar por duración, dificultad u otros criterios.

Y aquí está el truco: muchos juegos aparecen en varias categorías, por lo que nunca estás limitado a una sola forma de encontrar lo que necesitas.

## Tablas No Tan Dinámicas
La verdadera magia ocurre con dos plugins de Obsidian: **Dataview** y **Dataview Serializer**.

Dataview me permite crear listas y tablas dinámicas utilizando consultas similares a bases de datos. ¿El inconveniente? Estas tablas solo funcionan dentro de Obsidian porque los archivos Markdown subyacentes no se modifican.

Entra Dataview Serializer. Este plugin convierte esas tablas dinámicas en formato Markdown estático y las escribe directamente en el archivo. Cuando el sitio se compila usando MkDocs, las tablas son estáticas pero se generaron esencialmente de forma dinámica sin conexión.

Estas consultas pueden ser bastante complejas, lo que me permite buscar o mostrar partes específicas de la wiki, como todas las descripciones de juegos o artículos escritos por un autor específico. Y como se actualizan automáticamente (a través del paso del serializador), añadir información nueva y construir una estructura navegable es pan comido.

Pero no todo es color de rosa. El proceso no es totalmente automático. Dataview Serializer solo puede reescribir un archivo si está abierto en Obsidian. Por ahora, esto es manejable: he etiquetado cada página con una tabla o lista dinámica, lo que facilita su recorrido. Pero si el número de estas páginas crece significativamente, podría necesitar replantear el enfoque.

## Herramientas y Modelos de Lenguaje
Las descripciones originales de los juegos eran una mezcla en cuanto a formato y calidad. Para agilizar el proceso, recurrí a modelos de lenguaje (LLM). Elaboré un *prompt* específico, completo con formato de ejemplo, para asegurar que el contenido en sí no se alterara (sin reescrituras innecesarias). Aun así, revisé manualmente cada resultado e hice pequeños ajustes donde fue necesario.

Aquí está la conclusión: cuando se usan correctamente, estas herramientas son *increíblemente* potentes. La clave es ser preciso e intencional en cómo se enmarcan las tareas.

Los cambios finales son principalmente de formato: cómo se presenta la información y las descripciones de los juegos. Sin embargo, los metadatos se introdujeron todos manualmente. Dado que tuve que revisar todo de todos modos, hacerlo a mano fue más rápido en este caso.

Sin embargo, es un proceso lento. Trabajando a tiempo parcial, gestiono entre 10 y 15 juegos al día. El progreso es constante, pero va a llevar tiempo.

## Desafíos por Delante
Un obstáculo potencial son las traducciones. Las consultas de búsqueda tendrían que adaptarse para encontrar versiones específicas del idioma de los juegos o etiquetas. Por ahora, esto se puede manejar manualmente, pero si el sistema crece, la automatización podría ser necesaria.

La traducción es un tema complejo, y lo abordaré con más detalle en otro momento.

## ¿Por Qué Molestarse?
¿La respuesta corta? Escalabilidad.

Este sistema está diseñado para crecer. Al estandarizar el formato, aprovechar los metadatos y utilizar herramientas dinámicas, he creado una base que puede manejar más contenido sin volverse inmanejable.

## ¿Qué Más Hay de Nuevo?
La función de búsqueda ha recibido algunas mejoras:
- **Autocompletado**: A medida que escribes, la búsqueda sugiere consultas que arrojan más resultados. Esto no se basa en el comportamiento del usuario —no rastreamos las búsquedas— sino en el índice de búsqueda estático generado cuando se compila el sitio.
- **Búsquedas guardadas**: Haz clic en un pequeño icono junto a la barra de búsqueda y tu consulta (y resultados) se guardan en la URL. Márcala como favorita y obtendrás los mismos resultados cada vez.

Es una característica pequeña, pero podría volverse increíblemente útil a medida que la wiki crezca y cubra temas más diversos.
