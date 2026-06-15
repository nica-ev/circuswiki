import { api } from "./client.js";

export const getObsidianStatus = () => api("/api/obsidian/status");
export const openInObsidianApi = (path) => api("/api/obsidian/open", { method: "POST", body: JSON.stringify({ path }) });
