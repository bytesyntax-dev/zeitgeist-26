# Generator for merchandise.html (Official Zeitgeist'26 Merchandise Vault)

def get_merchandise_content():
    title = "Official Merchandise Store | ZEITGEIST'26 | IIT Ropar"
    description = "Official festival merchandise for ZEITGEIST'26 at IIT Ropar. Official gothic T-Shirts in Regular & Oversized fits, and exclusive cursed heavyweight hoodie."

    extra_css = """
/* Merchandise Specific Styles */
.merch-hero {
  text-align: center;
  padding-top: clamp(100px, 12vh, 140px);
  padding-bottom: 20px;
  position: relative;
}

.merch-neon-hdr {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(34px, 5.5vw, 68px);
  font-weight: 900;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 12px;
  line-height: 1.1;
}

.merch-title-our {
  color: #ffffff;
  text-shadow: 0 0 16px rgba(255, 255, 255, 0.45), 0 0 30px rgba(192, 38, 211, 0.45);
}

.merch-title-glow {
  color: #f0abfc;
  text-shadow: 0 0 10px #e879f9, 0 0 25px #d946ef, 0 0 50px #a855f7, 0 0 80px #7e22ce;
}

.merch-subhdr {
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-size: clamp(20px, 2.8vw, 32px);
  font-weight: 800;
  letter-spacing: 0.16em;
  color: #ffffff;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.merch-desc {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(15px, 1.3vw, 19px);
  color: var(--bone-dim, #92877E);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.price-pills-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin: 12px 0 36px;
}

.price-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 24px;
  background: rgba(22, 11, 18, 0.85);
  border: 1px solid rgba(232, 121, 249, 0.35);
  border-radius: 9999px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(14px, 1.15vw, 17px);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #f5f3ff;
  box-shadow: 0 0 18px rgba(192, 38, 211, 0.18), inset 0 0 12px rgba(232, 121, 249, 0.1);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.price-pill .price-val {
  color: #f0abfc;
  font-weight: 800;
  font-size: 1.1em;
  text-shadow: 0 0 10px rgba(232, 121, 249, 0.6);
}

/* 4 T-Shirts Responsive Grid */
.merch-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 80px;
}

@media (max-width: 1200px) {
  .merch-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .merch-grid {
    grid-template-columns: 1fr;
  }
}

.merch-card {
  background: linear-gradient(180deg, #12090e 0%, #080407 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 18px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
}

.merch-card:hover {
  transform: translateY(-6px);
  border-color: rgba(217, 70, 239, 0.5);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.8), 0 0 28px rgba(192, 38, 211, 0.25);
}

.merch-card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.card-category-badge {
  font-family: 'Cinzel', serif;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #ffffff;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
}

.card-edition-badge {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #f0abfc;
  background: rgba(217, 70, 239, 0.15);
  border: 1px solid rgba(217, 70, 239, 0.3);
  padding: 3px 8px;
  border-radius: 4px;
}

.merch-img-container {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 5;
  border-radius: 12px;
  overflow: hidden;
  background: #060305;
  border: 1px solid rgba(255, 255, 255, 0.06);
  cursor: pointer;
}

.merch-img-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease, opacity 0.3s ease;
  display: block;
}

.merch-card:hover .merch-img-container img {
  transform: scale(1.04);
}

.zoom-hint {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  padding: 4px 10px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #fff;
  opacity: 0;
  transform: translateY(-4px);
  transition: all 0.25s ease;
  pointer-events: none;
}

.merch-card:hover .zoom-hint {
  opacity: 1;
  transform: translateY(0);
}

/* Card Fit Switcher */
.card-fit-switcher {
  display: flex;
  gap: 8px;
  margin: 12px 0 10px;
}

.fit-btn {
  flex: 1;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--bone-dim, #92877E);
  padding: 7px 4px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.fit-btn:hover {
  border-color: rgba(217, 70, 239, 0.4);
  color: #ffffff;
}

.fit-btn.active {
  background: rgba(217, 70, 239, 0.18);
  border-color: #d946ef;
  color: #ffffff;
  box-shadow: 0 0 12px rgba(217, 70, 239, 0.3);
}

.card-info {
  margin-top: 4px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.card-title {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #ffffff;
  text-transform: uppercase;
  margin-top: 2px;
}

.card-subtitle {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  color: var(--bone-dim, #92877E);
  letter-spacing: 0.06em;
}

.card-price-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.current-price {
  font-family: 'Cinzel', serif;
  font-size: 20px;
  font-weight: 900;
  color: #f0abfc;
  text-shadow: 0 0 12px rgba(217, 70, 239, 0.5);
}

.fit-note {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  color: var(--bone-dim, #92877E);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.card-action-btns {
  margin-top: 10px;
}

.btn-merch-order {
  width: 100%;
  background: linear-gradient(135deg, #a20d18 0%, #d10f20 100%);
  border: 1px solid #ff4d5e;
  color: #ffffff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-weight: 800;
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 4px 15px rgba(209, 15, 32, 0.35);
  text-align: center;
}

.btn-merch-order:hover {
  background: linear-gradient(135deg, #d10f20 0%, #ff1e38 100%);
  box-shadow: 0 6px 22px rgba(230, 28, 48, 0.6);
  transform: translateY(-2px);
}

/* ========================================================
   EXCLUSIVE HOODIE SECTION (Dedicated Bottom Showcase)
   ======================================================== */
.exclusive-hoodie-section {
  text-align: center;
  padding: 40px 0 90px;
  position: relative;
}

.hoodie-section-hdr {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(24px, 3.8vw, 44px);
  font-weight: 900;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #ffffff;
  margin-bottom: 26px;
  text-shadow: 0 0 16px rgba(255, 255, 255, 0.35), 0 0 30px rgba(217, 70, 239, 0.4);
}

.hoodie-showcase-box {
  max-width: 680px;
  margin: 0 auto;
  background: linear-gradient(180deg, #130a11 0%, #080407 100%);
  border: 1px solid rgba(217, 70, 239, 0.45);
  border-radius: 24px;
  padding: clamp(16px, 3vw, 24px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9), 0 0 40px rgba(217, 70, 239, 0.2);
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.hoodie-showcase-box:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.95), 0 0 50px rgba(217, 70, 239, 0.35);
  border-color: #d946ef;
}

.hoodie-img-wrap {
  width: 100%;
  aspect-ratio: 4 / 3.4;
  border-radius: 16px;
  overflow: hidden;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hoodie-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.hoodie-showcase-box:hover .hoodie-img-wrap img {
  transform: scale(1.03);
}

.hoodie-details-box {
  margin-top: 22px;
}

.hoodie-item-title {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(20px, 2.5vw, 30px);
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #ffffff;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.hoodie-meta-line {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(15px, 1.3vw, 19px);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #cbd5e1;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  margin-bottom: 20px;
}

.hoodie-meta-line .val {
  color: #ffffff;
  font-weight: 700;
}

.hoodie-meta-line .price-tag {
  color: #f0abfc;
  font-weight: 800;
  font-size: 1.15em;
  text-shadow: 0 0 10px rgba(217, 70, 239, 0.5);
}

.btn-hoodie-claim {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(135deg, #a20d18 0%, #d10f20 100%);
  border: 1px solid #ff4d5e;
  color: #ffffff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  padding: 13px 34px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 6px 20px rgba(209, 15, 32, 0.4);
}

.btn-hoodie-claim:hover {
  background: linear-gradient(135deg, #d10f20 0%, #ff1e38 100%);
  box-shadow: 0 8px 30px rgba(230, 28, 48, 0.65);
  transform: translateY(-2px);
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: rgba(3, 1, 3, 0.94);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lightbox-modal.active {
  display: flex;
}

.lightbox-box {
  position: relative;
  max-width: 900px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.lightbox-box img {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 12px;
  border: 1px solid rgba(217, 70, 239, 0.35);
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.9), 0 0 35px rgba(217, 70, 239, 0.25);
}

.lightbox-caption {
  margin-top: 14px;
  font-family: 'Cinzel', serif;
  font-size: 16px;
  letter-spacing: 0.12em;
  color: #ffffff;
  text-transform: uppercase;
  text-align: center;
}

.lightbox-close {
  position: absolute;
  top: -42px;
  right: 0;
  background: none;
  border: none;
  color: #ffffff;
  font-size: 32px;
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s;
}

.lightbox-close:hover {
  color: #e879f9;
}


"""

    main_html = """
<div style="max-width:1400px; margin:0 auto; padding:0 clamp(16px, 4vw, 50px); width:100%; box-sizing:border-box;">

  <!-- Hero Header shifted down with clean spacing -->
  <header class="merch-hero">
    <div class="merch-neon-hdr">
      <span class="merch-title-our">OUR</span> <span class="merch-title-glow">MERCHANDISE</span>
    </div>
    <div class="merch-subhdr">OFFICIAL T-SHIRTS</div>
    <p class="merch-desc">Available in various designs and fits</p>

    <!-- Pricing badges: Normal & Oversized -->
    <div class="price-pills-row">
      <div class="price-pill">
        <span>Normal:</span>
        <span class="price-val">₹399</span>
      </div>
      <div class="price-pill">
        <span>Oversized:</span>
        <span class="price-val">₹449</span>
      </div>
    </div>
  </header>

  <!-- 4 Official T-Shirts Grid in single clean row -->
  <div class="merch-grid" id="merch-grid">

    <!-- Card 1: Death Note -->
    <div class="merch-card" id="card-death-note">
      <div class="merch-card-top">
        <span class="card-category-badge">T-SHIRT</span>
        <span class="card-edition-badge">BLACK T-SHIRT</span>
      </div>
      <div class="merch-img-container" onclick="openLightbox('assets/merch/death-note-normal.png', 'Death Note // Regular Fit Black T-Shirt')">
        <img id="img-death-note" src="assets/merch/death-note-normal.png" alt="Death Note Official T-Shirt Zeitgeist" loading="lazy">
        <div class="zoom-hint">🔍 CLICK TO INSPECT</div>
      </div>
      <div class="card-fit-switcher">
        <button class="fit-btn active" onclick="switchCardFit('death-note', 'normal', 'assets/merch/death-note-normal.png', 399, 'Justice Is Served • Regular Fit', this)">Normal: ₹399</button>
        <button class="fit-btn" onclick="switchCardFit('death-note', 'oversized', 'assets/merch/death-note-oversized.png', 449, 'Oversized Fit Black T-Shirt', this)">Oversized: ₹449</button>
      </div>
      <div class="card-info">
        <div class="card-title">Death Note</div>
        <div class="card-subtitle" id="sub-death-note">Justice Is Served • Regular Fit</div>
        <div class="card-price-row">
          <div class="current-price" id="price-death-note">₹399</div>
          <div class="fit-note" id="fitlabel-death-note">Regular Fit</div>
        </div>
        <div class="card-action-btns">
          <button class="btn-merch-order" onclick="openMerchForm(event, 'Death Note')">Claim Yours Now</button>
        </div>
      </div>
    </div>

    <!-- Card 2: Fear The Dead -->
    <div class="merch-card" id="card-fear-dead">
      <div class="merch-card-top">
        <span class="card-category-badge">T-SHIRT</span>
        <span class="card-edition-badge">LIGHT GREY</span>
      </div>
      <div class="merch-img-container" onclick="openLightbox('assets/merch/fear-the-dead-normal.png', 'Fear The Dead // Regular Fit Grey T-Shirt')">
        <img id="img-fear-dead" src="assets/merch/fear-the-dead-normal.png" alt="Fear The Dead Official T-Shirt Zeitgeist" loading="lazy">
        <div class="zoom-hint">🔍 CLICK TO INSPECT</div>
      </div>
      <div class="card-fit-switcher">
        <button class="fit-btn active" onclick="switchCardFit('fear-dead', 'normal', 'assets/merch/fear-the-dead-normal.png', 399, 'Regular Fit Light Grey T-Shirt', this)">Normal: ₹399</button>
        <button class="fit-btn" onclick="switchCardFit('fear-dead', 'oversized', 'assets/merch/fear-the-dead-oversized.png', 449, 'Oversized Fit Light Grey T-Shirt', this)">Oversized: ₹449</button>
      </div>
      <div class="card-info">
        <div class="card-title">Fear The Dead</div>
        <div class="card-subtitle" id="sub-fear-dead">Why Do We Fear The Dead • Regular Fit</div>
        <div class="card-price-row">
          <div class="current-price" id="price-fear-dead">₹399</div>
          <div class="fit-note" id="fitlabel-fear-dead">Regular Fit</div>
        </div>
        <div class="card-action-btns">
          <button class="btn-merch-order" onclick="openMerchForm(event, 'Fear The Dead')">Claim Yours Now</button>
        </div>
      </div>
    </div>

    <!-- Card 3: Grim Reaper -->
    <div class="merch-card" id="card-grim-reaper">
      <div class="merch-card-top">
        <span class="card-category-badge">T-SHIRT</span>
        <span class="card-edition-badge">DARK BLUE</span>
      </div>
      <div class="merch-img-container" onclick="openLightbox('assets/merch/grim-reaper-normal.png', 'Grim Reaper // Dark Blue T-Shirt')">
        <img id="img-grim-reaper" src="assets/merch/grim-reaper-normal.png" alt="Grim Reaper Official T-Shirt Zeitgeist" loading="lazy">
        <div class="zoom-hint">🔍 CLICK TO INSPECT</div>
      </div>
      <div class="card-fit-switcher">
        <button class="fit-btn active" onclick="switchCardFit('grim-reaper', 'normal', 'assets/merch/grim-reaper-normal.png', 399, 'Regular Fit Dark Blue T-Shirt', this)">Normal: ₹399</button>
        <button class="fit-btn" onclick="switchCardFit('grim-reaper', 'oversized', 'assets/merch/grim-reaper-oversized.png', 449, 'Oversized Fit Dark Blue T-Shirt', this)">Oversized: ₹449</button>
      </div>
      <div class="card-info">
        <div class="card-title">Grim Reaper</div>
        <div class="card-subtitle" id="sub-grim-reaper">Hellscape Scythe • Regular Fit</div>
        <div class="card-price-row">
          <div class="current-price" id="price-grim-reaper">₹399</div>
          <div class="fit-note" id="fitlabel-grim-reaper">Regular Fit</div>
        </div>
        <div class="card-action-btns">
          <button class="btn-merch-order" onclick="openMerchForm(event, 'Grim Reaper')">Claim Yours Now</button>
        </div>
      </div>
    </div>

    <!-- Card 4: Hypnosis -->
    <div class="merch-card" id="card-hypnosis">
      <div class="merch-card-top">
        <span class="card-category-badge">T-SHIRT</span>
        <span class="card-edition-badge">EARTH BROWN</span>
      </div>
      <div class="merch-img-container" onclick="openLightbox('assets/merch/hypnosis-normal.png', 'Hypnosis // Earth Brown T-Shirt')">
        <img id="img-hypnosis" src="assets/merch/hypnosis-normal.png" alt="Hypnosis Official T-Shirt Zeitgeist" loading="lazy">
        <div class="zoom-hint">🔍 CLICK TO INSPECT</div>
      </div>
      <div class="card-fit-switcher">
        <button class="fit-btn active" onclick="switchCardFit('hypnosis', 'normal', 'assets/merch/hypnosis-normal.png', 399, 'Regular Fit Brown T-Shirt', this)">Normal: ₹399</button>
        <button class="fit-btn" onclick="switchCardFit('hypnosis', 'oversized', 'assets/merch/hypnosis-oversized.png', 449, 'Oversized Fit Brown T-Shirt', this)">Oversized: ₹449</button>
      </div>
      <div class="card-info">
        <div class="card-title">Hypnosis</div>
        <div class="card-subtitle" id="sub-hypnosis">Witness Surreal Hypnosis • Regular Fit</div>
        <div class="card-price-row">
          <div class="current-price" id="price-hypnosis">₹399</div>
          <div class="fit-note" id="fitlabel-hypnosis">Regular Fit</div>
        </div>
        <div class="card-action-btns">
          <button class="btn-merch-order" onclick="openMerchForm(event, 'Hypnosis')">Claim Yours Now</button>
        </div>
      </div>
    </div>

  </div>

  <!-- Dedicated EXCLUSIVE HOODIE Section (Matching user reference layout) -->
  <section class="exclusive-hoodie-section">
    <h2 class="hoodie-section-hdr">EXCLUSIVE HOODIE</h2>

    <div class="hoodie-showcase-box" onclick="openLightbox('assets/merch/cursed-pokemon-hoodie.png', 'Cursed Pokemon // Heavyweight Black Fleece Hoodie')">
      <div class="hoodie-img-wrap">
        <img src="assets/merch/cursed-pokemon-hoodie.png" alt="Zeitgeist Cursed Pokemon Hoodie" loading="lazy">
      </div>
    </div>

    <div class="hoodie-details-box">
      <h3 class="hoodie-item-title">ZEITGEIST CURSED HOODIE</h3>
      <div class="hoodie-meta-line">
        <span>Color: <span class="val">Black</span></span>
        <span>Price: <span class="price-tag">TBA</span></span>
      </div>
      <button class="btn-hoodie-claim" onclick="openMerchForm(event, 'Zeitgeist Cursed Hoodie')">
        Claim Hoodie Now →
      </button>
    </div>
  </section>

</div>

<!-- High Resolution Lightbox Modal -->
<div class="lightbox-modal" id="lightbox-modal" onclick="closeLightbox(event)">
  <div class="lightbox-box">
    <button class="lightbox-close" onclick="closeLightboxDirect()">✕</button>
    <img id="lightbox-img" src="" alt="Merch Full View">
    <div class="lightbox-caption" id="lightbox-caption"></div>
  </div>
</div>
"""

    page_scripts = """
// 🔗 Enter your Google Form URL here when available:
const MERCH_GOOGLE_FORM_URL = "";

function openMerchForm(e, itemName) {
  if (e && e.preventDefault) e.preventDefault();
  if (MERCH_GOOGLE_FORM_URL && MERCH_GOOGLE_FORM_URL.trim() !== '' && MERCH_GOOGLE_FORM_URL !== '#') {
    window.open(MERCH_GOOGLE_FORM_URL, '_blank');
  } else {
    alert('The official Google Form for Zeitgeist Merchandise pre-orders will be released shortly. Stay tuned!');
    if (window.toast) {
      window.toast('📋 Merchandise Google Form link coming soon!');
    }
  }
}

function switchCardFit(cardId, fitType, imgPath, price, subtitle, btn) {
  const card = document.getElementById('card-' + cardId);
  if (!card) return;

  // Toggle active button style
  card.querySelectorAll('.fit-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  // Change image
  const img = document.getElementById('img-' + cardId);
  if (img) {
    img.style.opacity = '0.3';
    setTimeout(() => {
      img.src = imgPath;
      img.style.opacity = '1';
    }, 150);
  }

  // Update container onclick for lightbox
  const container = card.querySelector('.merch-img-container');
  if (container) {
    container.onclick = () => openLightbox(imgPath, cardId.replace('-', ' ').toUpperCase() + ' // ' + subtitle);
  }

  // Update price and labels
  const priceEl = document.getElementById('price-' + cardId);
  if (priceEl) priceEl.innerText = price === 'TBA' ? 'TBA' : ('₹' + price);

  const subEl = document.getElementById('sub-' + cardId);
  if (subEl) subEl.innerText = subtitle;

  const fitEl = document.getElementById('fitlabel-' + cardId);
  if (fitEl) fitEl.innerText = fitType === 'normal' ? 'Regular Fit' : 'Oversized Fit';

  // Update order button
  const orderBtn = card.querySelector('.btn-merch-order');
  if (orderBtn) {
    const rawName = card.querySelector('.card-title') ? card.querySelector('.card-title').innerText : 'T-Shirt';
    orderBtn.onclick = (e) => openMerchForm(e, rawName + ' (' + (fitType === 'normal' ? 'Normal Fit' : 'Oversized Fit') + ')');
  }
}

function openLightbox(src, caption) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  const cap = document.getElementById('lightbox-caption');
  if (!modal || !img) return;

  img.src = src;
  cap.innerText = caption || 'Zeitgeist Official Merch';
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox(e) {
  if (e.target.id === 'lightbox-modal') {
    closeLightboxDirect();
  }
}

function closeLightboxDirect() {
  const modal = document.getElementById('lightbox-modal');
  if (modal) modal.classList.remove('active');
  document.body.style.overflow = '';
}
"""

    return title, description, extra_css, main_html, page_scripts
