# -*- coding: utf-8 -*-
"""Shared templates & helpers for the Star Dental Clinic (Hisar) static site."""
import json, os

SITE_NAME = "Star Dental Clinic"
SITE_TAGLINE = "Dr. Tarun's Star Dental Clinic — Hisar"
DOMAIN = "https://stardentalhisar.zeradental.in"
PHONE_DISPLAY = "+91 98966 95691"
PHONE_TEL = "+919896695691"
WA_NUMBER = "919896695691"
ADDRESS_LINE1 = "DSS 37, Fawara Chowk, Near Khalsa Petrol Pump"
ADDRESS_LINE2 = "Old Courts Commercial Complex, Lajpat Nagar"
ADDRESS_CITY = "Hisar, Haryana 125001"
ADDRESS_FULL = f"{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_CITY}"
MAP_EMBED_SRC = "https://www.google.com/maps?q=Star+Dental+Clinic+DSS+37+Fawara+Chowk+Lajpat+Nagar+Hisar&output=embed"
GBP_URL = "https://share.google/FkqVolaQCX1WWk0ns"
# Verified directly from the clinic's Google Business Profile (screenshot supplied by the
# client, 23 Sep 2026: "Dr. Tarun's Star Dental Clinic", 4.9 stars, 546 Google reviews).
GBP_RATING = "4.9"
GBP_REVIEW_COUNT = 546
OUT_DIR = os.path.join(os.path.dirname(__file__))

NAV_ITEMS = [
    {"label": "Home", "href": "index.html"},
    {"label": "Implants", "href": "dental-implants-hisar.html"},
    {"label": "Aligners", "href": "clear-aligners-hisar.html"},
    {
        "label": "Services",
        "href": "services.html",
        "children": [
            ("services.html", "All Services"),
            ("root-canal-treatment.html", "Root Canal Treatment"),
            ("full-mouth-rehabilitation.html", "Full Mouth Rehabilitation"),
            ("smile-design-cosmetic-dentistry.html", "Smile Design & Cosmetic"),
            ("orthodontics-braces.html", "Orthodontics & Braces"),
            ("crowns-bridges.html", "Crowns & Bridges"),
            ("kids-dentistry.html", "Kids Dentistry"),
            ("patient-education.html", "Patient Education Hub"),
        ],
    },
    {"label": "About", "href": "about-doctors.html"},
    {"label": "Gallery", "href": "gallery.html"},
    {"label": "Reviews", "href": "reviews.html"},
    {"label": "Contact", "href": "contact.html"},
]

FOOTER_SERVICE_LINKS = [
    ("dental-implants-hisar.html", "Dental Implants"),
    ("clear-aligners-hisar.html", "Clear Aligners / Invisalign"),
    ("root-canal-treatment.html", "Root Canal Treatment"),
    ("full-mouth-rehabilitation.html", "Full Mouth Rehabilitation"),
    ("smile-design-cosmetic-dentistry.html", "Smile Design & Cosmetic"),
    ("orthodontics-braces.html", "Orthodontics & Braces"),
    ("crowns-bridges.html", "Crowns & Bridges"),
    ("kids-dentistry.html", "Kids Dentistry"),
]

FOOTER_LINKS = [
    ("about-doctors.html", "About & Doctors"),
    ("gallery.html", "Gallery"),
    ("patient-education.html", "Patient Education"),
    ("reviews.html", "Patient Reviews"),
    ("contact.html", "Contact & Directions"),
]

