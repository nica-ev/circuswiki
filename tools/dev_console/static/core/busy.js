import { $ } from "./dom.js";

export function setControlsBusy(controlIds, isBusy) {
  controlIds.forEach((id) => {
    const element = $(id);
    if (element) {
      element.disabled = isBusy;
    }
  });
}
