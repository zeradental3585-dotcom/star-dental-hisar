# -*- coding: utf-8 -*-
"""Generates the full Star Dental Clinic (Hisar) static site."""
from build_common import *

IMG = "assets/img/full/"
THUMB = "assets/img/thumb/"

# ---------------------------------------------------------------- HOME ----

def page_home():
    active = "index.html"
    hero = f"""
<section class="hero">
  <div class="container">
    <div>
      {eyebrow("Hisar's Advanced Implant &amp; Aligner Centre")}
      <h1>Get Your Smile Fixed by Hisar's MDS-Qualified Dental Specialists</h1>
      <p class="lede">Dr. Tarun's Star Dental Clinic is a premier ISO-certified practice at Fawara Chowk, Hisar — led by an MDS specialist couple offering single-sitting root canals, dental implants, invisible aligners and complete family dental care.</p>
      <div class="trust-pills">
        <a class="trust-pill" href="{GBP_URL}" target="_blank" rel="noopener">{ICONS['star']} {GBP_RATING}★ · {GBP_REVIEW_COUNT} Google Reviews</a>
        <span class="trust-pill">{ICONS['check']} ISO-Certified Clinic</span>
        <span class="trust-pill">{ICONS['check']} MDS Specialist (PGIMS, Rohtak)</span>
        <span class="trust-pill">{ICONS['check']} 14+ Years Experience</span>
        <span class="trust-pill">{ICONS['check']} Advanced Implant Centre</span>
      </div>
      <div class="cta-row">
        <a class="btn btn-wa" data-wa data-wa-msg="Hi Star Dental Clinic, I'd like to book a consultation." href="#">{ICONS['wa']} Book on WhatsApp</a>
        <a class="btn btn-outline-light" href="tel:{PHONE_TEL}">{ICONS['phone']} Call {PHONE_DISPLAY}</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="{IMG}both-doctors-standing.jpg" alt="Dr. Tarun Kalra and Dr. Shweta Kalra, Star Dental Clinic Hisar" loading="eager">
      <div class="hero-badge">
        <strong>14+ Yrs</strong>
        <span>Clinical experience treating families across Hisar</span>
      </div>
    </div>
  </div>
</section>
""".strip("\n")

    badges = f"""
<div class="badge-row center" style="justify-content:center">
  <span class="badge">{ICONS['check']} Premier ISO Certified Clinic</span>
  <span class="badge">{ICONS['check']} Advanced RCT &amp; Implant Centre</span>
  <span class="badge">{ICONS['check']} Complete Family Dental Care</span>
  <span class="badge">{ICONS['check']} ₹200 Consultation</span>
</div>
""".strip("\n")

    why = f"""
{eyebrow("Why Hisar Chooses Us")}
<h2>A specialist husband–wife team, under one roof</h2>
<p class="lede">Most dental clinics in Hisar are run by a single general dentist. Star Dental Clinic is different — you get an MDS-qualified specialist for root canals and implants, and a dedicated cosmetic dentist for smile design and aligners, both practicing from the same ISO-certified clinic.</p>
<div class="grid grid-2" style="margin-top:28px">
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Single-sitting RCT</strong> — most root canal treatments completed in one visit, no repeated appointments.</span></li>
    <li>{ICONS['check']} <span><strong>Advanced implant &amp; aligner centre</strong> — tooth replacement and invisible teeth-straightening under specialist supervision.</span></li>
    <li>{ICONS['check']} <span><strong>ISO-certified sterilisation &amp; protocols</strong> — the same safety standard you'd expect at a hospital-grade facility.</span></li>
  </ul>
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Family-run practice</strong> — Dr. Tarun Kalra (MDS, Endodontics) and Dr. Shweta Kalra (Cosmetic Dentistry) see patients together.</span></li>
    <li>{ICONS['check']} <span><strong>Central Hisar location</strong> — at Fawara Chowk, Old Courts Commercial Complex, Lajpat Nagar — easy to reach from anywhere in the city.</span></li>
    <li>{ICONS['check']} <span><strong>Transparent pricing</strong> — a ₹200 consultation gets you a clear, written treatment plan with no hidden charges.</span></li>
  </ul>
</div>
""".strip("\n")

    services = [
        ("dental-implants-hisar.html", "Dental Implants", "Fixed, permanent tooth replacement that looks, feels and functions like your natural teeth."),
        ("clear-aligners-hisar.html", "Clear Aligners", "Straighten your teeth invisibly — no metal wires, removable, virtually undetectable."),
        ("full-mouth-rehabilitation.html", "Full Mouth Rehabilitation", "A complete plan to restore function and appearance when multiple teeth need attention."),
        ("root-canal-treatment.html", "Root Canal Treatment", "Single-sitting RCT by an MDS Endodontist — save the tooth, stop the pain, in one visit."),
        ("smile-design-cosmetic-dentistry.html", "Smile Design &amp; Cosmetic", "Veneers, whitening and bonding to redesign your smile with natural-looking results."),
        ("orthodontics-braces.html", "Orthodontics &amp; Braces", "Traditional braces and modern alignment options for children, teens and adults."),
        ("crowns-bridges.html", "Crowns &amp; Bridges", "Durable, custom-shaded restorations to repair damaged or missing teeth."),
        ("kids-dentistry.html", "Kids Dentistry", "Gentle, patient-friendly dental care that keeps young smiles healthy from the start."),
    ]
    service_cards = "".join(
        f"""<a class="card service-card" href="{href}">
  <div class="card-icon">{ICONS['star']}</div>
  <h3>{title}</h3>
  <p>{desc}</p>
  <span class="card-link">Learn more →</span>
</a>""" for href, title, desc in services
    )
    services_section = f"""
{eyebrow("Our Services")}
<h2>Every stage of your dental care, in one clinic</h2>
<p class="lede">From a single filling to a full-mouth implant plan — explore what Star Dental Clinic treats, and what to expect at each step.</p>
<div class="grid grid-4" style="margin-top:28px">{service_cards}</div>
""".strip("\n")

    doctors = f"""
{eyebrow("Meet Your Doctors")}
<h2>The specialists behind every treatment plan</h2>
<div class="grid grid-2" style="margin-top:28px">
  <div class="doctor-card">
    <img src="{IMG}dr-tarun-portrait.jpg" alt="Dr. Tarun Kalra, MDS, Star Dental Clinic Hisar">
    <div>
      <div class="doctor-name">Dr. Tarun Kalra</div>
      <div class="doctor-title">BDS, MDS (PGIMS, Rohtak) — Endodontics &amp; Implants</div>
      <ul class="cred-list">
        <li>{ICONS['check']} 14+ years of clinical practice in Hisar</li>
        <li>{ICONS['check']} Specialist in single-sitting root canal treatment</li>
        <li>{ICONS['check']} Focus on dental implants &amp; advanced restorative care</li>
      </ul>
      <a class="btn btn-call btn-sm" href="about-doctors.html">Full profile →</a>
    </div>
  </div>
  <div class="doctor-card">
    <img src="{IMG}dr-shweta-portrait.jpg" alt="Dr. Shweta Kalra, Cosmetic Dentist, Star Dental Clinic Hisar">
    <div>
      <div class="doctor-name">Dr. Shweta Kalra</div>
      <div class="doctor-title">BDS, MIDA — Cosmetic Dentistry</div>
      <ul class="cred-list">
        <li>{ICONS['check']} 9+ years treating patients in Hisar</li>
        <li>{ICONS['check']} Focus on smile design, aligners &amp; cosmetic dentistry</li>
        <li>{ICONS['check']} Gentle approach with children &amp; first-time patients</li>
      </ul>
      <a class="btn btn-call btn-sm" href="about-doctors.html">Full profile →</a>
    </div>
  </div>
</div>
""".strip("\n")

    photos = f"""
{eyebrow("Inside The Clinic")}
<h2>A modern, ISO-certified clinic at Fawara Chowk</h2>
<div class="photo-strip" style="margin-top:24px">
  <span class="ph-frame"><img src="{THUMB}clinic-exterior.jpg" alt="Star Dental Clinic exterior, Fawara Chowk, Hisar"></span>
  <span class="ph-frame"><img src="{THUMB}dr-tarun-reception.jpg" alt="Reception at Star Dental Clinic, Hisar"></span>
  <span class="ph-frame"><img src="{THUMB}both-doctors-two-chairs.jpg" alt="Treatment chairs at Star Dental Clinic, Hisar"></span>
  <span class="ph-frame"><img src="{THUMB}dr-shweta-treating-patient.jpg" alt="Dr. Shweta Kalra treating a patient at Star Dental Clinic, Hisar"></span>
</div>
<div class="center" style="margin-top:24px"><a class="btn btn-call" href="gallery.html">View Full Gallery →</a></div>
""".strip("\n")

    steps = f"""
{eyebrow("How It Works")}
<h2>From first message to a finished smile</h2>
<div class="steps" style="margin-top:28px">
  <div class="step"><h3>Message or Call</h3><p>Send us your concern on WhatsApp or call the clinic — we'll suggest the right doctor and a convenient slot.</p></div>
  <div class="step"><h3>₹200 Consultation</h3><p>An in-person exam and X-rays (if needed) so Dr. Tarun or Dr. Shweta can see exactly what's going on.</p></div>
  <div class="step"><h3>Clear Treatment Plan</h3><p>You get a written plan and transparent quote before any treatment begins — no surprises.</p></div>
  <div class="step"><h3>Treatment &amp; Aftercare</h3><p>Most procedures — including RCT — are completed in a single sitting, with follow-up guidance included.</p></div>
</div>
""".strip("\n")

    location = f"""
{eyebrow("Serving Hisar &amp; Beyond")}
<h2>Conveniently located for patients across the district</h2>
<p class="lede">Star Dental Clinic sits at Fawara Chowk in Lajpat Nagar, Hisar's central commercial hub — an easy reach from every part of the city, and a short drive for patients from nearby towns seeking specialist implant and aligner care.</p>
<div class="ring-tags" style="margin-top:18px">
  <span class="tag">Model Town</span><span class="tag">Urban Estate</span><span class="tag">Civil Lines</span>
  <span class="tag">Railway Road</span><span class="tag">Azad Nagar</span><span class="tag">Sector 13–16</span>
  <span class="tag">Hansi</span><span class="tag">Barwala</span><span class="tag">Adampur</span>
  <span class="tag">Narnaund</span><span class="tag">Uklana</span><span class="tag">Agroha</span>
</div>
""".strip("\n")

    faqs = [
        ("Where is Star Dental Clinic located?", f"We're at {ADDRESS_FULL}, right at Fawara Chowk near Khalsa Petrol Pump — one of the most central and easy-to-find locations in Hisar."),
        ("Do I need an appointment, or can I walk in?", "Booking ahead on WhatsApp or by phone is recommended so we can plan the right time slot with the right doctor, but walk-ins are welcome during clinic hours."),
        ("What are your clinic timings?", "We're open Monday to Saturday, 10:00 AM to 8:00 PM."),
        ("Do you treat children?", "Yes — Dr. Shweta Kalra and Dr. Tarun Kalra both see young patients, from routine check-ups to more involved kids' dentistry."),
        ("How much does a consultation cost?", "An initial consultation is ₹200, which includes a clinical examination and a clear discussion of your treatment options."),
    ]
    faq_section = f"""
{eyebrow("Frequently Asked Questions")}
<h2>Common questions from our patients</h2>
<div style="margin-top:20px">{faq_block(faqs)}</div>
""".strip("\n")

    body = "\n".join([
        hero,
        section(badges, "section-tight"),
        section(why),
        section(services_section, "section-alt"),
        section(doctors),
        section(photos, "section-alt"),
        section(steps),
        section(location, "section-alt"),
        section(faq_section),
        section(cta_band(
            "Ready to fix your smile?",
            "Message us on WhatsApp with your concern — Dr. Tarun or Dr. Shweta will personally guide you on the next step.",
        )),
    ])

    write_page("index.html", page_shell(
        active_href=active,
        title="Star Dental Clinic Hisar | Dental Implants, Aligners & Root Canal | Dr. Tarun Kalra",
        meta_description="ISO-certified dental clinic in Hisar at Fawara Chowk. MDS specialist Dr. Tarun Kalra & Dr. Shweta Kalra offer dental implants, invisible aligners, single-sitting RCT & family dental care. Book on WhatsApp.",
        page_label="Home",
        body_html=body,
        extra_schemas=[faq_schema(faqs)],
    ))


