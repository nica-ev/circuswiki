var FALLBACK_LANGUAGE_CODES = ["de", "en"];

function currentScriptPath(scriptName) {
  var scripts = document.getElementsByTagName("script");
  for (var i = 0; i < scripts.length; i += 1) {
    var src = scripts[i].src || "";
    if (src.indexOf("/javascripts/" + scriptName) !== -1) {
      return new URL(src, window.location.href).pathname;
    }
  }
  return window.location.pathname;
}

function pageTranslationContext() {
  var element = document.querySelector('script[data-cw-page-translations="true"]');
  if (!element) {
    return null;
  }
  try {
    return JSON.parse(element.textContent || "{}");
  } catch (error) {
    return null;
  }
}

function languageCodes(context) {
  if (context && Array.isArray(context.languages) && context.languages.length) {
    return context.languages;
  }
  return FALLBACK_LANGUAGE_CODES;
}

function siteRootPath(codes) {
  var scriptPath = currentScriptPath("language-switcher.js");
  var root = scriptPath.replace(/javascripts\/language-switcher\.js$/, "");
  root = root.replace(new RegExp("(?:" + codes.join("|") + ")\\/$"), "");
  if (!root.startsWith("/")) {
    root = "/" + root;
  }
  return root.endsWith("/") ? root : root + "/";
}

function currentRelativePath(path, codes, defaultLanguage, base) {
  for (var i = 0; i < codes.length; i += 1) {
    var language = codes[i];
    if (language === defaultLanguage) {
      continue;
    }
    var languageRoot = base + language + "/";
    if (path.indexOf(languageRoot) === 0) {
      return path.slice(languageRoot.length);
    }
  }
  if (path.indexOf(base) === 0) {
    return path.slice(base.length);
  }
  return path.replace(/^\/+/, "");
}

function rewriteLanguageLinks() {
  var translation = pageTranslationContext();
  var codes = languageCodes(translation);
  var defaultLanguage = (translation && translation.default_language) || "de";
  var base = siteRootPath(codes);
  var relativePath = currentRelativePath(window.location.pathname, codes, defaultLanguage, base);

  if (codes.some(function(language) {
    return relativePath === language || relativePath === language + "/";
  })) {
    relativePath = "";
  }

  codes.forEach(function(language) {
    var languageRoot = language === defaultLanguage ? base : base + language + "/";
    var entry = translation && translation.links ? translation.links[language] : null;
    var href = entry && entry.url ? entry.url : languageRoot + relativePath;
    document.querySelectorAll('[hreflang="' + language + '"]').forEach(function(link) {
      link.href = href;
      if (entry && entry.fallback) {
        link.title = "Translation missing. Opens a fallback page.";
      } else {
        link.removeAttribute("title");
      }
    });
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(rewriteLanguageLinks);
} else {
  document.addEventListener("DOMContentLoaded", rewriteLanguageLinks);
}
