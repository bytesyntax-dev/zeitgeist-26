# Generator for pronites.html (The Midnight Lineup - Headline Star Nights)

def get_pronites_content():
    title = "The Midnight Lineup — Pronites | ZEITGEIST'26 | IIT Ropar"
    description = "Three nights of auditory exorcism. Experience headline rock bands, international EDM DJs, and grand Bollywood vocalists at ZEITGEIST'26."

    extra_css = """
/* Pronites Lineup Styles */
.lineup-hero {
  margin-bottom: 50px;
}

.lineup-hero h1 {
  font-size: clamp(40px, 8vw, 90px);
  margin-top: 14px;
}

.lineup-hero p {
  color: var(--bone-dim);
  font: italic 400 clamp(18px, 2.5vw, 28px) var(--serif);
  max-width: 38ch;
  margin-top: 12px;
}

.lineup-grid {
  display: grid;
  gap: 60px;
  margin-bottom: 80px;
  perspective: 1400px;
}

.lineup-card {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: clamp(24px, 4vw, 56px);
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: clamp(24px, 4vw, 44px);
  position: relative;
  overflow: hidden;
  align-items: center;
  transform-style: preserve-3d;
  transition: transform 0.15s ease-out, border-color 0.4s, box-shadow 0.4s;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
}

.lineup-card .lineup-glare {
  position: absolute;
  inset: -50%;
  pointer-events: none;
  background: radial-gradient(circle 350px at var(--mx, 50%) var(--my, 50%), rgba(255, 255, 255, 0.12), rgba(165, 29, 41, 0.15) 35%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s;
  mix-blend-mode: screen;
  z-index: 10;
}

.lineup-card:hover .lineup-glare {
  opacity: 1;
}

.lineup-card:hover {
  border-color: var(--crim);
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 0 0 40px var(--crim-glow);
}

.lineup-card:nth-child(even) {
  grid-template-columns: 1fr 1.1fr;
}

.lineup-card:nth-child(even) .lineup-img-wrap {
  order: 2;
}

.lineup-img-wrap {
  position: relative;
  aspect-ratio: 16 / 11;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: var(--char);
  transform: translateZ(30px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
}

.lineup-card:hover .lineup-img-wrap {
  transform: translateZ(44px);
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.95), 0 0 30px var(--crim-glow);
}

.lineup-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(85%) contrast(120%) brightness(0.85);
  transition: transform 0.6s ease, filter 0.6s ease;
}

.lineup-card:hover .lineup-img-wrap img {
  transform: scale(1.06);
  filter: grayscale(0%) contrast(110%) brightness(0.95);
}

.lineup-overlay-badge {
  position: absolute;
  top: 16px;
  left: 16px;
  background: rgba(4, 3, 4, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid var(--crim);
  color: var(--crim-bright);
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  padding: 6px 12px;
  text-transform: uppercase;
  transform: translateZ(48px);
}

.lineup-info-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font: 500 11px var(--mono);
  letter-spacing: 0.25em;
  color: var(--amber);
  text-transform: uppercase;
  margin-bottom: 12px;
  transform: translateZ(28px);
}

.lineup-card h2 {
  font: 700 clamp(28px, 4vw, 44px)/1 var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 14px;
  transform: translateZ(32px);
}

.lineup-artist-name {
  font: italic 600 clamp(20px, 2.5vw, 26px) var(--serif);
  color: var(--bone);
  margin-bottom: 16px;
  display: block;
  transform: translateZ(26px);
}

.lineup-desc {
  color: var(--bone-dim);
  font: 400 13px/1.7 var(--sans);
  margin-bottom: 24px;
  max-width: 52ch;
  transform: translateZ(20px);
}

.lineup-meta-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 20px;
  margin-bottom: 28px;
  font: 400 11px var(--mono);
  transform: translateZ(24px);
}

.lineup-action-wrap {
  transform: translateZ(32px);
}

/* 3D Audio Equalizer Spectrum */
.lineup-eq-3d {
  display: inline-flex;
  align-items: flex-end;
  gap: 4px;
  height: 18px;
  margin-left: 10px;
  vertical-align: middle;
  transform: translateZ(36px);
}

.lineup-eq-3d span {
  width: 3px;
  height: 100%;
  background: var(--crim-bright);
  box-shadow: 0 0 8px var(--crim-glow);
  transform-origin: bottom;
  animation: eqBounce 1.2s ease-in-out infinite alternate;
}

.lineup-eq-3d span:nth-child(1) { height: 40%; animation-delay: 0.1s; }
.lineup-eq-3d span:nth-child(2) { height: 95%; animation-delay: 0.35s; }
.lineup-eq-3d span:nth-child(3) { height: 60%; animation-delay: 0.18s; }
.lineup-eq-3d span:nth-child(4) { height: 100%; animation-delay: 0.45s; }
.lineup-eq-3d span:nth-child(5) { height: 50%; animation-delay: 0.22s; }

@keyframes eqBounce {
  0% { transform: scaleY(0.2); }
  100% { transform: scaleY(1); }
}

.lineup-meta-list dt {
  color: var(--ash);
  font-size: 9px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.lineup-meta-list dd {
  font-size: 13px;
  color: var(--bone);
  font-weight: 500;
}

.guidelines-box {
  background: rgba(20, 17, 19, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: clamp(28px, 4vw, 44px);
  margin-bottom: 80px;
}

.guidelines-box h3 {
  font: 700 22px var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 20px;
  color: var(--amber);
}

.guidelines-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
  font: 400 12px/1.6 var(--mono);
  color: var(--bone-dim);
}

.guidelines-grid div strong {
  display: block;
  color: var(--bone);
  margin-bottom: 6px;
  font-size: 13px;
  letter-spacing: 0.1em;
}

@media (max-width: 900px) {
  .lineup-card, .lineup-card:nth-child(even) {
    grid-template-columns: 1fr;
  }
  .lineup-card:nth-child(even) .lineup-img-wrap {
    order: 0;
  }
}
"""

    main_html = """
<main id="pronites">
  <div class="lineup-hero">
    <span class="eyebrow" style="color:var(--crim);">THE CELEBRITY ARENA // MMXXVI</span>
    <h1 class="disp">THE MIDNIGHT LINEUP</h1>
    <p>"When the Punjab sun sinks beyond the Sutlej River, the main festival arena transforms under blinding strobes and thunderous sub-bass."</p>
  </div>

  <div class="lineup-grid">
    <!-- Night 01: Rock & Metal -->
    <article class="lineup-card" aria-label="Night 01 Pronite">
      <div class="lineup-glare" aria-hidden="true"></div>
      <div class="lineup-img-wrap">
        <img src="assets/pronites/artist_1.webp" alt="Rock Band Headliner at Zeitgeist" loading="lazy">
        <span class="lineup-overlay-badge">OCTOBER 30 // 08:30 PM</span>
      </div>
      <div>
        <div class="lineup-info-badge">
          NIGHT 01 · ROCK & METAL ARENA
          <span class="lineup-eq-3d" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></span>
        </div>
        <h2>NIRVANA'S ECLIPSE</h2>
        <span class="lineup-artist-name">THE LOST PARIAHS & EASTERN METAL ENSEMBLE</span>
        <p class="lineup-desc">
          An electrifying headline assault of progressive post-rock and crushing alt-metal rhythms. Twin electric guitars, full stage fire cannons, and haunting gothic vocals echoing across the Open Air Amphitheatre.
        </p>
        <dl class="lineup-meta-list">
          <div><dt>ARENA VENUE</dt><dd>Open Air Amphitheatre (Sector 03)</dd></div>
          <div><dt>GATES OPEN</dt><dd>06:30 PM</dd></div>
          <div><dt>STAGE DURATION</dt><dd>150 Minutes</dd></div>
          <div><dt>ENTRY PROTOCOL</dt><dd>Pronite Pass Required</dd></div>
        </dl>
        <div class="lineup-action-wrap" style="display:flex; gap:12px; flex-wrap:wrap;">
          <a class="btn btn-crim" href="passes.html" data-c="PASS"><span>CLAIM PRONITE PASS</span></a>
          <button class="btn-mini" type="button" onclick="playChime(180); toast('SOUNDCHECK 01: 44.1 kHz STEREO CONFIRMED.');" data-c="SOUNDCHECK">🔊 SOUNDCHECK</button>
        </div>
      </div>
    </article>

    <!-- Night 02: EDM Rave -->
    <article class="lineup-card" aria-label="Night 02 Pronite">
      <div class="lineup-glare" aria-hidden="true"></div>
      <div class="lineup-img-wrap">
        <img src="assets/pronites/artist_2.webp" alt="EDM DJ Producer at Zeitgeist" loading="lazy">
        <span class="lineup-overlay-badge">OCTOBER 31 // 09:00 PM</span>
      </div>
      <div>
        <div class="lineup-info-badge" style="color:var(--crim-bright);">
          NIGHT 02 · HALLOWEEN MIDNIGHT RAVE
          <span class="lineup-eq-3d" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></span>
        </div>
        <h2>THE PHANTOM RAVE</h2>
        <span class="lineup-artist-name">KRYPTIC PHANTOM & GUEST ELECTRONIC PRODUCERS</span>
        <p class="lineup-desc">
          A full-scale audiovisual invasion. Powered by an unyielding 60-foot LED monolith, cryogenic fog jets, and synchronized laser grid choreography. Prepare for four relentless hours of bone-shaking bass.
        </p>
        <dl class="lineup-meta-list">
          <div><dt>ARENA VENUE</dt><dd>Main Sports Complex (Sector 01)</dd></div>
          <div><dt>GATES OPEN</dt><dd>07:00 PM</dd></div>
          <div><dt>STAGE DURATION</dt><dd>240 Minutes</dd></div>
          <div><dt>ENTRY PROTOCOL</dt><dd>Wristband & Clearance Scan</dd></div>
        </dl>
        <div class="lineup-action-wrap" style="display:flex; gap:12px; flex-wrap:wrap;">
          <a class="btn btn-crim" href="passes.html" data-c="PASS"><span>CLAIM PRONITE PASS</span></a>
          <button class="btn-mini" type="button" onclick="playGlitch(); toast('SUB-BASS TRANSDUCERS ENGAGED: 32Hz BASS HIT.');" data-c="BASS">⚡ BASS HIT</button>
        </div>
      </div>
    </article>

    <!-- Night 03: Bollywood Grand Finale -->
    <article class="lineup-card" aria-label="Night 03 Pronite">
      <div class="lineup-glare" aria-hidden="true"></div>
      <div class="lineup-img-wrap">
        <img src="assets/pronites/artist_3.webp" alt="Bollywood Sensation at Zeitgeist" loading="lazy">
        <span class="lineup-overlay-badge">NOVEMBER 01 // 08:00 PM</span>
      </div>
      <div>
        <div class="lineup-info-badge">
          NIGHT 03 · GRAND BOLLYWOOD FINALE
          <span class="lineup-eq-3d" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></span>
        </div>
        <h2>SYMPHONY OF SOULS</h2>
        <span class="lineup-artist-name">AARYAV & 16-PIECE STRINGS ORCHESTRA</span>
        <p class="lineup-desc">
          The festival's emotional farewell. Chart-topping Bollywood anthems merged seamlessly with classical Sufi crescendo and live violins under midnight candle flame. A collective singing ritual under the Punjab stars.
        </p>
        <dl class="lineup-meta-list">
          <div><dt>ARENA VENUE</dt><dd>Senate Amphitheatre (Sector 02)</dd></div>
          <div><dt>GATES OPEN</dt><dd>06:00 PM</dd></div>
          <div><dt>STAGE DURATION</dt><dd>180 Minutes</dd></div>
          <div><dt>ENTRY PROTOCOL</dt><dd>All-Access / VIP Pass</dd></div>
        </dl>
        <div class="lineup-action-wrap" style="display:flex; gap:12px; flex-wrap:wrap;">
          <a class="btn btn-crim" href="passes.html" data-c="PASS"><span>CLAIM PRONITE PASS</span></a>
          <button class="btn-mini" type="button" onclick="playChime(440); toast('ORCHESTRAL A4 TUNING CONFIRMED.');" data-c="TUNE">🎻 TUNE</button>
        </div>
      </div>
    </article>
  </div>

  <!-- Pronite Guidelines Box -->
  <div class="guidelines-box">
    <h3>PRONITE SECTOR PROTOCOLS & SAFETY DIRECTIVES</h3>
    <div class="guidelines-grid">
      <div>
        <strong>01. ACCREDITATION VERIFICATION</strong>
        Every attendee must wear their verified RFID festival wristband issued at Sector 01 (Main Gate Checkpoint). Tampered or detached wristbands are immediately invalid.
      </div>
      <div>
        <strong>02. BAGGAGE & PROHIBITED GEAR</strong>
        Laser pointers, glass containers, aerosol sprays, alcohol, and contraband substances are strictly forbidden. Campus security and local police frisking active at all perimeter portals.
      </div>
      <div>
        <strong>03. MEDICAL & STROBE ADVISORY</strong>
        Night 02 (The Phantom Rave) contains intense high-frequency strobe lights and dense theatrical fog. Paramedic units and ambulances on standby at Sector 01 and Sector 03.
      </div>
      <div>
        <strong>04. MIDNIGHT GATES CLOSURE</strong>
        Curfew enforcement begins at 01:30 AM across hostel corridors. Outstation attendees must carry their hostel clearance docket and college photo identification.
      </div>
    </div>
  </div>
</main>
"""

    page_scripts = """
// 3D Lineup Card Tilt Physics
document.querySelectorAll('.lineup-card').forEach(card => {
  card.addEventListener('pointermove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -6;
    const ry = ((x - cx) / cx) * 6;
    card.style.transform = `perspective(1200px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(14px)`;
    card.style.setProperty('--mx', `${(x / rect.width * 100).toFixed(1)}%`);
    card.style.setProperty('--my', `${(y / rect.height * 100).toFixed(1)}%`);
  });
  card.addEventListener('pointerleave', () => {
    card.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
  });
});
"""
    return title, description, extra_css, main_html, page_scripts
