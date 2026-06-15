import {
  applyNavigation,
  initNavigation,
  previewNavigation,
  scanNavigation,
  translateAllNavigationLabelsApi,
} from "../api/navigation.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let context = {
  getDefaultSourceLang: () => "",
  getModelName: () => "",
};
const busyControls = ["nav-scan", "nav-init", "nav-translate", "nav-preview", "nav-apply"];
let scanResult = null;
let previewResult = null;
let eventScope = createEventScope();

export function mountNavigationFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("nav-scan"), "click", () => {
    loadNavigationScan().catch((error) => navLog(error.message));
  });
  eventScope.listen($("nav-init"), "click", () => {
    initNavigationModel().catch((error) => navLog(error.message));
  });
  eventScope.listen($("nav-translate"), "click", () => {
    translateNavigationLabels().catch((error) => navLog(error.message));
  });
  eventScope.listen($("nav-preview"), "click", () => {
    previewNavigationModel().catch((error) => navLog(error.message));
  });
  eventScope.listen($("nav-apply"), "click", () => {
    applyNavigationModel().catch((error) => navLog(error.message));
  });
  if (scanResult) {
    $("nav-model").value = JSON.stringify(scanResult.model, null, 2);
  }
  renderNavigationLanguageOptions();
  renderNavigationScan();
  renderNavigationPreview();
}

export function unmountNavigationFeature() {
  eventScope.clear();
}

export function navLog(value) {
  const log = $("nav-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasNavigationScan() {
  return Boolean(scanResult);
}

export async function loadNavigationScan() {
  setBusy(true);
  navLog("Scanning navigation...");
  try {
    scanResult = await scanNavigation();
    $("nav-model").value = JSON.stringify(scanResult.model, null, 2);
    renderNavigationLanguageOptions();
    renderNavigationScan();
    navLog(scanResult);
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function initNavigationModel() {
  const sourceLang = $("nav-source").value || context.getDefaultSourceLang() || "";
  if (!sourceLang) {
    navLog("Select a navigation source language.");
    return;
  }
  setBusy(true);
  navLog(`Creating canonical model from ${sourceLang} nav...`);
  try {
    const result = await initNavigation({ language: sourceLang });
    $("nav-model").value = JSON.stringify(result.model, null, 2);
    previewResult = result.preview;
    renderNavigationPreview();
    await loadNavigationScan();
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function translateNavigationLabels() {
  const model = currentNavigationModel();
  if (!model) {
    return;
  }
  const sourceLang = $("nav-source").value || context.getDefaultSourceLang() || "";
  if (!sourceLang) {
    navLog("Select a navigation source language.");
    return;
  }

  setBusy(true);
  navLog(`Translating navigation labels from ${sourceLang} to all other configured languages...`);
  try {
    const result = await translateAllNavigationLabelsApi({
      model,
      source_lang: sourceLang,
      llm_model: context.getModelName(),
    });
    $("nav-model").value = JSON.stringify(result.model, null, 2);
    previewResult = result.preview;
    renderNavigationPreview();
    navLog({
      source: languageLabel(result.source_lang, result.source_language),
      target_count: result.target_count,
      results: result.results.map((item) => ({
        target: languageLabel(item.target_lang, item.target_language),
        translated_count: item.translated_count,
        translations: item.translations,
      })),
    });
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewNavigationModel() {
  const model = currentNavigationModel();
  if (!model) {
    return;
  }

  setBusy(true);
  navLog("Rendering navigation preview...");
  try {
    previewResult = await previewNavigation({ model });
    renderNavigationPreview();
    navLog(previewResult);
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function applyNavigationModel() {
  const model = currentNavigationModel();
  if (!model) {
    return;
  }

  setBusy(true);
  navLog("Previewing before apply...");
  try {
    previewResult = await previewNavigation({ model });
    renderNavigationPreview();
    const result = await applyNavigation({ model });
    navLog(result);
    await loadNavigationScan();
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

function currentNavigationModel() {
  try {
    return JSON.parse($("nav-model").value);
  } catch (error) {
    navLog(`Invalid navigation JSON: ${error.message}`);
    return null;
  }
}

function renderNavigationLanguageOptions() {
  const select = $("nav-source");
  const scan = scanResult;
  if (!scan) {
    select.innerHTML = "";
    return;
  }
  const current = select.value || context.getDefaultSourceLang() || scan.languages[0] || "";
  select.innerHTML = scan.languages
    .map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, scan.language_names[language]))}</option>`)
    .join("");
  if (scan.languages.includes(current)) {
    select.value = current;
  }
}

function renderNavigationScan() {
  if (!$("nav-summary")) {
    return;
  }
  const scan = scanResult;
  if (!scan) {
    $("nav-summary").innerHTML = "";
    $("nav-diagnostics").innerHTML = "";
    return;
  }

  $("nav-summary").innerHTML = `
    <span class="pill">Model: <strong>${scan.model_exists ? "exists" : "missing"}</strong></span>
    <span class="pill ${scan.has_multiple_navs ? "yellow" : "green"}">Nav variants: <strong>${scan.nav_variants.length}</strong></span>
    <span class="pill">Languages: <strong>${scan.languages.length}</strong></span>
    <span class="pill">Orphan candidates: <strong>${scan.orphan_candidate_count}</strong></span>
    <span class="pill ${scan.model_missing_targets.length ? "yellow" : "green"}">Model missing targets: <strong>${scan.model_missing_targets.length}</strong></span>
  `;

  const configCards = Object.entries(scan.configs).map(([language, config]) => `
    <article class="nav-card">
      <strong>${escapeHtml(languageLabel(language, scan.language_names[language]))}</strong>
      <span>${config.count} entries</span>
      ${config.duplicate_pages.length ? `<p>Duplicate pages: ${escapeHtml(config.duplicate_pages.join(", "))}</p>` : ""}
      ${config.missing_files.length ? `<p>Missing files: ${config.missing_files.length}</p>` : ""}
    </article>
  `).join("");

  const variants = scan.nav_variants.map((variant, index) => `
    <article class="nav-card">
      <strong>Variant ${index + 1}</strong>
      <p>${escapeHtml(variant.languages.join(", "))}</p>
    </article>
  `).join("");

  const orphans = scan.orphan_candidates.slice(0, 20).map((item) =>
    `<li>${escapeHtml(item.title)} <span class="muted-inline">${escapeHtml(item.page)}</span></li>`
  ).join("");

  $("nav-diagnostics").innerHTML = `
    ${variants}
    ${configCards}
    <article class="nav-card">
      <strong>Orphan candidates</strong>
      <ul>${orphans || "<li>none</li>"}</ul>
    </article>
  `;
}

function renderNavigationPreview() {
  if (!$("nav-preview-output")) {
    return;
  }
  const preview = previewResult;
  if (!preview) {
    $("nav-preview-output").innerHTML = "";
    return;
  }

  const changed = Object.entries(preview.changed).map(([language, isChanged]) => `
    <article class="nav-card">
      <strong>${escapeHtml(language)}</strong>
      <span class="${isChanged ? "pill yellow" : "pill green"}">${isChanged ? "will change" : "unchanged"}</span>
      <pre class="inline-code">${escapeHtml((preview.rendered[language] || "").slice(0, 900))}</pre>
    </article>
  `).join("");

  $("nav-preview-output").innerHTML = `
    <article class="nav-card">
      <strong>Preview</strong>
      <p>${preview.changed_count} config files would change.</p>
    </article>
    ${changed}
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
