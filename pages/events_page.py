# Generator for events.html (The Archives - 12 Competitive Arenas)

def get_events_content():
    title = "The Archives — Events | ZEITGEIST'26 | IIT Ropar"
    description = "Declassified competitive arenas, rulebooks, and registration dockets for ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Events Specific Styles */
.cat-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 24px 0 10px;
  margin-top: 16px;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}

.cat-chips::-webkit-scrollbar {
  display: none;
}

.chip {
  flex-shrink: 0;
  padding: 8px 16px;
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.1);
  font: 500 10px var(--mono);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ash);
  transition: all 0.3s;
}

.chip:hover {
  color: var(--bone);
  border-color: rgba(255, 255, 255, 0.3);
}

.chip.active {
  background: var(--surface);
  border-color: var(--crim);
  color: var(--bone);
  box-shadow: 0 0 12px var(--crim-glow);
}

.fb {
  position: sticky;
  top: calc(60px + env(safe-area-inset-top, 0px));
  z-index: 70;
  background: rgba(4, 3, 4, 0.95);
  backdrop-filter: blur(14px);
  padding: 16px 0;
  border-block: 1px solid rgba(255, 255, 255, 0.08);
  display: grid;
  grid-template-columns: 2fr repeat(5, 1fr) auto;
  gap: 10px;
}

.fb input, .fb select {
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0 14px;
  min-height: 46px;
  width: 100%;
  border-radius: 0;
  font: 400 12px var(--mono);
  appearance: none;
  color: var(--bone);
  transition: border-color 0.3s, background 0.3s;
}

.fb input:focus, .fb select:focus {
  border-color: var(--crim);
  background: var(--surface);
}

.fb select {
  background-image: linear-gradient(45deg, transparent 50%, var(--ash) 50%), linear-gradient(135deg, var(--ash) 50%, transparent 50%);
  background-position: calc(100% - 16px) 20px, calc(100% - 11px) 20px;
  background-size: 5px 5px;
  background-repeat: no-repeat;
  padding-right: 28px;
}

.fb input::placeholder {
  color: var(--ash);
}

.fb button {
  padding: 0 16px;
  min-height: 46px;
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--ash);
  border: 1px solid rgba(255, 255, 255, 0.12);
  text-transform: uppercase;
  transition: color 0.3s, border-color 0.3s;
  white-space: nowrap;
}

.fb button:hover {
  color: var(--bone);
  border-color: var(--crim);
}

.cnt-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 24px 0 18px;
  flex-wrap: wrap;
  gap: 12px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.ev {
  grid-column: span 6;
  background: var(--void);
  padding: clamp(20px, 2.5vw, 32px);
  min-height: 220px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  transition: background 0.5s, box-shadow 0.4s, transform 0.15s ease-out;
  animation: in 0.6s both;
  transform-style: preserve-3d;
  will-change: transform;
}

.ev.w { grid-column: span 7; }
.ev.n { grid-column: span 5; }

@keyframes in {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.ev::before {
  content: attr(data-n);
  position: absolute;
  right: -0.05em;
  top: -0.22em;
  font: 700 clamp(48px, 6vw, 84px)/1 var(--serif);
  opacity: 0.04;
  color: var(--bone);
  transition: color 0.5s, transform 0.6s, opacity 0.5s;
  pointer-events: none;
}

.ev .card-glare {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s;
  background: radial-gradient(circle 280px at var(--gx, 50%) var(--gy, 50%), rgba(148, 23, 34, 0.22), rgba(173, 95, 38, 0.06) 50%, transparent 80%);
  z-index: 1;
}

.ev:hover .card-glare {
  opacity: 1;
}

.ev:hover {
  background: var(--surface-hover);
  box-shadow: inset 0 0 0 1px rgba(148, 23, 34, 0.5), 0 12px 36px rgba(0, 0, 0, 0.7);
}

.ev:hover::before {
  color: var(--crim);
  opacity: 0.15;
  transform: translateX(-12px);
}

.ev > * {
  position: relative;
  z-index: 2;
}

.ev h2 {
  font: 700 clamp(18px, 2vw, 24px)/1.08 var(--disp-sans);
  text-transform: uppercase;
  margin: 12px 0 18px;
  transition: transform 0.4s, color 0.3s;
}

.ev:hover h2 {
  transform: translateX(8px);
  color: var(--bone);
}

.mt {
  display: flex;
  gap: 8px 24px;
  flex-wrap: wrap;
  color: var(--bone-dim);
  font: 400 12px var(--mono);
}

.tags {
  display: flex;
  gap: 8px;
  margin-top: 22px;
  align-items: center;
  flex-wrap: wrap;
}

.tg {
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 5px 10px;
  font: 500 9px var(--mono);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ash);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.tg.Open {
  border-color: rgba(173, 95, 38, 0.6);
  color: var(--amber);
}

.tg.Open .beacon {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--amber);
  animation: beacon-ping 1.8s infinite;
}

