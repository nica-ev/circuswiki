function translationStatusLabel(status) {
  return {
    "original": "original",
    "machine-translated": "machine translated",
    "needs-review": "needs review",
    "missing-translation": "translation missing",
  }[status] || "Translation status";
}

function translationStatusDetails(group, language, entry) {
  var sourceLang = entry.source_lang || group.source_lang || "";
  var sourceEntry = group.languages && sourceLang ? group.languages[sourceLang] : null;
  var sourcePath = entry.source || (sourceEntry && sourceEntry.path) || "";
  var authors = entry.authors && entry.authors.length ? entry.authors.join(", ") : "";
  var lines = [
    "Status: " + translationStatusLabel(entry.status),
    "Language: " + (language || entry.source_lang || "unknown"),
  ];

  if (entry.path) {
    lines.push("File: " + entry.path);
  }

  if (authors) {
    lines.push("Author: " + authors);
  }

  if (sourceLang) {
    lines.push("Source language: " + sourceLang);
  }

  if (sourcePath) {
    lines.push("Source file: " + sourcePath);
  }

  if (entry.model) {
    lines.push("Model: " + entry.model);
  }

  if (entry.updated) {
    lines.push("Updated: " + entry.updated);
  }

  if (entry.fallback) {
    lines.push("This is a fallback page; a dedicated translation is missing.");
  }

  return lines.join("\n");
}

function findCurrentTranslationEntry(map, path) {
  if (!map || !map.groups) {
    return null;
  }

  var normalizedCurrent = normalizedPath(path);
  var groupKeys = Object.keys(map.groups);

  for (var i = 0; i < groupKeys.length; i += 1) {
    var group = map.groups[groupKeys[i]];
    var languages = group.languages || {};
    var languageKeys = Object.keys(languages);

    for (var j = 0; j < languageKeys.length; j += 1) {
      var language = languageKeys[j];
      var entry = languages[language];
      if (entry && normalizedPath(entry.url) === normalizedCurrent) {
        return { group: group, language: language, entry: entry };
      }
    }
  }

  return null;
}

function closeTranslationStatusPopups(except) {
  document.querySelectorAll(".translation-status__badge[aria-expanded='true']").forEach(function(button) {
    if (button === except) {
      return;
    }

    button.setAttribute("aria-expanded", "false");
    var popupId = button.getAttribute("aria-controls");
    var popup = popupId ? document.getElementById(popupId) : null;
    if (popup) {
      popup.hidden = true;
    }
  });
}

