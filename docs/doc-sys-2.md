---
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-01-24 03:16:31
title: Dokumentations-System
authors:
  - Marc Bielert
---

[[doc-sys-manifest|Manifest]]{ .md-button } | [[Obsidian Setup]]{ .md-button }
## Systemarchitektur

Die allgemeine Idee
> [!info] Übersicht der Architektur
>
> Hier ist eine grafische Darstellung der Systemarchitektur:
>```mermaid
>flowchart LR
>A(Inhalte) --> B(Versionskontrolle)
>C(Bearbeitungssoftware) --> A
>A --> D(Online zugänglich machen)
>```

Im Detail :

> [!info] Übersicht der Architektur
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Files}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs) 
>D --> F(Github Pages)
>G(Theme: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Ein optionaler, aber von mir empfohlener Texteditor für die Bearbeitung von Markdown-Dateien.
> *   **Files:** Die Markdown-Dateien, die den Inhalt meiner Dokumentation enthalten.
> *   **Github Desktop:** Ein Tool zur einfachen Verwaltung meiner Git-Repositories.
> *   **Github:** Ein Online-Dienst zur Versionskontrolle und Zusammenarbeit.
> *  **Github Pages:** Ein kostenloser Dienst zur Veröffentlichung meiner Webseite.
> *   **MkDocs:** Ein Tool zur automatischen Erstellung der Webseite aus meinen Markdown-Dateien.
> *   **MkDocs-Material:** Ein Theme für MkDocs, das ein modernes und ansprechendes Layout bietet.
> * **MkDocs-Publisher**: Eine Kollektion von Plugins welche die Zusammenarbeit mit Obsidian einfacher macht sowie zusätzliche Funktionalität bietet.

## Komponenten im Detail

### 1. Markdown

> [!info] Markdown als Basis
> Ich verwende das [[Markdown|Markdown Format]] für meine Dokumentation. Markdown ist eine einfache Auszeichnungssprache, die es mir ermöglicht, Text mit einfachen Formatierungen zu versehen (z.B. Überschriften, Listen, Links).

**Vorteile:**

*   Es ist einfach zu erlernen und zu verwenden, was mir erlaubt, mich auf den Inhalt zu konzentrieren.
*   Es ist plattformunabhängig, sodass ich meine Arbeit auf jedem Gerät fortsetzen kann.
*   Es ist ideal für die Versionskontrolle, was mir ermöglicht, Änderungen nachzuverfolgen und zu verwalten.
*   Es ist zukunftssicher und nicht proprietär, was mir die Gewissheit gibt, dass meine Arbeit langfristig zugänglich bleibt.

[[Markdown]]{ .md-buttons }

### 2. Obsidian

> [!info] Obsidian als Texteditor
> [[Obsidian Setup|Obsidian]] ist ein optionaler, aber von mir empfohlener Texteditor. Er bietet mir folgende Vorteile:

*   Ich kann meine Daten lokal speichern und offline bearbeiten, was mir Flexibilität und Kontrolle gibt.
*   Ich kann Dateien einfach verlinken und miteinander vernetzen, was mir hilft, komplexe Informationen zu organisieren.
*   Ich kann Dateien mit Tags versehen und einfach verwalten, was mir eine zusätzliche Dimension der Organisation ermöglicht.
*   Ich kann meine Daten grafisch darstellen, was mir hilft, Muster und Beziehungen zu erkennen.
*   Ich kann die Funktionalität von Obsidian durch Plugins erweitern, was mir erlaubt, das Tool an meine spezifischen Bedürfnisse anzupassen.

### 3. Git und Github

> [!info] Git für Versionskontrolle
> [Git](https://git-scm.com/) ist ein Versionskontrollsystem, das es mir ermöglicht, Änderungen an der Dokumentation nachzuverfolgen und zu verwalten. [Github](https://github.com/) ist ein Online-Dienst, der mir ermöglicht, meine Git-Repositories zu speichern und mit anderen zusammenzuarbeiten.

**Vorteile:**

*   Versionskontrolle: Jede Änderung wird dokumentiert und kann jederzeit nachvollzogen werden, was mir hilft, Fehler zu vermeiden und den Überblick zu behalten.
*   Zusammenarbeit: Mehrere Personen können gleichzeitig an der Dokumentation arbeiten, was mir die Möglichkeit gibt, Feedback und Beiträge von anderen zu integrieren.
*   Backup: Meine Dokumentation ist sicher und wird regelmäßig gesichert, was mir die Gewissheit gibt, dass meine Arbeit nicht verloren geht.

### 4. Github Desktop

> [!info] Github Desktop als Tool
> [Github Desktop](Github%20Desktop.md) ist eine grafische Oberfläche für Git, die es mir ermöglicht, Git einfach und ohne Kommandozeile zu nutzen.

**Vorteile:**

*   Einfache Bedienung, was mir die Nutzung von Git erleichtert.
*   Keine Kenntnisse der Kommandozeile notwendig, was mir Zeit und Mühe spart.
*   Vereinfacht meinen Workflow, was mir erlaubt, mich auf die Erstellung von Inhalten zu konzentrieren.

### 5. MkDocs

> [!info] MkDocs als Webseitengenerator
> [MkDocs](https://mkdocs.org) ist ein statischer Seiten-Generator, der meine Markdown-Dateien in eine statische Webseite umwandelt.

**Vorteile:**

*   Einfache Webseitenerstellung, was mir erlaubt, meine Dokumentation schnell und einfach zu veröffentlichen.
*   Schnelle Aktualisierung, was mir ermöglicht, Änderungen in Echtzeit zu sehen.
*   Konsistentes Layout, was eine professionelle und einheitliche Darstellung meiner Dokumentation sicherstellt.
*   Offline-Vorschau, was mir erlaubt, meine Dokumentation zu überprüfen, bevor ich sie veröffentliche.

### 6. Github Pages

> [!info] Github Pages für das Hosting
> [Github Pages](Github%20Pages.md) ist ein kostenloser Hosting-Service von Github, der es mir ermöglicht, meine Webseite einfach online zu veröffentlichen.

**Vorteile:**

*   Kostenfreies Hosting, was es mir ermöglicht, meine Dokumentation ohne zusätzliche Kosten zu veröffentlichen.
*   Einfache Veröffentlichung, was mir die technische Umsetzung der Veröffentlichung abnimmt.
*   Zuverlässig, was mir die Gewissheit gibt, dass meine Dokumentation jederzeit verfügbar ist.

### 7. MkDocs-Material

> [!info] MkDocs-Material als Theme
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) ist ein Theme für MkDocs, das ein modernes und ansprechendes Layout bietet.

**Vorteile:**

*   Modernes Design, was meine Dokumentation professionell und zeitgemäß aussehen lässt.
*   Anpassbar, was mir erlaubt, das Layout an meine spezifischen Bedürfnisse anzupassen.
*   Benutzerfreundlich, was mir die Nutzung der Dokumentation erleichtert.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher als Plugin-Sammlung  
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) ist eine Sammlung von MkDocs Plugins, die die Zusammenarbeit mit Obsidian vereinfachen und zusätzliche Funktionen bieten.

**Vorteile:**

- **Vereinfachte Obsidian-Integration:** Automatisches anpassen von Obsidians Markdown Syntax (Callouts, Wikilinks etc.)
- **Erweiterte Metadaten:** Integration von Tags und Kategorien aus Obsidian-Frontmatter.

## Workflow

> [!info] Mein Workflow
> Hier ist mein typischer Workflow:

1.  Ich erstelle und bearbeite Markdown-Dateien mit einem Texteditor (optional Obsidian).
2.  Ich speichere die Markdown-Dateien lokal.
3.  Ich übertrage meine Änderungen auf das Git-Repository mit Github Desktop.
4.  Ich lasse automatisch die Webseite mit MkDocs erstellen.
5.  Ich veröffentliche die Webseite mit Github Pages.

## Dateisystem

> [!info] Verzeichnisstruktur
> Hier ist die Verzeichnisstruktur meines Systems:
>
> ```
>/docs/     (Hier liegen meine Markdown-Dateien)
>/site/     (Hier wird die Webseite generiert)
>license    (Lizenzinformationen)
>mkdocs.yml (Konfigurationsdatei für MkDocs)
>readme.md  (Datei zur Beschreibung des Repositories)
>```

## Alternativen zur Inhaltserstellung

> [!info] Alternativen für die Inhaltserstellung
> Ich bin mir bewusst, dass nicht jeder mit Markdown und Git vertraut ist. Daher biete ich folgende Alternativen an:

1.  **Wordpress:** Inhalte können in Wordpress als Seite erstellt werden.
2.  **Textdatei, Word-Datei:** Inhalte können als Textdatei, Word-Datei (oder in anderen typischen Formaten) erstellt werden.

In diesen Fällen kann ich die Inhalte dann in das System einpflegen.