@keyframes beacon-ping {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.6); opacity: 0.4; }
  100% { transform: scale(1); opacity: 1; }
}

.tg.Soon { border-color: var(--ash); }
.tg.Closed { opacity: 0.45; }

.tg.registered {
  border-color: #27ae60;
  color: #2ecc71;
  background: rgba(39, 174, 96, 0.1);
}

.tg.prize {
  border-color: rgba(148, 23, 34, 0.45);
  color: var(--crim);
}

.ar {
  margin-left: auto;
  font-size: 18px;
  transition: transform 0.4s, color 0.3s;
  color: var(--ash);
}

.ev:hover .ar {
  transform: translateX(8px);
  color: var(--crim);
}

/* Detail View Styles */
.detail-nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 24px;
}

.back {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 0;
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--ash);
  transition: color 0.3s;
}

.back:hover {
  color: var(--bone);
}

.detail-actions {
  display: flex;
  gap: 12px;
}

.detail-hero {
  will-change: transform;

  aspect-ratio: 24 / 9;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: linear-gradient(135deg, #090608 0%, #170d10 50%, #080507 100%);
  display: flex;
  align-items: flex-end;
  padding: clamp(24px, 4vw, 48px);
}

.detail-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 32px 32px;
  pointer-events: none;
}

.detail-hero-reticle {
  position: absolute;
  top: 20px;
  right: 24px;
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--crim);
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: right;
}

.detail-hero-tag {
  font: 700 clamp(48px, 9vw, 110px)/0.8 var(--serif);
  color: rgba(226, 219, 206, 0.05);
  position: absolute;
  left: 20px;
  top: 10px;
  pointer-events: none;
  text-transform: uppercase;
  white-space: nowrap;
}

.detail-hero-caption {
  position: relative;
  z-index: 2;
  font: 500 11px var(--mono);
  letter-spacing: 0.28em;
  color: var(--ash);
  text-transform: uppercase;
}

.dt {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: clamp(30px, 6vw, 90px);
  margin-top: clamp(36px, 5vw, 60px);
  align-items: start;
}

.dt h2 {
  font: 500 10px var(--mono);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--amber);
  margin: 44px 0 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.dt h2::after {
  content: "";
  height: 1px;
  flex: 1;
  background: rgba(173, 95, 38, 0.2);
}

.dt h2:first-child { margin-top: 0; }
.dt p, .dt li { color: var(--bone-dim); max-width: 66ch; line-height: 1.7; }
.dt ol { padding-left: 24px; display: grid; gap: 12px; }
.dt ol li::marker { color: var(--crim); font-family: var(--mono); }

.tl {
  list-style: none;
  padding: 0 !important;
  border-left: 1px solid rgba(148, 23, 34, 0.4);
}

.tl li {
  padding: 0 0 24px 24px;
  position: relative;
  display: flex;
  gap: 20px;
}

.tl li::before {
  content: "";
  position: absolute;
  left: -4px;
  top: 8px;
  width: 7px;
  height: 7px;
  background: var(--crim);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--crim);
}

.tl b {
  color: var(--bone);
  min-width: 90px;
  font-family: var(--mono);
  font-weight: 500;
  font-size: 13px;
}

aside {
  position: sticky;
  top: 100px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(14, 11, 13, 0.9);
  backdrop-filter: blur(14px);
  padding: clamp(24px, 3.2vw, 38px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6);
}

.ds {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px 16px;
  margin: 24px 0 32px;
}

.ds dt {
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--ash);
  text-transform: uppercase;
}

.ds dd {
  font: 700 20px/1.2 var(--serif);
  text-transform: uppercase;
  word-break: break-word;
  color: var(--bone);
  margin-top: 4px;
}

