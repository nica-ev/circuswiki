---
lang: en
translation_id: obsidian-setup
publish: true
tags: 
title: Obsidian Setup
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:26:00+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:18+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian is highly customizable, which can be a challenge for newcomers.
We provide a base setup that can be used as is, including plugins and themes, along with their finely tuned settings.
This is a foundational setup and can be further adjusted to suit anyone's personal preferences.
We're offering a functional solution that we will document and explain here.

## Terms Used
**Vault** - A collection of Markdown files and images that form the knowledge base.

## Plugins

- Advanced Canvas
- BRAT
- Better Word Count
- Clear Unused Images
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
Provides access to numerous new functionalities and styling options for Canvas.

### BRAT
Required for installing unofficial plugins or plugins not registered in Obsidian's ecosystem, specifically:
- Dataview Serializer
- Sortable

### Better Word Count
Primarily used for its ability to display the word and character count of highlighted text.
This is visible in the status bar.

### Beautitab
Purely cosmetic, it offers a customizable "empty new tab" page.

### Clear Unused Images
As the name suggests, this plugin helps organize the vault by identifying unused images.

❗I've excluded the subfolder ```/site/``` so it doesn't delete images from the built website (which isn't a critical issue, more of an annoyance).

❗Be cautious when using the "Clear Attachments" command, as this will always delete ```mkdocs.yml``` and the ```license.md``` file. If this happens, the files are in the `.trash` folder and can be recovered, but it's easy to overlook.

### Dataview
Enables SQL-like queries on your vault.

### Dataview Serializer
Converts Dataview results into Markdown.
This helps in reusing the results of Dataview queries within your actual notes.

### Emoji Toolbar
Provides easy access to emojis.
**Hotkey set to: ALT-E**
😍

### Linter
Cleans up Markdown files and frontmatter data.
Helps maintain a consistent format.

### Note Toolbar
Enables customizable toolbars at the top of a note, which can be defined at the folder or file level.

### Tag Wrangler
Offers additional options for working with tags, such as renaming tags.
This aids in organizing your vault.

### Templater
Allows for customizable templates that can be inserted manually or based on conditions (like when creating a new note).

### Status Bar Organizer
Allows you to hide items from the status bar.

### Sortable
Enables sorting of tables (both Markdown and Dataview tables) by clicking on their headers.

### Workspaces Plus
Allows for easy quick-switching of workspaces from the status bar.

## Vault File System

[Vault File System](Vault%20File%20System.md){ .md-button }
