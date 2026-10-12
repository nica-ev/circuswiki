import {
  createBatchPlanApi,
  createTranslationJob,
  getCurrentTranslationJob,
  getTranslationJob,
  runTranslationJobAction,
} from "../api/translation.js";
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
let currentJob = null;
let busy = false;
let pollTimer = null;
let mounted = false;
const refreshedTerminalJobs = new Set();
let eventScope = createEventScope();

export function mountTranslateBatchFeature(nextContext) {
  mounted = true;
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("batch-plan"), "click", () => {
    createBatchPlan().catch((error) => batchLog(error.message));
  });
  eventScope.listen($("batch-run"), "click", () => {
    startTranslationJob().catch((error) => batchLog(error.message));
  });
  eventScope.listen($("batch-pause"), "click", () => controlTranslationJob("pause").catch((error) => batchLog(error.message)));
  eventScope.listen($("batch-resume"), "click", () => controlTranslationJob("resume").catch((error) => batchLog(error.message)));
  eventScope.listen($("batch-cancel"), "click", () => {
    if (window.confirm("Cancel all queued translations? Currently running files will finish.")) {
      controlTranslationJob("cancel").catch((error) => batchLog(error.message));
    }
  });
  eventScope.listen($("batch-retry"), "click", () => controlTranslationJob("retry-failed").catch((error) => batchLog(error.message)));
  renderBatchPlan();
  renderCurrentJob();
  reconnectCurrentJob().catch((error) => batchLog(error.message));
}

export function unmountTranslateBatchFeature() {
  mounted = false;
  stopPolling();
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
    updateButtons();
    setBatchStatus(`Plan ready: ${batchPlan.planned_count}/${batchPlan.total_candidates} candidates selected.`);
  } catch (error) {
    batchPlan = null;
    batchLog(error.message);
    setBatchStatus("Planning failed.");
  } finally {
    setBusy(false);
  }
}

async function startTranslationJob() {
  const plan = batchPlan;
  if (!plan || !plan.candidates.length) {
    batchLog("Create a non-empty plan first.");
    return;
  }
  if (isActiveJob(currentJob)) {
    batchLog(`Translation job ${currentJob.id} is already active.`);
    return;
  }
  const concurrency = Number($("batch-concurrency").value);
  if (!Number.isInteger(concurrency) || concurrency < 1 || concurrency > 8) {
    batchLog("Concurrency must be between 1 and 8.");
    return;
  }

  setBusy(true);
  try {
    currentJob = await createTranslationJob({
      plan,
      model: context.getModelName(),
      prompt: context.getPrompt(),
      concurrency,
    });
    renderCurrentJob();
    schedulePoll();
  } catch (error) {
    batchLog(error.message);
    setBatchStatus("Could not start background translation job.");
  } finally {
    setBusy(false);
  }
}

async function reconnectCurrentJob() {
  const response = await getCurrentTranslationJob();
  if (!mounted) {
    return;
  }
  currentJob = response.job || null;
  renderCurrentJob();
  if (isActiveJob(currentJob)) {
    schedulePoll();
  }
}

async function pollCurrentJob() {
  stopPolling();
  if (!mounted || !currentJob?.id) {
    return;
  }
  try {
    currentJob = await getTranslationJob(currentJob.id);
    renderCurrentJob();
    if (isActiveJob(currentJob)) {
      schedulePoll();
    } else {
      await refreshAfterTerminalJob(currentJob);
    }
  } catch (error) {
    batchLog(error.message);
    schedulePoll(3000);
  }
}

async function controlTranslationJob(action) {
  if (!currentJob?.id) {
    batchLog("No translation job is selected.");
    return;
  }
  setBusy(true);
  try {
    currentJob = await runTranslationJobAction(currentJob.id, action);
    renderCurrentJob();
    if (isActiveJob(currentJob)) {
      schedulePoll();
    } else {
      stopPolling();
      await refreshAfterTerminalJob(currentJob);
    }
  } finally {
    setBusy(false);
  }
}

function schedulePoll(delay = 1000) {
  if (!mounted) {
    return;
  }
  stopPolling();
  pollTimer = window.setTimeout(() => pollCurrentJob(), delay);
}

function stopPolling() {
  if (pollTimer !== null) {
    window.clearTimeout(pollTimer);
    pollTimer = null;
  }
}

async function refreshAfterTerminalJob(job) {
  if (!job?.id || refreshedTerminalJobs.has(job.id)) {
    return;
  }
  refreshedTerminalJobs.add(job.id);
  await context.refreshAfterWrite();
}

