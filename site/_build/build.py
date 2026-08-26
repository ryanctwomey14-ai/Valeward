#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valeward Capital — interior page builder.

index.html is maintained by hand (it is the only page with the full hero
treatment). Every other page is generated here so the head, header, footer and
disclosure block can never drift apart across ten files.

    python _build/build.py        # run from site/

Edit PAGES below, re-run, commit the generated .html.
"""
import io
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("approach.html", "Approach"),
    ("why-multifamily.html", "Why Multifamily"),
    ("investor-experience.html", "For Investors"),
    ("about.html", "About"),
]

ARROW = ('<svg class="btn__arrow" width="15" height="10" viewBox="0 0 15 10" fill="none" aria-hidden="true">'
         '<path d="M10 1l4 4-4 4M14 5H1" stroke="currentColor" stroke-width="1.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

BRAND_SVG = ('<svg class="brand__mark" viewBox="0 0 60 70" fill="none" aria-hidden="true">'
             '<path d="M8 68V30a22 22 0 0 1 44 0v38" stroke="currentColor" stroke-width="3.5"/>'
             '<path d="M19 34l11 20 11-20" stroke="#B8873B" stroke-width="6" stroke-linejoin="round"/>'
             '<rect x="4" y="66" width="52" height="4" fill="#B8873B"/></svg>')

SVG_DEFS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="skyDusk2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#241830"/><stop offset="50%" stop-color="#4B2F47"/>
      <stop offset="78%" stop-color="#8A5450"/><stop offset="100%" stop-color="#C79A55"/>
    </linearGradient>
    <linearGradient id="skyDay" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6D5474"/><stop offset="60%" stop-color="#B08C86"/>
      <stop offset="100%" stop-color="#E9D2CB"/>
    </linearGradient>
    <pattern id="winGrid" width="30" height="40" patternUnits="userSpaceOnUse">
      <rect x="8" y="10" width="14" height="18" fill="#D9B266" opacity=".42"/>
    </pattern>
    <pattern id="winGridDim" width="26" height="34" patternUnits="userSpaceOnUse">
      <rect x="7" y="9" width="12" height="15" fill="#D9B266" opacity=".2"/>
    </pattern>
    <radialGradient id="haze" cx="50%" cy="82%" r="60%">
      <stop offset="0%" stop-color="#B8873B" stop-opacity=".38"/>
      <stop offset="100%" stop-color="#B8873B" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <symbol id="scene-dusk" viewBox="0 0 800 1000" preserveAspectRatio="xMidYMid slice">
    <rect width="800" height="1000" fill="url(#skyDusk2)"/>
    <rect width="800" height="1000" fill="url(#haze)"/>
    <g opacity=".55">
      <rect x="-20" y="520" width="150" height="480" fill="#2A1B33"/>
      <rect x="140" y="600" width="120" height="400" fill="#2A1B33"/>
      <rect x="620" y="560" width="200" height="440" fill="#2A1B33"/>
    </g>
    <g>
      <rect x="90" y="430" width="250" height="570" fill="#1E1329"/>
      <rect x="106" y="452" width="218" height="500" fill="url(#winGridDim)"/>
      <rect x="470" y="380" width="270" height="620" fill="#1E1329"/>
      <rect x="486" y="402" width="238" height="560" fill="url(#winGridDim)"/>
    </g>
    <g>
      <rect x="300" y="300" width="230" height="700" fill="#150D1D"/>
      <rect x="318" y="326" width="194" height="640" fill="url(#winGrid)"/>
      <rect x="326" y="336" width="14" height="18" fill="#F0CE8A" opacity=".95"/>
      <rect x="416" y="416" width="14" height="18" fill="#F0CE8A" opacity=".85"/>
      <rect x="356" y="536" width="14" height="18" fill="#F0CE8A" opacity=".9"/>
      <rect x="476" y="616" width="14" height="18" fill="#F0CE8A" opacity=".8"/>
      <rect x="386" y="736" width="14" height="18" fill="#F0CE8A" opacity=".95"/>
    </g>
    <rect y="940" width="800" height="60" fill="#120B19"/>
  </symbol>
  <symbol id="scene-facade" viewBox="0 0 800 560" preserveAspectRatio="xMidYMid slice">
    <rect width="800" height="560" fill="url(#skyDay)"/>
    <g opacity=".35"><rect x="0" y="180" width="800" height="380" fill="#5A4366"/></g>
    <g>
      <rect x="40" y="160" width="320" height="400" fill="#3C2A47"/>
      <rect x="60" y="190" width="280" height="330" fill="url(#winGrid)"/>
      <rect x="400" y="120" width="360" height="440" fill="#2E2038"/>
      <rect x="422" y="152" width="316" height="370" fill="url(#winGrid)"/>
      <rect x="30" y="150" width="340" height="14" fill="#B8873B" opacity=".8"/>
      <rect x="392" y="110" width="378" height="14" fill="#B8873B" opacity=".65"/>
    </g>
    <rect y="520" width="800" height="40" fill="#241830"/>
  </symbol>
  <!-- Lit facade seen through the arch -->
  <symbol id="scene-arch" viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice">
    <rect width="400" height="500" fill="url(#skyDusk2)"/>
    <rect y="70" width="400" height="430" fill="#4A3552"/>
    <rect y="70" width="400" height="430" fill="url(#haze)" opacity=".7"/>
    <g fill="#2E2038">
      <rect y="186" width="400" height="7"/><rect y="272" width="400" height="7"/>
      <rect y="358" width="400" height="7"/>
    </g>
    <g fill="#D9B266">
      <rect x="30" y="112" width="62" height="60" opacity=".34"/>
      <rect x="116" y="112" width="62" height="60" opacity=".72"/>
      <rect x="202" y="112" width="62" height="60" opacity=".28"/>
      <rect x="288" y="112" width="62" height="60" opacity=".55"/>
      <rect x="30" y="198" width="62" height="60" opacity=".62"/>
      <rect x="116" y="198" width="62" height="60" opacity=".26"/>
      <rect x="202" y="198" width="62" height="60" opacity=".8"/>
      <rect x="288" y="198" width="62" height="60" opacity=".3"/>
      <rect x="30" y="284" width="62" height="60" opacity=".3"/>
      <rect x="116" y="284" width="62" height="60" opacity=".58"/>
      <rect x="202" y="284" width="62" height="60" opacity=".24"/>
      <rect x="288" y="284" width="62" height="60" opacity=".68"/>
      <rect x="30" y="370" width="62" height="60" opacity=".5"/>
      <rect x="116" y="370" width="62" height="60" opacity=".22"/>
      <rect x="202" y="370" width="62" height="60" opacity=".64"/>
      <rect x="288" y="370" width="62" height="60" opacity=".28"/>
    </g>
    <g fill="#F6E2B4">
      <rect x="116" y="112" width="62" height="60" opacity=".5"/>
      <rect x="202" y="198" width="62" height="60" opacity=".55"/>
      <rect x="288" y="284" width="62" height="60" opacity=".42"/>
    </g>
    <rect y="462" width="400" height="38" fill="#1B1023"/>
  </symbol>
  <symbol id="scene-portrait" viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice">
    <rect width="400" height="500" fill="#2E2038"/>
    <circle cx="200" cy="196" r="76" fill="#5A4366"/>
    <path d="M60 500c0-84 63-152 140-152s140 68 140 152z" fill="#5A4366"/>
    <rect width="400" height="500" fill="url(#haze)" opacity=".5"/>
  </symbol>
</svg>
"""

def photo(scene, src, alt="", lazy=True):
    """lazy=False for anything above the fold or inside a clipped container:
    a clipped box can defer a lazy image indefinitely, and the interior hero
    is the LCP element on every generated page."""
    load = ' loading="lazy"' if lazy else ''
    return ('<div class="photo-slot">'
            '<svg width="100%" height="100%" preserveAspectRatio="xMidYMid slice">'
            '<use href="#' + scene + '"/></svg>'
            '<img src="assets/img/' + src + '" alt="' + alt + '"' + load + ' decoding="async"></div>')

