import { createBatchPlanApi, translateBatchFile } from "../api/translation.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let context = {
  getLanguageCodes: () => [],
  getLanguageNames: () => ({}),
  getDefaultTargetLang: () => "",
  getModelName: () => "",
  getPrompt: () => "",
  refreshAfterWrite: async () => {},
};
let batchPlan = null;
let eventScope = createEventScope();

export function mountTranslateBatchFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("batch-plan"), "click", () => {
    createBatchPlan().catch((error) => batchLog(error.message));
  });
  eventScope.listen($("batch-run"), "click", () => {
    runBatchTranslation().catch((error) => batchLog(error.message));
  });
  renderBatchPlan();
}

export function unmountTranslateBatchFeature() {
  eventScope.clear();
}

export function batchLog(value) {
  const log = $("batch-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function renderBatchLanguageOptions() {
  const targetSelect = $("batch-target");
  const sourceSelect = $("batch-source");
  const reasonSelect = $("batch-reason");
  if (!targetSelect || !sourceSelect || !reasonSelect) {
    return;
  }
  const currentTarget = targetSelect.value || context.getDefaultTargetLang() || "all";
  const currentSource = sourceSelect.value || "all";
  const currentReason = reasonSelect.value || "all";
  const languages = context.getLanguageCodes();
  const languageNames = context.getLanguageNames();
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
  setRunEnabled(false);
  setBatchStatus("Planning...");
  try {
    batchPlan = await createBatchPlanApi({
      target_lang: targetLang,
      source_lang: $("batch-source").value,
      reason: $("batch-reason").value,
      max_source_chars: $("batch-max-chars").value ? maxSourceChars : null,
      path_filter: $("batch-path-filter").value.trim(),
      max_files: maxFiles,
    });
    renderBatchPlan();
    setRunEnabled(batchPlan.candidates.length > 0);
    setBatchStatus(`Plan ready: ${batchPlan.planned_count}/${batchPlan.total_candidates} candidates selected.`);
  } catch (error) {
    batchPlan = null;
    batchLog(error.message);
    setBatchStatus("Planning failed.");
  } finally {
    setBusy(false);
    setRunEnabled(Boolean(batchPlan?.candidates.length));
  }
}

async function runBatchTranslation() {
  const plan = batchPlan;
  if (!plan || !plan.candidates.length) {
    batchLog("Create a non-empty plan first.");
    return;
  }

  const progress = $("batch-progress");
  if (progress) {
    progress.max = plan.candidates.length;
    progress.value = 0;
  }
  setBusy(true);
  const results = [];
  const startedAt = performance.now();

  try {
    for (let index = 0; index < plan.candidates.length; index += 1) {
      const item = plan.candidates[index];
      setBatchStatus(batchProgressLabel(
        "Translating",
        index + 1,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      ));
      const result = await translateBatchFile({
        source_path: item.source_path,
        source_lang: item.source_lang,
        target_lang: item.target_lang,
        model: context.getModelName(),
        prompt: context.getPrompt(),
      });
      results.push(result);
      if (progress) {
        progress.value = index + 1;
      }
      setBatchStatus(batchProgressLabel(
        "Translated",
        results.length,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      ));
      batchLog(results);
    }
    setBatchStatus(`Batch complete: ${results.length} translated (time left: 00:00 min).`);
    await context.refreshAfterWrite();
  } catch (error) {
    setBatchStatus(`Batch stopped after ${results.length}/${plan.candidates.length} (${batchTimeLeftLabel(
      startedAt,
      results.length,
      plan.candidates.length
    )}).`);
    batchLog({
      error: error.message,
      completed: results.length,
      total: plan.candidates.length,
      results,
    });
  } finally {
    setBusy(false);
    setRunEnabled(Boolean(batchPlan?.candidates.length));
  }
}

function renderBatchPlan() {
  if (!$("batch-summary")) {
    return;
  }
  const plan = batchPlan;
  if (!plan) {
    $("batch-summary").innerHTML = "";
    $("batch-list").innerHTML = "";
    return;
  }

  $("batch-summary").innerHTML = `
    <span class="pill">Target: <strong>${escapeHtml(languageLabel(plan.target_lang, plan.target_language))}</strong></span>
    <span class="pill">Planned: <strong>${plan.planned_count}</strong></span>
    <span class="pill">Candidates: <strong>${plan.total_candidates}</strong></span>
    <span class="pill">Source chars: <strong>${plan.total_source_chars}</strong></span>
    <span class="pill">Limit: <strong>${plan.max_files}</strong></span>
    <span class="pill">Source policy: <strong>${escapeHtml(formatSourcePolicy(plan.source_policy))}</strong></span>
    <span class="pill">Filters: <strong>${escapeHtml(formatBatchFilters(plan.filters || {}))}</strong></span>
    ${plan.source_counts ? `<span class="pill">By source: <strong>${escapeHtml(formatLanguageCounts(plan.source_counts, context.getLanguageNames()))}</strong></span>` : ""}
    ${plan.target_counts ? `<span class="pill">By language: <strong>${escapeHtml(formatTargetCounts(plan.target_counts, context.getLanguageNames()))}</strong></span>` : ""}
  `;

  $("batch-list").innerHTML = `
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

function formatBatchFilters(filters) {
  const names = context.getLanguageNames();
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
  const planButton = $("batch-plan");
  if (planButton) {
    planButton.disabled = isBusy;
  }
  if (isBusy) {
    setRunEnabled(false);
  }
}

function setBatchStatus(text) {
  const status = $("batch-status");
  if (status) {
    status.textContent = text;
  }
}

function setRunEnabled(isEnabled) {
  const button = $("batch-run");
  if (button) {
    button.disabled = !isEnabled;
  }
}

