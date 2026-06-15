export function cssPixelValue(value, fallback) {
  const parsed = Number.parseFloat(String(value).trim());
  return Number.isFinite(parsed) ? parsed : fallback;
}

export function matrixLayoutSizes() {
  const styles = getComputedStyle(document.documentElement);
  return {
    labelWidth: cssPixelValue(styles.getPropertyValue("--matrix-label-width"), 82),
    minPlotWidth: cssPixelValue(styles.getPropertyValue("--matrix-min-plot-width"), 1320),
  };
}
