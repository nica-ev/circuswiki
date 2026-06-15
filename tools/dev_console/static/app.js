import { openInObsidianApi } from "./api/obsidian.js";
import { getConfig } from "./api/config.js";
import { $ } from "./core/dom.js";
import { createEventScope } from "./core/events.js";
import { activateTab, createPanelStore, renderAppNavigation } from "./core/shell.js";
import { state } from "./core/state.js";
import {
  activateFeature,
  configureFeatures,
  loadInitialFeatureData,
  logForFeature,
  mountFeature,
  refreshTranslationState,
  refreshVaultHealth,
  resizeActiveFeature,
  unmountFeature,
  unmountFeatures,
} from "./features/lifecycle.js";
import { FEATURE_GROUPS, FEATURES } from "./features/registry.js";

const appEvents = createEventScope();
const panels = createPanelStore($("app-main"));

async function loadConfig() {
  const config = await getConfig();
  state.config = config;
  const modelInput = $("model");
  const promptInput = $("prompt");
  if (modelInput) {
    modelInput.value = config.default_model;
  }
  if (promptInput) {
    promptInput.value = config.default_prompt;
  }
  configureFeatures(config);
}

async function openInObsidian(path) {
  if (!path) {
    activeLog("No path selected.");
    return;
  }
  activeLog(`Opening in Obsidian: ${path}`);
  try {
    const result = await openInObsidianApi(path);
    activeLog(result);
  } catch (error) {
    activeLog(error.message);
  }
}

function activeLog(value) {
  logForFeature(state.activeTab, value);
}

function switchTab(tabName) {
  if (tabName === state.activeTab) {
    return;
  }
  unmountFeature(state.activeTab);
  panels.unmount(state.activeTab);
  state.activeTab = tabName;
  panels.mount(tabName);
  mountFeature(tabName, featureContext);
  activateTab(tabName);
  updateAppMode();
  renderNavigationShell();
  activateFeature(tabName);
}

function renderNavigationShell() {
  renderAppNavigation($("app-primary-nav"), $("app-secondary-nav"), FEATURE_GROUPS, FEATURES, state.activeTab);
}

function updateAppMode() {
  document.body.classList.toggle("graph-mode", state.activeTab === "original-graph");
}

renderNavigationShell();
panels.mount(state.activeTab);
updateAppMode();

appEvents.listen($("app-primary-nav"), "click", (event) => {
  const button = event.target.closest("[data-group]");
  if (!button) {
    return;
  }
  const firstFeature = FEATURES.find((feature) => feature.group === button.dataset.group);
  if (firstFeature) {
    switchTab(firstFeature.id);
  }
});

appEvents.listen($("app-secondary-nav"), "click", (event) => {
  const button = event.target.closest("[data-tab]");
  if (button?.dataset.tab) {
    switchTab(button.dataset.tab);
  }
});

appEvents.listen(document, "click", (event) => {
  const button = event.target.closest(".obsidian-open");
  if (!button) {
    return;
  }
  openInObsidian(button.dataset.obsidianPath || "").catch((error) => activeLog(error.message));
});

const featureContext = {
  refreshVaultHealth,
  getDefaultTargetLang: () => state.config?.default_target_lang || "",
  getDefaultSourceLang: () => state.config?.default_source_lang || "",
  getConfiguredLanguageNames: () => Object.fromEntries((state.config?.languages || []).map((language) => [language.code, language.name])),
  getModelName: () => $("model")?.value.trim() || "",
  getPrompt: () => $("prompt")?.value.trim() || "",
  refreshTranslationState: async () => refreshTranslationState(featureContext),
};
mountFeature(state.activeTab, featureContext);
appEvents.listen(window, "resize", () => {
  resizeActiveFeature(state.activeTab);
});
appEvents.listen(window, "beforeunload", () => {
  unmountFeatures();
  appEvents.clear();
});
loadConfig()
  .then(() => loadInitialFeatureData(featureContext))
  .catch((error) => {
    logForFeature("file-test", error.message);
    logForFeature("vault-health", error.message);
  });