function isActiveJob(job) {
  return Boolean(job && ["queued", "running"].includes(job.status));
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

function renderCurrentJob() {
  const summary = $("batch-job-summary");
  const progress = $("batch-progress");
  if (!summary || !progress) {
    return;
  }
  if (!currentJob) {
    summary.innerHTML = "";
    progress.max = 0;
    progress.value = 0;
    setBatchStatus("No background translation job.");
    updateButtons();
    return;
  }

  const counts = currentJob.counts || {};
  const rateLimit = currentJob.rate_limit || {};
  const usage = currentJob.usage || {};
  const status = currentJob.paused ? "paused" : currentJob.cancel_requested ? "cancelling" : currentJob.status;
  progress.max = currentJob.total_items || 0;
  progress.value = currentJob.terminal_items || 0;
  summary.innerHTML = `
    <span class="pill">Job: <strong>${escapeHtml(currentJob.id)}</strong></span>
    <span class="pill">Status: <strong>${escapeHtml(status)}</strong></span>
    <span class="pill">Workers: <strong>${currentJob.concurrency}</strong></span>
    <span class="pill">Running: <strong>${counts.running || 0}</strong></span>
    <span class="pill">Queued: <strong>${counts.queued || 0}</strong></span>
    <span class="pill">Completed: <strong>${counts.completed || 0}</strong></span>
    <span class="pill">Failed: <strong>${counts.failed || 0}</strong></span>
    <span class="pill">Stale: <strong>${counts.stale || 0}</strong></span>
    <span class="pill">Rate: <strong>${formatRate(currentJob.throughput_per_minute)}</strong></span>
    <span class="pill">ETA: <strong>${formatDuration(currentJob.eta_seconds)}</strong></span>
    <span class="pill">API calls: <strong>${usage.api_calls || 0}</strong></span>
    <span class="pill">Tokens: <strong>${usage.total_tokens || 0}</strong></span>
    <span class="pill">Cost: <strong>${formatCost(usage.cost)}</strong></span>
    ${rateLimit.active ? `<span class="pill">Cooldown: <strong>${formatDuration(rateLimit.remaining_seconds)}</strong></span>` : ""}
  `;
  setBatchStatus(jobStatusLabel(currentJob));
  batchLog({
    id: currentJob.id,
    status,
    counts,
    recent_failures: currentJob.recent_failures || [],
    rate_limit: rateLimit,
  });
  updateButtons();
}

function jobStatusLabel(job) {
  const completed = job.terminal_items || 0;
  const total = job.total_items || 0;
  if (job.cancel_requested && isActiveJob(job)) {
    return `Cancellation requested: ${completed}/${total} finished; running files may complete.`;
  }
  if (job.paused) {
    return `Paused: ${completed}/${total} finished (${formatDuration(job.eta_seconds)} remaining estimate).`;
  }
  if (isActiveJob(job)) {
    return `Background translation: ${completed}/${total} finished (${formatDuration(job.eta_seconds)} remaining estimate).`;
  }
  return `Job ${job.status}: ${completed}/${total} finished.`;
}

function formatDuration(seconds) {
  if (seconds == null || !Number.isFinite(Number(seconds))) {
    return "--";
  }
  const totalSeconds = Math.max(0, Math.round(Number(seconds)));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const remainingSeconds = totalSeconds % 60;
  if (hours) {
    return `${hours}h ${String(minutes).padStart(2, "0")}m`;
  }
  return `${minutes}m ${String(remainingSeconds).padStart(2, "0")}s`;
}

function formatRate(value) {
  const numeric = Number(value || 0);
  return numeric > 0 ? `${numeric.toFixed(2)}/min` : "--";
}

function formatCost(value) {
  const numeric = Number(value || 0);
  return numeric > 0 ? `$${numeric.toFixed(4)}` : "--";
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
  busy = isBusy;
  updateButtons();
}

function updateButtons() {
  const planButton = $("batch-plan");
  const runButton = $("batch-run");
  const pauseButton = $("batch-pause");
  const resumeButton = $("batch-resume");
  const cancelButton = $("batch-cancel");
  const retryButton = $("batch-retry");
  const active = isActiveJob(currentJob);
  if (planButton) {
    planButton.disabled = busy || active;
  }
  if (runButton) {
    runButton.disabled = busy || active || !batchPlan?.candidates.length;
  }
  if (pauseButton) {
    pauseButton.disabled = busy || !active || currentJob.paused || currentJob.cancel_requested;
  }
  if (resumeButton) {
    resumeButton.disabled = busy || !active || !currentJob.paused || currentJob.cancel_requested;
  }
  if (cancelButton) {
    cancelButton.disabled = busy || !active || currentJob.cancel_requested;
  }
  if (retryButton) {
    retryButton.disabled = busy || active || !(currentJob?.counts?.failed > 0);
  }
}

function setBatchStatus(text) {
  const status = $("batch-status");
  if (status) {
    status.textContent = text;
  }
}
