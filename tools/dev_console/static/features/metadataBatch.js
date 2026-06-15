import { createMetadataBatchPlanApi, translateMetadataBatchFile } from "../api/translation.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let context = {
  getLanguageCodes: () => [],
  getLanguageNames: () => ({}),
  getDefaultTargetLang: () => "",
  getModelName: () => "",
  refreshAfterWrite: async () => {},
};
let metadataPlan = null;
let eventScope = createEventScope();

export function mountMetadataBatchFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("metadata-plan"), "click", () => {
    createMetadataPlan().catch((error) => metadataLog(error.message));
  });
  eventScope.listen($("metadata-run"), "click", () => {
    runMetadataBatch().catch((error) => metadataLog(error.message));
  });
  renderMetadataPlan();
}

export function unmountMetadataBatchFeature() {
  eventScope.clear();
}

export function metadataLog(value) {
  const log = $("metadata-log");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function renderMetadataLanguageOptions() {
  const targetSelect = $("metadata-target");
  const sourceSelect = $("metadata-source");
  const reasonSelect = $("metadata-reason");
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
  setRunEnabled(false);
  setMetadataStatus("Planning...");
  try {
    metadataPlan = await createMetadataBatchPlanApi({
      target_lang: targetLang,
      source_lang: $("metadata-source").value,
      reason: $("metadata-reason").value,
      path_filter: $("metadata-path-filter").value.trim(),
      max_files: maxFiles,
    });
    renderMetadataPlan();
    setRunEnabled(metadataPlan.candidates.length > 0);
    setMetadataStatus(`Plan ready: ${metadataPlan.planned_count}/${metadataPlan.total_candidates} candidates selected.`);
  } catch (error) {
    metadataPlan = null;
    metadataLog(error.message);
    setMetadataStatus("Planning failed.");
  } finally {
    setBusy(false);
    setRunEnabled(Boolean(metadataPlan?.candidates.length));
  }
}

async function runMetadataBatch() {
  const plan = metadataPlan;
  if (!plan || !plan.candidates.length) {
    metadataLog("Create a non-empty metadata plan first.");
    return;
  }

  const progress = $("metadata-progress");
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
      setMetadataStatus(batchProgressLabel(
        "Translating metadata",
        index + 1,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      ));
      const result = await translateMetadataBatchFile({
        source_path: item.source_path,
        source_lang: item.source_lang,
        target_lang: item.target_lang,
        model: context.getModelName(),
      });
      results.push(result);
      if (progress) {
        progress.value = index + 1;
      }
      setMetadataStatus(batchProgressLabel(
        "Translated metadata",
        results.length,
        plan.candidates.length,
        item.translation_id,
        startedAt,
        results.length
      ));
      metadataLog(results);
    }
    setMetadataStatus(`Metadata batch complete: ${results.length} translated (time left: 00:00 min).`);
    await context.refreshAfterWrite();
  } catch (error) {
    setMetadataStatus(`Metadata batch stopped after ${results.length}/${plan.candidates.length} (${batchTimeLeftLabel(
      startedAt,
      results.length,
      plan.candidates.length
    )}).`);
    metadataLog({
      error: error.message,
      completed: results.length,
      total: plan.candidates.length,
      results,
    });
  } finally {
    setBusy(false);
    setRunEnabled(Boolean(metadataPlan?.candidates.length));
  }
}

function renderMetadataPlan() {
  if (!$("metadata-summary")) {
    return;
  }
  const plan = metadataPlan;
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
    ${plan.source_counts ? `<span class="pill">By source: <strong>${escapeHtml(formatLanguageCounts(plan.source_counts, context.getLanguageNames()))}</strong></span>` : ""}
    ${plan.target_counts ? `<span class="pill">By language: <strong>${escapeHtml(formatTargetCounts(plan.target_counts, context.getLanguageNames()))}</strong></span>` : ""}
  `;

  $("metadata-list").innerHTML = `
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

function formatMetadataFilters(filters) {
  const names = context.getLanguageNames();
  const parts = [
    `source=${languageLabel(filters.source_lang || "all", filters.source_lang === "all" ? "All source languages" : names[filters.source_lang])}`,
    `reason=${metadataReasonLabel(filters.reason || "all")}`,
  ];
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
  const planButton = $("metadata-plan");
  if (planButton) {
    planButton.disabled = isBusy;
  }
  if (isBusy) {
    setRunEnabled(false);
  }
}

function setMetadataStatus(text) {
  const status = $("metadata-status");
  if (status) {
    status.textContent = text;
  }
}

function setRunEnabled(isEnabled) {
  const button = $("metadata-run");
  if (button) {
    button.disabled = !isEnabled;
  }
}

