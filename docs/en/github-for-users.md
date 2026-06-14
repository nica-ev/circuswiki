---
lang: en
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: Contribute directly to the repository on GitHub
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:30:57+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:15+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] In a Nutshell
> This page is for people who want to work directly with the Markdown files of CircusWiki. You don't need this method for regular contributions: you can also simply send material via email.

Direct collaboration via GitHub is practical if you want to regularly correct pages, create new Markdown files, or work with the CircusWiki vault in an editor like Obsidian.

If you only want to contribute a game, a method, a PDF, a link, or a correction, the simpler method is usually better:

[Back to Contribute](mitmachen.md){ .md-button }

## What You Need

- A free GitHub account: [https://github.com/join](https://github.com/join)
- Optionally, GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- A text editor for Markdown files, for example Obsidian, VS Code, or a simple editor

GitHub Desktop is not mandatory, but it's easier for many people than using the command line.

## Finding the Repository

The public repository is located here:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

This is where the actual Markdown files, images, translations, and tools are stored, from which the website is built.

## Workflow in Brief

The typical process is:

1. Fork the repository on GitHub.
2. Clone your copy to your own computer.
3. Make changes in a new branch.
4. Edit files or create new Markdown files.
5. Commit changes.
6. Upload the branch to GitHub.
7. Open a Pull Request so the changes can be reviewed and merged.

## Step-by-Step with GitHub Desktop

### 1. Fork the Repository

Open the CircusWiki repository on GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Click `Fork`. This creates your own copy of the repository in your GitHub account. You can work in this copy without directly altering the main project.

### 2. Clone the Repository

Open GitHub Desktop and select:

```text
File -> Clone repository...
```

Choose your fork of `nica-ev/circuswiki` and specify a folder on your computer.

After this, you will have a local copy of the files.

### 3. Create a Branch

It's best to create a separate branch for your changes, for example:

```text
add-game-description
fix-link
new-balancing-method
```

A branch keeps your work separate from the main codebase. This makes the later review process easier.

### 4. Edit Files

The public content is primarily located in the language folders under `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

All languages are treated equally. There is no primary language in which new content must fundamentally originate.

If you are creating a new original page, place it in the language folder corresponding to the language of the text. For example, an original Spanish text belongs in `docs/es/`, an original German in `docs/de/`, and an original English in `docs/en/`.

The front matter at the beginning of the file is important. It must indicate that the page is an original, for example:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` should correspond to the language of the original text. From this original, translations into all supported languages can be automatically generated later.

When editing, pay attention to the following:

- Do not delete the front matter at the beginning of the file.
- For new original pages, set `translation_status: original` and the appropriate `translation_source_lang`.
- Preserve existing links as much as possible.
- Do not publish private data, API keys, or internal notes.
- Only use images if the usage rights are clear.
- Make small, clear changes rather than very large, mixed changes.

### 5. Commit Changes

In GitHub Desktop, you will see your changed files in the `Changes` section.

Write a brief summary, for example:

```text
Correct material list in movement game
Add safety note for Beigoma
Add new game description
```

Then click `Commit to <branch-name>`.

### 6. Upload Changes

Click `Push origin` to upload your branch to GitHub.

### 7. Open a Pull Request

GitHub Desktop or GitHub in your browser will then offer to create a Pull Request.

A Pull Request means: You are proposing your changes for the main repository. The changes will be reviewed, possibly commented on, and then merged or further developed.

## Markdown Basics

Markdown is a simple text format. The most important characters are sufficient for most contributions:

```markdown
# Main Heading
## Section Heading

Normal text with **bold text** and *italic text*.

- List item
- Another list item

[Link text](https://www.example.com)
```

## If Something is Unclear

You don't need to be perfect at direct collaboration via GitHub right away. If you open a Pull Request and something isn't quite right, it can be clarified during the review.

If you only want to contribute content and the technical process seems too complex, simply use the email on the [Contribute page](mitmachen.md).
