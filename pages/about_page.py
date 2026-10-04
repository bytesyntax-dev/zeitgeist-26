# Generator for about.html (The Lore — Festival Origins & Team)

def get_about_content():
    title = "The Lore — About | ZEITGEIST'26 | IIT Ropar"
    description = "Discover the origins of ZEITGEIST'26, the annual cultural festival of IIT Ropar. Meet the festival council, learn the dark history, and explore the mythos."

    extra_css = """
/* ===== ABOUT PAGE HERO ===== */
.about-hero {
  position: relative;
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  perspective: 1200px;
}

.about-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 50% 60% at 30% 50%, rgba(148, 23, 34, 0.3), transparent 70%),
    radial-gradient(ellipse 40% 50% at 80% 60%, rgba(173, 95, 38, 0.15), transparent 60%);
  pointer-events: none;
  z-index: 0;
  animation: aboutGlow 12s ease-in-out infinite alternate;
}

@keyframes aboutGlow {
  0% { opacity: 0.6; }
  100% { opacity: 1; }
}

.about-hero > * {
  position: relative;
  z-index: 1;
}

.about-hero h1 {
  font-size: clamp(44px, 9vw, 100px);
  line-height: 0.88;
  margin: 14px 0 20px;
  text-shadow: 0 0 40px rgba(148, 23, 34, 0.4);
}

.about-hero .hero-desc {
  font: italic 400 clamp(18px, 2.5vw, 28px)/1.45 var(--serif);
  color: var(--bone-dim);
  max-width: 48ch;
  margin-bottom: 30px;
}

/* Floating cobweb corners */
.cobweb {
  position: absolute;
  width: clamp(80px, 12vw, 200px);
  height: clamp(80px, 12vw, 200px);
  pointer-events: none;
  z-index: 2;
  opacity: 0.12;
  filter: drop-shadow(0 0 8px rgba(226, 219, 206, 0.3));
}

.cobweb.tl { top: 0; left: 0; }
.cobweb.tr { top: 0; right: 0; transform: scaleX(-1); }

/* ===== LORE TIMELINE ===== */
.lore-sec {
  margin: 80px 0;
}

.lore-sec h2 {
  margin-bottom: 40px;
}

.lore-timeline {
  position: relative;
  padding-left: 40px;
}

.lore-timeline::before {
  content: "";
  position: absolute;
  left: 12px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, var(--crim), var(--amber), var(--crim));
  box-shadow: 0 0 8px var(--crim-glow);
}

.lore-entry {
  position: relative;
  margin-bottom: 48px;
  padding: 24px 28px;
  background: rgba(13, 10, 12, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transform-style: preserve-3d;
  transition: transform 0.2s ease-out, border-color 0.3s, box-shadow 0.3s;
}

.lore-entry::before {
  content: "";
  position: absolute;
  left: -33px;
  top: 28px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--crim);
  box-shadow: 0 0 12px var(--crim), 0 0 24px var(--crim-glow);
  z-index: 2;
}

.lore-entry:hover {
  border-color: var(--crim);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), 0 0 20px var(--crim-glow);
}

.lore-year {
  font: 700 clamp(20px, 3vw, 32px) var(--disp-sans);
  color: var(--amber);
  margin-bottom: 8px;
  text-shadow: 0 0 12px var(--amber-glow);
}

.lore-entry h3 {
  font: 700 clamp(16px, 2vw, 22px)/1.1 var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 10px;
  transition: transform 0.3s;
}

.lore-entry:hover h3 {
  transform: translateX(6px);
}

.lore-entry p {
  font: 400 14px/1.7 var(--sans);
  color: var(--bone-dim);
  max-width: 64ch;
}

/* ===== TEAM / COUNCIL GRID ===== */
.council-sec {
  margin: 80px 0;
}

.council-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
  perspective: 1000px;
}

.council-card {
  background: rgba(13, 10, 12, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 28px 24px;
  text-align: center;
  transform-style: preserve-3d;
  transition: transform 0.2s ease-out, border-color 0.3s, box-shadow 0.3s;
  will-change: transform;
  position: relative;
  overflow: hidden;
}

.council-card::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle 200px at var(--cx, 50%) var(--cy, 50%), rgba(148, 23, 34, 0.15), transparent 50%);
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}

.council-card:hover::before {
  opacity: 1;
}

.council-card:hover {
  border-color: var(--crim);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.7), 0 0 20px var(--crim-glow);
}

.council-avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  margin: 0 auto 16px;
  background: linear-gradient(135deg, var(--blood), var(--crim));
  display: grid;
  place-items: center;
  font: 700 24px var(--serif);
  color: var(--bone);
  box-shadow: 0 4px 16px rgba(148, 23, 34, 0.4);
  transform: translateZ(20px);
  transition: transform 0.3s, box-shadow 0.3s;
}

.council-card:hover .council-avatar {
  transform: translateZ(30px) scale(1.08);
  box-shadow: 0 8px 24px rgba(148, 23, 34, 0.6);
}

.council-card h3 {
  font: 700 16px var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 4px;
  transform: translateZ(12px);
}

.council-card .council-role {
  font: 500 10px var(--mono);
  letter-spacing: 0.22em;
  color: var(--amber);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.council-card .council-desc {
  font: 400 12px/1.5 var(--sans);
  color: var(--bone-dim);
}

/* ===== QUICK FACTS GRID ===== */
.facts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.08);
  margin: 60px 0;
}

.fact-item {
  background: var(--void);
  padding: 28px 24px;
  position: relative;
  overflow: hidden;
  transform-style: preserve-3d;
  transition: transform 0.2s ease-out;
  will-change: transform;
}

.fact-item::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 50%, rgba(148, 23, 34, 0.15), transparent 60%);
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}

.fact-item:hover::after {
  opacity: 1;
}

.fact-icon {
  font-size: 28px;
  margin-bottom: 12px;
  display: block;
  filter: drop-shadow(0 0 8px var(--crim-glow));
  transform: translateZ(16px);
}

.fact-label {
  font: 500 10px var(--mono);
  letter-spacing: 0.2em;
  color: var(--ash);
  text-transform: uppercase;
  margin-bottom: 6px;
  display: block;
}

.fact-val {
  font: 700 clamp(18px, 2.5vw, 24px) var(--disp-sans);
  color: var(--bone);
  text-transform: uppercase;
  transform: translateZ(10px);
}

/* ===== CTA BANNER ===== */
.cta-banner {
  margin: 60px 0;
  padding: clamp(40px, 6vw, 80px);
  background:
    linear-gradient(135deg, rgba(90, 10, 17, 0.4) 0%, rgba(36, 5, 8, 0.8) 100%);
  border: 1px solid rgba(148, 23, 34, 0.5);
  text-align: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 40px var(--crim-glow);
}

.cta-banner::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 24px 24px;
  pointer-events: none;
}

.cta-banner h2 {
  font: 700 clamp(28px, 5vw, 56px) var(--serif);
  text-transform: uppercase;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
  position: relative;
  text-shadow: 0 0 30px rgba(148, 23, 34, 0.5);
}

.cta-banner p {
  font: italic 400 clamp(16px, 2vw, 22px)/1.5 var(--serif);
  color: var(--bone-dim);
  max-width: 48ch;
  margin: 0 auto 30px;
  position: relative;
}

.cta-banner .btn {
  position: relative;
}

@media (max-width: 900px) {
  .about-hero { min-height: auto; padding-top: 30px; }
  .cobweb { display: none; }
  .lore-timeline { padding-left: 30px; }
  .lore-timeline::before { left: 8px; }
  .lore-entry::before { left: -26px; width: 10px; height: 10px; }
}
"""

    main_html = """
<main id="about">
  <!-- Cobweb decorations -->
  <svg class="cobweb tl" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M0 0 L200 0 L0 200 Z" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
    <path d="M0 0 Q100 20 200 0" fill="none" stroke="currentColor" stroke-width="0.4" opacity="0.2"/>
    <path d="M0 0 Q20 100 0 200" fill="none" stroke="currentColor" stroke-width="0.4" opacity="0.2"/>
    <path d="M0 0 Q60 40 100 100" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.15"/>
    <path d="M0 0 Q40 60 100 100" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.15"/>
    <path d="M40 0 Q50 30 40 60" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.2"/>
    <path d="M0 40 Q30 50 60 40" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.2"/>
    <path d="M80 0 Q60 40 80 80" fill="none" stroke="currentColor" stroke-width="0.2" opacity="0.15"/>
    <path d="M0 80 Q40 60 80 80" fill="none" stroke="currentColor" stroke-width="0.2" opacity="0.15"/>
  </svg>
  <svg class="cobweb tr" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M0 0 L200 0 L0 200 Z" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
    <path d="M0 0 Q100 20 200 0" fill="none" stroke="currentColor" stroke-width="0.4" opacity="0.2"/>
    <path d="M0 0 Q20 100 0 200" fill="none" stroke="currentColor" stroke-width="0.4" opacity="0.2"/>
    <path d="M0 0 Q60 40 100 100" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.15"/>
    <path d="M0 0 Q40 60 100 100" fill="none" stroke="currentColor" stroke-width="0.3" opacity="0.15"/>
  </svg>

  <!-- Hero -->
  <section class="about-hero" aria-labelledby="about-title">
    <span class="eyebrow" style="color:var(--crim);">CLASSIFIED ORIGINS // THE UNTOLD MYTHOS</span>
    <h1 class="disp" id="about-title">THE LORE</h1>
    <p class="hero-desc">"Every October, the mist returns. Every October, the campus remembers what it buried beneath the amphitheatre. This is the origin of Zeitgeist."</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
      <a class="btn btn-crim" href="events.html" data-c="ARENAS"><span>ENTER THE ARENAS →</span></a>
      <a class="btn" href="contact.html" data-c="CONTACT"><span>REACH THE COUNCIL</span></a>
    </div>
  </section>

  <!-- Quick Facts -->
  <div class="facts-grid" aria-label="Festival facts">
    <div class="fact-item">
      <span class="fact-icon">🏛️</span>
      <span class="fact-label">Institution</span>
      <span class="fact-val">IIT Ropar</span>
    </div>
    <div class="fact-item">
      <span class="fact-icon">📅</span>
      <span class="fact-label">Founded</span>
      <span class="fact-val">Est. 2012</span>
    </div>
    <div class="fact-item">
      <span class="fact-icon">🌙</span>
      <span class="fact-label">Duration</span>
      <span class="fact-val">3 Nights</span>
    </div>
    <div class="fact-item">
      <span class="fact-icon">🎭</span>
      <span class="fact-label">Events</span>
      <span class="fact-val">12+ Arenas</span>
    </div>
    <div class="fact-item">
      <span class="fact-icon">🏆</span>
      <span class="fact-label">Prize Pool</span>
      <span class="fact-val">₹3,00,000+</span>
    </div>
  </div>

  <!-- Lore Timeline -->
  <section class="lore-sec" aria-labelledby="lore-title">
    <p class="eyebrow" style="color:var(--amber);">TEMPORAL RECORDS // ARCHIVES UNSEALED</p>
    <h2 class="disp" id="lore-title" style="font-size:clamp(28px, 5vw, 52px); margin-top:8px;">THE DARK CHRONICLE</h2>

    <div class="lore-timeline">
      <div class="lore-entry">
        <div class="lore-year">2012</div>
        <h3>The First Gathering</h3>
        <p>IIT Ropar was founded in 2008, and by 2012 the student body forged its first cultural festival — a modest gathering of a few hundred souls on a rain-soaked autumn evening. No one recorded what happened after midnight.</p>
      </div>

      <div class="lore-entry">
        <div class="lore-year">2015</div>
        <h3>The Amplification</h3>
        <p>Zeitgeist grew into a multi-day spectacle drawing 3,000+ participants from 30 colleges across North India. The music grew louder. The nights grew longer. The mist grew thicker around the amphitheatre.</p>
      </div>

      <div class="lore-entry">
        <div class="lore-year">2019</div>
        <h3>The Golden Epoch</h3>
        <p>With headline pronite performers, national-level competitions, and a sprawling cultural village, Zeitgeist became one of the most anticipated college festivals in the region. Attendance crossed 10,000 for the first time.</p>
      </div>

      <div class="lore-entry">
        <div class="lore-year">2020–2021</div>
        <h3>The Silent Years</h3>
        <p>The campus fell quiet. Virtual editions preserved the flame, but the grounds lay dormant under lockdown fog. Some say the silence only made what lived beneath grow restless.</p>
      </div>

      <div class="lore-entry">
        <div class="lore-year">2022–2025</div>
        <h3>The Resurgence</h3>
        <p>The festival returned with renewed fury — larger stages, international acts, and an ever-darkening aesthetic that leaned into the campus mythology. Each edition pushed boundaries further into the night.</p>
      </div>

      <div class="lore-entry">
        <div class="lore-year">2026</div>
        <h3>The Night We Never Left</h3>
        <p>ZEITGEIST'26 embraces its darkest chapter yet. Three nights of gothic cinema, ritual art, sonic exorcism, and spectral revelry. October 30 – November 01. This time, the festival dossier is fully declassified. But will you leave the grounds?</p>
      </div>
    </div>
  </section>

  <!-- Festival Council -->
  <section class="council-sec" aria-labelledby="council-title">
    <p class="eyebrow" style="color:var(--crim);">CLASSIFIED PERSONNEL // FESTIVAL COMMAND</p>
    <h2 class="disp" id="council-title" style="font-size:clamp(28px, 5vw, 52px); margin-top:8px; margin-bottom:36px;">THE COUNCIL</h2>

    <div class="council-grid">
      <div class="council-card">
        <div class="council-avatar">FC</div>
        <h3>Festival Convener</h3>
        <span class="council-role">Supreme Commander</span>
        <p class="council-desc">Oversees all festival operations, artist liaisons, security protocols, and the declassification of archival dossiers.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">CD</div>
        <h3>Creative Director</h3>
        <span class="council-role">Aesthetic Division</span>
        <p class="council-desc">Architects the visual language, stage design, and the haunted atmospheric identity across all festival sectors.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">TL</div>
        <h3>Technical Lead</h3>
        <span class="council-role">Infrastructure Core</span>
        <p class="council-desc">Commands sound engineering, lighting rigs, power distribution, and the campus-wide AV surveillance network.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">EH</div>
        <h3>Events Head</h3>
        <span class="council-role">Arena Command</span>
        <p class="council-desc">Coordinates all 12 competitive arenas, judging panels, rulebooks, and participant logistics from deployment to verdict.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">PH</div>
        <h3>Pronites Head</h3>
        <span class="council-role">Midnight Division</span>
        <p class="council-desc">Manages the headline star lineup, artist hospitality, main-stage production, and crowd control after curfew.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">MH</div>
        <h3>Marketing Head</h3>
        <span class="council-role">Signal Corps</span>
        <p class="council-desc">Deploys festival propaganda across all channels — social media, campus broadcasts, and encrypted transmissions.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">SH</div>
        <h3>Sponsorship Head</h3>
        <span class="council-role">Resource Acquisition</span>
        <p class="council-desc">Secures financial backing from corporate entities, negotiates brand integrations, and manages the festival treasury.</p>
      </div>
      <div class="council-card">
        <div class="council-avatar">WH</div>
        <h3>Web & Tech Head</h3>
        <span class="council-role">Digital Ops</span>
        <p class="council-desc">Maintains the festival web infrastructure, registration systems, live dashboards, and the digital archival vault.</p>
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <div class="cta-banner">
    <span class="eyebrow" style="color:var(--crim); margin-bottom:16px; display:block;">THE DOSSIER IS OPEN</span>
    <h2>ENTER THE GROUNDS</h2>
    <p>"Three nights. Twelve arenas. One campus sealed in mist. The night we never left begins October 30."</p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
      <a class="btn btn-crim" href="events.html" data-c="ARENAS"><span>EXPLORE EVENTS →</span></a>
      <a class="btn btn-amber" href="passes.html" data-c="PASSES"><span>GET YOUR PASS</span></a>
    </div>
  </div>
</main>
"""

    page_scripts = """
/* ===== 3D TILT — LORE ENTRIES ===== */
document.querySelectorAll('.lore-entry').forEach(entry => {
  entry.addEventListener('pointermove', e => {
    const rect = entry.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -3;
    const ry = ((x - cx) / cx) * 3;
    entry.style.transform = `perspective(1000px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(4px)`;
  });
  entry.addEventListener('pointerleave', () => {
    entry.style.transform = '';
  });
});

/* ===== 3D TILT — COUNCIL CARDS ===== */
document.querySelectorAll('.council-card').forEach(card => {
  card.addEventListener('pointermove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -6;
    const ry = ((x - cx) / cx) * 6;
    card.style.setProperty('--cx', (x / rect.width * 100) + '%');
    card.style.setProperty('--cy', (y / rect.height * 100) + '%');
    card.style.transform = `perspective(800px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(6px)`;
  });
  card.addEventListener('pointerleave', () => {
    card.style.transform = '';
  });
});

/* ===== 3D TILT — FACT ITEMS ===== */
document.querySelectorAll('.fact-item').forEach(item => {
  item.addEventListener('pointermove', e => {
    const rect = item.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -5;
    const ry = ((x - cx) / cx) * 5;
    item.style.transform = `perspective(800px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(8px)`;
  });
  item.addEventListener('pointerleave', () => {
    item.style.transform = '';
  });
});

/* ===== SCROLL REVEAL FOR LORE ENTRIES ===== */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.lore-entry, .council-card, .fact-item').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
  observer.observe(el);
});
"""
    return title, description, extra_css, main_html, page_scripts