ICONS = {
    "check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17l-5-5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "star": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 21 12 17.77 5.82 21 7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>',
    "phone": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "pin": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 1 1 18 0z" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="10" r="3" stroke="currentColor" stroke-width="2"/></svg>',
    "clock": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "wa": '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.28-.14-1.67-.82-1.93-.92-.26-.1-.45-.14-.64.14-.19.28-.74.92-.9 1.1-.17.19-.33.21-.61.07-.28-.14-1.18-.44-2.25-1.4-.83-.74-1.39-1.66-1.56-1.94-.16-.28-.02-.43.12-.57.13-.13.28-.33.42-.5.14-.16.19-.28.28-.47.09-.19.05-.35-.02-.5-.07-.14-.64-1.55-.88-2.12-.23-.56-.46-.48-.64-.49h-.55c-.19 0-.5.07-.76.35s-1 .98-1 2.4 1.02 2.78 1.16 2.97c.14.19 2 3.07 4.86 4.3.68.29 1.21.47 1.62.6.68.22 1.3.19 1.79.11.55-.08 1.67-.68 1.9-1.34.24-.65.24-1.21.17-1.33-.07-.12-.26-.19-.54-.33z"/><path d="M12 2a10 10 0 0 0-8.55 15.14L2 22l4.99-1.42A10 10 0 1 0 12 2zm0 18.2a8.17 8.17 0 0 1-4.17-1.14l-.3-.18-3.1.88.83-3-.2-.31A8.2 8.2 0 1 1 12 20.2z"/></svg>',
    "implant": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M7.5 4.2c0 2.9 1.9 4.6 4.5 4.6s4.5-1.7 4.5-4.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 8.8v2.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 11.4l-2.35 8.9a1 1 0 0 0 1.72.9L12 20l.63 1.2a1 1 0 0 0 1.72-.9L12 11.4z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.4 13.6h5.2M9.9 16.3h4.2M10.4 18.9h3.2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>',
    "google": '<svg width="16" height="16" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.9 29.3 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.1 8 3l5.7-5.7C34.6 6.1 29.6 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.7-.4-3.5z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.6 15.9 18.9 13 24 13c3.1 0 5.8 1.1 8 3l5.7-5.7C34.6 6.1 29.6 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.5 0 10.4-1.8 14.2-5l-6.6-5.4C29.5 35.4 26.9 36 24 36c-5.3 0-9.7-3.1-11.3-7.6l-6.5 5C9.6 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.3-2.3 4.2-4.2 5.6l6.6 5.4C40.9 36.6 44 30.9 44 24c0-1.3-.1-2.7-.4-3.5z"/></svg>',
}

