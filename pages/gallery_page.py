# Generator for gallery.html (The Classified Archives - Polaroids Lightbox & VHS Tape)

def get_gallery_content():
    title = "The Lost Archives — Recovered Footage & Polaroids | ZEITGEIST'26 | IIT Ropar"
    description = "Declassified recovered photographic evidence, 1986 polaroids, and surveillance logs from the archives of ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Gallery & Polaroids Styles */
.gallery-hero {
  margin-bottom: 40px;
}

.gallery-hero h1 {
  font-size: clamp(38px, 7vw, 86px);
  margin-top: 14px;
}

.polaroid-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 36px 28px;
  margin-bottom: 80px;
  perspective: 1200px;
}

.polaroid-card {
  background: #ede6d8;
  padding: 16px 16px 36px 16px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9), 0 0 10px rgba(0,0,0,0.5);
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.15s ease-out, box-shadow 0.3s ease;
  cursor: pointer;
  will-change: transform;
}

.polaroid-card:nth-child(1) { --base-rot: -2deg; transform: rotate(-2deg); }
.polaroid-card:nth-child(2) { --base-rot: 2.5deg; transform: rotate(2.5deg); }
.polaroid-card:nth-child(3) { --base-rot: -1.5deg; transform: rotate(-1.5deg); }
.polaroid-card:nth-child(4) { --base-rot: 1.8deg; transform: rotate(1.8deg); }

.polaroid-card:hover {
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 0 0 30px var(--crim-glow);
  z-index: 10;
}

.polaroid-tape {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%) translateZ(30px);
  width: 70px;
  height: 24px;
  background: rgba(220, 210, 190, 0.7);
  box-shadow: 0 3px 6px rgba(0,0,0,0.35);
  z-index: 5;
}

.polaroid-img-wrap {
  aspect-ratio: 1 / 1;
  overflow: hidden;
  background: #111;
  transform: translateZ(16px);
  box-shadow: inset 0 0 15px rgba(0,0,0,0.5), 0 4px 12px rgba(0,0,0,0.4);
}

.polaroid-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: sepia(35%) contrast(120%) brightness(0.9);
  transition: filter 0.4s ease, transform 0.4s ease;
}

.polaroid-card:hover .polaroid-img-wrap img {
  filter: sepia(0%) contrast(110%) brightness(1);
  transform: scale(1.03);
}

.polaroid-caption {
  font: 700 13px/1.3 var(--mono);
  color: #1a1618;
  margin-top: 14px;
  letter-spacing: 0.05em;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  transform: translateZ(22px);
}

.polaroid-date {
  font-size: 10px;
  color: #7a151e;
  font-weight: 500;
}

/* VHS Surveillance Screen */
.vhs-section {
  background: #090608;
  border: 1px solid rgba(148, 23, 34, 0.5);
  padding: clamp(24px, 4vw, 48px);
  margin-bottom: 80px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.9), inset 0 0 40px rgba(148, 23, 34, 0.15);
}

.crt-monitor {
  background: #040304;
  border: 2px solid #240508;
  aspect-ratio: 16 / 9;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 24px;
  margin-bottom: 24px;
}

.crt-monitor::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(rgba(18, 16, 16, 0) 0px, rgba(18, 16, 16, 0) 2px, rgba(0, 0, 0, 0.4) 3px, rgba(0, 0, 0, 0.4) 4px);
  pointer-events: none;
  opacity: 0.6;
}

.vhs-header {
  display: flex;
  justify-content: space-between;
  font: 700 12px var(--mono);
  letter-spacing: 0.25em;
  color: #2ecc71;
  text-transform: uppercase;
  z-index: 2;
}

.vhs-rec {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--crim-bright);
}

.rec-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--crim-bright);
  animation: pulse-dot 1.2s infinite;
}

.vhs-center-text {
  text-align: center;
  z-index: 2;
}

.vhs-center-text h3 {
  font: 700 clamp(24px, 4vw, 42px) var(--disp-sans);
  color: var(--bone);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-shadow: 2px 2px 0 var(--crim);
}

.vhs-center-text p {
  font: 400 12px var(--mono);
  color: var(--ash);
  margin-top: 8px;
  letter-spacing: 0.2em;
}

.vhs-footer {
  display: flex;
  justify-content: space-between;
  font: 500 11px var(--mono);
  color: var(--amber);
  z-index: 2;
}

