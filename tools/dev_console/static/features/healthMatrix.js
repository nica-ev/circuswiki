import { getVaultHealth, repairMetadata } from "../api/translation.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";
import { matrixLayoutSizes } from "../core/layout.js";

let context = {
  afterLoad: () => {},
};
const busyControls = ["refresh-health", "repair-health"];
let vaultHealth = null;
let matrixWindow = { start: 0, end: 0 };
let matrixDrag = null;
let eventScope = createEventScope();

export function mountHealthMatrixFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("refresh-health"), "click", () => {
    loadVaultHealth().catch((error) => healthLog(error.message));
  });
  eventScope.listen($("repair-health"), "click", () => {
    runMetadataRepair().catch((error) => healthLog(error.message));
  });
  eventScope.listen($("health-filter"), "input", () => {
    matrixWindow = { start: 0, end: 0 };
    renderVaultHealth();
  });
  eventScope.listen($("health-status"), "change", () => {
    matrixWindow = { start: 0, end: 0 };
    renderVaultHealth();
  });
  eventScope.listen($("matrix-window-start"), "pointerdown", (event) => startMatrixDrag("start", event));
  eventScope.listen($("matrix-window-end"), "pointerdown", (event) => startMatrixDrag("end", event));
  eventScope.listen($("matrix-window-selection"), "pointerdown", (event) => startMatrixDrag("range", event));
  eventScope.listen(document, "pointermove", updateMatrixDrag);
  eventScope.listen(document, "pointerup", stopMatrixDrag);
  renderVaultHealth();
}

export function unmountHealthMatrixFeature() {
  eventScope.clear();
  matrixDrag = null;
}

export function healthLog(value) {
  const log = $("health-details");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasVaultHealth() {
  return Boolean(vaultHealth);
}

export function getLanguageCodes() {
  return vaultHealth?.languages || [];
}

export function getLanguageNames() {
  return vaultHealth?.language_names || {};
}

export async function loadVaultHealth() {
  vaultHealth = await getVaultHealth();
  $("metric-matrix").textContent = `${vaultHealth.totals.green}/${vaultHealth.totals.yellow}/${vaultHealth.totals.red}`;
  renderVaultHealth();
  context.afterLoad(vaultHealth);
  return vaultHealth;
}

export function refreshHealthLayout() {
  renderVaultHealth();
}

async function runMetadataRepair() {
  if (!vaultHealth) {
    await loadVaultHealth();
  }

  const candidates = repairCandidates();
  if (!candidates.length) {
    healthLog("No yellow metadata issues found.");
    return;
  }

  const progress = $("repair-progress");
  const status = $("repair-status");
  progress.max = candidates.length;
  progress.value = 0;
  setBusy(true);
  status.textContent = `Repairing 0/${candidates.length}...`;
  const results = [];
  try {
    for (let index = 0; index < candidates.length; index += 1) {
      const candidate = candidates[index];
      status.textContent = `Repairing ${index + 1}/${candidates.length}: ${candidate.translation_id} (${candidate.language})`;
      const result = await repairMetadata({ path: candidate.path });
      results.push(result);
      progress.value = index + 1;
      healthLog(results);
    }
    status.textContent = `Repair complete: ${results.length} files.`;
    healthLog(results);
    await loadVaultHealth();
  } catch (error) {
    status.textContent = "Repair stopped.";
    healthLog(error.message);
  } finally {
    setBusy(false);
  }
}

function repairCandidates() {
  const seen = new Set();
  const candidates = [];
  for (const row of vaultHealth?.rows || []) {
    for (const language of vaultHealth.languages) {
      const cell = row.cells[language];
      if (cell.status !== "yellow" || !cell.exists || !cell.path) {
        continue;
      }
      if (seen.has(cell.path)) {
        continue;
      }
      seen.add(cell.path);
      candidates.push({
        path: cell.path,
        translation_id: row.translation_id,
        language,
      });
    }
  }
  return candidates;
}

function renderVaultHealth() {
  const health = vaultHealth;
  if (!health) {
    return;
  }
  if (!$("health-summary")) {
    return;
  }

  $("health-summary").innerHTML = `
    <span class="pill">Notes: <strong>${health.total_notes}</strong></span>
    <span class="pill green">Green: <strong>${health.totals.green}</strong></span>
    <span class="pill yellow">Yellow: <strong>${health.totals.yellow}</strong></span>
    <span class="pill red">Red: <strong>${health.totals.red}</strong></span>
    <span class="pill">Languages: <strong>${health.languages.join(", ")}</strong></span>
  `;

  const query = $("health-filter").value.toLowerCase();
  const statusFilter = $("health-status").value;
  const rows = health.rows.filter((row) => matchesHealthFilter(row, query, statusFilter));
  const window = normalizedMatrixWindow(rows.length);
  const visibleRows = rows.slice(window.start, window.end);
  updateMatrixWindowControls(rows.length, window.start, window.end);

  const table = $("health-matrix");
  const wrapWidth = $("health-matrix").parentElement.clientWidth || 900;
  const matrixLayout = matrixLayoutSizes();
  const plotWidth = Math.max(
    matrixLayout.minPlotWidth,
    wrapWidth - matrixLayout.labelWidth
  );
  const cellWidth = visibleRows.length
    ? Math.max(2, Math.floor((plotWidth - visibleRows.length - 1) / visibleRows.length))
    : 15;
  table.style.setProperty("--matrix-cell-width", `${cellWidth}px`);
  table.innerHTML = "";
  const thead = document.createElement("thead");
  const header = document.createElement("tr");
  header.innerHTML = `
    <th class="sticky-col lang-col">lang</th>
    ${visibleRows.map((row, index) => `<th class="note-index" title="${escapeHtml(row.translation_id)}">${window.start + index + 1}</th>`).join("")}
  `;
  thead.appendChild(header);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  health.languages.forEach((language) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `<th class="sticky-col lang-col">${escapeHtml(language)}</th>`;

    visibleRows.forEach((row) => {
      const cell = row.cells[language];
      const td = document.createElement("td");
      const button = document.createElement("button");
      button.type = "button";
      button.className = `status-cell ${cell.status}`;
      button.title = `${language} | ${row.translation_id} | ${cell.issues.length ? cell.issues.join(", ") : "ok"}`;
      button.setAttribute("aria-label", button.title);
      button.addEventListener("click", () => {
        healthLog({
          translation_id: row.translation_id,
          title: row.title,
          source_lang: row.source_lang,
          language,
          ...cell,
        });
      });
      td.appendChild(button);
      tr.appendChild(td);
    });

    tbody.appendChild(tr);
  });
  table.appendChild(tbody);
}