def head(page):
    schema = page.get("schema", "")
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://www.valewardcapital.com/__SLUG__">
<meta property="og:type" content="website">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:image" content="https://www.valewardcapital.com/assets/img/og-home.jpg">
<meta property="og:url" content="https://www.valewardcapital.com/__SLUG__">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="noindex, nofollow"><!-- PREVIEW ONLY: delete this line before launch -->
<meta name="theme-color" content="#1B1023">
<link rel="icon" href="assets/img/valeward-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css?v=20260826192605">
__SCHEMA__
</head>
""".replace("__TITLE__", page["title"]).replace("__DESC__", page["desc"]) \
   .replace("__SLUG__", page["slug"]).replace("__SCHEMA__", schema)

def header(active):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ''
        links += '        <a class="nav__link" href="' + href + '"' + cur + '>' + label + '</a>\n'

    mlinks = ""
    for href, label in NAV:
        mlinks += '    <a class="m-link" href="' + href + '">' + label + '</a>\n'

    return """<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="scroll-progress" aria-hidden="true"></div>
""" + SVG_DEFS + """
<header class="header header--dark">
  <div class="container">
    <div class="header__inner">
      <a class="brand" href="index.html" aria-label="Valeward Capital, home">
        """ + BRAND_SVG + """
        <span class="brand__text"><span class="brand__name">Valeward</span><span class="brand__sub">Capital</span></span>
      </a>
      <nav class="nav" aria-label="Primary">
""" + links + """      </nav>
      <div class="header__actions">
        <a class="btn btn--ghost btn--sm" href="https://portal.valewardcapital.com" rel="nofollow">Investor login</a>
        <a class="btn btn--gold btn--sm" href="invest.html">Speak with our team</a>
        <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </div>
</header>

<div class="mobile-menu" id="mobile-menu">
  <div class="container">
""" + mlinks + """    <a class="m-link" href="insights.html">Insights</a>
    <a class="m-link" href="faq.html">FAQ</a>
    <a class="btn btn--gold" href="invest.html">Speak with our team</a>
    <a class="btn btn--ghost" href="https://portal.valewardcapital.com" rel="nofollow">Investor login</a>
  </div>
</div>

<main id="main">
"""

def page_hero(page):
    """Interior hero: no aperture, no metric bar — the homepage keeps that
    treatment so arriving on it still feels like arriving somewhere."""
    return """
<section class="hero hero--page grain">
  <div class="hero__bg" aria-hidden="true">""" + photo("scene-dusk", "hero-interior.jpg", lazy=False) + """</div>
  <div class="container hero__inner">
    <div class="hero__grid">
      <div>
        <p class="breadcrumb hero-up" style="--i:0"><a href="index.html">Valeward</a> &nbsp;/&nbsp; __CRUMB__</p>
        <h1 class="h1" data-split><span class="reveal-line">__H1__</span></h1>
        <p class="lede hero-up" style="--i:1">__LEDE__</p>
      </div>
    </div>
  </div>
</section>
""".replace("__CRUMB__", page.get("crumb", page["nav_label"])) \
   .replace("__H1__", page["h1"]).replace("__LEDE__", page["lede"])

CTA_BAND = """
<section class="cta-band grain">
  <span class="cta-band__arch" aria-hidden="true"></span>
  <div class="container reveal">
    <h2 class="h2">Offerings are made available to our access list first</h2>
    <p class="lede">Access requests are reviewed within two business days. Joining places you under no obligation.</p>
    <div class="btn-row btn-row--center">
      <a class="btn btn--gold btn--lg" href="invest.html" data-magnetic>Speak with our team """ + ARROW + """</a>
      <a class="btn btn--ghost btn--lg" href="approach.html">Our strategy</a>
    </div>
    <p class="cta-band__fine">This page is not an offer to sell securities. Offers are made only through definitive offering documents to verified accredited investors.</p>
  </div>
</section>
"""

FOOTER = """
</main>

<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <a class="brand" href="index.html">""" + BRAND_SVG + """
          <span class="brand__text"><span class="brand__name">Valeward</span><span class="brand__sub">Capital</span></span>
        </a>
        <p class="footer__tag">Private multifamily investment.</p>
        <p class="footer__addr">[Street Address]<br>[City, ST ZIP]<br>
          <a href="tel:+10000000000">(000) 000&#8209;0000</a><br>
          <a href="mailto:investors@valewardcapital.com">investors@valewardcapital.com</a></p>
      </div>
      <div>
        <h4>Firm</h4>
        <ul>
          <li><a href="approach.html">Investment approach</a></li>
          <li><a href="portfolio.html">Portfolio</a></li>
          <li><a href="about.html">Team</a></li>
          <li><a href="insights.html">Insights</a></li>
        </ul>
      </div>
      <div>
        <h4>Investors</h4>
        <ul>
          <li><a href="invest.html">Speak with our team</a></li>
          <li><a href="investor-experience.html">The investor experience</a></li>
          <li><a href="why-multifamily.html">Why multifamily</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="https://portal.valewardcapital.com" rel="nofollow">Investor login</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="disclosures.html">Disclosures</a></li>
          <li><a href="disclosures.html#accredited">Accredited investor definition</a></li>
          <li><a href="privacy.html">Privacy policy</a></li>
          <li><a href="privacy.html#terms">Terms of use</a></li>
        </ul>
      </div>
    </div>

    <div class="footer__legal">
      <p><b>Important disclosures.</b> Valeward Capital LLC is a real estate sponsor, not a registered investment
        adviser, broker-dealer or tax adviser. Nothing on this website is investment, legal or tax advice, an offer
        to sell, or a solicitation of an offer to buy any security. Offers are made solely through a confidential
        private placement memorandum and definitive offering documents, only to verified accredited investors as
        defined in Rule 501(a) of Regulation D, and only in jurisdictions where such offers are permitted.</p>
      <p>Private real estate investments are speculative, illiquid and involve substantial risk, including the
        complete loss of principal. There is no public market for these interests and none is expected to develop.
        Targeted returns, distributions and hold periods are objectives only, based on assumptions that may prove
        incorrect; they are not guarantees, projections or predictions of results. Past performance is not
        indicative of future results. Any performance shown is historical, may be unaudited, and reflects specific
        assets that may not be representative of the portfolio as a whole. Prospective investors should consult
        their own legal, tax and financial advisers before investing.</p>
      <p><i>Site figures, properties, personnel and testimonials shown here are illustrative placeholders for design
        review and must be replaced with verified, documented information before this site is published.</i></p>
    </div>

    <div class="footer__bar">
      <span>&copy; <span data-year>2026</span> Valeward Capital LLC. All rights reserved.</span>
      <span>Website by LeadTide</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js?v=20260826192605"></script>
