import { api } from "./client.js";

export const scanCleanupOrphans = () => api("/api/cleanup/orphans");
export const deleteCleanupOrphans = (paths) => api("/api/cleanup/delete-orphans", { method: "POST", body: JSON.stringify({ paths }) });
export const deleteAllCleanupOrphans = () => api("/api/cleanup/delete-all-orphans", { method: "POST", body: JSON.stringify({}) });