.pn {
  display: flex;
  justify-content: space-between;
  margin-top: clamp(60px, 8vw, 100px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 30px;
  gap: 18px;
}

.pn a {
  font: 700 clamp(16px, 2vw, 22px) var(--serif);
  text-transform: uppercase;
  transition: color 0.3s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.pn a:hover { color: var(--crim); }
.rbar { display: none; }

/* Registration Modal */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 250;
  background: rgba(4, 3, 4, 0.88);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  display: grid;
  place-items: center;
  padding: var(--pad);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.modal-backdrop.open {
  opacity: 1;
  pointer-events: auto;
}

.modal-window {
  background: #0d0a0c;
  border: 1px solid rgba(148, 23, 34, 0.6);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9), 0 0 30px var(--crim-glow);
  width: 100%;
  max-width: 620px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  padding: clamp(24px, 4vw, 44px);
  transform: translateY(24px) scale(0.97);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-backdrop.open .modal-window {
  transform: translateY(0) scale(1);
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 36px;
  height: 36px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: grid;
  place-items: center;
  font: 400 16px var(--mono);
  color: var(--ash);
  transition: all 0.3s;
}

.modal-close:hover {
  border-color: var(--crim);
  color: var(--bone);
}

.modal-head {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 20px;
  margin-bottom: 24px;
}

.modal-head h3 {
  font: 700 clamp(20px, 3vw, 28px) var(--disp-sans);
  text-transform: uppercase;
  margin-top: 8px;
  color: var(--bone);
}

.modal-meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  padding: 14px;
  margin-bottom: 24px;
  font: 400 11px var(--mono);
}

.modal-meta-grid div span {
  color: var(--ash);
  display: block;
  font-size: 9px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.modal-form { display: grid; gap: 18px; }
.field-group { display: grid; gap: 6px; }

.field-group label {
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--ash);
}

.field-group input, .field-group select {
  background: #141113;
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 12px 16px;
  font: 400 13px var(--mono);
  color: var(--bone);
  width: 100%;
  transition: border-color 0.3s;
}

.field-group input:focus, .field-group select:focus {
  border-color: var(--crim);
  outline: none;
}

.field-terms {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font: 400 11px/1.5 var(--mono);
  color: var(--bone-dim);
  margin-top: 6px;
}

.field-terms input[type="checkbox"] {
  accent-color: var(--crim);
  width: 16px;
  height: 16px;
  margin-top: 2px;
  flex-shrink: 0;
}

.modal-success {
  display: none;
  text-align: center;
  padding: 20px 0;
}

.modal-success.active {
  display: block;
  animation: fx 0.6s ease;
}

.stamp-seal {
  display: inline-block;
  border: 2px solid var(--crim);
  color: var(--crim-bright);
  padding: 10px 24px;
  font: 700 16px var(--mono);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  margin-bottom: 24px;
  transform: rotate(-3deg);
  box-shadow: 0 0 20px var(--crim-glow);
}

.passcode-card {
  background: rgba(20, 17, 19, 0.9);
  border: 1px dashed rgba(255, 255, 255, 0.2);
  padding: 20px;
  margin: 20px 0;
  text-align: center;
}

.passcode-val {
  font: 700 24px var(--mono);
  letter-spacing: 0.2em;
  color: var(--amber);
  margin: 10px 0;
  word-break: break-all;
}

@media (max-width: 900px) {
  .fb { grid-template-columns: 1fr 1fr; position: static; }
  .fb input { grid-column: 1 / -1; }
  .ev, .ev.w, .ev.n { grid-column: 1 / -1; min-height: 180px; }
  .dt { grid-template-columns: 1fr; }
  aside { position: static; order: -1; border: none; border-bottom: 1px solid rgba(255,255,255,0.1); background: var(--void); padding: 0 0 24px 0; }
  .detail-hero { aspect-ratio: 16 / 10; }
  aside .btn { display: none; }
  .rbar { display: block; position: fixed; inset: auto 0 0; z-index: 70; padding: 14px var(--pad) calc(14px + env(safe-area-inset-bottom, 0px)); background: rgba(4, 3, 4, 0.95); border-top: 1px dashed rgba(255, 255, 255, 0.2); }
}
"""

    main_html = """
<main id="list">
  <p class="eyebrow">Archive 01 // Classified Competitive Arenas</p>
  <h1 class="disp" tabindex="-1">Declassified Events Dossier</h1>
  
  <!-- Category Quick-Chips -->
  <div class="cat-chips" id="cat-chips" role="tablist" aria-label="Category quick filter">
    <button class="chip active" type="button" data-cat="" role="tab" aria-selected="true" data-c="FILTER">All Sectors</button>
    <button class="chip" type="button" data-cat="Music" role="tab" aria-selected="false" data-c="FILTER">Music</button>
    <button class="chip" type="button" data-cat="Dance" role="tab" aria-selected="false" data-c="FILTER">Dance</button>
    <button class="chip" type="button" data-cat="Dramatics" role="tab" aria-selected="false" data-c="FILTER">Dramatics</button>
    <button class="chip" type="button" data-cat="Fashion" role="tab" aria-selected="false" data-c="FILTER">Fashion</button>
    <button class="chip" type="button" data-cat="Literary" role="tab" aria-selected="false" data-c="FILTER">Literary</button>
    <button class="chip" type="button" data-cat="Fine Arts" role="tab" aria-selected="false" data-c="FILTER">Fine Arts</button>
    <button class="chip" type="button" data-cat="Cinematics" role="tab" aria-selected="false" data-c="FILTER">Cinematics</button>
    <button class="chip" type="button" data-cat="Gaming" role="tab" aria-selected="false" data-c="FILTER">Gaming</button>
  </div>

  <!-- Search & Filter Bar -->
  <form class="fb" role="search" aria-label="Find events" onsubmit="return false">
    <input id="q" type="search" placeholder="Search events, arenas, sector codes, prize..." aria-label="Search events" autocomplete="off">
    <select id="fc" aria-label="Category"></select>
    <select id="fd" aria-label="Day"></select>
    <select id="fv" aria-label="Venue"></select>
    <select id="fe" aria-label="Solo or team"></select>
    <select id="fs" aria-label="Registration status"></select>
    <button type="button" id="clr" data-c="CLEAR">Clear</button>
  </form>
  
  <div class="cnt-bar">
    <p class="eyebrow cnt" id="cnt" aria-live="polite">Dossier: Initializing records...</p>
    <span class="eyebrow" id="reg-indicator"></span>
  </div>
  
  <div class="grid" id="grid"></div>
</main>

<main id="detail" hidden></main>

<!-- Registration Docket Modal -->
<div class="modal-backdrop" id="reg-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden>
  <div class="modal-window">
    <button class="modal-close" id="modal-close-btn" type="button" aria-label="Close docket" data-c="DISMISS">✕</button>
    
    <div id="modal-content-form">
      <div class="modal-head">
        <span class="eyebrow" style="color:var(--crim);">CLASSIFIED REGISTRATION PROTOCOL</span>
        <h3 id="modal-title">COMMENCE RITUAL ENROLLMENT</h3>
      </div>
      
      <div class="modal-meta-grid" id="modal-meta">
        <div><span>SECTOR ARENA</span><strong id="meta-venue">—</strong></div>
        <div><span>SCHEDULE TIMING</span><strong id="meta-time">—</strong></div>
        <div><span>FORMAT</span><strong id="meta-entry">—</strong></div>
        <div><span>REGISTRATION LEVY</span><strong id="meta-fee" style="color:var(--amber);">—</strong></div>
      </div>
      
      <form class="modal-form" id="docket-form">
        <div class="field-group">
          <label for="lead-name">Operative / Squad Lead Name *</label>
          <input type="text" id="lead-name" required placeholder="e.g. Arjun Varma" autocomplete="name">
        </div>
        
        <div class="field-group">
          <label for="lead-college">Institutional Entity / College *</label>
          <input type="text" id="lead-college" required placeholder="e.g. IIT Ropar / Thapar University">
        </div>
        
        <div class="field-group">
          <label for="lead-email">Encrypted Comms Frequency (Email) *</label>
          <input type="email" id="lead-email" required placeholder="operative@institution.edu" autocomplete="email">
        </div>
        
        <div class="field-group">
          <label for="lead-phone">Transmission Channel (Phone / WhatsApp) *</label>
          <input type="tel" id="lead-phone" required placeholder="+91 98765 43210" autocomplete="tel">
        </div>
        
        <div class="field-group" id="group-team-size" style="display:none;">
          <label for="team-count">Roster Size (Team Members)</label>
          <select id="team-count">
            <option value="4">4 Operatives</option>
            <option value="6" selected>6 Operatives</option>
            <option value="8">8 Operatives</option>
            <option value="10">10 Operatives</option>
            <option value="12">12 Operatives (Full Legion)</option>
          </select>
        </div>
        
        <label class="field-terms">
          <input type="checkbox" id="terms-chk" required>
          <span>I formally acknowledge the festival curfew, midnight decreta, and accept the finality of the judges' verdict under festival law.</span>
        </label>
        
        <button class="btn btn-crim" type="submit" id="submit-docket-btn" style="width:100%; margin-top:8px;" data-c="SEAL">
          <span>SEAL THE COVENANT // SUBMIT DOSSIER</span>
        </button>
      </form>
    </div>
    
    <div class="modal-success" id="modal-success">
      <div class="stamp-seal">COVENANT SEALED</div>
      <p class="eyebrow" style="margin-bottom:12px;">CLEARANCE TOKEN GENERATED & SIGNED</p>
      <h3 style="font:700 24px var(--disp-sans); color:var(--bone);" id="success-event-name">EVENT NAME</h3>
      
      <div class="passcode-card">
        <span class="eyebrow">YOUR OFFICIAL PASSCODE</span>
        <div class="passcode-val" id="success-passcode">ZG26-EVT-000-0000</div>
        <p style="font:400 11px var(--mono); color:var(--ash);">Preserve this token. Required at registration checkpoint in Sector 01.</p>
      </div>
      
      <div style="display:flex; gap:12px; justify-content:center; margin-top:24px;">
        <button class="btn-mini" type="button" id="copy-pass-btn" data-c="COPY">COPY TOKEN</button>
        <button class="btn btn-crim" type="button" id="success-done-btn" style="min-height:38px; padding:8px 24px;" data-c="DISMISS">CLOSE DOSSIER</button>
      </div>
    </div>
  </div>
</div>
"""

    page_scripts = """
/* Events Data & Router Script */
const CATS = ["Music", "Dance", "Dramatics", "Fashion", "Literary", "Fine Arts", "Cinematics", "Quizzing", "Gaming", "Special Events"];
const VENUES = ["Senate Amphitheatre", "Lecture Complex", "Student Activity Centre", "Open Air Theatre", "Sports Grounds", "Central Library Lawn"];
const pad = n => String(n).padStart(3, "0");

const EVENT_NAMES = [
  "Sonic Exorcism // Battle of the Bands",
  "The Danse Macabre // Western Choreo",
  "Shadows of the Street // Nukkad Natak",
  "Haute Occult // The Midnight Pageant",
  "The Lost Manuscript // Slam Poetry",
  "Canvas of Ashes // Live Charcoal Arts",
  "48-Hour Midnight Film // Reel of Horrors",
  "Occult Lore & Enigma // General Quiz",
  "Purgatory LAN // Valorant & CS2 Arena",
  "The Alchemist's Trial // Science Mystery",
  "Rhapsody in Blood // Solo Eastern Vocals",
  "The Final Masquerade // Mono Act Showcase"
];

const EVENTS = Array.from({ length: 12 }, (_, i) => {
  const team = i % 3 === 1;
  return {
    id: "evt-" + pad(i + 1),
    n: i + 1,
    name: EVENT_NAMES[i],
    cat: CATS[i % CATS.length],
    day: (i % 3) + 1,
    date: ["Oct 30, 2026", "Oct 31, 2026", "Nov 01, 2026"][i % 3],
    time: ["11:00 AM", "02:30 PM", "05:00 PM", "08:30 PM"][i % 4],
    venue: VENUES[i % VENUES.length],
    entry: team ? "Team" : "Solo",
    teamSize: team ? "4 - 12 Members" : "1 Participant",
    fee: team ? "₹500 / Team" : "₹150 / Person",
    prize: ["₹40,000", "₹30,000", "₹25,000", "₹50,000"][i % 4],
    status: ["Open", "Open", "Soon", "Closed"][i % 4],
    short: "Enter the arena where the sound refuses to die and the judges judge under candle fire.",
    desc: "A headline competitive ritual at Zeitgeist'26. Open to recognized colleges and independent collectives across the nation. Participants will be judged on precision, thematic horror integration, technical mastery, and stage presence under midnight stage lighting.",
    rules: [
      "All registered teams must report at least 45 minutes prior to slot timing with clearance token.",
      "Time limit: 12 minutes on stage + 3 minutes setup. Negative marking beyond deadline.",
      "Explicit vulgarity is prohibited; psychological and dark editorial interpretations are strongly encouraged.",
      "Decisions of the judge panel are final, absolute, and binding under festival law."
    ],
    timeline: [
      ["10:00 AM", "Registration & Dossier Verification"],
      ["11:00 AM", "Preliminary Round & Soundcheck"],
      ["04:00 PM", "Finals Showcase & Verdict"]
    ],
    contact: "Event Lead: Kabir Sharma · +91 98765 43210 · events@zeitgeist.org.in"
  };
});

const STATUS = {
  Open: "Commence Ritual",
  Soon: "Pending Clearance",
  Closed: "Dossier Sealed"
};

const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];

