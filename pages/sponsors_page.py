# Generator for sponsors.html (Clean Coming Soon)

def get_sponsors_content():
    title = "Sponsors | ZEITGEIST'26 | IIT Ropar"
    description = "Official Sponsors for ZEITGEIST'26 at IIT Ropar."

    extra_css = """
.cs-clean-wrapper {
  min-height: calc(100vh - 180px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px 20px;
}

.cs-clean-eyebrow {
  font-family: 'Cinzel', serif;
  font-size: clamp(14px, 1.2vw, 18px);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--bone-dim, #92877E);
  margin-bottom: 12px;
}

.cs-clean-title {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: clamp(40px, 8vw, 92px);
  font-weight: 900;
  letter-spacing: 0.08em;
  color: #ffffff;
  text-transform: uppercase;
  text-shadow: 0 0 25px rgba(209, 15, 32, 0.6), 0 0 50px rgba(0, 0, 0, 0.9);
  line-height: 1.1;
  margin-bottom: 28px;
}
"""

    main_html = """
<div class="cs-clean-wrapper">
  <div class="cs-clean-eyebrow">Official Sponsors</div>
  <h1 class="cs-clean-title">COMING SOON</h1>
  <a class="btn" href="index.html">← Back to Home</a>
</div>
"""

    return title, description, extra_css, main_html, ""
