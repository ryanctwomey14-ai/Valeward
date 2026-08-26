/* ==========================================================================
   VALEWARD CAPITAL — Interaction layer
   --------------------------------------------------------------------------
   Motion rules enforced here:
   - transform / opacity / clip-path only (no layout-triggering properties)
   - strong ease-out, cubic-bezier(.23,1,.32,1), owned by the stylesheet
   - staggers 65-70ms, never all-at-once
   - every effect gated on prefers-reduced-motion and (hover:hover)
   - scroll work is rAF-throttled; observers unobserve after firing
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)');
  var prefersReduced = function () { return reduce.matches; };

  /* --------------------------------------------------------------------
     1. PAGE-LOAD SEQUENCE
     The hero headline sets word by word, then the supporting copy and CTAs
     lift in. Purpose: explanation — it establishes reading order on a page
     the visitor sees once. Fires after fonts settle so words don't reflow.
     -------------------------------------------------------------------- */
  function startLoadSequence() {
    document.documentElement.classList.add('is-ready');
  }
  if (document.fonts && document.fonts.ready) {
    var safety = setTimeout(startLoadSequence, 900); // never let a slow font block the page
    document.fonts.ready.then(function () {
      clearTimeout(safety);
      requestAnimationFrame(startLoadSequence);
    });
  } else {
    requestAnimationFrame(startLoadSequence);
  }

  /* --------------------------------------------------------------------
     2. SPLIT HEADLINE INTO WORDS
     Each word gets its own overflow-clipped line so it rises out of a mask.
     -------------------------------------------------------------------- */
  document.querySelectorAll('[data-split]').forEach(function (el) {
    var index = 0;
    Array.prototype.slice.call(el.querySelectorAll('.reveal-line')).forEach(function (line) {
      var words = line.textContent.trim().split(/\s+/);
      line.textContent = '';
      words.forEach(function (word, i) {
        var span = document.createElement('span');
        span.className = 'reveal-word';
        span.style.setProperty('--i', index++);
        span.textContent = word;
        line.appendChild(span);
        if (i < words.length - 1) line.appendChild(document.createTextNode(' '));
      });
    });
  });

  /* --------------------------------------------------------------------
     3. SCROLL REVEAL
     Purpose: preventing a jarring change — sections resolve as they enter
     rather than snapping in fully formed. Children stagger via --i.
     -------------------------------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal, .reveal-arch');
  if ('IntersectionObserver' in window && revealables.length) {
    var revealObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    revealables.forEach(function (el) { revealObserver.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* auto-stagger: any group marked [data-stagger] indexes its own children */
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    Array.prototype.slice.call(group.children).forEach(function (child, i) {
      if (child.classList.contains('reveal')) child.style.setProperty('--i', i);
    });
  });

  /* --------------------------------------------------------------------
     4. COUNTERS
     Purpose: state indication — the numbers are the proof, so they earn a
     beat of attention. Skipped entirely under reduced motion (value shown
     immediately, never withheld).
     -------------------------------------------------------------------- */
  function formatNumber(value, decimals) {
    return value.toFixed(decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }

  function runCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';

    if (isNaN(target)) return;
    if (prefersReduced()) {
      el.textContent = prefix + formatNumber(target, decimals) + suffix;
      return;
    }

    var duration = 1500;
    var start = null;
    function frame(now) {
      if (start === null) start = now;
      var p = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3); // ease-out cubic, matches the CSS curve family
      el.textContent = prefix + formatNumber(target * eased, decimals) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && counters.length) {
    var counterObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        runCounter(entry.target);
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { counterObserver.observe(el); });
  } else {
    counters.forEach(runCounter);
  }

  /* --------------------------------------------------------------------
     5. HEADER STATE + SCROLL PROGRESS
     One rAF-throttled scroll handler for both. Progress bar uses scaleX.
     -------------------------------------------------------------------- */
  var header = document.querySelector('.header');
  var progress = document.querySelector('.scroll-progress');
  var ticking = false;

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('is-stuck', y > 24);
    if (progress) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = 'scaleX(' + (max > 0 ? Math.min(y / max, 1) : 0) + ')';
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  /* --------------------------------------------------------------------
     6. HERO APERTURE PARALLAX
     Purpose: spatial depth. Tiny (max ~34px), transform-only, desktop-only,
     off under reduced motion. Parallax that you notice is parallax that
     is too strong.
     -------------------------------------------------------------------- */
  var aperture = document.querySelector('[data-parallax]');
  if (aperture && fine.matches && !prefersReduced()) {
    var pTicking = false;
    window.addEventListener('scroll', function () {
      if (pTicking) return;
      pTicking = true;
      requestAnimationFrame(function () {
        var y = window.scrollY || window.pageYOffset;
        if (y < window.innerHeight * 1.2) {
          aperture.style.transform = 'translate3d(0,' + (y * 0.075).toFixed(2) + 'px,0)';
        }
        pTicking = false;
      });
    }, { passive: true });
  }

  /* --------------------------------------------------------------------
     7. MAGNETIC PRIMARY CTA
     Decorative mouse-tracking — permitted on a marketing page, and only
     here. 7px maximum pull, released on leave. Never on data or forms.
     -------------------------------------------------------------------- */
  if (fine.matches && !prefersReduced()) {
    document.querySelectorAll('[data-magnetic]').forEach(function (btn) {
      var raf = null;
      btn.addEventListener('mousemove', function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var r = btn.getBoundingClientRect();
          var dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
          var dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
          btn.style.transform = 'translate3d(' + (dx * 7).toFixed(2) + 'px,' + (dy * 5).toFixed(2) + 'px,0)';
          raf = null;
        });
      });
      btn.addEventListener('mouseleave', function () {
        btn.style.transform = '';
      });
    });
  }

  /* --------------------------------------------------------------------
     8. MOBILE MENU
     -------------------------------------------------------------------- */
  var burger = document.querySelector('.burger');
  var mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    var setMenu = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      mobileMenu.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () {
      setMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        burger.focus();
      }
    });
  }

  /* --------------------------------------------------------------------
     9. ACCORDION
     height is the one sanctioned exception — there is no transform
     equivalent for opening a panel. Measured, then released to auto.
     -------------------------------------------------------------------- */
  document.querySelectorAll('.acc__btn').forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;

    btn.addEventListener('click', function () {
      var isOpen = btn.getAttribute('aria-expanded') === 'true';
      var group = btn.closest('.accordion');

      // close siblings — one open panel keeps the list scannable
      if (!isOpen && group) {
        group.querySelectorAll('.acc__btn[aria-expanded="true"]').forEach(function (other) {
          var otherPanel = document.getElementById(other.getAttribute('aria-controls'));
          other.setAttribute('aria-expanded', 'false');
          if (otherPanel) {
            otherPanel.style.height = otherPanel.scrollHeight + 'px';
            requestAnimationFrame(function () { otherPanel.style.height = '0px'; });
          }
        });
      }

      btn.setAttribute('aria-expanded', String(!isOpen));
      if (isOpen) {
        panel.style.height = panel.scrollHeight + 'px';
        requestAnimationFrame(function () { panel.style.height = '0px'; });
      } else {
        panel.style.height = panel.scrollHeight + 'px';
        panel.addEventListener('transitionend', function done(e) {
          if (e.propertyName !== 'height') return;
          panel.style.height = 'auto';
          panel.removeEventListener('transitionend', done);
        });
      }
    });
  });

  /* --------------------------------------------------------------------
     10. MARQUEE — duplicate the track so the loop is seamless
     -------------------------------------------------------------------- */
  document.querySelectorAll('.marquee').forEach(function (m) {
    var track = m.querySelector('.marquee__track');
    if (track && !m.dataset.cloned) {
      m.appendChild(track.cloneNode(true));
      m.dataset.cloned = 'true';
    }
  });

  /* --------------------------------------------------------------------
     10b. HERO VIDEO
     Background motion is decorative, so it must not play for anyone who has
     asked for less of it. Pausing leaves the poster frame showing, which is
     the same picture without the movement.
     -------------------------------------------------------------------- */
  (function heroVideo() {
    var v = document.querySelector('.hero__video');
    if (!v) return;
    var src = v.querySelector('source[data-src]');
    if (!src) return;

    // Don't spend 2MB of someone's mobile data on decoration, and don't play
    // it at all for anyone who asked for less motion. Both cases keep the
    // poster frame, which is the same picture without the movement.
    if (prefersReduced() || window.innerWidth < 760) return;

    src.setAttribute('src', src.getAttribute('data-src'));
    v.load();
    var attempt = v.play();
    if (attempt && attempt.catch) attempt.catch(function () {
      v.addEventListener('canplay', function () { v.play().catch(function () {}); }, { once: true });
    });
  })();

  /* --------------------------------------------------------------------
     11. PHOTO SLOTS
     Each image sits over an SVG scene. If the photo isn't in place yet,
     drop the <img> and the illustrated scene stands in. Replace the files
     in /assets/img and the photography takes over with no code change.
     -------------------------------------------------------------------- */
  document.querySelectorAll('.photo-slot img').forEach(function (img) {
    img.addEventListener('error', function () {
      img.remove();
    });
    if (img.complete && img.naturalWidth === 0) img.remove();
  });

  /* --------------------------------------------------------------------
     12. FORMS
     Inline validation on blur (never on keystroke), errors beside the
     field, focus moved to the first problem on submit. Demo-only: no
     endpoint is wired, so submission is intercepted.
     -------------------------------------------------------------------- */
  document.querySelectorAll('[data-form]').forEach(function (form) {
    var fields = form.querySelectorAll('input[required], select[required]');

    var validate = function (input) {
      var wrap = input.closest('.field') || input.closest('.check');
      if (!wrap) return true;
      var ok = input.checkValidity();
      wrap.classList.toggle('has-error', !ok);
      return ok;
    };

    fields.forEach(function (input) {
      input.addEventListener('blur', function () { validate(input); });
      input.addEventListener('input', function () {
        var wrap = input.closest('.field');
        if (wrap && wrap.classList.contains('has-error')) validate(input);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      fields.forEach(function (input) {
        if (!validate(input) && !firstBad) firstBad = input;
      });
      if (firstBad) { firstBad.focus(); return; }

      var success = form.parentNode.querySelector('.form-success');
      if (success) {
        form.classList.add('is-hidden');
        success.classList.add('is-visible');
        success.setAttribute('tabindex', '-1');
        success.focus();
      }
    });
  });

  /* --------------------------------------------------------------------
     13. RETURN MODEL
     Two sliders, live output. Every number shown is derived from the
     ASSUMPTIONS block below and nowhere else -- change a target there and
     the whole panel follows. Results are ranges, never single figures,
     because the underlying targets are ranges.
     -------------------------------------------------------------------- */
  var ASSUMPTIONS = {
    cashLow: 0.07,    // 7%  annual cash distribution, low end
    cashHigh: 0.10,   // 10% annual cash distribution, high end
    totalLow: 0.15,   // 15% blended annual rate of return, low end
    totalHigh: 0.20   // 20% blended annual rate of return, high end
  };

  (function returnModel() {
    var amountEl = document.getElementById('calc-amount');
    var yearsEl = document.getElementById('calc-years');
    if (!amountEl || !yearsEl) return;

    var amountOut = document.getElementById('calc-amount-out');
    var yearsOut = document.getElementById('calc-years-out');
    var outCash = document.getElementById('out-cash');
    var outMultiple = document.getElementById('out-multiple');
    var outProfit = document.getElementById('out-profit');
    var outTotal = document.getElementById('out-total');

    var money = function (n) {
      return '$' + Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    };
    var range = function (lo, hi, fmt) { return fmt(lo) + ' – ' + fmt(hi); };

    function paintTrack(el) {
      // --fill is consumed by the ::-webkit-slider-runnable-track gradient
      var pct = (el.value - el.min) / (el.max - el.min) * 100;
      el.style.setProperty('--fill', pct.toFixed(1) + '%');
    }

    function update() {
      var amount = parseFloat(amountEl.value);
      var years = parseFloat(yearsEl.value);

      amountOut.textContent = money(amount);
      yearsOut.textContent = years + (years === 1 ? ' year' : ' years');

      var cashLo = amount * ASSUMPTIONS.cashLow * years;
      var cashHi = amount * ASSUMPTIONS.cashHigh * years;
      var totalLo = amount * Math.pow(1 + ASSUMPTIONS.totalLow, years);
      var totalHi = amount * Math.pow(1 + ASSUMPTIONS.totalHigh, years);

      outCash.textContent = range(cashLo, cashHi, money);
      outMultiple.textContent = range(totalLo / amount, totalHi / amount, function (v) { return v.toFixed(1) + 'x'; });
      outProfit.textContent = range(totalLo - amount, totalHi - amount, money);
      outTotal.textContent = range(totalLo, totalHi, money);

      paintTrack(amountEl);
      paintTrack(yearsEl);
    }

    amountEl.addEventListener('input', update);
    yearsEl.addEventListener('input', update);
    update();
  })();

  /* --------------------------------------------------------------------
     14. MIGRATION MAP
     A tile-grid map built from data rather than hand-placed markup, so the
     figures and the picture can never drift apart. Equal cells are a
     deliberate choice: land area is not population.
     -------------------------------------------------------------------- */
  (function migrationMap() {
    var root = document.querySelector('[data-migration]');
    if (!root) return;

    // [abbr, col, row, name, illustrative net domestic migration in thousands]
    var STATES = [
      ['AK',0,0,'Alaska',-4],   ['ME',10,0,'Maine',6],
      ['VT',9,1,'Vermont',1],   ['NH',10,1,'New Hampshire',5],
      ['WA',0,2,'Washington',-10],['ID',1,2,'Idaho',25],['MT',2,2,'Montana',12],
      ['ND',3,2,'North Dakota',-2],['MN',4,2,'Minnesota',-12],['IL',5,2,'Illinois',-85],
      ['WI',6,2,'Wisconsin',-3],['MI',7,2,'Michigan',-8],['NY',8,2,'New York',-180],
      ['RI',9,2,'Rhode Island',-1],['MA',10,2,'Massachusetts',-40],
      ['OR',0,3,'Oregon',-15],['NV',1,3,'Nevada',17],['WY',2,3,'Wyoming',3],
      ['SD',3,3,'South Dakota',4],['IA',4,3,'Iowa',-2],['IN',5,3,'Indiana',10],
      ['OH',6,3,'Ohio',-3],['PA',7,3,'Pennsylvania',-9],['NJ',8,3,'New Jersey',-48],
      ['CT',9,3,'Connecticut',-3],
      ['CA',0,4,'California',-240],['UT',1,4,'Utah',14],['CO',2,4,'Colorado',-8],
      ['NE',3,4,'Nebraska',-3],['MO',4,4,'Missouri',9],['KY',5,4,'Kentucky',8],
      ['WV',6,4,'West Virginia',5],['VA',7,4,'Virginia',-6],['MD',8,4,'Maryland',-18],
      ['DE',9,4,'Delaware',5],
      ['AZ',1,5,'Arizona',54],['NM',2,5,'New Mexico',-3],['KS',3,5,'Kansas',-5],
      ['AR',4,5,'Arkansas',11],['TN',5,5,'Tennessee',58],['NC',6,5,'North Carolina',82],
      ['SC',7,5,'South Carolina',68],['DC',8,5,'District of Columbia',-12],
      ['OK',3,6,'Oklahoma',18],['LA',4,6,'Louisiana',-35],['MS',5,6,'Mississippi',2],
      ['AL',6,6,'Alabama',22],['GA',7,6,'Georgia',42],
      ['HI',0,7,'Hawaii',-13],['TX',3,7,'Texas',125],['FL',8,7,'Florida',195]
    ];

    // Valeward operates here — surfaced on the panel
    var FOOTPRINT = { TN: 1, AL: 1, SC: 1, NC: 1, GA: 1, TX: 1 };

    // dominant flows, [from, to]
    var FLOWS = [
      ['CA','TX'], ['CA','AZ'], ['NY','FL'], ['NY','NC'],
      ['IL','TX'], ['IL','TN'], ['NJ','SC'], ['MA','FL']
    ];

    var SIZE = 44, STEP = 50;
    var svg = root.querySelector('.migration__map');
    var NS = 'http://www.w3.org/2000/svg';
    var byAbbr = {};
    STATES.forEach(function (st) { byAbbr[st[0]] = st; });

    var maxGain = 0, maxLoss = 0;
    STATES.forEach(function (st) {
      if (st[4] > maxGain) maxGain = st[4];
      if (st[4] < maxLoss) maxLoss = st[4];
    });

    function fillFor(net) {
      if (net > 0) {
        // gold, deepening with inflow
        var t = Math.pow(net / maxGain, 0.55);
        return 'rgba(184,135,59,' + (0.18 + t * 0.82).toFixed(3) + ')';
      }
      var l = Math.pow(net / maxLoss, 0.55);
      return 'rgba(90,67,102,' + (0.35 + l * 0.55).toFixed(3) + ')';
    }

    function centre(abbr) {
      var st = byAbbr[abbr];
      return { x: st[1] * STEP + SIZE / 2, y: st[2] * STEP + SIZE / 2 };
    }

    // ---- tiles ----
    var gTiles = document.createElementNS(NS, 'g');
    STATES.forEach(function (st) {
      var g = document.createElementNS(NS, 'g');
      g.setAttribute('class', 'mig-tile-g' + (st[4] > maxGain * 0.35 ? ' is-gain' : ''));
      g.setAttribute('tabindex', '0');
      g.setAttribute('role', 'button');
      g.setAttribute('aria-label', st[3] + ', net migration ' + (st[4] > 0 ? 'plus ' : 'minus ') + Math.abs(st[4]) + ' thousand');

      var r = document.createElementNS(NS, 'rect');
      r.setAttribute('class', 'mig-tile');
      r.setAttribute('x', st[1] * STEP);
      r.setAttribute('y', st[2] * STEP);
      r.setAttribute('width', SIZE);
      r.setAttribute('height', SIZE);
      r.setAttribute('rx', 4);
      r.setAttribute('fill', fillFor(st[4]));

      var t = document.createElementNS(NS, 'text');
      t.setAttribute('class', 'mig-label');
      t.setAttribute('x', st[1] * STEP + SIZE / 2);
      t.setAttribute('y', st[2] * STEP + SIZE / 2 + 4);
      t.setAttribute('text-anchor', 'middle');
      t.textContent = st[0];

      g.appendChild(r);
      g.appendChild(t);
      g.addEventListener('mouseenter', function () { select(st[0]); });
      g.addEventListener('focus', function () { select(st[0]); });
      g.addEventListener('click', function () { select(st[0]); });
      gTiles.appendChild(g);
    });

    // ---- flow arcs (behind the tiles) ----
    var gArcs = document.createElementNS(NS, 'g');
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    FLOWS.forEach(function (fl, i) {
      var a = centre(fl[0]), b = centre(fl[1]);
      var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
      var dx = b.x - a.x, dy = b.y - a.y;
      var len = Math.sqrt(dx * dx + dy * dy) || 1;
      // bow the arc perpendicular to its own run
      var cx = mx - dy / len * len * 0.22;
      var cy = my + dx / len * len * 0.22;
      var d = 'M' + a.x + ',' + a.y + ' Q' + cx.toFixed(1) + ',' + cy.toFixed(1) + ' ' + b.x + ',' + b.y;

      var p = document.createElementNS(NS, 'path');
      p.setAttribute('class', 'mig-arc');
      p.setAttribute('d', d);
      gArcs.appendChild(p);

      if (!reduced) {
        var dot = document.createElementNS(NS, 'circle');
        dot.setAttribute('class', 'mig-pulse');
        dot.setAttribute('r', '3');
        var m = document.createElementNS(NS, 'animateMotion');
        m.setAttribute('dur', (4.5 + i * 0.4).toFixed(1) + 's');
        m.setAttribute('repeatCount', 'indefinite');
        m.setAttribute('path', d);
        m.setAttribute('begin', (i * 0.5).toFixed(1) + 's');
        dot.appendChild(m);
        gArcs.appendChild(dot);
      }
    });

    svg.appendChild(gArcs);
    svg.appendChild(gTiles);

    // ---- detail panel ----
    var elName = root.querySelector('[data-mig-name]');
    var elNet = root.querySelector('[data-mig-net]');
    var elNote = root.querySelector('[data-mig-note]');
    var elFlag = root.querySelector('[data-mig-flag]');

    function select(abbr) {
      var st = byAbbr[abbr];
      if (!st) return;
      root.querySelectorAll('.mig-tile.is-active').forEach(function (n) { n.classList.remove('is-active'); });
      root.querySelectorAll('.migration__rank li.is-active').forEach(function (n) { n.classList.remove('is-active'); });
      var idx = STATES.indexOf(st);
      var tile = gTiles.children[idx] && gTiles.children[idx].querySelector('.mig-tile');
      if (tile) tile.classList.add('is-active');
      var row = root.querySelector('.migration__rank li[data-state="' + abbr + '"]');
      if (row) row.classList.add('is-active');

      elName.textContent = st[3];
      var gain = st[4] > 0;
      elNet.textContent = (gain ? '+' : '−') + Math.abs(st[4]) + 'k';
      elNet.className = 'migration__net ' + (gain ? 'is-gain' : 'is-loss');
      elNote.textContent = gain
        ? 'Net domestic in-migration. Household formation of this kind supports rental demand ahead of new supply.'
        : 'Net domestic out-migration. Capital tends to follow households, which is why we do not acquire here.';
      elFlag.style.display = FOOTPRINT[abbr] ? 'inline-block' : 'none';
    }

    // ---- ranked list ----
    var rank = root.querySelector('[data-mig-rank]');
    if (rank) {
      STATES.slice().sort(function (a, b) { return b[4] - a[4]; }).slice(0, 5).forEach(function (st) {
        var li = document.createElement('li');
        li.setAttribute('data-state', st[0]);
        li.innerHTML = '<span>' + st[3] + '</span><b>+' + st[4] + 'k</b>';
        li.addEventListener('mouseenter', function () { select(st[0]); });
        li.addEventListener('click', function () { select(st[0]); });
        rank.appendChild(li);
      });
    }

    select('TX');
  })();

  /* --------------------------------------------------------------------
     15. CURRENT YEAR
     -------------------------------------------------------------------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
