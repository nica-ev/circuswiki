# ADR-001: Scale CircusFinder maps with client-side clustering

**Status**: Accepted | **Date**: 2026-10-10 | **Participants**: CircusWiki maintainers and contributors

## Context

CircusFinder is a static Zensical page backed by a compact JSON export of the
Markdown/YAML directory. Its first substantial dataset contains roughly 500
mapped records, and future imports may raise this to 5,000 or more.

Two independent costs affect the map:

1. Raster map tiles must be requested, downloaded, decoded, and painted again
   for each newly visited zoom level. This causes the visible tile-loading
   effect and depends on the visitor's connection, browser cache, and tile
   service response time.
2. The original Leaflet implementation created one HTML marker for every
   matching record. Hundreds are workable, but repositioning thousands of DOM
   elements during pan, zoom, and filtering does not scale smoothly.

The exported marker data itself is comparatively small. Several thousand
compact records can still be downloaded and searched in the browser. Rendering
all of them as individual HTML elements is the earlier practical limit.

## Decision

We decided to retain the current static Leaflet architecture and add
client-side marker clustering as the first scaling step.

CircusFinder vendors Leaflet.markercluster 1.5.3 alongside Leaflet rather than
loading it from a runtime CDN. The map:

- groups nearby records into count-bearing cluster markers;
- expands a cluster when it is clicked;
- reveals and opens an individual marker when its result card is activated;
- bulk-adds markers with chunked processing; and
- removes clusters and markers sufficiently far outside the visible map bounds.

Search and type filters continue to operate on the complete exported dataset.
They rebuild the cluster layer from the matching records, while the Markdown
entries remain the source of truth.

Clustering is a marker-rendering optimization. It does not remove raster tile
network latency. The existing raster tile layer remains appropriate for the
prototype, but it must be evaluated separately as usage grows.

## Alternatives considered

- **Keep individual HTML markers:** simplest, but increasingly slow and
  visually crowded as the directory grows.
- **Move directly to Canvas rendering:** reduces DOM overhead, but clustering
  provides a larger immediate usability improvement and keeps existing markers
  and popups intact.
- **Move the static page directly to MapLibre/vector tiles:** offers smoother,
  GPU-assisted rendering and more scaling headroom, but adds complexity before
  the directory's needs justify replacing the working Leaflet prototype.
- **Build a separate location application now:** separation alone would not
  improve speed. It becomes useful when paired with a specialized rendering
  stack, offline caching, spatial indexing, or regional data loading.

## Consequences

- (+) World and regional views render far fewer HTML elements.
- (+) Dense areas become understandable instead of showing overlapping pins.
- (+) The same static JSON export and GitHub Pages deployment remain usable.
- (+) The vendored dependency works without a JavaScript CDN at runtime.
- (+) Chunked bulk loading provides headroom for datasets in the low thousands.
- (-) One additional JavaScript and CSS dependency must be maintained and
  tested with future Leaflet upgrades.
- (-) Opening an individual result may require an automatic zoom through its
  parent cluster.
- (-) Tile loading can still be visibly delayed on an uncached zoom level.
- (±) Five thousand records are a reasonable next target, not a guaranteed
  performance ceiling. Performance must be measured on desktop and mobile as
  the real dataset grows.

## Future work and decision triggers

Measure initial render, zoom, filter, and card-focus behavior when the mapped
dataset passes approximately 1,000 and 5,000 records. Prioritize the following
only when measurements or user experience justify them:

1. Avoid rebuilding unchanged markers during filtering and render only records
   needed near the current viewport.
2. Evaluate tile caching, preloading, and a tile service suitable for expected
   production traffic.
3. Evaluate Canvas-rendered point layers if high-zoom views still expose too
   many individual HTML markers.
4. For a dedicated CircusFinder application, evaluate MapLibre, vector tiles,
   GPU-rendered points, spatial indexes, regional data loading, and a service
   worker for offline caching.

A dedicated application should continue consuming a validated, compact export
from the CircusWiki repository. It should not require moving the authoritative
place records out of Markdown.