<script src="assets/js/agent.js?v=20260826192605" defer></script>
</body>
</html>
"""

# ==========================================================================
#  PAGES
# ==========================================================================
PAGES = []

# ---------------------------------------------------------------- APPROACH
PAGES.append({
    "slug": "approach.html", "nav_label": "Approach", "active": "approach.html",
    "title": "Investment Approach | Valeward Capital Multifamily",
    "desc": "Valeward Capital acquisition criteria, a return model you can adjust, and the migration patterns behind our Sun Belt multifamily markets.",
    "h1": "Investment approach",
    "lede": "Valeward acquires established apartment communities in growing secondary markets, finances them conservatively and improves them through operations. The approach is deliberately unexceptional; consistency of process is the source of the return.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Current acquisition criteria</h2>
      <p class="lede">A documented mandate is a discipline mechanism. Its purpose is to prevent a capable team from reasoning its way into an unsuitable acquisition in a competitive market.</p>
    </div>
    <div class="criteria" data-stagger>
      <div class="criterion reveal">
        <span class="criterion__value">150&ndash;400</span>
        <span class="criterion__label">Units per community</span>
        <p>1985&ndash;2005 vintage, Class&nbsp;B garden or mid-rise.</p>
      </div>
      <div class="criterion reveal">
        <span class="criterion__value">1&ndash;2%</span>
        <span class="criterion__label">Population growth, YoY</span>
        <p>Sun Belt submarkets compounding ahead of the national average year on year.</p>
      </div>
      <div class="criterion reveal">
        <span class="criterion__value">20&ndash;35%</span>
        <span class="criterion__label">Rent discount</span>
        <p>Below competing new construction within a three-mile radius.</p>
      </div>
      <div class="criterion reveal">
        <span class="criterion__value">3.5x</span>
        <span class="criterion__label">Income to rent</span>
        <p>Minimum median household income measured against the in-place rent.</p>
      </div>
      <div class="criterion reveal">
        <span class="criterion__value">Identifiable</span>
        <span class="criterion__label">Cause of underperformance</span>
        <p>Deferred maintenance, inadequate management or below-market leases.</p>
      </div>
      <div class="criterion reveal">
        <span class="criterion__value">Declining</span>
        <span class="criterion__label">Forward supply</span>
        <p>New supply as a share of stock falls after the current delivery wave.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2" id="model">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Model a position</h2>
      <p class="lede">Move the commitment and the hold period to see the range our stated targets imply. These are hypothetical illustrations of targets, not a projection of any particular offering, and not a promise of results.</p>
    </div>

    <div class="calc reveal">
      <div class="calc__controls">
        <div class="calc__field">
          <label class="calc__label" for="calc-amount">Commitment</label>
          <output class="calc__value" id="calc-amount-out" for="calc-amount">$250,000</output>
          <input class="calc__slider" id="calc-amount" type="range" min="50000" max="1000000" step="25000" value="250000" aria-describedby="calc-amount-out">
          <div class="calc__scale"><span>$50,000</span><span>$1,000,000</span></div>
        </div>

        <div class="calc__field">
          <label class="calc__label" for="calc-years">Hold period</label>
          <output class="calc__value" id="calc-years-out" for="calc-years">5 years</output>
          <input class="calc__slider" id="calc-years" type="range" min="5" max="7" step="1" value="5" aria-describedby="calc-years-out">
          <div class="calc__scale"><span>5 years</span><span>7 years</span></div>
        </div>

        <p class="calc__assump">Modelled on the targets stated across this site: a <b>7&ndash;10%</b> annual cash distribution and a <b>15&ndash;20%</b> blended annual rate of return. Every figure opposite is derived from those two ranges.</p>
      </div>

      <div class="calc__results" aria-live="polite">
        <div class="calc__row">
          <span class="calc__row-label">Cash distributed over the hold</span>
          <span class="calc__row-value" id="out-cash">&mdash;</span>
        </div>
        <div class="calc__row">
          <span class="calc__row-label">Implied equity multiple</span>
          <span class="calc__row-value" id="out-multiple">&mdash;</span>
        </div>
        <div class="calc__row">
          <span class="calc__row-label">Total profit</span>
          <span class="calc__row-value" id="out-profit">&mdash;</span>
        </div>
        <div class="calc__row calc__row--total">
          <span class="calc__row-label">Total value at exit</span>
          <span class="calc__row-value" id="out-total">&mdash;</span>
        </div>
      </div>
    </div>

    <p class="disclosure-inline">
      This tool is illustrative only. It applies a fixed set of target assumptions to the figures you enter and
      does not model any specific asset, its debt, its fees, its tax treatment or its timing of cash flows.
      Outputs are hypothetical, are not projections, forecasts or guarantees, and no investor should rely on them.
      Actual results will differ and may be materially worse, including the loss of the entire investment.
      Targeted returns are objectives only. Past performance is not indicative of future results.
    </p>
  </div>
</section>

<section class="section section--ink grain" id="markets">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Where the households are going</h2>
      <p class="lede">We buy where population is arriving before the price reflects it. The map shows net domestic migration by state; the arcs show the dominant flows. Select any state to read it.</p>
    </div>

    <div class="migration reveal" data-migration>
      <div>
        <div class="migration__mapwrap">
          <svg class="migration__map" viewBox="-6 -6 562 412" role="img"
               aria-label="Tile-grid map of the United States showing net domestic migration by state, with arcs marking dominant flows from high-cost coastal states to the Sun Belt."></svg>
        </div>
        <p class="migration__hint">Scroll the map sideways, then tap any state.</p>
        <div class="migration__legend">
          <span><i class="migration__swatch" style="background:rgba(184,135,59,.95)"></i>Net in-migration</span>
          <span><i class="migration__swatch" style="background:rgba(90,67,102,.8)"></i>Net out-migration</span>
          <span><i class="migration__swatch" style="background:var(--gold-lt);border-radius:999px;width:8px;height:8px"></i>Dominant flow</span>
        </div>
      </div>

      <div class="migration__panel">
        <p class="migration__state" data-mig-name>Texas</p>
        <span class="migration__net is-gain" data-mig-net>+125k</span>
        <span class="migration__net-lbl">Net domestic migration, latest full year</span>
        <p class="migration__note" data-mig-note>Net domestic in-migration.</p>
        <span class="migration__flag" data-mig-flag>Valeward operates here</span>

        <div class="migration__rank">
          <h4>Largest net gains</h4>
          <ul data-mig-rank></ul>
        </div>
      </div>
    </div>

    <p class="disclosure-inline">
      Migration figures shown are illustrative placeholders for design review and must be replaced with cited,
      dated figures before publication [source: U.S. Census Bureau, State-to-State Migration Flows, YYYY].
      Population movement is one input among many and does not predict the performance of any asset or market.
    </p>
  </div>
</section>

"""})

