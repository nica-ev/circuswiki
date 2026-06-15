import { materializeBaseLabelsApi, planBaseLabelsApi, scanBaseLabels, translateBaseLabelsApi } from "../api/baseLabels.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let context = {
  getModelName: () => "",
};
const busyControls = ["base-label-scan", "base-label-plan", "base-label-translate", "base-label-materialize"];
let scanResult = null;
let planResult = null;
let selectedId = null;
let eventScope = createEventScope();

export function mountBaseLabelsFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("base-label-scan"), "click", () => {
    loadBaseLabelScan().catch((error) => baseLabelLog(error.message));
  });
  eventScope.listen($("base-label-plan"), "click", () => {
    planBaseLabels().catch((error) => baseLabelLog(error.message));
  });
  eventScope.listen($("base-label-translate"), "click", () => {
    translateBaseLabels().catch((error) => baseLabelLog(error.message));
  });
  eventScope.listen($("base-label-materialize"), "click", () => {
    materializeBaseLabels().catch((error) => baseLabelLog(error.message));
  });
  eventScope.listen($("base-label-base"), "change", () => {
    selectedId = null;
    renderBaseLabelScan();
  });
  eventScope.listen($("base-label-language"), "change", () => {
    planResult = null;
  });
  eventScope.listen($("base-label-filter"), "input", renderBaseLabelScan);
  renderBaseLabelScan();
  renderBaseLabelDetails();
  renderBaseLabelPlan();
}

export function unmountBaseLabelsFeature() {
  eventScope.clear();
}

