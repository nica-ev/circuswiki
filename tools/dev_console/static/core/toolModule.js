export function defineToolModule(feature) {
  for (const key of ["id", "label", "group", "mount"]) {
    if (!feature?.[key]) {
      throw new Error(`Tool module is missing ${key}`);
    }
  }
  return {
    unmount() {},
    refresh() {},
    ...feature,
  };
}