# --------------------------------------------------------------- PORTFOLIO
PAGES.append({
    "slug": "portfolio.html", "nav_label": "Portfolio", "active": "portfolio.html",
    "title": "Portfolio & Track Record | Valeward Capital Multifamily Assets",
    "desc": "The Valeward Capital apartment portfolio and realized results, including full-cycle returns and a review of an asset that performed below plan.",
    "h1": "Portfolio and realized results",
    "lede": "A record constitutes evidence only where it includes the outcomes a sponsor would prefer not to publish. Both underperforming assets are disclosed below alongside the realized results.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container">
    <div class="stat-row reveal">
      <div class="stat"><span class="stat__num num" data-count="312" data-prefix="$" data-suffix="M">$312M</span><span class="stat__label">Assets under management</span></div>
      <div class="stat"><span class="stat__num num" data-count="4180">4,180</span><span class="stat__label">Apartment homes</span></div>
      <div class="stat"><span class="stat__num num" data-count="9">9</span><span class="stat__label">Assets acquired since 2016</span></div>
      <div class="stat"><span class="stat__num num" data-count="0">0</span><span class="stat__label">Capital calls issued</span></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Assets under management</h2>
    </div>
    <div class="grid g-3" data-stagger>
      <article class="property reveal">
        <div class="property__img"><span class="property__tag">Operating</span>""" + photo("scene-facade", "property-2.jpg", "The Marlowe, Chattanooga TN") + """</div>
        <div class="property__body">
          <p class="property__meta">Chattanooga, TN &middot; 2004 vintage &middot; Acquired 2022</p>
          <h3 class="h3">The Marlowe</h3>
          <p class="small" style="margin-top:.5rem">Interior renovation programme 58% complete. Achieved premium is running $19 per unit above underwriting.</p>
          <div class="property__facts">
            <div class="property__fact"><b>312</b><span>Units</span></div>
            <div class="property__fact"><b>94%</b><span>Occupied</span></div>
            <div class="property__fact"><b>7.4%</b><span>Current CoC</span></div>
          </div>
        </div>
      </article>
      <article class="property reveal">
        <div class="property__img"><span class="property__tag">Operating</span>""" + photo("scene-facade", "property-3.jpg", "Cardinal Row, Huntsville AL") + """</div>
        <div class="property__body">
          <p class="property__meta">Huntsville, AL &middot; 2001 vintage &middot; Acquired 2021</p>
          <h3 class="h3">Cardinal Row</h3>
          <p class="small" style="margin-top:.5rem">Property management replaced in month four. Delinquency reduced from 6.1% to 1.8% within two quarters.</p>
          <div class="property__facts">
            <div class="property__fact"><b>276</b><span>Units</span></div>
            <div class="property__fact"><b>96%</b><span>Occupied</span></div>
            <div class="property__fact"><b>182</b><span>Renovated</span></div>
          </div>
        </div>
      </article>
      <article class="property reveal">
        <div class="property__img"><span class="property__tag">Operating</span>""" + photo("scene-facade", "property-4.jpg", "Ridgeline Commons, Greenville SC") + """</div>
        <div class="property__body">
          <p class="property__meta">Greenville, SC &middot; 1999 vintage &middot; Acquired 2021</p>
          <h3 class="h3">Ridgeline Commons</h3>
          <p class="small" style="margin-top:.5rem">Distributions suspended for two quarters in 2023 following a 61% insurance renewal; resumed Q3 2024. Asset review below.</p>
          <div class="property__facts">
            <div class="property__fact"><b>214</b><span>Units</span></div>
            <div class="property__fact"><b>93%</b><span>Occupied</span></div>
            <div class="property__fact"><b>4.1%</b><span>Current CoC</span></div>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Realized investments</h2>
      <p class="lede">Four assets acquired, repositioned and disposed of. Returns are stated net of all fees, at the investor level.</p>
    </div>
    <div class="table-wrap reveal">
      <table>
        <caption class="sr-only">Realized full-cycle investments</caption>
        <thead>
          <tr>
            <th scope="col">Asset</th><th scope="col">Market</th><th scope="col">Units</th>
            <th scope="col">Held</th><th scope="col" class="right">Equity multiple</th>
            <th scope="col" class="right">Net IRR</th><th scope="col">Against plan</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><b>Bellhaven Park</b></td><td>Greenville, SC</td><td class="num">248</td><td>2019&ndash;2023</td><td class="right num">2.1x</td><td class="right num">19.4%</td><td><span class="pill pill--good">Above plan</span></td></tr>
          <tr><td><b>Wexford Trace</b></td><td>Columbia, SC</td><td class="num">184</td><td>2018&ndash;2023</td><td class="right num">1.9x</td><td class="right num">16.1%</td><td><span class="pill pill--good">On plan</span></td></tr>
          <tr><td><b>Halstead Mill</b></td><td>Chattanooga, TN</td><td class="num">206</td><td>2016&ndash;2022</td><td class="right num">2.3x</td><td class="right num">21.0%</td><td><span class="pill pill--good">Above plan</span></td></tr>
          <tr><td><b>Ferrand Court</b></td><td>Augusta, GA</td><td class="num">160</td><td>2019&ndash;2025</td><td class="right num">1.4x</td><td class="right num">7.2%</td><td><span class="pill pill--hold">Below plan</span></td></tr>
        </tbody>
      </table>
    </div>
    <p class="disclosure-inline">Past performance is not indicative of future results. Figures are net of fees and reflect only realized assets; currently operating assets are excluded because their outcomes are not yet determined, and their eventual results may be materially worse. Ferrand Court returned investor capital but under-delivered against its underwritten plan after a 2020&ndash;21 lease-up disruption. Figures shown are illustrative pending final verified reporting.</p>
  </div>
</section>

<section class="section section--ink grain" id="ridgeline">
  <div class="container narrow">
    <div class="reveal">
      <h2 class="h2">Ridgeline Commons: asset review</h2>
      <div class="prose" style="margin-top:var(--s-4)">
        <p style="color:var(--muted-dark)"><b style="color:var(--paper)">The plan.</b> Acquired in 2021 at $131,000 per unit with fixed-rate agency debt to 2031. Renovate 140 of 214 units, lift rents $150, hold five years.</p>
        <p style="color:var(--muted-dark)"><b style="color:var(--paper)">Outcome.</b> The 2023 insurance renewal was priced 61% above the prior year, approximately $310 per unit annually, and payroll ran 11% ahead of plan in a constrained staffing market. Net operating income closed the year 14% below underwriting.</p>
        <p style="color:var(--muted-dark)"><b style="color:var(--paper)">Response.</b> Distributions were suspended for two quarters rather than funded from reserves. Investors were notified in writing nine days after the decision, with the revised model attached. Insurance was moved to a master programme across three assets, the property management company was replaced, and the renovation schedule was extended to preserve cash. Distributions resumed in Q3 2024 at a reduced rate. No capital call was issued.</p>
        <p style="color:var(--muted-dark)"><b style="color:var(--paper)">Changes adopted.</b> Insurance is now underwritten at quoted renewal rather than trailing cost across all transactions, and the reserve minimum was increased from nine to twelve months of debt service. Both changes derive from this asset.</p>
      </div>
      <div class="callout" style="margin-top:var(--s-5)">
        <p class="small">The complete investor memorandum, including the original and revised models, is available in the diligence room to investors with access.</p>
      </div>
    </div>
  </div>
</section>
"""})

# --------------------------------------------------------- WHY MULTIFAMILY
PAGES.append({
    "slug": "why-multifamily.html", "nav_label": "Why Multifamily", "active": "why-multifamily.html",
    "crumb": "Why multifamily",
    "title": "Why Invest in Multifamily Real Estate? | Valeward Capital",
    "desc": "How multifamily investments generate returns for accredited investors, the conditions supporting the current opportunity, and the principal risks involved.",
    "h1": "The case for multifamily",
    "lede": "An assessment of the asset class: the mechanics by which returns are generated, the conditions supporting the current opportunity, and the four principal ways in which an investment of this type loses money.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container">
    <div class="split split--l">
      <div class="reveal">
        <h2 class="h2">Demand characteristics</h2>
        <div class="prose" style="margin-top:var(--s-4)">
          <p>Most commercial property types depend on a discretionary decision. An office requires an occupier to elect to lease space; a retail centre requires consumers to elect to shop there. Residential demand derives from a non-discretionary requirement.</p>
          <p>This underpins the thesis. Apartment communities have historically demonstrated lower income volatility through recessionary periods than most other commercial real estate. Leases reset annually, allowing rents to track inflation rather than remaining fixed below it for an extended term.</p>
          <p>None of this constitutes a guarantee. Occupancy declines, operating expenses rise and submarkets over-build. The distinction is that the underlying demand is closer to a necessity than that supporting any other institutional property type.</p>
        </div>
      </div>
      <div class="reveal-arch">
        <div class="arch-figure">
          <div class="arch-figure__frame" style="max-width:400px">""" + photo("scene-facade", "why-1.jpg", "Workforce apartment community at dusk", lazy=False) + """</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Return drivers</h2>
      <p class="lede">An understanding of these mechanics clarifies why an identical asset may represent either a sound investment or a permanent loss, determined principally by the basis and structure at acquisition.</p>
    </div>
    <div class="grid g-4" data-stagger>
      <div class="card reveal">
        <p class="card__idx">01</p>
        <h3 class="h3">Cash flow</h3>
        <p>Rental income less operating costs and debt service. The residual is distributed. This is the only driver observable quarterly, and consequently the one that dominates investor perception of an asset.</p>
      </div>
      <div class="card reveal">
        <p class="card__idx">02</p>
        <h3 class="h3">Principal paydown</h3>
        <p>Rental income services the loan, and amortization converts a meaningful proportion of debt into equity over a five-year hold without further capital contribution.</p>
      </div>
      <div class="card reveal">
        <p class="card__idx">03</p>
        <h3 class="h3">Forced appreciation</h3>
        <p>Commercial property is valued on income. An additional $100 of monthly rent across 250 units represents approximately $300,000 of annual income and, at a 5.5% capitalization rate, some $5.4M of value.</p>
      </div>
      <div class="card reveal">
        <p class="card__idx">04</p>
        <h3 class="h3">Tax treatment</h3>
        <p>Depreciation, accelerated through cost segregation, produces passive losses reported on a Schedule K&#8209;1, frequently offsetting distributions received in the same period.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink grain">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Three conditions supporting the current opportunity</h2>
    </div>
    <div class="grid g-3" data-stagger>
      <div class="card card--flat reveal">
        <h3 class="h3">The supply cycle is turning</h3>
        <p>The 2022&ndash;2024 construction cycle is delivering into 2025&ndash;2026, and starts have declined materially since. Assets acquired now are generally held through the period in which new deliveries recede.</p>
      </div>
      <div class="card card--flat reveal">
        <h3 class="h3">Ownership is transferring</h3>
        <p>Sponsors that employed floating-rate debt in 2021 face maturities they are unable to refinance at the original basis. This produces motivated vendors for acquirers whose own capital structures remain intact.</p>
      </div>
      <div class="card card--flat reveal">
        <h3 class="h3">Household formation favours rental demand</h3>
        <p>Elevated mortgage rates and residential prices extend the period for which prospective purchasers remain renters. This is adverse for those households and supportive of apartment demand; we state the mechanism directly rather than obscure it.</p>
      </div>
    </div>
    <p class="disclosure-inline">Market observations reflect our views as of the date of publication, are not research or investment advice, and may prove incorrect. Conditions can change quickly and without notice.</p>
  </div>
</section>

"""})

