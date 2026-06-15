import { api } from "./client.js";

export const getPages = (sourceLang) => api(`/api/pages?source_lang=${encodeURIComponent(sourceLang)}`);
export const getHealth = (sourceLang, targetLang) =>
  api(`/api/health?source_lang=${encodeURIComponent(sourceLang)}&target_lang=${encodeURIComponent(targetLang)}`);
export const getPage = (path, sourceLang, targetLang) =>
  api(`/api/page?path=${encodeURIComponent(path)}&source_lang=${encodeURIComponent(sourceLang)}&target_lang=${encodeURIComponent(targetLang)}`);
export const translatePage = (payload) => api("/api/translate", { method: "POST", body: JSON.stringify(payload) });
export const translateMetadata = (payload) => api("/api/translate-metadata", { method: "POST", body: JSON.stringify(payload) });
export const repairMetadata = (payload) => api("/api/repair-metadata", { method: "POST", body: JSON.stringify(payload) });
export const createBatchPlanApi = (payload) => api("/api/batch-plan", { method: "POST", body: JSON.stringify(payload) });
export const translateBatchFile = (payload) => api("/api/batch-translate-file", { method: "POST", body: JSON.stringify(payload) });
export const createMetadataBatchPlanApi = (payload) => api("/api/metadata-batch-plan", { method: "POST", body: JSON.stringify(payload) });
export const translateMetadataBatchFile = (payload) => api("/api/metadata-batch-translate-file", { method: "POST", body: JSON.stringify(payload) });
export const getVaultHealth = () => api("/api/vault-health");