export function baseLabelLog(value) {
  const log = $("base-label-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasBaseLabelScan() {
  return Boolean(scanResult);
}

export function renderBaseLabelLanguageOptions(config) {
  const select = $("base-label-language");
  if (!select) {
    return;
  }
  const languages = config.languages || [];
  select.innerHTML = [
    '<option value="all">All target languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`),
  ].join("");
}

export async function loadBaseLabelScan() {
  setBusy(true);
  baseLabelLog("Scanning base display names...");
  try {
    scanResult = await scanBaseLabels();
    updateBaseLabelBaseOptions();
    renderBaseLabelScan();
    baseLabelLog(scanResult);
  } catch (error) {
    baseLabelLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function planBaseLabels() {
  setBusy(true);
  baseLabelLog("Planning base label translations...");
  try {
    const params = new URLSearchParams();
    if ($("base-label-base").value) {
      params.set("base", $("base-label-base").value);
    }
    params.set("target_lang", $("base-label-language").value || "all");
    planResult = await planBaseLabelsApi(params);
    renderBaseLabelPlan();
    baseLabelLog(planResult);
  } catch (error) {
    baseLabelLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function translateBaseLabels() {
  setBusy(true);
  baseLabelLog("Translating missing/stale base labels...");
  try {
    const result = await translateBaseLabelsApi({
      base: $("base-label-base").value,
      target_lang: $("base-label-language").value || "all",
      model: context.getModelName(),
    });
    baseLabelLog(result);
    await loadBaseLabelScan();
  } catch (error) {
    baseLabelLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function materializeBaseLabels() {
  setBusy(true);
  baseLabelLog("Regenerating localized generated base files...");
  try {
    const result = await materializeBaseLabelsApi({
      base: $("base-label-base").value,
      target_lang: $("base-label-language").value || "all",
    });
    baseLabelLog(result);
  } catch (error) {
    baseLabelLog(error.message);
  } finally {
    setBusy(false);
  }
}

function updateBaseLabelBaseOptions() {
  const select = $("base-label-base");
  if (!select || !scanResult) {
    return;
  }
  const current = select.value;
  select.innerHTML = [
    '<option value="">All base files</option>',
    ...scanResult.bases.map((base) => `<option value="${escapeHtml(base.path)}">${escapeHtml(base.path)}</option>`),
  ].join("");
  if (!current || scanResult.bases.some((base) => base.path === current)) {
    select.value = current;
  }
}

function baseLabelRows() {
  const scan = scanResult;
  if (!scan || !$("base-label-base") || !$("base-label-filter")) {
    return [];
  }
  const selectedBase = $("base-label-base").value;
  const filter = $("base-label-filter").value.toLowerCase();
  const rows = [];
  for (const base of scan.bases) {
    if (selectedBase && base.path !== selectedBase) {
      continue;
    }
    for (const property of base.properties) {
      const row = { ...property, base: base.path, source_lang: base.source_lang };
      const haystack = `${row.base} ${row.key} ${row.source} ${row.missing_languages.join(" ")} ${row.stale_languages.join(" ")}`.toLowerCase();
      if (!filter || haystack.includes(filter)) {
        rows.push(row);
      }
    }
  }
  return rows;
}

function renderBaseLabelScan() {
  if (!$("base-label-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("base-label-summary").innerHTML = "";
    $("base-label-list").innerHTML = "";
    $("base-label-details").innerHTML = "";
    return;
  }
  const baseCount = scan.bases.length;
  const propertyCount = scan.bases.reduce((sum, base) => sum + base.property_count, 0);
  const missingCount = scan.bases.reduce((sum, base) => sum + base.missing_count, 0);
  const staleCount = scan.bases.reduce((sum, base) => sum + base.stale_count, 0);
  $("base-label-summary").innerHTML = `
    <span class="pill">Bases: <strong>${baseCount}</strong></span>
    <span class="pill">Properties: <strong>${propertyCount}</strong></span>
    <span class="pill ${missingCount ? "yellow" : "green"}">Missing: <strong>${missingCount}</strong></span>
    <span class="pill ${staleCount ? "yellow" : "green"}">Stale: <strong>${staleCount}</strong></span>
    <span class="pill">Config: <strong>${escapeHtml(scan.config_path)}</strong></span>
  `;
  const rows = baseLabelRows();
  $("base-label-list").innerHTML = "";
  rows.forEach((row) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page";
    const id = `${row.base}::${row.key}`;
    if (selectedId === id) {
      button.classList.add("active");
    }
    button.textContent = `${row.key} | ${row.source}`;
    button.title = row.base;
    button.addEventListener("click", () => {
      selectedId = id;
      renderBaseLabelScan();
      baseLabelLog(row);
    });
    $("base-label-list").appendChild(button);
  });
  renderBaseLabelDetails();
}

function renderBaseLabelDetails() {
  if (!$("base-label-details")) {
    return;
  }
  const rows = baseLabelRows();
  const row = rows.find((item) => `${item.base}::${item.key}` === selectedId);
  if (!row) {
    $("base-label-details").innerHTML = "";
    return;
  }
  $("base-label-details").innerHTML = `
    <article class="nav-card">
      <strong>${escapeHtml(row.key)}</strong>
      <p>${escapeHtml(row.base)}</p>
      <p>Source (${escapeHtml(row.source_lang)}): ${escapeHtml(row.source)}</p>
      <p>Translated languages: ${row.translation_count}</p>
      <p>Missing: ${escapeHtml(row.missing_languages.join(", ") || "none")}</p>
      <p>Stale: ${escapeHtml(row.stale_languages.join(", ") || "none")}</p>
    </article>
  `;
}

function renderBaseLabelPlan() {
  if (!$("base-label-summary") || !$("base-label-details")) {
    return;
  }
  const plan = planResult;
  if (!plan) {
    return;
  }
  $("base-label-summary").innerHTML = `
    <span class="pill">Planned: <strong>${plan.candidate_count}</strong></span>
    <span class="pill">Target: <strong>${escapeHtml(plan.target_lang)}</strong></span>
    <span class="pill">Base: <strong>${escapeHtml(plan.base || "all")}</strong></span>
  `;
  $("base-label-details").innerHTML = plan.candidates.slice(0, 80).map((item) => `
    <article class="nav-card">
      <strong>${escapeHtml(item.property)} -> ${escapeHtml(item.target_lang)}</strong>
      <p>${escapeHtml(item.base)}</p>
      <p>${escapeHtml(item.source)} <span class="pill yellow">${escapeHtml(item.reason)}</span></p>
    </article>
  `).join("") || '<article class="nav-card"><strong>No missing or stale labels.</strong></article>';
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