# ------------------------------------------------------------ IMPLANTS ----

def page_implants():
    active = "dental-implants-hisar.html"
    hero = f"""
<section class="hero">
  <div class="container">
    <div>
      {eyebrow("Dental Implants in Hisar")}
      <h1>Fixed, Permanent Tooth Replacement — Dental Implants in Hisar</h1>
      <p class="lede">Missing teeth affect how you eat, speak and smile. Dental implants replace the tooth root itself, giving you a fixed replacement that looks, feels and functions like a natural tooth — placed under Dr. Tarun Kalra's specialist care.</p>
      <div class="cta-row">
        <a class="btn btn-wa" data-wa data-wa-msg="Hi, I want to know more about dental implants at Star Dental Clinic." href="#">{ICONS['wa']} Ask About Implants</a>
        <a class="btn btn-outline-light" href="tel:{PHONE_TEL}">{ICONS['phone']} Call {PHONE_DISPLAY}</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="{IMG}dr-tarun-elderly-patient.jpg" alt="Dr. Tarun Kalra examining a patient for dental implants at Star Dental Clinic Hisar">
    </div>
  </div>
</section>
""".strip("\n")

    price = f"""
<div class="price-band">
  <div>
    <div class="eyebrow" style="margin-bottom:4px">Transparent Pricing</div>
    <div class="amount">Personalised implant quote</div>
    <div class="note">Implant cost depends on the number of teeth, bone condition and the implant system used.</div>
  </div>
  <a class="btn btn-wa" data-wa data-wa-msg="Hi, I'd like a personalised quote for dental implants." href="#">{ICONS['wa']} Get My Quote on WhatsApp</a>
</div>
<p class="price-disclaimer">Every case is different — during your ₹200 consultation, Dr. Tarun Kalra will examine your X-rays and give you a clear, written quote with no hidden charges before any treatment begins.</p>
""".strip("\n")

    why_implants = f"""
{eyebrow("Why Choose An Implant")}
<h2>The only tooth replacement that replaces the root, too</h2>
<div class="grid grid-2" style="margin-top:24px;align-items:start">
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Looks &amp; feels natural</strong> — custom-matched to your bite and smile.</span></li>
    <li>{ICONS['check']} <span><strong>Protects surrounding teeth</strong> — unlike a bridge, no need to cut down healthy neighbouring teeth.</span></li>
    <li>{ICONS['check']} <span><strong>Preserves your jawbone</strong> — stimulates bone the way a natural tooth root does, preventing the bone loss that follows tooth loss.</span></li>
  </ul>
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Built to last</strong> — with good care, implants are designed as a long-term, permanent solution.</span></li>
    <li>{ICONS['check']} <span><strong>Eat what you like</strong> — a fixed implant restores full chewing function, unlike a removable denture.</span></li>
    <li>{ICONS['check']} <span><strong>Single tooth or full mouth</strong> — from one missing tooth to a complete implant-supported rehabilitation.</span></li>
  </ul>
</div>
""".strip("\n")

    process = f"""
{eyebrow("The Implant Process")}
<h2>What to expect, start to finish</h2>
<div class="steps" style="margin-top:28px">
  <div class="step"><h3>Consultation &amp; Scan</h3><p>Clinical exam and X-rays to assess bone density and plan the ideal implant position.</p></div>
  <div class="step"><h3>Treatment Plan</h3><p>A written plan covering the number of implants needed, timeline and full cost — before you commit.</p></div>
  <div class="step"><h3>Implant Placement</h3><p>The titanium implant is placed under local anaesthesia in a comfortable, ISO-certified setting.</p></div>
  <div class="step"><h3>Healing &amp; Crown</h3><p>After a healing period, a custom crown is fitted — completing a tooth that looks and functions naturally.</p></div>
</div>
""".strip("\n")

    candidates = f"""
{eyebrow("Who Are Implants For")}
<h2>Common situations we treat with implants</h2>
<div class="grid grid-3" style="margin-top:24px">
  <div class="card"><div class="card-icon">{ICONS['star']}</div><h3>Single missing tooth</h3><p>Replace one tooth without touching the teeth next to it.</p></div>
  <div class="card"><div class="card-icon">{ICONS['star']}</div><h3>Multiple missing teeth</h3><p>Implant-supported bridges to restore several teeth at once.</p></div>
  <div class="card"><div class="card-icon">{ICONS['star']}</div><h3>Full-mouth restoration</h3><p>A complete implant-supported solution for patients missing most or all of their teeth — see our <a href="full-mouth-rehabilitation.html">Full Mouth Rehabilitation</a> page.</p></div>
</div>
""".strip("\n")

    faqs = [
        ("Does getting a dental implant hurt?", "The procedure is done under local anaesthesia, so you shouldn't feel pain during placement. Some mild soreness for a few days afterward is normal and manageable with standard medication."),
        ("How long does an implant take to heal?", "Healing time varies by patient and bone quality, typically a few months before the final crown is fitted — Dr. Tarun will give you a timeline specific to your case at your consultation."),
        ("Am I a candidate for implants if I've had missing teeth for years?", "In most cases, yes — though long-term tooth loss can affect bone volume. An X-ray during your consultation will confirm whether any additional preparation is needed."),
        ("How is the cost of an implant decided?", "Cost depends on the number of implants, the system used and whether any additional procedures (like bone grafting) are needed. You'll get a full written quote before starting treatment."),
        ("Do you offer implants for a full arch or full mouth?", "Yes — Dr. Tarun Kalra plans full-mouth implant rehabilitation for patients missing most or all of their teeth in an arch."),
    ]
    faq_section = f"""
{eyebrow("Implant FAQs")}
<h2>Questions patients ask before getting an implant</h2>
<div style="margin-top:20px">{faq_block(faqs)}</div>
""".strip("\n")

    body = "\n".join([
        hero,
        section(price, "section-tight"),
        section(why_implants),
        section(process, "section-alt"),
        section(candidates),
        section(faq_section, "section-alt"),
        section(cta_band(
            "Get a personalised implant quote",
            "Send Dr. Tarun a quick WhatsApp message with your concern — he'll tell you exactly what to expect at your consultation.",
            wa_msg="Hi, I'd like to book an implant consultation at Star Dental Clinic.",
        )),
    ])

    write_page("dental-implants-hisar.html", page_shell(
        active_href=active,
        title="Dental Implants in Hisar | Star Dental Clinic — Dr. Tarun Kalra",
        meta_description="Get permanent, natural-looking dental implants in Hisar from MDS specialist Dr. Tarun Kalra at Star Dental Clinic, Fawara Chowk. Single tooth to full-mouth implants. Book a consultation.",
        page_label="Dental Implants",
        body_html=body,
        extra_schemas=[faq_schema(faqs), breadcrumb_schema([("Home", ""), ("Dental Implants", active)])],
    ))


