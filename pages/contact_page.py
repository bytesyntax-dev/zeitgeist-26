# Generator for contact.html (Liaisons & Campus Sectors - Map & Travel Directives)

def get_contact_content():
    title = "Liaisons & Campus Sectors | ZEITGEIST'26 | IIT Ropar"
    description = "Contact the core organizing team, explore the interactive campus sectors, and review travel directives to IIT Ropar for ZEITGEIST'26."

    extra_css = """
/* Contact & Sectors Styles */
.contact-hero {
  margin-bottom: 40px;
}

.contact-hero h1 {
  font-size: clamp(38px, 7vw, 86px);
  margin-top: 14px;
}

.section-head {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 14px;
  margin: 50px 0 30px;
}

.section-head h2 {
  font: 700 clamp(22px, 3vw, 32px) var(--disp-sans);
  text-transform: uppercase;
  color: var(--amber);
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px 20px;
  margin-bottom: 70px;
  perspective: 1200px;
}

.team-card {
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 32px 24px 24px;
  position: relative;
  transform-style: preserve-3d;
  transform-origin: top center;
  transition: transform 0.15s ease-out, border-color 0.3s, box-shadow 0.3s;
}

.team-card-clip {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%) translateZ(32px);
  width: 36px;
  height: 12px;
  background: linear-gradient(180deg, #999 0%, #444 50%, #222 100%);
  border: 1px solid #bbb;
  border-radius: 3px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.7);
}

.team-card-clip::after {
  content: "";
  position: absolute;
  top: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 16px;
  height: 6px;
  border-radius: 5px 5px 0 0;
  border: 2px solid #ccc;
  border-bottom: none;
}

.team-card:hover {
  border-color: var(--crim);
  background: var(--surface);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9), 0 0 25px var(--crim-glow);
}

.team-card h3 {
  font: 700 20px var(--serif);
  letter-spacing: 0.05em;
  color: var(--bone);
  margin: 8px 0 4px;
  transform: translateZ(28px);
}

.team-role {
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--crim-bright);
  text-transform: uppercase;
  margin-bottom: 16px;
  display: block;
  transform: translateZ(24px);
}

.team-links {
  display: grid;
  gap: 6px;
  font: 400 11px var(--mono);
  color: var(--bone-dim);
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  padding-top: 14px;
  transform: translateZ(18px);
}

.team-links a:hover {
  color: var(--amber);
}

/* Sectors Interactive Grid */
.sectors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 70px;
  perspective: 1200px;
}

.sector-card {
  background: linear-gradient(135deg, rgba(20, 17, 19, 0.9) 0%, rgba(9, 6, 8, 0.95) 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 24px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.2s ease-out, border-color 0.3s, box-shadow 0.3s;
}

.sector-card:hover {
  border-color: var(--amber);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9), 0 0 25px var(--amber-glow);
  transform: perspective(900px) translateZ(16px) rotateX(-3deg) rotateY(3deg);
}

.sector-num {
  font: 700 24px var(--mono);
  color: var(--amber);
  margin-bottom: 6px;
  display: block;
  transform: translateZ(28px);
  text-shadow: 0 0 15px rgba(255, 179, 71, 0.4);
}

.sector-card h3 {
  font: 700 18px var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 12px;
  transform: translateZ(22px);
}

.sector-card p {
  color: var(--bone-dim);
  font: 400 12px/1.6 var(--mono);
  transform: translateZ(16px);
}

/* Travel Directives */
.travel-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-bottom: 70px;
}

.travel-card {
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 24px;
}

.travel-card h3 {
  font: 700 16px var(--mono);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--bone);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.travel-card p {
  color: var(--bone-dim);
  font: 400 12px/1.6 var(--mono);
}

/* Comms Form */
.comms-form-box {
  background: #0d0a0c;
  border: 1px solid rgba(148, 23, 34, 0.4);
  padding: clamp(28px, 4vw, 44px);
  margin-bottom: 80px;
}

.comms-form-box h3 {
  font: 700 22px var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 20px;
  color: var(--bone);
}

.comms-form {
  display: grid;
  gap: 18px;
  max-width: 640px;
}

.comms-field {
  display: grid;
  gap: 6px;
}

.comms-field label {
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  color: var(--ash);
  text-transform: uppercase;
}

.comms-field input, .comms-field select, .comms-field textarea {
  background: #141113;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 12px 16px;
  font: 400 13px var(--mono);
  color: var(--bone);
  width: 100%;
}

.comms-field input:focus, .comms-field select:focus, .comms-field textarea:focus {
  border-color: var(--crim);
  outline: none;
}
"""

    main_html = """
<main id="contact">
  <div class="contact-hero">
    <span class="eyebrow" style="color:var(--crim);">FESTIVAL COMMAND & LIAISONS</span>
    <h1 class="disp">SECTORS & LIAISONS</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Direct lines to student conveners, faculty advisory, and travel directives to IIT Ropar.</p>
  </div>

  <!-- Organizing Council -->
  <div class="section-head">
    <span class="eyebrow">DECLASSIFIED PERSONNEL DIRECTORY</span>
    <h2>CORE ORGANIZING COUNCIL</h2>
  </div>

  <div class="team-grid">
    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 01</span>
      <h3>KABIR SHARMA</h3>
      <span class="team-role">Overall Festival Convener</span>
      <div class="team-links">
        <span>Sector: Central Command</span>
        <a href="tel:+919876543210">📞 +91 98765 43210</a>
        <a href="mailto:convener@zeitgeist.org.in">✉ convener@zeitgeist.org.in</a>
      </div>
    </article>

    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 02</span>
      <h3>ANANYA VERMA</h3>
      <span class="team-role">Competitions & Arenas Lead</span>
      <div class="team-links">
        <span>Sector: Arena Operations</span>
        <a href="tel:+919876543211">📞 +91 98765 43211</a>
        <a href="mailto:events@zeitgeist.org.in">✉ events@zeitgeist.org.in</a>
      </div>
    </article>

    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 03</span>
      <h3>ROHAN MALHOTRA</h3>
      <span class="team-role">Pronites & Artist Relations</span>
      <div class="team-links">
        <span>Sector: Main Stage</span>
        <a href="tel:+919876543212">📞 +91 98765 43212</a>
        <a href="mailto:pronites@zeitgeist.org.in">✉ pronites@zeitgeist.org.in</a>
      </div>
    </article>

    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 04</span>
      <h3>SIMRANJIT KAUR</h3>
      <span class="team-role">Hospitality & Outstation Stays</span>
      <div class="team-links">
        <span>Sector: Hostels Desk</span>
        <a href="tel:+919876543213">📞 +91 98765 43213</a>
        <a href="mailto:hospitality@zeitgeist.org.in">✉ hospitality@zeitgeist.org.in</a>
      </div>
    </article>

    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 05</span>
      <h3>ADITYA SEN</h3>
      <span class="team-role">Public Relations & Media</span>
      <div class="team-links">
        <span>Sector: Press Room</span>
        <a href="tel:+919876543214">📞 +91 98765 43214</a>
        <a href="mailto:pr@zeitgeist.org.in">✉ pr@zeitgeist.org.in</a>
      </div>
    </article>

    <article class="team-card">
      <div class="team-card-clip" aria-hidden="true"></div>
      <span class="eyebrow">COMMAND 06</span>
      <h3>DR. P. K. SINGH</h3>
      <span class="team-role">Faculty Cultural Advisory</span>
      <div class="team-links">
        <span>Office: Dean of Student Affairs</span>
        <a href="tel:+911881242100">📞 +91 1881 242100</a>
        <a href="mailto:dosa@iitrpr.ac.in">✉ dosa@iitrpr.ac.in</a>
      </div>
    </article>
  </div>

  <!-- Campus Sectors Guide -->
  <div class="section-head" id="sectors">
    <span class="eyebrow">CAMPUS TOPOGRAPHY & RETICLE</span>
    <h2>SECTOR ACCREDITATION MAP</h2>
  </div>

  <div class="sectors-grid">
    <div class="sector-card">
      <span class="sector-num">SECTOR 01</span>
      <h3>MAIN GATE CHECKPOINT</h3>
      <p>Primary accreditation portal, RFID wristband issuance, vehicle parking, security frisking, and emergency medical response station.</p>
    </div>

    <div class="sector-card">
      <span class="sector-num">SECTOR 02</span>
      <h3>SENATE AMPHITHEATRE</h3>
      <p>Western Choreo, Battle of the Bands, Mono Acting, and Night 03 Bollywood Grand Finale venue with tiered outdoor stone seating.</p>
    </div>

    <div class="sector-card">
      <span class="sector-num">SECTOR 03</span>
      <h3>OPEN AIR THEATRE (OAT)</h3>
      <p>Night 01 Rock & Metal concert grounds, acoustic vocal competitions, fire dance installations, and midnight food stalls.</p>
    </div>

    <div class="sector-card">
      <span class="sector-num">SECTOR 04</span>
      <h3>CENTRAL LIBRARY & LAWNS</h3>
      <p>Nukkad Natak street theatre, outdoor art installations, informal gaming arenas, chill-out zone, and archival polaroid exhibits.</p>
    </div>

    <div class="sector-card">
      <span class="sector-num">SECTOR 05</span>
      <h3>STUDENT ACTIVITY CENTRE</h3>
      <p>Purgatory LAN Gaming arena (CS2 & Valorant), indoor rehearsal halls, live charcoal art competitions, and organizing control room.</p>
    </div>

    <div class="sector-card">
      <span class="sector-num">SECTOR 06</span>
      <h3>HOSTEL CONTINGENTS</h3>
      <p>Outstation student accommodation wings, mess facilities, registration key desk, security checkpoint, and 24/7 help desk.</p>
    </div>
  </div>

  <!-- Travel Directives -->
  <div class="section-head">
    <span class="eyebrow">TRANSIT TO RUPNAGAR, PUNJAB</span>
    <h2>TRAVEL DIRECTIVES</h2>
  </div>

  <div class="travel-grid">
    <div class="travel-card">
      <h3>✈ BY AIR (FLIGHT)</h3>
      <p>
        The nearest airport is <strong>Shaheed Bhagat Singh International Airport, Chandigarh (IXC)</strong>, located 55 km from the IIT Ropar campus. Pre-booked festival shuttles and app-based cabs (Ola / Uber) operate directly from the terminal.
      </p>
    </div>

    <div class="travel-card">
      <h3>🚆 BY TRAIN (RAIL)</h3>
      <p>
        <strong>Rupnagar Railway Station (RPAR)</strong> is just 4 km from campus. <strong>Chandigarh Railway Station (CDG)</strong> is 45 km away with express connections across India. Free festival e-rickshaws will shuttle attendees from RPAR station.
      </p>
    </div>

    <div class="travel-card">
      <h3>🚗 BY ROAD (HIGHWAY)</h3>
      <p>
        Situated on <strong>NH 205 (Chandigarh-Manali Highway)</strong>. Direct luxury buses run regularly from ISBT 43 Chandigarh and ISBT Kashmiri Gate Delhi to Rupnagar Bus Stand (3 km from campus).
      </p>
    </div>
  </div>

  <!-- Comms Transmission Form -->
  <div class="comms-form-box">
    <span class="eyebrow" style="color:var(--crim);">TRANSMIT TO CONTROL ROOM</span>
    <h3>DIRECT INQUIRY FREQUENCY</h3>
    <form class="comms-form" id="contact-form">
      <div class="comms-field">
        <label for="c-name">Operative / Delegate Name *</label>
        <input type="text" id="c-name" required placeholder="e.g. Divyanshu Bansal">
      </div>
      <div class="comms-field">
        <label for="c-email">Comms Frequency (Email) *</label>
        <input type="email" id="c-email" required placeholder="delegate@college.edu">
      </div>
      <div class="comms-field">
        <label for="c-dept">Department Liaison</label>
        <select id="c-dept">
          <option value="General Festival Inquiry">General Festival Inquiry</option>
          <option value="Events & Arena Rules">Events & Arena Rules</option>
          <option value="Pronites & Concert Passes">Pronites & Concert Passes</option>
          <option value="Hospitality & Hostel Stay">Hospitality & Hostel Stay</option>
          <option value="Sponsorship & Brand Relations">Sponsorship & Brand Relations</option>
        </select>
      </div>
      <div class="comms-field">
        <label for="c-msg">Encrypted Transmission Message *</label>
        <textarea id="c-msg" rows="4" required placeholder="Transmit your query to the Zeitgeist Cultural Council..."></textarea>
      </div>
      <button class="btn btn-crim" type="submit" id="c-submit-btn" data-c="TRANSMIT">
        <span>TRANSMIT DISPATCH TO COMMAND</span>
      </button>
    </form>
  </div>
</main>
"""

    page_scripts = """
/* Contact Form Dispatch Simulation */
document.getElementById("contact-form").onsubmit = e => {
  e.preventDefault();
  const btn = document.getElementById("c-submit-btn");
  btn.setAttribute("aria-disabled", "true");
  btn.querySelector("span").textContent = "TRANSMITTING ENCRYPTED DISPATCH...";
  playGlitch();

  setTimeout(() => {
    btn.removeAttribute("aria-disabled");
    btn.querySelector("span").textContent = "TRANSMIT DISPATCH TO COMMAND";
    document.getElementById("contact-form").reset();
    playChime(500);
    toast("DISPATCH TRANSMITTED // RESPONSE LOGGED WITHIN 2 HOURS.");
  }, 1000);
};

// 3D Lanyard ID Badge Tilt Physics
document.querySelectorAll('.team-card').forEach(card => {
  card.addEventListener('pointermove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    // Pendulum swing centered from top clip
    const rx = ((y - cy) / cy) * -8;
    const ry = ((x - cx) / cx) * 10;
    const rz = ((x - cx) / cx) * 2;
    card.style.transform = `perspective(1000px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) rotateZ(${rz.toFixed(2)}deg) translateZ(16px)`;
  });
  card.addEventListener('pointerleave', () => {
    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translateZ(0px)';
  });
});

// 3D Sector Cards Hover Lift
document.querySelectorAll('.sector-card').forEach(card => {
  card.addEventListener('pointermove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rx = ((y - cy) / cy) * -6;
    const ry = ((x - cx) / cx) * 6;
    card.style.transform = `perspective(900px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(18px)`;
  });
  card.addEventListener('pointerleave', () => {
    card.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
  });
});
"""
    return title, description, extra_css, main_html, page_scripts
