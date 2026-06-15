import { api } from "./client.js";

export const scanNavigation = () => api("/api/navigation/scan");
export const initNavigation = (payload) => api("/api/navigation/init", { method: "POST", body: JSON.stringify(payload) });
export const translateNavigationLabelsApi = (payload) => api("/api/navigation/translate-labels", { method: "POST", body: JSON.stringify(payload) });
export const translateAllNavigationLabelsApi = (payload) => api("/api/navigation/translate-all-labels", { method: "POST", body: JSON.stringify(payload) });
export const previewNavigation = (payload) => api("/api/navigation/preview", { method: "POST", body: JSON.stringify(payload) });
export const applyNavigation = (payload) => api("/api/navigation/apply", { method: "POST", body: JSON.stringify(payload) });
