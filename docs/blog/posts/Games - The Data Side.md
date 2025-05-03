---
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:41
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Games - The Data Side
description: How game descriptions were standardized and made more dynamic using metadata and Obsidian plugins.
authors:
  - Marc Bielert
categories: 
  - development
---

# **Games - The Data Side**  
**How game descriptions were standardized and made more dynamic using metadata and Obsidian plugins.**

When it comes to managing content, consistency is key. For the first major section of this project, I tackled the games—about 170 of them, each with its own unique format, style, and accessibility. The problem? Many of these descriptions relied on hard-coded, static links, making it a nightmare to add new games or adjust the structure.  

So, I rolled up my sleeves and got to work.  
<!-- more -->
## Step 1: A Unified Format  
The first order of business was to establish a consistent format for all game descriptions. I drew inspiration from the "Tasifan Spielebuch" (Tasifan Game Book), a well-organized resource for game descriptions. To make things even more user-friendly, I added short summaries so that all the essential details are visible at a glance—even in a preview.  

But the real game-changer? Metadata.  

## Step 2: Metadata Magic  
Now, all the key information—group size, materials, duration, and more—is stored as metadata at the top of each Markdown file in a format called YAML (or frontmatter). This not only keeps things organized but also makes the data reusable across the system.  

To make finding the right game easier, I implemented a simple yet effective logic:  
1. **Choose a category**: What kind of game are you looking for? A cool-down game? A tag game? Something for team-building? I’ve created a set of categories to start with, but these can be tweaked or expanded as needed.  
2. **Browse the table**: Once you’ve picked a category, you’ll see a table listing all the games that fit. The table is sortable—just click the headers to organize by duration, difficulty, or other criteria.  

And here’s the kicker: many games appear in multiple categories, so you’re never limited to just one way of finding what you need.  

## Not-Quite-Dynamic Tables  
The real magic happens with two Obsidian plugins: **Dataview** and **Dataview Serializer**.  

Dataview lets me create dynamic lists and tables using database-like queries. The catch? These tables only work within Obsidian because the underlying Markdown files aren’t modified.  

Enter Dataview Serializer. This plugin converts those dynamic tables into static Markdown format and writes them directly into the file. When the site is built using MkDocs, the tables are static but were essentially generated dynamically offline.  

These queries can get pretty complex, allowing me to search or display specific parts of the wiki—like all game descriptions or articles written by a specific author. And because they update automatically (via the serializer step), adding new information and building a navigable structure is a breeze.  

But it’s not all sunshine and rainbows. The process isn’t fully automatic. Dataview Serializer can only rewrite a file if it’s open in Obsidian. For now, this is manageable—I’ve tagged every page with a dynamic table or list, making it easy to cycle through them. But if the number of these pages grows significantly, I might need to rethink the approach.  

## Tools and Language Models  
The original game descriptions were a mixed bag in terms of formatting and quality. To streamline the process, I turned to language models (LLMs). I crafted a specific prompt, complete with example formatting, to ensure the content itself wasn’t altered (no unnecessary rewrites). Still, I manually reviewed each result and made small adjustments where needed.  

Here’s the takeaway: when used correctly, these tools are *incredibly* powerful. The key is to be precise and intentional in how you frame your tasks.  

The final changes are mostly about formatting—how the information and game descriptions are presented. The metadata, however, was all entered manually. Since I had to double-check everything anyway, doing it by hand was faster in this case.  

It’s a slow process, though. Working on it part-time, I manage about 10-15 games per day. Progress is steady, but it’s going to take a while.  

## Challenges Ahead  
One potential hurdle is translations. Search queries would need to be adapted to find language-specific versions of games or tags. For now, this can be handled manually, but if the system grows, automation might be necessary.  

Translation is a complex topic, and I’ll dive deeper into it another time.  

## Why Bother?  
The short answer? Scalability.  

This system is designed to grow. By standardizing the format, leveraging metadata, and using dynamic tools, I’ve created a foundation that can handle more content without becoming unwieldy.  

## What Else is New?  
The search function has gotten a few upgrades:  
- **Autocomplete**: As you type, the search suggests queries that yield the most hits. This isn’t based on user behavior—we don’t track searches—but on the static search index generated when the site is built.  
- **Saved searches**: Click a small icon next to the search bar, and your query (and results) are saved in the URL. Bookmark it, and you’ll get the same results every time.  

It’s a small feature, but it could become incredibly useful as the wiki grows and covers more diverse topics.  
