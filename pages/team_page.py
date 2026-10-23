# Generator for team.html (The Council - Overall Coordinators & Department Heads)
#
# The roster is rendered at build time from assets/team/team.json (single source
# of truth). To change a name, role or photo, edit that JSON / the photo files
# and rebuild with `python3 build_site.py`.

import html
import json
import os

TEAM_JSON = os.path.join(os.path.dirname(__file__), "..", "assets", "team", "team.json")

OC_TEAM_ID = "overall-coordinators"

# Short codes shown on each card's badge ("WEB // 02"), keyed by team id.
TEAM_CODES = {
    "overall-coordinators": "OC",
    "content-and-anchoring": "CNT",
    "finance": "FIN",
    "sponsorship": "SPN",
    "event-management": "EVM",
    "decoration": "DEC",
    "graphic-design": "GFX",
    "web-development": "WEB",
    "security": "SEC",
    "social-media-and-coverage": "SMC",
    "pronite": "PRN",
    "media-and-publicity": "MNP",
    "workshop": "WKS",
    "hospitality": "HSP",
}

# Per-photo crop fixes for the 3:4 frame (default is 50% 30%), keyed by photo path.
PHOTO_POSITIONS = {
    "assets/team/01-overall-coordinators/adrika-sikader.webp": "85% 30%",
    "assets/team/02-content-and-anchoring/saurabh-sharma.webp": "30% 30%",  # keeps the ARTURO watermark out of frame
    "assets/team/08-web-development/tanish-jain.webp": "100% 30%",
}


def _load_team():
    with open(TEAM_JSON, encoding="utf-8") as f:
        data = json.load(f)
    teams = sorted(data["teams"], key=lambda t: t["order"])
    total = sum(len(t["members"]) for t in teams)
    assert total == data["totalMembers"], f"team.json lists {total} members, expected {data['totalMembers']}"
    return teams, total


def _render_card(team, index, member, is_oc):
    name = html.escape(member["name"])
    role = html.escape(member["role"])
    photo = html.escape(member["photo"])
    badge = f"{TEAM_CODES[team['id']]} // {index:02d}"

    if is_oc:
        domain, clearance = "Festival Command", "All Sectors"
    else:
        domain, clearance = html.escape(team["name"]), f"Sector {team['order']:02d}"

    position = PHOTO_POSITIONS.get(member["photo"])
    img_style = f' style="object-position:{position};"' if position else ""
    loading = "eager" if is_oc else "lazy"

    return f"""
      <article class="council-card" aria-label="{name}, {role}">
        <div class="council-photo">
          <img src="{photo}" alt="{name}" width="{member['photoWidth']}" height="{member['photoHeight']}" loading="{loading}" decoding="async"{img_style}>
          <span class="council-badge">{badge}</span>
          <span class="council-year" aria-hidden="true">MMXXVI</span>
        </div>
        <div class="council-info">
          <div class="council-role">{role}</div>
          <h3 class="council-name">{name}</h3>
          <dl class="council-meta">
            <div><dt>DOMAIN</dt><dd>{domain}</dd></div>
            <div><dt>CLEARANCE</dt><dd>{clearance}</dd></div>
          </dl>
        </div>
      </article>"""


def _render_section(team):
    is_oc = team["id"] == OC_TEAM_ID
    cards = "".join(_render_card(team, i, m, is_oc) for i, m in enumerate(team["members"], 1))
    team_name = html.escape(team["name"])
    return f"""
  <section class="council-section" id="{html.escape(team['id'])}" aria-label="{team_name}">
    <div class="council-section-hdr">
      <h2 class="council-section-title">* {team_name}</h2>
      <div class="council-count">SHOWING <span>{len(team['members']):02d}</span> COUNCIL WARDENS</div>
    </div>
    <div class="council-grid">{cards}
    </div>
  </section>"""


