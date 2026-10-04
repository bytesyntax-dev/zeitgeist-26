# ZEITGEIST'26 — Website Developer & Expansion Guide

Welcome to the **ZEITGEIST'26** website codebase. This guide explains how the website is architected, how to edit existing festival details (events, schedule, passes, pronites, team, sponsors), and how to add brand new pages.

---

## 1. Architecture Overview

This project uses a **modular Python-driven static compilation system**:
* **High Performance**: Compiles to 100% pure, lightweight HTML, CSS, and Vanilla JavaScript with zero runtime framework overhead.
* **Single Source of Truth**: Global layout, navigation bars, mobile drawers, audio engines, footers, and horror design tokens are managed centrally.
* **Instant Compilation**: Running a single command rebuilds all 10 festival pages in under 1 second.

### Directory Structure

```text
ZT/
├── build_site.py           # Master compiler & shared shell (nav, footer, audio, CSS tokens)
├── build_homepage.py       # Homepage builder (3D hero, horror lore, audio synthesis)
├── pages/                  # Modular content generators for each subpage
│   ├── about_page.py       # Lore, festival dossier & history
│   ├── contact_page.py     # Emergency desk, faculty liaisons & sector map
│   ├── events_page.py      # The Archives (60+ competitive arenas, modal rulebooks)
│   ├── gallery_page.py     # Recovered 1986 polaroids & archive photos
│   ├── passes_page.py      # Clearance passes, pricing tiers & accommodation
│   ├── pronites_page.py    # Midnight star lineup, stage gates & artist cards
│   ├── schedule_page.py    # Full 3-day chronological festival schedule
│   ├── sponsors_page.py    # Corporate partners & title benefactors
│   └── team_page.py        # Student coordinators & department council
├── assets/                 # Logos, stage photos, audio textures, and icons
├── *.html                  # Compiled production files (index, events, schedule, etc.)
└── WEBSITE_GUIDE.md        # This guide
```

---

## 2. The Golden Rule of Development

> [!IMPORTANT]
> **NEVER edit the `.html` files directly.**
>
> The HTML files (`index.html`, `events.html`, `schedule.html`, etc.) are automatically compiled artifacts. If you edit them directly, your changes will be overwritten the next time the build script runs.
>
> **Always edit the source files:**
> 1. Make your changes in `pages/*.py`, `build_site.py`, or `build_homepage.py`.
> 2. Compile the site:
>    ```bash
>    python3 build_site.py
>    ```
> 3. Refresh your browser at `http://localhost:8000` to see your changes.

---

## 3. How to Edit Existing Details

Each page's content lives in its own file inside the `pages/` directory.

### A. Updating Events & Rulebooks (`pages/events_page.py`)
Events are defined in the JavaScript `EVENTS` array inside `pages/events_page.py`:

```javascript
{
  id: "synchronize",
  name: "Synchronize: Western Group Dance",
  cat: "Dance",
  type: "Team (8-25)",
  prize: "₹45,000",
  date: "Day 02 • Nov 01",
  time: "14:00 - 18:30 IST",
  venue: "Main Amphitheatre",
  fee: "₹800 / crew",
  reg_link: "https://forms.gle/your-form-link",
  rulebook_link: "assets/rulebooks/synchronize.pdf",
  desc: "The flagship collegiate crew battle. High-octane choreography...",
  rules: [
    "Time limit: 8-12 minutes inclusive of stage setup.",
    "Soundtrack must be submitted 2 hours prior on USB drives."
  ],
  contacts: [
    { name: "Aarav Sharma", phone: "+91 98765 43210" }
  ]
}
```
* **To add an event:** Add a new JSON object into the `EVENTS` array.
* **To change categories:** Update the `CATS` array at the top of the script.
* **To update registration links or prize pools:** Change `reg_link` or `prize`.

---

### B. Updating Schedule & Timelines (`pages/schedule_page.py`)
Open `pages/schedule_page.py` and navigate to the timeline blocks:

```html
<div class="timeline-slot" data-day="day1">
  <div class="slot-time">18:00 — 21:00</div>
  <div class="slot-details">
    <div class="slot-badge badge-music">PRO-STAGE</div>
    <h3 class="slot-title">Battle of the Bands: Prelims</h3>
    <p class="slot-desc">12 collegiate rock and metal bands duel for the grand stage finals.</p>
    <div class="slot-meta">📍 Open Air Theatre • Open to all Pass Holders</div>
  </div>
</div>
```
* Change `data-day` to `"day1"`, `"day2"`, or `"day3"`.
* Update time, title, description, and location metadata as required.

---

### C. Updating Star Pronites & Artists (`pages/pronites_page.py`)
In `pages/pronites_page.py`, each pronite night is defined in an artist card:

```html
<div class="pronite-card" data-night="night1">
  <div class="pronite-date">OCTOBER 30 • NIGHT 01</div>
  <h2 class="pronite-artist">THE HEADLINING BAND</h2>
  <span class="pronite-genre">SYMPHONIC ROCK / EXORCISM</span>
  <p class="pronite-bio">Short bio and lore about the performing artist...</p>
  <div class="pronite-gate">GATE CLEARANCE: PASS REQUIRED • 19:00 IST</div>
</div>
```

---

### D. Updating Passes & Accommodation Pricing (`pages/passes_page.py`)
In `pages/passes_page.py`, edit the pricing cards:

```html
<div class="pass-card featured">
  <div class="pass-tier">ALL-ACCESS VIP CLEARANCE</div>
  <div class="pass-price">₹1,499 <span>/ FESTIVAL</span></div>
  <ul class="pass-perks">
    <li>Entry to all 3 Star Pronite Nights (Front Stage Pit)</li>
    <li>Free entry to participate in all 60+ competitive arenas</li>
    <li>Official Festival Merchandise Kit & RFID Wristband</li>
  </ul>
  <a class="btn btn-crim" href="https://rzp.io/l/your-link" target="_blank">ACQUIRE PASS →</a>
</div>
```

---

### E. Updating Organizing Team & Council (`pages/team_page.py`)
In `pages/team_page.py`, cards are grouped by department:

```html
<div class="council-card" data-category="convenors">
  <div class="avatar-frame">AS</div>
  <div class="member-role">Festival Chief Convenor</div>
  <div class="member-name">Aarav Sharma</div>
  <div class="member-dept">Overall Management & Rites</div>
  <div class="contact-links">
    <a class="contact-line" href="tel:+919876543210">📞 +91 98765 43210</a>
    <a class="contact-line" href="mailto:convenor.zeitgeist@iitrpr.ac.in">✉ convenor.zeitgeist@iitrpr.ac.in</a>
  </div>
</div>
```
* Use `data-category` matching the filter chips (`"convenors"`, `"events"`, `"pronites"`, `"sponsorship"`, `"media"`).

---

### F. Updating Sponsors & Partners (`pages/sponsors_page.py`)
In `pages/sponsors_page.py`, sponsors are arranged by tiers (`Title Sponsor`, `Associate Sponsors`, `Media Partners`, etc.):

```html
<div class="sponsor-card">
  <img class="sponsor-logo" src="assets/sponsors/sponsor_name.png" alt="Company Name">
  <div class="sponsor-tier-tag">CO-POWERED BY</div>
  <h4 class="sponsor-name">Company Name</h4>
  <p class="sponsor-caption">Official Cloud & Compute Partner</p>
</div>
```

---

### G. Updating the Homepage (`build_homepage.py`)
`build_homepage.py` generates the immersive landing page (`index.html`).
* **Hero Text & Catchphrase**: Search for `hero-title` or `hero-sub` to adjust slogans.
* **Highlights / Quick Stats**: Search for `stat-item` to adjust footfall numbers, prize total, etc.
* **Interactive 3D Stages**: Ambient lighting, pumpkin candle toggles, and audio synthesis are managed at the bottom of the script.

---

## 4. How to Add a Brand New Page

Want to add a new page (e.g. `workshops.html`)? Follow this 3-step recipe:

### Step 1: Create `pages/workshops_page.py`
Create a new file in `pages/` following this template:

```python
# Generator for workshops.html (Workshops & Masterclasses)

def get_workshops_content():
    title = "Workshops & Masterclasses | ZEITGEIST'26 | IIT Ropar"
    description = "Hands-on creative and technical masterclasses conducted by industry veterans at ZEITGEIST'26."

    extra_css = """
    .workshops-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 28px;
      margin-top: 40px;
    }
    .workshop-card {
      background: var(--surface);
      border: 1px solid rgba(255,255,255,0.1);
      padding: 32px;
      position: relative;
    }
    """

    main_html = """
    <main class="page-container" style="padding-top:120px;">
      <div class="section-hdr">
        <span class="eyebrow">ACADEMIA OF THE UNKNOWN</span>
        <h1 class="disp">MASTERCLASSES</h1>
        <p class="sub">Intensive creative workshops led by visionary creators.</p>
      </div>

      <div class="workshops-grid">
        <div class="workshop-card">
          <span class="badge">CINEMATOGRAPHY</span>
          <h3>Gothic Filmmaking & Low-Light Lighting</h3>
          <p>Learn shadow framing and eerie visual composition.</p>
          <a class="btn" href="#">Reserve Seat →</a>
        </div>
      </div>
    </main>
    """

    page_scripts = """
    // Optional page-specific JS logic
    """

    return title, description, extra_css, main_html, page_scripts
```

### Step 2: Register in `build_site.py`
Open `build_site.py`:

1. **Import your new generator:**
   ```python
   from pages.workshops_page import get_workshops_content
   ```

2. **Add to Navigation in `generate_shell()` (around line 1140):**
   ```python
   pages = [
       ("index.html", "Home", "HOME"),
       ("about.html", "About", "ABOUT"),
       ("events.html", "Events", "EVENTS"),
       ("workshops.html", "Workshops", "WORKSHOPS"), # <--- ADD HERE
       ("pronites.html", "Pronites", "PRONITES"),
       ...
   ]
   ```

3. **Add to `subpages` list in `build_all()` (around line 1765):**
   ```python
   subpages = [
       ("about.html", get_about_content),
       ("events.html", get_events_content),
       ("workshops.html", get_workshops_content), # <--- ADD HERE
       ("pronites.html", get_pronites_content),
       ...
   ]
   ```

### Step 3: Compile
Run:
```bash
python3 build_site.py
```
`workshops.html` will be generated with full navigation, defense scripts, audio toggle, and footer!

---

## 5. Global Design System & Styling Guide

The site's visual identity is built on a dark Gothic / Horror theme with neon-accented rituals.

### Color Tokens (defined in `build_site.py`)
Use these CSS variables in any component:
* `var(--void)`: `#040304` (deep obsidian black background)
* `var(--surface)`: `#141113` (card background)
* `var(--surface-hover)`: `#1c171b` (interactive card hover state)
* `var(--bone)`: `#e2dbce` (primary parchment text)
* `var(--bone-dim)`: `#9e978c` (secondary text)
* `var(--ash)`: `#736f68` (muted labels & borders)
* `var(--crim)`: `#941722` (primary brand blood red)
* `var(--crim-bright)`: `#e61c30` (active glow red)
* `var(--amber)`: `#ad5f26` (sub-accent amber / lantern glow)

### Typography
* `var(--disp-sans)`: `"Syncopate", sans-serif` (headers, badges, festival name)
* `var(--serif)`: `"Cormorant Garamond", Georgia, serif` (lore text, quotes)
* `var(--mono)`: `"JetBrains Mono", monospace` (timestamps, telemetry, buttons)

### Built-In CSS Utility Classes
* `.btn` — Standard boxed Gothic button with hover fill transition.
* `.btn-crim` — Highlighted crimson button with red glow.
* `.eyebrow` — Small uppercase tracking sub-header.
* `.disp` — Large Syncopate display heading.
* `.chip` — Category pill filter button.

---

## 6. Commands Reference

| Action | Terminal Command |
| :--- | :--- |
| **Recompile All Pages** | `python3 build_site.py` |
| **Start Local Web Server** | `python3 -m http.server 8000` |
| **Open Site in Browser** | `open http://localhost:8000` |
| **Stop Local Web Server** | Press `Ctrl + C` in the running terminal |
