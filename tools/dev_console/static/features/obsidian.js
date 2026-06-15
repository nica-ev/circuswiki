import { getObsidianStatus, openInObsidianApi } from "../api/obsidian.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let statusResult = null;
let eventScope = createEventScope();

export function mountObsidianFeature() {
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("obsidian-status-refresh"), "click", () => {
    loadObsidianStatus().catch((error) => obsidianLog(error.message));
  });
  eventScope.listen($("obsidian-open-path"), "click", () => {
    openObsidianPath().catch((error) => obsidianLog(error.message));
  });
  renderObsidianStatus();
}

export function unmountObsidianFeature() {
  eventScope.clear();
}

export function obsidianLog(value) {
  const log = $("obsidian-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasObsidianStatus() {
  return Boolean(statusResult);
}

export async function loadObsidianStatus() {
  obsidianLog("Checking Obsidian CLI...");
  statusResult = await getObsidianStatus();
  renderObsidianStatus();
  obsidianLog(statusResult);
  return statusResult;
}

async function openObsidianPath() {
  const path = $("obsidian-path").value.trim();
  if (!path) {
    obsidianLog("Enter a repository-relative path first.");
    return;
  }
  obsidianLog(`Opening in Obsidian: ${path}`);
  const result = await openInObsidianApi(path);
  obsidianLog(result);
}

function renderObsidianStatus() {
  const summary = $("obsidian-summary");
  if (!summary) {
    return;
  }
  if (!statusResult) {
    summary.innerHTML = '<span class="pill yellow">Status: <strong>not checked</strong></span>';
    return;
  }
  summary.innerHTML = `
    <span class="pill ${statusResult.available ? "green" : "red"}">CLI: <strong>${statusResult.available ? "available" : "missing"}</strong></span>
    <span class="pill">Command: <strong>${escapeHtml(statusResult.command || "-")}</strong></span>
  `;
}