# ------------------------------------------------------------- ALIGNERS ----

def page_aligners():
    active = "clear-aligners-hisar.html"
    hero = f"""
<section class="hero">
  <div class="container">
    <div>
      {eyebrow("Clear Aligners in Hisar")}
      <h1>Straighten Your Teeth Invisibly — Clear Aligners in Hisar</h1>
      <p class="lede">Clear aligners let you fix crowding, gaps and bite issues without metal braces — removable, virtually invisible, and planned around your life. Dr. Shweta Kalra designs every aligner treatment personally.</p>
      <div class="cta-row">
        <a class="btn btn-wa" data-wa data-wa-msg="Hi, I want to know more about clear aligners at Star Dental Clinic." href="#">{ICONS['wa']} Ask About Aligners</a>
        <a class="btn btn-outline-light" href="tel:{PHONE_TEL}">{ICONS['phone']} Call {PHONE_DISPLAY}</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="{IMG}dr-shweta-posing.jpg" alt="Dr. Shweta Kalra, Cosmetic Dentist, Star Dental Clinic Hisar">
    </div>
  </div>
</section>
""".strip("\n")

    price = f"""
<div class="price-band">
  <div>
    <div class="eyebrow" style="margin-bottom:4px">Transparent Pricing</div>
    <div class="amount">Personalised aligner quote</div>
    <div class="note">Cost depends on how much movement your teeth need and the number of aligner sets required.</div>
  </div>
  <a class="btn btn-wa" data-wa data-wa-msg="Hi, I'd like a personalised quote for clear aligners." href="#">{ICONS['wa']} Get My Quote on WhatsApp</a>
</div>
<p class="price-disclaimer">Every smile is different — during your ₹200 consultation, Dr. Shweta Kalra will assess your teeth and give you a clear, written aligner quote before you commit.</p>
""".strip("\n")

    why = f"""
{eyebrow("Why Choose Aligners")}
<h2>Straighter teeth, without anyone noticing you're treating them</h2>
<div class="grid grid-2" style="margin-top:24px;align-items:start">
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Virtually invisible</strong> — clear plastic trays most people won't even notice.</span></li>
    <li>{ICONS['check']} <span><strong>Removable</strong> — take them out to eat, brush and floss normally.</span></li>
    <li>{ICONS['check']} <span><strong>No metal wires or brackets</strong> — smoother, more comfortable than traditional braces.</span></li>
  </ul>
  <ul class="check-list">
    <li>{ICONS['check']} <span><strong>Planned digitally</strong> — you can see how your smile will move before treatment starts.</span></li>
    <li>{ICONS['check']} <span><strong>Fewer clinic visits</strong> — aligners are typically changed at home, with periodic check-ins.</span></li>
    <li>{ICONS['check']} <span><strong>Good for adults &amp; teens</strong> — a discreet option for professionals and students alike.</span></li>
  </ul>
</div>
""".strip("\n")

    process = f"""
{eyebrow("The Aligner Journey")}
<h2>From crooked to confident</h2>
<div class="steps" style="margin-top:28px">
  <div class="step"><h3>Consultation &amp; Scan</h3><p>Dr. Shweta examines your bite and discusses what you'd like to change about your smile.</p></div>
  <div class="step"><h3>Digital Treatment Plan</h3><p>A custom plan mapping out how your teeth will move, set by set.</p></div>
  <div class="step"><h3>Wear Your Aligners</h3><p>Wear each set as directed, changing to the next in the series on schedule.</p></div>
  <div class="step"><h3>Reveal Your Smile</h3><p>Regular check-ins track progress until your teeth reach their final, straighter position.</p></div>
</div>
""".strip("\n")

    vs = f"""
{eyebrow("Aligners vs Braces")}
<h2>Not sure which is right for you?</h2>
<p class="lede">Both aligners and traditional braces can straighten teeth effectively — the right choice depends on your case, lifestyle and budget. Dr. Shweta Kalra will recommend the best option for you at your consultation. Read our full comparison in the <a href="patient-education.html">Patient Education Hub</a>, or see our <a href="orthodontics-braces.html">Orthodontics &amp; Braces</a> page for traditional options.</p>
""".strip("\n")

    faqs = [
        ("How long does clear aligner treatment take?", "Treatment length depends on how much movement your teeth need — mild cases can be shorter, more complex cases take longer. Dr. Shweta will give you an estimated timeline at your consultation."),
        ("Do clear aligners hurt?", "You may feel mild pressure for a day or two after switching to a new aligner set — this is normal and a sign the aligners are working. It's generally more comfortable than traditional braces."),
        ("Can I eat and drink with aligners in?", "Aligners should be removed before eating or drinking anything other than water, then cleaned and reinserted — this is one of the biggest advantages over fixed braces."),
        ("Are clear aligners as effective as braces?", "For many cases of crowding, spacing and mild-to-moderate bite issues, aligners can be just as effective as braces. More complex bite problems may still need traditional braces — Dr. Shweta will advise honestly which is right for you."),
        ("At what age can someone start aligner treatment?", "Aligners work well for teens (once enough adult teeth have come in) through adults. Bring your child in for an evaluation and we'll advise on timing."),
    ]
    faq_section = f"""
{eyebrow("Aligner FAQs")}
<h2>Questions patients ask before starting aligners</h2>
<div style="margin-top:20px">{faq_block(faqs)}</div>
""".strip("\n")

    body = "\n".join([
        hero,
        section(price, "section-tight"),
        section(why),
        section(process, "section-alt"),
        section(vs),
        section(faq_section, "section-alt"),
        section(cta_band(
            "Start your aligner journey",
            "Message Dr. Shweta on WhatsApp with a photo of your smile — she'll tell you what to expect at your consultation.",
            wa_msg="Hi, I'd like to book an aligner consultation at Star Dental Clinic.",
        )),
    ])

    write_page("clear-aligners-hisar.html", page_shell(
        active_href=active,
        title="Clear Aligners in Hisar | Invisible Teeth Straightening — Star Dental Clinic",
        meta_description="Straighten your teeth invisibly with clear aligners in Hisar. Dr. Shweta Kalra plans every case personally at Star Dental Clinic, Fawara Chowk. Book a consultation on WhatsApp.",
        page_label="Clear Aligners",
        body_html=body,
        extra_schemas=[faq_schema(faqs), breadcrumb_schema([("Home", ""), ("Clear Aligners", active)])],
    ))


