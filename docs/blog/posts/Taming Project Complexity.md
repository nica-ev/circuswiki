---
created: 2025-05-02 04:37:37
update: 2025-05-02 05:03:23
date: 2025-05-02T05:03:00
publish: true
tags: 
title: Taming Project Complexity
description: 
authors:
  - Marc Bielert
---

# Taming Project Complexity
**Versioning the Dev Environment Without Polluting Your Main Repo**

As projects evolve, especially knowledge bases or documentation sites involving multiple tools like MkDocs, Obsidian, custom scripts, and specialized IDEs like Cursor, complexity naturally increases. Integrating these tools creates powerful workflows, but also introduces a new challenge: managing the growing number of configuration files, drafts, scripts, and planning documents that support the core project.

**The Pain Point: When `.gitignore` Isn't Enough**

I recently hit a painful milestone many developers encounter: **losing several hours of work**. The culprit? Files crucial for my development workflow weren't under version control.
<!-- more -->
Like many, I wanted to keep my public-facing GitHub repository clean. For my project "docs-nica", this meant committing only the core Markdown content and the essential MkDocs files needed to build the website. Everything else – my Obsidian vault configuration, Cursor settings, draft translation scripts, task planning notes – was diligently listed in `.gitignore`. This kept the main repo tidy, but it left my vital development scaffolding unprotected.

This wake-up call happened relatively early, thankfully. While working on integrating translation tools and planning the workflow using notes within my project structure, a mishap overwrote significant planning work. Frustrating, yes, but a valuable lesson learned before the stakes got higher.

**Searching for a Solution: The GUI Roadblock**

My first thought was to explore ways to have multiple Git histories within the same project directory, perhaps using nested repositories with different ignore rules. The idea was sound in theory, but I quickly ran into practical issues. GUI tools I rely on, like Cursor and GitHub Desktop, seemed confused by this setup, often defaulting to one repository or failing to recognize the nested structure correctly. While managing this purely via the command line is possible, it wasn't ideal for my preferred workflow.

**A Layered Approach: The "Dev Environment" Repo**

This led me to refine the idea into a layered structure that, while requiring conscious management, seems to solve the core problems and might even offer long-term benefits:

Imagine a top-level directory, let's call it `docs-nica-dev`. This directory acts as the root for my *entire* development environment for this project. Inside it sits the familiar `docs-nica` directory, which is essentially a clone of my "clean" GitHub repository.

Here's the breakdown:

1.  **`docs-nica-dev/` (Outer Repository - Repo 1):**
    *   This is a Git repository initialized at the top level.
    *   It tracks **everything** needed for development: the `docs-nica` subdirectory, IDE configurations (`.vscode/`), potentially Obsidian settings (`.obsidian/` - managed carefully, see below), draft scripts, planning files, etc.
    *   Its `.gitignore` file is minimal but **crucially ignores the inner repository's Git data (`docs-nica/.git/`)**. It also ignores standard temporary files and potentially secrets specific to the dev environment itself.
    *   **Purpose:** Provides version control for the *entire* development setup, acting as a comprehensive backup and state tracker.

2.  **`docs-nica-dev/docs-nica/` (Inner Repository - Repo 2):**
    *   This is a standard Git repository, likely cloned from GitHub. (Let's call the project itself "CircusWiki" for this example).
    *   It contains the core project: the Markdown files (`docs/`), MkDocs configuration (`mkdocs.yml`, themes, essential plugins), and finalized helper scripts.
    *   Its `.gitignore` file excludes local development artifacts like `.obsidian/`, build output (`site/`), environment secrets (`.env`), etc.
    *   **Purpose:** Represents the clean, shareable, and deployable version of the project – the source of truth for the knowledge base itself.

*(Note on `.obsidian`: Since Obsidian expects its `.obsidian` folder in the vault root, it would live inside `docs-nica/.obsidian`. The inner repo ignores it, while the outer repo tracks it.)*

**How This Works in Practice:**

This setup gives me two independent Git histories:

*   **Inner Repo (`docs-nica`):** Tracks the granular changes to the core content and build configuration. Commits here happen frequently as the knowledge base evolves. This is the repo pushed to the public GitHub project.
*   **Outer Repo (`docs-nica-dev`):** Acts more like a comprehensive snapshot of the development state. When I work on the broader dev environment (e.g., configuring Cursor, drafting complex scripts) or simply want to save the *entire* current state (including the latest changes pulled into or committed within the inner repo), I commit here.

This avoids the need for immediate double-commits. Changes made and committed frequently in the inner repo are simply seen as file modifications by the outer repo, ready to be included in its next "snapshot" commit.

**The Benefits:**

This layered approach achieves two key goals:

1.  **Complete Versioning:** All my crucial development files, notes, configurations, and drafts are now safely under version control in the outer repository, preventing the kind of data loss I experienced.
2.  **Optional Workflow Sharing:** The outer repository (`docs-nica-dev`) *could* potentially be shared (perhaps privately or as a separate public project), allowing someone else to replicate my entire development setup, tools, and workflows, or at least use it as a starting point.

**Setting Boundaries:**

It's important to define the roles clearly. The inner repository (`docs-nica`) remains the single source of truth for the "CircusWiki" knowledge base – the "official" project. This is the only repository intended for collaboration or direct contributions to the content itself. The outer repository (`docs-nica-dev`) is primarily for *my* development backup and workflow capture; I wouldn't accept external contributions there, though others might find it useful to clone.

**Conclusion:**

Is this setup perfect? It requires managing two repositories and a conscious workflow for committing and occasionally syncing states between them. However, it directly solves the critical problem of versioning *everything* necessary for a complex development process without compromising the cleanliness of the main project repository or fighting GUI tools with standard nested repos. For projects that outgrow simple `.gitignore` strategies, this layered approach offers a pragmatic path forward, providing safety and structure for the inevitable, messy reality of development work.

