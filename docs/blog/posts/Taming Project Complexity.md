---
created: 2025-05-02 04:37:37
update: 2025-05-03 01:14:21
date: 2025-05-03T11:00:00
publish: true
tags: []
title: Taming Project Complexity - The Saga
description: The journey to effectively version a complex dev environment without polluting the main project repository.
authors:
  - Marc Bielert
---

# Taming Project Complexity - The Saga
**Versioning the Dev Environment Without Polluting Your Main Repo**

As projects evolve, especially knowledge bases or documentation sites involving multiple tools like MkDocs, Obsidian, custom scripts, and specialized IDEs like Cursor, complexity naturally increases. Integrating these tools creates powerful workflows, but also introduces a new challenge: managing the growing number of configuration files, drafts, scripts, and planning documents that support the core project.

## The Pain Point: When `.gitignore` Isn't Enough

I recently hit a painful milestone many developers encounter: **losing several hours of work**. The culprit? Files crucial for my development workflow weren't under version control.
<!-- more -->
Like many, I wanted to keep my public-facing GitHub repository clean. For my project "docs-nica", this meant committing only the core Markdown content and the essential MkDocs files needed to build the website. Everything else – my Obsidian vault configuration, Cursor settings, draft translation scripts, task planning notes – was diligently listed in `.gitignore`. This kept the main repo tidy, but it left my vital development scaffolding unprotected.

This wake-up call happened relatively early, thankfully. While working on integrating translation tools and planning the workflow using notes within my project structure, a mishap overwrote significant planning work. Frustrating, yes, but a valuable lesson learned before the stakes got higher.

## Searching for a Solution: The Failed Attempts

My initial ideas revolved around using Git itself more cleverly, but I ran into roadblocks.

### Attempt 1: Nested Repos - The Branch Switching Nightmare

My first thought was to explore ways to have multiple Git histories within the same project directory, perhaps using nested repositories. The idea was to have a top-level "dev" repository tracking *everything* (IDE settings, drafts, the inner repo's files) while the inner "public" repository contained only the clean, deployable project files. The outer repo would ignore the inner repo's `.git` directory.

In theory, this sounded like a neat layered approach. However, when I actually tried to set this up, I very soon realized this wasn't working. First off, Git doesn't really support nested repos, at least not the way I envisioned it. And it makes sense. There is a caveat that I hadn't thought about: Let's say I am working in the inner repo (`docs-nica`) and switch to a different branch. Now all the files in that folder change (to reflect the branch) - but the outer repo (`docs-nica-dev`) is still on its main branch. The outer repo now sees all these file changes and thinks *they* are changes to *its* main branch... It's clearly visible why this is an issue. Okay, so this approach wasn't working.

### Attempt 2: Separate Repos + Git Hooks - The Copy Catastrophe

Back to the drawing board. My next idea was having two repositories completely separate. A `dev` one that contains everything I need (scripts, notes, configs, *and* the core project files). And a `public` one that only contains the markdown content and the MkDocs setup – just the bare-bones, the way it's intended for deployment.

But here comes the catch: if we change something in the `public` repo (maybe a quick fix directly there, or pulling collaborators' changes), how should the `dev` repo know about this? And more commonly, how do changes in `dev` get reflected in `public`? We need some way to link them.

The first idea was to use GitHub hooks (or local Git hooks). These let you define commands to run after certain Git actions, like a commit. I set up a hook that, after a commit in the `dev` repo, would basically just copy the relevant files (the `docs/` folder, `mkdocs.yml`, etc.) over to the `public` repo directory.

It seemed to work at first glance, but this approach had two main issues:

1.  **Noisy History:** The hook copied *all* relevant files on *each* commit. This meant that the `public` repo always thought that *all* its content had changed. While technically not breaking anything, the commit history became less useful, showing hundreds (or thousands) of files changed in every single commit, making it impossible to instantly pinpoint which file *contents* really changed.
2.  **Deletion Blindness:** The script just *copied* files. If I deleted a file or folder in the `dev` repo, this change wouldn't get reflected in the `public` repo. The old file would just linger there.

Damn, already spent hours on this – and still no working solution.

## The Breakthrough: Separate Repos + File Synchronization

Then I remembered an open-source software that I'd tested a long time ago for syncing local folders: **FreeFileSync**. While it's unfortunate to add another set of tools/software to the stack that's needed, it actually accomplished exactly what I wanted.

The setup now involves:

1.  Two separate Git repositories: `docs-nica-dev` (containing everything) and `docs-nica` (the clean, public version).
2.  **FreeFileSync:** Used to define the rules for how to synchronize the specific folders (like `docs/`, theme files, `mkdocs.yml`) between the two repository locations. It can handle two-way syncs, mirroring, and crucially, propagating deletions correctly.
3.  **RealTimeSync (part of FreeFileSync):** Used to monitor the defined folders for changes and trigger the synchronization automatically based on the FreeFileSync rules.

This combination finally bridges the gap between the two repositories effectively. Changes made in the `dev` repo's core content folders are mirrored to the `public` repo, and vice-versa if needed (though my primary flow is dev -> public). Deletions are handled correctly, and because it syncs only *changed* files, the commit history in the `public` repo accurately reflects actual modifications.

## The Remaining Catch: Sync vs. Commit Timing

There is still one downside, though. When I change a file in the `dev` repo, and RealTimeSync is running, those changes are synced to the `public` repo's directory *immediately*, even if not committed in the `dev` repo yet. The sync solution is decoupled from Git.

It's not a super big deal, but it requires a bit more carefulness when actually committing and pushing changes. Basically, when I work on the `dev` repo, I need to make sure to commit everything there *before* I switch focus to the `public` repo to commit and push. Also, it reinforces the habit of *really reviewing the changes* staged for commit in the `public` repo before actually committing and pushing, just to ensure the state is exactly what I intend it to be.

## Who is This For? (Important Clarification)

Hold on, though – before you think this whole setup is mandatory just to use the wiki, let me clarify. **All this complexity? It's *not* needed if you just want to work with the core content.** The main entry point is still super simple: clone the public `docs-nica` repo (which just has the Markdown files and the MkDocs setup) and use whatever tools *you* prefer. That's it.

So, why did I go through all this trouble? This rather complex dev setup serves two main purposes for *me*:

1.  **My Personal Safety Net:** It's crucial version control for *all* my development bits and pieces – the configurations, the half-finished scripts, the planning notes – stuff I can't afford to lose again.
2.  **Sharing My Exact Workflow (Optionally):** If someone *wants* to replicate my specific environment, they can clone the `docs-nica-dev` repo. They'll get my complete Obsidian setup (plugins, settings, bookmarks, searches, the works!), potentially Cursor settings, and any other integrated tools I've configured. It's a way to share a ready-to-go base setup.

But the fundamental idea hasn't changed: you can absolutely grab just the public repo and build your own workflow around it with your favorite tools. This elaborate dance is about managing *my* development chaos and offering a blueprint for those who want it.

## Conclusion: A Hard-Won Solution

Overall, I am happy that I found a solution to the issue now – even though this did cost me like two days of trial, error, and frustration. But getting this workflow right was crucial to avoid further issues down the line, ensuring both a clean public repository and a fully version-controlled development environment.

Is this setup perfect? It requires managing two repositories and an external synchronization tool, plus a conscious workflow for committing. However, it directly solves the critical problem of versioning *everything* necessary for a complex development process without compromising the cleanliness of the main project repository or fighting Git's limitations with nested structures. For projects that outgrow simple `.gitignore` strategies, this approach offers a pragmatic path forward, providing safety and structure for the inevitable, messy reality of development work.