# Real patient reviews, sourced directly from the clinic's Google Business Profile
# ("Dr. Tarun's Star Dental Clinic", https://share.google/FkqVolaQCX1WWk0ns), filtered
# using Google's own "dental implant" / "clear aligners" / "invisalign treatment" review
# tags so only feedback specifically about those two services is ever shown here — kept
# deliberately narrow to protect the implant & aligner specialist positioning. Quotes are
# verbatim (only trimmed of the reviewer's own trailing "... More" where Google truncates
# on the listing itself); nothing is invented. None of these reviewers has a personal
# photo on their Google profile — Google itself shows a plain colour-initial avatar for
# each of them — so the site mirrors that exactly rather than sourcing or fabricating a
# headshot for someone who never uploaded one.
REVIEWS = [
    {
        "id": "kulwinderjit",
        "name": "Kulwinderjit Singh",
        "initial": "K",
        "color": "#3b5b80",
        "stars": 5,
        "time_ago": "3 months ago",
        "review_count": "3 reviews",
        "topic": "implant",
        "tag": "Dental Implant",
        "quote": "I am from Fatehabad and was scheduled for dental implant surgery in Delhi. My friend suggested Hisar. I found Dr Tarun on Google. After a preliminary consultation, decided to go with him. I am giving this review after 48 hours of the implant being done, and am happy and satisfied. Recommended \U0001F44D",
    },
    {
        "id": "wahid",
        "name": "Md Wahid Reza",
        "initial": "M",
        "color": "#6b4ea3",
        "stars": 5,
        "time_ago": "7 months ago",
        "review_count": "1 review",
        "topic": "implant",
        "tag": "Dental Implant",
        "quote": "I took my father to Dr Tarun for Implants. He explained the process very patiently and cleared all our doubts. Later we went ahead with surgery. He underwent full mouth implants and got fixed permanent teeth in just 5 sittings. He is very happy, eats everything, even nuts. Dr Tarun is extremely humble and a skilled surgeon. It's one of the best dental implant centres in Hisar, even in Haryana.",
    },
    {
        "id": "shakti",
        "name": "Shakti Dhankar",
        "initial": "S",
        "color": "#c1573b",
        "stars": 5,
        "time_ago": "3 months ago",
        "review_count": "1 review",
        "topic": "implant",
        "tag": "Dental Implant",
        "quote": "Best dental implant centre in Hisar. I can feel natural teeth. Best services for dental treatment in Hisar.",
    },
    {
        "id": "ajaib",
        "name": "Ajaib Singh",
        "initial": "A",
        "color": "#1f7a6c",
        "stars": 5,
        "time_ago": "8 months ago",
        "review_count": "1 review",
        "topic": "implant",
        "tag": "Dental Implant",
        "quote": "Highly satisfied with the dental implant — I can eat everything. Best dental implant surgeon.",
    },
    {
        "id": "haan",
        "name": "Haan Babbe",
        "initial": "H",
        "color": "#a3823f",
        "stars": 5,
        "time_ago": "1 year ago",
        "review_count": "1 review",
        "topic": "aligner",
        "tag": "Clear Aligner",
        "quote": "The experience of “clear aligner” treatment with them was very positive. Everything went smoothly. Above all, the process was quicker than I thought. The staff's friendliness enhances the overall atmosphere. Highly recommended for orthodontic services in Hisar.",
    },
    {
        "id": "badri",
        "name": "Badri Parsad",
        "initial": "B",
        "color": "#3b5b80",
        "stars": 5,
        "time_ago": "2 years ago",
        "review_count": "1 review",
        "topic": "aligner",
        "tag": "Invisalign Treatment",
        "quote": "Highly satisfied with clear invisalign treatment, and my mom got a dental implant-supported fixed denture. Perfect dental services in Hisar... thanks Dr Tarun and all team.",
    },
]


def review_card(r):
    stars = ICONS["star"] * r["stars"]
    return f"""
<div class="testi-card review-card">
  <div class="stars">{stars}</div>
  <p class="review-quote">&ldquo;{r['quote']}&rdquo;</p>
  <div class="review-foot">
    <span class="review-avatar" style="background:{r['color']}">{r['initial']}</span>
    <div>
      <div class="testi-name">{r['name']}</div>
      <div class="testi-role">{r['review_count']} &middot; {r['time_ago']}</div>
    </div>
    <span class="review-google-badge" title="Posted on Google">{ICONS['google']}</span>
  </div>
  <span class="tag review-topic-tag">{r['tag']}</span>
</div>""".strip("\n")


def reviews_grid(topic=None, ids=None, cols=3):
    if ids:
        chosen = [r for r in REVIEWS if r["id"] in ids]
    elif topic:
        chosen = [r for r in REVIEWS if r["topic"] == topic]
    else:
        chosen = REVIEWS
    cards = "".join(review_card(r) for r in chosen)
    return f'<div class="grid grid-{cols}" style="margin-top:28px">{cards}</div>'


def reviews_schema(topic=None, ids=None):
    if ids:
        chosen = [r for r in REVIEWS if r["id"] in ids]
    elif topic:
        chosen = [r for r in REVIEWS if r["topic"] == topic]
    else:
        chosen = REVIEWS
    return [
        {
            "@context": "https://schema.org",
            "@type": "Review",
            "itemReviewed": {"@type": "Dentist", "name": SITE_NAME},
            "author": {"@type": "Person", "name": r["name"]},
            "reviewRating": {"@type": "Rating", "ratingValue": str(r["stars"]), "bestRating": "5"},
            "reviewBody": r["quote"],
            "publisher": {"@type": "Organization", "name": "Google"},
        }
        for r in chosen
    ]

