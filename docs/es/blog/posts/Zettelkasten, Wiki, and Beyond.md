---
lang: es
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki y más allá
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:00:05+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:12+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki y Más Allá**  
**Por qué inicié este proyecto, las ideas detrás de él y hacia dónde podría dirigirse.**

En 2013, trabajaba como gestor de proyectos para un circo juvenil. Los formadores a menudo me preguntaban si conocía otros juegos, métodos o trucos. En ese momento, tenía muchos recursos —libros, revistas, notas de talleres— pero todo estaba desorganizado y apenas digitalizado.  
<!-- more -->
Mi primer intento para hacer que estos recursos fueran accesibles para los formadores fue un wiki clásico. Muchas de las descripciones de juegos que se ven hoy en día se originaron en esa época. Simultáneamente, comencé a digitalizar mis fuentes. Descubrí el método *Zettelkasten* (caja de fichas) de Niklas Luhmann y empecé a organizar mis datos siguiendo sus principios.  

El wiki fue un fracaso. Hubo poca interacción; los formadores lo usaron unas pocas veces y pronto se olvidó. Mi Zettelkasten personal, sin embargo, comenzó a crecer. Aunque inicialmente utilicé software especializado, pronto empecé a pensar en cómo asegurar la longevidad de esta colección cada vez más valiosa.  

¿Qué significa eso? La primera llamada de atención llegó cuando me di cuenta de que el software que estaba utilizando ya no se desarrollaba. Tuve que encontrar un nuevo software y pensar en cómo migrar mis datos a él. Fue entonces cuando descubrí Markdown.  

Markdown es un formato de archivo simple —esencialmente un archivo de texto plano— diseñado para funcionar independientemente de cualquier software específico. En otras palabras, es un estándar ampliamente adoptado que puede ser leído y editado con las herramientas más básicas.  

El formato soportaba todo lo que necesitaba: formato de texto básico, enlaces, etiquetas y metadatos (por ejemplo, título, autor, descripción, etc.). Encontré un nuevo software que utilizaba Markdown y continué construyendo mi Zettelkasten. En ese momento, tenía alrededor de 600 notas (o archivos/páginas). Más tarde, volví a cambiar de software, y la transición fue perfecta.  

>[!info]  Conclusión Clave
>Asegurar la longevidad de tus datos significa usar un formato simple y ampliamente adoptado que sea independiente de software específico.  

## Colaboración y Compartir  

Mi primer intento de wiki no funcionó, en parte porque no logré inspirar a otros a contribuir. A lo largo de los años, mi Zettelkasten personal creció hasta más de 3.000 notas, muchas de ellas sobre temas como pedagogía circense, juegos, malabares y más.  

Durante un tiempo, simplemente lo hice accesible en línea, pero más allá de unas pocas personas que lo conocían y consultaban ocasionalmente descripciones de juegos, no hubo una colaboración real ni un intercambio más amplio.  

Ahora, unos 12 años después de empezar mi Zettelkasten, lo intento de nuevo. El objetivo es crear una base de conocimiento compartida para temas como la pedagogía circense y del movimiento, las artes circenses y más allá.  

### Consideraciones y Preguntas Clave  
- **Independencia de sistemas específicos**  
- **Formato de datos simple y fácil de entender**  
- **Utilidad y público objetivo**  
- **Datos estructurados**  

El software de wiki tradicional (o plataformas como WordPress) quedaron descartados porque crean dependencia de un único sistema. Si bien esto puede funcionar a corto o medio plazo, es una debilidad clara a largo plazo.  

En su lugar, gestiono los datos (como archivos Markdown e imágenes) independientemente de cómo se presenten finalmente. Esto asegura que, incluso dentro de 20 años, los datos sigan siendo utilizables. La forma en que se muestren o editen puede cambiar drásticamente, pero los datos subyacentes permanecen iguales.  

Hay innumerables formas de presentar los datos: como un sitio web, un libro electrónico, un PDF o incluso una aplicación. Se puede comprimir en un archivo y leer o editar sin conexión con un simple editor de texto. Si quieres mostrarlo como un sitio de WordPress o un wiki, es solo cuestión de importar los datos —dado que están estructurados y son fáciles de leer, es relativamente sencillo de implementar (con los conocimientos adecuados).  

## Mi Solución Actual para el Sitio Web  

Estoy utilizando MkDocs y el tema MkDocs-Material para generar un sitio web estático. Hay muchos programas que crean archivos HTML estáticos a partir de Markdown, pero MkDocs está diseñado específicamente para documentación. Muchas de las funciones que genera —como la búsqueda de texto completo y la navegación— son increíblemente útiles.  

MkDocs es también una solución de código abierto ampliamente utilizada y respaldada por grandes empresas, lo que garantiza que seguirá siendo funcional al menos a medio plazo.  

## Colaboración  

El siguiente paso es convertir esto en un esfuerzo colaborativo. Estoy explorando formas de invitar a otros a contribuir, ya sea añadiendo contenido nuevo, refinando entradas existentes o sugiriendo mejoras. El objetivo es crear un recurso vivo y en evolución que se beneficie del conocimiento y la experiencia colectivos.
