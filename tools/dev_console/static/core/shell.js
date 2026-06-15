import { escapeHtml } from "./html.js";

export function activeGroupId(features, activeTab) {
  return features.find((feature) => feature.id === activeTab)?.group || features[0]?.group || "";
}

export function renderAppNavigation(primaryRoot, secondaryRoot, groups, features, activeTab) {
  const groupId = activeGroupId(features, activeTab);
  primaryRoot.innerHTML = groups.map((group) => `
    <button class="primary-tab${group.id === groupId ? " active" : ""}" type="button" data-group="${escapeHtml(group.id)}">
      ${escapeHtml(group.label)}
    </button>
  `).join("");

  const items = features.filter((feature) => feature.group === groupId);
  secondaryRoot.innerHTML = items.map((feature) => `
    <button class="tab${feature.id === activeTab ? " active" : ""}" type="button" data-tab="${escapeHtml(feature.id)}">
      ${escapeHtml(feature.label)}
    </button>
  `).join("");
}

export function activateTab(tabName) {
  document.querySelectorAll(".tab").forEach((button) => {
    button.classList.toggle("active", button.dataset.tab === tabName);
  });
}

export function createPanelStore(root) {
  const panels = new Map();
  root.querySelectorAll(".tab-panel").forEach((panel) => {
    const id = panel.id.replace(/^tab-/, "");
    panel.classList.remove("active");
    panels.set(id, panel);
    panel.remove();
  });
  return {
    mount(id) {
      const panel = panels.get(id);
      if (!panel) {
        throw new Error(`Unknown panel: ${id}`);
      }
      root.replaceChildren(panel);
      panel.classList.add("active");
      return panel;
    },
    unmount(id) {
      const panel = panels.get(id);
      if (panel?.parentElement === root) {
        panel.classList.remove("active");
        panel.remove();
      }
    },
    has(id) {
      return panels.has(id);
    },
  };
}
