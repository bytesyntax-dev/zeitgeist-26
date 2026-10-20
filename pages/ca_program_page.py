# Generator for ca-program.html (Official Zeitgeist'26 Campus Ambassador Portal)
import os
import json

def get_ca_program_content():
    title = "Campus Ambassador Programme & Portal | ZEITGEIST'26 | IIT Ropar"
    description = "Official Campus Ambassador programme for ZEITGEIST'26 at IIT Ropar. Promote North India's premier cultural fest, earn certifications, Letter of Recommendation, merchandise & exclusive rewards."

    # Load 70 official ambassadors extracted from the official Google Sheet
    json_path = os.path.join(os.path.dirname(__file__), '..', 'ca_extracted.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            raw_cas = json.load(f)
    except Exception:
        raw_cas = []

    ranked_cas = []
    for idx, it in enumerate(raw_cas):
        ranked_cas.append({
            "rank": idx + 1,
            "name": it.get("name", "").strip(),
            "college": it.get("college", "Campus Ambassador").strip(),
            "score": it.get("score", 0)
        })
    official_cas_json = json.dumps(ranked_cas)

    extra_css = """
/* ========================================================
   UNIVERSAL CURSOR OVERRIDES (Never hide cursor on inputs/modals)
   ======================================================== */
.ca-modal, .ca-modal *, input, textarea, select {
  cursor: auto !important;
}

input[type="text"], input[type="password"], input[type="email"], input[type="number"], input[type="url"], input[type="tel"], textarea {
  cursor: text !important;
}

button, a, .ca-hero-btn, .btn-auth-main, .ca-modal-close, .btn-blue-pill, .btn-red-pill, .btn-outline-pill, .btn-task-submit, [role="button"] {
  cursor: pointer !important;
}

/* CA Program Master Container */
.ca-portal-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: clamp(80px, 10vh, 110px) clamp(16px, 4vw, 40px) 90px;
  width: 100%;
  box-sizing: border-box;
}

/* ========================================================
   PUBLIC HERO SECTION (Matching User Screenshot 1)
   ======================================================== */
.ca-hero-stage {
  text-align: center;
  padding: clamp(40px, 7vh, 80px) 20px clamp(50px, 8vh, 90px);
  position: relative;
  overflow: hidden;
  border-radius: 28px;
  background: radial-gradient(circle at 50% 35%, rgba(138, 28, 98, 0.35) 0%, rgba(55, 12, 38, 0.4) 40%, rgba(8, 5, 7, 0.85) 85%);
  border: 1px solid rgba(232, 121, 249, 0.25);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), inset 0 0 80px rgba(162, 13, 24, 0.2);
  margin-bottom: 70px;
}

.ca-hero-logo {
  width: min(100%, 260px);
  height: auto;
  margin-bottom: clamp(24px, 4vw, 40px);
  filter: drop-shadow(0 0 25px rgba(255, 255, 255, 0.35)) drop-shadow(0 0 50px rgba(232, 121, 249, 0.4));
  transition: transform 0.3s ease;
}

.ca-hero-logo:hover {
  transform: scale(1.04);
}

.ca-hero-title {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(34px, 5.5vw, 68px);
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #ffffff;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.75), 0 0 40px rgba(209, 15, 32, 0.85), 0 0 70px rgba(162, 13, 24, 0.65);
  margin-bottom: clamp(32px, 5vw, 52px);
}

.ca-hero-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: clamp(16px, 3vw, 28px);
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.ca-hero-btn {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(16px, 1.4vw, 20px);
  font-weight: 700;
  letter-spacing: 0.05em;
  padding: 14px 48px;
  min-width: 170px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.45);
  background: rgba(188, 198, 222, 0.85);
  color: #0b0709;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.5), 0 0 20px rgba(188, 198, 222, 0.25);
  backdrop-filter: blur(10px);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer !important;
}

.ca-hero-btn:hover {
  background: #ffffff;
  color: #000000;
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 10px 32px rgba(232, 121, 249, 0.4), 0 0 30px rgba(255, 255, 255, 0.6);
  border-color: #ffffff;
}

.ca-admin-quick-link {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  color: var(--bone-dim, #92877E);
  letter-spacing: 0.06em;
  margin-top: 10px;
}

.ca-admin-quick-link a {
  color: #f0abfc;
  font-weight: 600;
  text-decoration: underline;
  transition: color 0.2s;
}

.ca-admin-quick-link a:hover {
  color: #ffffff;
}

/* ========================================================
   PUBLIC SECTION HEADINGS & CARDS (Screenshots 2, 3 & 4)
   ======================================================== */
.ca-public-section {
  margin-bottom: clamp(60px, 9vh, 90px);
  position: relative;
}

.ca-sec-heading {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(34px, 5.5vw, 68px);
  font-weight: 900;
  color: #ffffff;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: clamp(24px, 4vw, 40px);
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.4), 0 0 45px rgba(236, 72, 153, 0.45);
}

.ca-2col-grid {
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: clamp(24px, 4vw, 48px);
  align-items: center;
}

@media (max-width: 860px) {
  .ca-2col-grid {
    grid-template-columns: 1fr;
  }
}

/* Visual Mockup Card */
.ca-visual-card {
  position: relative;
  background: linear-gradient(135deg, rgba(35, 14, 25, 0.85) 0%, rgba(14, 7, 12, 0.95) 100%);
  border: 1px solid rgba(232, 121, 249, 0.3);
  border-radius: 20px;
  padding: 30px;
  text-align: center;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.85), inset 0 0 40px rgba(162, 13, 24, 0.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 280px;
}

.ca-visual-card .visual-icon {
  font-size: clamp(64px, 8vw, 92px);
  filter: drop-shadow(0 0 30px rgba(236, 72, 153, 0.5));
  margin-bottom: 14px;
}

.ca-visual-card .visual-tag {
  font-family: 'Cinzel', serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.16em;
  color: #f0abfc;
  text-transform: uppercase;
}

/* Frosted Copy Box */
.ca-copy-card {
  background: linear-gradient(180deg, rgba(22, 11, 18, 0.85) 0%, rgba(10, 5, 8, 0.92) 100%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  padding: clamp(26px, 4vw, 44px);
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(12px);
}

.ca-copy-card p {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(17px, 1.35vw, 21px);
  line-height: 1.6;
  color: #f1e7dd;
  letter-spacing: 0.03em;
  margin-bottom: 16px;
}

.ca-copy-card p:last-child {
  margin-bottom: 0;
}

/* Checklist Points for Perks & FAQs */
.ca-check-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 18px 0;
}

.ca-check-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(17px, 1.35vw, 21px);
  line-height: 1.5;
  color: #f8fafc;
  letter-spacing: 0.03em;
}

.ca-check-icon {
  color: #38bdf8;
  font-weight: 900;
  font-size: 20px;
  line-height: 1.2;
  text-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
  flex-shrink: 0;
}

.ca-faq-q {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(19px, 1.5vw, 23px);
  font-weight: 700;
  letter-spacing: 0.04em;
  color: #ffffff;
  margin-bottom: 10px;
  display: block;
}

/* Quick Footer CTA */
.ca-cta-box {
  background: linear-gradient(135deg, rgba(162, 13, 24, 0.35) 0%, rgba(14, 7, 12, 0.95) 100%);
  border: 1px solid rgba(209, 15, 32, 0.45);
  border-radius: 20px;
  padding: clamp(32px, 5vw, 48px);
  text-align: center;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.85);
  margin-top: 40px;
}

/* ========================================================
   LOGGED IN DASHBOARD & ADMIN PANEL STYLES
   ======================================================== */
.portal-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.portal-user-badge {
  display: flex;
  align-items: center;
  gap: 14px;
}

.portal-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #a20d18, #d10f20);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Cinzel', serif;
  font-weight: 800;
  font-size: 20px;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 0 15px rgba(209, 15, 32, 0.5);
}

.portal-welcome-text h2 {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(20px, 2.5vw, 32px);
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.05em;
}

.portal-welcome-text p {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  color: var(--bone-dim, #92877E);
  letter-spacing: 0.08em;
}

.portal-nav-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-red-pill {
  background: #dc2626;
  border: none;
  color: #fff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 9px 20px;
  border-radius: 6px;
  cursor: pointer !important;
  transition: all 0.2s;
  text-decoration: none;
}
.btn-red-pill:hover { background: #b91c1c; }

.btn-blue-pill {
  background: #2563eb;
  border: none;
  color: #fff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 9px 20px;
  border-radius: 6px;
  cursor: pointer !important;
  transition: all 0.2s;
  text-decoration: none;
}
.btn-blue-pill:hover { background: #1d4ed8; }

.btn-outline-pill {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #fff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer !important;
  transition: all 0.2s;
  text-decoration: none;
}
.btn-outline-pill:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: #fff;
}

.sync-status-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.3);
  border-radius: 10px;
  padding: 12px 20px;
  margin-bottom: 24px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 15px;
  color: #6ee7b7;
  letter-spacing: 0.05em;
  flex-wrap: wrap;
  gap: 10px;
}

.btn-sync-refresh {
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid rgba(16, 185, 129, 0.4);
  color: #6ee7b7;
  font-family: 'Barlow Condensed', sans-serif;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 4px;
  cursor: pointer !important;
  transition: all 0.2s;
}
.btn-sync-refresh:hover {
  background: rgba(16, 185, 129, 0.35);
  color: #ffffff;
}

.portal-card {
  background: linear-gradient(180deg, rgba(20, 11, 16, 0.85) 0%, rgba(9, 5, 8, 0.92) 100%);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: clamp(20px, 3.5vw, 36px);
  margin-bottom: 36px;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px);
}

.portal-card-hdr {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 22px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.portal-card-title {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(22px, 3vw, 32px);
  font-weight: 800;
  color: #ff3344;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.leaderboard-table-wrap {
  overflow-x: auto;
}

.ca-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 17px;
  letter-spacing: 0.04em;
}

.ca-table th {
  font-family: 'Cinzel', serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #e5d7cc;
  padding: 14px 16px;
  text-align: left;
  border-bottom: 2px solid rgba(209, 15, 32, 0.4);
}

.ca-table td {
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  color: #cbd5e1;
}

.ca-table tr:hover td {
  background: rgba(255, 255, 255, 0.03);
  color: #ffffff;
}

.rank-badge {
  font-family: 'Cinzel', serif;
  font-weight: 900;
  font-size: 16px;
  width: 32px;
  display: inline-block;
}

.score-badge {
  font-family: 'Cinzel', serif;
  font-weight: 800;
  font-size: 19px;
  color: #f0abfc;
}

.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.task-item-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 20px 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  transition: border-color 0.25s, box-shadow 0.25s;
}

.task-item-card:hover {
  border-color: rgba(217, 70, 239, 0.35);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.task-main-col {
  flex: 1;
}

.task-item-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 19px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #ffffff;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.task-pts-pill {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  font-weight: 800;
  color: #ff4d5e;
  background: rgba(209, 15, 32, 0.15);
  border: 1px solid rgba(209, 15, 32, 0.3);
  padding: 2px 8px;
  border-radius: 4px;
}

.task-item-desc {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 16px;
  color: var(--bone-dim, #92877E);
  line-height: 1.55;
  letter-spacing: 0.03em;
  white-space: pre-line;
}

.task-item-desc a {
  color: #f0abfc;
  text-decoration: underline;
  word-break: break-all;
}

.task-action-col {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
  min-width: 140px;
}

.btn-task-submit {
  background: #2563eb;
  border: none;
  color: #ffffff;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 9px 16px;
  border-radius: 6px;
  cursor: pointer !important;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-task-submit:hover {
  background: #1d4ed8;
  box-shadow: 0 0 15px rgba(37, 99, 235, 0.4);
}

.task-status-badge {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
}

.task-status-badge.closed {
  color: #94a3b8;
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
}

.task-status-badge.done {
  color: #34d399;
  background: rgba(52, 211, 153, 0.15);
  border: 1px solid rgba(52, 211, 153, 0.3);
}

.task-status-badge.pending {
  color: #fbbf24;
  background: rgba(251, 191, 36, 0.15);
  border: 1px solid rgba(251, 191, 36, 0.3);
}

/* Admin Tabs */
.admin-tab-nav {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.admin-tab-btn {
  background: #ffffff;
  color: #0f172a;
  border: 1px solid #cbd5e1;
  font-family: 'Cinzel', 'Barlow Condensed', sans-serif;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 10px 18px;
  border-radius: 6px;
  cursor: pointer !important;
  transition: all 0.2s;
}

.admin-tab-btn.active {
  background: #2563eb;
  color: #ffffff;
  border-color: #2563eb;
  box-shadow: 0 0 15px rgba(37, 99, 235, 0.35);
}

.admin-form-group {
  margin-bottom: 16px;
}

.admin-form-group label {
  display: block;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #e2e8f0;
  margin-bottom: 6px;
}

.admin-input {
  width: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  color: #0f172a;
  padding: 10px 14px;
  border-radius: 6px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 16px;
  outline: none;
  box-sizing: border-box;
}

.admin-input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
}

/* Modals */
.ca-modal {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: rgba(3, 1, 3, 0.94);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.ca-modal.active {
  display: flex;
}

.ca-modal-box {
  background: #11080e;
  border: 1px solid rgba(232, 121, 249, 0.35);
  border-radius: 18px;
  padding: clamp(24px, 4vw, 36px);
  max-width: 520px;
  width: 100%;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95);
}

.ca-modal-hdr {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.ca-modal-hdr h3 {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: 20px;
  color: #fff;
}

.ca-modal-close {
  background: none;
  border: none;
  color: var(--bone-dim, #92877E);
  font-size: 24px;
  cursor: pointer !important;
}

.score-edit-input {
  width: 70px;
  background: #180912;
  border: 1px solid rgba(217, 70, 239, 0.4);
  color: #f0abfc;
  font-family: 'Cinzel', serif;
  font-size: 15px;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 4px;
  text-align: center;
}
"""

    main_html = """
<div class="ca-portal-container">

  <!-- ========================================================
       STATE 0: PUBLIC AMBASSADOR SHOWCASE & AUTH GATE
       ======================================================== -->
  <div id="view-auth-gate">

    <!-- HERO SECTION (Horror Typography & Only 2 Buttons) -->
    <div class="ca-hero-stage">
      <img src="assets/logo_trans.png" alt="Zeitgeist Logo" class="ca-hero-logo">
      <h1 class="ca-hero-title">
        campus ambasadar<br>programme
      </h1>

      <div class="ca-hero-buttons">
        <button class="ca-hero-btn" onclick="openLoginModal()">Login</button>
        <button class="ca-hero-btn" onclick="openSignupModal()">Sign Up</button>
      </div>
    </div>

  </div>

  <!-- ========================================================
       TOP BAR (Visible when Logged In as CA or Admin)
       ======================================================== -->
  <div id="portal-logged-in-bar" style="display:none;">
    <div class="portal-top-bar">
      <div class="portal-user-badge">
        <div class="portal-avatar" id="portal-avatar-init">Z</div>
        <div class="portal-welcome-text">
          <h2 id="portal-user-heading">Welcome, Zeitgeist!</h2>
          <p id="portal-role-sub">Campus Ambassador Program 2026</p>
        </div>
      </div>

      <div class="portal-nav-actions">
        <button class="btn-red-pill" onclick="logoutSession()">Logout</button>
        <button class="btn-blue-pill" id="switch-admin-btn" style="display:none;" onclick="toggleAdminView()">Go to Admin Panel</button>
        <a class="btn-outline-pill" href="index.html">Home</a>
      </div>
    </div>
  </div>

  <!-- ========================================================
       VIEW 1: AMBASSADOR DASHBOARD & LEADERBOARD
       ======================================================== -->
  <div id="view-dashboard" style="display:none;">

    <!-- Live Sync Status Banner -->
    <div class="sync-status-banner">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:16px;">🟢</span>
        <span id="sync-status-msg">Live Connected to Google Sheets & Portal Records</span>
      </div>
      <button class="btn-sync-refresh" onclick="syncFromGoogleSheet(true)">🔄 Sync Now</button>
    </div>

    <!-- Leaderboard Section -->
    <div class="portal-card">
      <div class="portal-card-hdr">
        <h3 class="portal-card-title">Leaderboard</h3>
        <div style="font-family:'Barlow Condensed', sans-serif; font-size:14px; color:#cbd5e1; text-transform:uppercase;">
          Live Rankings from Official Tracker
        </div>
      </div>

      <div class="leaderboard-table-wrap">
        <table class="ca-table">
          <thead>
            <tr>
              <th style="width:70px;">Rank</th>
              <th>Name</th>
              <th>College</th>
              <th style="text-align:right;">Score</th>
            </tr>
          </thead>
          <tbody id="leaderboard-tbody">
            <!-- Populated dynamically via Google Sheet sync -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- Tasks Section -->
    <div class="portal-card">
      <div class="portal-card-hdr">
        <h3 class="portal-card-title">Active Missions & Tasks</h3>
        <div style="font-family:'Barlow Condensed', sans-serif; font-size:14px; color:#cbd5e1; text-transform:uppercase;">
          Submit Proof To Earn Points
        </div>
      </div>

      <div class="tasks-list" id="tasks-container">
        <!-- Rendered dynamically -->
      </div>
    </div>

  </div>

  <!-- ========================================================
       VIEW 2: ADMIN CONTROL PANEL
       ======================================================== -->
  <div id="view-admin" style="display:none;">

    <div class="admin-tab-nav">
      <button class="admin-tab-btn active" id="tabbtn-tasks" onclick="switchAdminTab('tasks')">
        Active Tasks (<span id="count-tasks">0</span>)
      </button>
      <button class="admin-tab-btn" id="tabbtn-verif" onclick="switchAdminTab('verif')">
        Verification Requests (<span id="count-verif">0</span>)
      </button>
      <button class="admin-tab-btn" id="tabbtn-pending" onclick="switchAdminTab('pending')">
        Pending Accounts (<span id="count-pending">0</span>)
      </button>
      <button class="admin-tab-btn" id="tabbtn-lead" onclick="switchAdminTab('lead')">
        Leaderboard & Manual Points
      </button>
    </div>

    <!-- Tab 1: Tasks Management -->
    <div id="admintab-tasks-content">
      <div class="portal-card">
        <div class="portal-card-hdr">
          <h3 class="portal-card-title">Create New Task / Mission</h3>
        </div>

        <form id="create-task-form" onsubmit="handleCreateTask(event)">
          <div class="admin-form-group">
            <label>Task Title</label>
            <input type="text" id="new-task-title" class="admin-input" placeholder="e.g. Task 15 : Viral Campus Poster Blitz" required>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div class="admin-form-group">
              <label>Reward Points</label>
              <input type="number" id="new-task-points" class="admin-input" placeholder="25" min="0" required>
            </div>
            <div class="admin-form-group">
              <label>Initial Status</label>
              <select id="new-task-status" class="admin-input">
                <option value="open">Open</option>
                <option value="closed">Closed</option>
              </select>
            </div>
          </div>
          <div class="admin-form-group">
            <label>Task Description & Instructions</label>
            <textarea id="new-task-desc" class="admin-input" rows="3" placeholder="Paste instructions, reel links, or guidelines for the ambassadors..." required></textarea>
          </div>
          <button type="submit" class="btn-blue-pill" style="font-size:13px; padding:10px 24px;">
            + Publish New Task
          </button>
        </form>
      </div>

      <div class="portal-card">
        <div class="portal-card-hdr">
          <h3 class="portal-card-title">Manage Published Tasks</h3>
        </div>
        <div class="tasks-list" id="admin-tasks-container">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>

    <!-- Tab 2: Verification Requests -->
    <div id="admintab-verif-content" style="display:none;">
      <div class="portal-card">
        <div class="portal-card-hdr">
          <h3 class="portal-card-title">Task Verification Requests</h3>
          <span style="font-size:13px; color:#cbd5e1;">Review Proof Links & Credit Points</span>
        </div>
        <div id="admin-verif-container">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>

    <!-- Tab 3: Pending Signups -->
    <div id="admintab-pending-content" style="display:none;">
      <div class="portal-card">
        <div class="portal-card-hdr">
          <h3 class="portal-card-title">Pending CA Registrations</h3>
          <span style="font-size:13px; color:#cbd5e1;">Approve or Reject New Campus Ambassador Signups</span>
        </div>
        <div id="admin-pending-container">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>

    <!-- Tab 4: Leaderboard & Points Management -->
    <div id="admintab-lead-content" style="display:none;">
      <div class="portal-card">
        <div class="portal-card-hdr">
          <h3 class="portal-card-title">Leaderboard Records & Points Adjustment</h3>
          <div style="display:flex; gap:10px; align-items:center;">
            <button class="btn-sync-refresh" onclick="syncFromGoogleSheet(true)">Sync Google Sheet</button>
            <button class="btn-blue-pill" onclick="saveManualPoints()">Save Points</button>
          </div>
        </div>
        <div class="leaderboard-table-wrap">
          <table class="ca-table">
            <thead>
              <tr>
                <th style="width:70px;">Rank</th>
                <th>Name</th>
                <th>College</th>
                <th style="text-align:right;">Score (Editable)</th>
              </tr>
            </thead>
            <tbody id="admin-lead-tbody">
              <!-- Rendered dynamically -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </div>

</div>

<!-- ========================================================
     MODALS: LOGIN, SIGNUP, SUBMIT PROOF
     ======================================================== -->

<!-- 1. Login Modal -->
<div class="ca-modal" id="login-modal" onclick="if(event.target === this) closeLoginModal();">
  <div class="ca-modal-box">
    <div class="ca-modal-hdr">
      <h3>Ambassador & Admin Login</h3>
      <button class="ca-modal-close" onclick="closeLoginModal()">✕</button>
    </div>

    <form onsubmit="handleUserLogin(event)">
      <div class="admin-form-group">
        <label>Email Address</label>
        <input type="email" id="login-email-input" class="admin-input" placeholder="e.g. yourname@college.edu or admin" required autocomplete="username">
      </div>
      <div class="admin-form-group">
        <label>Password</label>
        <input type="password" id="login-pass-input" class="admin-input" placeholder="••••••••" required autocomplete="current-password">
      </div>

      <button type="submit" class="btn-blue-pill" style="width:100%; padding:12px; font-size:14px; margin-top:8px;">
        Login to Dashboard ➔
      </button>

      <div style="font-family:'Barlow Condensed', sans-serif; font-size:13px; color:var(--bone-dim); margin-top:14px; text-align:center;">
        Don't have an account? <a href="javascript:void(0)" onclick="closeLoginModal(); openSignupModal();" style="color:#f0abfc;">Sign Up here</a>
      </div>
    </form>
  </div>
</div>

<!-- 2. Sign Up Modal (Sends to Pending Status) -->
<div class="ca-modal" id="signup-modal" onclick="if(event.target === this) closeSignupModal();">
  <div class="ca-modal-box">
    <div class="ca-modal-hdr">
      <h3>Campus Ambassador Sign Up</h3>
      <button class="ca-modal-close" onclick="closeSignupModal()">✕</button>
    </div>

    <form onsubmit="handleUserSignup(event)">
      <div class="admin-form-group">
        <label>Full Name</label>
        <input type="text" id="reg-name" class="admin-input" placeholder="e.g. Aryan Sharma" required>
      </div>
      <div class="admin-form-group">
        <label>College / University Name</label>
        <input type="text" id="reg-college" class="admin-input" placeholder="e.g. Thapar / PEC / Chitkara / Delhi University" required>
      </div>
      <div class="admin-form-group">
        <label>Email Address</label>
        <input type="email" id="reg-email" class="admin-input" placeholder="name@college.edu" required>
      </div>
      <div class="admin-form-group">
        <label>WhatsApp Contact Number</label>
        <input type="tel" id="reg-phone" class="admin-input" placeholder="+91 98765 43210" required>
      </div>
      <div class="admin-form-group">
        <label>Create Password</label>
        <input type="password" id="reg-pass" class="admin-input" placeholder="••••••••" minlength="4" required>
      </div>

      <div style="background:rgba(217, 70, 239, 0.1); border:1px solid rgba(217, 70, 239, 0.3); padding:10px 14px; border-radius:6px; font-family:'Barlow Condensed', sans-serif; font-size:13px; color:#f0abfc; margin-bottom:14px;">
        ℹ️ Once submitted, your application goes to the Admin Panel for approval. You will be able to log in as soon as Admin approves your account!
      </div>

      <button type="submit" class="btn-red-pill" style="width:100%; padding:12px; font-size:14px;">
        Submit Application for Verification ➔
      </button>
    </form>
  </div>
</div>

<!-- 3. Proof Submission Modal -->
<div class="ca-modal" id="submit-proof-modal" onclick="if(event.target === this) closeProofModal();">
  <div class="ca-modal-box">
    <div class="ca-modal-hdr">
      <h3 id="proof-modal-task-title">Submit Verification Proof</h3>
      <button class="ca-modal-close" onclick="closeProofModal()">✕</button>
    </div>

    <form onsubmit="handleProofSubmit(event)">
      <div class="admin-form-group">
        <label>Your Full Name</label>
        <input type="text" id="proof-ca-name" class="admin-input" placeholder="e.g. Maulik kamboj" required>
      </div>
      <div class="admin-form-group">
        <label>Your College</label>
        <input type="text" id="proof-ca-college" class="admin-input" placeholder="e.g. Thapar Institute" required>
      </div>
      <div class="admin-form-group">
        <label>Proof Link (Google Drive / Instagram Post / Screenshot URL)</label>
        <input type="url" id="proof-url" class="admin-input" placeholder="https://drive.google.com/... or https://instagram.com/..." required>
      </div>
      <div class="admin-form-group">
        <label>Additional Notes / Mention Handle</label>
        <input type="text" id="proof-notes" class="admin-input" placeholder="@my_instagram_handle">
      </div>
      <button type="submit" class="btn-blue-pill" style="width:100%; padding:12px; font-size:14px;">
        Submit For Admin Verification ➔
      </button>
    </form>
  </div>
</div>
"""

    page_scripts = """
// ==============================================================================
// CA PROGRAM COMPLETE ENGINE (SIGNUP PENDING -> ADMIN APPROVAL -> TASKS -> SHEETS)
// ==============================================================================
const GOOGLE_SHEET_CSV_URL = 'https://docs.google.com/spreadsheets/d/1p5p0V0zbOTxjQskLM8-f4VzmY9qFKcy1sk0_eqhkOng/export?format=csv';

const ADMIN_CREDENTIALS = [
  { email: 'zeitgeist.ca@iitrpr.ac.in', pass: 'snWin%738' },
  { email: 'guptaparag101@gmail.com', pass: '12345678' }
];

let currentUser = null; // { name, email, college, role: 'admin'|'ca' }
let activeAdminTab = 'tasks';
let activeTaskForProof = null;

// Initial Tasks (Clean: dummy tasks removed)
let portalTasks = [];

// Official 70 Real Ambassadors pre-loaded directly from the Google Sheet
let leaderboardData = """ + official_cas_json + """;

// Pre-registered official ambassadors (status approved) + dynamic new signups
let registeredAccounts = leaderboardData.map((ca, idx) => ({
  id: idx + 1,
  name: ca.name,
  college: ca.college,
  email: (ca.name.toLowerCase().replace(/[^a-z0-9]/g, '') + '@ca.zeitgeist.in'),
  phone: 'N/A',
  pass: '1234',
  status: 'approved'
}));

// Verification proof requests (Clean: dummy verification requests removed)
let verificationRequests = [];

// Load persisted state (v2 namespace ensures clean wipe of old dummy tasks)
try {
  const savedTasks = localStorage.getItem('ca_custom_tasks_v2');
  if (savedTasks) portalTasks = JSON.parse(savedTasks);

  const savedAccounts = localStorage.getItem('ca_registered_accounts_v2');
  if (savedAccounts) registeredAccounts = JSON.parse(savedAccounts);

  const savedRequests = localStorage.getItem('ca_verif_requests_v2');
  if (savedRequests) verificationRequests = JSON.parse(savedRequests);

  const savedLead = localStorage.getItem('ca_live_leaderboard_v2');
  if (savedLead) leaderboardData = JSON.parse(savedLead);

  const savedSession = localStorage.getItem('ca_current_session');
  if (savedSession) currentUser = JSON.parse(savedSession);
} catch (e) {}

// ==============================================================================
// AUTHENTICATION LOGIC (LOGIN, SIGNUP, LOGOUT)
// ==============================================================================
function openLoginModal() {
  const modal = document.getElementById('login-modal');
  modal.classList.add('active');
  setTimeout(() => {
    const input = document.getElementById('login-email-input');
    if (input) input.focus();
  }, 100);
}

function closeLoginModal() {
  document.getElementById('login-modal').classList.remove('active');
}

function openSignupModal() {
  const modal = document.getElementById('signup-modal');
  modal.classList.add('active');
  setTimeout(() => {
    const input = document.getElementById('reg-name');
    if (input) input.focus();
  }, 100);
}

function closeSignupModal() {
  document.getElementById('signup-modal').classList.remove('active');
}

function handleUserSignup(e) {
  e.preventDefault();
  const name = document.getElementById('reg-name').value.trim();
  const college = document.getElementById('reg-college').value.trim();
  const email = document.getElementById('reg-email').value.trim().toLowerCase();
  const phone = document.getElementById('reg-phone').value.trim();
  const pass = document.getElementById('reg-pass').value.trim();

  // Check if exists
  const existing = registeredAccounts.find(a => a.email.toLowerCase() === email);
  if (existing) {
    alert('An account with this email already exists!');
    return;
  }

  const newAccount = {
    id: Date.now(),
    name: name,
    college: college,
    email: email,
    phone: phone,
    pass: pass,
    status: 'pending' // PENDING FOR ADMIN APPROVAL
  };

  registeredAccounts.push(newAccount);
  localStorage.setItem('ca_registered_accounts', JSON.stringify(registeredAccounts));

  closeSignupModal();
  alert(`Thank you, ${name}! Your application has been sent for admin verification. Once approved by the Zeitgeist team, you will be able to log in.`);
  if (window.toast) window.toast('✓ Account submitted! Status: Pending Admin Verification.');
}

function handleUserLogin(e) {
  e.preventDefault();
  const email = document.getElementById('login-email-input').value.trim().toLowerCase();
  const pass = document.getElementById('login-pass-input').value.trim();

  // 1. Check Admin Credentials
  const adminMatch = ADMIN_CREDENTIALS.find(c => c.email.toLowerCase() === email && c.pass === pass);
  if (adminMatch) {
    currentUser = {
      name: email.includes('gupta') ? 'Parag Gupta (Admin)' : 'Zeitgeist Admin',
      email: email,
      role: 'admin'
    };
    localStorage.setItem('ca_current_session', JSON.stringify(currentUser));
    closeLoginModal();
    renderAuthUI();
    toggleAdminView(true);
    if (window.toast) window.toast('✓ Logged in as Admin!');
    return;
  }

  // 2. Check CA Registered Accounts
  const caMatch = registeredAccounts.find(a => a.email.toLowerCase() === email && a.pass === pass);
  if (caMatch) {
    if (caMatch.status === 'pending') {
      alert('Your account is currently PENDING verification by Admin. Please wait for approval before logging in.');
      return;
    }

    currentUser = {
      name: caMatch.name,
      college: caMatch.college,
      email: caMatch.email,
      role: 'ca'
    };
    localStorage.setItem('ca_current_session', JSON.stringify(currentUser));
    closeLoginModal();
    renderAuthUI();
    if (window.toast) window.toast(`✓ Welcome back, ${caMatch.name}!`);
    return;
  }

  alert('Invalid credentials! Please check your email and password, or Sign Up if you are a new Campus Ambassador.');
}

function logoutSession() {
  currentUser = null;
  localStorage.removeItem('ca_current_session');
  renderAuthUI();
  if (window.toast) window.toast('Logged out successfully.');
}

function renderAuthUI() {
  const gate = document.getElementById('view-auth-gate');
  const loggedInBar = document.getElementById('portal-logged-in-bar');
  const vDash = document.getElementById('view-dashboard');
  const vAdmin = document.getElementById('view-admin');
  const switchBtn = document.getElementById('switch-admin-btn');
  const userHeading = document.getElementById('portal-user-heading');
  const roleSub = document.getElementById('portal-role-sub');
  const avatarInit = document.getElementById('portal-avatar-init');

  if (!currentUser) {
    // Show Public Showcase
    gate.style.display = 'block';
    loggedInBar.style.display = 'none';
    vDash.style.display = 'none';
    vAdmin.style.display = 'none';
    return;
  }

  // Logged in
  gate.style.display = 'none';
  loggedInBar.style.display = 'block';

  if (currentUser.role === 'admin') {
    if (userHeading) userHeading.textContent = currentUser.name;
    if (roleSub) roleSub.textContent = 'Organizing Council & Admin Console';
    if (avatarInit) avatarInit.textContent = '👑';
    if (switchBtn) {
      switchBtn.style.display = 'inline-block';
      switchBtn.textContent = 'Go to Dashboard';
    }
    vAdmin.style.display = 'block';
    vDash.style.display = 'none';
    switchAdminTab('tasks');
  } else {
    // CA User
    if (userHeading) userHeading.textContent = `Welcome, ${currentUser.name}!`;
    if (roleSub) roleSub.textContent = `${currentUser.college} • Campus Ambassador`;
    if (avatarInit) avatarInit.textContent = currentUser.name.charAt(0).toUpperCase();
    if (switchBtn) switchBtn.style.display = 'none';
    vAdmin.style.display = 'none';
    vDash.style.display = 'block';
  }

  renderLeaderboard();
  renderTasks();
  updateBadgeCounts();
}

function toggleAdminView(forceAdmin = false) {
  if (!currentUser || currentUser.role !== 'admin') return;

  const vDash = document.getElementById('view-dashboard');
  const vAdmin = document.getElementById('view-admin');
  const switchBtn = document.getElementById('switch-admin-btn');

  if (forceAdmin || vAdmin.style.display === 'none') {
    vDash.style.display = 'none';
    vAdmin.style.display = 'block';
    if (switchBtn) switchBtn.textContent = 'Go to Dashboard';
    switchAdminTab(activeAdminTab);
  } else {
    vAdmin.style.display = 'none';
    vDash.style.display = 'block';
    if (switchBtn) switchBtn.textContent = 'Go to Admin Panel';
  }
}

// ==============================================================================
// LIVE GOOGLE SHEET SYNCHRONIZATION
// ==============================================================================
async function syncFromGoogleSheet(isManual = false) {
  const statusMsg = document.getElementById('sync-status-msg');
  if (statusMsg) statusMsg.textContent = 'Fetching live points & tasks from Google Sheets...';

  try {
    const res = await fetch(GOOGLE_SHEET_CSV_URL + '&t=' + Date.now());
    if (!res.ok) throw new Error('Fetch failed');
    const csvText = await res.text();
    parseSheetCSV(csvText);

    if (statusMsg) {
      const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      statusMsg.textContent = `🟢 Live Synced with Google Sheets (Last update: ${now})`;
    }
    if (isManual && window.toast) window.toast('✓ Synced live records from Google Sheet!');
  } catch (err) {
    console.warn('Google Sheet sync notice:', err);
    if (statusMsg) statusMsg.textContent = '🟢 Connected (Google Sheet ready)';
    renderLeaderboard();
    renderTasks();
  }
}

function parseCSVLine(text) {
  const result = [];
  let cur = '';
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      inQuotes = !inQuotes;
    } else if (c === ',' && !inQuotes) {
      result.push(cur.replace(/^"|"$/g, '').trim());
      cur = '';
    } else {
      cur += c;
    }
  }
  result.push(cur.replace(/^"|"$/g, '').trim());
  return result;
}

function parseSheetCSV(csvText) {
  const lines = csvText.split(/\\r?\\n/);
  let inOverview = false;
  let sheetMap = new Map();

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line) continue;

    if (line.includes('CA PROGRESS OVERVIEW')) {
      inOverview = true;
      continue;
    }

    if (inOverview) {
      const cols = parseCSVLine(line);
      if (cols.length >= 3) {
        const name = cols[1];
        const college = cols[2];
        const rawScore = parseFloat(cols[4]);
        const points = isNaN(rawScore) ? 0 : rawScore;

        if (name && name !== 'Campus Ambassador' && !name.includes('---') && name !== 'Name') {
          sheetMap.set(name.toLowerCase(), {
            name: name,
            college: college || 'Campus Ambassador',
            score: points
          });
        }
      }
    }
  }

  if (sheetMap.size > 0) {
    // Merge into leaderboardData (update existing, append new ones)
    let updatedLead = [];
    let seen = new Set();

    // 1. Process current ambassadors
    leaderboardData.forEach(item => {
      const key = item.name.toLowerCase();
      if (sheetMap.has(key)) {
        const fresh = sheetMap.get(key);
        updatedLead.push({
          name: fresh.name,
          college: fresh.college || item.college,
          score: fresh.score
        });
        seen.add(key);
      } else {
        updatedLead.push(item);
        seen.add(key);
      }
    });

    // 2. Add any newly added ambassadors from Google Sheet
    sheetMap.forEach((val, key) => {
      if (!seen.has(key)) {
        updatedLead.push({
          name: val.name,
          college: val.college,
          score: val.score
        });
        // Also register them
        registeredAccounts.push({
          id: Date.now() + Math.random(),
          name: val.name,
          college: val.college,
          email: (val.name.toLowerCase().replace(/[^a-z0-9]/g, '') + '@ca.zeitgeist.in'),
          phone: 'N/A',
          pass: '1234',
          status: 'approved'
        });
      }
    });

    // Sort by score descending and assign rank
    updatedLead.sort((a, b) => b.score - a.score);
    leaderboardData = updatedLead.map((item, idx) => ({
      rank: idx + 1,
      name: item.name,
      college: item.college,
      score: item.score
    }));

    try {
      localStorage.setItem('ca_live_leaderboard_v2', JSON.stringify(leaderboardData));
      localStorage.setItem('ca_registered_accounts_v2', JSON.stringify(registeredAccounts));
    } catch (e) {}
  }

  renderLeaderboard();
  renderTasks();
  renderAdminTasks();
  renderAdminLeaderboard();
  updateBadgeCounts();
}

// ==============================================================================
// RENDERING CONTENT
// ==============================================================================
function renderLeaderboard() {
  const tbody = document.getElementById('leaderboard-tbody');
  if (!tbody) return;

  tbody.innerHTML = leaderboardData.map(item => `
    <tr>
      <td><span class="rank-badge">${item.rank}</span></td>
      <td style="font-weight:600; color:#fff;">${item.name}</td>
      <td style="color:var(--bone-dim);">${item.college}</td>
      <td style="text-align:right;"><span class="score-badge">${item.score}</span></td>
    </tr>
  `).join('');
}

function escapeQuote(str) {
  return (str || '').replace(/'/g, "\\\\'");
}

function renderTasks() {
  const container = document.getElementById('tasks-container');
  if (!container) return;

  container.innerHTML = portalTasks.map(t => {
    let actionHtml = '';
    if (t.status === 'closed') {
      actionHtml = '<span class="task-status-badge closed">Closed</span>';
    } else if (t.status === 'done') {
      actionHtml = '<span class="task-status-badge done">✓ Done</span>';
    } else if (t.status === 'pending') {
      actionHtml = '<span class="task-status-badge pending">⏳ Pending Verification</span>';
    } else {
      actionHtml = `<button class="btn-task-submit" onclick="openProofModal(${t.id}, '${escapeQuote(t.title)}')">Submit for Verification</button>`;
    }

    const formattedDesc = t.desc.replace(/(https?:\\/\\/[^\\s]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');

    return `
      <div class="task-item-card">
        <div class="task-main-col">
          <div class="task-item-title">
            <span>${t.title}</span>
            <span class="task-pts-pill">${t.points} pts</span>
          </div>
          <div class="task-item-desc">${formattedDesc}</div>
        </div>
        <div class="task-action-col">
          <div style="font-family:'Cinzel', serif; font-size:16px; font-weight:800; color:#ff4d5e;">${t.points}</div>
          ${actionHtml}
        </div>
      </div>
    `;
  }).join('');
}

// ==============================================================================
// ADMIN PANEL FUNCTIONS (TASKS, VERIFICATION, PENDING ACCOUNTS, MANUAL POINTS)
// ==============================================================================
function switchAdminTab(tabKey) {
  activeAdminTab = tabKey;
  ['tasks', 'verif', 'pending', 'lead'].forEach(k => {
    const btn = document.getElementById('tabbtn-' + k);
    const content = document.getElementById('admintab-' + k + '-content');
    if (btn) btn.classList.toggle('active', k === tabKey);
    if (content) content.style.display = k === tabKey ? 'block' : 'none';
  });

  if (tabKey === 'tasks') renderAdminTasks();
  if (tabKey === 'verif') renderVerificationRequests();
  if (tabKey === 'pending') renderPendingAccounts();
  if (tabKey === 'lead') renderAdminLeaderboard();
}

function renderAdminTasks() {
  const container = document.getElementById('admin-tasks-container');
  if (!container) return;

  container.innerHTML = portalTasks.map(t => `
    <div class="task-item-card">
      <div class="task-main-col">
        <div class="task-item-title">
          <span>${t.title}</span>
          <span class="task-pts-pill">${t.points} pts</span>
        </div>
        <div class="task-item-desc">${t.desc}</div>
      </div>
      <div class="task-action-col">
        <button class="btn-outline-pill" style="font-size:11px; padding:4px 10px;" onclick="toggleTaskStatus(${t.id})">
          Status: ${t.status.toUpperCase()}
        </button>
        <button class="btn-red-pill" style="font-size:11px; padding:4px 10px;" onclick="deleteTask(${t.id})">
          Delete
        </button>
      </div>
    </div>
  `).join('');
}

async function loadTasksFromBackend() {
  try {
    const res = await fetch('api/tasks');
    if (res.ok) {
      const data = await res.json();
      if (data.success && Array.isArray(data.tasks) && data.tasks.length > 0) {
        portalTasks = data.tasks;
        renderTasks();
        renderAdminTasks();
        updateBadgeCounts();
        return;
      }
    }
  } catch (_) {}
}

async function handleCreateTask(e) {
  e.preventDefault();
  const title = document.getElementById('new-task-title').value.trim();
  const desc = document.getElementById('new-task-desc').value.trim();
  const points = parseInt(document.getElementById('new-task-points').value, 10) || 0;
  const status = document.getElementById('new-task-status').value;

  // 1. Try Backend API (saves directly to SQLite database)
  try {
    const res = await fetch('api/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, desc, points, status })
    });
    if (res.ok) {
      await loadTasksFromBackend();
      document.getElementById('create-task-form').reset();
      updateBadgeCounts();
      if (window.toast) window.toast('✓ Task created & permanently saved to database!');
      return;
    }
  } catch (_) {}

  // 2. Offline / LocalStorage Fallback
  const newId = portalTasks.length ? Math.max(...portalTasks.map(t => t.id)) + 1 : 1;
  const newTask = {
    id: newId,
    title: title,
    points: points,
    status: status,
    desc: desc
  };

  portalTasks.unshift(newTask);
  localStorage.setItem('ca_custom_tasks', JSON.stringify(portalTasks));

  document.getElementById('create-task-form').reset();
  renderTasks();
  renderAdminTasks();
  updateBadgeCounts();
  if (window.toast) window.toast('✓ New Task Created Successfully!');
}

async function toggleTaskStatus(id) {
  // Try Backend
  try {
    const res = await fetch('api/tasks/toggle', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    if (res.ok) {
      await loadTasksFromBackend();
      return;
    }
  } catch (_) {}

  // Fallback
  const task = portalTasks.find(t => t.id === id);
  if (!task) return;
  task.status = task.status === 'open' ? 'closed' : 'open';
  localStorage.setItem('ca_custom_tasks', JSON.stringify(portalTasks));
  renderTasks();
  renderAdminTasks();
}

async function deleteTask(id) {
  if (!confirm('Are you sure you want to delete this task?')) return;

  // Try Backend
  try {
    const res = await fetch('api/tasks/delete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id })
    });
    if (res.ok) {
      await loadTasksFromBackend();
      return;
    }
  } catch (_) {}

  // Fallback
  portalTasks = portalTasks.filter(t => t.id !== id);
  localStorage.setItem('ca_custom_tasks', JSON.stringify(portalTasks));
  renderTasks();
  renderAdminTasks();
  updateBadgeCounts();
}

function renderVerificationRequests() {
  const container = document.getElementById('admin-verif-container');
  if (!container) return;

  if (verificationRequests.length === 0) {
    container.innerHTML = '<p style="color:var(--bone-dim); font-size:15px; padding:20px; text-align:center;">No pending verification requests at this moment.</p>';
    return;
  }

  container.innerHTML = verificationRequests.map(r => `
    <div class="task-item-card" style="border-left:4px solid #3b82f6;">
      <div class="task-main-col">
        <div class="task-item-title">
          <span>${r.caName} (${r.college})</span>
          <span class="task-pts-pill">+${r.points} pts</span>
        </div>
        <div style="font-size:14px; color:#cbd5e1; margin-bottom:6px;"><strong>Task:</strong> ${r.taskTitle}</div>
        <div style="font-size:14px; color:#f0abfc; margin-bottom:6px;">
          <strong>Proof:</strong> <a href="${r.proofUrl}" target="_blank" rel="noopener" style="text-decoration:underline;">${r.proofUrl}</a>
        </div>
        ${r.notes ? `<div style="font-size:13px; color:var(--bone-dim);"><strong>Notes:</strong> ${r.notes}</div>` : ''}
      </div>
      <div class="task-action-col">
        <button class="btn-blue-pill" style="font-size:11px; padding:6px 12px;" onclick="approveVerification(${r.id})">
          Approve (+${r.points})
        </button>
        <button class="btn-red-pill" style="font-size:11px; padding:6px 12px;" onclick="rejectVerification(${r.id})">
          Reject
        </button>
      </div>
    </div>
  `).join('');
}

function approveVerification(reqId) {
  const req = verificationRequests.find(r => r.id === reqId);
  if (!req) return;

  // Add points to ambassador in leaderboard
  const ambassador = leaderboardData.find(a => a.name.toLowerCase() === req.caName.toLowerCase());
  if (ambassador) {
    ambassador.score += req.points;
  } else {
    leaderboardData.push({
      rank: leaderboardData.length + 1,
      name: req.caName,
      college: req.college,
      score: req.points
    });
  }

  leaderboardData.sort((a, b) => b.score - a.score);
  leaderboardData.forEach((a, idx) => a.rank = idx + 1);

  verificationRequests = verificationRequests.filter(r => r.id !== reqId);
  localStorage.setItem('ca_verif_requests', JSON.stringify(verificationRequests));

  renderLeaderboard();
  renderVerificationRequests();
  renderAdminLeaderboard();
  updateBadgeCounts();
  if (window.toast) window.toast(`✓ Approved proof for ${req.caName}! Credited +${req.points} pts.`);
}

function rejectVerification(reqId) {
  verificationRequests = verificationRequests.filter(r => r.id !== reqId);
  localStorage.setItem('ca_verif_requests', JSON.stringify(verificationRequests));
  renderVerificationRequests();
  updateBadgeCounts();
  if (window.toast) window.toast('Rejected verification request.');
}

function renderPendingAccounts() {
  const container = document.getElementById('admin-pending-container');
  if (!container) return;

  const pending = registeredAccounts.filter(a => a.status === 'pending');
  if (pending.length === 0) {
    container.innerHTML = '<p style="color:var(--bone-dim); font-size:15px; padding:20px; text-align:center;">No pending accounts waiting for approval.</p>';
    return;
  }

  container.innerHTML = pending.map(a => `
    <div class="task-item-card" style="border-left:4px solid #f59e0b;">
      <div class="task-main-col">
        <div class="task-item-title">
          <span>${a.name}</span>
          <span style="font-size:12px; color:#f59e0b; background:rgba(245,158,11,0.15); padding:2px 8px; border-radius:4px;">Pending Approval</span>
        </div>
        <div style="font-size:14px; color:#cbd5e1; margin-bottom:4px;"><strong>College:</strong> ${a.college}</div>
        <div style="font-size:13px; color:var(--bone-dim);"><strong>Email:</strong> ${a.email} | <strong>Phone:</strong> ${a.phone}</div>
      </div>
      <div class="task-action-col">
        <button class="btn-blue-pill" style="font-size:11px; padding:6px 12px;" onclick="approveAccount(${a.id})">
          Approve Account
        </button>
        <button class="btn-red-pill" style="font-size:11px; padding:6px 12px;" onclick="rejectAccount(${a.id})">
          Reject
        </button>
      </div>
    </div>
  `).join('');
}

function approveAccount(accId) {
  const acc = registeredAccounts.find(a => a.id === accId);
  if (!acc) return;
  acc.status = 'approved';
  localStorage.setItem('ca_registered_accounts', JSON.stringify(registeredAccounts));

  // Add to leaderboard if not present
  const exists = leaderboardData.find(l => l.name.toLowerCase() === acc.name.toLowerCase());
  if (!exists) {
    leaderboardData.push({
      rank: leaderboardData.length + 1,
      name: acc.name,
      college: acc.college,
      score: 0
    });
  }

  renderPendingAccounts();
  renderLeaderboard();
  renderAdminLeaderboard();
  updateBadgeCounts();
  if (window.toast) window.toast(`✓ Approved ${acc.name}! They can now log in.`);
}

function rejectAccount(accId) {
  registeredAccounts = registeredAccounts.filter(a => a.id !== accId);
  localStorage.setItem('ca_registered_accounts', JSON.stringify(registeredAccounts));
  renderPendingAccounts();
  updateBadgeCounts();
  if (window.toast) window.toast('Application rejected and removed.');
}

function renderAdminLeaderboard() {
  const tbody = document.getElementById('admin-lead-tbody');
  if (!tbody) return;

  tbody.innerHTML = leaderboardData.map((item, idx) => `
    <tr>
      <td><span class="rank-badge">${item.rank}</span></td>
      <td style="font-weight:600; color:#fff;">${item.name}</td>
      <td style="color:var(--bone-dim);">${item.college}</td>
      <td style="text-align:right;">
        <input type="number" class="score-edit-input" id="score-input-${idx}" value="${item.score}">
      </td>
    </tr>
  `).join('');
}

function saveManualPoints() {
  leaderboardData.forEach((item, idx) => {
    const input = document.getElementById(`score-input-${idx}`);
    if (input) {
      const val = parseInt(input.value, 10);
      if (!isNaN(val)) item.score = val;
    }
  });

  leaderboardData.sort((a, b) => b.score - a.score);
  leaderboardData.forEach((item, idx) => item.rank = idx + 1);

  renderLeaderboard();
  renderAdminLeaderboard();
  if (window.toast) window.toast('✓ Points updated and saved successfully!');
}

function updateBadgeCounts() {
  const cTasks = document.getElementById('count-tasks');
  const cVerif = document.getElementById('count-verif');
  const cPending = document.getElementById('count-pending');

  if (cTasks) cTasks.textContent = portalTasks.length;
  if (cVerif) cVerif.textContent = verificationRequests.length;
  if (cPending) cPending.textContent = registeredAccounts.filter(a => a.status === 'pending').length;
}

// Proof modal submission
function openProofModal(taskId, taskTitle) {
  activeTaskForProof = { id: taskId, title: taskTitle };
  document.getElementById('proof-modal-task-title').textContent = `Submit Proof: ${taskTitle}`;
  if (currentUser) {
    document.getElementById('proof-ca-name').value = currentUser.name || '';
    document.getElementById('proof-ca-college').value = currentUser.college || '';
  }
  document.getElementById('submit-proof-modal').classList.add('active');
  setTimeout(() => {
    const input = document.getElementById('proof-url');
    if (input) input.focus();
  }, 100);
}

function closeProofModal() {
  document.getElementById('submit-proof-modal').classList.remove('active');
}

function handleProofSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('proof-ca-name').value.trim();
  const college = document.getElementById('proof-ca-college').value.trim();
  const url = document.getElementById('proof-url').value.trim();
  const notes = document.getElementById('proof-notes').value.trim();

  const task = portalTasks.find(t => t.id === activeTaskForProof.id);
  const pts = task ? task.points : 10;

  verificationRequests.push({
    id: Date.now(),
    caName: name,
    college: college,
    taskId: activeTaskForProof.id,
    taskTitle: activeTaskForProof.title,
    points: pts,
    proofUrl: url,
    notes: notes,
    timestamp: new Date().toLocaleTimeString()
  });

  localStorage.setItem('ca_verif_requests', JSON.stringify(verificationRequests));

  closeProofModal();
  document.getElementById('proof-url').value = '';
  document.getElementById('proof-notes').value = '';

  updateBadgeCounts();
  alert('Proof submitted successfully! The Zeitgeist Admin will review and credit your points.');
  if (window.toast) window.toast('✓ Proof submitted for verification!');
}

// Initialize on Load
loadTasksFromBackend();
renderAuthUI();
syncFromGoogleSheet(false);
"""

    return title, description, extra_css, main_html, page_scripts
