---
lang: en
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki, and Beyond
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T19:19:52+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:09+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki, and Beyond**  
**Why I started this project, the ideas behind it, and where it might lead.**

In 2013, I was working as a project manager for a youth circus. Trainers would often approach me asking if I knew any other games, methods, or tricks. At the time, I had a wealth of resources—books, magazines, notes from workshops—but everything was disorganized and barely digitized.  
<!-- more -->
My first attempt to make these resources accessible to the trainers was a classic wiki. Many of the game descriptions you see today originated from that period. Simultaneously, I began digitizing my sources. I discovered Niklas Luhmann’s *Zettelkasten* (slip-box) method and started organizing my data using its principles.  

The wiki was a failure. There was little interaction; the trainers used it a few times, and it was quickly forgotten. My personal Zettelkasten, however, began to grow. While I initially used specialized software, I soon started thinking about how to future-proof this increasingly valuable collection.  

What does that mean? The first wake-up call came when I realized the software I was using was no longer being developed. I had to find new software—and figure out how to migrate my data into it. That’s when I discovered Markdown.  

Markdown is a simple file format—essentially a plain text file—designed to work independently of any specific software. In other words, it’s a widely adopted standard that can be read and edited with the most basic tools.  

The format supported everything I needed: basic text formatting, links, tags, and metadata (e.g., title, author, description, etc.). I found new software that used Markdown and continued building my Zettelkasten. At that point, I had about 600 notes (or files/pages). Later, I switched software again, and the transition was seamless.  

>[!info]  Key Takeaway
>Future-proofing your data means using a simple, widely adopted format that’s independent of specific software.  

## Collaboration and Sharing  

My first attempt at a wiki didn’t work—partly because I failed to inspire others to contribute. Over the years, my personal Zettelkasten grew to over 3,000 notes, many of them on topics like circus pedagogy, games, juggling, and more.  

For a while, I simply made it accessible online, but beyond a few people who knew about it and occasionally looked up game descriptions, there was no real collaboration or broader sharing.  

Now, about 12 years after starting my Zettelkasten, I’m giving it another shot. The goal is to create a shared knowledge base for topics like circus and movement pedagogy, circus arts, and beyond.  

### Key Considerations and Questions  
- **Independence from specific systems**  
- **Simple, easy-to-understand data format**  
- **Utility and target audience**  
- **Structured data**  

Traditional wiki software (or platforms like WordPress) were out of the question because they create dependency on a single system. While this might work in the short or medium term, it’s a clear weakness in the long run.  

Instead, I’m managing the data (as Markdown and image files) independently of how it’s ultimately presented. This ensures that, even in 20 years, the data remains usable. The way it’s displayed or edited might change drastically, but the underlying data stays the same.  

There are countless ways to present the data: as a website, an eBook, a PDF, or even an app. It can be zipped into a file and read or edited offline with a simple text editor. If you want to display it as a WordPress site or wiki, that’s just a matter of importing the data—since it’s structured and easy to read, it’s relatively straightforward to implement (with the right know-how).  

## My Current Solution for the Website  

I’m using MkDocs and the MkDocs-Material theme to generate a static website. There are many programs that create static HTML files from Markdown, but MkDocs is specifically designed for documentation. Many of the features it generates—like full-text search and navigation—are incredibly helpful.  

MkDocs is also a widely used, open-source solution supported by major companies, which ensures it will remain functional at least in the medium term.  

## Collaboration  

The next step is to make this a collaborative effort. I’m exploring ways to invite others to contribute, whether by adding new content, refining existing entries, or suggesting improvements. The goal is to create a living, evolving resource that benefits from collective knowledge and expertise.
