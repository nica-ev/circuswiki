import {
  baseLabelLog,
  hasBaseLabelScan,
  loadBaseLabelScan,
  mountBaseLabelsFeature,
  renderBaseLabelLanguageOptions,
  unmountBaseLabelsFeature,
} from "./baseLabels.js";
import { cleanupLog, hasCleanupScan, loadCleanupScan, mountCleanupFeature, unmountCleanupFeature } from "./cleanup.js";
import {
  dynamicLog,
  hasDynamicScan,
  loadDynamicScan,
  mountDynamicPagesFeature,
  renderDynamicLanguageOptions,
  unmountDynamicPagesFeature,
} from "./dynamicPages.js";
import {
  getLanguageCodes,
  getLanguageNames,
  hasVaultHealth,
  healthLog,
  loadVaultHealth,
  mountHealthMatrixFeature,
  refreshHealthLayout,
  unmountHealthMatrixFeature,
} from "./healthMatrix.js";
import {
  hasLinkRepairScan,
  linkRepairLog,
  loadLinkRepairScan,
  mountLinkRepairFeature,
  renderLinkRepairLanguageOptions,
  unmountLinkRepairFeature,
} from "./linkRepair.js";
import { metadataLog, mountMetadataBatchFeature, renderMetadataLanguageOptions, unmountMetadataBatchFeature } from "./metadataBatch.js";
import { hasObsidianStatus, loadObsidianStatus, mountObsidianFeature, obsidianLog, unmountObsidianFeature } from "./obsidian.js";
import {
  graphLog,
  hasOriginalGraph,
  loadOriginalGraph,
  mountOriginalGraphFeature,
  resizeOriginalGraphChart,
  unmountOriginalGraphFeature,
} from "./originalGraph.js";
import { hasNavigationScan, loadNavigationScan, mountNavigationFeature, navLog, unmountNavigationFeature } from "./navigation.js";
import {
  hasSourceLinkStyleScan,
  loadSourceLinkStyleScan,
  mountSourceLinkStyleFeature,
  renderSourceLinkStyleLanguageOptions,
  unmountSourceLinkStyleFeature,
} from "./sourceLinkStyle.js";
import { batchLog, mountTranslateBatchFeature, renderBatchLanguageOptions, unmountTranslateBatchFeature } from "./translateBatch.js";
import {
  loadSingleFileHealth,
  mountTranslateSingleFeature,
  renderFileLanguageOptions,
  singleFileLog,
  unmountTranslateSingleFeature,
} from "./translateSingle.js";

const featureLoggers = {
  "file-test": singleFileLog,
  "vault-health": healthLog,
  "batch-translate": batchLog,
  "batch-metadata": metadataLog,
  "original-graph": graphLog,
  navigation: navLog,
  dynamic: dynamicLog,
  "base-labels": baseLabelLog,
  cleanup: cleanupLog,
  "link-repair": linkRepairLog,
  "source-link-style": linkRepairLog,
  obsidian: obsidianLog,
};

export function logForFeature(featureId, value) {
  try {
    (featureLoggers[featureId] || singleFileLog)(value);
  } catch (error) {
    console.warn("Feature log target is not mounted.", { featureId, value, error });
  }
}

let appConfig = null;
let currentFeatureId = null;
let lifecycleContext = null;

export function configureFeatures(config) {
  appConfig = config;
  configureMountedFeature(currentFeatureId);
}

export function mountFeature(featureId, context) {
  lifecycleContext = context;
  if (currentFeatureId && currentFeatureId !== featureId) {
    unmountFeature(currentFeatureId);
  }
  currentFeatureId = featureId;
  const mount = featureMounts[featureId];
  if (!mount) {
    throw new Error(`Unknown feature: ${featureId}`);
  }
  mount(context);
  configureMountedFeature(featureId);
}

export function unmountFeature(featureId) {
  const unmount = featureUnmounts[featureId];
  unmount?.();
  if (currentFeatureId === featureId) {
    currentFeatureId = null;
  }
}

export async function refreshVaultHealth() {
  return loadVaultHealth();
}

export async function loadInitialFeatureData(context) {
  await loadSingleFileHealth();
  await context.refreshVaultHealth();
}

export async function refreshTranslationState(context) {
  await loadSingleFileHealth();
  await context.refreshVaultHealth();
}

