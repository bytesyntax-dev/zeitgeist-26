# Generator for schedule.html (The Timeline - 3-Day Chronological Itinerary)

def get_schedule_content():
    title = "The Timeline — Festival Schedule | ZEITGEIST'26 | IIT Ropar"
    description = "Full three-day chronological schedule for ZEITGEIST'26 at IIT Ropar. Master timeline for competitive arenas and midnight star pronites."

    extra_css = """
/* Schedule Styles */
.schedule-hero {
  margin-bottom: 40px;
}

.schedule-hero h1 {
  font-size: clamp(36px, 7vw, 84px);
  margin-top: 14px;
}

.day-bar {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding: 16px 0 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 30px;
}

.day-tab {
  padding: 14px 24px;
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.12);
  font: 500 11px var(--mono);
  letter-spacing: 0.25em;
  color: var(--ash);
  text-transform: uppercase;
  transition: all 0.3s;
  white-space: nowrap;
}

.day-tab:hover {
  color: var(--bone);
  border-color: rgba(255, 255, 255, 0.3);
}

.day-tab.active {
  background: var(--surface);
  border-color: var(--crim);
  color: var(--bone);
  box-shadow: 0 0 16px var(--crim-glow);
}

.filter-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 36px;
}

.filter-select {
  background: var(--char);
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 10px 20px;
  color: var(--bone);
  font: 400 12px var(--mono);
}

.timeline-feed {
  display: grid;
  gap: 16px;
  margin-bottom: 80px;
  perspective: 1200px;
}

.timeline-card {
  display: grid;
  grid-template-columns: 160px 1fr auto;
  gap: 24px;
  align-items: center;
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: clamp(18px, 2.5vw, 26px);
  transform-style: preserve-3d;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s, box-shadow 0.3s;
}

.timeline-card:hover {
  border-color: var(--crim);
  background: var(--surface);
  transform: perspective(900px) translateZ(16px) rotateX(-1.5deg) translateX(8px);
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.8), 0 0 25px var(--crim-glow);
}

.time-slot {
  font: 700 16px var(--mono);
  color: var(--amber);
  display: flex;
  flex-direction: column;
  gap: 4px;
  transform: translateZ(20px);
}

.time-slot small {
  font-size: 10px;
  color: var(--ash);
  letter-spacing: 0.15em;
  font-weight: 500;
}

.timeline-info h3 {
  font: 700 clamp(16px, 2vw, 22px) var(--disp-sans);
  text-transform: uppercase;
  margin-bottom: 6px;
  transform: translateZ(24px);
}

.timeline-tags {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
  transform: translateZ(16px);
}

.timeline-action {
  white-space: nowrap;
  transform: translateZ(24px);
}

.timeline-tag {
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 4px 8px;
  font: 500 9px var(--mono);
  letter-spacing: 0.18em;
  color: var(--ash);
  text-transform: uppercase;
}

.timeline-tag.venue {
  color: var(--bone-dim);
  border-color: rgba(255, 255, 255, 0.2);
}

.timeline-tag.pronite {
  border-color: var(--crim);
  color: var(--crim-bright);
}

.timeline-action {
  white-space: nowrap;
}

@media (max-width: 768px) {
  .timeline-card {
    grid-template-columns: 1fr;
    gap: 14px;
  }
}
"""

    main_html = """
<main id="schedule">
  <div class="schedule-hero">
    <span class="eyebrow" style="color:var(--crim);">MASTER FESTIVAL CHRONOLOGY</span>
    <h1 class="disp">THE TIMELINE</h1>
    <p class="eyebrow" style="margin-top:12px; color:var(--bone-dim);">Complete hourly agenda across all sectors and stages for October 30 – November 01, 2026.</p>
  </div>

  <!-- Day Selector Bar -->
  <div class="day-bar" role="tablist" aria-label="Select day">
    <button class="day-tab active" type="button" data-day="1" role="tab" aria-selected="true" data-c="DAY 1">DAY 01 // OCT 30 — THE AWAKENING</button>
    <button class="day-tab" type="button" data-day="2" role="tab" aria-selected="false" data-c="DAY 2">DAY 02 // OCT 31 — THE MIDNIGHT ECLIPSE</button>
    <button class="day-tab" type="button" data-day="3" role="tab" aria-selected="false" data-c="DAY 3">DAY 03 // NOV 01 — THE FINAL VERDICT</button>
  </div>

  <!-- Filter & Action Controls -->
  <div class="filter-row">
    <div>
      <select class="filter-select" id="venue-filter" aria-label="Filter by sector">
        <option value="">All Campus Sectors</option>
        <option value="Senate Amphitheatre">Sector 02 // Senate Amphitheatre</option>
        <option value="Open Air Theatre">Sector 03 // Open Air Amphitheatre</option>
        <option value="Student Activity Centre">Sector 05 // Student Activity Centre</option>
        <option value="Sports Grounds">Sector 01 // Sports Arena Grounds</option>
        <option value="Lecture Complex">Sector 04 // Lecture Complex</option>
        <option value="Central Library Lawn">Sector 04 // Library Lawn</option>
      </select>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="btn-mini" type="button" id="print-schedule-btn" data-c="PRINT">🖶 PRINT ITINERARY</button>
      <button class="btn-mini" type="button" id="export-cal-btn" data-c="CALENDAR">📅 EXPORT .ICS CALENDAR</button>
    </div>
  </div>

  <div class="timeline-feed" id="timeline-feed" aria-live="polite"></div>
</main>
"""

    page_scripts = """
/* Schedule Data & Interactive Filtering */
const SCHEDULE_DATA = [
  // Day 1
  { day: 1, time: "09:30 AM", end: "11:00 AM", title: "Contingent Reporting & Security Dossier Verification", venue: "Sports Grounds", cat: "Protocol", link: "contact.html#sectors" },
  { day: 1, time: "11:00 AM", end: "02:30 PM", title: "Sonic Exorcism // Battle of the Bands (Prelims)", venue: "Senate Amphitheatre", cat: "Music", link: "events.html#/event/evt-001" },
  { day: 1, time: "01:30 PM", end: "04:30 PM", title: "Shadows of the Street // Nukkad Natak", venue: "Central Library Lawn", cat: "Dramatics", link: "events.html#/event/evt-003" },
  { day: 1, time: "03:00 PM", end: "07:00 PM", title: "Purgatory LAN // Valorant & CS2 Arena (Day 1)", venue: "Student Activity Centre", cat: "Gaming", link: "events.html#/event/evt-009" },
  { day: 1, time: "05:00 PM", end: "07:00 PM", title: "The Lost Manuscript // Slam Poetry Slam", venue: "Lecture Complex", cat: "Literary", link: "events.html#/event/evt-005" },
  { day: 1, time: "07:30 PM", end: "11:00 PM", title: "NIGHT 01 PRONITE // NIRVANA'S ECLIPSE (Rock & Metal)", venue: "Open Air Theatre", cat: "Pronite", link: "pronites.html", isPronite: true },

  // Day 2
  { day: 2, time: "10:00 AM", end: "01:00 PM", title: "48-Hour Midnight Film // Reel of Horrors Screening", venue: "Lecture Complex", cat: "Cinematics", link: "events.html#/event/evt-007" },
  { day: 2, time: "11:30 AM", end: "03:00 PM", title: "The Danse Macabre // Western Choreo Competition", venue: "Senate Amphitheatre", cat: "Dance", link: "events.html#/event/evt-002" },
  { day: 2, time: "02:00 PM", end: "05:00 PM", title: "Canvas of Ashes // Live Charcoal Arts Duel", venue: "Student Activity Centre", cat: "Fine Arts", link: "events.html#/event/evt-006" },
  { day: 2, time: "04:30 PM", end: "07:30 PM", title: "Haute Occult // The Midnight Pageant (Fashion)", venue: "Senate Amphitheatre", cat: "Fashion", link: "events.html#/event/evt-004" },
  { day: 2, time: "08:30 PM", end: "01:00 AM", title: "NIGHT 02 PRONITE // THE PHANTOM RAVE (EDM & Bass)", venue: "Sports Grounds", cat: "Pronite", link: "pronites.html", isPronite: true },

  // Day 3
  { day: 3, time: "10:30 AM", end: "01:30 PM", title: "Occult Lore & Enigma // General Quiz Finals", venue: "Lecture Complex", cat: "Quizzing", link: "events.html#/event/evt-008" },
  { day: 3, time: "01:00 PM", end: "03:30 PM", title: "The Alchemist's Trial // Science Mystery Challenge", venue: "Senate Amphitheatre", cat: "Special Events", link: "events.html#/event/evt-010" },
  { day: 3, time: "03:30 PM", end: "05:30 PM", title: "Rhapsody in Blood // Solo Eastern Vocals", venue: "Open Air Theatre", cat: "Music", link: "events.html#/event/evt-011" },
  { day: 3, time: "05:00 PM", end: "07:00 PM", title: "The Final Masquerade // Mono Act Showcase", venue: "Senate Amphitheatre", cat: "Dramatics", link: "events.html#/event/evt-012" },
  { day: 3, time: "07:00 PM", end: "08:00 PM", title: "Grand Valedictory Ceremony & Bounty Distribution", venue: "Senate Amphitheatre", cat: "Ceremony", link: "events.html" },
  { day: 3, time: "08:00 PM", end: "11:30 PM", title: "NIGHT 03 PRONITE // SYMPHONY OF SOULS (Bollywood Finale)", venue: "Sports Grounds", cat: "Pronite", link: "pronites.html", isPronite: true }
];

let activeDay = 1;
let activeVenue = "";

function renderSchedule() {
  const container = document.getElementById("timeline-feed");
  const filtered = SCHEDULE_DATA.filter(item => item.day === activeDay && (!activeVenue || item.venue === activeVenue));

  if (!filtered.length) {
    container.innerHTML = `<div style="padding:60px 20px; text-align:center; color:var(--ash);">No scheduled rites match this venue filter for Day 0${activeDay}.</div>`;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <article class="timeline-card" aria-label="${item.title}">
      <div class="time-slot">
        <span>${item.time}</span>
        <small>UNTIL ${item.end}</small>
      </div>
      <div class="timeline-info">
        <h3>${item.title}</h3>
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

document.querySelectorAll(".day-tab").forEach(tab => {
  tab.onclick = () => {
    document.querySelectorAll(".day-tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");
    activeDay = parseInt(tab.dataset.day, 10);
    playClick(600);
    renderSchedule();
  };
});

document.getElementById("venue-filter").onchange = e => {
  activeVenue = e.target.value;
  playClick(500);
  renderSchedule();
};

document.getElementById("print-schedule-btn").onclick = () => {
  playClick(500);
  window.print();
};

// Export .ics Calendar
document.getElementById("export-cal-btn").onclick = () => {
  playClick(700);
  const icsLines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//ZEITGEIST Cultural Council//IIT Ropar//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:ZEITGEIST 2026 Festival Schedule",
    "X-WR-TIMEZONE:Asia/Kolkata"
  ];

  SCHEDULE_DATA.forEach((ev, idx) => {
    const dayStr = ev.day === 1 ? "20261030" : (ev.day === 2 ? "20261031" : "20261101");
    icsLines.push("BEGIN:VEVENT");
    icsLines.push(`UID:zg26-sched-${idx}@zeitgeist.iitrpr.ac.in`);
    icsLines.push(`DTSTAMP:20261001T000000Z`);
    icsLines.push(`DTSTART;TZID=Asia/Kolkata:${dayStr}T100000`);
    icsLines.push(`DTEND;TZID=Asia/Kolkata:${dayStr}T220000`);
    icsLines.push(`SUMMARY:${ev.title}`);
    icsLines.push(`LOCATION:${ev.venue}, IIT Ropar, Rupnagar, Punjab`);
    icsLines.push(`DESCRIPTION:ZEITGEIST 2026 Festival Event // Category: ${ev.cat}`);
    icsLines.push("END:VEVENT");
  });

  icsLines.push("END:VCALENDAR");

  const blob = new Blob([icsLines.join("\\r\\n")], { type: "text/calendar;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "zeitgeist26_schedule.ics";
  a.click();
  URL.revokeObjectURL(url);
  toast("MASTER CALENDAR (.ICS) EXPORTED.");
};

renderSchedule();
"""
    return title, description, extra_css, main_html, page_scripts