# --------------------------------------------------------- ABOUT/DOCTORS --

def page_about():
    active = "about-doctors.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("About & Doctors", None)])}
    {eyebrow("About Star Dental Clinic")}
    <h1>A Specialist Couple, One ISO-Certified Clinic</h1>
    <p class="lede">Star Dental Clinic was built around a simple idea: Hisar deserves specialist-level dental care, not just a general check-up. Dr. Tarun Kalra and Dr. Shweta Kalra run the clinic together from Fawara Chowk — he focused on root canals, implants and restorative dentistry; she focused on cosmetic dentistry and smile design.</p>
  </div>
</section>
""".strip("\n")

    tarun = f"""
<div class="doctor-card">
  <img src="{IMG}dr-tarun-award-event.jpg" alt="Dr. Tarun Kalra being felicitated at a dental event">
  <div>
    <div class="doctor-name">Dr. Tarun Kalra</div>
    <div class="doctor-title">BDS, MDS (PGIMS, Rohtak) — Endodontics &amp; Implants</div>
    <p>Dr. Tarun Kalra completed his Master's in Dental Surgery (MDS) from Pt. B.D. Sharma PGIMS, Rohtak — one of Haryana's leading government dental institutes — and has practiced in Hisar for over 14 years. His clinical focus is single-sitting root canal treatment and dental implants, and he leads treatment planning for every implant and full-mouth rehabilitation case at the clinic.</p>
    <ul class="cred-list">
      <li>{ICONS['check']} MDS (Master of Dental Surgery) — PGIMS, Rohtak</li>
      <li>{ICONS['check']} 14+ years of clinical practice in Hisar</li>
      <li>{ICONS['check']} Specialist focus: root canal treatment &amp; dental implants</li>
      <li>{ICONS['check']} Recognised at regional dental association events</li>
    </ul>
  </div>
</div>
""".strip("\n")

    shweta = f"""
<div class="doctor-card">
  <img src="{IMG}dr-shweta-treating-woman.jpg" alt="Dr. Shweta Kalra treating a patient at Star Dental Clinic Hisar">
  <div>
    <div class="doctor-name">Dr. Shweta Kalra</div>
    <div class="doctor-title">BDS, MIDA — Cosmetic Dentistry</div>
    <p>Dr. Shweta Kalra brings a gentle, detail-focused approach to cosmetic dentistry — from clear aligners and smile design to routine family care. She has treated patients in Hisar for over 9 years, and is known among patients for taking the time to explain treatment options clearly before recommending a plan.</p>
    <ul class="cred-list">
      <li>{ICONS['check']} BDS, MIDA</li>
      <li>{ICONS['check']} 9+ years of clinical practice in Hisar</li>
      <li>{ICONS['check']} Specialist focus: clear aligners, smile design &amp; cosmetic dentistry</li>
      <li>{ICONS['check']} Known for a gentle approach with children &amp; nervous patients</li>
    </ul>
  </div>
</div>
""".strip("\n")

    clinic_story = f"""
{eyebrow("Our Clinic")}
<h2>Why we built an ISO-certified clinic in the heart of Hisar</h2>
<div class="two-col">
  <div>
    <p>Star Dental Clinic operates from the Old Courts Commercial Complex at Fawara Chowk — one of the most recognisable, central locations in Hisar. We built the clinic around ISO-certified sterilisation and safety protocols, because dental care should meet the same standard patients expect from a hospital, not just a shop-front dentist.</p>
    <p>Every treatment plan — whether it's a single filling or a full-mouth implant rehabilitation — starts with a proper clinical exam and X-rays where needed, followed by a clear, written quote. No patient starts treatment without understanding exactly what it involves and what it costs.</p>
    <div class="badge-row">
      <span class="badge">{ICONS['check']} ISO Certified</span>
      <span class="badge">{ICONS['check']} Advanced RCT &amp; Implant Centre</span>
      <span class="badge">{ICONS['check']} Complete Family Dental Care</span>
    </div>
  </div>
  <img src="{IMG}dr-tarun-reception.jpg" alt="Reception area, Star Dental Clinic, Hisar" style="border-radius:16px">
