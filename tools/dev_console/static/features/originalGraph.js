import { getOriginalGraph } from "../api/graph.js";
import { setControlsBusy } from "../core/busy.js";
import { $ } from "../core/dom.js";
import { createEventScope } from "../core/events.js";
import { escapeHtml, jsonText } from "../core/html.js";

let context = {
  getLanguageNames: () => ({}),
};
const busyControls = ["graph-refresh", "graph-fit", "graph-zoom-in", "graph-zoom-out"];
let graphResult = null;
let chart = null;
let resizeObserver = null;
let drag = null;
let eventScope = createEventScope();
let chartEventScope = createEventScope();
const options = {
  showLabels: true,
  excludeSitemap: true,
  repulsion: 260,
  gravity: 0.06,
  edgeLength: 190,
  zoom: 1,
};

export function mountOriginalGraphFeature(nextContext) {
  context = { ...context, ...nextContext };
  eventScope.clear();
  eventScope = createEventScope();
  eventScope.listen($("graph-refresh"), "click", () => {
    loadOriginalGraph().catch((error) => graphLog(error.message));
  });
  eventScope.listen($("graph-fit"), "click", fitOriginalGraph);
  eventScope.listen($("graph-zoom-in"), "click", () => zoomOriginalGraph(1.25));
  eventScope.listen($("graph-zoom-out"), "click", () => zoomOriginalGraph(0.8));
  eventScope.listen($("graph-labels"), "change", updateOriginalGraphForces);
  eventScope.listen($("graph-exclude-sitemap"), "change", () => {
    loadOriginalGraph().catch((error) => graphLog(error.message));
  });
  eventScope.listen($("graph-repulsion"), "input", updateOriginalGraphForces);
  eventScope.listen($("graph-gravity"), "input", updateOriginalGraphForces);
  eventScope.listen($("graph-edge-length"), "input", updateOriginalGraphForces);
  updateGraphControlLabels();
  renderOriginalGraphSummary();
  renderOriginalGraph();
}

export function unmountOriginalGraphFeature() {
  eventScope.clear();
  chartEventScope.clear();
  resizeObserver?.disconnect();
  resizeObserver = null;
  chart?.dispose();
  chart = null;
  drag = null;
}

export function graphLog(value) {
  const log = $("graph-details");
  if (log) {
    log.textContent = jsonText(value);
  }
}

export function hasOriginalGraph() {
  return Boolean(graphResult);
}

export async function loadOriginalGraph() {
  setBusy(true);
  graphLog("Loading original graph...");
  try {
    readGraphControls();
    graphResult = await getOriginalGraph(options.excludeSitemap);
    renderOriginalGraphSummary();
    renderOriginalGraph();
    graphDiagnosticsLog(graphResult.diagnostics?.slice(0, 80) || []);
  } catch (error) {
    graphLog(error.message);
  } finally {
    setBusy(false);
  }
}

export function resizeOriginalGraphChart() {
  if (!chart) {
    return;
  }
  const element = $("original-graph-chart");
  if (!element) {
    return;
  }
  const rect = element.getBoundingClientRect();
  chart.resize({
    width: Math.max(1, Math.floor(rect.width)),
    height: Math.max(1, Math.floor(rect.height)),
  });
}

function graphDiagnosticsLog(value) {
  const log = $("graph-diagnostics");
  if (log) {
    log.textContent = jsonText(value);
  }
}

function readGraphControls() {
  options.showLabels = $("graph-labels").checked;
  options.excludeSitemap = $("graph-exclude-sitemap").checked;
  options.repulsion = Number($("graph-repulsion").value);
  options.gravity = Number($("graph-gravity").value);
  options.edgeLength = Number($("graph-edge-length").value);
  updateGraphControlLabels();
}

function updateGraphControlLabels() {
  if (!$("graph-repulsion-value")) {
    return;
  }
  $("graph-repulsion-value").textContent = String(options.repulsion);
  $("graph-gravity-value").textContent = options.gravity.toFixed(2);
  $("graph-edge-length-value").textContent = String(options.edgeLength);
}

function renderOriginalGraphSummary() {
  if (!$("graph-summary")) {
    return;
  }
  const graph = graphResult;
  if (!graph) {
    $("graph-summary").innerHTML = "";
    return;
  }
  const counts = formatLanguageCounts(graph.summary?.language_counts || {}, context.getLanguageNames());
  $("graph-summary").innerHTML = `
    <span class="pill">Originals: <strong>${graph.summary?.node_count || 0}</strong></span>
    <span class="pill">Edges: <strong>${graph.summary?.edge_count || 0}</strong></span>
    <span class="pill ${graph.summary?.diagnostic_count ? "yellow" : "green"}">Diagnostics: <strong>${graph.summary?.diagnostic_count || 0}</strong></span>
    <span class="pill">Excluded: <strong>${escapeHtml((graph.summary?.excluded_relative_paths || []).join(", ") || "none")}</strong></span>
    <span class="pill">Languages: <strong>${escapeHtml(counts || "none")}</strong></span>
  `;
}

