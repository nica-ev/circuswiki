export function createEventScope() {
  const removers = [];
  return {
    listen(target, type, handler, options) {
      target.addEventListener(type, handler, options);
      removers.push(() => target.removeEventListener(type, handler, options));
    },
    clear() {
      while (removers.length) {
        removers.pop()();
      }
    },
  };
}