# A large, faint decorative line-art motif used only as hero background texture
# (never a UI icon) — evokes a tooth/implant silhouette without needing real
# clinical photography. Purely decorative: aria-hidden, no semantic meaning.
IMPLANT_MOTIF_SVG = '''<svg class="hero-motif" width="520" height="520" viewBox="0 0 100 100" fill="none" aria-hidden="true" focusable="false">
  <path d="M50 6C32 6 19 18 21 34c1 8 6 12 5 20-1 9 6 12 11 6 3-4 4-7 4-11v-1c0 4 1 7 4 11 5 6 12 3 11-6-1-8 4-12 5-20C81 18 68 6 50 6Z" stroke="var(--gold)" stroke-width="0.6" opacity="0.5"/>
  <path d="M38 34h24M40 44h20M42 54h16" stroke="var(--gold)" stroke-width="0.5" opacity="0.35"/>
</svg>'''


def esc(s):
    return s


def render_nav_children(children):
    return "".join(f'<a href="{href}">{label}</a>' for href, label in children)


def render_nav(active_href):
    items_html = []
    for item in NAV_ITEMS:
        active = " active" if item["href"] == active_href else ""
        if "children" in item:
            child_active = any(c[0] == active_href for c in item["children"])
            open_cls = " open" if child_active else ""
            items_html.append(
                f'<li class="has-dropdown{open_cls}">'
                f'<a class="nav-link{active}" href="{item["href"]}">{item["label"]}</a>'
                f'<div class="dropdown">{render_nav_children(item["children"])}</div>'
                f"</li>"
            )
        else:
            items_html.append(f'<li><a class="nav-link{active}" href="{item["href"]}">{item["label"]}</a></li>')
    return "".join(items_html)


def header_html(active_href, page_label):
    nav_items = render_nav(active_href)
    return f"""
<div class="topbar">
  <div class="container">
    <div class="tb-left">
      <span>{ICONS['pin']} {ADDRESS_CITY}</span>
      <span>{ICONS['clock']} Mon–Sat, 10:00 AM – 8:00 PM</span>
    </div>
    <div class="tb-right">
      <a href="tel:{PHONE_TEL}">{ICONS['phone']} {PHONE_DISPLAY}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="container nav-wrap">
    <a href="index.html" class="brand">
      <span class="mark">{ICONS['star']}</span>
      <span>{SITE_NAME}<small>Implant &amp; Aligner Centre, Hisar</small></span>
    </a>
    <nav class="primary-nav" aria-label="Primary">
      <ul>{nav_items}</ul>
    </nav>
    <div class="header-cta">
      <a class="btn btn-call btn-sm" href="tel:{PHONE_TEL}">{ICONS['phone']} <span class="txt">Call Now</span></a>
      <a class="btn btn-wa btn-sm" data-wa href="#">{ICONS['wa']} <span class="txt">WhatsApp</span></a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="nav-scrim"></div>
</header>
""".strip("\n")


def footer_html():
    service_links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in FOOTER_SERVICE_LINKS)
    page_links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in FOOTER_LINKS)
    year = 2026
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="grid grid-4">
      <div>
        <div class="f-brand"><span class="mark" style="width:34px;height:34px;border-radius:8px;background:var(--gold);color:var(--navy-dark);display:inline-flex;align-items:center;justify-content:center;">{ICONS['star']}</span> {SITE_NAME}</div>
        <p>Premier ISO-certified dental clinic in Hisar led by Dr. Tarun Kalra (MDS) and Dr. Shweta Kalra — advanced implants, invisible aligners, single-sitting RCT and complete family dental care.</p>
        <a class="btn btn-wa btn-sm" data-wa href="#">{ICONS['wa']} Chat on WhatsApp</a>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{service_links}</ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>{page_links}</ul>
      </div>
      <div>
        <h4>Visit the Clinic</h4>
        <ul>
          <li>{ICONS['pin']} {ADDRESS_FULL}</li>
          <li>{ICONS['phone']} <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li>{ICONS['clock']} Mon–Sat, 10:00 AM – 8:00 PM</li>
          <li><a href="{GBP_URL}" target="_blank" rel="noopener">View on Google Maps →</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {year} Star Dental Clinic, Hisar. All rights reserved.</span>
      <span>Website by <a href="https://zeradental.in" target="_blank" rel="noopener">Zera Dental</a> — a Zera Technologies company</span>
    </div>
  </div>
