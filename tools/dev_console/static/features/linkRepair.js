import {
  previewLinkRepair,
  repairAllSafeLinkItemsApi,
  repairLinkItems,
  scanLinkRepair,
} from "../api/links.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText, pathWithObsidianButton } from "../core/html.js";

let context = {
};
const busyControls = ["link-repair-scan", "link-repair-preview", "link-repair-selected", "link-repair-all"];
let scanResult = null;
let selectedPath = null;
let checkedPaths = new Set();
let eventScope = createEventScope();

export function mountLinkRepairFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("link-repair-scan"), "click", () => {
    loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
  });
  eventScope.listen($("link-repair-preview"), "click", () => {
    previewLinkRepairSelected().catch((error) => linkRepairLog(error.message));
  });
  eventScope.listen($("link-repair-selected"), "click", () => {
    repairSelectedLinkItems().catch((error) => linkRepairLog(error.message));
  });
  eventScope.listen($("link-repair-all"), "click", () => {
    repairAllSafeLinkItems().catch((error) => linkRepairLog(error.message));
  });
  eventScope.listen($("link-repair-language"), "change", () => {
    selectedPath = null;
    checkedPaths.clear();
    loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
  });
  eventScope.listen($("link-repair-filter"), "input", renderLinkRepairScan);
  renderLinkRepairScan();
  renderLinkRepairDetails();
}

export function unmountLinkRepairFeature() {
  eventScope.clear();
}

export function linkRepairLog(value) {
  const log = $("link-repair-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function renderLinkRepairLanguageOptions(config) {
  const select = $("link-repair-language");
  if (!select) {
    return;
  }
  const languages = config.languages || [];
  select.innerHTML = [
    '<option value="">All languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`),
  ].join("");
}

export function hasLinkRepairScan() {
  return Boolean(scanResult);
}

export async function loadLinkRepairScan() {
  setBusy(true);
  linkRepairLog("Scanning translated link targets...");
  try {
    const language = $("link-repair-language").value || "";
    scanResult = await scanLinkRepair(language);
    const currentPaths = new Set(scanResult.items.map((item) => item.path));
    checkedPaths = new Set([...checkedPaths].filter((path) => currentPaths.has(path)));
    if (selectedPath && !currentPaths.has(selectedPath)) {
      selectedPath = null;
    }
    renderLinkRepairScan();
    linkRepairLog(scanResult);
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewLinkRepairSelected() {
  if (!selectedPath) {
    linkRepairLog("Select a link repair item first.");
    return;
  }
  setBusy(true);
  linkRepairLog("Previewing link repair...");
  try {
    const result = await previewLinkRepair(selectedPath);
    linkRepairLog({
      ...result,
      current_body: result.current_body.slice(0, 4000),
      repaired_body: result.repaired_body.slice(0, 4000),
      truncated: result.current_body.length > 4000 || result.repaired_body.length > 4000,
    });
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairSelectedLinkItems() {
  const paths = [...checkedPaths];
  if (!paths.length) {
    linkRepairLog("Select at least one safe repair item first.");
    return;
  }
  if (!window.confirm(`Repair link targets in ${paths.length} translated file(s)?`)) {
    return;
  }
  setBusy(true);
  linkRepairLog("Repairing selected link targets...");
  try {
    const result = await repairLinkItems(paths);
    checkedPaths.clear();
    linkRepairLog(result);
    await loadLinkRepairScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairAllSafeLinkItems() {
  const count = scanResult?.safe_count || 0;
  if (!count) {
    linkRepairLog("No safe link repairs found.");
    return;
  }
  if (!window.confirm(`Repair all ${count} safe translated file(s)?`)) {
    return;
  }
  setBusy(true);
  linkRepairLog("Repairing all safe link targets and dynamic labels...");
  try {
    const result = await repairAllSafeLinkItemsApi($("link-repair-language").value || "");
    checkedPaths.clear();
    linkRepairLog(result);
    await loadLinkRepairScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderLinkRepairScan() {
  if (!$("link-repair-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("link-repair-summary").innerHTML = "";
    $("link-repair-list").innerHTML = "";
    $("link-repair-details").innerHTML = "";
    return;
  }

  $("link-repair-summary").innerHTML = `
    <span class="pill">Items: <strong>${scan.total}</strong></span>
    <span class="pill ${scan.safe_count ? "yellow" : "green"}">Safe files: <strong>${scan.safe_count}</strong></span>
    <span class="pill">Total repairs: <strong>${scan.repair_count}</strong></span>
    <span class="pill">Dynamic labels: <strong>${scan.label_repair_count || 0}</strong></span>
  `;

  const filter = $("link-repair-filter").value.toLowerCase();
  const items = scan.items.filter((item) =>
    `${item.path} ${item.source} ${item.reasons.join(" ")} ${item.translation_id}`.toLowerCase().includes(filter)
  );
  $("link-repair-list").innerHTML = "";
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
      renderLinkRepairDetails();
    });

    const button = document.createElement("button");
    button.type = "button";
    button.className = "cleanup-item-main";
    button.innerHTML = `
      <strong>${escapeHtml(item.path)}</strong>
      <span>${escapeHtml(item.reasons.join(", ") || "target_repaired")} | repairs: ${item.repair_count} | labels: ${item.label_repair_count || 0} | ${escapeHtml(item.translation_id || "-")}</span>
    `;
    button.addEventListener("click", () => {
      selectedPath = item.path;
      renderLinkRepairScan();
      linkRepairLog(item);
    });

    row.appendChild(checkbox);
    row.appendChild(button);
    $("link-repair-list").appendChild(row);
  });
  renderLinkRepairDetails();
}

function renderLinkRepairDetails() {
  if (!$("link-repair-details")) {
    return;
  }
  const selected = scanResult?.items.find((item) => item.path === selectedPath);
  if (!selected) {
    $("link-repair-details").innerHTML = `
      <dt>Checked</dt><dd>${checkedPaths.size}</dd>
    `;
    return;
  }
  $("link-repair-details").innerHTML = `
    <dt>Path</dt><dd>${pathWithObsidianButton(selected.path)}</dd>
    <dt>Status</dt><dd>${escapeHtml(selected.status || "-")}</dd>
    <dt>ID</dt><dd>${escapeHtml(selected.translation_id || "-")}</dd>
    <dt>Source</dt><dd>${pathWithObsidianButton(selected.source)}</dd>
    <dt>Repairs</dt><dd>${selected.repair_count}</dd>
    <dt>Dynamic Labels</dt><dd>${selected.label_repair_count || 0}</dd>
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
