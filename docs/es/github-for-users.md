---
lang: es
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub - Colaborar directamente en el repositorio
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:35+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:19+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] En resumen
> Esta página está pensada para personas que desean trabajar directamente en los archivos Markdown de CircusWiki. Para contribuciones normales, no necesitas este método: también puedes enviar material simplemente por correo electrónico.

La colaboración directa a través de GitHub es práctica si deseas corregir páginas con regularidad, crear nuevos archivos Markdown o trabajar con la bóveda de CircusWiki en un editor como Obsidian.

Si solo deseas aportar un juego, un método, un PDF, un enlace o una corrección, el camino más sencillo suele ser mejor:

[Volver a Colaborar](mitmachen.md){ .md-button }

## Lo que necesitas

- Una cuenta gratuita de GitHub: [https://github.com/join](https://github.com/join)
- Opcionalmente, GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- Un editor de texto para archivos Markdown, por ejemplo, Obsidian, VS Code o un editor sencillo.

GitHub Desktop no es obligatorio, pero para muchas personas es más fácil que la línea de comandos.

## Encontrar el repositorio

El repositorio público se encuentra aquí:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Allí se encuentran los archivos Markdown reales, imágenes, traducciones y herramientas a partir de los cuales se construye la página web.

## Flujo de trabajo en resumen

El proceso típico es:

1. Hacer un "fork" del repositorio en GitHub.
2. Clonar tu copia a tu propio ordenador.
3. Realizar cambios en una nueva rama ("branch").
4. Editar archivos o crear nuevos archivos Markdown.
5. Confirmar ("commit") los cambios.
6. Subir la rama a GitHub.
7. Abrir una solicitud de extracción ("Pull Request") para que el cambio pueda ser revisado y aceptado.

## Paso a paso con GitHub Desktop

### 1. Hacer un "fork" del repositorio

Abre el repositorio de CircusWiki en GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Haz clic en `Fork`. Esto crea una copia propia del repositorio en tu cuenta de GitHub. En esta copia puedes trabajar sin modificar directamente el proyecto principal.

### 2. Clonar el repositorio

Abre GitHub Desktop y selecciona:

```text
File -> Clone repository...
```

Selecciona tu "fork" de `nica-ev/circuswiki` y define una carpeta en tu ordenador.

Después de esto, tendrás una copia local de los archivos.

### 3. Crear una rama ("branch")

Para tu cambio, es mejor crear tu propia rama, por ejemplo:

```text
añadir-descripcion-juego
corregir-enlace
nueva-metodo-equilibrio
```

Una rama mantiene tu trabajo separado del estado principal. Esto facilita la revisión posterior.

### 4. Editar archivos

Los contenidos públicos se encuentran principalmente en las carpetas de idiomas bajo `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Todos los idiomas son equivalentes. No hay un idioma principal en el que los nuevos contenidos deban crearse fundamentalmente.

Si creas una nueva página original, colócala en la carpeta de idioma en cuyo idioma esté escrito el texto. Un texto original en español pertenece, por ejemplo, a `docs/es/`, uno en alemán a `docs/de/`, uno en inglés a `docs/en/`.

El "frontmatter" al principio del archivo es importante. Allí debe ser reconocible que la página es un original, por ejemplo:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` corresponde al idioma del texto original. A partir de este original, se pueden generar automáticamente traducciones a todos los idiomas admitidos más tarde.

Al editar, presta atención a lo siguiente:

- No borres el "frontmatter" al principio del archivo.
- Para las nuevas páginas originales, establece `translation_status: original` y el `translation_source_lang` adecuado.
- Conserva los enlaces existentes siempre que sea posible.
- No publiques datos privados, claves de API o notas internas.
- Utiliza imágenes solo si los derechos de uso están claros.
- Es preferible hacer cambios pequeños y claros que cambios mixtos muy grandes.

### 5. Confirmar ("commit") los cambios

En GitHub Desktop, verás tus archivos modificados en el área `Changes`.

Escribe un resumen breve, por ejemplo:

```text
Corregir lista de materiales en el juego de movimiento
Añadir aviso de seguridad para Beigoma
Agregar nueva descripción de juego
```

Luego, haz clic en `Commit to <branch-name>`.

### 6. Subir los cambios

Haz clic en `Push origin` para subir tu rama a GitHub.

### 7. Abrir una solicitud de extracción ("Pull Request")

GitHub Desktop o GitHub en el navegador ofrecerán entonces la opción de crear una solicitud de extracción.

Una solicitud de extracción significa: Propones tu cambio para el repositorio principal. El cambio se revisa, se comentan si es necesario y luego se acepta o se sigue trabajando en él.

## Fundamentos de Markdown

Markdown es un formato de texto sencillo. Los caracteres más importantes son suficientes para la mayoría de las contribuciones:

```markdown
# Encabezado grande
## Encabezado de sección

Texto normal con **énfasis en negrita** y *énfasis en cursiva*.

- Elemento de lista
- Otro elemento de lista

[Texto del enlace](https://www.example.com)
```

## Si algo no está claro

No es necesario dominar la colaboración directa a través de GitHub de inmediato. Si abres una solicitud de extracción y algo aún no está correcto, se puede aclarar durante la revisión.

Si solo deseas aportar contenido y el método técnico te parece demasiado complicado, simplemente utiliza el correo electrónico en la [página de Colaboración](mitmachen.md).