# ----------------------------------------------------- INVESTOR EXPERIENCE
PAGES.append({
    "slug": "investor-experience.html", "nav_label": "For Investors", "active": "investor-experience.html",
    "crumb": "The investor experience",
    "title": "The Investor Experience | Valeward Capital",
    "desc": "The Valeward investor relationship in detail: subscription process, quarterly distributions, reporting standards and Schedule K-1 delivery by April 15.",
    "h1": "The investor experience",
    "lede": "Sponsors describe the transaction; few describe the five years that follow it. Set out below is every stage of the relationship, in sequence, together with the standards to which we hold ourselves.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">From access request to funding</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="step__n">01</div><div class="step__body"><h3 class="h3">Access request</h3><p>A brief form. No financial documentation is requested, no credit enquiry is made and no obligation arises. We ask about objectives and liquidity requirements because we would rather decline a subscription than accept capital an investor may need returned.</p></div></div>
      <div class="step reveal"><div class="step__n">02</div><div class="step__body"><h3 class="h3">Introductory call</h3><p>Thirty minutes with a principal. The discussion covers objectives, horizon and prior experience of private investments. Where Valeward is not an appropriate fit, we say so during that call.</p></div></div>
      <div class="step reveal"><div class="step__n">03</div><div class="step__body"><h3 class="h3">Accreditation verification</h3><p>Conducted by an independent third-party provider. Tax returns and account statements are furnished to that provider and not to Valeward. Verification remains valid for twelve months.</p></div></div>
      <div class="step reveal"><div class="step__n">04</div><div class="step__body"><h3 class="h3">Diligence room access</h3><p>On release of an offering, investors receive the complete file: the underwriting model with editable assumptions, rent roll, trailing twelve-month financials, property condition assessment, third-party market study, debt term sheet, insurance quotations and the private placement memorandum.</p></div></div>
      <div class="step reveal"><div class="step__n">05</div><div class="step__body"><h3 class="h3">Allocation and funding</h3><p>An allocation may be reserved without obligation while diligence is completed. Subscription documents are executed electronically and funded by wire or ACH, with written confirmation issued the same day.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--ink grain">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h2">Standards we hold ourselves to</h2>
      <p class="lede">These are operating standards rather than aspirations. Where one is not met, investors are informed by us before they identify it themselves.</p>
    </div>
    <div class="grid g-2" data-stagger>
      <div class="card card--flat reveal"><h3 class="h3">Quarterly distributions</h3><p>Remitted by ACH on the fifteenth of the month following each quarter close. Where a distribution is to be reduced or suspended, written notice setting out the reason is issued before the payment date.</p></div>
      <div class="card card--flat reveal"><h3 class="h3">Quarterly asset report</h3><p>Occupancy, delinquency, capital works completed and actual performance against underwriting, together with a statement of any variance running behind plan. That final section appears in every report.</p></div>
      <div class="card card--flat reveal"><h3 class="h3">Schedule K&#8209;1 by April 15</h3><p>Reflected in the engagement terms with our accountants. Where a K&#8209;1 will be delayed for reasons outside our control, investors receive a specific delivery date before April 1.</p></div>
      <div class="card card--flat reveal"><h3 class="h3">Annual audited financials</h3><p>Fund-level financials audited by an independent firm and delivered to every investor, alongside a summary of any material findings.</p></div>
      <div class="card card--flat reveal"><h3 class="h3">A named point of contact</h3><p>Investors hold the direct line and email address of the principal responsible for the asset, rather than a general enquiries address or a rotating relationship manager.</p></div>
      <div class="card card--flat reveal"><h3 class="h3">Material event notice within ten days</h3><p>Refinancing, a change to distributions, a change of management, litigation, material casualty or a purchase offer: investors are notified in writing within ten business days.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split split--l">
      <div class="reveal">
        <h2 class="h2">Tax treatment</h2>
        <div class="prose" style="margin-top:var(--s-4)">
          <p>Investors receive a Schedule K&#8209;1 for each offering, reporting their share of income, loss and depreciation. As a cost segregation study is commissioned on every acquisition, most investors report a passive loss in the first year notwithstanding distributions received in the same period.</p>
          <p>Such losses are generally passive in character and therefore offset passive income rather than employment income, unless the investor or their spouse qualifies for real estate professional status. Whether that applies is a question for the investor&rsquo;s own tax adviser.</p>
          <p>Where an investment is made through a self-directed IRA or solo 401(k) plan, leveraged real estate may generate unrelated business income tax. This is identified before subscription rather than discovered at filing.</p>
        </div>
        <div class="callout" style="margin-top:var(--s-4)">
          <p class="small"><b>Valeward does not provide tax advice.</b> Nothing set out here constitutes a recommendation in respect of any individual circumstance. Investors should review their Schedule K&#8209;1 and this material with a qualified accountant.</p>
        </div>
      </div>
      <div class="reveal">
        <div class="card">
          <h3 class="h3">Accepted investment vehicles</h3>
          <ul class="prose" style="margin-top:var(--s-3)">
            <li>Individual and joint accounts</li>
            <li>Revocable and irrevocable trusts</li>
            <li>LLCs, partnerships and corporations</li>
            <li>Self-directed IRAs (traditional and Roth)</li>
            <li>Solo 401(k) plans</li>
            <li>Family offices and registered advisers on behalf of clients</li>
          </ul>
          <div class="card__foot"><a class="link-arrow" href="invest.html">Speak with our team """ + ARROW + """</a></div>
        </div>
      </div>
    </div>
  </div>
</section>
"""})

# ------------------------------------------------------------------- ABOUT
PAGES.append({
    "slug": "about.html", "nav_label": "About", "active": "about.html",
    "title": "About Valeward Capital | Carla Kiernan",
    "desc": "Carla Kiernan and the origins of Valeward Capital: how two market cycles shaped the way the firm underwrites, finances and reports on multifamily assets.",
    "h1": "About Valeward",
    "lede": "Valeward was established to apply institutional underwriting and reporting standards to a small portfolio of workforce apartment communities, on behalf of a limited number of private investors.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container narrow">
    <div class="reveal prose">
      <h2 class="h2">Origins</h2>
      <p style="margin-top:var(--s-4)">The first apartment community underwritten by the firm&rsquo;s founder closed in 2007. Within eighteen months, well-capitalised operators were losing assets that remained fully occupied and cash-generative, on account of how those assets had been financed rather than how they performed.</p>
      <p>That experience produced a particular set of priorities. We will pay a somewhat higher price for a better basis. We give limited weight to rent growth assumptions. We are reluctant to reduce reserves. And we will not accept a loan structure capable of removing a performing asset from the partnership.</p>
      <p>Valeward was founded in 2016 to pursue a single strategy, in one asset class, across a small number of markets that can be reached within a day. We have declined capital that would have required the firm to acquire faster than it can underwrite.</p>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="container">
    <div class="split split--r">
      <div class="reveal-arch">
        <div class="arch-figure">
          <div class="arch-figure__frame" style="max-width:420px">
            <div class="photo-slot">
              <svg width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><use href="#scene-portrait"/></svg>
              <img src="assets/img/carla-kiernan.jpg" alt="Carla Kiernan of Valeward Capital" decoding="async">
            </div>
          </div>
        </div>
      </div>

      <div class="reveal">
        <h2 class="h2">Carla Kiernan</h2>
        <p class="person__role" style="margin:var(--s-3) 0 var(--s-4)">[Title]</p>

        <p class="lede">&ldquo;Valeward exists to give private investors the kind of ownership I spent
          my career arranging for institutions &mdash; the same assets, the same underwriting discipline,
          and reporting written for people who intend to read it.&rdquo;</p>

        <div class="prose" style="margin-top:var(--s-4)">
          <p>Carla founded Valeward Capital in 2016, after [number] years in [background]. She has
            [led / overseen] [scope of prior responsibility], and has underwritten multifamily assets
            through two complete market cycles.</p>
          <p>She sets the acquisition criteria, signs off on every financing decision, and is the point
            of contact for investors in [markets]. She is personally committed to every Valeward
            offering on the same terms as every other investor. [Credential], [University].</p>
        </div>

        <div class="person__links" style="margin-top:var(--s-5)">
          <a href="mailto:carla@valewardcapital.com">Email</a>
        </div>
      </div>
    </div>
  </div>
</section>

"""})

