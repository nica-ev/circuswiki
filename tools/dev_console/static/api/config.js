import { api } from "./client.js";

export const getConfig = () => api("/api/config");