const getRegisteredEvents = () => {
  try { return JSON.parse(localStorage.getItem("zg_regs") || "{}"); } catch (e) { return {}; }
};

const saveRegistration = (eventId, token, details) => {
  try {
    const data = getRegisteredEvents();
    data[eventId] = { token, date: new Date().toISOString(), ...details };
    localStorage.setItem("zg_regs", JSON.stringify(data));
  } catch (e) {}
};

const fill = (id, label, arr) => {
  $(id).innerHTML = `<option value="">${label}</option>` + arr.map(a => `<option value="${a[0]}">${a[1]}</option>`).join("");
};

fill("#fc", "All Categories", CATS.map(c => [c, c]));
fill("#fd", "All Days", [1, 2, 3].map(d => [d, "Day 0" + d]));
fill("#fv", "All Venues", VENUES.map(v => [v, v]));
fill("#fe", "Solo / Team", [["Solo", "Solo Arena"], ["Team", "Team Arena"]]);
fill("#fs", "Any Status", Object.keys(STATUS).map(s => [s, s]));

const F = { q: "", cat: "", day: "", venue: "", entry: "", status: "" };
const map = { q: "#q", cat: "#fc", day: "#fd", venue: "#fv", entry: "#fe", status: "#fs" };

Object.entries(map).forEach(([k, s]) => $(s).addEventListener(k === "q" ? "input" : "change", e => {
  F[k] = k === "q" ? e.target.value.trim().toLowerCase() : e.target.value;
  if (k === "cat") {
    $$(".chip").forEach(c => c.classList.toggle("active", c.dataset.cat === F.cat));
  }
  playClick(500);
  drawList();
}));