export function activateFeature(featureId) {
  if (featureId === "vault-health" && !hasVaultHealth()) {
    loadVaultHealth().catch((error) => healthLog(error.message));
    return;
  }
  if (featureId === "navigation" && !hasNavigationScan()) {
    loadNavigationScan().catch((error) => navLog(error.message));
    return;
  }
  if (featureId === "original-graph") {
    if (!hasOriginalGraph()) {
      loadOriginalGraph().catch((error) => graphLog(error.message));
    } else {
      setTimeout(resizeOriginalGraphChart, 0);
    }
    return;
  }
  if (featureId === "dynamic" && !hasDynamicScan()) {
    loadDynamicScan().catch((error) => dynamicLog(error.message));
    return;
  }
  if (featureId === "base-labels" && !hasBaseLabelScan()) {
    loadBaseLabelScan().catch((error) => baseLabelLog(error.message));
    return;
  }
  if (featureId === "link-repair" && !hasLinkRepairScan()) {
    loadLinkRepairScan().catch((error) => linkRepairLog(error.message));
    return;
  }
  if (featureId === "source-link-style" && !hasSourceLinkStyleScan()) {
    loadSourceLinkStyleScan().catch((error) => linkRepairLog(error.message));
    return;
  }
  if (featureId === "cleanup" && !hasCleanupScan()) {
    loadCleanupScan().catch((error) => cleanupLog(error.message));
    return;
  }
  if (featureId === "obsidian" && !hasObsidianStatus()) {
    loadObsidianStatus().catch((error) => obsidianLog(error.message));
  }
}

export function resizeActiveFeature(featureId) {
  if (featureId === "vault-health") {
    refreshHealthLayout();
  }
  if (featureId === "original-graph") {
    resizeOriginalGraphChart();
  }
}

export function unmountFeatures() {
  if (currentFeatureId) {
    unmountFeature(currentFeatureId);
  }
  unmountHealthMatrixFeature();
  unmountOriginalGraphFeature();
}

function configureMountedFeature(featureId) {
  if (!featureId || !appConfig) {
    return;
  }
  if (featureId === "file-test") {
    renderFileLanguageOptions(appConfig);
  }
  if (featureId === "batch-translate") {
    renderBatchLanguageOptions();
  }
  if (featureId === "batch-metadata") {
    renderMetadataLanguageOptions();
  }
  if (featureId === "dynamic") {
    renderDynamicLanguageOptions(appConfig);
  }
  if (featureId === "base-labels") {
    renderBaseLabelLanguageOptions(appConfig);
  }
  if (featureId === "link-repair") {
    renderLinkRepairLanguageOptions(appConfig);
    renderSourceLinkStyleLanguageOptions(appConfig);
  }
}

const featureMounts = {
  "file-test": (context) => mountTranslateSingleFeature({ refreshVaultHealth: context.refreshVaultHealth }),
  "vault-health": () => mountHealthMatrixFeature({
    afterLoad: () => {
      renderBatchLanguageOptions();
      renderMetadataLanguageOptions();
    },
  }),
  "batch-translate": (context) => mountTranslateBatchFeature({
    getLanguageCodes,
    getLanguageNames,
    getDefaultTargetLang: context.getDefaultTargetLang,
    getModelName: context.getModelName,
    getPrompt: context.getPrompt,
    refreshAfterWrite: context.refreshTranslationState,
  }),
  "batch-metadata": (context) => mountMetadataBatchFeature({
    getLanguageCodes,
    getLanguageNames,
    getDefaultTargetLang: context.getDefaultTargetLang,
    getModelName: context.getModelName,
    refreshAfterWrite: context.refreshTranslationState,
  }),
  "original-graph": (context) => mountOriginalGraphFeature({
    getLanguageNames: context.getConfiguredLanguageNames,
  }),
  navigation: (context) => mountNavigationFeature({
    getDefaultSourceLang: context.getDefaultSourceLang,
    getModelName: context.getModelName,
  }),
  dynamic: () => mountDynamicPagesFeature(),
  "base-labels": (context) => mountBaseLabelsFeature({
    getModelName: context.getModelName,
  }),
  "link-repair": () => {
    mountLinkRepairFeature();
    mountSourceLinkStyleFeature();
  },
  cleanup: (context) => mountCleanupFeature({ loadVaultHealth: context.refreshVaultHealth }),
  obsidian: () => mountObsidianFeature(),
};

const featureUnmounts = {
  "file-test": unmountTranslateSingleFeature,
  "vault-health": unmountHealthMatrixFeature,
  "batch-translate": unmountTranslateBatchFeature,
  "batch-metadata": unmountMetadataBatchFeature,
  "original-graph": unmountOriginalGraphFeature,
  navigation: unmountNavigationFeature,
  dynamic: unmountDynamicPagesFeature,
  "base-labels": unmountBaseLabelsFeature,
  "link-repair": () => {
    unmountLinkRepairFeature();
    unmountSourceLinkStyleFeature();
  },
  cleanup: unmountCleanupFeature,
  obsidian: unmountObsidianFeature,
};
