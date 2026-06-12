---
lang: de
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub - direkt im Repository mitarbeiten
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: de
---

> [!info] Kurz gesagt
> Diese Seite ist für Menschen gedacht, die direkt an den Markdown-Dateien von CircusWiki arbeiten möchten. Für normale Beiträge brauchst du diesen Weg nicht: Du kannst Material auch einfach per E-Mail schicken.

Die direkte Mitarbeit über GitHub ist praktisch, wenn du regelmäßig Seiten korrigieren, neue Markdown-Dateien anlegen oder mit dem CircusWiki-Vault in einem Editor wie Obsidian arbeiten möchtest.

Wenn du nur ein Spiel, eine Methode, ein PDF, einen Link oder eine Korrektur beitragen möchtest, ist der einfachere Weg meistens besser:

[Zurück zu Mitmachen](mitmachen.md){ .md-button }

## Was du brauchst

- ein kostenloses GitHub-Konto: [https://github.com/join](https://github.com/join)
- optional GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- einen Texteditor für Markdown-Dateien, zum Beispiel Obsidian, VS Code oder einen einfachen Editor

GitHub Desktop ist nicht verpflichtend, aber für viele Menschen einfacher als die Kommandozeile.

## Repository finden

Das öffentliche Repository liegt hier:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Dort liegen die eigentlichen Markdown-Dateien, Bilder, Übersetzungen und Werkzeuge, aus denen die Webseite gebaut wird.

## Arbeitsweise in Kurzform

Der typische Ablauf ist:

1. Repository auf GitHub forken.
2. Deine Kopie auf den eigenen Computer klonen.
3. Änderungen in einem neuen Branch machen.
4. Dateien bearbeiten oder neue Markdown-Dateien anlegen.
5. Änderungen committen.
6. Branch zu GitHub hochladen.
7. Pull Request öffnen, damit die Änderung geprüft und übernommen werden kann.

## Schritt für Schritt mit GitHub Desktop

### 1. Repository forken

Öffne das CircusWiki-Repository auf GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Klicke auf `Fork`. Dadurch entsteht eine eigene Kopie des Repositorys in deinem GitHub-Konto. In dieser Kopie kannst du arbeiten, ohne das Hauptprojekt direkt zu verändern.

### 2. Repository klonen

Öffne GitHub Desktop und wähle:

```text
File -> Clone repository...
```

Wähle deinen Fork von `nica-ev/circuswiki` aus und lege einen Ordner auf deinem Computer fest.

Danach hast du eine lokale Kopie der Dateien.

### 3. Einen Branch anlegen

Lege für deine Änderung am besten einen eigenen Branch an, zum Beispiel:

```text
spiel-beschreibung-ergaenzen
link-korrigieren
neue-methode-balancieren
```

Ein Branch hält deine Arbeit getrennt vom Hauptstand. Das macht die spätere Prüfung einfacher.

### 4. Dateien bearbeiten

Die öffentlichen Inhalte liegen vor allem in den Sprachordnern unter `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Alle Sprachen sind gleichwertig. Es gibt keine Hauptsprache, in der neue Inhalte grundsätzlich entstehen müssen.

Wenn du eine neue Originalseite erstellst, lege sie in dem Sprachordner an, in dessen Sprache der Text geschrieben ist. Ein spanischer Originaltext gehört zum Beispiel nach `docs/es/`, ein deutscher nach `docs/de/`, ein englischer nach `docs/en/`.

Wichtig ist das Frontmatter am Anfang der Datei. Dort muss erkennbar sein, dass die Seite ein Original ist, zum Beispiel:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` entspricht dabei der Sprache des Originaltexts. Aus diesem Original können später automatisch Übersetzungen in alle unterstützten Sprachen erzeugt werden.

Achte beim Bearbeiten auf Folgendes:

- Frontmatter am Anfang der Datei nicht löschen.
- Bei neuen Originalseiten `translation_status: original` und die passende `translation_source_lang` setzen.
- Bestehende Links möglichst erhalten.
- Keine privaten Daten, API-Schlüssel oder internen Notizen veröffentlichen.
- Bilder nur verwenden, wenn die Nutzungsrechte klar sind.
- Lieber kleine, klare Änderungen machen als sehr große Mischänderungen.

### 5. Änderungen committen

In GitHub Desktop siehst du deine geänderten Dateien im Bereich `Changes`.

Schreibe eine kurze Zusammenfassung, zum Beispiel:

```text
Korrigiere Materialliste im Bewegungsspiel
Ergänze Sicherheitshinweis zu Beigoma
Füge neue Spielbeschreibung hinzu
```

Klicke dann auf `Commit to <branch-name>`.

### 6. Änderungen hochladen

Klicke auf `Push origin`, um deinen Branch zu GitHub hochzuladen.

### 7. Pull Request öffnen

GitHub Desktop oder GitHub im Browser bietet danach an, einen Pull Request zu erstellen.

Ein Pull Request bedeutet: Du schlägst deine Änderung für das Hauptrepository vor. Die Änderung wird geprüft, eventuell kommentiert und dann übernommen oder weiterbearbeitet.

## Markdown-Grundlagen

Markdown ist ein einfaches Textformat. Die wichtigsten Zeichen reichen für die meisten Beiträge:

```markdown
# Große Überschrift
## Abschnittsüberschrift

Normaler Text mit **fetter Stelle** und *kursiver Stelle*.

- Listenpunkt
- Noch ein Listenpunkt

[Linktext](https://www.example.com)
```

## Wenn etwas unklar ist

Direkte Mitarbeit über GitHub muss man nicht sofort perfekt können. Wenn du einen Pull Request öffnest und etwas noch nicht stimmt, kann das im Review geklärt werden.

Wenn du nur Inhalt beitragen möchtest und der technische Weg zu aufwendig wirkt, nutze einfach die E-Mail auf der [Mitmachen-Seite](mitmachen.md).
