import { getHealth, getPage, translateMetadata, translatePage } from "../api/translation.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText, pathWithObsidianButton } from "../core/html.js";

let context = {
  refreshVaultHealth: async () => {},
};
const busyControls = ["dry-run", "translate", "translate-metadata", "refresh"];
let config = null;
let pages = [];
let selectedPath = null;
let pageDetails = null;
let eventScope = createEventScope();

export function mountTranslateSingleFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("filter"), "input", renderPages);
  eventScope.listen($("refresh"), "click", () => {
    loadSingleFileHealth().catch((error) => singleFileLog(error.message));
    context.refreshVaultHealth().catch((error) => singleFileLog(error.message));
  });
  eventScope.listen($("file-source-lang"), "change", () => {
    selectedPath = null;
    pageDetails = null;
    renderDetails();
    loadSingleFileHealth().catch((error) => singleFileLog(error.message));
  });
  eventScope.listen($("file-target-lang"), "change", () => {
    if (selectedPath) {
      selectPage(selectedPath).catch((error) => singleFileLog(error.message));
    }
    loadSingleFileHealth().catch((error) => singleFileLog(error.message));
  });
  eventScope.listen($("dry-run"), "click", () => runTranslation(true));
  eventScope.listen($("translate-metadata"), "click", () => runMetadataTranslation(false));
  eventScope.listen($("translate"), "click", () => runTranslation(false));
  renderPages();
  renderDetails();
}

export function unmountTranslateSingleFeature() {
  eventScope.clear();
}

export function singleFileLog(value) {
  const log = $("log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function renderFileLanguageOptions(nextConfig) {
  config = nextConfig;
  const languages = config.languages || [];
  const options = languages
    .map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`)
    .join("");
  $("file-source-lang").innerHTML = options;
  $("file-target-lang").innerHTML = options;
  $("file-source-lang").value = config.default_source_lang || languages[0]?.code || "";
  $("file-target-lang").value = config.default_target_lang || languages[0]?.code || "";
}

export async function loadSingleFileHealth() {
  const health = await getHealth(fileSourceLang(), fileTargetLang());
  if ($("metric-total")) {
    $("metric-total").textContent = health.total;
    $("metric-translated").textContent = health.translated;
    $("metric-needs").textContent = health.needs_translation;
    $("metric-issues").textContent = health.with_issues;
  }
  pages = health.pages;
  renderPages();
}

function renderPages() {
  if (!$("pages")) {
    return;
  }
  const filter = $("filter").value.toLowerCase();
  const visiblePages = pages.filter((page) =>
    page.source.toLowerCase().includes(filter)
  );
  $("pages").innerHTML = "";

  visiblePages.forEach((page) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page";
    if (selectedPath === page.source) {
      button.classList.add("active");
    }
    button.textContent = page.source.replace(`docs/${fileSourceLang()}/`, "");
    button.title = page.source;
    button.addEventListener("click", () => selectPage(page.source));
    $("pages").appendChild(button);
  });
}

async function selectPage(path) {
  selectedPath = path;
  renderPages();
  pageDetails = await getPage(path, fileSourceLang(), fileTargetLang());
  renderDetails();
}

function renderDetails() {
  if (!$("details")) {
    return;
  }
  const page = pageDetails;
  if (!page) {
    $("details").innerHTML = "";
    return;
  }

  const issues = page.issues.length
    ? page.issues.map((issue) => `<span class="issue">${escapeHtml(issue)}</span>`).join("")
    : '<span class="ok">none</span>';

  $("details").innerHTML = `
    <dt>Source</dt><dd>${pathWithObsidianButton(page.source)}</dd>
    <dt>Target</dt><dd>${pathWithObsidianButton(page.target)}</dd>
    <dt>ID</dt><dd>${escapeHtml(page.translation_id)}</dd>
    <dt>Hash</dt><dd>${escapeHtml(page.source_hash.slice(0, 12))}</dd>
    <dt>Target Exists</dt><dd>${page.target_exists ? "yes" : "no"}</dd>
    <dt>Needs Work</dt><dd>${page.needs_translation ? "yes" : "no"}</dd>
    <dt>Issues</dt><dd>${issues}</dd>
  `;
}

async function runTranslation(dryRun) {
  if (!selectedPath) {
    singleFileLog("Select a source page first.");
    return;
  }

  setBusy(true);
  singleFileLog(dryRun ? "Running dry run..." : "Translating file...");
  try {
    const result = await translatePage({
      path: selectedPath,
      source_lang: fileSourceLang(),
      target_lang: fileTargetLang(),
      model: $("model").value.trim(),
      prompt: $("prompt").value.trim(),
      dry_run: dryRun,
    });
    singleFileLog(result);
    await loadSingleFileHealth();
    await context.refreshVaultHealth();
    await selectPage(selectedPath);
  } catch (error) {
    singleFileLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function runMetadataTranslation(dryRun) {
  if (!selectedPath) {
    singleFileLog("Select a source page first.");
    return;
  }

  setBusy(true);
  singleFileLog(dryRun ? "Running metadata dry run..." : "Translating metadata...");
  try {
    const result = await translateMetadata({
      path: selectedPath,
      source_lang: fileSourceLang(),
      target_lang: fileTargetLang(),
      model: $("model").value.trim(),
      dry_run: dryRun,
    });
    singleFileLog(result);
    await loadSingleFileHealth();
    await context.refreshVaultHealth();
    await selectPage(selectedPath);
  } catch (error) {
    singleFileLog(error.message);
  } finally {
    setBusy(false);
  }
}

function fileSourceLang() {
  return $("file-source-lang")?.value || config?.default_source_lang || "";
}

function fileTargetLang() {
  return $("file-target-lang")?.value || config?.default_target_lang || "";
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