</div>
""".strip("\n")

    body = "\n".join([
        hero,
        section(f'<div class="grid grid-2" style="align-items:start">{tarun}{shweta}</div>'),
        section(clinic_story, "section-alt"),
        section(cta_band(
            "Meet Dr. Tarun or Dr. Shweta in person",
            "Book a consultation on WhatsApp and let us know which concern you'd like to discuss.",
        )),
    ])

    write_page("about-doctors.html", page_shell(
        active_href=active,
        title="About Us | Dr. Tarun Kalra & Dr. Shweta Kalra — Star Dental Clinic Hisar",
        meta_description="Meet Dr. Tarun Kalra (MDS, PGIMS Rohtak) and Dr. Shweta Kalra of Star Dental Clinic, Hisar — an ISO-certified clinic specialising in implants, root canal and cosmetic dentistry.",
        page_label="About & Doctors",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("About & Doctors", active)])],
    ))


# ------------------------------------------------------------- SERVICES ---

SERVICE_DEFS = [
    dict(slug="root-canal-treatment.html", name="Root Canal Treatment", short="Single-sitting RCT by an MDS Endodontist — save the tooth, stop the pain.",
         img="dr-tarun-woman-patient.jpg",
         intro="A root canal treats infection or damage deep inside a tooth, removing the source of pain and saving the tooth rather than extracting it. Dr. Tarun Kalra, an MDS-qualified specialist, completes most root canal treatments in a single sitting — meaning less time off work and fewer visits to the clinic.",
         points=[
             "Single-sitting treatment for most cases — no repeated appointments",
             "Performed under local anaesthesia for a comfortable experience",
             "Followed by a crown to protect and restore the treated tooth",
             "Handled by an MDS specialist, not general dentistry alone",
         ],
         faqs=[
             ("Is root canal treatment painful?", "The procedure itself is done under local anaesthesia, so you shouldn't feel pain during treatment. In fact, RCT relieves the pain caused by the underlying infection."),
             ("Can it really be done in a single visit?", "In most straightforward cases, yes — Dr. Tarun Kalra specialises in single-sitting RCT. More complex cases may need a follow-up visit, which he'll explain upfront."),
             ("What happens after the root canal?", "The tooth is typically capped with a crown to protect it and restore full chewing function — see our Crowns & Bridges page for details."),
         ]),
    dict(slug="full-mouth-rehabilitation.html", name="Full Mouth Rehabilitation", short="A complete plan to restore function and appearance when multiple teeth need attention.",
         img="dr-tarun-elderly-patient.jpg",
         intro="When several teeth are missing, damaged or worn down, treating them one at a time rarely gives the best result. Full mouth rehabilitation is a coordinated treatment plan — combining implants, crowns, root canal treatment and bite correction where needed — designed by Dr. Tarun Kalra to restore both function and appearance together.",
         points=[
             "One coordinated plan instead of piecemeal treatments",
             "Combines implants, crowns and restorative dentistry as needed",
             "Restores chewing function, bite alignment and appearance",
             "Ideal for patients with multiple missing or damaged teeth",
         ],
         faqs=[
             ("Who needs full mouth rehabilitation?", "Patients with several missing, broken or heavily worn teeth, or long-standing bite problems, are the most common candidates. Dr. Tarun will assess your case and explain if this approach is right for you."),
             ("How long does full mouth rehabilitation take?", "Timelines vary significantly by case — from a few weeks to several months when implants are involved. You'll receive a specific timeline as part of your written treatment plan."),
             ("Is this the same as getting dentures?", "Not necessarily — depending on your case, the plan may use fixed implants, crowns and bridges rather than removable dentures. Dr. Tarun will discuss the options suited to your situation."),
         ]),
    dict(slug="smile-design-cosmetic-dentistry.html", name="Smile Design & Cosmetic Dentistry", short="Veneers, whitening and bonding to redesign your smile with natural-looking results.",
         img="dr-shweta-posing.jpg",
         intro="Smile design looks at your whole smile — tooth shape, colour, alignment and gum line — and plans changes that look natural, not artificial. Dr. Shweta Kalra leads cosmetic treatment at Star Dental Clinic, from teeth whitening and bonding to more involved smile makeovers.",
         points=[
             "Personalised smile assessment before any treatment",
             "Teeth whitening, bonding and cosmetic contouring",
             "Natural-looking results matched to your face and features",
             "Can be combined with aligners or crowns for a full smile makeover",
         ],
         faqs=[
             ("What's included in a smile design consultation?", "Dr. Shweta examines your teeth, gums and bite, discusses what you'd like to change, and recommends an approach — which may be as simple as whitening or as involved as a full smile makeover."),
             ("Is cosmetic dentistry only for aesthetics?", "Primarily yes, though many cosmetic treatments (like bonding or crowns) also restore function or protect a damaged tooth."),
             ("How long do cosmetic results last?", "It depends on the treatment — whitening results fade gradually over time with normal use, while veneers and crowns are longer-lasting. Dr. Shweta will explain what to expect for your specific plan."),
         ]),
    dict(slug="orthodontics-braces.html", name="Orthodontics & Braces", short="Traditional braces and modern alignment options for children, teens and adults.",
         img="dr-tarun-girl-patient-posing.jpg",
         intro="Crowded, crooked or gapped teeth affect more than appearance — they can make cleaning harder and affect your bite. Star Dental Clinic offers traditional braces for patients who need more involved correction, alongside clear aligners for candidates who prefer a removable, less visible option.",
         points=[
             "Suitable for children, teens and adults",
             "Traditional metal and ceramic braces available",
             "Clear aligners offered for eligible cases — see our dedicated page",
             "Regular adjustment visits to track progress",
         ],
         faqs=[
             ("At what age should a child see an orthodontist?", "It's worth an evaluation once most adult teeth have come in, though some bite issues are best caught earlier. Bring your child in and we'll advise on timing."),
             ("Braces or aligners — which is right for me?", "It depends on your case. Braces can treat more complex bite issues; aligners suit mild-to-moderate cases where a removable, less visible option matters. Dr. Shweta and Dr. Tarun will recommend honestly after an exam."),
             ("How long does orthodontic treatment take?", "Treatment length varies by case, generally from several months to a couple of years — you'll get a specific estimate after your consultation."),
         ]),
    dict(slug="crowns-bridges.html", name="Crowns & Bridges", short="Durable, custom-shaded restorations to repair damaged or missing teeth.",
         img="dr-tarun-woman-patient.jpg",
         intro="A crown caps and protects a damaged or root-canal-treated tooth, while a bridge replaces one or more missing teeth using the surrounding teeth as support. Both are custom-made and shade-matched so they blend naturally with the rest of your smile.",
         points=[
             "Crowns protect teeth after root canal treatment or significant damage",
             "Bridges replace missing teeth without surgery",
             "Custom shade-matching for a natural appearance",
             "Built to restore full chewing function",
         ],
         faqs=[
             ("How long do crowns and bridges last?", "With good care, they're designed to last many years — Dr. Tarun will advise on maintenance specific to your restoration."),
             ("Is getting a crown painful?", "The procedure is done under local anaesthesia where needed, and most patients find it straightforward and comfortable."),
             ("Crown or implant — how do I choose?", "It depends on whether the natural tooth root can be saved. Dr. Tarun will explain which option fits your specific case at your consultation."),
         ]),
    dict(slug="kids-dentistry.html", name="Kids Dentistry", short="Gentle, patient-friendly dental care that keeps young smiles healthy from the start.",
         img="dr-tarun-girl-patient.jpg",
         intro="Children need a different approach to dental care — one that builds comfort and trust, not just treats teeth. Dr. Shweta Kalra and Dr. Tarun Kalra both see young patients at Star Dental Clinic, from routine check-ups and cleanings to cavity treatment and early orthodontic evaluation.",
         points=[
             "Gentle, patient-friendly approach for first-time visits",
             "Routine check-ups, cleanings and cavity treatment",
             "Early evaluation for orthodontic or bite concerns",
             "Guidance for parents on at-home dental care habits",
         ],
         faqs=[
             ("When should my child have their first dental visit?", "General guidance is to bring children in once their first teeth appear or by their first birthday, and then for regular check-ups after that — but it's never too late to start if you haven't yet."),
             ("What if my child is scared of the dentist?", "Our team takes a gentle, unhurried approach with young or nervous patients, explaining each step in a way children can understand."),
             ("Do you treat cavities in baby teeth?", "Yes — baby teeth matter for chewing, speech and guiding adult teeth into place, so we treat cavities in them just as we would in adult teeth."),
         ]),
]


def service_detail_body(svc):
    price = f"""
