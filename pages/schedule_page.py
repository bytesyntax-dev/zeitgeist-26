# Generator for schedule.html (The Master Festival Chronology & Venue Itinerary)

def get_schedule_content():
    title = "The Timeline — Festival Schedule | ZEITGEIST'26 | IIT Ropar"
    description = "Full three-day chronological schedule for ZEITGEIST'26 at IIT Ropar. Official timetable across Audi, Main Stage, LHC, Senate, and campus arenas."

    extra_css = """
/* Master Schedule Styles */
.schedule-hero {
  margin-bottom: 36px;
}

.schedule-hero h1 {
  font-size: clamp(34px, 6.5vw, 78px);
  margin-top: 12px;
  line-height: 1.05;
}

.day-bar {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding: 14px 0 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 28px;
  scrollbar-width: none;
}

.day-bar::-webkit-scrollbar {
  display: none;
}

.day-tab {
  padding: 14px 24px;
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.12);
  font: 600 11px var(--mono);
  letter-spacing: 0.22em;
  color: var(--ash);
  text-transform: uppercase;
  transition: all 0.25s ease;
  white-space: nowrap;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.day-tab:hover {
  color: var(--bone);
  border-color: rgba(255, 255, 255, 0.35);
  background: var(--surface-hover);
}

.day-tab.active {
  background: var(--surface);
  border-color: var(--crim);
  color: var(--bone);
  box-shadow: 0 0 20px var(--crim-glow);
}



.timeline-feed {
  display: grid;
  gap: 14px;
  margin-bottom: 80px;
  perspective: 1200px;
}

.timeline-card {
  display: grid;
  grid-template-columns: 170px 1fr auto;
  gap: 22px;
  align-items: center;
  background: #0d090b;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: clamp(16px, 2.2vw, 24px);
  position: relative;
  overflow: hidden;
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s, box-shadow 0.25s, background 0.25s;
}

.timeline-card::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--amber);
  opacity: 0.5;
  transition: opacity 0.25s, background 0.25s;
}

.timeline-card:hover {
  border-color: var(--crim);
  background: var(--surface-hover);
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7), 0 0 20px var(--crim-glow);
}

.timeline-card:hover::before {
  opacity: 1;
  background: var(--crim);
}

.timeline-card.pronite-card {
  background: linear-gradient(135deg, rgba(209, 15, 32, 0.08), #0d090b 60%);
  border-color: rgba(209, 15, 32, 0.4);
}

.timeline-card.pronite-card::before {
  background: var(--crim);
  opacity: 1;
  width: 4px;
}

.time-slot {
  font: 700 15px var(--mono);
  color: var(--amber);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.time-slot small {
  font-size: 11px;
  color: var(--ash);
  letter-spacing: 0.12em;
  font-weight: 500;
}

.timeline-info h3 {
  font: 700 clamp(17px, 2.2vw, 24px) var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 6px;
  letter-spacing: 0.03em;
  color: var(--bone);
}

.timeline-desc {
  font-size: 13px;
  color: var(--bone-dim);
  margin-bottom: 10px;
  line-height: 1.45;
}

.timeline-tags {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
}

.timeline-tag {
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 4px 10px;
  font: 500 10px var(--mono);
  letter-spacing: 0.14em;
  color: var(--ash);
  text-transform: uppercase;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.02);
}

.timeline-tag.venue {
  color: var(--bone);
  border-color: rgba(195, 75, 22, 0.45);
  background: rgba(195, 75, 22, 0.08);
}

.timeline-tag.pronite {
  border-color: var(--crim);
  color: #fff;
  background: rgba(209, 15, 32, 0.25);
  font-weight: 700;
  box-shadow: 0 0 10px rgba(209, 15, 32, 0.3);
}

.timeline-action {
  white-space: nowrap;
}

@media (max-width: 768px) {
  .timeline-card {
    grid-template-columns: 1fr;
    gap: 14px;
  }
  .timeline-action {
    display: flex;
    justify-content: flex-start;
  }
}
"""

    main_html = """
<main id="schedule">
  <div class="schedule-hero">
    <span class="eyebrow" style="color:var(--crim);">OFFICIAL TIMETABLE & SECTOR DIRECTORY</span>
    <h1 class="disp">FESTIVAL TIMELINE</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Complete hourly agenda across Audi, Main Stage, LHC, Senate, and campus sectors for October 30 – November 01, 2026.</p>
  </div>

  <!-- Day Selector Bar -->
  <div class="day-bar" role="tablist" aria-label="Select day">
    <button class="day-tab active" type="button" data-day="1" role="tab" aria-selected="true" data-c="DAY 1">DAY 01 // OCT 30 — THE AWAKENING</button>
    <button class="day-tab" type="button" data-day="2" role="tab" aria-selected="false" data-c="DAY 2">DAY 02 // OCT 31 — THE MIDNIGHT ECLIPSE</button>
    <button class="day-tab" type="button" data-day="3" role="tab" aria-selected="false" data-c="DAY 3">DAY 03 // NOV 01 — THE FINAL VERDICT</button>
  </div>

  <div class="timeline-feed" id="timeline-feed" aria-live="polite"></div>
</main>
"""

    page_scripts = """
/* Master Schedule Data (Synchronized with Official Master Grid) */
const SCHEDULE_DATA = [
  // ==========================================
  // DAY 1 — Friday, October 30, 2026
  // ==========================================
  {
    day: 1,
    time: "10:00 AM",
    end: "01:00 PM",
    title: "Story Writing",
    venue: "M5",
    cat: "Literary",
    desc: "Fiction & narrative storytelling arena under strict time limits.",
    link: "events.html"
  },
  {
    day: 1,
    time: "11:00 AM",
    end: "02:00 PM",
    title: "Director's Buffer",
    venue: "M6",
    cat: "Special Events",
    desc: "Executive briefing, stage preparation & festival operations buffer.",
    link: "events.html"
  },
  {
    day: 1,
    time: "11:00 AM",
    end: "03:00 PM",
    title: "Standup Comedy",
    venue: "Audi",
    cat: "Comedy & Dramatics",
    desc: "Solo standup performances, comedic timing trials & crowd work face-off.",
    link: "events.html"
  },
  {
    day: 1,
    time: "11:00 AM",
    end: "03:00 PM",
    title: "Squid Game",
    venue: "Rose Garden",
    cat: "Informal & Fun",
    desc: "Survival knockout trials, psychological campus games & bounty challenge.",
    link: "events.html"
  },
  {
    day: 1,
    time: "01:00 PM",
    end: "05:00 PM",
    title: "Bidvertise",
    venue: "M5",
    cat: "Management & Media",
    desc: "Commercial pitch creation, marketing warfare & live auction bidding.",
    link: "events.html"
  },
  {
    day: 1,
    time: "03:00 PM",
    end: "06:00 PM",
    title: "Arteez",
    venue: "M4",
    cat: "Fine Arts",
    desc: "Live design duel, rapid sketching & creative fine arts showdown.",
    link: "events.html"
  },
  {
    day: 1,
    time: "03:00 PM",
    end: "07:00 PM",
    title: "Director's Buffer",
    venue: "Senate",
    cat: "Special Events",
    desc: "VIP contingent reception, festival dossier audits & production reserve.",
    link: "events.html"
  },
  {
    day: 1,
    time: "04:00 PM",
    end: "07:00 PM",
    title: "Swaltza",
    venue: "Audi",
    cat: "Dance",
    desc: "Competitive dance showcase featuring western synchrony & dynamic movement.",
    link: "events.html"
  },
  {
    day: 1,
    time: "04:00 PM",
    end: "07:00 PM",
    title: "Street Play (Nukkad Natak)",
    venue: "Rose Garden",
    cat: "Dramatics",
    desc: "High-octane open-air theatre, rhythmic percussion & social commentary.",
    link: "events.html"
  },
  {
    day: 1,
    time: "08:00 PM",
    end: "11:30 PM",
    title: "NIGHT 01 PRONITE // NIRVANA'S ECLIPSE (Rock & Metal)",
    venue: "Main Stage",
    cat: "Pronite",
    desc: "The festival unchains with headlining rock fury, distorted riffs, and thunderous metal.",
    link: "pronites.html",
    isPronite: true
  },

  // ==========================================
  // DAY 2 — Saturday, October 31, 2026
  // ==========================================
  {
    day: 2,
    time: "09:00 AM",
    end: "12:00 PM",
    title: "Foody Frenzy",
    venue: "Foyer",
    cat: "Informal & Fun",
    desc: "Fast-paced gastronomic challenges, culinary tastings & food trials.",
    link: "events.html"
  },
  {
    day: 2,
    time: "09:00 AM",
    end: "06:00 PM",
    title: "MUN (Model United Nations) — Day 1",
    venue: "Senate",
    cat: "Literary & Debating",
    desc: "Diplomatic committee sessions, international resolution drafting & caucusing.",
    link: "events.html"
  },
  {
    day: 2,
    time: "10:00 AM",
    end: "12:00 PM",
    title: "APD (Asian Parliamentary Debate)",
    venue: "M6",
    cat: "Literary & Debating",
    desc: "3v3 parliamentary clash debating high-stakes motions under adjudicator scrutiny.",
    link: "events.html"
  },
  {
    day: 2,
    time: "10:00 AM",
    end: "02:00 PM",
    title: "Xuberance",
    venue: "Audi",
    cat: "Dance",
    desc: "Flagship western group choreo competition with cinematic formations & rhythm.",
    link: "events.html"
  },
  {
    day: 2,
    time: "10:00 AM",
    end: "05:00 PM",
    title: "War of Bands",
    venue: "Main Stage",
    cat: "Music",
    desc: "The monumental collegiate battle of guitar solos, drum assaults & original rock sets.",
    link: "events.html"
  },
  {
    day: 2,
    time: "12:00 PM",
    end: "02:00 PM",
    title: "Film-Making Showcase",
    venue: "M5",
    cat: "Cinematics",
    desc: "48-hour short film screenings, gothic cinematography & director QA.",
    link: "events.html"
  },
  {
    day: 2,
    time: "12:00 PM",
    end: "07:00 PM",
    title: "One Question After Another",
    venue: "TBA",
    cat: "Quizzing",
    desc: "An open general quiz by Chandrakanth Nair.",
    link: "events.html"
  },
  {
    day: 2,
    time: "01:00 PM",
    end: "04:00 PM",
    title: "Batter and Brush",
    venue: "Council Room",
    cat: "Fine Arts",
    desc: "Creative dessert sculpting, edible painting duel & confectionery art.",
    link: "events.html"
  },
  {
    day: 2,
    time: "01:00 PM",
    end: "05:00 PM",
    title: "JAM (Just A Minute) — Arena 1",
    venue: "M3",
    cat: "Literary",
    desc: "60 seconds of uninterrupted English fluency without hesitation, repetition, or deviation.",
    link: "events.html"
  },
  {
    day: 2,
    time: "01:00 PM",
    end: "07:00 PM",
    title: "JAM (Just A Minute) — Arena 2",
    venue: "M4",
    cat: "Literary",
    desc: "High-octane knockout bracket for rapid-fire speaking mastery.",
    link: "events.html"
  },
  {
    day: 2,
    time: "01:00 PM",
    end: "06:00 PM",
    title: "Face Painting",
    venue: "Rose Garden",
    cat: "Fine Arts",
    desc: "Character transformation, theatrical prosthetic brushwork & dark fantasy art.",
    link: "events.html"
  },
  {
    day: 2,
    time: "02:00 PM",
    end: "05:00 PM",
    title: "Monoact",
    venue: "Audi",
    cat: "Dramatics",
    desc: "Solo theatrical brilliance commanding the auditorium stage with raw emotional power.",
    link: "events.html"
  },
  {
    day: 2,
    time: "03:00 PM",
    end: "06:00 PM",
    title: "Poetry Slam",
    venue: "M5",
    cat: "Literary",
    desc: "Spoken word verses, rhythm-infused poetry & heartfelt emotional cadence.",
    link: "events.html"
  },
  {
    day: 2,
    time: "04:00 PM",
    end: "07:00 PM",
    title: "Improv",
    venue: "M6",
    cat: "Comedy & Dramatics",
    desc: "Unscripted improvisational scenes, quick wit games & live audience prompts.",
    link: "events.html"
  },
  {
    day: 2,
    time: "04:00 PM",
    end: "07:00 PM",
    title: "Smack-That",
    venue: "Mocha",
    cat: "Informal & Fun",
    desc: "Reflex arcade duel testing lightning speed and high-adrenaline reaction times.",
    link: "events.html"
  },
  {
    day: 2,
    time: "05:00 PM",
    end: "07:00 PM",
    title: "Solo Instrumental",
    venue: "CY",
    cat: "Music",
    desc: "Acoustic, classical & electric instrumental virtuosity in the central courtyard.",
    link: "events.html"
  },
  {
    day: 2,
    time: "08:30 PM",
    end: "01:00 AM",
    title: "NIGHT 02 PRONITE // THE PHANTOM RAVE (EDM & Bass)",
    venue: "Main Stage",
    cat: "Pronite",
    desc: "An all-out electronic dance spectacle with laser light projections and world-class DJ sets.",
    link: "pronites.html",
    isPronite: true
  },

  // ==========================================
  // DAY 3 — Sunday, November 01, 2026
  // ==========================================
  {
    day: 3,
    time: "09:00 AM",
    end: "12:00 PM",
    title: "Mixology",
    venue: "Foyer",
    cat: "Lifestyle & Workshop",
    desc: "Art of beverage blending, aromatic mocktail crafts & presentation masterclass.",
    link: "events.html"
  },
  {
    day: 3,
    time: "09:00 AM",
    end: "06:00 PM",
    title: "MUN (Model United Nations) — Day 2",
    venue: "Senate",
    cat: "Literary & Debating",
    desc: "Final crisis sessions, international voting procedures & valedictory diplomacy awards.",
    link: "events.html"
  },
  {
    day: 3,
    time: "10:00 AM",
    end: "04:00 PM",
    title: "Mr & Mrs Zeitgeist",
    venue: "Audi",
    cat: "Fashion & Personality",
    desc: "The festival's signature personality pageant celebrating charisma, runway elegance & poise.",
    link: "events.html"
  },
  {
    day: 3,
    time: "11:00 AM",
    end: "02:00 PM",
    title: "Wicked Hats-Off",
    venue: "LHC Open",
    cat: "Fashion & Creative",
    desc: "Avant-garde millinery crafting, headwear fashioning & open-air runway display.",
    link: "events.html"
  },
  {
    day: 3,
    time: "03:00 PM",
    end: "06:00 PM",
    title: "Solo / Duet Singing",
    venue: "M5",
    cat: "Music",
    desc: "Eastern and western vocal competition celebrating pure acoustic melody and vocal range.",
    link: "events.html"
  },
  {
    day: 3,
    time: "04:00 PM",
    end: "07:00 PM",
    title: "Lashkara",
    venue: "Audi",
    cat: "Dance & Culture",
    desc: "Vibrant Bhangra beats, energetic folk choreography & celebratory cultural spirit.",
    link: "events.html"
  },
  {
    day: 3,
    time: "06:00 PM",
    end: "08:00 PM",
    title: "Rapsody",
    venue: "Garden",
    cat: "Music",
    desc: "Hip-hop cypher, freestyle rhyme battles & lyrical rap showdown under the stars.",
    link: "events.html"
  },
  {
    day: 3,
    time: "07:00 PM",
    end: "08:00 PM",
    title: "Grand Valedictory Ceremony & Trophies",
    venue: "Audi",
    cat: "Ceremony",
    desc: "Official festival culmination, overall championship trophy awards & grand closing address.",
    link: "events.html"
  },
  {
    day: 3,
    time: "08:00 PM",
    end: "11:30 PM",
    title: "NIGHT 03 PRONITE // SYMPHONY OF SOULS (Bollywood Star Finale)",
    venue: "Main Stage",
    cat: "Pronite",
    desc: "The grand cinematic climax featuring celebrated Bollywood playback sensations and anthemic melodies.",
    link: "pronites.html",
    isPronite: true
  }
];

let activeDay = 1;

function renderSchedule() {
  const container = document.getElementById("timeline-feed");
  const filtered = SCHEDULE_DATA.filter(item => item.day === activeDay);

  if (!filtered.length) {
    container.innerHTML = `
      <div style="padding:60px 20px; text-align:center; background:var(--surface); border:1px solid rgba(255,255,255,0.08);">
        <p style="color:var(--amber); font:700 16px var(--mono); margin-bottom:8px;">NO SCHEDULED EVENTS FOUND</p>
        <p style="color:var(--ash); font-size:13px;">No rites found for Day 0${activeDay}.</p>
      </div>`;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <article class="timeline-card ${item.isPronite ? 'pronite-card' : ''}" aria-label="${item.title}">
      <div class="time-slot">
        <span>${item.time}</span>
        <small>UNTIL ${item.end}</small>
      </div>
      <div class="timeline-info">
        <h3>${item.title}</h3>
        ${item.desc ? `<p class="timeline-desc">${item.desc}</p>` : ''}
        <div class="timeline-tags">
          <span class="timeline-tag venue">📍 ${item.venue}</span>
          <span class="timeline-tag ${item.isPronite ? 'pronite' : ''}">${item.cat}</span>
        </div>
      </div>
      <div class="timeline-action">
        <a class="btn-mini" href="${item.link}" data-c="DOSSIER">
          ${item.isPronite ? 'VIEW LINEUP →' : 'INSPECT DOSSIER →'}
        </a>
      </div>
    </article>
  `).join("");
}

// Day Tab switching
document.querySelectorAll(".day-tab").forEach(tab => {
  tab.onclick = () => {
    document.querySelectorAll(".day-tab").forEach(t => {
      t.classList.remove("active");
      t.setAttribute("aria-selected", "false");
    });
    tab.classList.add("active");
    tab.setAttribute("aria-selected", "true");
    activeDay = parseInt(tab.dataset.day, 10);
    if (typeof playClick === "function") playClick(600);
    renderSchedule();
  };
});

renderSchedule();
"""
    return title, description, extra_css, main_html, page_scripts
