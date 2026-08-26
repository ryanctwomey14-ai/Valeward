# Valeward Capital — website

Static HTML/CSS/JS. No framework, no build dependencies, no runtime.
Built by LeadTide.

> ### ⚠️ This is a design preview, not a launch build
>
> Every figure, property, testimonial and named third party on this site is an
> **illustrative placeholder**. Nothing here has been verified, and the site
> carries `noindex` so it cannot be picked up by search engines while it is in
> review. See **Before launch** at the bottom of this file.

---

## Repository layout

```
/                       source assets as supplied by the client
├── Valeward Hero.mp4            original hero footage (13.6MB)
├── Valeward Section 2 Home.mp4  original aerial footage
├── Carla Kiernan Logo.JPG       original headshot
├── Valeward Capital Logo.png    logomark
├── STRATEGY.md          ICP, conversion logic, SEO plan, design direction
└── site/                the deployable website
    ├── index.html               homepage (hand-maintained)
    ├── *.html                   generated — edit _build/build.py instead
    ├── assets/css/styles.css    the entire design system
    ├── assets/js/main.js        interaction layer
    ├── assets/js/agent.js       investor assistant
    ├── assets/img, assets/video optimised media
    └── _build/build.py          page generator (not deployed)
```

## Running it locally

```bash
python -m http.server 8899 --directory site
```

Open `http://localhost:8899`. Use `http://`, not `file://` — the stylesheet
will not resolve otherwise.

## Editing

**Homepage** — edit `site/index.html` directly.

**Every other page** — edit its entry in `site/_build/build.py`, then:

```bash
cd site && python _build/build.py
```

The header, footer, disclosure block and page shell live in that one file so
they cannot drift apart across eleven pages. Editing a generated `.html`
directly works until the next build overwrites it.

## Design system

Everything is tokenised at the top of `styles.css`. Reskin by changing tokens,
not components.

| | |
|---|---|
| **Display type** | Cinzel — the face in the VALEWARD wordmark |
| **Body type** | Jost — the face in the CAPITAL subline |
| **Gold** `#B8873B` | Reserved for the primary CTA. Using it elsewhere weakens every button. |
| **The arch** | `--arch: 999px 999px 4px 4px`. Used on the logomark, timeline markers, image frames and the assistant launcher. |
| **Motion** | One curve, `--ease-out`. 140ms press / 220ms UI / 760ms reveal. |

## The investor assistant

`site/assets/js/agent.js`. Bottom-right on every page.

It answers from a **curated knowledge base built from this site's own published
content** — not a live language model. That is deliberate: a static site cannot
hold an API key without exposing it publicly, and answers that can only come
from approved copy cannot drift from what the site says.

**Guardrails (do not remove without counsel):**
- Refuses personalised suitability questions and hands off to the team
- Answers only from published content; declines anything else in writing
- Carries a standing "not investment advice" disclosure

**Keeping it accurate:** figures in the `KB` array mirror the published pages.
If a number changes on the site, change it in `agent.js` in the same commit.

**To connect a real model later**, set an endpoint before the script loads:

```html
<script>window.VALEWARD_AGENT_ENDPOINT = 'https://your-api/investor-agent';</script>
```

It will `POST {question, history}` and render `{answer}`, keeping the same UI,
guardrails and disclosure. The API key stays server-side, where it belongs.

## Media

| File | Source | Output |
|---|---|---|
| `assets/video/hero.mp4` | `Valeward Hero.mp4` (13.6MB) | 2.1MB, audio stripped, faststart |
| `assets/img/hero-poster.jpg` | frame at 1s | 198KB |
| `assets/img/principles-bg.jpg` | `Valeward Section 2 Home.mp4` frame at 2s | 306KB |
| `assets/img/carla-kiernan.jpg` | `Carla Kiernan Logo.JPG` | 158KB, cropped 4:5 |

The hero video **does not download on phones or under `prefers-reduced-motion`** —
those visitors get the poster frame instead.

Remaining images are illustrated SVG placeholders. Drop a real photo into
`assets/img/` with the matching filename and it takes over automatically; if the
file is absent, the illustration stands in. Filenames are listed in
`site/README.md`.

## Accessibility

Skip link, one `<h1>` per page, sequential headings, visible focus rings, ARIA on
the accordion, mobile menu and assistant, 44px minimum touch targets,
`prefers-reduced-motion` honoured throughout, hover effects gated to fine
pointers, tables with captions and scoped headers. Verified at 375, 768, 1024
and 1440px with no horizontal overflow.

---

## Before launch

**Compliance — do this first**

- [ ] Confirm with securities counsel whether the offering is **506(b) or 506(c)**.
      This site is built for 506(c). If it is 506(b), public performance figures
      and offering marketing must come down.
- [ ] Counsel reviews `/disclosures`, `/privacy`, the performance methodology,
      the testimonial policy **and the assistant's knowledge base**.
- [ ] Replace every placeholder figure with verified, documented numbers and
      state the as-of date and calculation method.
- [ ] **Reconcile the return figures.** The site states a 1.8–2.2x equity multiple
      *and* a 15–20% blended annual return. At a five-year hold those imply
      2.0–2.5x, which the calculator on `/approach` displays. Pick one:
      raise the multiple to 2.0–2.5x, or lower the annual figure to 13–17%.
- [ ] Replace the illustrative migration figures with cited Census data.
- [ ] Obtain written, dated permission for each testimonial.

**Content**

- [ ] Fill `[Title]` and the bracketed bio fields on Carla Kiernan's section
- [ ] Replace `[Audit Firm]`, `[Fund Admin]`, addresses, phone numbers
- [ ] `Origins` on `/about` still says "either principal" / "both principals"

**Technical**

- [ ] **Remove the `noindex` tag from every page** — search for `PREVIEW ONLY`
- [ ] **Restore the production `robots.txt`** (the rules are commented in the file)
- [ ] Connect both forms to your CRM with server-side validation and spam control
- [ ] Point `Investor login` at the real portal
- [ ] Analytics with conversion events on both form submissions
- [ ] Clean URLs, HTTPS, canonical tags, Search Console