function renderOriginalGraph() {
  if (!$("original-graph-chart")) {
    return;
  }
  const graph = graphResult;
  if (!graph) {
    return;
  }
  if (!window.echarts) {
    graphLog("ECharts failed to load. Check the CDN connection or vendor ECharts locally.");
    return;
  }

  const element = $("original-graph-chart");
  if (!chart) {
    chart = window.echarts.init(element, null, { renderer: "canvas" });
    chart.on("click", (params) => {
      graphLog(params.data || params);
    });
    chartEventScope.listen(element, "wheel", graphWheel, { passive: false });
    chartEventScope.listen(element, "pointerdown", startGraphDrag);
    chartEventScope.listen(element, "pointermove", updateGraphDrag);
    chartEventScope.listen(element, "pointerup", stopGraphDrag);
    chartEventScope.listen(element, "pointercancel", stopGraphDrag);
    chartEventScope.listen(element, "lostpointercapture", stopGraphDrag);
    resizeObserver = new ResizeObserver(() => resizeOriginalGraphChart());
    resizeObserver.observe(element);
  }
  resizeOriginalGraphChart();
  readGraphControls();

  const categories = (graph.categories || []).map((category) => ({
    name: category.name,
    itemStyle: { color: graphLanguageColor(category.name) },
  }));
  const data = (graph.nodes || []).map((node) => ({
    ...node,
    itemStyle: { color: graphLanguageColor(node.lang) },
    label: { show: options.showLabels && node.value > 1 },
    tooltip: {
      formatter: [
        `<strong>${escapeHtml(node.title)}</strong>`,
        `${escapeHtml(node.language)} (${escapeHtml(node.lang)})`,
        `${escapeHtml(node.path)}`,
        `in: ${node.in_degree} | out: ${node.out_degree}`,
      ].join("<br>"),
    },
  }));
  const links = (graph.edges || []).map((edge) => ({
    ...edge,
    lineStyle: { width: Math.min(5, 1 + Number(edge.value || 1)), opacity: 0.48 },
    tooltip: {
      formatter: [
        `${escapeHtml(edge.source)} -> ${escapeHtml(edge.target)}`,
        `links: ${edge.value}`,
        ...(edge.links || []).slice(0, 4).map((link) => escapeHtml(link.resolved_path || link.target)),
      ].join("<br>"),
    },
  }));

  chart.setOption({
    backgroundColor: "transparent",
    tooltip: { trigger: "item", confine: true },
    legend: [{
      data: categories.map((category) => category.name),
      textStyle: { color: "#9aa89d" },
      top: 8,
      left: 8,
    }],
    series: [{
      type: "graph",
      layout: "force",
      roam: true,
      draggable: true,
      zoom: options.zoom,
      data,
      links,
      categories,
      edgeSymbol: ["none", "arrow"],
      edgeSymbolSize: 7,
      label: {
        color: "#edf4eb",
        formatter: (params) => params.data.title || params.data.name,
        position: "right",
      },
      emphasis: {
        focus: "adjacency",
        lineStyle: { opacity: 0.95 },
      },
      force: {
        repulsion: options.repulsion,
        gravity: options.gravity,
        edgeLength: [Math.max(30, Math.round(options.edgeLength * 0.45)), options.edgeLength],
      },
      lineStyle: {
        color: "source",
        curveness: 0.08,
      },
    }],
  }, true);
  resizeOriginalGraphChart();
  setTimeout(resizeOriginalGraphChart, 0);
}

function fitOriginalGraph() {
  if (chart) {
    options.zoom = 1;
    chart.dispatchAction({ type: "restore" });
    renderOriginalGraph();
  }
}

function zoomOriginalGraph(factor) {
  options.zoom = Math.max(
    0.15,
    Math.min(5, options.zoom * factor)
  );
  renderOriginalGraph();
}

function updateOriginalGraphForces() {
  readGraphControls();
  renderOriginalGraph();
}

function graphWheel(event) {
  if (!chart) {
    return;
  }
  event.preventDefault();
  const zoom = event.deltaY < 0 ? 1.12 : 0.89;
  options.zoom = Math.max(
    0.15,
    Math.min(5, options.zoom * zoom)
  );
  chart.dispatchAction({
    type: "graphRoam",
    seriesIndex: 0,
    zoom,
    originX: event.offsetX,
    originY: event.offsetY,
  });
}

function startGraphDrag(event) {
  if (!chart || event.button !== 0) {
    return;
  }
  event.preventDefault();
  $("original-graph-chart").setPointerCapture(event.pointerId);
  drag = {
    pointerId: event.pointerId,
    x: event.clientX,
    y: event.clientY,
  };
}

function updateGraphDrag(event) {
  if (!drag || drag.pointerId !== event.pointerId || !chart) {
    return;
  }
  event.preventDefault();
  const dx = event.clientX - drag.x;
  const dy = event.clientY - drag.y;
  drag.x = event.clientX;
  drag.y = event.clientY;
  chart.dispatchAction({
    type: "graphRoam",
    seriesIndex: 0,
    dx,
    dy,
  });
}

function stopGraphDrag(event) {
  if (!drag) {
    return;
  }
  if (event?.pointerId && event.pointerId !== drag.pointerId) {
    return;
  }
  drag = null;
}

function graphLanguageColor(language) {
  const palette = {
    de: "#e0a64b",
    en: "#5fb3d9",
    pl: "#d95f76",
    hu: "#8fd95f",
    it: "#5fd997",
    nl: "#d98e5f",
    el: "#9b7bda",
    es: "#d9c95f",
    uk: "#5f7ed9",
    pt: "#59c2b0",
    cs: "#c878d8",
    sk: "#88a85c",
  };
  return palette[language] || "#9aa89d";
}

function formatLanguageCounts(counts, names) {
  return Object.entries(counts)
    .map(([code, count]) => `${names[code] || code}: ${count}`)
    .join(", ");
}

function setBusy(isBusy) {
  setControlsBusy(busyControls, isBusy);
}