function normalizedMatrixWindow(rowCount) {
  if (rowCount <= 0) {
    matrixWindow = { start: 0, end: 0 };
    return matrixWindow;
  }

  let start = Number.isInteger(matrixWindow.start) ? matrixWindow.start : 0;
  let end = Number.isInteger(matrixWindow.end) && matrixWindow.end > 0
    ? matrixWindow.end
    : rowCount;

  start = Math.max(0, Math.min(start, rowCount - 1));
  end = Math.max(start + 1, Math.min(end, rowCount));
  matrixWindow = { start, end };
  return matrixWindow;
}

function updateMatrixWindowControls(rowCount, start, end) {
  const startHandle = $("matrix-window-start");
  const endHandle = $("matrix-window-end");
  const selection = $("matrix-window-selection");
  const label = $("matrix-window-label");

  if (!rowCount) {
    startHandle.style.setProperty("--handle-left", "0%");
    endHandle.style.setProperty("--handle-left", "0%");
    selection.style.setProperty("--range-left", "0%");
    selection.style.setProperty("--range-width", "0%");
    label.textContent = "0/0";
    return;
  }

  const startPercent = (start / rowCount) * 100;
  const endPercent = (end / rowCount) * 100;
  startHandle.style.setProperty("--handle-left", `${startPercent}%`);
  endHandle.style.setProperty("--handle-left", `${endPercent}%`);
  selection.style.setProperty("--range-left", `${startPercent}%`);
  selection.style.setProperty("--range-width", `${endPercent - startPercent}%`);
  label.textContent = `${start + 1}-${end} / ${rowCount}`;
}

function setMatrixWindow(start, end) {
  matrixWindow = { start, end };
  renderVaultHealth();
}

function filteredVaultRows() {
  const health = vaultHealth;
  if (!health) {
    return [];
  }
  const query = $("health-filter").value.toLowerCase();
  const statusFilter = $("health-status").value;
  return health.rows.filter((row) => matchesHealthFilter(row, query, statusFilter));
}

function matrixIndexFromPointer(event) {
  const rows = filteredVaultRows();
  if (!rows.length) {
    return 0;
  }
  const rect = $("matrix-window-range").getBoundingClientRect();
  const ratio = Math.max(0, Math.min(1, (event.clientX - rect.left) / Math.max(1, rect.width)));
  return Math.round(ratio * rows.length);
}

function startMatrixDrag(kind, event) {
  event.preventDefault();
  const rows = filteredVaultRows();
  if (!rows.length) {
    return;
  }
  $("matrix-window-range").setPointerCapture(event.pointerId);
  matrixDrag = {
    kind,
    pointerId: event.pointerId,
    startWindow: normalizedMatrixWindow(rows.length),
    startIndex: matrixIndexFromPointer(event),
  };
  updateMatrixDrag(event);
}

function updateMatrixDrag(event) {
  const drag = matrixDrag;
  if (!drag || drag.pointerId !== event.pointerId) {
    return;
  }
  const rows = filteredVaultRows();
  if (!rows.length) {
    return;
  }
  const index = matrixIndexFromPointer(event);
  const startWindow = drag.startWindow;
  if (drag.kind === "start") {
    setMatrixWindow(Math.min(index, startWindow.end - 1), startWindow.end);
    return;
  }
  if (drag.kind === "end") {
    setMatrixWindow(startWindow.start, Math.max(index, startWindow.start + 1));
    return;
  }
  const width = Math.max(1, startWindow.end - startWindow.start);
  const offset = index - drag.startIndex;
  let start = startWindow.start + offset;
  let end = start + width;
  if (start < 0) {
    start = 0;
    end = width;
  }
  if (end > rows.length) {
    end = rows.length;
    start = Math.max(0, end - width);
  }
  setMatrixWindow(start, end);
}

function stopMatrixDrag() {
  matrixDrag = null;
}

function matchesHealthFilter(row, query, statusFilter) {
  if (query) {
    const haystack = `${row.translation_id} ${row.title} ${row.source_lang}`.toLowerCase();
    if (!haystack.includes(query)) {
      return false;
    }
  }
  if (statusFilter === "all") {
    return true;
  }
  return Object.values(row.cells).some((cell) => cell.status === statusFilter);
}

function setBusy(isBusy) {
  setControlsBusy(busyControls, isBusy);
}