function injectTranslationStatusStyles() {
  if (document.getElementById("translation-status-styles")) {
    return;
  }

  var style = document.createElement("style");
  style.id = "translation-status-styles";
  style.textContent = [
    ".translation-status {",
    "  display: flex;",
    "  align-items: center;",
    "  position: relative;",
    "  margin: 0 0 0.45rem;",
    "  padding: 0;",
    "  font-size: 0.58rem;",
    "  line-height: 1;",
    "}",
    ".translation-status__badge {",
    "  display: inline-flex;",
    "  align-items: center;",
    "  width: max-content;",
    "  padding: 0.18rem 0.55rem;",
    "  border: 1px solid color-mix(in srgb, var(--cw-success, #2f6f5e) 48%, transparent);",
    "  border-radius: 999px;",
    "  background: color-mix(in srgb, var(--cw-success, #2f6f5e) 14%, var(--cw-panel-solid, #fffaf0));",
    "  box-shadow: 0 0.08rem 0.28rem color-mix(in srgb, var(--cw-ink, #1f2924) 12%, transparent);",
    "  color: var(--cw-success, #2f6f5e);",
    "  font: inherit;",
    "  font-weight: 700;",
    "  letter-spacing: 0.06em;",
    "  text-transform: uppercase;",
    "  cursor: pointer;",
    "}",
    ".translation-status__badge:hover,",
    ".translation-status__badge:focus-visible {",
    "  background: color-mix(in srgb, var(--cw-success, #2f6f5e) 20%, var(--cw-panel-solid, #fffaf0));",
    "  outline: none;",
    "  box-shadow: 0 0.1rem 0.34rem color-mix(in srgb, var(--cw-ink, #1f2924) 18%, transparent);",
    "}",
    ".translation-status--original .translation-status__badge {",
    "  border-color: color-mix(in srgb, var(--cw-success, #2f6f5e) 44%, transparent);",
    "  color: var(--cw-success, #2f6f5e);",
    "}",
    ".translation-status--machine-translated .translation-status__badge {",
    "  border-color: color-mix(in srgb, var(--cw-accent, #d99b36) 58%, transparent);",
    "  background: color-mix(in srgb, var(--cw-accent, #d99b36) 18%, var(--cw-panel-solid, #fffaf0));",
    "  color: var(--cw-accent, #8a5d12);",
    "}",
    ".translation-status--needs-review .translation-status__badge,",
    ".translation-status--missing-translation .translation-status__badge {",
    "  border-color: color-mix(in srgb, var(--cw-danger, #b94632) 58%, transparent);",
    "  background: color-mix(in srgb, var(--cw-danger, #b94632) 14%, var(--cw-panel-solid, #fffaf0));",
    "  color: var(--cw-danger, #b94632);",
    "}",
    ".translation-status__popup {",
    "  position: absolute;",
    "  z-index: 10;",
    "  top: calc(100% + 0.38rem);",
    "  left: 0;",
    "  width: min(26rem, calc(100vw - 2rem));",
    "  padding: 0.72rem 0.82rem;",
    "  border: 1px solid var(--cw-line, rgba(47, 111, 94, 0.24));",
    "  border-radius: 0.7rem;",
    "  background: var(--cw-panel-solid, #fffaf0);",
    "  box-shadow: 0 0.45rem 1.25rem color-mix(in srgb, var(--cw-ink, #1f2924) 22%, transparent);",
    "  color: var(--cw-ink, var(--md-default-fg-color, #1f2924));",
    "  font-size: 0.68rem;",
    "  line-height: 1.45;",
    "  white-space: pre-wrap;",
    "}",
    ".translation-status__popup[hidden] {",
    "  display: none;",
    "}",
  ].join("\n");
  document.head.appendChild(style);
}

function renderTranslationStatus() {
  var content = document.querySelector("article.md-content__inner");
  if (!content) {
    return;
  }

  loadTranslationMap(currentLanguageRootPath()).then(function(map) {
    var current = findCurrentTranslationEntry(map, window.location.pathname);
    if (!current) {
      return;
    }

    injectTranslationStatusStyles();

    var existing = content.querySelector(":scope > .translation-status");
    if (existing) {
      existing.remove();
    }

    var banner = document.createElement("aside");
    var status = current.entry.status || "unknown";
    banner.className = "translation-status translation-status--" + status;
    banner.setAttribute("aria-label", "Translation status");

    var details = translationStatusDetails(current.group, current.language, current.entry);
    var popupId = "translation-status-popup";

    var badge = document.createElement("button");
    badge.type = "button";
    badge.className = "translation-status__badge";
    badge.textContent = translationStatusLabel(status);
    badge.title = details;
    badge.setAttribute("aria-label", "Show translation metadata");
    badge.setAttribute("aria-expanded", "false");
    badge.setAttribute("aria-controls", popupId);

    var popup = document.createElement("div");
    popup.id = popupId;
    popup.className = "translation-status__popup";
    popup.setAttribute("role", "dialog");
    popup.setAttribute("aria-label", "Translation metadata");
    popup.hidden = true;
    popup.textContent = details;

    badge.addEventListener("click", function(event) {
      event.stopPropagation();
      var isOpen = badge.getAttribute("aria-expanded") === "true";
      closeTranslationStatusPopups(isOpen ? null : badge);
      badge.setAttribute("aria-expanded", isOpen ? "false" : "true");
      popup.hidden = isOpen;
    });

    badge.addEventListener("keydown", function(event) {
      if (event.key === "Escape") {
        closeTranslationStatusPopups();
        badge.focus();
      }
    });

    banner.appendChild(badge);
    banner.appendChild(popup);
    content.insertBefore(banner, content.firstChild);
  });
}

document.addEventListener("click", function() {
  closeTranslationStatusPopups();
});

if (typeof document$ !== "undefined") {
  document$.subscribe(renderTranslationStatus);
} else {
  document.addEventListener("DOMContentLoaded", renderTranslationStatus);
}