<div class="price-band">
  <div>
    <div class="eyebrow" style="margin-bottom:4px">Transparent Pricing</div>
    <div class="amount">Get a personalised quote</div>
    <div class="note">Cost depends on your specific case — you'll get a clear, written quote after your ₹200 consultation.</div>
  </div>
  <a class="btn btn-wa" data-wa data-wa-msg="Hi, I'd like to know more about {svc['name']} at Star Dental Clinic." href="#">{ICONS['wa']} Ask on WhatsApp</a>
</div>
""".strip("\n")
    points_html = "".join(f'<li>{ICONS["check"]} <span>{p}</span></li>' for p in svc["points"])
    intro = f"""
{breadcrumbs_html([("Home", "index.html"), ("Services", "services.html"), (svc["name"], None)])}
<div class="two-col">
  <div>
    {eyebrow(svc["name"])}
    <h1>{svc["name"]} in Hisar</h1>
    <p class="lede">{svc["intro"]}</p>
    <div class="cta-row">
      <a class="btn btn-wa" data-wa data-wa-msg="Hi, I'd like to book a consultation for {svc['name']}." href="#">{ICONS['wa']} Book a Consultation</a>
      <a class="btn btn-call" href="tel:{PHONE_TEL}">{ICONS['phone']} Call {PHONE_DISPLAY}</a>
    </div>
  </div>
  <img src="{IMG}{svc['img']}" alt="{svc['name']} at Star Dental Clinic, Hisar" style="border-radius:16px">
</div>
""".strip("\n")
    points_section = f"""
{eyebrow("What To Expect")}
<h2>Why patients choose us for {svc['name'].lower()}</h2>
<ul class="check-list" style="margin-top:20px">{points_html}</ul>
""".strip("\n")
    faq_section = f"""
{eyebrow("FAQs")}
<h2>Common questions</h2>
<div style="margin-top:20px">{faq_block(svc['faqs'])}</div>
""".strip("\n")
    body = "\n".join([
        section(intro),
        section(price, "section-tight section-alt"),
        section(points_section),
        section(faq_section, "section-alt"),
        section(cta_band(
            f"Ready to discuss {svc['name'].lower()}?",
            "Message us on WhatsApp — we'll help you book the right doctor and time.",
            wa_msg=f"Hi, I'd like to book a consultation for {svc['name']}.",
        )),
    ])
    return body, svc["faqs"]


def page_service_details():
    for svc in SERVICE_DEFS:
        body, faqs = service_detail_body(svc)
        write_page(svc["slug"], page_shell(
            active_href=svc["slug"],
            title=f"{svc['name']} in Hisar | Star Dental Clinic",
            meta_description=f"{svc['short']} Star Dental Clinic, Fawara Chowk, Hisar. Book a consultation on WhatsApp.",
            page_label=svc["name"],
            body_html=body,
            extra_schemas=[faq_schema(faqs), breadcrumb_schema([("Home", ""), ("Services", "services.html"), (svc["name"], svc["slug"])])],
        ))


def page_services():
    active = "services.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("Services", None)])}
    {eyebrow("All Services")}
    <h1>Complete Dental Care, Under One Roof</h1>
    <p class="lede">From a routine check-up to full-mouth implant rehabilitation — here's everything Star Dental Clinic treats, and the doctor who leads each area.</p>
  </div>
</section>
""".strip("\n")
    pillar_cards = f"""
<div class="grid grid-2">
  <a class="card service-card" href="dental-implants-hisar.html">
    <div class="card-icon">{ICONS['star']}</div>
    <h3>Dental Implants</h3>
    <p>Fixed, permanent tooth replacement led by Dr. Tarun Kalra (MDS).</p>
    <span class="card-link">Learn more →</span>
  </a>
  <a class="card service-card" href="clear-aligners-hisar.html">
    <div class="card-icon">{ICONS['star']}</div>
    <h3>Clear Aligners</h3>
    <p>Invisible teeth straightening designed by Dr. Shweta Kalra.</p>
    <span class="card-link">Learn more →</span>
  </a>
</div>
""".strip("\n")
    cards = "".join(
        f"""<a class="card service-card" href="{s['slug']}">
  <div class="card-icon">{ICONS['star']}</div>
  <h3>{s['name']}</h3>
  <p>{s['short']}</p>
  <span class="card-link">Learn more →</span>
</a>""" for s in SERVICE_DEFS
    )
    body = "\n".join([
        hero,
        section(pillar_cards),
        section(f'<div class="grid grid-3">{cards}</div>', "section-alt"),
        section(cta_band(
            "Not sure which service you need?",
            "Tell us what's bothering you on WhatsApp and we'll point you to the right treatment.",
        )),
    ])
    write_page("services.html", page_shell(
        active_href=active,
        title="Dental Services in Hisar | Star Dental Clinic",
        meta_description="Explore all dental services at Star Dental Clinic, Hisar — implants, aligners, root canal, full mouth rehabilitation, cosmetic dentistry, orthodontics, crowns & bridges, and kids dentistry.",
        page_label="Services",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Services", active)])],
    ))


# --------------------------------------------------------------- GALLERY --

GALLERY_IMAGES = [
    ("clinic-exterior.jpg", "Star Dental Clinic exterior at Fawara Chowk, Hisar"),
    ("dr-tarun-reception.jpg", "Clinic reception, Star Dental Clinic, Hisar"),
    ("both-doctors-standing.jpg", "Dr. Tarun Kalra and Dr. Shweta Kalra, Star Dental Clinic"),
    ("both-doctors-sitting.jpg", "Dr. Tarun Kalra and Dr. Shweta Kalra"),
    ("both-doctors-two-chairs.jpg", "Treatment chairs at Star Dental Clinic, Hisar"),
    ("both-doctors-two-patients.jpg", "Dr. Tarun Kalra and Dr. Shweta Kalra treating patients"),
    ("both-doctors-female-patient.jpg", "Consultation at Star Dental Clinic, Hisar"),
    ("dr-tarun-portrait.jpg", "Dr. Tarun Kalra, MDS, Star Dental Clinic"),
    ("dr-tarun-award-event.jpg", "Dr. Tarun Kalra being felicitated at a dental event"),
    ("dr-tarun-woman-patient.jpg", "Dr. Tarun Kalra treating a patient"),
    ("dr-tarun-elderly-patient.jpg", "Dr. Tarun Kalra with a patient"),
    ("dr-tarun-girl-patient.jpg", "Dr. Tarun Kalra with a young patient"),
    ("dr-tarun-girl-patient-posing.jpg", "A young patient at Star Dental Clinic"),
    ("dr-tarun-kid-standing.jpg", "A young patient visiting Star Dental Clinic"),
    ("dr-shweta-portrait.jpg", "Dr. Shweta Kalra, Star Dental Clinic"),
    ("dr-shweta-posing.jpg", "Dr. Shweta Kalra, Cosmetic Dentist"),
    ("dr-shweta-treating-patient.jpg", "Dr. Shweta Kalra treating a patient"),
    ("dr-shweta-treating-woman.jpg", "Dr. Shweta Kalra treating a patient"),
]


def page_gallery():
    active = "gallery.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("Gallery", None)])}
    {eyebrow("Gallery")}
    <h1>Inside Star Dental Clinic</h1>
    <p class="lede">A look at our clinic, our doctors and the care we provide — all real photos from Fawara Chowk, Hisar.</p>
  </div>