$$(".chip").forEach(ch => {
  ch.onclick = () => {
    $$(".chip").forEach(c => c.classList.remove("active"));
    ch.classList.add("active");
    F.cat = ch.dataset.cat || "";
    $("#fc").value = F.cat;
    playClick(600);
    drawList();
  };
});

$("#clr").onclick = () => {
  Object.keys(F).forEach(k => { F[k] = ""; $(map[k]).value = ""; });
  $$(".chip").forEach(c => c.classList.toggle("active", c.dataset.cat === ""));
  playClick(350);
  drawList();
  toast("DOSSIER FILTERS CLEARED.");
};

function drawList() {
  const registered = getRegisteredEvents();
  const regCount = Object.keys(registered).length;
  $("#reg-indicator").textContent = regCount ? `[YOUR DOSSIERS SEALED: ${regCount}]` : "";

  const r = EVENTS.filter(e =>
    (!F.q || `${e.name} ${e.cat} ${e.venue} ${e.id} event ${pad(e.n)} ${e.entry} ${e.status} ${e.prize}`.toLowerCase().includes(F.q)) &&
    (!F.cat || e.cat === F.cat) &&
    (!F.day || e.day == F.day) &&
    (!F.venue || e.venue === F.venue) &&
    (!F.entry || e.entry === F.entry) &&
    (!F.status || e.status === F.status)
  );

  $("#cnt").textContent = `Dossier: ${r.length} of ${EVENTS.length} classified arenas declassified`;

  $("#grid").innerHTML = r.length ? r.map((e, i) => {
    const isReg = !!registered[e.id];
    return `
      <a class="ev ${[" w", " n", " n", " w"][i % 4].trim()}" data-n="${pad(e.n)}" href="#/event/${e.id}" style="animation-delay:${Math.min(i, 8) * 40}ms" data-c="INSPECT" aria-label="${e.name}, ${e.cat}, ${e.status}">
        <div class="card-glare"></div>
        <div>
          <span class="eyebrow">Dossier ${pad(e.n)} · ${e.cat}</span>
          <h2>${e.name}</h2>
          <div class="mt">
            <span>Day 0${e.day} · ${e.time}</span>
            <span>${e.venue}</span>
          </div>
        </div>
        <div class="tags">
          <span class="tg">${e.entry}</span>
          <span class="tg ${e.status}">
            ${e.status === "Open" ? '<span class="beacon"></span>' : ''}
            ${e.status}
          </span>
          <span class="tg prize">Pool: ${e.prize}</span>
          ${isReg ? '<span class="tg registered">✓ COVENANT SEALED</span>' : ''}
          <span class="ar" aria-hidden="true">→</span>
        </div>
      </a>
    `;
  }).join("") : `
    <div class="empty" style="grid-column: 1 / -1; padding: 80px 20px; text-align: center;">
      <h2>Nothing stirs in this sector.</h2>
      <p class="eyebrow" style="margin-top:12px;">No arena records match your search parameters. Try clearing filters.</p>
    </div>
  `;

  attachCardTilt();
}

