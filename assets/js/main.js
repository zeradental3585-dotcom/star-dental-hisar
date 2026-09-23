// Star Dental Clinic (Hisar) — shared site behaviour
(function () {
  var WHATSAPP_NUMBER = "919896695691"; // +91 98966 95691

  function buildWaLink(msg) {
    var text = encodeURIComponent(msg || "Hi Star Dental Clinic, I'd like to book an appointment.");
    return "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + text;
  }

  // Wire up every [data-wa] element with a page-aware, pre-filled WhatsApp link
  function wireWhatsAppLinks() {
    var els = document.querySelectorAll("[data-wa]");
    els.forEach(function (el) {
      var msg = el.getAttribute("data-wa-msg");
      if (!msg) {
        var page = document.body.getAttribute("data-page-label") || document.title;
        msg = "Hi Star Dental Clinic, I saw the " + page + " page and I'd like to book an appointment.";
      }
      el.setAttribute("href", buildWaLink(msg));
      el.setAttribute("target", "_blank");
      el.setAttribute("rel", "noopener");
    });
  }

  // Mobile nav toggle
  function wireNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.querySelector("nav.primary-nav");
    var scrim = document.querySelector(".nav-scrim");
    if (!toggle || !nav) return;
    function close() {
      nav.classList.remove("open");
      if (scrim) scrim.classList.remove("show");
      toggle.setAttribute("aria-expanded", "false");
    }
    function open() {
      nav.classList.add("open");
      if (scrim) scrim.classList.add("show");
      toggle.setAttribute("aria-expanded", "true");
    }
    toggle.addEventListener("click", function () {
      nav.classList.contains("open") ? close() : open();
    });
    if (scrim) scrim.addEventListener("click", close);

    // Dropdown toggling on touch/mobile
    document.querySelectorAll(".has-dropdown > a.nav-link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (window.innerWidth <= 980) {
          e.preventDefault();
          link.parentElement.classList.toggle("open");
        }
      });
    });
  }

  // FAQ accordions
  function wireFaq() {
    document.querySelectorAll(".faq-item").forEach(function (item) {
      var q = item.querySelector(".faq-q");
      if (!q) return;
      q.addEventListener("click", function () {
        var wasOpen = item.classList.contains("open");
        item.parentElement.querySelectorAll(".faq-item").forEach(function (i) {
          i.classList.remove("open");
        });
        if (!wasOpen) item.classList.add("open");
      });
    });
  }

  // Contact form -> forwards to WhatsApp with the entered details pre-filled
  function wireContactForm() {
    var form = document.querySelector("#contact-form");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.querySelector("#cf-name");
      var phone = form.querySelector("#cf-phone");
      var interest = form.querySelector("#cf-interest");
      var message = form.querySelector("#cf-message");
      var parts = [
        "Hi Star Dental Clinic, I'd like to book an appointment.",
        name && name.value ? "Name: " + name.value : "",
        phone && phone.value ? "Phone: " + phone.value : "",
        interest && interest.value ? "Interested in: " + interest.value : "",
        message && message.value ? "Message: " + message.value : "",
      ].filter(Boolean);
      window.open(buildWaLink(parts.join("\n")), "_blank", "noopener");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wireWhatsAppLinks();
    wireNav();
    wireFaq();
    wireContactForm();
  });
})();
