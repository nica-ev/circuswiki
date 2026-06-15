import { api } from "./client.js";

export const scanBaseLabels = () => api("/api/base-labels/scan");
export const planBaseLabelsApi = (params) => api(`/api/base-labels/plan?${params.toString()}`);
export const translateBaseLabelsApi = (payload) => api("/api/base-labels/translate", { method: "POST", body: JSON.stringify(payload) });
export const materializeBaseLabelsApi = (payload) => api("/api/base-labels/materialize", { method: "POST", body: JSON.stringify(payload) });
