# Generator for sponsors.html (Partners & Benefactors Dossier)

def get_sponsors_content():
    title = "Official Partners & Sponsors | ZEITGEIST'26 | IIT Ropar"
    description = "Explore the esteemed corporate partners, title benefactors, and alliances powering ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Sponsors Specific Styles */
.sponsors-hero {
  margin-bottom: 50px;
}

.sponsors-hero h1 {
  font-size: clamp(38px, 7vw, 86px);
  margin-top: 14px;
}

.tier-section {
  margin-bottom: 70px;
}

.tier-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 30px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.tier-title {
  font: 700 13px var(--mono);
  letter-spacing: 0.25em;
  color: var(--amber);
  text-transform: uppercase;
}

.sponsors-grid-major {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 28px;
}

.sponsors-grid-mid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 22px;
}

.sponsors-grid-compact {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
}

.sponsor-card {
  background: rgba(14, 11, 13, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 36px 28px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.sponsor-card:hover {
  transform: translateY(-5px);
  border-color: var(--crim);
  box-shadow: 0 12px 30px rgba(148, 23, 34, 0.25);
}

.sponsor-badge {
  font: 600 10px var(--mono);
  letter-spacing: 0.2em;
  color: var(--crim-bright);
  text-transform: uppercase;
  margin-bottom: 20px;
  padding: 4px 10px;
  background: rgba(148, 23, 34, 0.15);
  border: 1px solid rgba(230, 28, 48, 0.3);
  border-radius: 4px;
}

.sponsor-logo-wrap {
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 22px;
  width: 100%;
}

.sponsor-name {
  font: 700 22px var(--serif);
  color: var(--bone);
  margin-bottom: 8px;
}

.sponsor-role {
  font: 400 12px/1.5 var(--sans);
  color: var(--bone-dim);
  margin-bottom: 18px;
}

.sponsor-link {
  font: 600 11px var(--mono);
  letter-spacing: 0.15em;
  color: var(--amber);
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s, transform 0.2s;
}

.sponsor-link:hover {
  color: var(--bone);
  transform: translateX(4px);
}

.stats-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 60px 0;
  background: rgba(10, 8, 9, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 30px;
  border-radius: 8px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font: 700 36px var(--serif);
  color: var(--crim-bright);
  margin-bottom: 4px;
}

.stat-label {
  font: 600 11px var(--mono);
  letter-spacing: 0.15em;
  color: var(--ash);
  text-transform: uppercase;
}

.dossier-cta-box {
  background: linear-gradient(135deg, rgba(20, 8, 12, 0.95), rgba(8, 4, 6, 0.95));
  border: 1px solid var(--crim);
  padding: 50px 36px;
  border-radius: 8px;
  text-align: center;
  margin-top: 60px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.6);
}
"""

    main_html = """
<main id="sponsors">
<header class="sponsors-hero rv">
  <div class="goth-tag">
    <span class="tag-glyph">⚔</span>
    <span>ARCHIVE 08 // ALLIANCES & PATRONS</span>
  </div>
  <h1 class="disp">The Benefactors.</h1>
  <p style="font:400 14px/1.8 var(--sans); color:var(--bone-dim); max-width:680px; margin-top:16px;">
    The monumental cultural rites of ZEITGEIST'26 are made possible through the backing of forward-thinking national leaders, industrial titans, and premier lifestyle innovators.
  </p>
</header>

<div class="stats-bar rv">
  <div class="stat-item">
    <div class="stat-number">250+</div>
    <div class="stat-label">Colleges Represented</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">12,000+</div>
    <div class="stat-label">Student Footfall</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">1.5M+</div>
    <div class="stat-label">Digital Impressions</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">₹15L+</div>
    <div class="stat-label">Total Prize Bounty</div>
  </div>
</div>

<!-- TITLE & CO-TITLE SPONSORS -->
<section class="tier-section rv">
  <div class="tier-header">
    <span class="tag-glyph" style="color:var(--crim-bright);">✦</span>
    <h2 class="tier-title">Title & Principal Benefactors</h2>
  </div>

  <div class="sponsors-grid-major">
    <div class="sponsor-card">
      <span class="sponsor-badge">Powered by // Title Partner</span>
      <div class="sponsor-logo-wrap">
        <svg viewBox="0 0 200 60" style="max-height:50px; fill:var(--bone);">
          <text x="100" y="38" font-family="var(--sans)" font-weight="700" font-size="20" text-anchor="middle" fill="#fff" letter-spacing="2">REALTY NATION</text>
        </svg>
      </div>
      <h3 class="sponsor-name">Realty Nation</h3>
      <p class="sponsor-role">Leading national real estate advisory powering student opportunities and grand festival stages.</p>
      <a class="sponsor-link" href="https://realtynationusa.com/" target="_blank" rel="noopener noreferrer">Visit Portal ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Co-Powered by</span>
      <div class="sponsor-logo-wrap">
        <svg viewBox="0 0 200 60" style="max-height:50px; fill:var(--bone);">
          <text x="100" y="38" font-family="var(--sans)" font-weight="700" font-size="22" text-anchor="middle" fill="#fff" letter-spacing="3">TATA STEEL</text>
        </svg>
      </div>
      <h3 class="sponsor-name">Tata Steel</h3>
      <p class="sponsor-role">Pioneering industrial strength and engineering excellence partnering in youth empowerment.</p>
      <a class="sponsor-link" href="https://www.tatasteel.com/" target="_blank" rel="noopener noreferrer">Visit Portal ↗</a>
    </div>
  </div>
</section>

<!-- ASSOCIATE PARTNERS -->
<section class="tier-section rv">
  <div class="tier-header">
    <span class="tag-glyph" style="color:var(--amber);">◈</span>
    <h2 class="tier-title">In Association With</h2>
  </div>

  <div class="sponsors-grid-mid">
    <div class="sponsor-card">
      <span class="sponsor-badge" style="color:var(--amber); border-color:rgba(173,95,38,0.3); background:rgba(173,95,38,0.1);">Associate Partner</span>
      <div class="sponsor-logo-wrap">
        <svg viewBox="0 0 160 50" style="max-height:44px;">
          <text x="80" y="32" font-family="var(--sans)" font-weight="700" font-size="20" text-anchor="middle" fill="var(--bone)" letter-spacing="2">VERKA</text>
        </svg>
      </div>
      <h3 class="sponsor-name">Verka</h3>
      <p class="sponsor-role">Punjab's pride dairy federation refreshing campus arenas with pure nutrition.</p>
      <a class="sponsor-link" href="https://verka.coop/" target="_blank" rel="noopener noreferrer">Official Portal ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge" style="color:var(--amber); border-color:rgba(173,95,38,0.3); background:rgba(173,95,38,0.1);">Associate Partner</span>
      <div class="sponsor-logo-wrap">
        <svg viewBox="0 0 200 50" style="max-height:44px;">
          <text x="100" y="32" font-family="var(--sans)" font-weight="700" font-size="16" text-anchor="middle" fill="var(--bone)" letter-spacing="2">DESI URBAN CHAI</text>
        </svg>
      </div>
      <h3 class="sponsor-name">Desi Urban Chai</h3>
      <p class="sponsor-role">Authentic artisan brews keeping minds fueled across three midnight rituals.</p>
      <a class="sponsor-link" href="https://desiurbanchai.com/" target="_blank" rel="noopener noreferrer">Official Portal ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge" style="color:var(--amber); border-color:rgba(173,95,38,0.3); background:rgba(173,95,38,0.1);">Associate Partner</span>
      <div class="sponsor-logo-wrap">
        <svg viewBox="0 0 200 50" style="max-height:44px;">
          <text x="100" y="32" font-family="var(--sans)" font-weight="700" font-size="16" text-anchor="middle" fill="var(--bone)" letter-spacing="2">ESS COMPANIES</text>
        </svg>
      </div>
      <h3 class="sponsor-name">ESS Construction</h3>
      <p class="sponsor-role">Infrastructure visionaries supporting architectural staging and student designs.</p>
      <a class="sponsor-link" href="https://esscompanies.com/" target="_blank" rel="noopener noreferrer">Official Portal ↗</a>
    </div>
  </div>
</section>

<!-- CATEGORY & LIFESTYLE PARTNERS -->
<section class="tier-section rv">
  <div class="tier-header">
    <span class="tag-glyph">⬡</span>
    <h2 class="tier-title">Category & Lifestyle Partners</h2>
  </div>

  <div class="sponsors-grid-compact">
    <div class="sponsor-card">
      <span class="sponsor-badge">Fragrance Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">MYOP</h3>
      <p class="sponsor-role">Make Your Own Perfume</p>
      <a class="sponsor-link" href="https://myop.in/" target="_blank" rel="noopener noreferrer">myop.in ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Hair Care Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">2.Oh!</h3>
      <p class="sponsor-role">Color and Care Specialist</p>
      <a class="sponsor-link" href="https://www.2pointoh.in/" target="_blank" rel="noopener noreferrer">2pointoh.in ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Banking Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Bank of Maharashtra</h3>
      <p class="sponsor-role">One Family, One Bank</p>
      <a class="sponsor-link" href="https://bankofmaharashtra.bank.in/" target="_blank" rel="noopener noreferrer">bankofmaharashtra.in ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Streaming Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">JioSaavn</h3>
      <p class="sponsor-role">Official Music Streamer</p>
      <a class="sponsor-link" href="https://www.jiosaavn.com/" target="_blank" rel="noopener noreferrer">jiosaavn.com ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Merch Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Kapdamart</h3>
      <p class="sponsor-role">Official Festival Wear</p>
      <a class="sponsor-link" href="https://kapdamart.com/" target="_blank" rel="noopener noreferrer">kapdamart.com ↗</a>
    </div>

    <div class="sponsor-card">
      <span class="sponsor-badge">Hydration Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Bluora</h3>
      <p class="sponsor-role">Pure Hydration Grid</p>
      <span class="eyebrow" style="color:var(--ash);">Campus Arena</span>
    </div>
  </div>
</section>

<!-- PRESENTED BY -->
<section class="tier-section rv">
  <div class="tier-header">
    <span class="tag-glyph">⬡</span>
    <h2 class="tier-title">Presented By</h2>
  </div>

  <div class="sponsors-grid-compact">
    <div class="sponsor-card">
      <span class="sponsor-badge">Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Konark Global</h3>
      <p class="sponsor-role">Global Hospitality Services</p>
    </div>
    <div class="sponsor-card">
      <span class="sponsor-badge">Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Anusha Hospitality</h3>
      <p class="sponsor-role">Guest Logistics & Services</p>
    </div>
    <div class="sponsor-card">
      <span class="sponsor-badge">Partner</span>
      <h3 class="sponsor-name" style="font-size:18px;">Ideal Catering</h3>
      <p class="sponsor-role">Food Courts & Banquet Lead</p>
    </div>
  </div>
</section>

<!-- CALL TO ACTION FOR SPONSORSHIP -->
<div class="dossier-cta-box rv">
  <span class="eyebrow" style="color:var(--amber);">COLLABORATE WITH ZEITGEIST'26</span>
  <h2 class="disp" style="font-size:clamp(28px, 4vw, 44px); margin:12px 0 16px;">Partner With North India's Cultural Colossus.</h2>
  <p style="font:400 13px/1.8 var(--sans); color:var(--bone-dim); max-width:620px; margin:0 auto 28px;">
    Position your brand in front of 12,000+ top engineering and design minds from across India. Custom brand integrations, on-ground experiential arenas, and digital broadcasts available.
  </p>
  <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
    <a class="btn" href="mailto:sponsors.zeitgeist@iitrpr.ac.in">REQUEST SPONSORSHIP DECK →</a>
    <a class="btn" href="contact.html" style="background:transparent; border:1px solid rgba(255,255,255,0.2);">SPEAK TO LIAISONS</a>
  </div>
</div>
</main>
"""

    page_scripts = """
// Subtle reveal hooks
console.log("Benefactors dossier mounted successfully.");
"""

    return title, description, extra_css, main_html, page_scripts
