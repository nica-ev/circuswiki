(function () {
  var MEASUREMENT_ID = "G-ZJ5FMB5HRM";
  var CONSENT_KEY = "circuswiki:analytics-consent";
  var GA_SCRIPT_ID = "cw-google-analytics";
  var SETTINGS_ID = "cw-analytics-settings";
  var BANNER_ID = "cw-analytics-consent";
  var loaded = false;

  var TEXT = {
    de: {
      title: "Cookie-Einstellungen",
      description:
        "Wir nutzen Google Analytics nur mit deiner Zustimmung, um zu verstehen, welche Seiten hilfreich sind und wie CircusWiki verbessert werden kann.",
      accept: "Akzeptieren",
      decline: "Ablehnen",
      change: "Cookie-Einstellungen ändern",
      accepted: "Analytics ist aktuell aktiviert.",
      declined: "Analytics ist aktuell deaktiviert.",
    },
    en: {
      title: "Cookie settings",
      description:
        "We use Google Analytics only with your consent to understand which pages are useful and how CircusWiki can be improved.",
      accept: "Accept",
      decline: "Decline",
      change: "Change cookie settings",
      accepted: "Analytics is currently enabled.",
      declined: "Analytics is currently disabled.",
    },
  };

  function language() {
    var lang = (document.documentElement.getAttribute("lang") || navigator.language || "en").toLowerCase();
    return lang.indexOf("de") === 0 ? "de" : "en";
  }

  function messages() {
    return TEXT[language()] || TEXT.en;
  }

  function storedConsent() {
    try {
      return window.localStorage.getItem(CONSENT_KEY);
    } catch (error) {
      return null;
    }
  }

  function storeConsent(value) {
    try {
      window.localStorage.setItem(CONSENT_KEY, value);
    } catch (error) {
      // Consent still applies for this page if storage is unavailable.
    }
  }

  function currentPath() {
    return window.location.pathname + window.location.search + window.location.hash;
  }

  function sendPageView() {
    if (!loaded || typeof window.gtag !== "function") {
      return;
    }

    window.gtag("event", "page_view", {
      page_title: document.title,
      page_location: window.location.href,
      page_path: currentPath(),
    });
  }

  function loadAnalytics() {
    if (loaded || document.getElementById(GA_SCRIPT_ID)) {
      loaded = true;
      sendPageView();
      return;
    }

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () {
      window.dataLayer.push(arguments);
    };
    window.gtag("js", new Date());
    window.gtag("config", MEASUREMENT_ID, { send_page_view: false });

    var script = document.createElement("script");
    script.id = GA_SCRIPT_ID;
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(MEASUREMENT_ID);
    script.addEventListener("load", function () {
      loaded = true;
      sendPageView();
    });
    document.head.appendChild(script);
  }

  function expireCookie(name, domain, path) {
    document.cookie =
      name +
      "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=" +
      path +
      (domain ? "; domain=" + domain : "") +
      "; SameSite=Lax";
  }

  function deleteAnalyticsCookies() {
    var names = ["_ga", "_gid", "_gat", "_gat_gtag_" + MEASUREMENT_ID.replace(/-/g, "_")];
    var hostname = window.location.hostname;
    var domains = ["", hostname, "." + hostname];
    var paths = ["/", window.location.pathname.replace(/[^/]*$/, "") || "/"];

    names.forEach(function (name) {
      domains.forEach(function (domain) {
        paths.forEach(function (path) {
          expireCookie(name, domain, path);
        });
      });
    });
  }

  function removeBanner() {
    var existing = document.getElementById(BANNER_ID);
    if (existing) {
      existing.remove();
    }
  }

  function setConsent(value) {
    storeConsent(value);
    removeBanner();
    updateSettingsLink();

    if (value === "accepted") {
      loadAnalytics();
    } else {
      deleteAnalyticsCookies();
    }
  }

  function button(label, className, value) {
    var element = document.createElement("button");
    element.type = "button";
    element.className = className;
    element.textContent = label;
    element.addEventListener("click", function () {
      setConsent(value);
    });
    return element;
  }

  function showBanner(force) {
    if (!force && storedConsent()) {
      return;
    }

    removeBanner();

    var text = messages();
    var banner = document.createElement("section");
    banner.id = BANNER_ID;
    banner.className = "cw-analytics-consent";
    banner.setAttribute("aria-labelledby", BANNER_ID + "-title");
    banner.innerHTML = [
      '<div class="cw-analytics-consent__body">',
      '<h2 id="' + BANNER_ID + '-title">' + text.title + "</h2>",
      "<p>" + text.description + "</p>",
      "</div>",
      '<div class="cw-analytics-consent__actions"></div>',
    ].join("");

    var actions = banner.querySelector(".cw-analytics-consent__actions");
    actions.appendChild(button(text.decline, "cw-analytics-consent__button cw-analytics-consent__button--secondary", "declined"));
    actions.appendChild(button(text.accept, "cw-analytics-consent__button cw-analytics-consent__button--primary", "accepted"));
    document.body.appendChild(banner);
  }

  function updateSettingsLink() {
    var link = document.getElementById(SETTINGS_ID);
    if (!link) {
      return;
    }

    var text = messages();
    var consent = storedConsent();
    link.textContent = text.change;
    link.title = consent === "accepted" ? text.accepted : text.declined;
  }

  function ensureSettingsLink() {
    if (document.getElementById(SETTINGS_ID)) {
      updateSettingsLink();
      return;
    }

    var text = messages();
    var footer = document.querySelector(".md-footer-meta__inner, .md-footer, footer") || document.body;
    var link = document.createElement("button");
    link.id = SETTINGS_ID;
    link.type = "button";
    link.className = "cw-analytics-settings";
    link.textContent = text.change;
    link.addEventListener("click", function () {
      showBanner(true);
    });

    footer.appendChild(link);
    updateSettingsLink();
  }

  function installNavigationTracking() {
    if (window.document$ && typeof window.document$.subscribe === "function") {
      window.document$.subscribe(function () {
        if (storedConsent() === "accepted") {
          sendPageView();
        }
        ensureSettingsLink();
      });
      return;
    }

    ["pushState", "replaceState"].forEach(function (method) {
      var original = window.history[method];
      if (typeof original !== "function") {
        return;
      }
      window.history[method] = function () {
        var result = original.apply(this, arguments);
        if (storedConsent() === "accepted") {
          window.setTimeout(sendPageView, 0);
        }
        return result;
      };
    });

    window.addEventListener("popstate", function () {
      if (storedConsent() === "accepted") {
        window.setTimeout(sendPageView, 0);
      }
    });
  }

  function init() {
    ensureSettingsLink();
    installNavigationTracking();

    if (storedConsent() === "accepted") {
      loadAnalytics();
    } else if (!storedConsent()) {
      showBanner(false);
    } else {
      deleteAnalyticsCookies();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