def get_team_content():
    title = "The Council — Team | ZEITGEIST'26 | IIT Ropar"
    description = "Meet the organizing council of ZEITGEIST'26: the overall coordinators and team heads across 13 departments at IIT Ropar."

    teams, total_members = _load_team()
    oc_teams = [t for t in teams if t["id"] == OC_TEAM_ID]
    departments = [t for t in teams if t["id"] != OC_TEAM_ID]

    extra_css = """
/* Team / Council Styles */
.council-hero {
  margin-bottom: 60px;
}

.council-hero h1 {
  font-size: clamp(40px, 8vw, 90px);
  margin-top: 14px;
}

.council-section {
  scroll-margin-top: 120px;
}

.council-section + .council-section {
  margin-top: 80px;
}

.council-section-hdr {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 12px 24px;
  margin-bottom: 24px;
}

.council-section-title {
  font-family: 'Cinzel', serif;
  font-weight: 800;
  font-size: clamp(20px, 2.5vw, 26px);
  line-height: 1.35;
  color: var(--amber);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  border-left: 4px solid var(--crim);
  padding-left: 16px;
  margin: 0;
}

.council-count {
  font: 500 9px var(--mono);
  letter-spacing: 0.2em;
  color: var(--ash);
  text-transform: uppercase;
}

.council-count span {
  color: var(--crim);
}

.council-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 24px;
}

.council-card {
  background: #0d0a0c;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 20px 20px 24px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
  position: relative;
  min-width: 0;
}

main#team .council-card:hover {
  border-color: var(--crim) !important;
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 0 0 40px var(--crim-glow) !important;
}

.council-photo {
  position: relative;
  aspect-ratio: 3 / 4;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: var(--char);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
}

.council-photo img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 30%;
  transition: transform 0.6s ease;
}

.council-card:hover .council-photo img {
  transform: scale(1.04);
}

.council-photo::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 40%;
  background: linear-gradient(to bottom, rgba(8, 5, 6, 0), rgba(8, 5, 6, 0.85));
  pointer-events: none;
  z-index: 1;
}

.council-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(4, 3, 4, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--crim);
  color: var(--crim-bright);
  font: 500 10px var(--mono);
  letter-spacing: 0.25em;
  padding: 6px 12px;
  text-transform: uppercase;
  z-index: 2;
}

.council-year {
  position: absolute;
  right: 14px;
  bottom: 14px;
  font: 500 9px var(--mono);
  letter-spacing: 0.3em;
  color: var(--ash);
  opacity: 0.8;
  z-index: 2;
}

.council-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 22px;
}

.council-role {
  font: 500 11px var(--mono);
  letter-spacing: 0.25em;
  color: var(--amber);
  text-transform: uppercase;
}

.council-name {
  font: 700 23px/28px 'Cinzel Decorative', 'Cinzel', serif;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--bone);
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.95), 0 0 28px rgba(209, 15, 32, 0.45);
  overflow-wrap: anywhere;
  margin: 0;
  transition: text-shadow 0.4s ease;
}

.council-card:hover .council-name {
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.95), 0 0 34px rgba(209, 15, 32, 0.75);
}

.council-meta {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 16px;
  margin: 6px 0 0;
}

.council-meta dt {
  font: 500 9px var(--mono);
  letter-spacing: 0.2em;
  color: var(--ash);
  margin-bottom: 4px;
}

.council-meta dd {
  font: 400 11px/1.4 var(--mono);
  color: var(--bone);
  margin: 0;
}

.council-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 56px 0 64px;
}

.council-divider::before {
  content: "";
  flex: 0 0 48px;
  height: 1px;
  background: var(--crim);
}

.council-divider span {
  font: 500 10px/1.6 var(--mono);
  letter-spacing: 0.3em;
  color: var(--ash);
  text-transform: uppercase;
}

@media (max-width: 1200px) {
  .council-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

@media (max-width: 900px) {
  .council-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (max-width: 600px) {
  .council-grid { grid-template-columns: minmax(0, 1fr); }
  .council-section + .council-section { margin-top: 64px; }
}

@media (prefers-reduced-motion: reduce) {
  main#team .council-card:hover { transform: none !important; }
  .council-card:hover .council-photo img { transform: none; }
}
"""

    oc_html = "".join(_render_section(t) for t in oc_teams)
    dept_html = "".join(_render_section(t) for t in departments)

    main_html = f"""
<main id="team">
  <div class="council-hero">
    <span class="eyebrow" style="color:var(--crim);">THE ORGANIZING COUNCIL // MMXXVI</span>
    <h1 class="disp">THE COUNCIL</h1>
  </div>
{oc_html}

  <div class="council-divider">
    <span>{len(departments)} DEPARTMENTS · {total_members} WARDENS · ROSTER UNSEALS BELOW</span>
  </div>
{dept_html}
</main>
"""

    return title, description, extra_css, main_html, ""
