(function () {
  "use strict";

  if (!window.fetch || window.__cwLazySearchInstalled) {
    return;
  }

  window.__cwLazySearchInstalled = true;
  var nativeFetch = window.fetch.bind(window);
  var unlocked = false;
  var queued = [];

  function isSearchIndex(resource) {
    try {
      var value = resource && resource.url ? resource.url : resource;
      var url = new URL(String(value), window.location.href);
      return /\/search\.json$/.test(url.pathname);
    } catch (error) {
      return false;
    }
  }

  function unlockSearch() {
    if (unlocked) {
      return;
    }
    unlocked = true;
    queued.splice(0).forEach(function (start) {
      start();
    });
  }

  window.fetch = function (resource, options) {
    if (unlocked || !isSearchIndex(resource)) {
      return nativeFetch(resource, options);
    }
    return new Promise(function (resolve, reject) {
      queued.push(function () {
        nativeFetch(resource, options).then(resolve, reject);
      });
    });
  };

  if (window.XMLHttpRequest) {
    var nativeOpen = window.XMLHttpRequest.prototype.open;
    var nativeSend = window.XMLHttpRequest.prototype.send;
    var nativeAbort = window.XMLHttpRequest.prototype.abort;

    window.XMLHttpRequest.prototype.open = function (method, url) {
      this.__cwLazySearchAborted = false;
      this.__cwLazySearchGeneration = (this.__cwLazySearchGeneration || 0) + 1;
      this.__cwLazySearchRequest = isSearchIndex(url);
      return nativeOpen.apply(this, arguments);
    };

    window.XMLHttpRequest.prototype.send = function (body) {
      var request = this;
      var generation = request.__cwLazySearchGeneration;
      if (unlocked || !request.__cwLazySearchRequest) {
        return nativeSend.apply(request, arguments);
      }
      queued.push(function () {
        if (!request.__cwLazySearchAborted && request.__cwLazySearchGeneration === generation) {
          nativeSend.call(request, body);
        }
      });
    };

    window.XMLHttpRequest.prototype.abort = function () {
      this.__cwLazySearchAborted = true;
      return nativeAbort.apply(this, arguments);
    };
  }

  document.addEventListener("click", function (event) {
    if (event.target.closest('label[for="__search"], .md-search__button')) {
      unlockSearch();
    }
  }, true);

  function isSearchFieldInteraction(event) {
    var path = typeof event.composedPath === "function" ? event.composedPath() : [event.target];
    return path.some(function (node) {
      if (!node || typeof node.matches !== "function") {
        return false;
      }
      if (node.matches('.md-search__input, [data-md-component="search"] input')) {
        return true;
      }
      return node.matches('input[role="combobox"]') &&
        typeof ShadowRoot !== "undefined" &&
        node.getRootNode() instanceof ShadowRoot;
    });
  }

  ["focus", "input"].forEach(function (eventName) {
    document.addEventListener(eventName, function (event) {
      if (isSearchFieldInteraction(event)) {
        unlockSearch();
      }
    }, true);
  });

  document.addEventListener("keydown", function (event) {
    var target = event.target;
    var isTyping = target && (target.matches("input, textarea, select") || target.isContentEditable);
    if (event.key === "/" && !event.altKey && !event.ctrlKey && !event.metaKey && !isTyping) {
      unlockSearch();
    }
  }, true);
})();
