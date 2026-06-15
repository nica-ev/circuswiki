import { checkDynamicPages as checkDynamicPagesApi, previewDynamicPage, refreshDynamicPages, scanDynamicPages } from "../api/dynamic.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, pathWithObsidianButton, jsonText } from "../core/html.js";

let context = {
};
const busyControls = ["dynamic-scan", "dynamic-check", "dynamic-preview", "dynamic-refresh-selected", "dynamic-refresh-all"];
let scanResult = null;
let selectedPath = null;
let eventScope = createEventScope();

export function mountDynamicPagesFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("dynamic-scan"), "click", () => {
    loadDynamicScan().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-check"), "click", () => {
    checkDynamicPages().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-preview"), "click", () => {
    previewDynamicSelected().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-refresh-selected"), "click", () => {
    refreshDynamicSelected().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-refresh-all"), "click", () => {
    refreshAllDynamicPages().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-language"), "change", () => {
    selectedPath = null;
    loadDynamicScan().catch((error) => dynamicLog(error.message));
  });
  eventScope.listen($("dynamic-filter"), "input", renderDynamicScan);
  renderDynamicScan();
  renderDynamicDetails();
}

export function unmountDynamicPagesFeature() {
  eventScope.clear();
}

export function dynamicLog(value) {
  const log = $("dynamic-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasDynamicScan() {
  return Boolean(scanResult);
}

export function renderDynamicLanguageOptions(config) {
  const select = $("dynamic-language");
  if (!select) {
    return;
  }
  const languages = config.languages || [];
  select.innerHTML = [
    '<option value="">All languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`),
  ].join("");
}

export async function loadDynamicScan() {
  setBusy(true);
  dynamicLog("Scanning dynamic pages...");
  try {
    const language = $("dynamic-language").value || "";
    scanResult = await scanDynamicPages(language);
    if (selectedPath && !scanResult.pages.some((page) => page.path === selectedPath)) {
      selectedPath = null;
    }
    renderDynamicScan();
    dynamicLog(scanResult);
  } catch (error) {
    dynamicLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function checkDynamicPages() {
  setBusy(true);
  dynamicLog("Checking dynamic pages...");
  try {
    const language = $("dynamic-language").value || "";
    const result = await checkDynamicPagesApi(language, selectedPath || "");
    dynamicLog(result);
  } catch (error) {
    dynamicLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewDynamicSelected() {
  await runDynamicRefresh(true, selectedPath || "");
}

async function refreshDynamicSelected() {
  await runDynamicRefresh(false, selectedPath || "");
  await loadDynamicScan();
}

async function refreshAllDynamicPages() {
  await runDynamicRefresh(false, "");
  await loadDynamicScan();
}

async function runDynamicRefresh(dryRun, path) {
  if (path === "" && dryRun) {
    dynamicLog("Select a dynamic page first.");
    return;
  }
  setBusy(true);
  dynamicLog(dryRun ? "Previewing dynamic refresh..." : "Refreshing dynamic pages...");
  try {
    const payload = {
      path,
      language: path ? "" : $("dynamic-language").value,
    };
    const result = dryRun ? await previewDynamicPage(path) : await refreshDynamicPages(payload);
    dynamicLog(result);
  } catch (error) {
    dynamicLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderDynamicScan() {
  if (!$("dynamic-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("dynamic-summary").innerHTML = "";
    $("dynamic-pages").innerHTML = "";
    $("dynamic-details").innerHTML = "";
    return;
  }

  const issueCount = scan.pages.filter((page) => page.issues.length).length;
  const validCount = scan.pages.filter((page) => page.valid_block_count > 0).length;
  $("dynamic-summary").innerHTML = `
    <span class="pill">Pages: <strong>${scan.total}</strong></span>
    <span class="pill green">Refreshable: <strong>${validCount}</strong></span>
    <span class="pill ${issueCount ? "yellow" : "green"}">Issues: <strong>${issueCount}</strong></span>
    <span class="pill ${scan.obsidian?.available ? "green" : "red"}">Obsidian CLI: <strong>${scan.obsidian?.available ? "available" : "missing"}</strong></span>
  `;

  const filter = $("dynamic-filter").value.toLowerCase();
  const pages = scan.pages.filter((page) =>
    `${page.path} ${page.title} ${page.language}`.toLowerCase().includes(filter)
  );
  $("dynamic-pages").innerHTML = "";
  pages.forEach((page) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page";
    if (selectedPath === page.path) {
      button.classList.add("active");
    }
    button.textContent = `${page.language || "?"} | ${page.title}`;
    button.title = page.path;
    button.addEventListener("click", () => {
      selectedPath = page.path;
      renderDynamicScan();
      dynamicLog(page);
    });
    $("dynamic-pages").appendChild(button);
  });
  renderDynamicDetails();
}

function renderDynamicDetails() {
  if (!$("dynamic-details")) {
    return;
  }
  const page = scanResult?.pages.find((item) => item.path === selectedPath);
  if (!page) {
    $("dynamic-details").innerHTML = "";
    return;
  }
  const issues = page.issues.length
    ? page.issues.map((issue) => `<span class="issue">${escapeHtml(issue)}</span>`).join("")
    : '<span class="ok">none</span>';
  $("dynamic-details").innerHTML = `
    <dt>Path</dt><dd>${pathWithObsidianButton(page.path)}</dd>
    <dt>Language</dt><dd>${escapeHtml(page.language || "-")}</dd>
    <dt>Title</dt><dd>${escapeHtml(page.title)}</dd>
    <dt>Blocks</dt><dd>${page.valid_block_count}/${page.block_count} valid</dd>
    <dt>Tags</dt><dd>${escapeHtml(page.tags.join(", ") || "-")}</dd>
    <dt>Issues</dt><dd>${issues}</dd>
  `;
}

function languageLabel(code, name) {
  if (!code) {
    return "";
  }
  if (code === "all") {
    return name || "All target languages";
  }
  if (!name || name === code) {
    return code;
  }
  return `${name} (${code})`;
}

function setBusy(isBusy) {
  setControlsBusy(busyControls, isBusy);
}
