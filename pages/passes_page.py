# Generator for passes.html (Clearance Passes & Stay - Booking Docket)

def get_passes_content():
    title = "Clearance Passes & Stay | ZEITGEIST'26 | IIT Ropar"
    description = "Secure official festival clearance passes and student hostel accommodations for ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Passes Specific Styles */
.passes-hero {
  margin-bottom: 40px;
}

.passes-hero h1 {
  font-size: clamp(38px, 7vw, 86px);
  margin-top: 14px;
}

.passes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 70px;
  perspective: 1200px;
}

.pass-card {
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: clamp(24px, 3vw, 36px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  transform-style: preserve-3d;
  overflow: hidden;
  transition: transform 0.12s ease-out, border-color 0.3s, box-shadow 0.3s;
}

.pass-card .hologram-glare {
  position: absolute;
  inset: -40%;
  pointer-events: none;
  background: radial-gradient(circle 300px at var(--mx, 50%) var(--my, 50%), rgba(255, 255, 255, 0.2), rgba(165, 29, 41, 0.15) 35%, transparent 65%),
              linear-gradient(135deg, transparent 35%, rgba(212, 160, 23, 0.15) 50%, rgba(56, 189, 248, 0.15) 65%, transparent 80%);
  opacity: 0;
  transition: opacity 0.3s;
  mix-blend-mode: screen;
  z-index: 8;
}

.pass-card:hover .hologram-glare {
  opacity: 1;
}

.pass-card:hover {
  border-color: var(--crim);
}

.pass-card.featured {
  border-color: var(--crim);
  background: linear-gradient(135deg, rgba(36, 5, 8, 0.6) 0%, rgba(13, 10, 12, 0.95) 100%);
  box-shadow: 0 0 30px var(--crim-glow);
}

.featured-ribbon {
  position: absolute;
  top: 14px;
  right: 14px;
  background: var(--crim);
  color: var(--bone);
  font: 700 9px var(--mono);
  letter-spacing: 0.2em;
  padding: 4px 10px;
  text-transform: uppercase;
  transform: translateZ(35px);
}

.pass-rfid-chip {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 9px var(--mono);
  letter-spacing: 0.18em;
  color: var(--amber);
  margin-bottom: 14px;
  transform: translateZ(28px);
}

.chip-gold {
  width: 26px;
  height: 20px;
  border-radius: 3px;
  background: linear-gradient(135deg, #d4af37 0%, #fff2a8 50%, #996515 100%);
  border: 1px solid #ffe57f;
  box-shadow: 0 0 10px rgba(212, 175, 55, 0.4), inset 0 0 4px rgba(0, 0, 0, 0.5);
  position: relative;
  display: inline-block;
  flex-shrink: 0;
}

.chip-gold::after {
  content: "";
  position: absolute;
  inset: 3px;
  border: 1px dashed rgba(0,0,0,0.5);
  border-radius: 1px;
}

.pass-card h2 {
  font: 700 clamp(20px, 2.5vw, 26px) var(--disp-sans);
  text-transform: uppercase;
  margin: 12px 0 8px;
  transform: translateZ(30px);
}

.pass-price {
  font: 700 clamp(32px, 4vw, 44px) var(--mono);
  color: var(--amber);
  margin-bottom: 20px;
  display: block;
  transform: translateZ(34px);
  text-shadow: 0 0 16px rgba(255, 179, 71, 0.35);
}

.pass-price small {
  font-size: 11px;
  color: var(--ash);
  font-weight: 400;
  letter-spacing: 0.1em;
}

.pass-features {
  list-style: none;
  display: grid;
  gap: 12px;
  margin-bottom: 30px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 20px;
  font: 400 12px/1.5 var(--mono);
  color: var(--bone-dim);
  transform: translateZ(20px);
}

.pass-features li {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.pass-features li::before {
  content: "✓";
  color: var(--crim-bright);
  font-weight: 700;
}

/* Booking Modal */
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
  max-width: 600px;
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

.field-group { display: grid; gap: 6px; margin-bottom: 16px; }

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
}

.field-group input:focus, .field-group select:focus {
  border-color: var(--crim);
  outline: none;
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

.rules-box {
  background: rgba(20, 17, 19, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: clamp(24px, 3.5vw, 40px);
  margin-bottom: 80px;
}

.rules-box h3 {
  font: 700 20px var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 18px;
  color: var(--amber);
}

.rules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  font: 400 12px/1.6 var(--mono);
  color: var(--bone-dim);
}

.rules-grid div strong {
  display: block;
  color: var(--bone);
  margin-bottom: 4px;
}
"""

    main_html = """
<main id="passes">
  <div class="passes-hero">
    <span class="eyebrow" style="color:var(--crim);">SECTOR ACCREDITATION & ENTRY DOSSIERS</span>
    <h1 class="disp">CLEARANCE PASSES</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Authorize your presence across campus competitive sectors and reserve student hostel accommodation.</p>
  </div>

  <div class="passes-grid">
    <!-- Pass 1: Day Operative -->
    <article class="pass-card" aria-label="Day Operative Pass">
      <div class="hologram-glare" aria-hidden="true"></div>
      <div>
        <div class="pass-rfid-chip" aria-hidden="true"><span class="chip-gold"></span><span>RFID // SINGLE DAY CLEARANCE</span></div>
        <span class="eyebrow">TIER 01 // SINGLE DAY</span>
        <h2>DAY OPERATIVE PASS</h2>
        <span class="pass-price">₹299 <small>/ DAY</small></span>
        <ul class="pass-features">
          <li>Access to all 12 daytime competitive arenas</li>
          <li>Entry to Central Library lawn art exhibits</li>
          <li>Student Activity Centre gaming lounge access</li>
          <li>Campus food street & merchandise zone</li>
          <li>Official digital accreditation badge</li>
        </ul>
      </div>
      <button class="btn" type="button" onclick="openPassModal('Day Operative Pass', '₹299')" data-c="SELECT" style="transform:translateZ(25px);">CLAIM DAY PASS</button>
    </article>

    <!-- Pass 2: Pronites Access -->
    <article class="pass-card" aria-label="Three-Night Pronite Pass">
      <div class="hologram-glare" aria-hidden="true"></div>
      <div>
        <div class="pass-rfid-chip" aria-hidden="true"><span class="chip-gold"></span><span>RFID // 3 NIGHTS CONCERT BADGE</span></div>
        <span class="eyebrow" style="color:var(--crim);">TIER 02 // 3 NIGHTS</span>
        <h2>PRONITES CONCERT PASS</h2>
        <span class="pass-price">₹699 <small>/ ALL NIGHTS</small></span>
        <ul class="pass-features">
          <li>Night 01: Nirvana's Eclipse (Rock & Metal)</li>
          <li>Night 02: The Phantom Rave (EDM Spectacle)</li>
          <li>Night 03: Symphony of Souls (Bollywood Finale)</li>
          <li>RFID Concert Wristband at Sector 01 Checkpoint</li>
          <li>Includes all daytime arena visitor access</li>
        </ul>
      </div>
      <button class="btn btn-crim" type="button" onclick="openPassModal('Pronites Concert Pass', '₹699')" data-c="SELECT" style="transform:translateZ(25px);">CLAIM PRONITE PASS</button>
    </article>

    <!-- Pass 3: VIP All-Access -->
    <article class="pass-card featured" aria-label="VIP All-Access Master Pass">
      <div class="hologram-glare" aria-hidden="true"></div>
      <span class="featured-ribbon">RECOMMENDED</span>
      <div>
        <div class="pass-rfid-chip" aria-hidden="true"><span class="chip-gold"></span><span>RFID // ALL-ACCESS VIP MASTER</span></div>
        <span class="eyebrow" style="color:var(--amber);">TIER 03 // ALL ACCESS</span>
        <h2>VIP MASTER PASS</h2>
        <span class="pass-price">₹1,199 <small>/ 3 DAYS</small></span>
        <ul class="pass-features">
          <li>Front-of-stage VIP pit enclosure for all 3 Pronites</li>
          <li>Priority fast-track entry gates across all sectors</li>
          <li>Official ZEITGEIST'26 Horror T-Shirt & Lanyard</li>
          <li>Exclusive access to backstage lounge area</li>
          <li>Direct clearance for all 12 daytime arenas</li>
        </ul>
      </div>
      <button class="btn btn-crim" type="button" onclick="openPassModal('VIP Master Pass', '₹1,199')" data-c="SELECT" style="transform:translateZ(25px);">CLAIM VIP PASS</button>
    </article>

    <!-- Pass 4: Outstation Contingent + Hostel -->
    <article class="pass-card" aria-label="Contingent Pass plus Hostels">
      <div class="hologram-glare" aria-hidden="true"></div>
      <div>
        <div class="pass-rfid-chip" aria-hidden="true"><span class="chip-gold"></span><span>RFID // 3 DAYS + HOSTEL STAY</span></div>
        <span class="eyebrow">TIER 04 // FULL STAY</span>
        <h2>CONTINGENT + HOSTEL</h2>
        <span class="pass-price">₹1,899 <small>/ 3 DAYS + STAY</small></span>
        <ul class="pass-features">
          <li>All-Access 3-day festival entry + all 3 pronites</li>
          <li>3 Nights student hostel room stay at IIT Ropar</li>
          <li>Mattress, bedding, and 24/7 security credential</li>
          <li>High-speed campus Wi-Fi & electricity clearance</li>
          <li>Free shuttle transit between RPAR station & campus</li>
        </ul>
      </div>
      <button class="btn btn-amber" type="button" onclick="openPassModal('Contingent + Hostel Pass', '₹1,899')" data-c="SELECT" style="transform:translateZ(25px);">RESERVE STAY & PASS</button>
    </article>
  </div>

  <!-- Rules Box -->
  <div class="rules-box">
    <h3>CAMPUS ACCREDITATION & ACCOMMODATION BYLAWS</h3>
    <div class="rules-grid">
      <div>
        <strong>IDENTIFICATION MANDATE</strong>
        A valid Government-issued Photo ID (Aadhaar / Voter ID / Passport) alongside college student identification is strictly required at Sector 01 security gate.
      </div>
      <div>
        <strong>HOSTEL CHECK-IN WINDOW</strong>
        Hostel allotment commences October 29 at 02:00 PM. Check-out deadline is November 02 by 11:00 AM. Key deposits returned upon room inspection.
      </div>
      <div>
        <strong>SECURITY CURFEW</strong>
        Hostel corridors lock at 01:30 AM every night following conclusion of pronites. Unauthorized loitering near Sutlej river banks is prohibited.
      </div>
      <div>
        <strong>REFUND & TRANSFER POLICY</strong>
        Clearance passes are strictly non-refundable once cryptographically sealed and registered in the festival database.
      </div>
    </div>
  </div>
</main>

<!-- Pass Booking Modal -->
<div class="modal-backdrop" id="pass-modal" role="dialog" aria-modal="true" aria-labelledby="pass-modal-title" hidden>
  <div class="modal-window">
    <button class="modal-close" id="pass-modal-close" type="button" aria-label="Close modal" data-c="DISMISS">✕</button>
    
    <div id="pass-form-container">
      <div style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:18px; margin-bottom:20px;">
        <span class="eyebrow" style="color:var(--crim);">FESTIVAL ACCREDITATION DOCKET</span>
        <h3 id="pass-modal-title" style="font:700 24px var(--disp-sans); text-transform:uppercase; margin-top:8px;">CLAIM PASS</h3>
        <p style="font:400 12px var(--mono); color:var(--amber); margin-top:6px;" id="pass-modal-tier-price">TIER: —</p>
      </div>

      <form id="pass-form">
        <div class="field-group">
          <label for="pass-name">Attendee / Operative Name *</label>
          <input type="text" id="pass-name" required placeholder="e.g. Priyanshu Sharma" autocomplete="name">
        </div>

        <div class="field-group">
          <label for="pass-college">College / Institutional Collective *</label>
          <input type="text" id="pass-college" required placeholder="e.g. IIT Delhi / Thapar University">
        </div>

        <div class="field-group">
          <label for="pass-email">Encrypted Comms (Email Address) *</label>
          <input type="email" id="pass-email" required placeholder="attendee@college.edu" autocomplete="email">
        </div>

        <div class="field-group">
          <label for="pass-phone">Contact Transmission (Phone Number) *</label>
          <input type="tel" id="pass-phone" required placeholder="+91 98765 43210" autocomplete="tel">
        </div>

        <div class="field-group">
          <label for="pass-qty">Pass Quantity</label>
          <select id="pass-qty">
            <option value="1">1 Clearance Pass</option>
            <option value="2">2 Clearance Passes</option>
            <option value="3">3 Clearance Passes</option>
            <option value="5">5 Passes (Delegation)</option>
          </select>
        </div>

        <button class="btn btn-crim" type="submit" id="submit-pass-btn" style="width:100%; margin-top:10px;" data-c="AUTHORIZE">
          <span>SEAL PASS CLEARANCE // ISSUE CREDENTIAL</span>
        </button>
      </form>
    </div>

    <div id="pass-success" style="display:none; text-align:center; padding:16px 0;">
      <div style="border:2px solid var(--crim); color:var(--crim-bright); padding:8px 20px; display:inline-block; font:700 16px var(--mono); letter-spacing:0.3em; margin-bottom:20px; transform:rotate(-2deg);">
        CLEARANCE GRANTED
      </div>
      <p class="eyebrow" style="margin-bottom:8px;">OFFICIAL FESTIVAL ENTRY TOKEN</p>
      <h3 style="font:700 22px var(--disp-sans);" id="success-tier-title">TIER NAME</h3>

      <div class="passcode-card">
        <span class="eyebrow">CLEARANCE PASSCODE</span>
        <div class="passcode-val" id="success-pass-token">ZG26-PASS-0000</div>
        <p style="font:400 11px var(--mono); color:var(--ash);">Present this token along with valid student ID at Sector 01 RFID desk.</p>
      </div>

      <div style="display:flex; gap:12px; justify-content:center; margin-top:20px;">
        <button class="btn-mini" type="button" id="copy-pass-token-btn" data-c="COPY">COPY TOKEN</button>
        <button class="btn btn-crim" type="button" id="pass-done-btn" style="min-height:36px; padding:6px 20px;" data-c="DISMISS">CLOSE</button>
      </div>
    </div>
  </div>
</div>
"""

    page_scripts = """
/* Passes Booking Modal Logic */
let currentPassTier = "";
let currentPassPrice = "";

function openPassModal(tier, price) {
  currentPassTier = tier;
  currentPassPrice = price;
  const modal = document.getElementById("pass-modal");
  document.getElementById("pass-modal-title").textContent = "ACCREDITATION // " + tier;
  document.getElementById("pass-modal-tier-price").textContent = "TIER: " + tier + " · LEVY: " + price;
  
  document.getElementById("pass-form-container").style.display = "block";
  document.getElementById("pass-success").style.display = "none";
  document.getElementById("pass-form").reset();

  modal.hidden = false;
  void modal.offsetWidth;
  modal.classList.add("open");
  playChime(420);

  const inp = document.getElementById("pass-name");
  if (inp) inp.focus();
}

function closePassModal() {
  const modal = document.getElementById("pass-modal");
  modal.classList.remove("open");
  setTimeout(() => { modal.hidden = true; }, 350);
  playClick(400);
}

document.getElementById("pass-modal-close").onclick = closePassModal;
document.getElementById("pass-done-btn").onclick = closePassModal;

document.getElementById("pass-modal").onclick = e => {
  if (e.target === document.getElementById("pass-modal")) closePassModal();
};

document.addEventListener("keydown", e => {
  if (e.key === "Escape" && !document.getElementById("pass-modal").hidden) closePassModal();
});

document.getElementById("pass-form").onsubmit = e => {
  e.preventDefault();
  const btn = document.getElementById("submit-pass-btn");
  btn.setAttribute("aria-disabled", "true");
  btn.querySelector("span").textContent = "VERIFYING BIOMETRICS & GENERATING TOKEN...";
  playGlitch();

  setTimeout(() => {
    const randomHex = Math.floor(1000 + Math.random() * 9000);
    const token = `ZG26-PASS-${randomHex}`;

    const attendee = document.getElementById("pass-name").value.trim();
    const college = document.getElementById("pass-college").value.trim();
    const email = document.getElementById("pass-email").value.trim();

    try {
      const passes = JSON.parse(localStorage.getItem("zg_passes") || "[]");
      passes.push({ token, attendee, college, email, tier: currentPassTier, price: currentPassPrice, date: new Date().toISOString() });
      localStorage.setItem("zg_passes", JSON.stringify(passes));
    } catch (err) {}

    playChime(600);

    document.getElementById("pass-form-container").style.display = "none";
    document.getElementById("pass-success").style.display = "block";
    document.getElementById("success-tier-title").textContent = currentPassTier;
    document.getElementById("success-pass-token").textContent = token;

    btn.removeAttribute("aria-disabled");
    btn.querySelector("span").textContent = "SEAL PASS CLEARANCE // ISSUE CREDENTIAL";

    toast(`CLEARANCE TOKEN ISSUED: ${token}`);
  }, 900);
};

document.getElementById("copy-pass-token-btn").onclick = () => {
  playClick(800);
  const tok = document.getElementById("success-pass-token").textContent;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(tok).then(() => {
      toast("CLEARANCE PASS TOKEN COPIED.");
    });
  } else {
    toast("TOKEN: " + tok);
  }
};

/* 3D Holographic Card Tilt Listener */
document.querySelectorAll(".pass-card").forEach(c => {
  c.addEventListener("pointermove", e => {
    const r = c.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    c.style.setProperty("--mx", (e.clientX - r.left) + "px");
    c.style.setProperty("--my", (e.clientY - r.top) + "px");
    c.style.transform = `perspective(1000px) rotateX(${-y * 18}deg) rotateY(${x * 18}deg) translateZ(16px)`;
    c.style.boxShadow = `${-x * 25}px ${20 + y * 15}px 50px rgba(0, 0, 0, 0.95), 0 0 30px var(--crim-glow)`;
  });
  c.addEventListener("pointerleave", () => {
    c.style.transform = "";
    c.style.boxShadow = "";
  });
});
"""
    return title, description, extra_css, main_html, page_scripts
