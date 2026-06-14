---
lang: en
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Documentation System
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T19:22:24+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:06+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian Setup](Obsidian%20Setup.md){ .md-button }
## System Architecture

The General Idea
> [!info] Architecture Overview
>
> Here is a graphical representation of the system architecture:
>```mermaid
>flowchart LR
>A(Content) --> B(Version Control)
>C(Editing Software) --> A
>A --> D(Make Accessible Online)
>```

In Detail:

> [!info] Architecture Overview
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
> *   **Obsidian:** An optional, but recommended text editor for working with Markdown files.
> *   **Files:** The Markdown files containing the content of my documentation.
> *   **Github Desktop:** A tool for easily managing my Git repositories.
> *   **Github:** An online service for version control and collaboration.
> *   **Github Pages:** A free service for publishing my website.
> *   **MkDocs:** A tool for automatically building the website from my Markdown files.
> *   **MkDocs-Material:** A theme for MkDocs that provides a modern and appealing layout.
> *   **MkDocs-Publisher:** A collection of plugins that simplifies collaboration with Obsidian and offers additional functionality.

## Components in Detail

### 1. Markdown

> [!info] Markdown as the Foundation
> I use the [Markdown format](Markdown.md) for my documentation. Markdown is a simple markup language that allows me to format text with basic styling (e.g., headings, lists, links).

**Advantages:**

*   It's easy to learn and use, allowing me to focus on the content.
*   It's platform-independent, so I can continue my work on any device.
*   It's ideal for version control, enabling me to track and manage changes.
*   It's future-proof and not proprietary, giving me confidence that my work will remain accessible long-term.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian as a Text Editor
> [Obsidian](Obsidian%20Setup.md) is an optional, but recommended text editor. It offers me the following benefits:

*   I can store my data locally and edit it offline, providing flexibility and control.
*   I can easily link and connect files, helping me organize complex information.
*   I can tag and manage files easily, offering an additional dimension of organization.
*   I can visualize my data graphically, helping me identify patterns and relationships.
*   I can extend Obsidian's functionality with plugins, allowing me to tailor the tool to my specific needs.

### 3. Git and Github

> [!info] Git for Version Control
> [Git](https://git-scm.com/) is a version control system that allows me to track and manage changes to the documentation. [Github](https://github.com/) is an online service that enables me to store my Git repositories and collaborate with others.

**Advantages:**

*   Version Control: Every change is documented and can be traced back at any time, helping me avoid errors and maintain an overview.
*   Collaboration: Multiple people can work on the documentation simultaneously, allowing me to integrate feedback and contributions from others.
*   Backup: My documentation is secure and regularly backed up, giving me the assurance that my work will not be lost.

### 4. Github Desktop

> [!info] Github Desktop as a Tool
> [Github Desktop](../_inbox/Github%20Desktop.md) is a graphical interface for Git, allowing me to use Git easily without the command line.

**Advantages:**

*   Simple to use, making Git accessible.
*   No command-line knowledge required, saving time and effort.
*   Streamlines my workflow, allowing me to focus on content creation.

### 5. MkDocs

> [!info] MkDocs as a Website Generator
> [MkDocs](https://mkdocs.org) is a static site generator that converts my Markdown files into a static website.

**Advantages:**

*   Easy website creation, allowing me to publish my documentation quickly and simply.
*   Fast updates, enabling me to see changes in near real-time.
*   Consistent layout, ensuring a professional and uniform presentation of my documentation.
*   Offline preview, allowing me to review my documentation before publishing.

### 6. Github Pages

> [!info] Github Pages for Hosting
> [Github Pages](../_inbox/Github%20Pages.md) is a free hosting service from Github that allows me to easily publish my website online.

**Advantages:**

*   Free hosting, enabling me to publish my documentation at no additional cost.
*   Simple publishing, handling the technical aspects of deployment for me.
*   Reliable, ensuring my documentation is always available.

### 7. MkDocs-Material

> [!info] MkDocs-Material as a Theme
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) is a theme for MkDocs that offers a modern and appealing layout.

**Advantages:**

*   Modern design, making my documentation look professional and contemporary.
*   Customizable, allowing me to adapt the layout to my specific needs.
*   User-friendly, making the documentation easy to navigate.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher as a Plugin Collection
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) is a collection of MkDocs plugins that simplify collaboration with Obsidian and provide additional features.

**Advantages:**

*   **Simplified Obsidian Integration:** Automatically adapts Obsidian's Markdown syntax (callouts, wikilinks, etc.).
*   **Enhanced Metadata:** Integrates tags and categories from Obsidian frontmatter.

## Workflow

> [!info] My Workflow
> Here is my typical workflow:

1.  I create and edit Markdown files using a text editor (optionally Obsidian).
2.  I save the Markdown files locally.
3.  I push my changes to the Git repository using Github Desktop.
4.  The website is automatically built using MkDocs.
5.  I publish the website using Github Pages.

## File System

> [!info] Directory Structure
> Here is the directory structure of my system:
>
> ```
>/docs/     (My Markdown files are located here)
>/site/     (The website is generated here)
>license    (License information)
>mkdocs.yml (Configuration file for MkDocs)
>readme.md  (File describing the repository)
>```

## Alternatives for Content Creation

> [!info] Alternatives for Content Creation
> I am aware that not everyone is familiar with Markdown and Git. Therefore, I offer the following alternatives:

1.  **Wordpress:** Content can be created as a page in Wordpress.
2.  **Text File, Word Document:** Content can be created as a text file, Word document (or in other typical formats).

In these cases, I can then integrate the content into the system.
