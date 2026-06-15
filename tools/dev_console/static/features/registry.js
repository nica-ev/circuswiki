export const FEATURE_GROUPS = [
  { id: "translate", label: "Translate" },
  { id: "dynamic-content", label: "Dynamic" },
  { id: "links", label: "Links" },
  { id: "structure", label: "Structure" },
  { id: "maintenance", label: "Maintenance" },
];

export const FEATURES = [
  { id: "file-test", label: "Single File", group: "translate" },
  { id: "batch-translate", label: "Batch Body", group: "translate" },
  { id: "batch-metadata", label: "Batch Metadata", group: "translate" },
  { id: "vault-health", label: "Health", group: "translate" },
  { id: "dynamic", label: "Pages", group: "dynamic-content" },
  { id: "base-labels", label: "Base Labels", group: "dynamic-content" },
  { id: "link-repair", label: "Translation Repair", group: "links" },
  { id: "navigation", label: "Navigation", group: "structure" },
  { id: "original-graph", label: "Original Graph", group: "structure" },
  { id: "cleanup", label: "Cleanup", group: "maintenance" },
  { id: "obsidian", label: "Obsidian", group: "maintenance" },
];
