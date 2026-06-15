import {
  previewSourceLinkStyle,
  repairAllSafeSourceLinkStylesApi,
  repairSourceLinkStyles,
  scanSourceLinkStyle,
} from "../api/links.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText, pathWithObsidianButton } from "../core/html.js";

let context = {
};
const busyControls = ["source-link-style-scan", "source-link-style-preview", "source-link-style-selected", "source-link-style-all"];
let scanResult = null;
let selectedPath = null;
let checkedPaths = new Set();
let eventScope = createEventScope();

export function mountSourceLinkStyleFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("source-link-style-scan"), "click", () => {
    loadSourceLinkStyleScan().catch((error) => sourceLinkStyleLog(error.message));
  });
  eventScope.listen($("source-link-style-preview"), "click", () => {
    previewSourceLinkStyleSelected().catch((error) => sourceLinkStyleLog(error.message));
  });
  eventScope.listen($("source-link-style-selected"), "click", () => {
    repairSelectedSourceLinkStyles().catch((error) => sourceLinkStyleLog(error.message));
  });
  eventScope.listen($("source-link-style-all"), "click", () => {
    repairAllSafeSourceLinkStyles().catch((error) => sourceLinkStyleLog(error.message));
  });
  eventScope.listen($("source-link-style-language"), "change", () => {
    selectedPath = null;
    checkedPaths.clear();
    loadSourceLinkStyleScan().catch((error) => sourceLinkStyleLog(error.message));
  });
  eventScope.listen($("source-link-style-filter"), "input", renderSourceLinkStyleScan);
  renderSourceLinkStyleScan();
  renderSourceLinkStyleDetails();
}

export function unmountSourceLinkStyleFeature() {
  eventScope.clear();
}

