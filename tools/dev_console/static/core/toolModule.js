export function defineToolModule(feature) {
  for (const key of ["id", "label", "group"]) {
    if (!feature?.[key]) {
      throw new Error(`Tool module is missing ${key}`);
    }
  }
  if (typeof feature?.mount !== "function") {
    throw new Error("Tool module is missing mount");
  }
  return {
    unmount() {},
    refresh() {},
    ...feature,
  };
}