</section>
""".strip("\n")
    imgs = "".join(
        f'<a href="{IMG}{fn}" target="_blank" rel="noopener"><img src="{THUMB}{fn}" alt="{alt}" loading="lazy"></a>'
        for fn, alt in GALLERY_IMAGES
    )
    grid = f'<div class="gallery-grid grid grid-4">{imgs}</div>'
    body = "\n".join([
        hero,
        section(grid),
        section(cta_band("Like what you see?", "Book your visit to Star Dental Clinic on WhatsApp today.")),
    ])
    write_page("gallery.html", page_shell(
        active_href=active,
        title="Gallery | Star Dental Clinic, Hisar",
        meta_description="Photos of Star Dental Clinic, Hisar — our ISO-certified facility, Dr. Tarun Kalra, Dr. Shweta Kalra and patient care in action.",
        page_label="Gallery",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Gallery", active)])],
    ))


# ----------------------------------------------------- PATIENT EDUCATION --

ARTICLES = [
    dict(slug="blog-dental-implant-cost-hisar.html", title="What Affects the Cost of a Dental Implant?",
         tag="Dental Implants", img="dr-tarun-elderly-patient.jpg",
         excerpt="Implant cost isn't one fixed number — here's what actually drives it, and how to get an accurate quote.",
         body=[
            "One of the first questions patients ask about dental implants is simple: how much will it cost? The honest answer is that it depends — and understanding what it depends on helps you ask the right questions at your consultation.",
            "<h2>Number of implants needed</h2><p>Replacing a single tooth is a very different plan from replacing several teeth, or restoring a full arch. Your treatment plan will specify exactly how many implants your case needs and why.</p>",
            "<h2>Bone condition</h2><p>Dental implants need enough healthy jawbone to anchor into. If bone volume has reduced — common after teeth have been missing for a while — additional preparation may be needed before or during implant placement.</p>",
            "<h2>The implant system used</h2><p>Implant systems vary in material and design. Dr. Tarun Kalra will explain which system he recommends for your case and why, as part of your written treatment plan.</p>",
            "<h2>What's included in the crown</h2><p>The implant itself is only part of the picture — the crown that sits on top, custom-shade-matched to your other teeth, is a separate part of the plan and cost.</p>",
            "<h2>The only reliable way to know your cost</h2><p>Because every case is different, the only accurate way to know what your implant will cost is a proper consultation with X-rays. At Star Dental Clinic, that consultation is ₹200, and you'll leave with a clear, written quote — no guessing, no hidden charges.</p>",
         ]),
    dict(slug="blog-clear-aligners-vs-braces.html", title="Clear Aligners vs Braces: Which Should You Choose?",
         tag="Clear Aligners", img="dr-shweta-posing.jpg",
         excerpt="Both straighten teeth effectively — the right choice depends on your case, lifestyle and how visible you want treatment to be.",
         body=[
            "If you're considering straightening your teeth, you've probably already come across both options — traditional braces and clear aligners. Both work. The right one for you depends on a few honest factors.",
            "<h2>How complex is your case?</h2><p>Traditional braces can handle a wider range of bite and alignment issues, including more complex cases. Clear aligners work very well for mild-to-moderate crowding, spacing and alignment issues.</p>",
            "<h2>How visible do you want treatment to be?</h2><p>Clear aligners are far less noticeable than metal braces — a common reason adults and professionals prefer them.</p>",
            "<h2>Do you want a removable option?</h2><p>Aligners come out for eating, brushing and flossing. Braces are fixed to your teeth for the full treatment period.</p>",
            "<h2>How disciplined can you be?</h2><p>Because aligners are removable, results depend on wearing them as directed. Braces don't rely on patient compliance in the same way.</p>",
            "<h2>Our honest recommendation approach</h2><p>At Star Dental Clinic, Dr. Shweta Kalra examines your bite and explains — honestly — whether aligners are likely to give you the result you want, or whether braces are the better fit. We'd rather recommend the right treatment than the more expensive one.</p>",
         ]),
    dict(slug="blog-root-canal-myths.html", title="5 Root Canal Myths That Keep People in Pain",
         tag="Root Canal Treatment", img="dr-tarun-woman-patient.jpg",
         excerpt="Root canal treatment has a bad reputation it doesn't deserve. Here's what's actually true.",
         body=[
            "\"Root canal\" might be one of the most feared phrases in dentistry — and most of the fear is based on outdated ideas. Here's what's actually true.",
            "<h2>Myth 1: Root canal treatment is extremely painful</h2><p>In reality, the procedure is done under local anaesthesia. The pain patients associate with root canals is usually the infection itself — which the treatment relieves, not causes.</p>",
            "<h2>Myth 2: It takes many visits</h2><p>Dr. Tarun Kalra, an MDS specialist, completes most root canal treatments in a single sitting — meaning one appointment, not a drawn-out series of visits.</p>",
            "<h2>Myth 3: It's better to just extract the tooth</h2><p>Saving your natural tooth is almost always better for long-term chewing function and jaw health than extracting it. Root canal treatment is specifically designed to save the tooth.</p>",
            "<h2>Myth 4: The tooth is \"dead\" and will look different afterward</h2><p>With a properly fitted crown afterward, a root-canal-treated tooth functions and looks just like your other teeth.</p>",
            "<h2>Myth 5: You'll need it again later</h2><p>A well-performed root canal, followed by a crown and good oral hygiene, is designed to be a long-term, permanent solution.</p>",
            "<p>If you're dealing with tooth pain and dreading the idea of a root canal, the most useful next step is simply getting it examined — most patients are relieved to learn it's far more manageable than they expected.</p>",
         ]),
    dict(slug="blog-kids-first-dental-visit.html", title="When Should Your Child's First Dental Visit Be?",
         tag="Kids Dentistry", img="dr-tarun-girl-patient.jpg",
         excerpt="Earlier than most parents think — and it sets the tone for how your child feels about dental care for life.",
         body=[
            "Many parents wait until a child complains of tooth pain before booking a first dental visit. Starting earlier — and making that first visit positive — makes a real difference.",
            "<h2>General guidance on timing</h2><p>A good rule of thumb is to bring your child in once their first teeth appear, or by their first birthday. If you haven't started yet and your child is older, it's still worth booking a visit now rather than waiting.</p>",
            "<h2>Why baby teeth matter</h2><p>Baby teeth aren't \"practice teeth\" — they matter for chewing, speech development, and guiding adult teeth into the correct position later. Cavities in baby teeth are treated seriously for these reasons.</p>",
            "<h2>Making the first visit positive</h2><p>At Star Dental Clinic, we take a gentle, unhurried approach with young and first-time patients — explaining each step in a way children can understand, rather than rushing through a routine exam.</p>",
            "<h2>What we check for</h2><p>A first visit typically includes a check of tooth development, early signs of decay, and guidance for parents on brushing habits and diet — building a foundation for healthy dental habits.</p>",
            "<p>If your child hasn't had a dental check-up yet, there's no need to wait for a problem to appear — an early, calm first visit is one of the best things you can do for their long-term dental health.</p>",
         ]),
]


def article_page(a):
    active = a["slug"]
    body_html = "".join(f"<p>{b}</p>" if not b.startswith("<h2>") else b for b in a["body"])
    content = f"""
{breadcrumbs_html([("Home", "index.html"), ("Patient Education", "patient-education.html"), (a["title"], None)])}
<div class="prose">
  {eyebrow(a["tag"])}
  <h1>{a["title"]}</h1>
  <img src="{IMG}{a['img']}" alt="{a['title']}" style="border-radius:16px;margin:20px 0">
  {body_html}
