"""Render the link-preview card, docs/assets/img/social-card.png (1200x630).

Uses a local Chrome in headless mode. Run: python scripts/social_card.py
Set CHROME to the browser binary if it is not at the default macOS path.
"""

import os
import subprocess
import tempfile
from pathlib import Path

CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)

ROOT = Path(__file__).resolve().parent.parent
LOGO = (ROOT / "docs/assets/img/logo.svg").read_text()
OUT = ROOT / "docs/assets/img/social-card.png"

HTML = f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  html, body {{ margin: 0; }}
  body {{
    width: 1200px; height: 630px; box-sizing: border-box;
    padding: 72px 84px; display: flex; flex-direction: column;
    justify-content: space-between;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #fbf4ef;
    background:
      radial-gradient(circle at 82% 14%, rgba(200, 85, 43, 0.32), transparent 420px),
      radial-gradient(circle at 9% 20%, rgba(238, 220, 209, 0.10), transparent 380px),
      linear-gradient(140deg, #1a0f0a, #2a1810 62%, #3d2216);
  }}
  .brand {{ display: flex; align-items: center; gap: 22px;
    font-size: 40px; font-weight: 800; letter-spacing: -0.02em; }}
  .brand svg {{ width: 84px; height: 84px; }}
  h1 {{ margin: 0; font-size: 82px; line-height: 1.04; font-weight: 800;
    letter-spacing: -0.035em; }}
  p {{ margin: 0; font-size: 30px; color: #e2cbbd; }}
  .url {{ color: #f2a27f; font-weight: 700; }}
</style></head><body>
  <div class="brand">{LOGO}<span>AI for Scientists</span></div>
  <h1>Delegate what<br>you can check.</h1>
  <p>Recipes for giving research tasks to agents. <span class="url">aiforscientists.eu</span></p>
</body></html>"""

with tempfile.TemporaryDirectory() as tmp:
    src = Path(tmp) / "card.html"
    src.write_text(HTML)
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--hide-scrollbars",
            "--window-size=1200,630",
            f"--user-data-dir={tmp}/profile",
            f"--screenshot={OUT}",
            src.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
print(f"wrote {OUT}")
