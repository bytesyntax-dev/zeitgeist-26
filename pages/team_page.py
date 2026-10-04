# Generator for team.html (Organizing Committee & Council Dossier)

def get_team_content():
    title = "The Council — Organizing Team | ZEITGEIST'26 | IIT Ropar"
    description = "Meet the student coordinators, department heads, and visionaries orchestrating ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Team Specific Styles */
.team-hero {
  margin-bottom: 40px;
}

.team-hero h1 {
  font-size: clamp(38px, 7vw, 86px);
  margin-top: 14px;
}

.team-filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 44px;
}

.dept-chip {
  padding: 8px 18px;
  background: rgba(14, 10, 13, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--bone-dim);
  font: 600 11px var(--mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.dept-chip:hover, .dept-chip.active {
  background: var(--crim);
  color: #fff;
  border-color: var(--crim-bright);
  box-shadow: 0 0 15px var(--crim-glow);
}

.lead-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
  margin-bottom: 60px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
  margin-bottom: 80px;
}

.council-card {
  background: rgba(14, 11, 13, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 24px;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
}

.council-card:hover {
  transform: translateY(-6px);
  border-color: var(--crim);
  box-shadow: 0 14px 34px rgba(148, 23, 34, 0.3);
}

.council-card.lead-card {
  border-color: rgba(173, 95, 38, 0.4);
  background: linear-gradient(180deg, rgba(24, 12, 16, 0.95), rgba(12, 6, 8, 0.95));
}

.council-card.lead-card:hover {
  border-color: var(--amber);
  box-shadow: 0 14px 34px rgba(173, 95, 38, 0.3);
}

.avatar-frame {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid var(--crim);
  display: flex;
  align-items: center;
  justify-content: center;
  font: 700 24px var(--serif);
  color: var(--bone);
  margin-bottom: 18px;
  box-shadow: 0 0 16px rgba(148, 23, 34, 0.35);
}

.council-card.lead-card .avatar-frame {
  border-color: var(--amber);
  box-shadow: 0 0 18px rgba(173, 95, 38, 0.4);
}

.member-role {
  font: 600 10px var(--mono);
  letter-spacing: 0.2em;
  color: var(--crim-bright);
  text-transform: uppercase;
  margin-bottom: 6px;
}

.council-card.lead-card .member-role {
  color: var(--amber);
}

.member-name {
  font: 700 22px var(--serif);
  color: var(--bone);
  margin-bottom: 8px;
}

.member-dept {
  font: 400 12px var(--sans);
  color: var(--bone-dim);
  margin-bottom: 18px;
}

.contact-links {
  margin-top: auto;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.contact-line {
  font: 500 11px var(--mono);
  color: var(--ash);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  transition: color 0.2s;
}

.contact-line:hover {
  color: var(--amber);
}
"""

    main_html = """
<main id="team">
<header class="team-hero rv">
  <div class="goth-tag">
    <span class="tag-glyph">☠</span>
    <span>ARCHIVE 09 // FESTIVAL SECRETARIAT</span>
  </div>
  <h1 class="disp">The Council.</h1>
  <p style="font:400 14px/1.8 var(--sans); color:var(--bone-dim); max-width:680px; margin-top:16px;">
    The architects, custodians, and operatives behind the curtain. Reach out to department leads for arena logistics, corporate tie-ups, registrations, and artist handling.
  </p>
</header>

<div class="team-filter-bar rv">
  <button class="dept-chip active" data-filter="all">All Cadres (22)</button>
  <button class="dept-chip" data-filter="lead">Overall Leads</button>
  <button class="dept-chip" data-filter="web">Web & Tech</button>
  <button class="dept-chip" data-filter="spons">Sponsorship</button>
  <button class="dept-chip" data-filter="security">Security & Protocols</button>
  <button class="dept-chip" data-filter="content">Content & Anchoring</button>
  <button class="dept-chip" data-filter="media">Video & Coverage</button>
  <button class="dept-chip" data-filter="hosp">Hospitality</button>
  <button class="dept-chip" data-filter="publicity">Media & Publicity</button>
</div>

<!-- OVERALL COORDINATORS -->
<h2 class="disp" style="font-size:24px; color:var(--amber); margin-bottom:20px;" class="rv">Festival Leadership</h2>
<div class="lead-grid rv">
  <div class="council-card lead-card" data-category="lead">
    <div class="avatar-frame">NM</div>
    <div class="member-role">Overall Coordinator</div>
    <div class="member-name">Nikunj Mahajan</div>
    <div class="member-dept">Board of Cultural Activities, IIT Ropar</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919872475955">📞 +91 98724 75955</a>
      <a class="contact-line" href="mailto:2023meb1363@iitrpr.ac.in">✉ 2023meb1363@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card lead-card" data-category="lead">
    <div class="avatar-frame">PA</div>
    <div class="member-role">Overall Coordinator</div>
    <div class="member-name">Pranshu Aggarwal</div>
    <div class="member-dept">Board of Cultural Activities, IIT Ropar</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919814676399">📞 +91 98146 76399</a>
      <a class="contact-line" href="mailto:2023mmb1420@iitrpr.ac.in">✉ 2023mmb1420@iitrpr.ac.in</a>
    </div>
  </div>
</div>

<!-- DEPARTMENT HEADS -->
<h2 class="disp" style="font-size:24px; color:var(--bone); margin-bottom:20px;" class="rv">Department Commanders</h2>
<div class="team-grid rv" id="team-cards-wrap">
  <!-- WEB & TECH -->
  <div class="council-card" data-category="web">
    <div class="avatar-frame">CP</div>
    <div class="member-role">Web Development Head</div>
    <div class="member-name">Charvi Pahuja</div>
    <div class="member-dept">Digital Grid & Portals</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918076668905">📞 +91 80766 68905</a>
      <a class="contact-line" href="mailto:2023csb1114@iitrpr.ac.in">✉ 2023csb1114@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="web">
    <div class="avatar-frame">KA</div>
    <div class="member-role">Web Development Head</div>
    <div class="member-name">Krishna Agarwal</div>
    <div class="member-dept">Digital Grid & Infrastructure</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919667612704">📞 +91 96676 12704</a>
      <a class="contact-line" href="mailto:2023csb1131@iitrpr.ac.in">✉ 2023csb1131@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- SPONSORSHIP -->
  <div class="council-card" data-category="spons">
    <div class="avatar-frame">TM</div>
    <div class="member-role">Sponsorship Head</div>
    <div class="member-name">Tamanna</div>
    <div class="member-dept">Corporate Alliances</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+917009756939">📞 +91 70097 56939</a>
      <a class="contact-line" href="mailto:2023csb1169@iitrpr.ac.in">✉ 2023csb1169@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="spons">
    <div class="avatar-frame">KG</div>
    <div class="member-role">Sponsorship Head</div>
    <div class="member-name">Kamakshi Gupta</div>
    <div class="member-dept">Corporate Alliances</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919315575840">📞 +91 93155 75840</a>
      <a class="contact-line" href="mailto:2023aib1008@iitrpr.ac.in">✉ 2023aib1008@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="spons">
    <div class="avatar-frame">AI</div>
    <div class="member-role">Sponsorship Head</div>
    <div class="member-name">Aditya Ingle</div>
    <div class="member-dept">Corporate Alliances</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918766483216">📞 +91 87664 83216</a>
      <a class="contact-line" href="mailto:2023eeb1178@iitrpr.ac.in">✉ 2023eeb1178@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="spons">
    <div class="avatar-frame">RS</div>
    <div class="member-role">Sponsorship Head</div>
    <div class="member-name">Raj Sureka</div>
    <div class="member-dept">Corporate Alliances</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919320893180">📞 +91 93208 93180</a>
      <a class="contact-line" href="mailto:2023epb1282@iitrpr.ac.in">✉ 2023epb1282@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="spons">
    <div class="avatar-frame">UA</div>
    <div class="member-role">Sponsorship Head</div>
    <div class="member-name">Udish Arora</div>
    <div class="member-dept">Corporate Alliances</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919878169201">📞 +91 98781 69201</a>
      <a class="contact-line" href="mailto:2023aib1316@iitrpr.ac.in">✉ 2023aib1316@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- SECURITY -->
  <div class="council-card" data-category="security">
    <div class="avatar-frame">AC</div>
    <div class="member-role">Security Head</div>
    <div class="member-name">Anuj Choudhary</div>
    <div class="member-dept">Campus Defense Grid & Crowd Control</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919160823790">📞 +91 91608 23790</a>
      <a class="contact-line" href="mailto:security.zeitgeist@iitrpr.ac.in">✉ security.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="security">
    <div class="avatar-frame">SS</div>
    <div class="member-role">Security Head</div>
    <div class="member-name">Shubham Singh</div>
    <div class="member-dept">Gate Control & VIP Enclosures</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919315575840">📞 +91 93155 75840</a>
      <a class="contact-line" href="mailto:2023meb1381@iitrpr.ac.in">✉ 2023meb1381@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="security">
    <div class="avatar-frame">GV</div>
    <div class="member-role">Security Head</div>
    <div class="member-name">Gunjan Verma</div>
    <div class="member-dept">Arena Vigilance</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918306867356">📞 +91 83068 67356</a>
      <a class="contact-line" href="mailto:2023meb1343@iitrpr.ac.in">✉ 2023meb1343@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- CONTENT & ANCHORING -->
  <div class="council-card" data-category="content">
    <div class="avatar-frame">LM</div>
    <div class="member-role">Content & Anchoring</div>
    <div class="member-name">Lakshay Manchanda</div>
    <div class="member-dept">Scripts & Stage Conclaves</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+917082450024">📞 +91 70824 50024</a>
      <a class="contact-line" href="mailto:content.zeitgeist@iitrpr.ac.in">✉ content.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="content">
    <div class="avatar-frame">AT</div>
    <div class="member-role">Content & Anchoring</div>
    <div class="member-name">Ayush Tiwari</div>
    <div class="member-dept">Scripts & Editorial</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918178308335">📞 +91 81783 08335</a>
      <a class="contact-line" href="mailto:2023meb1333@iitrpr.ac.in">✉ 2023meb1333@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- VIDEO & COVERAGE -->
  <div class="council-card" data-category="media">
    <div class="avatar-frame">PC</div>
    <div class="member-role">Video & Coverage</div>
    <div class="member-name">Pratyush Chauhan</div>
    <div class="member-dept">Cinematics & Aftermovies</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+917876853698">📞 +91 78768 53698</a>
      <a class="contact-line" href="mailto:2023mcb1310@iitrpr.ac.in">✉ 2023mcb1310@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="media">
    <div class="avatar-frame">PK</div>
    <div class="member-role">Video & Coverage</div>
    <div class="member-name">Prabhreet Kaur</div>
    <div class="member-dept">Live Broadcasts</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+917719715449">📞 +91 77197 15449</a>
      <a class="contact-line" href="mailto:2023meb1368@iitrpr.ac.in">✉ 2023meb1368@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="media">
    <div class="avatar-frame">HS</div>
    <div class="member-role">Video & Coverage</div>
    <div class="member-name">Hemant</div>
    <div class="member-dept">Camera Operations</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918708987930">📞 +91 87089 87930</a>
      <a class="contact-line" href="mailto:media.zeitgeist@iitrpr.ac.in">✉ media.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- HOSPITALITY -->
  <div class="council-card" data-category="hosp">
    <div class="avatar-frame">MA</div>
    <div class="member-role">Hospitality Head</div>
    <div class="member-name">Malay Ayachit</div>
    <div class="member-dept">Guest Accommodations</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919425607657">📞 +91 94256 07657</a>
      <a class="contact-line" href="mailto:2023mmb1415@iitrpr.ac.in">✉ 2023mmb1415@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="hosp">
    <div class="avatar-frame">AK</div>
    <div class="member-role">Hospitality Head</div>
    <div class="member-name">Atul Kharat</div>
    <div class="member-dept">Logistics & Transit</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919404725169">📞 +91 94047 25169</a>
      <a class="contact-line" href="mailto:2023csb1105@iitrpr.ac.in">✉ 2023csb1105@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="hosp">
    <div class="avatar-frame">AS</div>
    <div class="member-role">Hospitality Head</div>
    <div class="member-name">Ayush Singh</div>
    <div class="member-dept">Food Courts & Stalls</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919034422154">📞 +91 90344 22154</a>
      <a class="contact-line" href="mailto:2023meb1332@iitrpr.ac.in">✉ 2023meb1332@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- GRAPHICS -->
  <div class="council-card" data-category="web">
    <div class="avatar-frame">AM</div>
    <div class="member-role">Graphic Designing Head</div>
    <div class="member-name">Aadit Mahajan</div>
    <div class="member-dept">Visual Identity & Art Assets</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919103545236">📞 +91 91035 45236</a>
      <a class="contact-line" href="mailto:design.zeitgeist@iitrpr.ac.in">✉ design.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>

  <!-- PUBLICITY -->
  <div class="council-card" data-category="publicity">
    <div class="avatar-frame">HG</div>
    <div class="member-role">Media & Publicity</div>
    <div class="member-name">Harshit</div>
    <div class="member-dept">National Outreach</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+918052208269">📞 +91 80522 08269</a>
      <a class="contact-line" href="mailto:publicity.zeitgeist@iitrpr.ac.in">✉ publicity.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="publicity">
    <div class="avatar-frame">AS</div>
    <div class="member-role">Media & Publicity</div>
    <div class="member-name">Aditya Sharma</div>
    <div class="member-dept">Campus Ambassadors</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+917665489941">📞 +91 76654 89941</a>
      <a class="contact-line" href="mailto:2023meb1325@iitrpr.ac.in">✉ 2023meb1325@iitrpr.ac.in</a>
    </div>
  </div>

  <div class="council-card" data-category="publicity">
    <div class="avatar-frame">KI</div>
    <div class="member-role">Media & Publicity</div>
    <div class="member-name">Kabir Inamdar</div>
    <div class="member-dept">Press & External Media</div>
    <div class="contact-links">
      <a class="contact-line" href="tel:+919315575840">📞 +91 93155 75840</a>
      <a class="contact-line" href="mailto:press.zeitgeist@iitrpr.ac.in">✉ press.zeitgeist@iitrpr.ac.in</a>
    </div>
  </div>
</div>
</main>
"""

    page_scripts = """
// Interactive filter chips for departments
document.querySelectorAll('.dept-chip').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.dept-chip').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    document.querySelectorAll('.council-card').forEach(card => {
      if (filter === 'all' || card.dataset.category === filter) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  });
});
"""

    return title, description, extra_css, main_html, page_scripts