function attachCardTilt() {
  if (matchMedia("(pointer: coarse)").matches) return;
  $$(".ev").forEach(card => {
    card.addEventListener("pointermove", e => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;
      card.style.transform = `perspective(700px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
      card.style.setProperty("--gx", `${x}px`);
      card.style.setProperty("--gy", `${y}px`);
    });
    card.addEventListener("pointerleave", () => {
      card.style.transform = "perspective(700px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)";
    });
  });
}
function attachDetailTilt() {
  if (matchMedia("(pointer: coarse)").matches) return;
  const hero = $(".detail-hero");
  if (!hero) return;
  hero.addEventListener('pointermove', e => {
    const rect = hero.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -5;
    const ry = ((x - cx) / cx) * 5;
    hero.style.transform = `perspective(1200px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(8px)`;
  });
  hero.addEventListener('pointerleave', () => {
    hero.style.transform = '';
  });
}

function drawDetail(id) {
  const i = EVENTS.findIndex(e => e.id === id);
  const e = EVENTS[i];
  const d = $("#detail");
  const registered = getRegisteredEvents();
  const isReg = registered[id];

  if (!e) {
    d.innerHTML = `
      <a class="back" href="#/" data-c="RETURN">← Return to all dossiers</a>
      <h1 class="disp" tabindex="-1" style="margin-top:20px;">Dossier Classified</h1>
      <p style="margin-top:20px; color:var(--ash);">This arena record has vanished into the Punjab fog.</p>
    `;
    document.title = "Not Found — ZEITGEIST'26";
    return;
  }

  const p = EVENTS[(i + EVENTS.length - 1) % EVENTS.length];
  const n = EVENTS[(i + 1) % EVENTS.length];
  const open = e.status === "Open";

  const btnLabel = isReg ? `COVENANT SEALED [${isReg.token}]` : STATUS[e.status];
  const btnClass = isReg ? "btn btn-crim registered-btn" : (open ? "btn btn-crim" : "btn");
  const btnAction = open ? `data-reg-id="${e.id}"` : `data-disabled-msg="${STATUS[e.status]}"`;
  const btnHtml = `<button type="button" class="${btnClass}" ${btnAction} aria-disabled="${!open && !isReg}" data-c="${isReg ? 'VIEW' : 'REGISTER'}">${btnLabel}</button>`;

  d.innerHTML = `
    <div class="detail-nav-bar">
      <a class="back" href="#/" data-c="RETURN">← All Dossiers Archive</a>
      <div class="detail-actions">
        <button type="button" class="btn-mini" id="share-dossier-btn" data-c="SHARE">⎘ Share Link</button>
        <button type="button" class="btn-mini" id="print-dossier-btn" data-c="PRINT">🖶 Print Directive</button>
      </div>
    </div>

    <p class="eyebrow" style="margin-top:8px;">CLASSIFIED RITUAL · ARENA ${pad(e.n)} // ${e.cat}</p>
    <h1 class="disp" tabindex="-1" style="font-size:clamp(30px, 5.5vw, 68px); margin-top:10px;">${e.name}</h1>
    
    <div class="detail-hero">
      <span class="detail-hero-tag" aria-hidden="true">${e.cat}</span>
      <div class="detail-hero-reticle">
        <span>SECTOR: ${e.venue.toUpperCase()}</span>
        <span>CLEARANCE: LEVEL OMEGA</span>
        <span>STATUS: ${e.status.toUpperCase()}</span>
      </div>
      <div class="detail-hero-caption">
        [CLASSIFIED SURVEILLANCE DOSSIER // IIT ROPAR ARENA ${pad(e.n)} · DAY 0${e.day}]
      </div>
    </div>
    
    <div class="dt">
      <div>
        <h2>The Decree</h2>
        <p style="font:italic 500 clamp(20px, 2.2vw, 28px)/1.35 var(--serif); color:var(--bone); border-left:2px solid var(--crim); padding-left:20px;">
          "${e.short}"
        </p>
        
        <h2>Full Dossier Briefing</h2>
        <p>${e.desc}</p>
        
        <h2>Decrees & Protocols</h2>
        <ol>${e.rules.map(r => `<li>${r}</li>`).join("")}</ol>
        
        <h2>Sequence of Rites</h2>
        <ul class="tl">${e.timeline.map(t => `<li><b>${t[0]}</b><span>${t[1]}</span></li>`).join("")}</ul>
        
        <h2>Contact Liaison</h2>
        <p>${e.contact}</p>
      </div>
      
      <aside aria-label="Event facts">
        <span class="eyebrow">Day 0${e.day} · ${e.date}</span>
        <dl class="ds">
          <div><dt>TIME</dt><dd>${e.time}</dd></div>
          <div><dt>SECTOR</dt><dd>${e.venue}</dd></div>
          <div><dt>ENTRY</dt><dd>${e.entry}</dd></div>
          <div><dt>TEAM SIZE</dt><dd>${e.teamSize}</dd></div>
          <div><dt>REG FEE</dt><dd>${e.fee}</dd></div>
          <div style="grid-column: 1 / -1;"><dt>PRIZE POOL</dt><dd style="color:var(--amber); font-size:26px;">${e.prize}</dd></div>
        </dl>
        ${btnHtml}
      </aside>
    </div>
    
    <div class="rbar">${btnHtml}</div>
    
    <div class="pn">
      <a href="#/event/${p.id}" data-c="PREV">← Previous: ${p.name}</a>
      <a href="#/event/${n.id}" data-c="NEXT">Next: ${n.name} →</a>
    </div>
  `;

  document.title = `${e.name} — ${e.cat} | ZEITGEIST'26`;
attachDetailTilt();

  const shareBtn = $("#share-dossier-btn");
  if (shareBtn) {
    shareBtn.onclick = () => {
      playClick(750);
      if (navigator.clipboard) {
        navigator.clipboard.writeText(location.href).then(() => {
          toast("DOSSIER FREQUENCY COPIED TO CLIPBOARD.");
        });
      } else {
        toast("DOSSIER LINK: " + location.href);
      }
    };
  }

  const printBtn = $("#print-dossier-btn");
  if (printBtn) {
    printBtn.onclick = () => { playClick(500); window.print(); };
  }
}

let activeRegistrationEvent = null;

function openRegistrationModal(eventId) {
  const e = EVENTS.find(x => x.id === eventId);
  if (!e) return;
  activeRegistrationEvent = e;

  const modal = $("#reg-modal");
  const isTeam = e.entry === "Team";

  $("#modal-title").textContent = `ENROLLMENT // ${e.name}`;
  $("#meta-venue").textContent = e.venue;
  $("#meta-time").textContent = `Day 0${e.day} · ${e.time}`;
  $("#meta-entry").textContent = `${e.entry} (${e.teamSize})`;
  $("#meta-fee").textContent = e.fee;

  $("#group-team-size").style.display = isTeam ? "grid" : "none";
  $("#modal-content-form").style.display = "block";
  $("#modal-success").classList.remove("active");
  $("#modal-success").style.display = "none";
  $("#docket-form").reset();

  modal.hidden = false;
  void modal.offsetWidth;
  modal.classList.add("open");
  playChime(400);

  const firstInput = $("#lead-name");
  if (firstInput) firstInput.focus();
}

function closeRegistrationModal() {
  const modal = $("#reg-modal");
  modal.classList.remove("open");
  setTimeout(() => {
    modal.hidden = true;
    activeRegistrationEvent = null;
  }, 350);
  playClick(400);
}

$("#modal-close-btn").onclick = closeRegistrationModal;
$("#success-done-btn").onclick = closeRegistrationModal;
$("#reg-modal").onclick = e => { if (e.target === $("#reg-modal")) closeRegistrationModal(); };

document.addEventListener("keydown", e => {
  if (e.key === "Escape" && !$("#reg-modal").hidden) closeRegistrationModal();
});

$("#docket-form").onsubmit = e => {
  e.preventDefault();
  if (!activeRegistrationEvent) return;

  const btn = $("#submit-docket-btn");
  btn.setAttribute("aria-disabled", "true");
  btn.querySelector("span").textContent = "TRANSMITTING ENCRYPTED DOSSIER...";
  playGlitch();

  setTimeout(() => {
    const randomHex = Math.floor(1000 + Math.random() * 9000);
    const token = `ZG26-${activeRegistrationEvent.id.toUpperCase()}-${randomHex}`;

    const leadName = $("#lead-name").value.trim();
    const college = $("#lead-college").value.trim();
    const email = $("#lead-email").value.trim();

    saveRegistration(activeRegistrationEvent.id, token, {
      leadName,
      college,
      email,
      eventName: activeRegistrationEvent.name
    });

    playChime(500);

    $("#modal-content-form").style.display = "none";
    const succ = $("#modal-success");
    succ.style.display = "block";
    succ.classList.add("active");

    $("#success-event-name").textContent = activeRegistrationEvent.name;
    $("#success-passcode").textContent = token;

    btn.removeAttribute("aria-disabled");
    btn.querySelector("span").textContent = "SEAL THE COVENANT // SUBMIT DOSSIER";

    if (location.hash.startsWith("#/event/")) {
      drawDetail(activeRegistrationEvent.id);
    } else {
      drawList();
    }

    toast(`COVENANT SEALED FOR ${activeRegistrationEvent.name}`);
  }, 800);
};

$("#copy-pass-btn").onclick = () => {
  playClick(800);
  const pass = $("#success-passcode").textContent;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(pass).then(() => {
      toast("CLEARANCE TOKEN COPIED TO CLIPBOARD.");
    });
  } else {
    toast("TOKEN: " + pass);
  }
};

document.addEventListener("click", ev => {
  const regBtn = ev.target.closest("[data-reg-id]");
  if (regBtn) {
    ev.preventDefault();
    openRegistrationModal(regBtn.dataset.regId);
    return;
  }
  const disBtn = ev.target.closest("[data-disabled-msg]");
  if (disBtn) {
    ev.preventDefault();
    playGlitch();
    toast(disBtn.dataset.disabledMsg.toUpperCase() + ".");
  }
});

function route() {
  const m = location.hash.match(/^#\\/event\\/([\\w-]+)/);
  const L = $("#list"), D = $("#detail");
  L.hidden = !!m;
  D.hidden = !m;
  
  if (m) {
    document.body.setAttribute("data-atm", "archive");
    drawDetail(m[1]);
  } else {
    document.body.setAttribute("data-atm", "events");
    document.title = "The Archives — Events | ZEITGEIST'26 | IIT Ropar";
    drawList();
  }
  
  const v = m ? D : L;
  v.style.animation = "none";
  void v.offsetWidth;
  v.style.animation = "";
  scrollTo(0, 0);
  const h = v.querySelector("h1");
  if (h) h.focus({ preventScroll: true });
}
addEventListener("hashchange", route);
route();

/* ===== 3D TILT — EVENT CARDS ===== */
function attach3DTilt() {
  document.querySelectorAll('.ev').forEach(card => {
    card.addEventListener('pointermove', e => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rx = ((y - cy) / cy) * -4;
      const ry = ((x - cx) / cx) * 4;
      card.style.setProperty('--gx', (x / rect.width * 100) + '%');
      card.style.setProperty('--gy', (y / rect.height * 100) + '%');
      card.style.transform = `perspective(1000px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(4px)`;
    });
    card.addEventListener('pointerleave', () => {
      card.style.transform = '';
    });
  });
}
// Re-attach after list is redrawn
const origDL = typeof drawList === 'function' ? drawList : null;
if (origDL) {
  const _dl = drawList;
  drawList = function() {
    _dl.apply(this, arguments);
    requestAnimationFrame(attach3DTilt);
  };
}
attach3DTilt();
"""

    return title, description, extra_css, main_html, page_scripts
