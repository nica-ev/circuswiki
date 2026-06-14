---
lang: it
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: Collaborare direttamente nel repository GitHub
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:17+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:16+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] In sintesi
> Questa pagina è pensata per chi desidera lavorare direttamente sui file Markdown di CircusWiki. Per contributi normali non è necessario questo percorso: puoi anche semplicemente inviare materiale via e-mail.

La collaborazione diretta tramite GitHub è utile se desideri correggere regolarmente pagine, creare nuovi file Markdown o lavorare con il vault di CircusWiki in un editor come Obsidian.

Se desideri contribuire solo con un gioco, un metodo, un PDF, un link o una correzione, il percorso più semplice è spesso quello migliore:

[Torna a Contribuisci](mitmachen.md){ .md-button }

## Cosa ti serve

- Un account GitHub gratuito: [https://github.com/join](https://github.com/join)
- Opzionale GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- Un editor di testo per file Markdown, ad esempio Obsidian, VS Code o un editor semplice

GitHub Desktop non è obbligatorio, ma per molte persone è più semplice della riga di comando.

## Trovare il repository

Il repository pubblico si trova qui:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Qui si trovano i file Markdown effettivi, le immagini, le traduzioni e gli strumenti da cui viene costruito il sito web.

## Come funziona in breve

Il flusso tipico è:

1. Effettuare un fork del repository su GitHub.
2. Clonare la propria copia sul computer locale.
3. Apportare modifiche in un nuovo branch.
4. Modificare i file o creare nuovi file Markdown.
5. Effettuare il commit delle modifiche.
6. Caricare il branch su GitHub.
7. Aprire una Pull Request, in modo che la modifica possa essere revisionata e integrata.

## Passo dopo passo con GitHub Desktop

### 1. Effettuare il fork del repository

Apri il repository di CircusWiki su GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Fai clic su `Fork`. Questo creerà una copia personale del repository nel tuo account GitHub. In questa copia puoi lavorare senza modificare direttamente il progetto principale.

### 2. Clonare il repository

Apri GitHub Desktop e seleziona:

```text
File -> Clone repository...
```

Scegli il tuo fork di `nica-ev/circuswiki` e specifica una cartella sul tuo computer.

Successivamente, avrai una copia locale dei file.

### 3. Creare un branch

È meglio creare un branch separato per la tua modifica, ad esempio:

```text
aggiungere-descrizione-gioco
correggere-link
nuovo-metodo-equilibrio
```

Un branch mantiene il tuo lavoro separato dallo stato principale. Questo semplifica la revisione successiva.

### 4. Modificare i file

I contenuti pubblici si trovano principalmente nelle cartelle delle lingue sotto `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Tutte le lingue sono equivalenti. Non esiste una lingua principale in cui i nuovi contenuti debbano essere creati di default.

Se crei una nuova pagina originale, inseriscila nella cartella della lingua in cui è scritto il testo. Un testo originale in spagnolo, ad esempio, va in `docs/es/`, uno tedesco in `docs/de/`, uno inglese in `docs/en/`.

È importante il frontmatter all'inizio del file. Lì deve essere riconoscibile che la pagina è un originale, ad esempio:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` corrisponde alla lingua del testo originale. Da questo originale, le traduzioni in tutte le lingue supportate possono essere generate automaticamente in seguito.

Presta attenzione a quanto segue durante la modifica:

- Non eliminare il frontmatter all'inizio del file.
- Per le nuove pagine originali, imposta `translation_status: original` e la `translation_source_lang` appropriata.
- Conserva i link esistenti quando possibile.
- Non pubblicare dati privati, chiavi API o note interne.
- Utilizza immagini solo se i diritti di utilizzo sono chiari.
- Preferisci apportare modifiche piccole e chiare piuttosto che modifiche miste molto grandi.

### 5. Effettuare il commit delle modifiche

In GitHub Desktop, vedrai i tuoi file modificati nell'area `Changes`.

Scrivi un breve riassunto, ad esempio:

```text
Correggi lista materiali nel gioco di movimento
Aggiungi avviso di sicurezza per Beigoma
Aggiungi nuova descrizione del gioco
```

Quindi fai clic su `Commit to <branch-name>`.

### 6. Caricare le modifiche

Fai clic su `Push origin` per caricare il tuo branch su GitHub.

### 7. Aprire una Pull Request

GitHub Desktop o GitHub nel browser offriranno quindi la possibilità di creare una Pull Request.

Una Pull Request significa: proponi la tua modifica al repository principale. La modifica verrà revisionata, eventualmente commentata e poi integrata o ulteriormente elaborata.

## Fondamenti di Markdown

Markdown è un formato di testo semplice. I caratteri più importanti sono sufficienti per la maggior parte dei contributi:

```markdown
# Titolo principale
## Titolo di sezione

Testo normale con **enfasi in grassetto** e *enfasi in corsivo*.

- Punto elenco
- Un altro punto elenco

[Testo del link](https://www.example.com)
```

## Se qualcosa non è chiaro

Non è necessario essere subito perfetti nella collaborazione diretta tramite GitHub. Se apri una Pull Request e qualcosa non è ancora corretto, può essere chiarito nella revisione.

Se desideri contribuire solo con contenuti e il percorso tecnico ti sembra troppo complicato, utilizza semplicemente l'e-mail sulla [pagina Contribuisci](mitmachen.md).
