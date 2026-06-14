---
lang: it
translation_id: obsidian-setup
publish: true
tags: 
title: Configurazione Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:07:36+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:20+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian è estremamente personalizzabile, il che può rappresentare un problema per i nuovi utenti.
Forniamo una configurazione di base che può essere utilizzata così com'è, includendo plugin e temi, oltre alle loro impostazioni ottimizzate.
Questa è una configurazione di base e può essere ulteriormente personalizzata secondo le preferenze individuali.
Forniamo semplicemente una soluzione funzionante, che documenteremo e spiegheremo qui.

## Termini utilizzati
**Vault** - una raccolta di file markdown e immagini che costituiscono la base di conoscenza

## Plugin

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
Offre accesso a molte nuove funzionalità e opzioni di stile per Canvas.

### BRAT
Necessario per installare plugin non ufficiali / plugin non registrati nell'ecosistema di Obsidian, ovvero:
- Dataview Serializer
- Sortable

### Better Word Count
Utilizzato principalmente per la sua capacità di mostrare il numero di parole/caratteri nel testo evidenziato.
È visibile nella barra di stato.

### Beautitab
Puramente cosmetico, fornisce una pagina personalizzabile per la "nuova scheda vuota".

### Clear Unused Images
Come dice il nome, aiuta a organizzare il vault identificando le immagini non utilizzate.

❗Ho escluso la sottocartella ```/site/``` in modo che non vengano eliminate sempre le immagini dal sito web generato (il che non è un problema, più un fastidio).

❗Attenzione all'uso del comando "clear attachments", poiché questo eliminerà sempre ```mkdocs.yml``` e la ```license.``` --> se ciò accade, i file si trovano nella cartella .trash e possono essere recuperati. Ma è facile che sfuggano.

### Dataview
Abilita query simili a SQL sul vault.

### Dataview Serializer
Trasforma i risultati di Dataview in markdown.
Aiuta a riutilizzare i risultati delle query di Dataview nelle note effettive.

### Emoji Toolbar
Beh, offre un facile accesso alle emoji.
**Scorciatoia impostata su: ALT-E**
😍

### Linter
Pulisce i file markdown e i dati frontmatter.
Aiuta a mantenere una forma coerente.

### Note Toolbar
Abilita barre degli strumenti personalizzabili in cima a una nota che possono essere definite a livello di cartella/file.

### Tag Wrangler
Offre opzioni aggiuntive per lavorare con i tag.
- rinominare i tag
Aiuta a organizzare il vault.

### Templater
Consente modelli personalizzabili che possono essere inseriti manualmente o in base a condizioni (come la creazione di una nota).

### Status Bar Organizer
Consente di nascondere elementi dalla barra di stato.

### Sortable
Consente l'ordinamento delle tabelle (sia markdown che dataview) facendo clic sulle loro intestazioni.

### Workspaces Plus
Consente un rapido cambio di workspace dalla barra di stato.

## File System del Vault

[File System del Vault](Vault%20File%20System.md){ .md-button }
