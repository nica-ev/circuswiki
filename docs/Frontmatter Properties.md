---
publish: false
tags: 
title: Frontmatter Properties
description: Wie nutzen wir Frontmatter in den Markdown Dateien
created: 2025-01-21 18:09:55
update: 2025-01-23 22:02:43
authors:
  - Marc Bielert
---

Wir nutzen folgendes Frontmatter Format

| Eigenschaft | Datentyp    | Default | Erklärung                                                                             |
| ----------- | ----------- | ------- | ------------------------------------------------------------------------------------- |
| created     | Date + Time | auto    | Wann die Datei erzeugt wurde<br>wird automatisch eingetragen                          |
| update      | Date + Time | auto    | Wann die Datei zuletzt geändert wurde,<br>wird automatisch eingetragen                |
| publish     | Boolean     | false   | Entscheidet ob eine Datei veröffentlicht wird als Teil der Webseite                   |
| tags        | tags        | -       | Tags welche hier definiert sind werden auch auf der Webseite angezeigt                |
| title       | string      | -       | Der Titel wird in der Webseite als Überschrift vor dem eigentlichen Inhalt angezeigt, |
| authors     | list        | -       | eine Liste der Urheber des Inhaltes dieser Seite                                      |

