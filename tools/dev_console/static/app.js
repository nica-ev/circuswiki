import { api } from "./api.js";
import { $, escapeHtml } from "./dom.js";

let state = {
  config: null,
  pages: [],
  selected: null,
  details: null,
  vaultHealth: null,
  activeTab: "file-test",
  batchPlan: null,
  metadataPlan: null,
  originalGraph: null,
  originalGraphChart: null,
  originalGraphResizeObserver: null,
  originalGraphOptions: {
    showLabels: true,
    excludeSitemap: true,
    repulsion: 260,
    gravity: 0.06,
    edgeLength: 190,
    zoom: 1,
  },
  navigationScan: null,
  navigationPreview: null,
  dynamicScan: null,
  dynamicSelected: null,
  baseLabelScan: null,
  baseLabelPlan: null,
  baseLabelSelected: null,
  linkRepairScan: null,
  linkRepairSelected: null,
  linkRepairChecked: new Set(),
  sourceLinkStyleScan: null,
  sourceLinkStyleSelected: null,
  sourceLinkStyleChecked: new Set(),
  cleanupScan: null,
  cleanupSelected: null,
  cleanupChecked: new Set(),
  matrixWindow: { start: 0, end: 0 },
  matrixDrag: null,
  graphDrag: null,
};

function log(value) {
  $("log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function healthLog(value) {
  $("health-details").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

async function loadConfig() {
  const config = await api("/api/config");
  state.config = config;
  $("model").value = config.default_model;
  $("prompt").value = config.default_prompt;
  renderFileLanguageOptions(config);
  renderDynamicLanguageOptions(config);
  renderBaseLabelLanguageOptions(config);
  renderLinkRepairLanguageOptions(config);
  renderSourceLinkStyleLanguageOptions(config);
}

async function loadHealth() {
  const sourceLang = fileSourceLang();
  const targetLang = fileTargetLang();
  const health = await api(`/api/health?source_lang=${encodeURIComponent(sourceLang)}&target_lang=${encodeURIComponent(targetLang)}`);
  $("metric-total").textContent = health.total;
  $("metric-translated").textContent = health.translated;
  $("metric-needs").textContent = health.needs_translation;
  $("metric-issues").textContent = health.with_issues;
  state.pages = health.pages;
  renderPages();
}

async function loadPages() {
  const sourceLang = fileSourceLang();
  const result = await api(`/api/pages?source_lang=${encodeURIComponent(sourceLang)}`);
  state.pages = result.pages.map((source) => ({ source }));
  renderPages();
}

async function loadVaultHealth() {
  const health = await api("/api/vault-health");
  state.vaultHealth = health;
  $("metric-matrix").textContent = `${health.totals.green}/${health.totals.yellow}/${health.totals.red}`;
  renderBatchLanguageOptions();
  renderMetadataLanguageOptions();
  renderVaultHealth();
}

function renderPages() {
  const filter = $("filter").value.toLowerCase();
  const pages = state.pages.filter((page) =>
    page.source.toLowerCase().includes(filter)
  );
  $("pages").innerHTML = "";

  pages.forEach((page) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page";
    if (state.selected === page.source) {
      button.classList.add("active");
    }
    button.textContent = page.source.replace(`docs/${fileSourceLang()}/`, "");
    button.title = page.source;
    button.addEventListener("click", () => selectPage(page.source));
    $("pages").appendChild(button);
  });
}

async function selectPage(path) {
  state.selected = path;
  renderPages();
  state.details = await api(
    `/api/page?path=${encodeURIComponent(path)}&source_lang=${encodeURIComponent(fileSourceLang())}&target_lang=${encodeURIComponent(fileTargetLang())}`
  );
  renderDetails();
}

function renderDetails() {
  const page = state.details;
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
  if (!state.selected) {
    log("Select a source page first.");
    return;
  }

  setBusy(true);
  log(dryRun ? "Running dry run..." : "Translating file...");
  try {
    const result = await api("/api/translate", {
      method: "POST",
      body: JSON.stringify({
        path: state.selected,
        source_lang: fileSourceLang(),
        target_lang: fileTargetLang(),
        model: $("model").value.trim(),
        prompt: $("prompt").value.trim(),
        dry_run: dryRun,
      }),
    });
    log(result);
    await loadHealth();
    await loadVaultHealth();
    await selectPage(state.selected);
  } catch (error) {
    log(error.message);
  } finally {
    setBusy(false);
  }
}

async function runMetadataTranslation(dryRun) {
  if (!state.selected) {
    log("Select a source page first.");
    return;
  }

  setBusy(true);
  log(dryRun ? "Running metadata dry run..." : "Translating metadata...");
  try {
    const result = await api("/api/translate-metadata", {
      method: "POST",
      body: JSON.stringify({
        path: state.selected,
        source_lang: fileSourceLang(),
        target_lang: fileTargetLang(),
        model: $("model").value.trim(),
        dry_run: dryRun,
      }),
    });
    log(result);
    await loadHealth();
    await loadVaultHealth();
    await selectPage(state.selected);
  } catch (error) {
    log(error.message);
  } finally {
    setBusy(false);
  }
}

async function runMetadataRepair() {
  if (!state.vaultHealth) {
    await loadVaultHealth();
  }

  const candidates = repairCandidates();
  const progress = $("repair-progress");
  const status = $("repair-status");
  progress.max = candidates.length;
  progress.value = 0;

  if (!candidates.length) {
    status.textContent = "No yellow existing files to repair.";
    return;
  }

  setBusy(true);
  const results = [];
  try {
    for (let index = 0; index < candidates.length; index += 1) {
      const item = candidates[index];
      status.textContent = `Repairing ${index + 1}/${candidates.length}: ${item.path}`;
      const result = await api("/api/repair-metadata", {
        method: "POST",
        body: JSON.stringify({ path: item.path }),
      });
      results.push(result);
      progress.value = index + 1;
    }
    status.textContent = `Repair complete: ${results.filter((item) => item.changed).length} changed, ${results.length} processed.`;
    healthLog(results);
    await loadVaultHealth();
  } catch (error) {
    status.textContent = "Repair stopped.";
    healthLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function createBatchPlan() {
  const targetLang = $("batch-target").value;
  const maxFiles = Number($("batch-max-files").value);
  const maxSourceChars = Number($("batch-max-chars").value);
  if (!targetLang) {
    batchLog("Select a target language.");
    return;
  }
  if (!Number.isInteger(maxFiles) || maxFiles < 1) {
    batchLog("max_files must be at least 1.");
    return;
  }
  if ($("batch-max-chars").value && (!Number.isInteger(maxSourceChars) || maxSourceChars < 1)) {
    batchLog("max_source_chars must be empty or at least 1.");
    return;
  }

  setBusy(true);
  $("batch-run").disabled = true;
  $("batch-status").textContent = "Planning...";
  try {
    const plan = await api("/api/batch-plan", {
      method: "POST",
      body: JSON.stringify({
        target_lang: targetLang,
        source_lang: $("batch-source").value,
        reason: $("batch-reason").value,
        max_source_chars: $("batch-max-chars").value ? maxSourceChars : null,
        path_filter: $("batch-path-filter").value.trim(),
        max_files: maxFiles,
      }),
    });
    state.batchPlan = plan;
    renderBatchPlan();
    $("batch-run").disabled = plan.candidates.length === 0;
    $("batch-status").textContent = `Plan ready: ${plan.planned_count}/${plan.total_candidates} candidates selected.`;
  } catch (error) {
    state.batchPlan = null;
    batchLog(error.message);
    $("batch-status").textContent = "Planning failed.";
  } finally {
    setBusy(false);
    $("batch-run").disabled = !state.batchPlan || state.batchPlan.candidates.length === 0;
  }
}

async function runBatchTranslation() {
  const plan = state.batchPlan;
  if (!plan || !plan.candidates.length) {
    batchLog("Create a non-empty plan first.");
    return;
  }

  const progress = $("batch-progress");
  progress.max = plan.candidates.length;
  progress.value = 0;
  setBusy(true);
  const results = [];
  const startedAt = performance.now();

  try {
    for (let index = 0; index < plan.candidates.length; index += 1) {
      const item = plan.candidates[index];
      $("batch-status").textContent = batchProgressLabel(
        "Translating",
        index + 1,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      );
      const result = await api("/api/batch-translate-file", {
        method: "POST",
        body: JSON.stringify({
          source_path: item.source_path,
          source_lang: item.source_lang,
          target_lang: item.target_lang,
          model: $("model").value.trim(),
          prompt: $("prompt").value.trim(),
        }),
      });
      results.push(result);
      progress.value = index + 1;
      $("batch-status").textContent = batchProgressLabel(
        "Translated",
        results.length,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      );
      batchLog(results);
    }
    $("batch-status").textContent = `Batch complete: ${results.length} translated (time left: 00:00 min).`;
    await loadHealth();
    await loadVaultHealth();
  } catch (error) {
    $("batch-status").textContent = `Batch stopped after ${results.length}/${plan.candidates.length} (${batchTimeLeftLabel(
      startedAt,
      results.length,
      plan.candidates.length
    )}).`;
    batchLog({
      error: error.message,
      completed: results.length,
      total: plan.candidates.length,
      results,
    });
  } finally {
    setBusy(false);
    $("batch-run").disabled = !state.batchPlan || state.batchPlan.candidates.length === 0;
  }
}

async function createMetadataPlan() {
  const targetLang = $("metadata-target").value;
  const maxFiles = Number($("metadata-max-files").value);
  if (!targetLang) {
    metadataLog("Select a target language.");
    return;
  }
  if (!Number.isInteger(maxFiles) || maxFiles < 1) {
    metadataLog("max_files must be at least 1.");
    return;
  }

  setBusy(true);
  $("metadata-run").disabled = true;
  $("metadata-status").textContent = "Planning...";
  try {
    const plan = await api("/api/metadata-batch-plan", {
      method: "POST",
      body: JSON.stringify({
        target_lang: targetLang,
        source_lang: $("metadata-source").value,
        reason: $("metadata-reason").value,
        path_filter: $("metadata-path-filter").value.trim(),
        max_files: maxFiles,
      }),
    });
    state.metadataPlan = plan;
    renderMetadataPlan();
    $("metadata-run").disabled = plan.candidates.length === 0;
    $("metadata-status").textContent = `Plan ready: ${plan.planned_count}/${plan.total_candidates} candidates selected.`;
  } catch (error) {
    state.metadataPlan = null;
    metadataLog(error.message);
    $("metadata-status").textContent = "Planning failed.";
  } finally {
    setBusy(false);
    $("metadata-run").disabled = !state.metadataPlan || state.metadataPlan.candidates.length === 0;
  }
}

async function runMetadataBatch() {
  const plan = state.metadataPlan;
  if (!plan || !plan.candidates.length) {
    metadataLog("Create a non-empty metadata plan first.");
    return;
  }

  const progress = $("metadata-progress");
  progress.max = plan.candidates.length;
  progress.value = 0;
  setBusy(true);
  const results = [];
  const startedAt = performance.now();

  try {
    for (let index = 0; index < plan.candidates.length; index += 1) {
      const item = plan.candidates[index];
      $("metadata-status").textContent = batchProgressLabel(
        "Translating metadata",
        index + 1,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      );
      const result = await api("/api/metadata-batch-translate-file", {
        method: "POST",
        body: JSON.stringify({
          source_path: item.source_path,
          source_lang: item.source_lang,
          target_lang: item.target_lang,
          model: $("model").value.trim(),
        }),
      });
      results.push(result);
      progress.value = index + 1;
      $("metadata-status").textContent = batchProgressLabel(
        "Translated metadata",
        results.length,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      );
      metadataLog(results);
    }
    $("metadata-status").textContent = `Metadata batch complete: ${results.length} translated (time left: 00:00 min).`;
    await loadHealth();
    await loadVaultHealth();
  } catch (error) {
    $("metadata-status").textContent = `Metadata batch stopped after ${results.length}/${plan.candidates.length} (${batchTimeLeftLabel(
      startedAt,
      results.length,
      plan.candidates.length
    )}).`;
    metadataLog({
      error: error.message,
      completed: results.length,
      total: plan.candidates.length,
      results,
    });
  } finally {
    setBusy(false);
    $("metadata-run").disabled = !state.metadataPlan || state.metadataPlan.candidates.length === 0;
  }
}

function renderBatchLanguageOptions() {
  const targetSelect = $("batch-target");
  const sourceSelect = $("batch-source");
  const reasonSelect = $("batch-reason");
  const currentTarget = targetSelect.value || state.config?.default_target_lang || "all";
  const currentSource = sourceSelect.value || "all";
  const currentReason = reasonSelect.value || "all";
  const languages = state.vaultHealth?.languages || [];
  const languageNames = state.vaultHealth?.language_names || {};
  const targetOptions = [
    '<option value="all">All target languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, languageNames[language]))}</option>`),
  ];
  const sourceOptions = [
    '<option value="all">All source languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, languageNames[language]))}</option>`),
  ];
  const reasonOptions = batchReasonOptions().map(
    (reason) => `<option value="${escapeHtml(reason)}">${escapeHtml(batchReasonLabel(reason))}</option>`
  );
  targetSelect.innerHTML = targetOptions.join("");
  sourceSelect.innerHTML = sourceOptions.join("");
  reasonSelect.innerHTML = reasonOptions.join("");
  if (currentTarget === "all" || languages.includes(currentTarget)) {
    targetSelect.value = currentTarget;
  }
  if (currentSource === "all" || languages.includes(currentSource)) {
    sourceSelect.value = currentSource;
  }
  if (batchReasonOptions().includes(currentReason)) {
    reasonSelect.value = currentReason;
  }
}

function renderMetadataLanguageOptions() {
  const targetSelect = $("metadata-target");
  const sourceSelect = $("metadata-source");
  const reasonSelect = $("metadata-reason");
  if (!targetSelect || !sourceSelect || !reasonSelect) {
    return;
  }
  const currentTarget = targetSelect.value || state.config?.default_target_lang || "all";
  const currentSource = sourceSelect.value || "all";
  const currentReason = reasonSelect.value || "all";
  const languages = state.vaultHealth?.languages || [];
  const languageNames = state.vaultHealth?.language_names || {};
  const targetOptions = [
    '<option value="all">All target languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, languageNames[language]))}</option>`),
  ];
  const sourceOptions = [
    '<option value="all">All source languages</option>',
    ...languages.map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, languageNames[language]))}</option>`),
  ];
  const reasonOptions = metadataReasonOptions().map(
    (reason) => `<option value="${escapeHtml(reason)}">${escapeHtml(metadataReasonLabel(reason))}</option>`
  );
  targetSelect.innerHTML = targetOptions.join("");
  sourceSelect.innerHTML = sourceOptions.join("");
  reasonSelect.innerHTML = reasonOptions.join("");
  if (currentTarget === "all" || languages.includes(currentTarget)) {
    targetSelect.value = currentTarget;
  }
  if (currentSource === "all" || languages.includes(currentSource)) {
    sourceSelect.value = currentSource;
  }
  if (metadataReasonOptions().includes(currentReason)) {
    reasonSelect.value = currentReason;
  }
}

function renderFileLanguageOptions(config) {
  const languages = config.languages || [];
  const options = languages
    .map((language) => `<option value="${escapeHtml(language.code)}">${escapeHtml(languageLabel(language.code, language.name))}</option>`)
    .join("");
  $("file-source-lang").innerHTML = options;
  $("file-target-lang").innerHTML = options;
  $("file-source-lang").value = config.default_source_lang || languages[0]?.code || "";
  $("file-target-lang").value = config.default_target_lang || languages[0]?.code || "";
}

function renderDynamicLanguageOptions(config) {
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

function renderBaseLabelLanguageOptions(config) {
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

function renderLinkRepairLanguageOptions(config) {
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

function renderSourceLinkStyleLanguageOptions(config) {
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

function fileSourceLang() {
  return $("file-source-lang")?.value || state.config?.default_source_lang || "";
}

function fileTargetLang() {
  return $("file-target-lang")?.value || state.config?.default_target_lang || "";
}

function renderBatchPlan() {
  const plan = state.batchPlan;
  if (!plan) {
    $("batch-summary").innerHTML = "";
    $("batch-list").innerHTML = "";
    return;
  }

  $("batch-summary").innerHTML = `
    <span class="pill">Target: <strong>${escapeHtml(languageLabel(plan.target_lang, plan.target_language))}</strong></span>
    <span class="pill">Planned: <strong>${plan.planned_count}</strong></span>
    <span class="pill">Candidates: <strong>${plan.total_candidates}</strong></span>
    <span class="pill">Chars: <strong>${plan.total_source_chars}</strong></span>
    <span class="pill">Limit: <strong>${plan.max_files}</strong></span>
    <span class="pill">Source policy: <strong>${escapeHtml(formatSourcePolicy(plan.source_policy))}</strong></span>
    <span class="pill">Filters: <strong>${escapeHtml(formatBatchFilters(plan.filters || {}))}</strong></span>
    ${plan.source_counts ? `<span class="pill">By source: <strong>${escapeHtml(formatLanguageCounts(plan.source_counts, state.vaultHealth?.language_names || {}))}</strong></span>` : ""}
    ${plan.target_counts ? `<span class="pill">By language: <strong>${escapeHtml(formatTargetCounts(plan.target_counts, state.vaultHealth?.language_names || {}))}</strong></span>` : ""}
  `;

  const table = $("batch-list");
  table.innerHTML = `
    <thead>
      <tr>
        <th>#</th>
        <th>ID</th>
        <th>Source</th>
        <th>Target</th>
        <th>Chars</th>
        <th>Reason</th>
      </tr>
    </thead>
    <tbody>
      ${plan.candidates.map((item, index) => `
        <tr>
          <td>${index + 1}</td>
          <td>${escapeHtml(item.translation_id)}</td>
          <td>${escapeHtml(languageLabel(item.source_lang, item.source_language))}</td>
          <td>${escapeHtml(languageLabel(item.target_lang, item.target_language))}</td>
          <td>${item.source_chars}</td>
          <td>${escapeHtml(item.reason)}</td>
        </tr>
      `).join("")}
    </tbody>
  `;
  batchLog(plan);
}

function renderMetadataPlan() {
  const plan = state.metadataPlan;
  if (!plan) {
    $("metadata-summary").innerHTML = "";
    $("metadata-list").innerHTML = "";
    return;
  }

  $("metadata-summary").innerHTML = `
    <span class="pill">Target: <strong>${escapeHtml(languageLabel(plan.target_lang, plan.target_language))}</strong></span>
    <span class="pill">Planned: <strong>${plan.planned_count}</strong></span>
    <span class="pill">Candidates: <strong>${plan.total_candidates}</strong></span>
    <span class="pill">Metadata chars: <strong>${plan.total_metadata_chars}</strong></span>
    <span class="pill">Limit: <strong>${plan.max_files}</strong></span>
    <span class="pill">Source policy: <strong>${escapeHtml(formatSourcePolicy(plan.source_policy))}</strong></span>
    <span class="pill">Filters: <strong>${escapeHtml(formatMetadataFilters(plan.filters || {}))}</strong></span>
    ${plan.source_counts ? `<span class="pill">By source: <strong>${escapeHtml(formatLanguageCounts(plan.source_counts, state.vaultHealth?.language_names || {}))}</strong></span>` : ""}
    ${plan.target_counts ? `<span class="pill">By language: <strong>${escapeHtml(formatTargetCounts(plan.target_counts, state.vaultHealth?.language_names || {}))}</strong></span>` : ""}
  `;

  const table = $("metadata-list");
  table.innerHTML = `
    <thead>
      <tr>
        <th>#</th>
        <th>ID</th>
        <th>Source</th>
        <th>Target</th>
        <th>Source Title</th>
        <th>Target Title</th>
        <th>Desc</th>
        <th>Chars</th>
        <th>Reason</th>
      </tr>
    </thead>
    <tbody>
      ${plan.candidates.map((item, index) => `
        <tr>
          <td>${index + 1}</td>
          <td>${escapeHtml(item.translation_id)}</td>
          <td>${escapeHtml(languageLabel(item.source_lang, item.source_language))}</td>
          <td>${escapeHtml(languageLabel(item.target_lang, item.target_language))}</td>
          <td>${escapeHtml(item.source_title || "")}</td>
          <td>${escapeHtml(item.target_title || "")}</td>
          <td>${item.source_has_description ? "source" : "-"} / ${item.target_has_description ? "target" : "-"}</td>
          <td>${item.metadata_chars}</td>
          <td>${escapeHtml(metadataReasonLabel(item.reason))}</td>
        </tr>
      `).join("")}
    </tbody>
  `;
  metadataLog(plan);
}

function formatBatchTimeLeft(milliseconds) {
  const totalSeconds = Math.max(0, Math.round(milliseconds / 1000));
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;

  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")} min`;
}

function batchTimeLeftLabel(startedAt, completedCount, totalCount) {
  if (startedAt == null || completedCount < 1) {
    return "time left: --:-- min";
  }

  const elapsed = performance.now() - startedAt;
  const averagePerFile = elapsed / completedCount;
  const remainingCount = Math.max(0, totalCount - completedCount);

  return `time left: ${formatBatchTimeLeft(remainingCount * averagePerFile)}`;
}

function batchProgressLabel(action, currentCount, totalCount, translationId, startedAt, completedCount) {
  const timeLeft = batchTimeLeftLabel(startedAt, completedCount, totalCount);
  const fileLabel = translationId ? `: ${translationId}` : "";

  return `${action} ${currentCount}/${totalCount} (${timeLeft})${fileLabel}`;
}

function batchLog(value) {
  $("batch-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function metadataLog(value) {
  $("metadata-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function formatTargetCounts(counts, languageNames) {
  return formatLanguageCounts(counts, languageNames);
}

function formatLanguageCounts(counts, languageNames) {
  return Object.entries(counts)
    .map(([language, count]) => `${languageLabel(language, languageNames[language])}: ${count}`)
    .join(", ");
}

function formatSourcePolicy(policy) {
  if (policy === "canonical_source_per_translation_group") {
    return "Canonical source per group";
  }
  return policy || "default";
}

function batchReasonOptions() {
  return [
    "all",
    "missing_file",
    "fallback_page",
    "source_body_hash_mismatch",
    "missing_body_hash",
    "translation_source_lang_mismatch",
  ];
}

function batchReasonLabel(reason) {
  return {
    all: "All reasons",
    missing_file: "Missing file",
    fallback_page: "Fallback page",
    source_body_hash_mismatch: "Body hash mismatch",
    missing_body_hash: "Missing body hash",
    translation_source_lang_mismatch: "Source language mismatch",
  }[reason] || reason;
}

function metadataReasonOptions() {
  return [
    "all",
    "missing_metadata_hash",
    "metadata_hash_mismatch",
    "missing_title",
    "missing_description",
  ];
}

function metadataReasonLabel(reason) {
  return {
    all: "All reasons",
    missing_metadata_hash: "Missing metadata hash",
    metadata_hash_mismatch: "Metadata hash mismatch",
    missing_title: "Missing title",
    missing_description: "Missing description",
  }[reason] || reason;
}

function formatBatchFilters(filters) {
  const names = state.vaultHealth?.language_names || {};
  const parts = [
    `source=${languageLabel(filters.source_lang || "all", filters.source_lang === "all" ? "All source languages" : names[filters.source_lang])}`,
    `reason=${batchReasonLabel(filters.reason || "all")}`,
  ];
  if (filters.max_source_chars) {
    parts.push(`max chars=${filters.max_source_chars}`);
  }
  if (filters.path_filter) {
    parts.push(`text="${filters.path_filter}"`);
  }
  return parts.join(", ");
}

function formatMetadataFilters(filters) {
  const names = state.vaultHealth?.language_names || {};
  const parts = [
    `source=${languageLabel(filters.source_lang || "all", filters.source_lang === "all" ? "All source languages" : names[filters.source_lang])}`,
    `reason=${metadataReasonLabel(filters.reason || "all")}`,
  ];
  if (filters.path_filter) {
    parts.push(`text="${filters.path_filter}"`);
  }
  return parts.join(", ");
}

function pathWithObsidianButton(path) {
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

async function openInObsidian(path) {
  if (!path) {
    activeLog("No path selected.");
    return;
  }
  activeLog(`Opening in Obsidian: ${path}`);
  try {
    const result = await api("/api/obsidian/open", {
      method: "POST",
      body: JSON.stringify({ path, newtab: true }),
    });
    activeLog(result);
  } catch (error) {
    activeLog(error.message);
  }
}

function activeLog(value) {
  const loggers = {
    "file-test": log,
    "vault-health": healthLog,
    "batch-translate": batchLog,
    "batch-metadata": metadataLog,
    "original-graph": graphLog,
    navigation: navLog,
    dynamic: dynamicLog,
    "base-labels": baseLabelLog,
    cleanup: cleanupLog,
    "link-repair": linkRepairLog,
  };
  (loggers[state.activeTab] || log)(value);
}

function navLog(value) {
  $("nav-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function dynamicLog(value) {
  $("dynamic-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function baseLabelLog(value) {
  $("base-label-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function cleanupLog(value) {
  $("cleanup-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function linkRepairLog(value) {
  $("link-repair-log").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function graphLog(value) {
  $("graph-details").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function graphDiagnosticsLog(value) {
  $("graph-diagnostics").textContent =
    typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function readGraphControls() {
  state.originalGraphOptions.showLabels = $("graph-labels").checked;
  state.originalGraphOptions.excludeSitemap = $("graph-exclude-sitemap").checked;
  state.originalGraphOptions.repulsion = Number($("graph-repulsion").value);
  state.originalGraphOptions.gravity = Number($("graph-gravity").value);
  state.originalGraphOptions.edgeLength = Number($("graph-edge-length").value);
  updateGraphControlLabels();
}

function updateGraphControlLabels() {
  $("graph-repulsion-value").textContent = String(state.originalGraphOptions.repulsion);
  $("graph-gravity-value").textContent = state.originalGraphOptions.gravity.toFixed(2);
  $("graph-edge-length-value").textContent = String(state.originalGraphOptions.edgeLength);
}

async function loadOriginalGraph() {
  setBusy(true);
  graphLog("Loading original graph...");
  try {
    readGraphControls();
    const excludeSitemap = state.originalGraphOptions.excludeSitemap ? "true" : "false";
    const graph = await api(`/api/original-graph?exclude_sitemap=${excludeSitemap}`);
    state.originalGraph = graph;
    renderOriginalGraphSummary();
    renderOriginalGraph();
    graphDiagnosticsLog(graph.diagnostics?.slice(0, 80) || []);
  } catch (error) {
    graphLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderOriginalGraphSummary() {
  const graph = state.originalGraph;
  if (!graph) {
    $("graph-summary").innerHTML = "";
    return;
  }
  const counts = formatLanguageCounts(graph.summary?.language_counts || {}, languageNamesFromConfig());
  $("graph-summary").innerHTML = `
    <span class="pill">Originals: <strong>${graph.summary?.node_count || 0}</strong></span>
    <span class="pill">Edges: <strong>${graph.summary?.edge_count || 0}</strong></span>
    <span class="pill ${graph.summary?.diagnostic_count ? "yellow" : "green"}">Diagnostics: <strong>${graph.summary?.diagnostic_count || 0}</strong></span>
    <span class="pill">Excluded: <strong>${escapeHtml((graph.summary?.excluded_relative_paths || []).join(", ") || "none")}</strong></span>
    <span class="pill">Languages: <strong>${escapeHtml(counts || "none")}</strong></span>
  `;
}

function renderOriginalGraph() {
  const graph = state.originalGraph;
  if (!graph) {
    return;
  }
  if (!window.echarts) {
    graphLog("ECharts failed to load. Check the CDN connection or vendor ECharts locally.");
    return;
  }

  const element = $("original-graph-chart");
  if (!state.originalGraphChart) {
    state.originalGraphChart = window.echarts.init(element, null, { renderer: "canvas" });
    state.originalGraphChart.on("click", (params) => {
      graphLog(params.data || params);
    });
    element.addEventListener("wheel", graphWheel, { passive: false });
    element.addEventListener("pointerdown", startGraphDrag);
    element.addEventListener("pointermove", updateGraphDrag);
    element.addEventListener("pointerup", stopGraphDrag);
    element.addEventListener("pointercancel", stopGraphDrag);
    element.addEventListener("lostpointercapture", stopGraphDrag);
    state.originalGraphResizeObserver = new ResizeObserver(() => resizeOriginalGraphChart());
    state.originalGraphResizeObserver.observe(element);
  }
  resizeOriginalGraphChart();
  readGraphControls();
  const options = state.originalGraphOptions;

  const categories = (graph.categories || []).map((category) => ({
    name: category.name,
    itemStyle: { color: graphLanguageColor(category.name) },
  }));
  const data = (graph.nodes || []).map((node) => ({
    ...node,
    itemStyle: { color: graphLanguageColor(node.lang) },
    label: { show: options.showLabels && node.value > 1 },
    tooltip: {
      formatter: [
        `<strong>${escapeHtml(node.title)}</strong>`,
        `${escapeHtml(node.language)} (${escapeHtml(node.lang)})`,
        `${escapeHtml(node.path)}`,
        `in: ${node.in_degree} | out: ${node.out_degree}`,
      ].join("<br>"),
    },
  }));
  const links = (graph.edges || []).map((edge) => ({
    ...edge,
    lineStyle: { width: Math.min(5, 1 + Number(edge.value || 1)), opacity: 0.48 },
    tooltip: {
      formatter: [
        `${escapeHtml(edge.source)} -> ${escapeHtml(edge.target)}`,
        `links: ${edge.value}`,
        ...(edge.links || []).slice(0, 4).map((link) => escapeHtml(link.resolved_path || link.target)),
      ].join("<br>"),
    },
  }));

  state.originalGraphChart.setOption({
    backgroundColor: "transparent",
    tooltip: { trigger: "item", confine: true },
    legend: [{
      data: categories.map((category) => category.name),
      textStyle: { color: "#9aa89d" },
      top: 8,
      left: 8,
    }],
    series: [{
      type: "graph",
      layout: "force",
      roam: true,
      draggable: true,
      zoom: options.zoom,
      data,
      links,
      categories,
      edgeSymbol: ["none", "arrow"],
      edgeSymbolSize: 7,
      label: {
        color: "#edf4eb",
        formatter: (params) => params.data.title || params.data.name,
        position: "right",
      },
      emphasis: {
        focus: "adjacency",
        lineStyle: { opacity: 0.95 },
      },
      force: {
        repulsion: options.repulsion,
        gravity: options.gravity,
        edgeLength: [Math.max(30, Math.round(options.edgeLength * 0.45)), options.edgeLength],
      },
      lineStyle: {
        color: "source",
        curveness: 0.08,
      },
    }],
  }, true);
  resizeOriginalGraphChart();
  setTimeout(resizeOriginalGraphChart, 0);
}

function resizeOriginalGraphChart() {
  if (!state.originalGraphChart) {
    return;
  }
  const element = $("original-graph-chart");
  const rect = element.getBoundingClientRect();
  state.originalGraphChart.resize({
    width: Math.max(1, Math.floor(rect.width)),
    height: Math.max(1, Math.floor(rect.height)),
  });
}

function fitOriginalGraph() {
  if (state.originalGraphChart) {
    state.originalGraphOptions.zoom = 1;
    state.originalGraphChart.dispatchAction({ type: "restore" });
    renderOriginalGraph();
  }
}

function zoomOriginalGraph(factor) {
  state.originalGraphOptions.zoom = Math.max(
    0.15,
    Math.min(5, state.originalGraphOptions.zoom * factor)
  );
  renderOriginalGraph();
}

function updateOriginalGraphForces() {
  readGraphControls();
  renderOriginalGraph();
}

function graphWheel(event) {
  if (!state.originalGraphChart) {
    return;
  }
  event.preventDefault();
  const zoom = event.deltaY < 0 ? 1.12 : 0.89;
  state.originalGraphOptions.zoom = Math.max(
    0.15,
    Math.min(5, state.originalGraphOptions.zoom * zoom)
  );
  state.originalGraphChart.dispatchAction({
    type: "graphRoam",
    seriesIndex: 0,
    zoom,
    originX: event.offsetX,
    originY: event.offsetY,
  });
}

function startGraphDrag(event) {
  if (!state.originalGraphChart || event.button !== 0) {
    return;
  }
  event.preventDefault();
  $("original-graph-chart").setPointerCapture(event.pointerId);
  state.graphDrag = {
    pointerId: event.pointerId,
    x: event.clientX,
    y: event.clientY,
  };
}

function updateGraphDrag(event) {
  const drag = state.graphDrag;
  if (!drag || drag.pointerId !== event.pointerId || !state.originalGraphChart) {
    return;
  }
  event.preventDefault();
  const dx = event.clientX - drag.x;
  const dy = event.clientY - drag.y;
  drag.x = event.clientX;
  drag.y = event.clientY;
  state.originalGraphChart.dispatchAction({
    type: "graphRoam",
    seriesIndex: 0,
    dx,
    dy,
  });
}

function stopGraphDrag(event) {
  if (!state.graphDrag) {
    return;
  }
  if (event?.pointerId && event.pointerId !== state.graphDrag.pointerId) {
    return;
  }
  state.graphDrag = null;
}

function graphLanguageColor(language) {
  const palette = {
    de: "#e0a64b",
    en: "#5fb3d9",
    pl: "#d95f76",
    hu: "#8fd95f",
    it: "#5fd997",
    nl: "#d98e5f",
    el: "#9b7bda",
    es: "#d9c95f",
    uk: "#5f7ed9",
    pt: "#59c2b0",
    cs: "#c878d8",
    sk: "#88a85c",
  };
  return palette[language] || "#9aa89d";
}

function languageNamesFromConfig() {
  return Object.fromEntries((state.config?.languages || []).map((language) => [language.code, language.name]));
}

async function loadDynamicScan() {
  setBusy(true);
  dynamicLog("Scanning dynamic pages...");
  try {
    const language = $("dynamic-language").value || "";
    const query = language ? `?language=${encodeURIComponent(language)}` : "";
    const scan = await api(`/api/dynamic/scan${query}`);
    state.dynamicScan = scan;
    if (state.dynamicSelected && !scan.pages.some((page) => page.path === state.dynamicSelected)) {
      state.dynamicSelected = null;
    }
    renderDynamicScan();
    dynamicLog(scan);
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
    const path = state.dynamicSelected || "";
    const params = new URLSearchParams();
    if (language) {
      params.set("language", language);
    }
    if (path) {
      params.set("path", path);
    }
    const result = await api(`/api/dynamic/check?${params.toString()}`);
    dynamicLog(result);
  } catch (error) {
    dynamicLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewDynamicSelected() {
  await runDynamicRefresh(true, state.dynamicSelected || "");
}

async function refreshDynamicSelected() {
  await runDynamicRefresh(false, state.dynamicSelected || "");
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
    const result = await api(dryRun ? "/api/dynamic/preview" : "/api/dynamic/refresh", {
      method: "POST",
      body: JSON.stringify({
        path,
        language: path ? "" : $("dynamic-language").value,
      }),
    });
    dynamicLog(result);
  } catch (error) {
    dynamicLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderDynamicScan() {
  const scan = state.dynamicScan;
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
    if (state.dynamicSelected === page.path) {
      button.classList.add("active");
    }
    button.textContent = `${page.language || "?"} | ${page.title}`;
    button.title = page.path;
    button.addEventListener("click", () => {
      state.dynamicSelected = page.path;
      renderDynamicScan();
      dynamicLog(page);
    });
    $("dynamic-pages").appendChild(button);
  });
  renderDynamicDetails();
}

function renderDynamicDetails() {
  const page = state.dynamicScan?.pages.find((item) => item.path === state.dynamicSelected);
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

async function loadBaseLabelScan() {
  setBusy(true);
  baseLabelLog("Scanning base display names...");
  try {
    const scan = await api("/api/base-labels/scan");
    state.baseLabelScan = scan;
    updateBaseLabelBaseOptions();
    renderBaseLabelScan();
    baseLabelLog(scan);
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
    const plan = await api(`/api/base-labels/plan?${params.toString()}`);
    state.baseLabelPlan = plan;
    renderBaseLabelPlan();
    baseLabelLog(plan);
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
    const result = await api("/api/base-labels/translate", {
      method: "POST",
      body: JSON.stringify({
        base: $("base-label-base").value,
        target_lang: $("base-label-language").value || "all",
        model: $("model").value.trim(),
      }),
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
    const result = await api("/api/base-labels/materialize", {
      method: "POST",
      body: JSON.stringify({
        base: $("base-label-base").value,
        target_lang: $("base-label-language").value || "all",
      }),
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
  if (!select || !state.baseLabelScan) {
    return;
  }
  const current = select.value;
  select.innerHTML = [
    '<option value="">All base files</option>',
    ...state.baseLabelScan.bases.map((base) => `<option value="${escapeHtml(base.path)}">${escapeHtml(base.path)}</option>`),
  ].join("");
  if (!current || state.baseLabelScan.bases.some((base) => base.path === current)) {
    select.value = current;
  }
}

function baseLabelRows() {
  const scan = state.baseLabelScan;
  if (!scan) {
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
  const scan = state.baseLabelScan;
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
    if (state.baseLabelSelected === id) {
      button.classList.add("active");
    }
    button.textContent = `${row.key} | ${row.source}`;
    button.title = row.base;
    button.addEventListener("click", () => {
      state.baseLabelSelected = id;
      renderBaseLabelScan();
      baseLabelLog(row);
    });
    $("base-label-list").appendChild(button);
  });
  renderBaseLabelDetails();
}

function renderBaseLabelDetails() {
  const rows = baseLabelRows();
  const row = rows.find((item) => `${item.base}::${item.key}` === state.baseLabelSelected);
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
  const plan = state.baseLabelPlan;
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

async function loadLinkRepairScan() {
  setBusy(true);
  linkRepairLog("Scanning translated link targets...");
  try {
    const language = $("link-repair-language").value || "";
    const query = language ? `?language=${encodeURIComponent(language)}` : "";
    const scan = await api(`/api/link-repair/scan${query}`);
    state.linkRepairScan = scan;
    const currentPaths = new Set(scan.items.map((item) => item.path));
    state.linkRepairChecked = new Set([...state.linkRepairChecked].filter((path) => currentPaths.has(path)));
    if (state.linkRepairSelected && !currentPaths.has(state.linkRepairSelected)) {
      state.linkRepairSelected = null;
    }
    renderLinkRepairScan();
    linkRepairLog(scan);
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewLinkRepairSelected() {
  if (!state.linkRepairSelected) {
    linkRepairLog("Select a link repair item first.");
    return;
  }
  setBusy(true);
  linkRepairLog("Previewing link repair...");
  try {
    const result = await api(`/api/link-repair/preview?path=${encodeURIComponent(state.linkRepairSelected)}`);
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
  const paths = [...state.linkRepairChecked];
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
    const result = await api("/api/link-repair/repair", {
      method: "POST",
      body: JSON.stringify({ paths }),
    });
    state.linkRepairChecked.clear();
    linkRepairLog(result);
    await loadLinkRepairScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairAllSafeLinkItems() {
  const count = state.linkRepairScan?.safe_count || 0;
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
    const result = await api("/api/link-repair/repair-all", {
      method: "POST",
      body: JSON.stringify({ language: $("link-repair-language").value || "" }),
    });
    state.linkRepairChecked.clear();
    linkRepairLog(result);
    await loadLinkRepairScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderLinkRepairScan() {
  const scan = state.linkRepairScan;
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
    if (state.linkRepairSelected === item.path) {
      row.classList.add("active");
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.disabled = !item.safe_repair;
    checkbox.checked = state.linkRepairChecked.has(item.path);
    checkbox.title = item.safe_repair ? "Select for repair" : "Not safely repairable";
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        state.linkRepairChecked.add(item.path);
      } else {
        state.linkRepairChecked.delete(item.path);
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
      state.linkRepairSelected = item.path;
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
  const selected = state.linkRepairScan?.items.find((item) => item.path === state.linkRepairSelected);
  if (!selected) {
    $("link-repair-details").innerHTML = `
      <dt>Checked</dt><dd>${state.linkRepairChecked.size}</dd>
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
    <dt>Checked</dt><dd>${state.linkRepairChecked.size}</dd>
  `;
}

async function loadSourceLinkStyleScan() {
  setBusy(true);
  linkRepairLog("Scanning original source link styles...");
  try {
    const language = $("source-link-style-language").value || "";
    const query = language ? `?language=${encodeURIComponent(language)}` : "";
    const scan = await api(`/api/source-link-style/scan${query}`);
    state.sourceLinkStyleScan = scan;
    const currentPaths = new Set(scan.items.map((item) => item.path));
    state.sourceLinkStyleChecked = new Set([...state.sourceLinkStyleChecked].filter((path) => currentPaths.has(path)));
    if (state.sourceLinkStyleSelected && !currentPaths.has(state.sourceLinkStyleSelected)) {
      state.sourceLinkStyleSelected = null;
    }
    renderSourceLinkStyleScan();
    linkRepairLog(scan);
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function previewSourceLinkStyleSelected() {
  if (!state.sourceLinkStyleSelected) {
    linkRepairLog("Select a source style item first.");
    return;
  }
  setBusy(true);
  linkRepairLog("Previewing source link style repair...");
  try {
    const result = await api(`/api/source-link-style/preview?path=${encodeURIComponent(state.sourceLinkStyleSelected)}`);
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

async function repairSelectedSourceLinkStyles() {
  const paths = [...state.sourceLinkStyleChecked];
  if (!paths.length) {
    linkRepairLog("Select at least one source style item first.");
    return;
  }
  if (!window.confirm(`Repair source image syntax in ${paths.length} original file(s)?`)) {
    return;
  }
  setBusy(true);
  linkRepairLog("Repairing selected source link styles...");
  try {
    const result = await api("/api/source-link-style/repair", {
      method: "POST",
      body: JSON.stringify({ paths }),
    });
    state.sourceLinkStyleChecked.clear();
    linkRepairLog(result);
    await loadSourceLinkStyleScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function repairAllSafeSourceLinkStyles() {
  const count = state.sourceLinkStyleScan?.safe_count || 0;
  if (!count) {
    linkRepairLog("No safe source style repairs found.");
    return;
  }
  if (!window.confirm(`Repair all ${count} original source file(s)?`)) {
    return;
  }
  setBusy(true);
  linkRepairLog("Repairing all safe source link styles...");
  try {
    const result = await api("/api/source-link-style/repair-all", {
      method: "POST",
      body: JSON.stringify({ language: $("source-link-style-language").value || "" }),
    });
    state.sourceLinkStyleChecked.clear();
    linkRepairLog(result);
    await loadSourceLinkStyleScan();
  } catch (error) {
    linkRepairLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderSourceLinkStyleScan() {
  const scan = state.sourceLinkStyleScan;
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
    if (state.sourceLinkStyleSelected === item.path) {
      row.classList.add("active");
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.disabled = !item.safe_repair;
    checkbox.checked = state.sourceLinkStyleChecked.has(item.path);
    checkbox.title = item.safe_repair ? "Select for repair" : "Not safely repairable";
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        state.sourceLinkStyleChecked.add(item.path);
      } else {
        state.sourceLinkStyleChecked.delete(item.path);
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
      state.sourceLinkStyleSelected = item.path;
      renderSourceLinkStyleScan();
      linkRepairLog(item);
    });

    row.appendChild(checkbox);
    row.appendChild(button);
    $("source-link-style-list").appendChild(row);
  });
  renderSourceLinkStyleDetails();
}

function renderSourceLinkStyleDetails() {
  const selected = state.sourceLinkStyleScan?.items.find((item) => item.path === state.sourceLinkStyleSelected);
  if (!selected) {
    $("source-link-style-details").innerHTML = `
      <dt>Checked</dt><dd>${state.sourceLinkStyleChecked.size}</dd>
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
    <dt>Checked</dt><dd>${state.sourceLinkStyleChecked.size}</dd>
  `;
}

async function loadCleanupScan() {
  setBusy(true);
  cleanupLog("Scanning orphan translations...");
  try {
    const scan = await api("/api/cleanup/orphans");
    state.cleanupScan = scan;
    const currentPaths = new Set(scan.items.map((item) => item.path));
    state.cleanupChecked = new Set([...state.cleanupChecked].filter((path) => currentPaths.has(path)));
    if (state.cleanupSelected && !currentPaths.has(state.cleanupSelected)) {
      state.cleanupSelected = null;
    }
    renderCleanupScan();
    cleanupLog(scan);
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function deleteSelectedCleanupItems() {
  const paths = [...state.cleanupChecked];
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
    const result = await api("/api/cleanup/delete-orphans", {
      method: "POST",
      body: JSON.stringify({ paths }),
    });
    state.cleanupChecked.clear();
    cleanupLog(result);
    await loadCleanupScan();
    await loadVaultHealth();
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function deleteAllCleanupItems() {
  const count = state.cleanupScan?.deletable_count || 0;
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
    const result = await api("/api/cleanup/delete-all-orphans", {
      method: "POST",
      body: JSON.stringify({}),
    });
    state.cleanupChecked.clear();
    cleanupLog(result);
    await loadCleanupScan();
    await loadVaultHealth();
  } catch (error) {
    cleanupLog(error.message);
  } finally {
    setBusy(false);
  }
}

function renderCleanupScan() {
  const scan = state.cleanupScan;
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
    if (state.cleanupSelected === item.path) {
      row.classList.add("active");
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.disabled = !item.deletable;
    checkbox.checked = state.cleanupChecked.has(item.path);
    checkbox.title = item.deletable ? "Select for deletion" : "Not safely deletable";
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        state.cleanupChecked.add(item.path);
      } else {
        state.cleanupChecked.delete(item.path);
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
      state.cleanupSelected = item.path;
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
  const selected = state.cleanupScan?.items.find((item) => item.path === state.cleanupSelected);
  if (!selected) {
    $("cleanup-details").innerHTML = `
      <dt>Checked</dt><dd>${state.cleanupChecked.size}</dd>
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
    <dt>Checked</dt><dd>${state.cleanupChecked.size}</dd>
  `;
}

async function loadNavigationScan() {
  setBusy(true);
  navLog("Scanning navigation...");
  try {
    const scan = await api("/api/navigation/scan");
    state.navigationScan = scan;
    $("nav-model").value = JSON.stringify(scan.model, null, 2);
    renderNavigationLanguageOptions();
    renderNavigationScan();
    navLog(scan);
  } catch (error) {
    navLog(error.message);
  } finally {
    setBusy(false);
  }
}

async function initNavigationModel() {
  const sourceLang = $("nav-source").value || state.config?.default_source_lang || "";
  if (!sourceLang) {
    navLog("Select a navigation source language.");
    return;
  }
  setBusy(true);
  navLog(`Creating canonical model from ${sourceLang} nav...`);
  try {
    const result = await api("/api/navigation/init", {
      method: "POST",
      body: JSON.stringify({ language: sourceLang }),
    });
    $("nav-model").value = JSON.stringify(result.model, null, 2);
    state.navigationPreview = result.preview;
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
  const sourceLang = $("nav-source").value || state.config?.default_source_lang || "";
  if (!sourceLang) {
    navLog("Select a navigation source language.");
    return;
  }

  setBusy(true);
  navLog(`Translating navigation labels from ${sourceLang} to all other configured languages...`);
  try {
    const result = await api("/api/navigation/translate-all-labels", {
      method: "POST",
      body: JSON.stringify({
        model,
        source_lang: sourceLang,
        llm_model: $("model").value.trim(),
      }),
    });
    $("nav-model").value = JSON.stringify(result.model, null, 2);
    state.navigationPreview = result.preview;
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
    const preview = await api("/api/navigation/preview", {
      method: "POST",
      body: JSON.stringify({ model }),
    });
    state.navigationPreview = preview;
    renderNavigationPreview();
    navLog(preview);
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
    state.navigationPreview = await api("/api/navigation/preview", {
      method: "POST",
      body: JSON.stringify({ model }),
    });
    renderNavigationPreview();
    const result = await api("/api/navigation/apply", {
      method: "POST",
      body: JSON.stringify({ model }),
    });
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
  const scan = state.navigationScan;
  if (!scan) {
    select.innerHTML = "";
    return;
  }
  const current = select.value || state.config?.default_source_lang || scan.languages[0] || "";
  select.innerHTML = scan.languages
    .map((language) => `<option value="${escapeHtml(language)}">${escapeHtml(languageLabel(language, scan.language_names[language]))}</option>`)
    .join("");
  if (scan.languages.includes(current)) {
    select.value = current;
  }
}

function renderNavigationScan() {
  const scan = state.navigationScan;
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
  const preview = state.navigationPreview;
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

function repairCandidates() {
  const seen = new Set();
  const candidates = [];
  for (const row of state.vaultHealth?.rows || []) {
    for (const language of state.vaultHealth.languages) {
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
  const health = state.vaultHealth;
  if (!health) {
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
    state.matrixWindow = { start: 0, end: 0 };
    return state.matrixWindow;
  }

  let start = Number.isInteger(state.matrixWindow.start) ? state.matrixWindow.start : 0;
  let end = Number.isInteger(state.matrixWindow.end) && state.matrixWindow.end > 0
    ? state.matrixWindow.end
    : rowCount;

  start = Math.max(0, Math.min(start, rowCount - 1));
  end = Math.max(start + 1, Math.min(end, rowCount));
  state.matrixWindow = { start, end };
  return state.matrixWindow;
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
  state.matrixWindow = { start, end };
  renderVaultHealth();
}

function filteredVaultRows() {
  const health = state.vaultHealth;
  if (!health) {
    return [];
  }
  const query = $("health-filter").value.toLowerCase();
  const statusFilter = $("health-status").value;
  return health.rows.filter((row) => matchesHealthFilter(row, query, statusFilter));
}

function matrixIndexFromPointer(event) {
  const rows = filteredVaultRows();
  const rowCount = rows.length;
  if (!rowCount) {
    return 0;
  }

  const rect = $("matrix-window-range").getBoundingClientRect();
  const ratio = Math.max(0, Math.min(1, (event.clientX - rect.left) / rect.width));
  return Math.round(ratio * rowCount);
}

function startMatrixDrag(kind, event) {
  const rows = filteredVaultRows();
  if (!rows.length) {
    return;
  }

  event.preventDefault();
  const window = normalizedMatrixWindow(rows.length);
  state.matrixDrag = {
    kind,
    pointerStart: matrixIndexFromPointer(event),
    start: window.start,
    end: window.end,
    width: window.end - window.start,
  };
  $("matrix-window-start").classList.toggle("active", kind === "start");
  $("matrix-window-end").classList.toggle("active", kind === "end");
}

function updateMatrixDrag(event) {
  const drag = state.matrixDrag;
  if (!drag) {
    return;
  }

  const rowCount = filteredVaultRows().length;
  if (!rowCount) {
    return;
  }

  const pointer = matrixIndexFromPointer(event);
  if (drag.kind === "start") {
    setMatrixWindow(Math.max(0, Math.min(pointer, drag.end - 1)), drag.end);
    return;
  }
  if (drag.kind === "end") {
    setMatrixWindow(drag.start, Math.max(drag.start + 1, Math.min(pointer, rowCount)));
    return;
  }

  const delta = pointer - drag.pointerStart;
  const nextStart = Math.max(0, Math.min(drag.start + delta, rowCount - drag.width));
  setMatrixWindow(nextStart, nextStart + drag.width);
}

function stopMatrixDrag() {
  state.matrixDrag = null;
  $("matrix-window-start").classList.remove("active");
  $("matrix-window-end").classList.remove("active");
}

function matchesHealthFilter(row, query, statusFilter) {
  const cells = Object.values(row.cells);
  if (statusFilter !== "all" && !cells.some((cell) => cell.status === statusFilter)) {
    return false;
  }
  if (!query) {
    return true;
  }
  const haystack = [
    row.translation_id,
    row.title,
    row.relative_path,
    row.source_lang,
    ...cells.flatMap((cell) => [cell.path, cell.relative_path, ...cell.issues]),
  ].join(" ").toLowerCase();
  return haystack.includes(query);
}

function matrixLayoutSizes() {
  const styles = getComputedStyle(document.documentElement);
  return {
    labelWidth: cssPixelValue(styles.getPropertyValue("--matrix-label-width"), 82),
    minPlotWidth: cssPixelValue(styles.getPropertyValue("--matrix-min-plot-width"), 1320),
  };
}

function cssPixelValue(value, fallback) {
  const parsed = Number.parseFloat(String(value).trim());
  return Number.isFinite(parsed) ? parsed : fallback;
}

function switchTab(tabName) {
  state.activeTab = tabName;
  document.querySelectorAll(".tab").forEach((button) => {
    button.classList.toggle("active", button.dataset.tab === tabName);
  });
  document.querySelectorAll(".tab-panel").forEach((panel) => {
    panel.classList.toggle("active", panel.id === `tab-${tabName}`);
  });
  if (tabName === "vault-health" && !state.vaultHealth) {
    loadVaultHealth().catch((error) => healthLog(error.message));
  }
  if (tabName === "navigation" && !state.navigationScan) {
    loadNavigationScan().catch((error) => navLog(error.message));
  }
  if (tabName === "original-graph") {
    if (!state.originalGraph) {
      loadOriginalGraph().catch((error) => graphLog(error.message));
    } else {
      setTimeout(resizeOriginalGraphChart, 0);
    }
  }
  if (tabName === "dynamic" && !state.dynamicScan) {
    loadDynamicScan().catch((error) => dynamicLog(error.message));
  }
  if (tabName === "base-labels" && !state.baseLabelScan) {
    loadBaseLabelScan().catch((error) => baseLabelLog(error.message));
  }
  if (tabName === "link-repair" && !state.linkRepairScan) {
    loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
  }
  if (tabName === "link-repair" && !state.sourceLinkStyleScan) {
    loadSourceLinkStyleScan().catch((error) => linkRepairLog(error.message));
  }
  if (tabName === "cleanup" && !state.cleanupScan) {
    loadCleanupScan().catch((error) => cleanupLog(error.message));
  }
}

function setBusy(isBusy) {
  $("dry-run").disabled = isBusy;
  $("translate").disabled = isBusy;
  $("translate-metadata").disabled = isBusy;
  $("refresh").disabled = isBusy;
  $("refresh-health").disabled = isBusy;
  $("repair-health").disabled = isBusy;
  $("batch-plan").disabled = isBusy;
  $("metadata-plan").disabled = isBusy;
  $("graph-refresh").disabled = isBusy;
  $("graph-fit").disabled = isBusy;
  $("graph-zoom-in").disabled = isBusy;
  $("graph-zoom-out").disabled = isBusy;
  $("nav-scan").disabled = isBusy;
  $("nav-init").disabled = isBusy;
  $("nav-translate").disabled = isBusy;
  $("nav-preview").disabled = isBusy;
  $("nav-apply").disabled = isBusy;
  $("dynamic-scan").disabled = isBusy;
  $("dynamic-check").disabled = isBusy;
  $("dynamic-preview").disabled = isBusy;
  $("dynamic-refresh-selected").disabled = isBusy;
  $("dynamic-refresh-all").disabled = isBusy;
  $("base-label-scan").disabled = isBusy;
  $("base-label-plan").disabled = isBusy;
  $("base-label-translate").disabled = isBusy;
  $("base-label-materialize").disabled = isBusy;
  $("link-repair-scan").disabled = isBusy;
  $("link-repair-preview").disabled = isBusy;
  $("link-repair-selected").disabled = isBusy;
  $("link-repair-all").disabled = isBusy;
  $("source-link-style-scan").disabled = isBusy;
  $("source-link-style-preview").disabled = isBusy;
  $("source-link-style-selected").disabled = isBusy;
  $("source-link-style-all").disabled = isBusy;
  $("cleanup-scan").disabled = isBusy;
  $("cleanup-delete-selected").disabled = isBusy;
  $("cleanup-delete-all").disabled = isBusy;
  if (isBusy) {
    $("batch-run").disabled = true;
    $("metadata-run").disabled = true;
  }
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

document.querySelectorAll(".tab").forEach((button) => {
  button.addEventListener("click", () => switchTab(button.dataset.tab));
});

document.addEventListener("click", (event) => {
  const button = event.target.closest(".obsidian-open");
  if (!button) {
    return;
  }
  openInObsidian(button.dataset.obsidianPath || "").catch((error) => activeLog(error.message));
});

$("filter").addEventListener("input", renderPages);
$("refresh").addEventListener("click", () => {
  loadHealth().catch((error) => log(error.message));
  loadVaultHealth().catch((error) => healthLog(error.message));
});
$("file-source-lang").addEventListener("change", () => {
  state.selected = null;
  state.details = null;
  renderDetails();
  loadHealth().catch((error) => log(error.message));
});
$("file-target-lang").addEventListener("change", () => {
  if (state.selected) {
    selectPage(state.selected).catch((error) => log(error.message));
  }
  loadHealth().catch((error) => log(error.message));
});
$("refresh-health").addEventListener("click", () => {
  loadVaultHealth().catch((error) => healthLog(error.message));
});
$("repair-health").addEventListener("click", () => {
  runMetadataRepair().catch((error) => healthLog(error.message));
});
$("batch-plan").addEventListener("click", () => {
  createBatchPlan().catch((error) => batchLog(error.message));
});
$("batch-run").addEventListener("click", () => {
  runBatchTranslation().catch((error) => batchLog(error.message));
});
$("metadata-plan").addEventListener("click", () => {
  createMetadataPlan().catch((error) => metadataLog(error.message));
});
$("metadata-run").addEventListener("click", () => {
  runMetadataBatch().catch((error) => metadataLog(error.message));
});
$("graph-refresh").addEventListener("click", () => {
  loadOriginalGraph().catch((error) => graphLog(error.message));
});
$("graph-fit").addEventListener("click", fitOriginalGraph);
$("graph-zoom-in").addEventListener("click", () => zoomOriginalGraph(1.25));
$("graph-zoom-out").addEventListener("click", () => zoomOriginalGraph(0.8));
$("graph-labels").addEventListener("change", updateOriginalGraphForces);
$("graph-exclude-sitemap").addEventListener("change", () => {
  loadOriginalGraph().catch((error) => graphLog(error.message));
});
$("graph-repulsion").addEventListener("input", updateOriginalGraphForces);
$("graph-gravity").addEventListener("input", updateOriginalGraphForces);
$("graph-edge-length").addEventListener("input", updateOriginalGraphForces);
$("nav-scan").addEventListener("click", () => {
  loadNavigationScan().catch((error) => navLog(error.message));
});
$("nav-init").addEventListener("click", () => {
  initNavigationModel().catch((error) => navLog(error.message));
});
$("nav-translate").addEventListener("click", () => {
  translateNavigationLabels().catch((error) => navLog(error.message));
});
$("nav-preview").addEventListener("click", () => {
  previewNavigationModel().catch((error) => navLog(error.message));
});
$("nav-apply").addEventListener("click", () => {
  applyNavigationModel().catch((error) => navLog(error.message));
});
$("dynamic-scan").addEventListener("click", () => {
  loadDynamicScan().catch((error) => dynamicLog(error.message));
});
$("dynamic-check").addEventListener("click", () => {
  checkDynamicPages().catch((error) => dynamicLog(error.message));
});
$("dynamic-preview").addEventListener("click", () => {
  previewDynamicSelected().catch((error) => dynamicLog(error.message));
});
$("dynamic-refresh-selected").addEventListener("click", () => {
  refreshDynamicSelected().catch((error) => dynamicLog(error.message));
});
$("dynamic-refresh-all").addEventListener("click", () => {
  refreshAllDynamicPages().catch((error) => dynamicLog(error.message));
});
$("dynamic-language").addEventListener("change", () => {
  state.dynamicSelected = null;
  loadDynamicScan().catch((error) => dynamicLog(error.message));
});
$("dynamic-filter").addEventListener("input", renderDynamicScan);
$("base-label-scan").addEventListener("click", () => {
  loadBaseLabelScan().catch((error) => baseLabelLog(error.message));
});
$("base-label-plan").addEventListener("click", () => {
  planBaseLabels().catch((error) => baseLabelLog(error.message));
});
$("base-label-translate").addEventListener("click", () => {
  translateBaseLabels().catch((error) => baseLabelLog(error.message));
});
$("base-label-materialize").addEventListener("click", () => {
  materializeBaseLabels().catch((error) => baseLabelLog(error.message));
});
$("base-label-base").addEventListener("change", () => {
  state.baseLabelSelected = null;
  renderBaseLabelScan();
});
$("base-label-language").addEventListener("change", () => {
  state.baseLabelPlan = null;
});
$("base-label-filter").addEventListener("input", renderBaseLabelScan);
$("link-repair-scan").addEventListener("click", () => {
  loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
});
$("link-repair-preview").addEventListener("click", () => {
  previewLinkRepairSelected().catch((error) => linkRepairLog(error.message));
});
$("link-repair-selected").addEventListener("click", () => {
  repairSelectedLinkItems().catch((error) => linkRepairLog(error.message));
});
$("link-repair-all").addEventListener("click", () => {
  repairAllSafeLinkItems().catch((error) => linkRepairLog(error.message));
});
$("link-repair-language").addEventListener("change", () => {
  state.linkRepairSelected = null;
  state.linkRepairChecked.clear();
  loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
});
$("link-repair-filter").addEventListener("input", renderLinkRepairScan);
$("source-link-style-scan").addEventListener("click", () => {
  loadSourceLinkStyleScan().catch((error) => linkRepairLog(error.message));
});
$("source-link-style-preview").addEventListener("click", () => {
  previewSourceLinkStyleSelected().catch((error) => linkRepairLog(error.message));
});
$("source-link-style-selected").addEventListener("click", () => {
  repairSelectedSourceLinkStyles().catch((error) => linkRepairLog(error.message));
});
$("source-link-style-all").addEventListener("click", () => {
  repairAllSafeSourceLinkStyles().catch((error) => linkRepairLog(error.message));
});
$("source-link-style-language").addEventListener("change", () => {
  state.sourceLinkStyleSelected = null;
  state.sourceLinkStyleChecked.clear();
  loadSourceLinkStyleScan().catch((error) => linkRepairLog(error.message));
});
$("source-link-style-filter").addEventListener("input", renderSourceLinkStyleScan);
$("cleanup-scan").addEventListener("click", () => {
  loadCleanupScan().catch((error) => cleanupLog(error.message));
});
$("cleanup-delete-selected").addEventListener("click", () => {
  deleteSelectedCleanupItems().catch((error) => cleanupLog(error.message));
});
$("cleanup-delete-all").addEventListener("click", () => {
  deleteAllCleanupItems().catch((error) => cleanupLog(error.message));
});
$("cleanup-filter").addEventListener("input", renderCleanupScan);
$("health-filter").addEventListener("input", () => {
  state.matrixWindow = { start: 0, end: 0 };
  renderVaultHealth();
});
$("health-status").addEventListener("change", () => {
  state.matrixWindow = { start: 0, end: 0 };
  renderVaultHealth();
});
$("matrix-window-start").addEventListener("pointerdown", (event) => startMatrixDrag("start", event));
$("matrix-window-end").addEventListener("pointerdown", (event) => startMatrixDrag("end", event));
$("matrix-window-selection").addEventListener("pointerdown", (event) => startMatrixDrag("range", event));
document.addEventListener("pointermove", updateMatrixDrag);
document.addEventListener("pointerup", stopMatrixDrag);
window.addEventListener("resize", () => {
  if (state.activeTab === "vault-health") {
    renderVaultHealth();
  }
  if (state.activeTab === "original-graph") {
    resizeOriginalGraphChart();
  }
});
$("dry-run").addEventListener("click", () => runTranslation(true));
$("translate-metadata").addEventListener("click", () => runMetadataTranslation(false));
$("translate").addEventListener("click", () => runTranslation(false));

loadConfig()
  .then(loadHealth)
  .then(loadVaultHealth)
  .then(updateGraphControlLabels)
  .catch((error) => {
    log(error.message);
    healthLog(error.message);
  });