</div>
""".strip("\n")
    body = "\n".join([
        section(content),
        section(cta_band(
            "Have a question about this?",
            "Message us on WhatsApp — Dr. Tarun or Dr. Shweta will personally answer.",
        ), "section-alt"),
    ])
    write_page(a["slug"], page_shell(
        active_href=active,
        title=f"{a['title']} | Star Dental Clinic Hisar",
        meta_description=a["excerpt"],
        page_label=a["title"],
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Patient Education", "patient-education.html"), (a["title"], active)])],
    ))


def page_patient_education():
    active = "patient-education.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("Patient Education", None)])}
    {eyebrow("Patient Education Hub")}
    <h1>Straight Answers About Dental Care</h1>
    <p class="lede">Clear, honest articles from Dr. Tarun Kalra and Dr. Shweta Kalra — so you know what to expect before you ever sit in the chair.</p>
  </div>
</section>
""".strip("\n")
    cards = "".join(
        f"""<a class="article-card" href="{a['slug']}">
  <img src="{THUMB}{a['img']}" alt="{a['title']}">
  <div class="art-body">
    <div class="art-tag">{a['tag']}</div>
    <h3>{a['title']}</h3>
    <p>{a['excerpt']}</p>
  </div>
</a>""" for a in ARTICLES
    )
    body = "\n".join([
        hero,
        section(f'<div class="grid grid-2">{cards}</div>'),
        section(cta_band("Didn't find your answer?", "Ask us directly on WhatsApp — we're happy to help.")),
    ])
    write_page("patient-education.html", page_shell(
        active_href=active,
        title="Patient Education Hub | Star Dental Clinic Hisar",
        meta_description="Read clear, honest articles on dental implants, clear aligners, root canal treatment and kids dentistry from Star Dental Clinic, Hisar.",
        page_label="Patient Education",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Patient Education", active)])],
    ))


# ------------------------------------------------------------- REVIEWS ---

def page_reviews():
    active = "reviews.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("Reviews", None)])}
    {eyebrow("Patient Reviews")}
    <h1>What Patients Say on Google</h1>
    <p class="lede">We believe in real, verified reviews — not written testimonials on a website. See what patients are saying about Star Dental Clinic directly on our Google Business Profile.</p>
    <div class="trust-pills">
      <a class="trust-pill" href="{GBP_URL}" target="_blank" rel="noopener">{ICONS['star']} {GBP_RATING}★ Rated · {GBP_REVIEW_COUNT} Google Reviews</a>
    </div>
  </div>
</section>
""".strip("\n")
    gbp_card = f"""
<div class="card center" style="max-width:560px;padding:40px">
  <div class="card-icon center" style="margin-left:auto;margin-right:auto">{ICONS['star']}</div>
  <h2>{GBP_RATING} out of 5, from {GBP_REVIEW_COUNT} Google Reviews</h2>
  <p>Every review on our Google Business Profile comes from a real patient — see the latest feedback, or leave your own after your visit.</p>
  <a class="btn btn-gold" href="{GBP_URL}" target="_blank" rel="noopener">{ICONS['star']} View Reviews on Google</a>
</div>
""".strip("\n")
    ask = f"""
{eyebrow("Just Visited Us?")}
<h2>Tell us — and other patients — how it went</h2>
<p class="lede">If Dr. Tarun, Dr. Shweta or our team looked after you recently, a review on Google helps other patients in Hisar find the right care. It only takes a minute.</p>
<a class="btn btn-call" href="{GBP_URL}" target="_blank" rel="noopener">Leave a Google Review →</a>
""".strip("\n")
    body = "\n".join([
        hero,
        section(gbp_card),
        section(ask, "section-alt"),
        section(cta_band("Ready to book your visit?", "Message us on WhatsApp to get started.")),
    ])
    write_page("reviews.html", page_shell(
        active_href=active,
        title=f"Patient Reviews | {GBP_RATING}★ ({GBP_REVIEW_COUNT}+ Reviews) | Star Dental Clinic Hisar",
        meta_description=f"Rated {GBP_RATING} out of 5 from {GBP_REVIEW_COUNT} verified Google reviews. Read what Star Dental Clinic patients in Hisar are saying, or leave your own after your visit.",
        page_label="Reviews",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Reviews", active)])],
    ))


# ------------------------------------------------------------- CONTACT ---

def page_contact():
    active = "contact.html"
    hero = f"""
<section class="section section-navy" style="padding-top:52px">
  <div class="container">
    {breadcrumbs_html([("Home", "index.html"), ("Contact", None)])}
    {eyebrow("Contact & Directions")}
    <h1>Visit or Message Star Dental Clinic</h1>
    <p class="lede">We're at Fawara Chowk, Lajpat Nagar — one of the easiest-to-find locations in Hisar. Reach out on WhatsApp, call, or just walk in during clinic hours.</p>
  </div>
</section>
""".strip("\n")
    info_col = f"""
<div class="card">
  <h3>{ICONS['pin']} Address</h3>
  <p>{ADDRESS_FULL}</p>
  <h3 style="margin-top:20px">{ICONS['clock']} Clinic Hours</h3>
  <p>Monday – Saturday, 10:00 AM – 8:00 PM</p>
  <h3 style="margin-top:20px">{ICONS['phone']} Phone / WhatsApp</h3>
  <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
  <div class="cta-row">
    <a class="btn btn-wa" data-wa href="#">{ICONS['wa']} WhatsApp Us</a>
    <a class="btn btn-call" href="tel:{PHONE_TEL}">{ICONS['phone']} Call Now</a>
  </div>
</div>
""".strip("\n")
    form_col = f"""
<div class="card">
  <h3>Send Us a Message</h3>
  <p style="color:var(--muted);font-size:.88rem">This opens WhatsApp with your details pre-filled — we typically reply the same day.</p>
  <form class="contact-form" id="contact-form">
    <div><label for="cf-name">Name</label><input id="cf-name" name="name" type="text" required></div>
    <div><label for="cf-phone">Phone Number</label><input id="cf-phone" name="phone" type="tel" required></div>
    <div><label for="cf-interest">I'm interested in</label>
      <select id="cf-interest" name="interest">
        <option>Dental Implants</option>
        <option>Clear Aligners</option>
        <option>Root Canal Treatment</option>
        <option>Full Mouth Rehabilitation</option>
        <option>Smile Design / Cosmetic</option>
        <option>Orthodontics / Braces</option>
        <option>Crowns & Bridges</option>
        <option>Kids Dentistry</option>
        <option>General Check-up</option>
      </select>
    </div>
    <div><label for="cf-message">Message (optional)</label><textarea id="cf-message" name="message" rows="3"></textarea></div>
    <button type="submit" class="btn btn-wa btn-block">{ICONS['wa']} Send via WhatsApp</button>
  </form>
</div>
""".strip("\n")
    map_section = f"""
{eyebrow("Find Us")}
<h2>Fawara Chowk, Old Courts Commercial Complex</h2>
<div class="map-embed" style="margin-top:20px">
  <iframe src="{MAP_EMBED_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Star Dental Clinic location map"></iframe>
</div>
""".strip("\n")
    body = "\n".join([
        hero,
        section(f'<div class="grid grid-2" style="align-items:start">{info_col}{form_col}</div>'),
        section(map_section, "section-alt"),
    ])
    write_page("contact.html", page_shell(
        active_href=active,
        title="Contact Us | Star Dental Clinic Hisar",
        meta_description="Visit Star Dental Clinic at Fawara Chowk, Hisar. Call or WhatsApp +91 98966 95691 to book a consultation. Open Monday–Saturday, 10 AM–8 PM.",
        page_label="Contact",
        body_html=body,
        extra_schemas=[breadcrumb_schema([("Home", ""), ("Contact", active)])],
    ))


if __name__ == "__main__":
    page_home()
    page_implants()
    page_aligners()
    page_about()
    page_services()
    page_service_details()
    page_gallery()
    page_patient_education()
    for a in ARTICLES:
        article_page(a)
    page_reviews()
    page_contact()
