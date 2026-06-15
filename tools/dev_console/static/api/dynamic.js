import { api } from "./client.js";

export const scanDynamicPages = (language) => api(`/api/dynamic/scan?language=${encodeURIComponent(language)}`);
export const checkDynamicPages = (language, path = "") => {
  const params = new URLSearchParams();
  if (language) {
    params.set("language", language);
  }
  if (path) {
    params.set("path", path);
  }
  return api(`/api/dynamic/check?${params.toString()}`);
};
export const previewDynamicPage = (path) => api("/api/dynamic/preview", { method: "POST", body: JSON.stringify({ path }) });
export const refreshDynamicPages = (payload) => api("/api/dynamic/refresh", { method: "POST", body: JSON.stringify(payload) });
