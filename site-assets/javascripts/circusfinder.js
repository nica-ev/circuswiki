(function () {
  "use strict";

  var SCRIPT_NAME = "circusfinder.js";
  // Zensical's instant navigation changes the document URL while retaining the
  // loaded scripts. Capture this absolute URL during initial script execution;
  // reading script.src later would resolve its relative attribute against the
  // newly navigated page instead.
  var SCRIPT_SOURCE = document.currentScript && document.currentScript.src
    ? document.currentScript.src
    : "";
  var leafletPromise;

  var TRANSLATIONS = {
    de: {
      search: "Orte und Angebote durchsuchen",
      searchLabel: "CircusFinder durchsuchen",
      allKinds: "Alle Arten",
      nearby: "In meiner Nähe",
      locating: "Standort wird ermittelt …",
      locationError: "Der Standort konnte nicht ermittelt werden.",
      results: "Ergebnisse",
      oneResult: "1 Ergebnis",
      manyResults: "{count} Ergebnisse",
      noResults: "Keine passenden Einträge gefunden.",
      mapLabel: "Karte mit CircusFinder-Einträgen",
      listLabel: "CircusFinder-Ergebnisse",
      website: "Website",
      details: "Wiki-Eintrag",
      email: "E-Mail",
      distance: "{distance} km entfernt",
      demo: "Testdaten",
      exact: "Genaue Adresse",
      approximate: "Ungefähre Position",
      city: "Position zeigt nur die Stadt",
      networkNotice: "Ohne Kartenposition",
      exactMarker: "Blauer Marker: genaue Adresse",
      approximateMarker: "Orangefarbener Marker: ungefähre Position",
      contact: "Kontakt",
      schedule: "Zeiten",
      source: "Quelle",
      scheduleLink: "Aktuelle Termine",
      loadError: "CircusFinder konnte nicht geladen werden.",
      training_space: "Trainingsort",
      circus_school: "Zirkusschule",
      youth_circus: "Jugendzirkus",
      network: "Netzwerk",
      organization: "Organisation",
      network_contact: "Netzwerkkontakt",
      distributor: "Händler",
      global_partner_european: "Globaler Partner – Europa",
      global_partner_worldwide: "Globaler Partner – weltweit",
      regional_partner: "Regionaler Partner",
      local_partner: "Lokaler Partner"
    },
    en: {
      search: "Search places and activities",
      searchLabel: "Search CircusFinder",
      allKinds: "All types",
      nearby: "Near me",
      locating: "Finding your location …",
      locationError: "Your location could not be determined.",
      results: "Results",
      oneResult: "1 result",
      manyResults: "{count} results",
      noResults: "No matching entries found.",
      mapLabel: "Map of CircusFinder entries",
      listLabel: "CircusFinder results",
      website: "Website",
      details: "Wiki entry",
      email: "Email",
      distance: "{distance} km away",
      demo: "Demo data",
      exact: "Exact address",
      approximate: "Approximate position",
      city: "Position shows the city only",
      networkNotice: "No map position",
      exactMarker: "Blue marker: exact address",
      approximateMarker: "Orange marker: approximate position",
      contact: "Contact",
      schedule: "Schedule",
      source: "Source",
      scheduleLink: "Current schedule",
      loadError: "CircusFinder could not be loaded.",
      training_space: "Training space",
      circus_school: "Circus school",
      youth_circus: "Youth circus",
      network: "Network",
      organization: "Organization",
      network_contact: "Network contact",
      distributor: "Distributor",
      global_partner_european: "Global Partner – European",
      global_partner_worldwide: "Global Partner – World-Wide",
      regional_partner: "Regional Partner",
      local_partner: "Local Partner"
    }
  };

  function currentScriptUrl() {
    if (SCRIPT_SOURCE) {
      return SCRIPT_SOURCE;
    }
    var scripts = Array.prototype.slice.call(document.scripts || []);
    var script = scripts.find(function (item) {
      return (item.src || "").indexOf("/javascripts/" + SCRIPT_NAME) !== -1;
    });
    return script ? script.src : "";
  }

  function assetRoot() {
    var source = currentScriptUrl();
    return source ? new URL("../", source) : new URL("./", window.location.href);
  }

  function datasetUrl() {
    return new URL("data/circusfinder.v1.json", assetRoot()).toString();
  }

  function leafletAssetUrl(path) {
    return new URL("vendor/leaflet/" + path, assetRoot()).toString();
  }

  function ensureLeafletCss() {
    var existing = document.querySelector('link[data-cw-leaflet="true"]');
    if (existing) {
      if (existing.sheet) {
        return Promise.resolve();
      }
      return new Promise(function (resolve, reject) {
        existing.addEventListener("load", resolve, { once: true });
        existing.addEventListener("error", function () {
          reject(new Error("Map stylesheet request failed: " + existing.href));
        }, { once: true });
      });
    }
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = leafletAssetUrl("leaflet.css");
    link.setAttribute("data-cw-leaflet", "true");
    var loaded = new Promise(function (resolve, reject) {
      link.addEventListener("load", resolve, { once: true });
      link.addEventListener("error", function () {
        reject(new Error("Map stylesheet request failed: " + link.href));
      }, { once: true });
    });
    document.head.appendChild(link);
    return loaded;
  }

  function loadLeaflet() {
    return ensureLeafletCss().then(function () {
      if (window.L) {
        return window.L;
      }
      if (leafletPromise) {
        return leafletPromise;
      }
      leafletPromise = new Promise(function (resolve, reject) {
        var script = document.createElement("script");
        script.src = leafletAssetUrl("leaflet.js");
        script.onload = function () { resolve(window.L); };
        script.onerror = function () { reject(new Error("Map library request failed: " + script.src)); };
        document.head.appendChild(script);
      });
      return leafletPromise;
    });
  }

  function restoreFinder(container) {
    var map = container._circusFinderMap;
    if (!map) {
      container.removeAttribute("data-cw-ready");
      return false;
    }
    ensureLeafletCss().then(function () {
      window.requestAnimationFrame(function () {
        map.invalidateSize({ animate: false, pan: false });
      });
    }).catch(function (error) {
      showError(container, error);
    });
    return true;
  }

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function safeHttpUrl(value) {
    try {
      var url = new URL(value);
      return url.protocol === "http:" || url.protocol === "https:" ? url.toString() : "";
    } catch (error) {
      return "";
    }
  }

  function labelsFor(language) {
    return TRANSLATIONS[language] || TRANSLATIONS.en;
  }

  function kindLabel(kind, labels) {
    return labels[kind] || kind.replace(/_/g, " ");
  }

  function locationText(record) {
    var location = record.location || {};
    var cityLine = [location.postal_code, location.city].filter(Boolean).join(" ");
    return [location.address, cityLine, location.region, location.country_code].filter(Boolean).join(", ");
  }

  function searchText(record) {
    var location = record.location || {};
    return [
      record.title,
      record.description,
      record.organization,
      location.address,
      location.postal_code,
      location.city,
      location.region,
      location.country_code,
      (record.entry_kinds || []).join(" "),
      (record.collective_statuses || []).join(" "),
      ((record.contact && record.contact.people) || []).join(" "),
      ((record.contact && record.contact.emails) || []).join(" "),
      record.contact && record.contact.phone,
      (record.offers || []).join(" "),
      (record.opening_hours || []).join(" "),
      record.schedule_note,
      (record.source || []).map(function (source) { return source.name || ""; }).join(" ")
    ].join(" ").toLocaleLowerCase();
  }

  function sourceHtml(record, labels) {
    var sources = (record.source || []).map(function (source) {
      var name = escapeHtml(source.name || "");
      var url = safeHttpUrl(source.url);
      return url
        ? '<a href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + name + "</a>"
        : name;
    }).filter(Boolean);
    return sources.length
      ? '<span class="cw-finder__source"><strong>' + escapeHtml(labels.source) + ":</strong> " + sources.join(" / ") + "</span>"
      : "";
  }

  function hasCoordinates(record) {
    var location = record.location || {};
    return typeof location.latitude === "number" && typeof location.longitude === "number";
  }

  function distanceKm(origin, record) {
    if (!origin || !hasCoordinates(record)) {
      return null;
    }
    var location = record.location;
    var toRadians = function (value) { return value * Math.PI / 180; };
    var latitudeDelta = toRadians(location.latitude - origin.latitude);
    var longitudeDelta = toRadians(location.longitude - origin.longitude);
    var a = Math.sin(latitudeDelta / 2) * Math.sin(latitudeDelta / 2) +
      Math.cos(toRadians(origin.latitude)) * Math.cos(toRadians(location.latitude)) *
      Math.sin(longitudeDelta / 2) * Math.sin(longitudeDelta / 2);
    return 6371 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }

  function precisionLabel(record, labels) {
    var precision = record.location && record.location.precision;
    if (precision === "exact") {
      return labels.exact;
    }
    if (precision === "approximate") {
      return labels.approximate;
    }
    if (precision === "city") {
      return labels.city;
    }
    if (precision === "none") {
      return labels.networkNotice;
    }
    return "";
  }

  function recordActions(record, labels) {
    var actions = [];
    var website = safeHttpUrl(record.contact && record.contact.website);
    if (website) {
      actions.push('<a href="' + escapeHtml(website) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(labels.website) + "</a>");
    }
    var emails = record.contact && record.contact.emails && record.contact.emails.length
      ? record.contact.emails
      : (record.contact && record.contact.email ? [record.contact.email] : []);
    emails.forEach(function (email) {
      actions.push('<a href="mailto:' + encodeURIComponent(email) + '">' + escapeHtml(email) + "</a>");
    });
    var phone = record.contact && record.contact.phone;
    if (phone) {
      actions.push('<a href="tel:' + escapeHtml(phone.replace(/[^+0-9]/g, "")) + '">' + escapeHtml(phone) + "</a>");
    }
    var scheduleUrl = safeHttpUrl(record.schedule_url);
    if (scheduleUrl) {
      actions.push('<a href="' + escapeHtml(scheduleUrl) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(labels.scheduleLink) + "</a>");
    }
    if (record.detail_url) {
      actions.push('<a href="' + escapeHtml(record.detail_url) + '">' + escapeHtml(labels.details) + "</a>");
    }
    return actions.join("");
  }

  function popupHtml(record, labels, distance) {
    var location = locationText(record);
    var distanceText = distance == null ? "" : labels.distance.replace("{distance}", distance.toFixed(1));
    var people = record.contact && record.contact.people ? record.contact.people.join(" / ") : "";
    var hours = (record.opening_hours || []).join(" · ");
    return [
      '<article class="cw-finder-popup">',
      '<strong class="cw-finder-popup__title">' + escapeHtml(record.title) + "</strong>",
      location ? '<span class="cw-finder-popup__location">' + escapeHtml(location) + "</span>" : "",
      distanceText ? '<span class="cw-finder-popup__distance">' + escapeHtml(distanceText) + "</span>" : "",
      people ? '<span class="cw-finder-popup__contact"><strong>' + escapeHtml(labels.contact) + ":</strong> " + escapeHtml(people) + "</span>" : "",
      hours ? '<span class="cw-finder-popup__schedule"><strong>' + escapeHtml(labels.schedule) + ":</strong> " + escapeHtml(hours) + "</span>" : "",
      record.description ? "<p>" + escapeHtml(record.description) + "</p>" : "",
      sourceHtml(record, labels),
      '<span class="cw-finder-popup__actions">' + recordActions(record, labels) + "</span>",
      "</article>"
    ].join("");
  }

  function cardHtml(record, labels, distance) {
    var kinds = (record.entry_kinds || []).map(function (kind) {
      return '<span class="cw-finder__tag">' + escapeHtml(kindLabel(kind, labels)) + "</span>";
    }).join("");
    var statuses = (record.collective_statuses || []).map(function (status) {
      return '<span class="cw-finder__tag cw-finder__tag--status">' + escapeHtml(kindLabel(status, labels)) + "</span>";
    }).join("");
    var location = locationText(record);
    var precision = precisionLabel(record, labels);
    var distanceText = distance == null ? "" : labels.distance.replace("{distance}", distance.toFixed(1));
    var people = record.contact && record.contact.people ? record.contact.people.join(" / ") : "";
    var hours = (record.opening_hours || []).join(" · ");
    return [
      '<article class="cw-finder-card" data-record-id="' + escapeHtml(record.id) + '" tabindex="0">',
      '<div class="cw-finder-card__heading">',
      "<h3>" + escapeHtml(record.title) + "</h3>",
      record.is_demo ? '<span class="cw-finder__demo">' + escapeHtml(labels.demo) + "</span>" : "",
      "</div>",
      '<div class="cw-finder-card__tags">' + kinds + statuses + "</div>",
      location ? '<p class="cw-finder-card__location">' + escapeHtml(location) + "</p>" : "",
      precision ? '<p class="cw-finder-card__precision">' + escapeHtml(precision) + "</p>" : "",
      distanceText ? '<p class="cw-finder-card__distance">' + escapeHtml(distanceText) + "</p>" : "",
      people ? '<p class="cw-finder-card__contact"><strong>' + escapeHtml(labels.contact) + ":</strong> " + escapeHtml(people) + "</p>" : "",
      hours ? '<p class="cw-finder-card__schedule"><strong>' + escapeHtml(labels.schedule) + ":</strong> " + escapeHtml(hours) + "</p>" : "",
      record.schedule_note ? '<p class="cw-finder-card__schedule-note">' + escapeHtml(record.schedule_note) + "</p>" : "",
      record.description ? "<p>" + escapeHtml(record.description) + "</p>" : "",
      sourceHtml(record, labels),
      '<div class="cw-finder-card__actions">' + recordActions(record, labels) + "</div>",
      "</article>"
    ].join("");
  }

  function renderShell(container, labels) {
    container.innerHTML = [
      '<div class="cw-finder__toolbar">',
      '<label class="cw-finder__search">',
      '<span class="cw-sr-only">' + escapeHtml(labels.searchLabel) + "</span>",
      '<input type="search" data-cw-search placeholder="' + escapeHtml(labels.search) + '" autocomplete="off">',
      "</label>",
      '<label class="cw-finder__kind"><span class="cw-sr-only">' + escapeHtml(labels.allKinds) + "</span>",
      '<select data-cw-kind><option value="">' + escapeHtml(labels.allKinds) + "</option></select></label>",
      '<button type="button" class="cw-finder__nearby" data-cw-nearby>' + escapeHtml(labels.nearby) + "</button>",
      "</div>",
      '<p class="cw-finder__status" data-cw-status aria-live="polite"></p>',
      '<div class="cw-finder__layout">',
      '<div class="cw-finder__map-column">',
      '<div class="cw-finder__map" data-cw-map role="region" aria-label="' + escapeHtml(labels.mapLabel) + '"></div>',
      '<p class="cw-finder__map-note"><span class="cw-finder__map-key"><span class="cw-finder__marker-swatch cw-finder__marker--exact" aria-hidden="true"></span>' + escapeHtml(labels.exactMarker) + '</span><span class="cw-finder__map-key"><span class="cw-finder__marker-swatch cw-finder__marker--approximate" aria-hidden="true"></span>' + escapeHtml(labels.approximateMarker) + "</span></p>",
      "</div>",
      '<section class="cw-finder__results" aria-label="' + escapeHtml(labels.listLabel) + '">',
      '<div class="cw-finder__results-heading"><h2>' + escapeHtml(labels.results) + '</h2><span data-cw-count></span></div>',
      '<div class="cw-finder__cards" data-cw-cards></div>',
      "</section>",
      "</div>"
    ].join("");
  }

  function initializeFinder(container, dataset, L) {
    var labels = labelsFor(dataset.language);
    renderShell(container, labels);

    var records = dataset.records || [];
    var search = container.querySelector("[data-cw-search]");
    var kind = container.querySelector("[data-cw-kind]");
    var nearby = container.querySelector("[data-cw-nearby]");
    var status = container.querySelector("[data-cw-status]");
    var count = container.querySelector("[data-cw-count]");
    var cards = container.querySelector("[data-cw-cards]");
    var mapElement = container.querySelector("[data-cw-map]");
    var origin = null;
    var userLayer = null;
    var markers = {};

    Array.from(new Set(records.reduce(function (all, record) {
      return all.concat(record.entry_kinds || []);
    }, []))).sort().forEach(function (entryKind) {
      var option = document.createElement("option");
      option.value = entryKind;
      option.textContent = kindLabel(entryKind, labels);
      kind.appendChild(option);
    });

    var map = L.map(mapElement, { scrollWheelZoom: false }).setView([51.15, 10.45], 5);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map);
    var markerLayer = L.layerGroup().addTo(map);

    function markerOptions(record) {
      var precision = record.location && record.location.precision;
      var markerClass = precision === "exact" ? "exact" : "approximate";
      return {
        icon: L.divIcon({
          className: "cw-finder__marker-wrap",
          html: '<span class="cw-finder__marker cw-finder__marker--' + markerClass + '"></span>',
          iconSize: [24, 24],
          iconAnchor: [12, 12],
          popupAnchor: [0, -14]
        })
      };
    }

    function coordinateKey(record) {
      return record.location.latitude.toFixed(6) + "," + record.location.longitude.toFixed(6);
    }

    function displayCoordinates(record, coordinateCounts) {
      var coordinates = [record.location.latitude, record.location.longitude];
      var precision = record.location.precision;
      if ((precision !== "city" && precision !== "approximate") || coordinateCounts[coordinateKey(record)] < 2) {
        return coordinates;
      }
      var hash = Array.from(record.id).reduce(function (value, character) {
        return ((value << 5) - value + character.charCodeAt(0)) | 0;
      }, 0);
      var angle = (Math.abs(hash) % 360) * Math.PI / 180;
      var radius = 0.018 + (Math.abs(hash >> 8) % 5) * 0.004;
      var longitudeScale = Math.max(Math.cos(coordinates[0] * Math.PI / 180), 0.25);
      return [
        coordinates[0] + Math.sin(angle) * radius,
        coordinates[1] + Math.cos(angle) * radius / longitudeScale
      ];
    }

    function filteredRecords() {
      var query = search.value.trim().toLocaleLowerCase();
      var selectedKind = kind.value;
      return records.filter(function (record) {
        return (!query || searchText(record).indexOf(query) !== -1) &&
          (!selectedKind || (record.entry_kinds || []).indexOf(selectedKind) !== -1);
      }).map(function (record) {
        return { record: record, distance: distanceKm(origin, record) };
      }).sort(function (left, right) {
        if (origin) {
          if (left.distance == null) { return 1; }
          if (right.distance == null) { return -1; }
          if (left.distance !== right.distance) { return left.distance - right.distance; }
        }
        return left.record.title.localeCompare(right.record.title, dataset.language, { sensitivity: "base" });
      });
    }

    function focusRecord(id) {
      var marker = markers[id];
      if (!marker) {
        return;
      }
      map.setView(marker.getLatLng(), Math.max(map.getZoom(), 11), { animate: true });
      marker.openPopup();
      mapElement.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    function render() {
      var filtered = filteredRecords();
      markerLayer.clearLayers();
      markers = {};
      cards.innerHTML = filtered.length ? filtered.map(function (item) {
        return cardHtml(item.record, labels, item.distance);
      }).join("") : '<p class="cw-finder__empty">' + escapeHtml(labels.noResults) + "</p>";
      count.textContent = filtered.length === 1 ? labels.oneResult : labels.manyResults.replace("{count}", filtered.length);

      var bounds = [];
      var coordinateCounts = {};
      filtered.forEach(function (item) {
        if (hasCoordinates(item.record)) {
          var key = coordinateKey(item.record);
          coordinateCounts[key] = (coordinateCounts[key] || 0) + 1;
        }
      });
      filtered.forEach(function (item) {
        if (!hasCoordinates(item.record)) {
          return;
        }
        var coordinates = displayCoordinates(item.record, coordinateCounts);
        var marker = L.marker(coordinates, markerOptions(item.record)).bindPopup(popupHtml(item.record, labels, item.distance));
        marker.addTo(markerLayer);
        markers[item.record.id] = marker;
        bounds.push(coordinates);
      });
      if (origin) {
        bounds.push([origin.latitude, origin.longitude]);
      }
      if (bounds.length) {
        map.fitBounds(bounds, { padding: [32, 32], maxZoom: 11 });
      }

      cards.querySelectorAll("[data-record-id]").forEach(function (card) {
        var activate = function (event) {
          if (event.target.closest("a")) {
            return;
          }
          focusRecord(card.getAttribute("data-record-id"));
        };
        card.addEventListener("click", activate);
        card.addEventListener("keydown", function (event) {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            activate(event);
          }
        });
      });
    }

    search.addEventListener("input", render);
    kind.addEventListener("change", render);
    nearby.addEventListener("click", function () {
      if (!navigator.geolocation) {
        status.textContent = labels.locationError;
        return;
      }
      nearby.disabled = true;
      status.textContent = labels.locating;
      navigator.geolocation.getCurrentPosition(function (position) {
        origin = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        };
        if (userLayer) {
          userLayer.remove();
        }
        userLayer = L.circleMarker([origin.latitude, origin.longitude], {
          radius: 8,
          color: "#ffffff",
          weight: 3,
          fillColor: "#2f6f5e",
          fillOpacity: 1
        }).addTo(map);
        status.textContent = "";
        nearby.disabled = false;
        nearby.classList.add("cw-finder__nearby--active");
        render();
      }, function () {
        status.textContent = labels.locationError;
        nearby.disabled = false;
      }, { enableHighAccuracy: false, timeout: 10000, maximumAge: 300000 });
    });

    render();
    window.setTimeout(function () { map.invalidateSize(); }, 0);
    container._circusFinderMap = map;
  }

  function showError(container, error) {
    var language = (document.documentElement.lang || "en").split("-")[0];
    var labels = labelsFor(language);
    var detail = error && error.message ? error.message : "Unknown error";
    container.innerHTML = '<p class="cw-finder__error">' + escapeHtml(labels.loadError) +
      '<br><small>' + escapeHtml(detail) + "</small></p>";
    if (window.console && console.error) {
      console.error(error);
    }
  }

  function init() {
    document.body.classList.toggle("circuswiki-finder-page", Boolean(document.querySelector("[data-circusfinder]")));
    document.querySelectorAll("[data-circusfinder]").forEach(function (container) {
      if (container.getAttribute("data-cw-ready") === "true") {
        if (restoreFinder(container)) {
          return;
        }
      }
      container.setAttribute("data-cw-ready", "true");
      Promise.all([
        fetch(datasetUrl(), { headers: { Accept: "application/json" } }).then(function (response) {
          if (!response.ok) {
            throw new Error("Dataset request failed (" + response.status + "): " + response.url);
          }
          return response.json();
        }),
        loadLeaflet()
      ]).then(function (values) {
        initializeFinder(container, values[0], values[1]);
      }).catch(function (error) {
        showError(container, error);
      });
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