# --------------------------------------------------------------- INSIGHTS
PAGES.append({
    "slug": "insights.html", "nav_label": "Insights", "active": "",
    "crumb": "Insights",
    "title": "Insights | Multifamily Investing Analysis from Valeward Capital",
    "desc": "Analysis of multifamily underwriting, Sun Belt apartment markets, passive real estate taxation and sponsor due diligence for accredited investors.",
    "h1": "Insights",
    "lede": "Written for investors who wish to understand the mechanics of the asset class. Each piece addresses a specific question in underwriting, taxation, market analysis or sponsor diligence.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container">
    <p class="lede reveal" style="margin-bottom:var(--s-4)">Analysis is published to our investor list first. The pieces below are in preparation &mdash; ask us for any of them directly.</p>
    <div class="tag-row reveal" style="margin-bottom:var(--s-5)">
      <span class="tag">All</span><span class="tag">Underwriting</span><span class="tag">Markets</span>
      <span class="tag">Tax</span><span class="tag">Due diligence</span><span class="tag">Letters to investors</span>
    </div>
    <div class="grid g-3" data-stagger>
      <article class="card reveal">
        <p class="card__idx">Due diligence</p>
        <h2 class="h3">Four debt questions that anticipated the 2023 distribution suspensions</h2>
        <p>Rate, term, structure and treatment at maturity. These four enquiries would have identified the majority of offerings that subsequently suspended distributions.</p>
        <div class="card__foot"><span class="xs">9 min read</span></div>
      </article>
      <article class="card reveal">
        <p class="card__idx">Tax</p>
        <h2 class="h3">Cost segregation: mechanics and limitations</h2>
        <p>How a study separates one depreciation schedule into four, why it produces a first-year passive loss, and the recapture treatment applicable at disposition.</p>
        <div class="card__foot"><span class="xs">11 min read</span></div>
      </article>
      <article class="card reveal">
        <p class="card__idx">Markets</p>
        <h2 class="h3">Assessing a submarket supply pipeline</h2>
        <p>Permits, starts and deliveries are distinct measures. Conflating them is how investors acquire into a delivery cycle they believe has already concluded.</p>
        <div class="card__foot"><span class="xs">8 min read</span></div>
      </article>
      <article class="card reveal">
        <p class="card__idx">Underwriting</p>
        <h2 class="h3">Underwriting insurance at quotation rather than trailing cost</h2>
        <p>The line item that impaired Sun Belt multifamily returns more materially than interest rates in 2023, and the resulting change to our model.</p>
        <div class="card__foot"><span class="xs">7 min read</span></div>
      </article>
      <article class="card reveal">
        <p class="card__idx">Letters to investors</p>
        <h2 class="h3">Q4 letter: acquisitions, declined transactions and rationale</h2>
        <p>Eleven assets underwritten, two offers submitted, one completed. The reasoning behind the nine declined is generally more instructive than that behind the one acquired.</p>
        <div class="card__foot"><span class="xs">6 min read</span></div>
      </article>
      <article class="card reveal">
        <p class="card__idx">Due diligence</p>
        <h2 class="h3">The contents of a complete diligence file</h2>
        <p>A sponsor&rsquo;s willingness to provide the underwriting model with editable assumptions remains the most efficient assessment available to a prospective limited partner.</p>
        <div class="card__foot"><span class="xs">10 min read</span></div>
      </article>
    </div>
    <p class="disclosure-inline">Article titles shown are illustrative placeholders for design review. Insights are general educational material, reflect our views as at the date of publication, and do not constitute investment, legal or tax advice.</p>
  </div>
</section>
"""})

# ------------------------------------------------------------------ FAQ
PAGES.append({
    "slug": "faq.html", "nav_label": "FAQ", "active": "",
    "crumb": "FAQ",
    "title": "Investor FAQ | Valeward Capital Multifamily Investing",
    "desc": "Minimums, accreditation, hold periods, fees, distributions, K-1 timing, retirement accounts and risk, addressed for prospective Valeward investors.",
    "h1": "Frequently asked questions",
    "lede": "Questions not addressed below may be directed to our investor relations desk. We respond to every enquiry in writing, including those concerning underperformance.",
    "cta": True,
    "body": """
<section class="section">
  <div class="container narrow">

    <h2 class="h2 reveal" style="margin-bottom:var(--s-4)">Getting started</h2>
    <div class="accordion reveal" style="margin-bottom:var(--s-7)">
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q1" id="qb1">What is the minimum investment?</button>
        <div class="acc__panel" id="q1" role="region" aria-labelledby="qb1"><div class="acc__panel-inner"><p>The standard minimum is $50,000 per offering. A limited number of $25,000 allocations is reserved in each round for investors participating in a Valeward offering for the first time, permitting an initial commitment to be made before a larger allocation is considered.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q2" id="qb2">Do I need to be an accredited investor?</button>
        <div class="acc__panel" id="q2" role="region" aria-labelledby="qb2"><div class="acc__panel-inner"><p>Yes. Offerings are made under Rule 506(c) of Regulation D, which requires that every investor be verified as accredited. This generally means individual income above $200,000 (or $300,000 jointly) in each of the last two years, or net worth above $1M excluding a primary residence. Certain professional licences also qualify. See the <a href="disclosures.html#accredited">full definition</a>.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q3" id="qb3">How does verification work, and who sees my documents?</button>
        <div class="acc__panel" id="q3" role="region" aria-labelledby="qb3"><div class="acc__panel-inner"><p>An independent third-party provider reviews the documentation and issues a letter confirming status. Tax returns and account statements are furnished to that provider rather than to Valeward; we receive the letter only. Verification remains valid for twelve months.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q4" id="qb4">Can I invest through an IRA, trust or LLC?</button>
        <div class="acc__panel" id="q4" role="region" aria-labelledby="qb4"><div class="acc__panel-inner"><p>Yes. Self-directed IRAs, solo 401(k) plans, trusts, limited liability companies and partnerships are accepted, and we have worked with the principal custodians. Leveraged real estate held within a retirement account may generate unrelated business income tax; this is identified before subscription and should be reviewed with a tax adviser.</p></div></div></div>
    </div>

    <h2 class="h2 reveal" style="margin-bottom:var(--s-4)">Money and returns</h2>
    <div class="accordion reveal" style="margin-bottom:var(--s-7)">
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q5" id="qb5">What returns do you target?</button>
        <div class="acc__panel" id="q5" role="region" aria-labelledby="qb5"><div class="acc__panel-inner"><p>Offerings typically target a 7&ndash;10% annualized cash distribution, a 1.8&ndash;2.2x equity multiple over a five to seven year hold, and a 15&ndash;20% blended annual rate of return. These are objectives derived from underwriting rather than undertakings. Realized results have ranged from 1.4x to 2.3x and may be materially lower, including a total loss of capital.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q6" id="qb6">When and how are distributions paid?</button>
        <div class="acc__panel" id="q6" role="region" aria-labelledby="qb6"><div class="acc__panel-inner"><p>Quarterly, by ACH, on the fifteenth of the month following each quarter close. New investments generally commence distributions after the first full quarter of ownership. Where a distribution is to be reduced or suspended, written notice setting out the reason is issued before the payment date.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q7" id="qb7">Exactly how do you get paid?</button>
        <div class="acc__panel" id="q7" role="region" aria-labelledby="qb7"><div class="acc__panel-inner"><p>A 1.5% acquisition fee at closing, a 2% annual asset management fee on invested equity, and 25% of profits payable only after the return of all investor capital together with an 8% preferred return. There is no disposition fee, no refinancing fee and no fee on transactions that do not complete. The complete schedule is set out in the private placement memorandum for each offering.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q8" id="qb8">Could I lose money?</button>
        <div class="acc__panel" id="q8" role="region" aria-labelledby="qb8"><div class="acc__panel-inner"><p>Yes, including the entire investment. These are speculative, illiquid and unguaranteed securities. Lenders rank ahead of equity holders in any adverse outcome. Our structure is designed to reduce the likelihood of a forced disposition, but no structure eliminates the risk of loss.</p></div></div></div>
    </div>

    <h2 class="h2 reveal" style="margin-bottom:var(--s-4)">Time, tax and exit</h2>
    <div class="accordion reveal" style="margin-bottom:var(--s-7)">
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q9" id="qb9">How long is my capital committed?</button>
        <div class="acc__panel" id="q9" role="region" aria-labelledby="qb9"><div class="acc__panel-inner"><p>The target hold period is five to seven years. There is no secondary market, no redemption right and no facility for early withdrawal. Where a disposition or refinancing returns capital earlier, that is an incidental outcome rather than a basis on which to subscribe. We decline subscriptions from investors who indicate they may require the capital before realization.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q10" id="qb10">When will I receive my K-1?</button>
        <div class="acc__panel" id="q10" role="region" aria-labelledby="qb10"><div class="acc__panel-inner"><p>By April 15. Where a Schedule K&#8209;1 will be delayed for reasons outside our control, investors receive a specific delivery date before April 1.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q11" id="qb11">Will I get a tax loss in year one?</button>
        <div class="acc__panel" id="q11" role="region" aria-labelledby="qb11"><div class="acc__panel-inner"><p>Most investors do, as a cost segregation study is commissioned on every acquisition. Such losses are generally passive in character and typically offset passive income rather than employment income. Whether they assist any particular investor is a question for that investor&rsquo;s accountant. Valeward does not provide tax advice.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q12" id="qb12">What happens at the end?</button>
        <div class="acc__panel" id="q12" role="region" aria-labelledby="qb12"><div class="acc__panel-inner"><p>The asset is sold or refinanced, capital and the investor&rsquo;s share of profits are returned, and a final Schedule K&#8209;1 is issued. Investors are notified when an asset is brought to market rather than after it is placed under contract, and receive the full disposition analysis.</p></div></div></div>
    </div>

    <h2 class="h2 reveal" style="margin-bottom:var(--s-4)">About the firm</h2>
    <div class="accordion reveal">
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q13" id="qb13">Have any of your deals gone badly?</button>
        <div class="acc__panel" id="q13" role="region" aria-labelledby="qb13"><div class="acc__panel-inner"><p>Yes. Ridgeline Commons suspended distributions for two quarters in 2023, and Ferrand Court returned capital at 1.4x against an underwritten 1.9x. Both are documented in full on the <a href="portfolio.html#ridgeline">portfolio page</a>, together with the changes adopted as a result.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q14" id="qb14">Do you invest your own money?</button>
        <div class="acc__panel" id="q14" role="region" aria-labelledby="qb14"><div class="acc__panel-inner"><p>Principals commit no less than 5% of every equity raise in cash, on terms identical to those of every other investor. Not contributed services and not a deferred fee: cash, remitted at closing.</p></div></div></div>
      <div class="acc"><button class="acc__btn" aria-expanded="false" aria-controls="q15" id="qb15">How often will I be contacted?</button>
        <div class="acc__panel" id="q15" role="region" aria-labelledby="qb15"><div class="acc__panel-inner"><p>No. Investors receive notice when an offering is available and a quarterly letter. We do not employ deadlines, scarcity messaging or automated follow-up campaigns, and you may unsubscribe at any time.</p></div></div></div>
    </div>

  </div>
</section>
"""})

# ----------------------------------------------------------------- INVEST
PAGES.append({
    "slug": "invest.html", "nav_label": "Speak with our team", "active": "",
    "crumb": "Speak with our team",
    "title": "Speak With Our Team | Valeward Capital",
    "desc": "Speak with the Valeward Capital team about multifamily offerings. Enquiries are reviewed within two business days and place you under no obligation.",
    "h1": "Speak with our team",
    "lede": "A short form, and a response within two business days. Joining the access list places you under no obligation and does not commit you to any offering.",
    "cta": False,
    "body": """
<section class="section">
  <div class="container">
    <div class="split split--r" style="align-items:start">

      <div class="reveal" style="position:sticky;top:120px">
        <h2 class="h2">Three stages,<br>no obligation</h2>
        <div class="steps" style="margin-top:var(--s-4)">
          <div class="step"><div class="step__n">01</div><div class="step__body"><h3 class="h3">Review</h3><p>A principal reviews every request personally. Where Valeward is not an appropriate fit for the objectives described, we say so on the first call.</p></div></div>
          <div class="step"><div class="step__n">02</div><div class="step__body"><h3 class="h3">Introductory call</h3><p>Thirty minutes, without a presentation. The discussion covers objectives, time horizon and prior experience of private investments.</p></div></div>
          <div class="step"><div class="step__n">03</div><div class="step__body"><h3 class="h3">Diligence room</h3><p>On release of an offering you receive the complete underwriting file, with two to three weeks in which to review it.</p></div></div>
        </div>
        <div class="callout" style="margin-top:var(--s-5)">
          <h3 class="h3">Direct contact</h3>
          <p class="small">Telephone <a href="tel:+10000000000"><b>(000) 000&#8209;0000</b></a> or email <a href="mailto:investors@valewardcapital.com"><b>investors@valewardcapital.com</b></a>. Both are answered by a principal or by investor relations.</p>
        </div>
      </div>

      <div class="reveal">
        <div class="form-card">
          <form class="form" data-form novalidate>
            <p class="form-note">Valeward offerings are available solely to verified accredited investors under Rule 506(c). This form does not request financial documentation and creates no obligation.</p>

            <div class="form-row">
              <div class="field">
                <label for="f-first">First name <span class="req">*</span></label>
                <input id="f-first" name="first" type="text" autocomplete="given-name" required>
                <span class="field__error">Enter your first name.</span>
              </div>
              <div class="field">
                <label for="f-last">Last name <span class="req">*</span></label>
                <input id="f-last" name="last" type="text" autocomplete="family-name" required>
                <span class="field__error">Enter your last name.</span>
              </div>
            </div>

            <div class="field">
              <label for="f-email">Email <span class="req">*</span></label>
              <input id="f-email" name="email" type="email" autocomplete="email" required>
              <span class="field__error">Enter a valid email address.</span>
            </div>

            <div class="field">
              <label for="f-phone">Phone</label>
              <input id="f-phone" name="phone" type="tel" autocomplete="tel">
              <span class="field__help">Optional. Used solely to arrange the introductory call.</span>
            </div>

            <div class="field">
              <label for="f-accred">Accredited investor status <span class="req">*</span></label>
              <select id="f-accred" name="accreditation" required>
                <option value="">Select the statement that applies</option>
                <option>Income above $200,000 individually (or $300,000 jointly) in each of the last two years</option>
                <option>Net worth above $1M, excluding a primary residence</option>
                <option>Holder of a Series 7, 65 or 82 licence in good standing</option>
                <option>Investing through a qualifying entity or trust</option>
                <option>Not accredited, or status uncertain</option>
              </select>
              <span class="field__error">Select the statement that applies to you.</span>
              <span class="field__help">Self-reported at this stage. Independent verification is completed later, prior to any subscription.</span>
            </div>

            <div class="field">
              <label for="f-amount">Allocation under consideration</label>
              <select id="f-amount" name="amount">
                <option value="">Prefer not to say</option>
                <option>$25,000 &ndash; $50,000</option>
                <option>$50,000 &ndash; $100,000</option>
                <option>$100,000 &ndash; $250,000</option>
                <option>$250,000 &ndash; $500,000</option>
                <option>Above $500,000</option>
              </select>
              <span class="field__help">Indicative only. No allocation is reserved and no commitment arises.</span>
            </div>

            <div class="field">
              <label for="f-timing">Anticipated timing</label>
              <select id="f-timing" name="timing">
                <option value="">Select</option>
                <option>The next offering</option>
                <option>Within six months</option>
                <option>Within twelve months</option>
                <option>Currently researching</option>
              </select>
            </div>

            <div class="field">
              <label for="f-notes">Additional context</label>
              <textarea id="f-notes" name="notes" rows="3" placeholder="A liquidity event, a pending property disposition, a 1031 deadline, or requirements arising from a previous investment."></textarea>
            </div>

            <label class="check">
              <input type="checkbox" name="consent" required>
              <span>I understand that this is not an offer to sell securities, that any investment would be speculative and illiquid with the risk of total loss, and I consent to being contacted by Valeward Capital. <span class="req">*</span></span>
            </label>

            <button class="btn btn--gold btn--lg" type="submit" style="width:100%">Speak with our team """ + ARROW + """</button>
            <p class="xs">Reviewed within two business days. You may unsubscribe from any communication at any time.</p>
          </form>

          <div class="form-success">
            <h3 class="h3">Request received.</h3>
            <p class="small" style="margin-top:var(--s-2)">A principal will review the request personally and respond within two business days.</p>
            <p class="small" style="margin-top:var(--s-3)">In the interim, the <a href="portfolio.html">realized track record</a> and the <a href="portfolio.html#ridgeline">review of the asset that underperformed</a> are the most informative material available.</p>
          </div>
        </div>

        <p class="disclosure-inline">This form is a demonstration and is not connected to a mail service or CRM. Prior to launch it must be connected to your CRM with server-side validation, spam control and a privacy-policy link, and data handling confirmed against the <a href="privacy.html">privacy policy</a>.</p>
      </div>

    </div>
  </div>
</section>
"""})

# ------------------------------------------------------------ DISCLOSURES
PAGES.append({
    "slug": "disclosures.html", "nav_label": "Disclosures", "active": "",
    "crumb": "Disclosures",
    "title": "Legal Disclosures | Valeward Capital",
    "desc": "Regulatory disclosures, accredited investor definition, forward-looking statement notice and risk disclosure for Valeward Capital offerings.",
    "h1": "Disclosures",
    "lede": "Regulatory, risk and performance disclosures applicable to Valeward Capital offerings. Where any provision requires clarification, our investor relations desk will provide it in writing.",
    "cta": False,
    "body": """
<section class="section">
  <div class="container narrow prose reveal">

    <h2 class="h2">Not an offer</h2>
    <p>This website is for informational purposes only. It is not an offer to sell, or the solicitation of an offer to buy, any security, nor is it investment, legal, accounting or tax advice. Any offer or solicitation will be made only through definitive offering documents, including a confidential private placement memorandum, an operating agreement and a subscription agreement, and only to verified accredited investors in jurisdictions where such an offer is permitted. In the event of any inconsistency between this website and those documents, the offering documents control.</p>

    <h2 class="h2" id="accredited">Accredited investor definition</h2>
    <p>Valeward offerings are made in reliance on Rule 506(c) of Regulation D under the Securities Act of 1933, which permits general solicitation provided that all purchasers are accredited investors whose status has been verified. An individual generally qualifies if they meet any of the following:</p>
    <ul>
      <li>Individual income exceeding $200,000, or joint income with a spouse or spousal equivalent exceeding $300,000, in each of the two most recent years, with a reasonable expectation of the same in the current year</li>
      <li>Individual or joint net worth exceeding $1,000,000, excluding the value of a primary residence</li>
      <li>Holding a Series 7, Series 65 or Series 82 licence in good standing</li>
      <li>Being a knowledgeable employee of the issuing private fund</li>
    </ul>
    <p>Entities may qualify on other bases, including total assets above $5,000,000, or where all equity owners are themselves accredited. Verification is performed by an independent third-party provider; Valeward does not retain investor financial documents. This summary is not exhaustive and does not replace the definition in Rule 501(a).</p>

    <h2 class="h2">Risk of loss</h2>
    <p>Private real estate investments are speculative and involve a high degree of risk, including the complete loss of invested capital. Risks include, without limitation: illiquidity and the absence of any secondary market; the use of leverage, which magnifies both gains and losses; rising interest rates, insurance costs and property taxes; declines in occupancy, rents or property values; construction and renovation cost overruns; casualty and uninsured losses; changes in law, zoning, rent regulation or tax treatment; concentration in a single asset class and a small number of geographic markets; and dependence on the sponsor's key personnel. Lenders and other creditors are repaid before equity investors in any adverse outcome. Investors must be able to bear the total loss of their investment.</p>

    <h2 class="h2">Forward-looking statements</h2>
    <p>This website contains forward-looking statements, including targeted returns, distributions, hold periods, business plans and market observations. These are based on assumptions about future events that are inherently uncertain and may prove incorrect. Words such as target, expect, anticipate, project, believe and intend identify such statements. No representation is made that any target will be achieved, and actual results may differ materially. Valeward undertakes no obligation to update forward-looking statements.</p>

    <h2 class="h2">Performance information</h2>
    <p>Any performance information presented is historical and is not indicative of future results. Realized results reflect specific assets sold in specific market conditions and may not be representative of the portfolio as a whole or of any future investment. Performance may be unaudited and is subject to revision. Returns shown net of fees reflect the deduction of acquisition, asset management and performance compensation as described in the relevant offering documents; individual investor results vary based on timing, class of interest and tax circumstances.</p>

    <h2 class="h2">Testimonials and endorsements</h2>
    <p>Any investor statements shown on this website are the views of the individuals quoted as of the date given, may not represent the experience of other investors, and are not a guarantee of future performance. Where any compensation, discount or other consideration has been provided in exchange for a statement, that fact is disclosed adjacent to the statement. Valeward retains written, dated permission for every published statement.</p>

    <h2 class="h2">No advisory relationship</h2>
    <p>Valeward Capital LLC is a real estate sponsor and is not a registered investment adviser, broker-dealer, municipal advisor or tax adviser, and is not acting in a fiduciary capacity toward visitors to this website. Nothing here takes into account your objectives, financial situation or needs. Consult your own legal, tax and financial advisers before making any investment decision.</p>

    <h2 class="h2">Third parties</h2>
    <p>Third-party service providers named on this site perform defined engagements and do not endorse, recommend or approve any Valeward offering. Any third-party data is believed reliable but is not guaranteed as to accuracy or completeness.</p>

    <h2 class="h2">Contact</h2>
    <p>Questions about these disclosures may be directed to <a href="mailto:compliance@valewardcapital.com">compliance@valewardcapital.com</a> or to [Street Address, City, ST ZIP].</p>

    <div class="callout" style="margin-top:var(--s-6)">
      <h3 class="h3">Prior to publication</h3>
      <p class="small">This page is a structured drafting starting point prepared for design review. It does not constitute legal advice and is not a substitute for review by qualified securities counsel. Counsel should confirm the exemption relied upon, the accredited-investor language, the performance presentation methodology and the testimonial policy before publication.</p>
    </div>

  </div>
</section>
"""})

# --------------------------------------------------------------- PRIVACY
PAGES.append({
    "slug": "privacy.html", "nav_label": "Privacy", "active": "",
    "crumb": "Privacy &amp; terms",
    "title": "Privacy Policy & Terms of Use | Valeward Capital",
    "desc": "How Valeward Capital collects, uses and protects personal information submitted through this website, and the terms governing its use.",
    "h1": "Privacy and terms",
    "lede": "The information collected through this website, the purposes for which it is used, and the terms governing use of the site.",
    "cta": False,
    "body": """
<section class="section">
  <div class="container narrow prose reveal">

    <h2 class="h2">What we collect</h2>
    <p>When you submit a form on this site we collect the information you provide: name, email address, telephone number, self-reported accreditation status, indicative allocation, timing and any notes you choose to add. We also collect standard technical data such as IP address, browser type, referring page and pages viewed.</p>

    <h2 class="h2">Why we collect it</h2>
    <p>To respond to your request, to determine whether an offering may be appropriate to discuss with you, to send offering notices and investor communications you have asked for, to meet our record-keeping obligations under securities regulations, and to improve this website.</p>

    <h2 class="h2">What we will not do</h2>
    <ul>
      <li>We do not sell, rent or trade your personal information</li>
      <li>We do not share your information with other sponsors or lead buyers</li>
      <li>We do not collect financial documents through this website; accreditation verification is handled by an independent provider</li>
      <li>We do not enrol enquirers in automated marketing sequences</li>
    </ul>

    <h2 class="h2">Who we share it with</h2>
    <p>Only with service providers who need it to do their work for us &mdash; our CRM and email provider, our fund administrator, our accreditation verification provider and our professional advisers &mdash; each bound to confidentiality. We may also disclose information where required by law or regulation.</p>

    <h2 class="h2">Retention and your rights</h2>
    <p>We retain enquiry records for as long as needed for the purposes above and to satisfy regulatory record-keeping requirements. Depending on where you live you may have the right to access, correct, delete or port your personal information, or to object to certain processing. Write to <a href="mailto:privacy@valewardcapital.com">privacy@valewardcapital.com</a> and we will respond within thirty days. You can unsubscribe from any communication with one click.</p>

    <h2 class="h2">Cookies</h2>
    <p>This site uses essential cookies required for it to function, and may use analytics cookies to understand which pages are useful. You can control cookies through your browser settings. [If advertising or retargeting pixels are added, disclose them here and implement a consent banner for applicable jurisdictions.]</p>

    <h2 class="h2">Security</h2>
    <p>We use industry-standard measures including encryption in transit to protect information submitted through this site. No method of transmission or storage is completely secure, and we cannot guarantee absolute security.</p>

    <h2 class="h2" id="terms">Terms of use</h2>
    <p>By using this website you agree that the content is provided for general informational purposes without warranty of any kind, express or implied, including as to accuracy or completeness. Valeward is not liable for any loss arising from reliance on this website. Content, marks and design are the property of Valeward Capital LLC or its licensors and may not be reproduced without permission. Links to third-party sites are provided for convenience and do not constitute endorsement. These terms are governed by the laws of [State], without regard to conflict of law principles.</p>

    <p class="small">Last updated: [Date].</p>

    <div class="callout" style="margin-top:var(--s-6)">
      <h3 class="h3">Prior to publication</h3>
      <p class="small">This is a drafting starting point prepared for design review and does not constitute legal advice. Counsel should confirm obligations under applicable state privacy legislation, the GDPR where non-US investors are accepted, the CAN-SPAM Act, and the firm&rsquo;s actual data flows before publication.</p>
    </div>

  </div>
</section>
"""})

# ==========================================================================
def build():
    written = []
    for page in PAGES:
        html = head(page) + header(page.get("active", "")) + page_hero(page) + page["body"]
        if page.get("cta"):
            html += CTA_BAND
        html += FOOTER
        path = os.path.join(OUT, page["slug"])
        io.open(path, "w", encoding="utf-8").write(html)
        written.append(page["slug"])
    return written

if __name__ == "__main__":
    for name in build():
        print("built " + name)
