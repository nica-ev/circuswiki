import { api } from "./client.js";

export const scanLinkRepair = (language) => api(`/api/link-repair/scan?language=${encodeURIComponent(language)}`);
export const previewLinkRepair = (path) => api(`/api/link-repair/preview?path=${encodeURIComponent(path)}`);
export const repairLinkItems = (paths) => api("/api/link-repair/repair", { method: "POST", body: JSON.stringify({ paths }) });
export const repairAllSafeLinkItemsApi = (language) => api("/api/link-repair/repair-all", { method: "POST", body: JSON.stringify({ language }) });
export const scanSourceLinkStyle = (language) => api(`/api/source-link-style/scan?language=${encodeURIComponent(language)}`);
export const previewSourceLinkStyle = (path) => api(`/api/source-link-style/preview?path=${encodeURIComponent(path)}`);
export const repairSourceLinkStyles = (paths) => api("/api/source-link-style/repair", { method: "POST", body: JSON.stringify({ paths }) });
export const repairAllSafeSourceLinkStylesApi = (language) => api("/api/source-link-style/repair-all", { method: "POST", body: JSON.stringify({ language }) });
