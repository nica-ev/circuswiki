export function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

export function jsonText(value) {
  return typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

export function pathWithObsidianButton(path) {
  if (!path) {
    return "-";
  }
  const escaped = escapeHtml(path);
  return `
    <span class="path-action">
      <span>${escaped}</span>
      <button class="mini-button obsidian-open" type="button" data-obsidian-path="${escaped}">Open in Obsidian</button>
    </span>
  `;
}
