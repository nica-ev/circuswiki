import { deleteAllCleanupOrphans, deleteCleanupOrphans, scanCleanupOrphans } from "../api/cleanup.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText, pathWithObsidianButton } from "../core/html.js";

let context = {
  loadVaultHealth: async () => {},
};
const busyControls = ["cleanup-scan", "cleanup-delete-selected", "cleanup-delete-all"];
let scanResult = null;
let selectedPath = null;
let checkedPaths = new Set();
let eventScope = createEventScope();

export function mountCleanupFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("cleanup-scan"), "click", () => {
    loadCleanupScan().catch((error) => cleanupLog(error.message));
  });
  eventScope.listen($("cleanup-delete-selected"), "click", () => {
    deleteSelectedCleanupItems().catch((error) => cleanupLog(error.message));
  });
  eventScope.listen($("cleanup-delete-all"), "click", () => {
    deleteAllCleanupItems().catch((error) => cleanupLog(error.message));
  });
  eventScope.listen($("cleanup-filter"), "input", renderCleanupScan);
  renderCleanupScan();
  renderCleanupDetails();
}

export function unmountCleanupFeature() {
  eventScope.clear();
}

export function cleanupLog(value) {
  const log = $("cleanup-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasCleanupScan() {
  return Boolean(scanResult);
}

export async function loadCleanupScan() {
  setBusy(true);
  cleanupLog("Scanning orphan translations...");
  try {
    scanResult = await scanCleanupOrphans();
    const currentPaths = new Set(scanResult.items.map((item) => item.path));
    checkedPaths = new Set([...checkedPaths].filter((path) => currentPaths.has(path)));
    if (selectedPath && !currentPaths.has(selectedPath)) {
      selectedPath = null;
    }
    renderCleanupScan();
    cleanupLog(scanResult);
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

export async function deleteSelectedCleanupItems() {
  const paths = [...checkedPaths];
  if (!paths.length) {
    cleanupLog("Select at least one deletable orphan first.");
    return;
  }
  if (!window.confirm(`Delete ${paths.length} orphan translation file(s)? This cannot be undone by the tool.`)) {
    return;
  }
  setBusy(true);
  cleanupLog("Deleting selected orphan translations...");
  try {
    const result = await deleteCleanupOrphans(paths);
    checkedPaths.clear();
    cleanupLog(result);
    await loadCleanupScan();
    await context.loadVaultHealth();
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

export async function deleteAllCleanupItems() {
  const count = scanResult?.deletable_count || 0;
  if (!count) {
    cleanupLog("No deletable orphan translations found.");
    return;
  }
  if (!window.confirm(`Delete all ${count} deletable orphan translation file(s)? This cannot be undone by the tool.`)) {
    return;
  }
  setBusy(true);
  cleanupLog("Deleting all deletable orphan translations...");
  try {
    const result = await deleteAllCleanupOrphans();
    checkedPaths.clear();
    cleanupLog(result);
    await loadCleanupScan();
    await context.loadVaultHealth();
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

export function renderCleanupScan() {
  if (!$("cleanup-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("cleanup-summary").innerHTML = "";
    $("cleanup-list").innerHTML = "";
    $("cleanup-details").innerHTML = "";
    return;
  }

  const counts = Object.entries(scan.counts || {})
    .map(([reason, count]) => `${reason}: ${count}`)
    .join(", ");
  $("cleanup-summary").innerHTML = `
    <span class="pill">Items: <strong>${scan.total}</strong></span>
    <span class="pill ${scan.deletable_count ? "yellow" : "green"}">Deletable: <strong>${scan.deletable_count}</strong></span>
    <span class="pill">Reasons: <strong>${escapeHtml(counts || "none")}</strong></span>
  `;

  const filter = $("cleanup-filter").value.toLowerCase();
  const items = scan.items.filter((item) =>
    `${item.path} ${item.source} ${item.reason} ${item.translation_id}`.toLowerCase().includes(filter)
  );
  $("cleanup-list").innerHTML = "";
  items.forEach((item) => {
    const row = document.createElement("div");
    row.className = "cleanup-item";
    if (selectedPath === item.path) {
      row.classList.add("active");
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.disabled = !item.deletable;
    checkbox.checked = checkedPaths.has(item.path);
    checkbox.title = item.deletable ? "Select for deletion" : "Not safely deletable";
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        checkedPaths.add(item.path);
      } else {
        checkedPaths.delete(item.path);
      }
      renderCleanupDetails();
    });

    const button = document.createElement("button");
    button.type = "button";
    button.className = "cleanup-item-main";
    button.innerHTML = `
      <strong>${escapeHtml(item.path)}</strong>
      <span>${escapeHtml(item.reason)} | ${escapeHtml(item.status || "-")} | ${escapeHtml(item.translation_id || "-")}</span>
    `;
    button.addEventListener("click", () => {
      selectedPath = item.path;
      renderCleanupScan();
      cleanupLog(item);
    });

    row.appendChild(checkbox);
    row.appendChild(button);
    $("cleanup-list").appendChild(row);
  });
  renderCleanupDetails();
}

function renderCleanupDetails() {
  if (!$("cleanup-details")) {
    return;
  }
  const selected = scanResult?.items.find((item) => item.path === selectedPath);
  if (!selected) {
    $("cleanup-details").innerHTML = `
      <dt>Checked</dt><dd>${checkedPaths.size}</dd>
    `;
    return;
  }
  $("cleanup-details").innerHTML = `
    <dt>Path</dt><dd>${pathWithObsidianButton(selected.path)}</dd>
    <dt>Status</dt><dd>${escapeHtml(selected.status || "-")}</dd>
    <dt>ID</dt><dd>${escapeHtml(selected.translation_id || "-")}</dd>
    <dt>Source</dt><dd>${pathWithObsidianButton(selected.source)}</dd>
    <dt>Reason</dt><dd>${escapeHtml(selected.reason)}</dd>
    <dt>Deletable</dt><dd><span class="pill ${selected.deletable ? "yellow" : "red"}">${selected.deletable ? "yes" : "no"}</span></dd>
    <dt>Detail</dt><dd>${escapeHtml(selected.detail)}</dd>
    <dt>Checked</dt><dd>${checkedPaths.size}</dd>
  `;
}

function setBusy(isBusy) {
  setControlsBusy(busyControls, isBusy);
}