export function sourceLinkStyleLog(value) {
  const log = $("link-repair-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function renderSourceLinkStyleLanguageOptions(config) {
  const select = $("source-link-style-language");
  if (!select) {
    return;
  }
  const languages = config.languages || [];
  select.innerHTML = [
    '<option value="">All source languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`),
  ].join("");
}

export function hasSourceLinkStyleScan() {
  return Boolean(scanResult);
}

export async function loadSourceLinkStyleScan() {
  setBusy(true);
  sourceLinkStyleLog("Scanning original source link styles...");
  try {
    const language = $("source-link-style-language").value || "";
    scanResult = await scanSourceLinkStyle(language);
    const currentPaths = new Set(scanResult.items.map((item) => item.path));
    checkedPaths = new Set([...checkedPaths].filter((path) => currentPaths.has(path)));
    if (selectedPath && !currentPaths.has(selectedPath)) {
      selectedPath = null;
    }
    renderSourceLinkStyleScan();
    sourceLinkStyleLog(scanResult);
  } catch (error) {
    sourceLinkStyleLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewSourceLinkStyleSelected() {
  if (!selectedPath) {
    sourceLinkStyleLog("Select a source style item first.");
    return;
  }
  setBusy(true);
  sourceLinkStyleLog("Previewing source link style repair...");
  try {
    const result = await previewSourceLinkStyle(selectedPath);
    sourceLinkStyleLog({
      ...result,
      current_body: result.current_body.slice(0, 4000),
      repaired_body: result.repaired_body.slice(0, 4000),
      truncated: result.current_body.length > 4000 || result.repaired_body.length > 4000,
    });
  } catch (error) {
    sourceLinkStyleLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairSelectedSourceLinkStyles() {
  const paths = [...checkedPaths];
  if (!paths.length) {
    sourceLinkStyleLog("Select at least one source style item first.");
    return;
  }
  if (!window.confirm(`Repair source image syntax in ${paths.length} original file(s)?`)) {
    return;
  }
  setBusy(true);
  sourceLinkStyleLog("Repairing selected source link styles...");
  try {
    const result = await repairSourceLinkStyles(paths);
    checkedPaths.clear();
    sourceLinkStyleLog(result);
    await loadSourceLinkStyleScan();
  } catch (error) {
    sourceLinkStyleLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairAllSafeSourceLinkStyles() {
  const count = scanResult?.safe_count || 0;
  if (!count) {
    sourceLinkStyleLog("No safe source style repairs found.");
    return;
  }
  if (!window.confirm(`Repair all ${count} original source file(s)?`)) {
    return;
  }
  setBusy(true);
  sourceLinkStyleLog("Repairing all safe source link styles...");
  try {
    const result = await repairAllSafeSourceLinkStylesApi($("source-link-style-language").value || "");
    checkedPaths.clear();
    sourceLinkStyleLog(result);
    await loadSourceLinkStyleScan();
  } catch (error) {
    sourceLinkStyleLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderSourceLinkStyleScan() {
  if (!$("source-link-style-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("source-link-style-summary").innerHTML = "";
    $("source-link-style-list").innerHTML = "";
    $("source-link-style-details").innerHTML = "";
    return;
  }

  $("source-link-style-summary").innerHTML = `
    <span class="pill">Items: <strong>${scan.total}</strong></span>
    <span class="pill ${scan.safe_count ? "yellow" : "green"}">Safe files: <strong>${scan.safe_count}</strong></span>
    <span class="pill">Total repairs: <strong>${scan.repair_count}</strong></span>
  `;

  const filter = $("source-link-style-filter").value.toLowerCase();
  const items = scan.items.filter((item) =>
    `${item.path} ${item.reasons.join(" ")} ${item.translation_id}`.toLowerCase().includes(filter)
  );
  $("source-link-style-list").innerHTML = "";
  items.forEach((item) => {
    const row = document.createElement("div");
    row.className = "cleanup-item";
    if (selectedPath === item.path) {
      row.classList.add("active");
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.disabled = !item.safe_repair;
    checkbox.checked = checkedPaths.has(item.path);
    checkbox.title = item.safe_repair ? "Select for repair" : "Not safely repairable";
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        checkedPaths.add(item.path);
      } else {
        checkedPaths.delete(item.path);
      }
      renderSourceLinkStyleDetails();
    });

    const button = document.createElement("button");
    button.type = "button";
    button.className = "cleanup-item-main";
    button.innerHTML = `
      <strong>${escapeHtml(item.path)}</strong>
      <span>${escapeHtml(item.reasons.join(", ") || "source_image_style")} | repairs: ${item.repair_count} | ${escapeHtml(item.translation_id || "-")}</span>
    `;
    button.addEventListener("click", () => {
      selectedPath = item.path;
      renderSourceLinkStyleScan();
      sourceLinkStyleLog(item);
    });

    row.appendChild(checkbox);
    row.appendChild(button);
    $("source-link-style-list").appendChild(row);
  });
  renderSourceLinkStyleDetails();
}

function renderSourceLinkStyleDetails() {
  if (!$("source-link-style-details")) {
    return;
  }
  const selected = scanResult?.items.find((item) => item.path === selectedPath);
  if (!selected) {
    $("source-link-style-details").innerHTML = `
      <dt>Checked</dt><dd>${checkedPaths.size}</dd>
    `;
    return;
  }
  $("source-link-style-details").innerHTML = `
    <dt>Path</dt><dd>${pathWithObsidianButton(selected.path)}</dd>
    <dt>Status</dt><dd>${escapeHtml(selected.status || "-")}</dd>
    <dt>ID</dt><dd>${escapeHtml(selected.translation_id || "-")}</dd>
    <dt>Repairs</dt><dd>${selected.repair_count}</dd>
    <dt>Diagnostics</dt><dd>${selected.diagnostic_count}</dd>
    <dt>Safe</dt><dd><span class="pill ${selected.safe_repair ? "yellow" : "red"}">${selected.safe_repair ? "yes" : "no"}</span></dd>
    <dt>Reasons</dt><dd>${escapeHtml(selected.reasons.join(", ") || "-")}</dd>
    <dt>Checked</dt><dd>${checkedPaths.size}</dd>
  `;
}

function setBusy(isBusy) {
  setControlsBusy(busyControls, isBusy);
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
