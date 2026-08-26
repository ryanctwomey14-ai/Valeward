/* ==========================================================================
   VALEWARD CAPITAL — Investor assistant
   --------------------------------------------------------------------------
   Answers the questions a prospective investor actually asks, from a curated
   knowledge base built out of this site's own published content.

   WHY IT WORKS THIS WAY
   This is a static site. A live model call needs an API key, and any key
   shipped to the browser is public the moment the page loads. So the default
   build answers locally, from content Valeward has already approved in
   writing. Nothing it says can drift from what the site says.

   TO CONNECT A REAL MODEL LATER
   Set window.VALEWARD_AGENT_ENDPOINT to your own server route (which holds
   the key server-side). The widget will POST {question, history} and render
   {answer}. Everything else — the UI, the guardrails, the disclosure — stays.

   COMPLIANCE GUARDRAILS (do not remove without counsel)
   - Refuses personalised suitability / advice questions and hands off
   - Never states a figure that is not published elsewhere on this site
   - Appends a standing disclosure to substantive answers
   - Directs anything it cannot answer to a human
   ========================================================================== */
(function () {
  'use strict';

  var CONTACT = 'investors@valewardcapital.com';

  /* ---------- knowledge base -------------------------------------------
     Each entry: keys (matched against the question) and answer.
     Figures here MUST mirror the published pages. If a number changes on
     the site, change it here in the same commit.
     -------------------------------------------------------------------- */
  var KB = [
    { id: 'minimum',
      keys: ['minimum', 'least', 'smallest', 'start with', 'how much do i need', 'entry', 'ticket', '50000', '50k', '25k'],
      a: 'The standard minimum is <b>$50,000</b> per offering. A limited number of <b>$25,000</b> allocations is reserved in each round for investors participating in a Valeward offering for the first time.' },

    { id: 'accredited',
      keys: ['accredited', 'accreditation', 'qualify', 'eligible', 'eligibility', '506', 'reg d', 'regulation d', 'verified', 'net worth', 'income requirement'],
      a: 'Offerings are made under <b>Rule 506(c) of Regulation D</b>, so every investor must be verified as accredited. That generally means individual income above $200,000 (or $300,000 jointly) in each of the last two years, or net worth above $1M excluding your primary residence. Certain professional licences also qualify. Verification is handled by an independent third party — Valeward does not retain your financial documents.' },

    { id: 'hold',
      keys: ['how long', 'hold period', 'locked', 'lock up', 'lockup', 'liquidity', 'liquid', 'get my money back', 'withdraw', 'exit', 'secondary market', 'redeem', 'redemption'],
      a: 'Plan on <b>five to seven years</b>. There is no secondary market, no redemption right and no facility for early withdrawal. If a disposition or refinancing returns capital sooner, that is incidental — not a basis on which to subscribe. We decline subscriptions from investors who tell us they may need the capital back early.' },

    { id: 'distributions',
      keys: ['distribution', 'cash flow', 'paid', 'payment', 'quarterly', 'income', 'cash on cash', 'yield', 'when do i get paid', 'ach'],
      a: 'Distributions are targeted at a <b>7–10% annualized rate</b> on invested capital, remitted by ACH on the fifteenth of the month following each quarter close. New investments generally begin distributing after the first full quarter of ownership. If a distribution will be reduced or suspended, you receive written notice with the reason before the payment date.' },

    { id: 'returns',
      keys: ['return', 'returns', 'irr', 'multiple', 'equity multiple', 'how much can i make', 'target', 'profit', 'roi', '15', '20'],
      a: 'Offerings target a <b>7–10% annual cash distribution</b>, a <b>1.8–2.2x equity multiple</b>, and a <b>15–20% blended annual rate of return</b> over the hold. These are objectives derived from underwriting, not undertakings. Realized results to date have ranged from 1.4x to 2.3x, and outcomes may be materially worse — including total loss. You can model a position on the Approach page.' },

    { id: 'fees',
      keys: ['fee', 'fees', 'cost', 'charge', 'promote', 'waterfall', 'preferred return', 'how do you get paid', 'compensation', 'carry'],
      a: 'A <b>1.5% acquisition fee</b> at closing, a <b>2% annual asset management fee</b> on invested equity, and <b>25% of profits above an 8% preferred return</b> — payable only after all investor capital has been returned. There is no disposition fee, no refinancing fee, and no fee on transactions that do not complete. The complete schedule is in each offering’s private placement memorandum.' },

    { id: 'risk',
      keys: ['risk', 'lose', 'loss', 'downside', 'safe', 'guarantee', 'guaranteed', 'what if', 'crash', 'recession', 'worst case'],
      a: 'Yes — you can lose money, <b>including your entire investment</b>. These are speculative, illiquid, unguaranteed securities, and lenders rank ahead of equity in any adverse outcome. The principal risks are loan maturity in a constrained credit market, operating expenses outrunning rents, submarket over-supply, and sponsor error. Fixed-rate financing and twelve months of debt-service reserves are designed to reduce the likelihood of a forced sale, but no structure eliminates the risk of loss.' },

    { id: 'k1',
      keys: ['k-1', 'k1', 'tax form', 'schedule k', 'when is my k', 'filing', 'april 15', 'tax document'],
      a: 'Schedule K-1s are delivered by <b>April 15</b>. If a K-1 will be delayed for reasons outside our control, you hear from us with a specific delivery date before April 1.' },

    { id: 'tax',
      keys: ['tax', 'taxes', 'depreciation', 'cost segregation', 'passive loss', 'write off', 'deduction', 'shelter', 'recapture'],
      a: 'A <b>cost segregation study</b> is commissioned on every acquisition, so most investors report a first-year passive loss even though cash was distributed to them. Those losses are generally passive in character and typically offset passive income rather than employment income. Whether that helps your situation is a question for your accountant — <b>Valeward does not provide tax advice</b>.' },

    { id: 'ira',
      keys: ['ira', '401k', '401(k)', 'retirement', 'self directed', 'sdira', 'trust', 'llc', 'entity', 'ubit'],
      a: 'Yes — self-directed IRAs, solo 401(k) plans, trusts, LLCs and partnerships are all accepted, and we have worked with the principal custodians. Note that leveraged real estate held inside a retirement account may generate <b>unrelated business income tax</b>. We flag that before you subscribe; review it with your tax adviser.' },

    { id: 'process',
      keys: ['how do i start', 'process', 'next step', 'get started', 'sign up', 'invest', 'subscribe', 'subscription', 'apply', 'access'],
      a: 'Four steps, about three weeks: <br>1. <b>Request access</b> and complete third-party accreditation verification.<br>2. <b>Review the diligence file</b> — the underwriting model with editable assumptions, rent roll, T-12, property condition assessment, market study, debt term sheet and the PPM.<br>3. <b>Reserve an allocation</b>, then execute subscription documents and fund by wire or ACH.<br>4. <b>Receive quarterly distributions</b> and reporting.<br>No commitment arises until subscription documents are executed.' },

    { id: 'criteria',
      keys: ['what do you buy', 'criteria', 'buy box', 'mandate', 'type of property', 'class b', 'vintage', 'units', 'workforce'],
      a: 'We acquire <b>150–400 unit</b> communities, <b>1985–2005 vintage</b>, Class B garden or mid-rise, in Sun Belt submarkets growing <b>1–2% a year</b>. Target assets rent <b>20–35% below</b> competing new construction, sit in submarkets with median household income of at least <b>3.5x</b> the in-place rent, have an identifiable operational cause of underperformance, and face declining forward supply.' },

    { id: 'markets',
      keys: ['market', 'markets', 'where', 'location', 'state', 'sun belt', 'migration', 'texas', 'florida', 'tennessee', 'carolina', 'geography'],
      a: 'We operate in Sun Belt submarkets seeing net domestic in-migration — currently Texas, Tennessee, Alabama, Georgia and the Carolinas. The thesis is to buy where households are arriving <i>before</i> the price reflects it. There is an interactive migration map on the Approach page.' },

    { id: 'debt',
      keys: ['debt', 'loan', 'financing', 'leverage', 'interest rate', 'refinance', 'ltv', 'fixed rate', 'bridge', 'maturity'],
      a: 'Every asset carries <b>fixed-rate</b> agency or life company debt with at least two years of term beyond the business plan. Maximum 65% loan-to-value at acquisition, minimum 1.35x debt service coverage at closing, no cross-collateralisation, and no mezzanine debt or preferred equity ranking ahead of limited partners. <b>Valeward does not use floating-rate bridge debt</b> — that is what impaired most of the 2021 vintage.' },

    { id: 'reporting',
      keys: ['report', 'reporting', 'updates', 'communication', 'transparency', 'statements', 'portal', 'how often'],
      a: 'Quarterly distributions and a written asset report covering occupancy, delinquency, capital works completed, and actual performance against underwriting — including anything running behind plan. Annual audited fund-level financials, Schedule K-1 by April 15, and written notice of any material event within ten business days. You also have the direct line of the principal responsible for your asset.' },

    { id: 'team',
      keys: ['who', 'team', 'founder', 'carla', 'kiernan', 'principal', 'management', 'track record', 'experience', 'background'],
      a: '<b>Carla Kiernan</b> founded Valeward Capital in 2016 and sets the acquisition criteria, signs off on every financing decision, and is the point of contact for investors. She has underwritten multifamily assets through two complete market cycles. Principals commit no less than 5% of every equity raise in cash, on terms identical to every other investor.' },

    { id: 'underperform',
      keys: ['gone wrong', 'bad deal', 'lost money', 'underperform', 'failed', 'mistake', 'paused', 'suspended', 'ridgeline', 'ferrand'],
      a: 'Yes, and we publish both. <b>Ridgeline Commons</b> suspended distributions for two quarters in 2023 after a 61% insurance renewal; investors were notified in writing nine days after the decision, the manager was replaced, and distributions resumed in Q3 2024. No capital call was issued. <b>Ferrand Court</b> returned capital at 1.4x against an underwritten 1.9x. Both are documented in full on the Portfolio page.' },

    { id: 'multifamily',
      keys: ['why multifamily', 'why apartments', 'asset class', 'why real estate', 'vs stocks', 'reit', 'diversification'],
      a: 'Residential demand is non-discretionary — it derives from a requirement to have somewhere to live rather than a discretionary business decision. Leases reset annually, so rents can track inflation instead of being fixed below it for a decade. Returns come from four channels at once: distributions, loan amortization, forced appreciation through net operating income, and depreciation passed through on a K-1.' },

    { id: '1031',
      keys: ['1031', 'exchange', 'like kind', 'sell my rental', 'dst', 'defer'],
      a: 'A Valeward LP interest is <b>not</b> generally eligible for a 1031 exchange — exchanges require a direct interest in real property, and an LP interest does not qualify. Investors selling a rental often invest proceeds after paying the tax, or use the depreciation from a Valeward position to offset gain. Speak to your tax adviser, and tell us your timeline when you request access.' },

    { id: 'contact',
      keys: ['contact', 'speak', 'call', 'talk', 'email', 'phone', 'human', 'someone', 'reach'],
      a: 'Email <a href="mailto:' + CONTACT + '">' + CONTACT + '</a> or request access through the site — a principal reads every request personally and replies within two business days.' }
  ];

  /* advice-seeking patterns get a handoff, never an answer */
  var ADVICE = /\b(should i|is this right for me|do you recommend|recommend that i|advise me|what would you do|is it a good investment for me|suitable for me|how much should i invest|is this safe for me|can i afford)\b/i;

  var STOP = /\b(the|a|an|is|are|do|does|did|of|to|in|for|on|and|or|my|your|i|you|it|what|how|when|can|will|be|with|that|this|if|about|there|any|as|at|from|would|should|have|has)\b/g;

  function score(q, entry) {
    var s = 0;
    var norm = ' ' + q + ' ';
    entry.keys.forEach(function (k) {
      if (norm.indexOf(' ' + k + ' ') > -1) { s += k.indexOf(' ') > -1 ? 8 : 5; return; }
      if (norm.indexOf(k) > -1) { s += k.indexOf(' ') > -1 ? 6 : 3; }
    });
    return s;
  }

  function answer(question) {
    var q = question.toLowerCase().replace(/[^\w\s$%().-]/g, ' ').replace(/\s+/g, ' ').trim();

    if (ADVICE.test(question)) {
      return { text: 'I can’t advise on whether an investment suits your circumstances — that depends on your tax position, liquidity needs and goals, and Valeward is not a registered investment adviser. What I can do is set out the facts. Ask me about minimums, hold period, fees, distributions or risk, or <a href="invest.html">speak with the team</a>, who will tell you directly if you are not a fit.', bare: true };
    }

    var best = null, bestScore = 0;
    KB.forEach(function (e) {
      var sc = score(q, e);
      if (sc > bestScore) { bestScore = sc; best = e; }
    });

    if (!best || bestScore < 3) {
      return { text: 'I don’t have a published answer for that, and I won’t guess on an investment question. Email <a href="mailto:' + CONTACT + '">' + CONTACT + '</a> and a principal will answer in writing — usually within two business days.', bare: true };
    }
    return { text: best.a, bare: false };
  }

  /* ---------- optional live backend ------------------------------------ */
  function remoteAnswer(question, history) {
    var url = window.VALEWARD_AGENT_ENDPOINT;
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: question, history: history })
    }).then(function (r) {
      if (!r.ok) throw new Error('bad status');
      return r.json();
    }).then(function (d) { return { text: d.answer, bare: false }; });
  }

  /* ---------- UI -------------------------------------------------------- */
  var SUGGESTIONS = ['What is the minimum?', 'How long is my money committed?', 'How do you get paid?', 'Could I lose money?'];
  var DISCLOSURE = 'General information drawn from this site. Not investment, legal or tax advice, and not an offer to sell securities.';

  function build() {
    var wrap = document.createElement('div');
    wrap.className = 'agent';
    wrap.innerHTML =
      '<button class="agent__launch" aria-expanded="false" aria-controls="agent-panel" aria-label="Open investor questions">' +
        '<svg class="agent__icon" viewBox="0 0 24 28" fill="none" aria-hidden="true">' +
          '<path d="M3 26V11a9 9 0 0 1 18 0v15" stroke="currentColor" stroke-width="1.8"/>' +
          '<path d="M8 12l4 7 4-7" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>' +
        '</svg>' +
        '<span class="agent__launch-label">Investor questions</span>' +
      '</button>' +
      '<div class="agent__panel" id="agent-panel" role="dialog" aria-label="Investor questions" aria-modal="false" hidden>' +
        '<div class="agent__head">' +
          '<div><p class="agent__title">Investor questions</p>' +
          '<p class="agent__sub">Answers from Valeward’s published material</p></div>' +
          '<button class="agent__close" aria-label="Close">&times;</button>' +
        '</div>' +
        '<div class="agent__log" role="log" aria-live="polite"></div>' +
        '<div class="agent__chips"></div>' +
        '<form class="agent__form">' +
          '<label class="sr-only" for="agent-input">Ask a question</label>' +
          '<input class="agent__input" id="agent-input" type="text" autocomplete="off" placeholder="Ask about minimums, fees, risk…">' +
          '<button class="agent__send" type="submit" aria-label="Send">' +
            '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
          '</button>' +
        '</form>' +
        '<p class="agent__disc">' + DISCLOSURE + '</p>' +
      '</div>';
    document.body.appendChild(wrap);
    return wrap;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var wrap = build();
    var launch = wrap.querySelector('.agent__launch');
    var panel = wrap.querySelector('.agent__panel');
    var close = wrap.querySelector('.agent__close');
    var log = wrap.querySelector('.agent__log');
    var chips = wrap.querySelector('.agent__chips');
    var form = wrap.querySelector('.agent__form');
    var input = wrap.querySelector('.agent__input');
    var history = [];

    function bubble(role, html) {
      var b = document.createElement('div');
      b.className = 'agent__msg agent__msg--' + role;
      b.innerHTML = html;
      log.appendChild(b);
      log.scrollTop = log.scrollHeight;
      return b;
    }

    function typing() {
      var t = document.createElement('div');
      t.className = 'agent__msg agent__msg--bot agent__typing';
      t.innerHTML = '<span></span><span></span><span></span>';
      log.appendChild(t);
      log.scrollTop = log.scrollHeight;
      return t;
    }

    function respond(q) {
      bubble('you', q.replace(/</g, '&lt;'));
      history.push({ role: 'user', content: q });
      var t = typing();

      var done = function (res) {
        t.remove();
        bubble('bot', res.text);
        history.push({ role: 'assistant', content: res.text });
        renderChips();
      };

      if (window.VALEWARD_AGENT_ENDPOINT) {
        remoteAnswer(q, history).then(done).catch(function () { done(answer(q)); });
      } else {
        setTimeout(function () { done(answer(q)); }, 340);
      }
    }

    function renderChips() {
      chips.innerHTML = '';
      SUGGESTIONS.forEach(function (s) {
        var c = document.createElement('button');
        c.type = 'button';
        c.className = 'agent__chip';
        c.textContent = s;
        c.addEventListener('click', function () { respond(s); });
        chips.appendChild(c);
      });
    }

    function open(state) {
      launch.setAttribute('aria-expanded', String(state));
      panel.hidden = !state;
      wrap.classList.toggle('is-open', state);
      document.body.classList.toggle('agent-open', state && window.innerWidth < 640);
      if (state) {
        if (!log.children.length) {
          bubble('bot', 'Ask me anything about how a Valeward investment works — minimums, hold period, fees, tax treatment or risk. I answer only from what Valeward has published.');
          renderChips();
        }
        if (window.innerWidth >= 640) input.focus();
      } else {
        launch.focus();
      }
    }

    launch.addEventListener('click', function () { open(panel.hidden); });
    close.addEventListener('click', function () { open(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !panel.hidden) open(false);
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var q = input.value.trim();
      if (!q) return;
      input.value = '';
      respond(q);
    });
  });
})();
