import { api } from "./client.js";

export const getOriginalGraph = (excludeSitemap) => api(`/api/original-graph?exclude_sitemap=${excludeSitemap ? "true" : "false"}`);