.vhs-controls {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 260;
  background: rgba(4, 3, 4, 0.94);
  backdrop-filter: blur(16px);
  display: grid;
  place-items: center;
  padding: 30px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.lightbox-modal.open {
  opacity: 1;
  pointer-events: auto;
}

.lightbox-content {
  background: #ede6d8;
  padding: 20px 20px 40px 20px;
  max-width: 580px;
  width: 100%;
  box-shadow: 0 24px 70px rgba(0,0,0,0.9);
  position: relative;
}

.lightbox-close {
  position: absolute;
  top: -46px;
  right: 0;
  color: var(--bone);
  font: 700 24px var(--mono);
}

.lightbox-img-wrap {
  aspect-ratio: 1 / 1;
  overflow: hidden;
  background: #000;
}

.lightbox-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lightbox-details {
  margin-top: 18px;
  color: #141113;
}

.lightbox-details h4 {
  font: 700 18px var(--mono);
  letter-spacing: 0.05em;
}

.lightbox-details p {
  font: 400 12px/1.5 var(--mono);
  color: #555;
  margin-top: 6px;
}
"""

    main_html = """
<main id="gallery">
  <div class="gallery-hero">
    <span class="eyebrow" style="color:var(--crim);">DECLASSIFIED SURVEILLANCE & RECOVERED EVIDENCE</span>
    <h1 class="disp">THE LOST ARCHIVES</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Recovered photographic artifacts, lost tapes, and decrypted transmissions from 1986 to the present night.</p>
  </div>

  <!-- Polaroids Grid -->
  <div class="polaroid-grid">
    <!-- Polaroid 1 -->
    <article class="polaroid-card" onclick="openLightbox('assets/gallery/polaroid_1.webp', 'SECTOR 04 // THE NIGHT REHEARSAL', 'OCTOBER 31, 1986 · 02:40 AM', 'Recovered negative from the unpaved amphitheatre grounds. Stage lighting active under dense Punjab fog.')" data-c="ZOOM">
      <div class="polaroid-tape"></div>
      <div class="polaroid-img-wrap">
        <img src="assets/gallery/polaroid_1.webp" alt="Archival Polaroid 1" loading="lazy">
      </div>
      <div class="polaroid-caption">
        <span>SECTOR 04 // 02:40 AM</span>
        <span class="polaroid-date">OCT 31, 1986</span>
      </div>
    </article>

    <!-- Polaroid 2 -->
    <article class="polaroid-card" onclick="openLightbox('assets/gallery/polaroid_2.webp', 'THE LOST CHOIR // SOUNDCHECK', 'NOVEMBER 01, 1986 · 01:15 AM', 'Dramatics contingent rehearsing under candle fire along the Sutlej river bank. None of the participants returned for morning reporting.')" data-c="ZOOM">
      <div class="polaroid-tape"></div>
      <div class="polaroid-img-wrap">
        <img src="assets/gallery/polaroid_2.webp" alt="Archival Polaroid 2" loading="lazy">
      </div>
      <div class="polaroid-caption">
        <span>THE CHOIR REHEARSAL</span>
        <span class="polaroid-date">NOV 01, 1986</span>
      </div>
    </article>

    <!-- Polaroid 3 -->
    <article class="polaroid-card" onclick="openLightbox('assets/gallery/polaroid_3.webp', 'OLD SENATE ENTRANCE // ANOMALY', 'OCTOBER 30, 1996 · 11:58 PM', 'Long exposure capture outside the Senate complex. Note the light distortion along the perimeter fencing.')" data-c="ZOOM">
      <div class="polaroid-tape"></div>
      <div class="polaroid-img-wrap">
        <img src="assets/gallery/polaroid_3.webp" alt="Archival Polaroid 3" loading="lazy">
      </div>
      <div class="polaroid-caption">
        <span>SENATE PERIMETER</span>
        <span class="polaroid-date">OCT 30, 1996</span>
      </div>
    </article>

    <!-- Polaroid 4 -->
    <article class="polaroid-card" onclick="openLightbox('assets/gallery/polaroid_4.webp', 'THE FINAL EXIT // SEALED', 'OCTOBER 31, 2016 · 03:00 AM', 'Security checkpoint footage. Gates remained locked from the inside during the midnight blackout.')" data-c="ZOOM">
      <div class="polaroid-tape"></div>
      <div class="polaroid-img-wrap">
        <img src="assets/gallery/polaroid_4.webp" alt="Archival Polaroid 4" loading="lazy">
      </div>
      <div class="polaroid-caption">
        <span>CHECKPOINT 01 // LOCKED</span>
        <span class="polaroid-date">OCT 31, 2016</span>
      </div>
    </article>
  </div>

  <!-- Simulated VHS Surveillance Monitor -->
  <section class="vhs-section" aria-labelledby="vhs-title">
    <span class="eyebrow" style="color:var(--crim);">SURVEILLANCE TAPE 09-B // RPR CCTV</span>
    <h2 class="disp-sans" id="vhs-title" style="font-size:20px; margin: 8px 0 20px;">CAMPUS SECURITY INTERCEPT</h2>

    <div class="crt-monitor">
      <div class="vhs-header">
        <div class="vhs-rec"><span class="rec-dot"></span><span>REC ●</span></div>
        <div>PLAY ► SP [00:41:26]</div>
        <div>CH 04 // SUTLEJ SECTOR</div>
      </div>

      <div class="vhs-center-text">
        <h3 id="vhs-status-text">NO EXIT DETECTED</h3>
        <p>FREQUENCY: 88.4 MHz · MIST PENETRATION 92%</p>
      </div>

      <div class="vhs-footer">
        <span>OCT 31, 1986 // 02:44:18 AM</span>
        <span>SECURITY CLEARANCE: OMEGA</span>
      </div>
    </div>

    <div class="vhs-controls">
      <button class="btn btn-crim" type="button" id="vhs-play-btn" data-c="PLAY"><span>► REWIND ARCHIVE TAPE</span></button>
      <button class="btn-mini" type="button" id="vhs-static-btn" data-c="STATIC">⚡ BURST STATIC NOISE</button>
      <button class="btn-mini" type="button" onclick="toast('RADIO TRANSCRIPT: [SUTLEJ TOWER] THEY ARE STILL ON THE FIELD.'); playChime(150);" data-c="DECRYPT">📻 DECRYPT AUDIO LOG</button>
    </div>
  </section>
</main>

<!-- Lightbox Modal -->
<div class="lightbox-modal" id="lightbox" role="dialog" aria-modal="true" hidden>
  <div class="lightbox-content">
    <button class="lightbox-close" id="lightbox-close-btn" type="button" aria-label="Close image" data-c="DISMISS">✕</button>
    <div class="lightbox-img-wrap">
      <img id="lightbox-img" src="" alt="Zoomed Polaroid">
    </div>
    <div class="lightbox-details">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <h4 id="lightbox-title">TITLE</h4>
        <span class="polaroid-date" id="lightbox-date">DATE</span>
      </div>
      <p id="lightbox-desc">Description</p>
    </div>
  </div>
</div>
"""

    page_scripts = """
/* Gallery Lightbox & VHS Simulation */
function openLightbox(src, title, date, desc) {
  const modal = document.getElementById("lightbox");
  document.getElementById("lightbox-img").src = src;
  document.getElementById("lightbox-title").textContent = title;
  document.getElementById("lightbox-date").textContent = date;
  document.getElementById("lightbox-desc").textContent = desc;

  modal.hidden = false;
  void modal.offsetWidth;
  modal.classList.add("open");
  playChime(360);
}

function closeLightbox() {
  const modal = document.getElementById("lightbox");
  modal.classList.remove("open");
  setTimeout(() => { modal.hidden = true; }, 300);
  playClick(400);
}

document.getElementById("lightbox-close-btn").onclick = closeLightbox;
document.getElementById("lightbox").onclick = e => {
  if (e.target === document.getElementById("lightbox")) closeLightbox();
};

document.addEventListener("keydown", e => {
  if (e.key === "Escape" && !document.getElementById("lightbox").hidden) closeLightbox();
});

// VHS Controls
document.getElementById("vhs-play-btn").onclick = () => {
  playGlitch();
  const txt = document.getElementById("vhs-status-text");
  txt.textContent = "REWINDING TAPE...";
  toast("VHS MOTOR ENGAGED: REWINDING 1986 ARCHIVE.");
  setTimeout(() => {
    txt.textContent = "FOOTAGE RECOVERED // OCTOBER 31";
    playChime(220);
  }, 1200);
};

document.getElementById("vhs-static-btn").onclick = () => {
  playGlitch();
  const crt = document.querySelector(".crt-monitor");
  crt.style.filter = "invert(1) contrast(200%)";
  setTimeout(() => { crt.style.filter = ""; }, 180);
  toast("ANALOG TAPE STATIC DISCHARGE.");
};

// 3D Polaroid Physics & Cursor Tilt
document.querySelectorAll('.polaroid-card').forEach(card => {
  const baseRot = parseFloat(getComputedStyle(card).getPropertyValue('--base-rot')) || 0;
  card.addEventListener('pointermove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -12;
    const ry = ((x - cx) / cx) * 12;
    card.style.transform = `perspective(1000px) rotate(${baseRot}deg) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(24px) scale(1.05)`;
  });
  card.addEventListener('pointerleave', () => {
    card.style.transform = `perspective(1000px) rotate(${baseRot}deg) rotateX(0deg) rotateY(0deg) translateZ(0px) scale(1)`;
  });
});

// 3D CRT Monitor Scanline / Glass Curvature Tilt
const crt = document.querySelector('.crt-monitor');
if (crt) {
  crt.style.transition = 'transform 0.15s ease-out';
  crt.addEventListener('pointermove', e => {
    const rect = crt.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -5;
    const ry = ((x - cx) / cx) * 5;
    crt.style.transform = `perspective(800px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg)`;
  });
  crt.addEventListener('pointerleave', () => {
    crt.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg)';
  });
}
"""
    return title, description, extra_css, main_html, page_scripts
