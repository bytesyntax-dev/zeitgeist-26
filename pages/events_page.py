# Generator for events.html (Official Competitive Arenas & Dockets Catalog)
import json

def get_events_content():
    title = "The Archives — Events & Competitions | ZEITGEIST'26 | IIT Ropar"
    description = "Official catalog of all 24+ competitive arenas, unstop registration portals, and downloadable rulebooks for ZEITGEIST'26 at IIT Ropar."

    extra_css = """
/* Events Catalog Styles */
.events-hero {
  margin-bottom: 32px;
}

.events-hero h1 {
  font-size: clamp(34px, 6.5vw, 76px);
  margin-top: 10px;
  line-height: 1.05;
}



/* Search and Controls Bar */
.catalog-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 32px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.search-box-wrap {
  position: relative;
  min-width: 280px;
  flex: 1;
  max-width: 480px;
}

.search-input {
  width: 100%;
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 12px 18px 12px 42px;
  color: var(--bone);
  font: 400 13px var(--mono);
  border-radius: 999px;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
  box-sizing: border-box;
}

.search-input:focus {
  border-color: var(--crim);
  background: var(--surface);
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ash);
  font-size: 14px;
  pointer-events: none;
}

.stats-badge {
  font: 600 11px var(--mono);
  letter-spacing: 0.15em;
  color: var(--ash);
  text-transform: uppercase;
}

.stats-badge span {
  color: var(--amber);
  font-weight: 700;
}

/* Catalog Card Grid */
.catalog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 32px;
  margin-bottom: 80px;
}

/* Card Shell matching Reference Design with Moonlit Revelry Theme */
.catalog-card {
  background: #090608;
  border: 1px solid rgba(209, 15, 32, 0.5);
  border-radius: 14px;
  padding: 24px 20px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  box-shadow: 0 0 24px rgba(209, 15, 32, 0.15), inset 0 0 16px rgba(0, 0, 0, 0.9);
  outline: 1.5px solid rgba(255, 255, 255, 0.05);
  outline-offset: -8px;
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.28s, border-color 0.28s;
  overflow: hidden;
}

.catalog-card:hover {
  transform: translateY(-6px);
  border-color: var(--crim-bright);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.85), 0 0 32px var(--crim-glow), inset 0 0 20px rgba(209, 15, 32, 0.22);
}

.catalog-card-header {
  width: 100%;
  text-align: center;
  margin-bottom: 16px;
  min-height: 54px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.catalog-card-title {
  font: 700 clamp(18px, 1.7vw, 22px)/1.2 var(--disp-sans, var(--serif));
  color: var(--bone);
  letter-spacing: 0.03em;
  text-transform: capitalize;
}

.catalog-card-sub {
  font: 500 11px var(--mono);
  color: var(--ash);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-top: 4px;
}

/* Card Poster Image Container */
.catalog-card-media {
  width: 100%;
  aspect-ratio: 16 / 10;
  border-radius: 10px;
  overflow: hidden;
  background: #120709;
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  margin-bottom: 20px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
}

.catalog-card-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  transition: transform 0.4s ease;
  display: block;
}

.catalog-card:hover .catalog-card-media img {
  transform: scale(1.04);
}

.catalog-category-tag {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(8, 5, 6, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 4px 10px;
  border-radius: 999px;
  font: 600 9px var(--mono);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--bone);
}

/* 3 Action Buttons */
.catalog-actions {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.catalog-btn {
  width: 100%;
  padding: 12px 18px;
  border-radius: 999px;
  font: 700 12px var(--disp-sans, var(--sans));
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-align: center;
  cursor: pointer;
  transition: all 0.22s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  box-sizing: border-box;
}

/* 1. Register Button: Glowing Primary Pill */
.btn-register {
  background: linear-gradient(135deg, rgba(209, 15, 32, 0.95), rgba(162, 13, 24, 0.95));
  border: 1px solid var(--crim-bright);
  color: #ffffff;
  box-shadow: 0 0 16px var(--crim-glow);
}

.btn-register:hover {
  background: linear-gradient(135deg, #e61c30, #b80f1c);
  box-shadow: 0 0 24px rgba(230, 28, 48, 0.75);
  transform: scale(1.02);
}

/* 2. Explore More Button: Sleek Pill (non-functional/dossier preview per request) */
.btn-explore {
  background: rgba(24, 6, 7, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: var(--bone);
  cursor: default;
}

.btn-explore:hover {
  background: rgba(35, 12, 15, 0.95);
  border-color: rgba(255, 255, 255, 0.35);
}

/* 3. Rulebook Button: Pill with download icon */
.btn-rulebook {
  background: #0d080a;
  border: 1px solid rgba(195, 75, 22, 0.65);
  color: var(--amber);
}

.btn-rulebook:hover {
  border-color: var(--amber);
  background: rgba(195, 75, 22, 0.2);
  color: #ff9d66;
  box-shadow: 0 0 16px var(--amber-glow);
}

@media (max-width: 680px) {
  .catalog-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
}
"""

    main_html = """
<main id="events-catalog">
  <div class="events-hero">
    <span class="eyebrow" style="color:var(--crim);">OFFICIAL FESTIVAL ARENAS</span>
    <h1 class="disp">THE ARCHIVES</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Explore all official competitive arenas, download declassified rulebooks, and secure your place on the Unstop portal.</p>
  </div>



  <!-- Search and Stats Toolbar -->
  <div class="catalog-toolbar">
    <div class="search-box-wrap">
      <span class="search-icon">🔍</span>
      <input type="text" id="catalog-search" class="search-input" placeholder="Search by event title, genre, or keyword..." aria-label="Search events" />
    </div>
    <div class="stats-badge">
      SHOWING <span id="event-count">0</span> COMPETITIVE ARENAS
    </div>
  </div>

  <!-- Catalog Cards Grid -->
  <div class="catalog-grid" id="catalog-feed" aria-live="polite"></div>
</main>
"""

    page_scripts = """
/* Master Catalog Data (Unstop Registration & Rulebooks) */
const CATALOG_DATA = [
  {
    id: "bidvertise",
    title: "Bidvertise",
    subtitle: "Advertising & Auction Warfare",
    cat: "Management",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/o/iQw0YWX?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Bidvertise Rulebook.pdf"
  },
  {
    id: "jam",
    title: "JAM (Just A Minute)",
    subtitle: "Rapid-Fire Fluency & Wit",
    cat: "Literary",
    poster: "assets/events/Rulebook_JAM_zeitgeist_26_0.png",
    unstop: "https://unstop.com/o/C4s09Pc?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Rulebook JAM zeitgeist_26.pdf"
  },
  {
    id: "xuberance",
    title: "Xuberance",
    subtitle: "Western Group Choreo Duel",
    cat: "Dance",
    poster: "assets/events/Xuberance_Rulebook_0.png",
    unstop: "https://unstop.com/o/XVWysKc?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Xuberance Rulebook.pdf"
  },
  {
    id: "swaltza",
    title: "Swaltza",
    subtitle: "Duet Dance Synchronization",
    cat: "Dance",
    poster: "assets/events/Swaltza_Rulebook_0.png",
    unstop: "https://unstop.com/o/ybdwAZ9?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Swaltza Rulebook.pdf"
  },
  {
    id: "smack-that",
    title: "Smack That",
    subtitle: "Lightning Reaction Arcade Arena",
    cat: "Informal",
    poster: "assets/events/SMACK_THAT_0.png",
    unstop: "https://unstop.com/o/TDEzHQP?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/SMACK THAT.pdf"
  },
  {
    id: "beat-down-bash",
    title: "Beat Down Bash",
    subtitle: "Street Dance & Hip-Hop Face-Off",
    cat: "Dance",
    poster: "assets/events/Beat_down_bash_rulebook_0.png",
    unstop: "https://unstop.com/o/in6wkX3?utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Beat down bash rulebook.pdf"
  },
  {
    id: "mixology",
    title: "Mixology",
    subtitle: "Beverage Craft & Mocktail Duel",
    cat: "Lifestyle",
    poster: "assets/events/MIXOLOGY_RULEBOOK_ZT_26_0.png",
    unstop: "https://unstop.com/o/cLPHny1?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/MIXOLOGY RULEBOOK ZT_26.pdf"
  },
  {
    id: "foody-frenzy",
    title: "Foody Frenzy",
    subtitle: "Speed Eating & Culinary Trial",
    cat: "Informal",
    poster: "assets/events/Foody_Frenzy_X_Inferno_Rulebook_zeitgeist_26_0.png",
    unstop: "https://unstop.com/o/rc3PwKR?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Foody Frenzy X Inferno Rulebook zeitgeist_26.pdf"
  },
  {
    id: "batter-and-brush",
    title: "Batter and Brush",
    subtitle: "Confectionery & Dessert Artistry",
    cat: "Fine Arts",
    poster: "assets/events/Batter_and_Brush_Rulebook_2_0.png",
    unstop: "https://unstop.com/o/pWXGfj0?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Batter and Brush Rulebook-2.pdf"
  },
  {
    id: "war-of-bands",
    title: "War of Bands",
    subtitle: "National Battle of the Bands",
    cat: "Music",
    poster: "assets/events/WAR_OF_BANDS_0.png",
    unstop: "https://unstop.com/o/xHYnvLd?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/WAR OF BANDS.pdf"
  },
  {
    id: "voices-unbound",
    title: "Voices Unbound",
    subtitle: "Spoken Word & Slam Poetry",
    cat: "Literary",
    poster: "assets/events/Voices_Unbound_0.png",
    unstop: "https://unstop.com/o/brgV4jZ?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Voices Unbound.pdf"
  },
  {
    id: "rap-sody",
    title: "Rap-Sody",
    subtitle: "Freestyle Cypher & Rap Battle",
    cat: "Music",
    poster: "assets/events/RapSody_0.png",
    unstop: "https://unstop.com/o/tvsy5Zu?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/RapSody.pdf"
  },
  {
    id: "beyond-words",
    title: "Beyond Words",
    subtitle: "Mime & Silent Theatre Showcase",
    cat: "Dramatics",
    poster: "assets/events/BEYOND_WORDS_0.png",
    unstop: "https://unstop.com/o/ZtEMPyQ?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/BEYOND WORDS.pdf"
  },
  {
    id: "artees",
    title: "Artees: T-shirt Painting",
    subtitle: "Wearable Fine Arts & Design",
    cat: "Fine Arts",
    poster: "assets/events/_Rulebook_Artees_zeitgeist_26_0.png",
    unstop: "https://unstop.com/p/artees-indian-institute-of-technology-iit-ropar-1768583",
    rulebook: "assets/rulebooks/_Rulebook Artees zeitgeist_26.pdf"
  },
  {
    id: "halloween-hues",
    title: "Halloween Hues",
    subtitle: "Dark Character & Canvas Duel",
    cat: "Fine Arts",
    poster: "assets/events/halloween_hues.png",
    unstop: "https://unstop.com/p/halloween-hues-indian-institute-of-technology-iit-ropar-1768585",
    rulebook: ""
  },
  {
    id: "josh-e-junta",
    title: "Josh-e-Junta",
    subtitle: "High-Voltage Nukkad Natak",
    cat: "Dramatics",
    poster: "assets/events/josh_e_junta.png",
    unstop: "https://unstop.com/p/josh-e-junta-indian-institute-of-technology-iit-ropar-1768569",
    rulebook: ""
  },
  {
    id: "bakheda",
    title: "Bakheda",
    subtitle: "Main Stage Theatrical Riot",
    cat: "Dramatics",
    poster: "assets/events/bakheda.png",
    unstop: "https://unstop.com/p/bakheda-indian-institute-of-technology-iit-ropar-1768571",
    rulebook: ""
  },
  {
    id: "unleashed-monoact",
    title: "Unleashed: Monoact",
    subtitle: "Solo Dramatic Powerhouse",
    cat: "Dramatics",
    poster: "assets/events/unleashed_monoact.png",
    unstop: "https://unstop.com/p/unleashed-monoact-indian-institute-of-technology-iit-ropar-1768573",
    rulebook: ""
  },
  {
    id: "product-pixel",
    title: "Product Pixel",
    subtitle: "Digital Design & Brand Sprint",
    cat: "Design",
    poster: "assets/events/Copy_Product_Pixel_zeitgeist_26_0.png",
    unstop: "https://unstop.com/p/product-pixel-indian-institute-of-technology-iit-ropar-1768574",
    rulebook: "assets/rulebooks/Copy Product Pixel zeitgeist_26.pdf"
  },
  {
    id: "cineclash",
    title: "CineClash",
    subtitle: "Short Film Direction & Cinematic Challenge",
    cat: "Dramatics",
    poster: "assets/events/CINECLASH_RULEBOOK_0.png",
    unstop: "https://unstop.com/p/cineclash-indian-institute-of-technology-iit-ropar-1769301",
    rulebook: "assets/rulebooks/CINECLASH RULEBOOK.pdf"
  },
  {
    id: "hidden-element",
    title: "Hidden Element",
    subtitle: "Occult Enigma & Mystery Hunt",
    cat: "Quizzing",
    poster: "assets/events/Hidden_Element_zeitgeist_26_0.png",
    unstop: "https://unstop.com/p/hidden-element-indian-institute-of-technology-iit-ropar-1768577",
    rulebook: "assets/rulebooks/Hidden Element zeitgeist_26.pdf"
  },
  {
    id: "comic-sutra",
    title: "Comic Sutra",
    subtitle: "Standup Comedy Showdown",
    cat: "Comedy",
    poster: "assets/events/comic_sutra.png",
    unstop: "https://unstop.com/o/JjTs0SO?lb=HrYUNYG7&utm_medium=Share&utm_source=events&utm_campaign=Ameykem3658",
    rulebook: ""
  },
  {
    id: "wicked-hats",
    title: "Wicked Hats-Off",
    subtitle: "Avant-Garde Millinery Runway",
    cat: "Fashion",
    poster: "assets/events/wicked_hats.png",
    unstop: "https://unstop.com/o/NRnG9Sy?lb=lBZyqh8&utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: ""
  },
  {
    id: "squid-game",
    title: "Squid Game",
    subtitle: "5 Mysterious Elimination Survival Trials",
    cat: "Informal",
    poster: "assets/events/SQUID_GAME_0.png",
    unstop: "https://unstop.com/p/squid-game-indian-institute-of-technology-iit-ropar-1769324",
    rulebook: "assets/rulebooks/SQUID GAME.pdf"
  },
  {
    id: "kavyanjali",
    title: "Kavyanjali",
    subtitle: "Live Stage Poetry Slam & Spoken Word",
    cat: "Literary",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/o/mkh52TD?lb=M3pELvx1&utm_medium=Share&utm_source=events&utm_campaign=Sakshdha26236",
    rulebook: "assets/rulebooks/Kavyanjali Rulebook.pdf"
  },
  {
    id: "hobsons-ink",
    title: "Hobson's Ink",
    subtitle: "24-Hour Narrative Storytelling Arena",
    cat: "Literary",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/o/sn8o19N?lb=M3pELvx1&utm_medium=Share&utm_source=events&utm_campaign=Sakshdha26236",
    rulebook: "assets/rulebooks/Hobsons Ink Rulebook.pdf"
  },
  {
    id: "verses-vs-verses",
    title: "Verses vs. Verses",
    subtitle: "On-Spot Thematic Poetry Duel",
    cat: "Literary",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/o/W9NHtXh?lb=M3pELvx1&utm_medium=Share&utm_source=events&utm_campaign=Sakshdha26236",
    rulebook: "assets/rulebooks/Verses vs Verses Rulebook.pdf"
  },
  {
    id: "directors-bluff",
    title: "Director's Bluff",
    subtitle: "Movie Grid, Mystery & Movie Poker",
    cat: "Dramatics",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/o/6Gk1tqp?utm_medium=Share&utm_source=zeitgrop3312&utm_campaign=Events",
    rulebook: "assets/rulebooks/Directors Bluff Rulebook.pdf"
  },
  {
    id: "one-question-after-another",
    title: "One Question After Another",
    subtitle: "Open General Quiz by Major Chandrakanth Nair",
    cat: "Quizzing",
    poster: "assets/events/Bidvertise_Rulebook_0.png",
    unstop: "https://unstop.com/p/one-question-after-another-a-general-quiz-by-major-chandrakanth-nair-zeitgeist26-moonlit-revelry-indian-institute-of-t-1770552",
    rulebook: "assets/rulebooks/One Question After Another Quiz Rulebook.pdf"
  }
];

let activeCat = "all";
let searchQuery = "";

function renderCatalog() {
  const container = document.getElementById("catalog-feed");
  const q = searchQuery.toLowerCase().trim();

  const filtered = CATALOG_DATA.filter(item => {
    if (activeCat !== "all" && item.cat !== activeCat) return false;
    if (q) {
      const matchTitle = item.title.toLowerCase().includes(q);
      const matchSub = item.subtitle.toLowerCase().includes(q);
      const matchCat = item.cat.toLowerCase().includes(q);
      if (!matchTitle && !matchSub && !matchCat) return false;
    }
    return true;
  });

  document.getElementById("event-count").textContent = filtered.length;

  if (!filtered.length) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 70px 20px; text-align: center; background: var(--surface); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px;">
        <p style="color: var(--amber); font: 700 16px var(--mono); margin-bottom: 8px;">NO ARENAS MATCHING SEARCH</p>
        <p style="color: var(--ash); font-size: 13px;">No competitive dockets match your search or category filter. Try clearing filters.</p>
      </div>`;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <article class="catalog-card" aria-label="${item.title}">
      <div class="catalog-card-header">
        <h2 class="catalog-card-title">${item.title}</h2>
        <div class="catalog-card-sub">${item.subtitle}</div>
      </div>

      <div class="catalog-card-media">
        <span class="catalog-category-tag">${item.cat}</span>
        <img src="${item.poster}" alt="${item.title}" loading="lazy" onerror="this.onerror=null; this.src='assets/logo_trans.png';" />
      </div>

      <div class="catalog-actions">
        <!-- 1. Register Button: Direct Unstop Link -->
        <a class="catalog-btn btn-register" href="${item.unstop}" target="_blank" rel="noopener noreferrer" data-c="UNSTOP">
          REGISTER NOW ↗
        </a>

        <!-- 2. Explore More: Styled Non-working Button per request -->
        <button class="catalog-btn btn-explore" type="button" onclick="handleExploreMore('${item.title}')" data-c="EXPLORE">
          EXPLORE MORE
        </button>

        <!-- 3. Rulebook Button: Direct PDF Download or View -->
        ${item.rulebook ? `
          <a class="catalog-btn btn-rulebook" href="${item.rulebook}" download="${item.title} Rulebook.pdf" target="_blank" data-c="RULEBOOK">
            RULEBOOK ⤓
          </a>
        ` : `
          <a class="catalog-btn btn-rulebook" href="${item.unstop}" target="_blank" rel="noopener noreferrer" data-c="RULEBOOK">
            RULEBOOK (ON UNSTOP) ⤓
          </a>
        `}
      </div>
    </article>
  `).join("");
}



// Search Filter
document.getElementById("catalog-search").oninput = e => {
  searchQuery = e.target.value;
  renderCatalog();
};

// Explore More Click Handler (non-working per user instructions, but provides feedback)
function handleExploreMore(title) {
  if (typeof playClick === "function") playClick(450);
  if (typeof toast === "function") {
    toast(title.toUpperCase() + ": DETAILED DOSSIER RELEASING SOON.");
  }
}

renderCatalog();
"""
    return title, description, extra_css, main_html, page_scripts