</footer>
""".strip("\n")


def schema_scripts(extra_schemas=None):
    dentist_schema = {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "name": SITE_NAME,
        "image": f"{DOMAIN}/assets/img/full/clinic-exterior.jpg",
        "url": DOMAIN,
        "telephone": PHONE_TEL,
        "priceRange": "₹₹",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": f"{ADDRESS_LINE1}, {ADDRESS_LINE2}",
            "addressLocality": "Hisar",
            "addressRegion": "Haryana",
            "postalCode": "125001",
            "addressCountry": "IN",
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "10:00",
                "closes": "20:00",
            }
        ],
        "medicalSpecialty": ["Dentistry", "Endodontics", "Orthodontics", "Cosmetic Dentistry"],
        "founder": [
            {"@type": "Physician", "name": "Dr. Tarun Kalra"},
            {"@type": "Physician", "name": "Dr. Shweta Kalra"},
        ],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": GBP_RATING,
            "reviewCount": str(GBP_REVIEW_COUNT),
            "bestRating": "5",
        },
    }
    scripts = [f'<script type="application/ld+json">{json.dumps(dentist_schema, ensure_ascii=False)}</script>']
    for s in (extra_schemas or []):
        scripts.append(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>')
    return "\n".join(scripts)


def faq_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": f"{DOMAIN}/{href}" if href else DOMAIN}
            for i, (name, href) in enumerate(items)
        ],
    }


def page_shell(*, active_href, title, meta_description, page_label, body_html, extra_schemas=None, canonical=None, og_image=None):
    canonical_url = canonical or f"{DOMAIN}/{active_href}"
    og_img = og_image or f"{DOMAIN}/assets/img/og-cover.jpg"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_description}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{schema_scripts(extra_schemas)}
</head>
<body data-page-label="{page_label}">
{header_html(active_href, page_label)}
{body_html}
{footer_html()}
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def eyebrow(text):
    return f'<div class="eyebrow"><span class="eyebrow-rule"></span>{text}</div>'


def section(inner, cls=""):
    return f'<section class="section {cls}"><div class="container">{inner}</div></section>'


def cta_band(heading, sub, wa_msg=None):
    wa_attr = f' data-wa data-wa-msg="{wa_msg}"' if wa_msg else " data-wa"
    return f"""
<div class="cta-band">
  <h2>{heading}</h2>
  <p>{sub}</p>
  <div class="cta-row">
    <a class="btn btn-gold" {wa_attr} href="#">{ICONS['wa']} Chat on WhatsApp</a>
    <a class="btn btn-call" href="tel:{PHONE_TEL}">{ICONS['phone']} Call {PHONE_DISPLAY}</a>
  </div>
</div>
""".strip("\n")


def faq_block(items):
    rows = []
    for q, a in items:
        rows.append(f"""
<div class="faq-item">
  <button class="faq-q">{q} <span class="plus">+</span></button>
  <div class="faq-a"><p>{a}</p></div>
</div>""".strip("\n"))
    return f'<div class="faq-list">{"".join(rows)}</div>'


def breadcrumbs_html(items):
    parts = []
    for i, (name, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{href}">{name}</a>')
        else:
            parts.append(name)
    return f'<div class="breadcrumbs">{" &rsaquo; ".join(parts)}</div>'


def write_page(filename, html):
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html), "bytes")
