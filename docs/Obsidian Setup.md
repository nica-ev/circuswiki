---
publish: true
tags: 
title: Obsidian Setup
created: 2025-01-23 01:38:52
update: 2025-03-11 02:05:46
authors:
  - Marc Bielert
---

Obsidian is extremely customizable, wich can be an issue for newcomers.
We provide a base-setup that can be used as is, including plugins and themes aswell as their finetuned settings.
This is a base-setup and can be further tweaked to anyones personal preference.
We provide just a working solution - wich we will document and explain here.

## Terms used
**Vault** - a collection of markdown files and images that form the knowledge base

## Plugins

- Advanced Canvas
- BRAT
- Better Wordcount
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
Gives access to a lot of new functionality and styling options for Canvas

### BRAT
needed to install unofficial plugins / plugins not registered in Obsidians Ecosystem, namely:
- Dataview Serializer
- Sortable

### Better Word Count
Mainly used for its ability to show number of words/characters in highlighted text.
Is visible in status-bar

### Beautitab
Purely cosmetical, gives a customizable "empty new tab" page

### Clear unused Images
as the name says, helps with organizing the vault by identifying unused images

❗I exluded the subfolder ```/site/``` so it doesnt delete always the images from the build website (wich isnt an issue, more of an annoyance)

❗Careful with using the clear attachments command - as this will always delete ```mkdocs.yml``` and the ```license.``` --> if this happens, the files are in the .trash folder and can be recovered. But its easy to miss.

### Dataview
enables SQL like queries on the vault

### Dataview Serializer
turn Dataview results into markdown 
helps with re-using the results of dataview queries in the actual notes

### Emoji Toolbar
well, gives easy access to emojis
**Hotkey set to: ALT-E**
😍

### Linter
cleans up markdown files and frontmatter data
helps with keeping a consistent form

### Note Toolbar
enables customizable toolbars on top of a note that can be defined on a folder/file level

### Tag Wrangler
gives additional options to work with tags
- renaming tags
helps with organizing the vault

### Templater
allows customizable templates that can be inserted manually or based on conditions (like creating a note)

### Status Bar Organizer
Allows to hide items from the status bar

### Sortable
Allows sorting of tables (both markdown aswell as dataview tables) by clicking on their headers.

### Workspaces Plus
Allows for an easy quick-switch from the status bar

## Vault File System

[[Vault File System]]{ .md-button }