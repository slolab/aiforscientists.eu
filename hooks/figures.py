"""MkDocs hook: draw the site's figures as inline SVG at build time.

- `<!-- FIGURE: survey -->` becomes a bar chart of the group-leader survey,
  from docs/assets/data/survey.yml, followed by the same numbers as a table.
- `<!-- FIGURE: quadrants -->` becomes the "how far to let agents run" chart:
  how cheaply output can be checked against how much autonomy an agent gets.

The SVGs are inline, not <img>, so their text is searchable and each bar's
<title> shows as a tooltip. Colours come from CSS classes in recipes.css.
"""

from html import escape
from pathlib import Path

import yaml

SURVEY = "<!-- FIGURE: survey -->"
QUADRANTS = "<!-- FIGURE: quadrants -->"


def _survey(config):
    data = yaml.safe_load(
        (Path(config["docs_dir"]) / "assets/data/survey.yml").read_text("utf-8")
    )
    n = data["respondents"]
    width, bar_w, bar_h, row_h, head_h = 640, 470, 10, 40, 34
    x0 = 0
    rows, y = [], 52
    for group in data["groups"]:
        k = group["key"]
        rows.append(
            f'<text class="afs-fig__group afs-fig__group--{k}" x="{x0}" y="{y + 14}">'
            f'{escape(group["name"].upper())}</text>'
        )
        y += head_h
        for s in group["steps"]:
            h, u = s["handed"], s["unchecked"]
            hw = bar_w * h / 100
            uw = bar_w * u / 100
            tip = (
                f'{s["step"]}: {h}% handed at least partly to agents, '
                f"{u}% would accept the output without re-checking (n = {n})"
            )
            by = y + 18
            bars = f'<rect class="afs-fig__bar--{k}-light" x="{x0}" y="{by}" width="{hw:.1f}" height="{bar_h}" rx="3"/>'
            if u:
                # Dark segment from the baseline, with a 2px surface gap before
                # the light remainder.
                bars += (
                    f'<rect class="afs-fig__gap" x="{x0 + uw:.1f}" y="{by}" width="2" height="{bar_h}"/>'
                    f'<rect class="afs-fig__bar--{k}" x="{x0}" y="{by}" width="{uw:.1f}" height="{bar_h}" rx="3"/>'
                )
            value = f'<tspan class="afs-fig__strong">{h}%</tspan>'
            if u:
                value += f'<tspan dx="6">{u}% unchecked</tspan>'
            rows.append(
                f'<g class="afs-fig__row"><title>{escape(tip)}</title>'
                f'<rect class="afs-fig__hit" x="0" y="{y}" width="{width}" height="{row_h}"/>'
                f'<text class="afs-fig__label" x="{x0}" y="{y + 12}">{escape(s["step"])}</text>'
                f"{bars}"
                f'<text class="afs-fig__value" x="{x0 + hw + 8:.1f}" y="{by + 9}">{value}</text>'
                "</g>"
            )
            y += row_h
        y += 8
    grid = "".join(
        f'<line class="afs-fig__grid" x1="{x0 + bar_w * p / 100}" x2="{x0 + bar_w * p / 100}" y1="52" y2="{y - 8}"/>'
        f'<text class="afs-fig__tick" x="{x0 + bar_w * p / 100}" y="{y + 8}" text-anchor="middle">{p}%</text>'
        for p in (25, 50, 75, 100)
    )
    legend = (
        '<g class="afs-fig__legend">'
        '<rect class="afs-fig__bar--doing-light" x="0" y="8" width="12" height="10" rx="2"/>'
        '<rect class="afs-fig__bar--running-light" x="14" y="8" width="12" height="10" rx="2"/>'
        '<text x="32" y="17">handed at least partly to agents</text>'
        '<rect class="afs-fig__bar--doing" x="0" y="28" width="12" height="10" rx="2"/>'
        '<rect class="afs-fig__bar--running" x="14" y="28" width="12" height="10" rx="2"/>'
        '<text x="32" y="37">would accept without re-checking</text>'
        "</g>"
    )
    height = y + 16
    svg = (
        f'<svg class="afs-fig afs-fig--survey" viewBox="0 0 {width} {height}" role="img" '
        f'aria-labelledby="afs-survey-title">'
        f'<title id="afs-survey-title">Research steps handed to agents, and accepted unchecked, '
        f"by {n} group leaders</title>"
        f'{grid}{legend}{"".join(rows)}</svg>'
    )
    table = [
        "| Step | Handed to agents | Accepted unchecked |",
        "|---|---|---|",
    ]
    for group in data["groups"]:
        for s in group["steps"]:
            table.append(f'| {s["step"]} ({group["name"].lower()}) | {s["handed"]}% | {s["unchecked"]}% |')
    return (
        f'<figure class="afs-figure" markdown="0">{svg}'
        f"<figcaption>Share of {n} group leaders who had handed each research step at least partly to agents in the previous three months, "
        "and who would accept the output without re-checking. Hover a bar for its numbers.</figcaption></figure>\n\n"
        '??? note "The same numbers as a table"\n\n'
        + "\n".join("    " + line for line in table)
        + "\n"
    )


# Quadrant contents: (title, css key, items). Each item is (text, kind), where
# kind is "doing", "running" or "risk" (an observed failure or risk).
_QUADRANTS = [
    ("Danger zone", "danger", [
        ("silent method change", "risk"),
        ("metric gaming", "risk"),
        ("out-of-bounds data access", "risk"),
    ]),
    ("Automate", "automate", [
        ("speeding up verified code", "doing"),
        ("restarting failed jobs", "doing"),
        ("expense claims", "running"),
    ]),
    ("Keep human", "human", [
        ("new hypotheses", "doing"),
        ("review verdicts", "doing"),
        ("decisions about people", "running"),
    ]),
    ("Underused", "underused", [
        ("sourced literature tables", "doing"),
        ("pre-submission checks", "doing"),
        ("grant and staff overviews", "running"),
    ]),
]


def _quadrants():
    left, top, cell_w, cell_h, gap = 34, 8, 292, 178, 12
    cells = []
    for i, (title, key, items) in enumerate(_QUADRANTS):
        col, row = i % 2, i // 2
        x = left + col * (cell_w + gap)
        y = top + row * (cell_h + gap)
        dash = ' stroke-dasharray="6 5"' if key == "underused" else ""
        body = [
            f'<rect class="afs-fig__cell afs-fig__cell--{key}" x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="12"{dash}/>',
            f'<text class="afs-fig__qtitle afs-fig__qtitle--{key}" x="{x + 18}" y="{y + 30}">{title.upper()}</text>',
        ]
        for j, (text, kind) in enumerate(items):
            iy = y + 66 + j * 34
            if kind == "risk":
                body.append(f'<circle class="afs-fig__ring" cx="{x + 24}" cy="{iy - 5}" r="5.5"/>')
            else:
                body.append(f'<circle class="afs-fig__dot--{kind}" cx="{x + 24}" cy="{iy - 5}" r="6"/>')
            body.append(f'<text class="afs-fig__item" x="{x + 40}" y="{iy}">{escape(text)}</text>')
        cells.append("".join(body))
    right = left + 2 * cell_w + gap
    bottom = top + 2 * cell_h + gap
    mid_y = top + cell_h
    arrows = (
        # Danger zone to Automate: make the output checkable.
        f'<line class="afs-fig__move" x1="{left + cell_w - 90}" y1="{mid_y - 26}" x2="{left + cell_w + gap + 96}" y2="{mid_y - 26}" marker-end="url(#afs-arrow)"/>'
        f'<rect class="afs-fig__pill" x="{left + cell_w - 46}" y="{mid_y - 40}" width="104" height="28" rx="14"/>'
        f'<text class="afs-fig__pilltext" x="{left + cell_w + 6}" y="{mid_y - 21}" text-anchor="middle">add checks</text>'
        # Underused to Automate: hand the task over.
        f'<line class="afs-fig__move" x1="{right - 56}" y1="{mid_y + gap + 70}" x2="{right - 56}" y2="{mid_y - 34}" marker-end="url(#afs-arrow)"/>'
        f'<rect class="afs-fig__pill" x="{right - 106}" y="{mid_y - 8}" width="100" height="28" rx="14"/>'
        f'<text class="afs-fig__pilltext" x="{right - 56}" y="{mid_y + 11}" text-anchor="middle">hand over</text>'
    )
    axes = (
        f'<line class="afs-fig__axis" x1="12" y1="{bottom}" x2="12" y2="{top + 4}" marker-end="url(#afs-arrow-axis)"/>'
        f'<text class="afs-fig__axislabel" transform="translate(24 {top + cell_h + gap / 2}) rotate(-90)" text-anchor="middle">More autonomy for the agent</text>'
        f'<line class="afs-fig__axis" x1="{left}" y1="{bottom + 22}" x2="{right}" y2="{bottom + 22}" marker-end="url(#afs-arrow-axis)"/>'
        f'<text class="afs-fig__axislabel" x="{(left + right) / 2}" y="{bottom + 44}" text-anchor="middle">Cheaper to check the output</text>'
    )
    ly = bottom + 74
    legend = (
        f'<g class="afs-fig__legend">'
        f'<circle class="afs-fig__dot--doing" cx="{left + 6}" cy="{ly - 5}" r="6"/><text x="{left + 18}" y="{ly}">doing research</text>'
        f'<circle class="afs-fig__dot--running" cx="{left + 156}" cy="{ly - 5}" r="6"/><text x="{left + 168}" y="{ly}">running research</text>'
        f'<circle class="afs-fig__ring" cx="{left + 316}" cy="{ly - 5}" r="5.5"/><text x="{left + 328}" y="{ly}">observed failure or risk</text>'
        "</g>"
    )
    defs = (
        "<defs>"
        '<marker id="afs-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path class="afs-fig__arrowhead" d="M0 0 L10 5 L0 10 z"/></marker>'
        '<marker id="afs-arrow-axis" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path class="afs-fig__axishead" d="M0 0 L10 5 L0 10 z"/></marker>'
        "</defs>"
    )
    width, height = right + 4, ly + 10
    svg = (
        f'<svg class="afs-fig afs-fig--quadrants" viewBox="0 0 {width} {height}" role="img" aria-labelledby="afs-quad-title afs-quad-desc">'
        '<title id="afs-quad-title">How far to let agents run</title>'
        '<desc id="afs-quad-desc">Four quadrants. Hard to check with high autonomy: danger zone (silent method change, metric gaming, out-of-bounds data access). '
        "Easy to check with high autonomy: automate (speeding up verified code, restarting failed jobs, expense claims). "
        "Hard to check with low autonomy: keep human (new hypotheses, review verdicts, decisions about people). "
        "Easy to check, not yet handed over: underused (sourced literature tables, pre-submission checks, grant and staff overviews). "
        "Arrows: add checks moves work from the danger zone to automate; hand over moves work from underused to automate.</desc>"
        f'{defs}{"".join(cells)}{arrows}{axes}{legend}</svg>'
    )
    return (
        f'<figure class="afs-figure" markdown="0">{svg}'
        "<figcaption>How far to let agents run: how cheaply their output can be checked, against how much autonomy they get. "
        "Rings mark failures and risks observed at the centre. The arrows show the two recommended moves.</figcaption></figure>"
    )


def on_page_markdown(markdown, page, config, files):
    if SURVEY in markdown:
        markdown = markdown.replace(SURVEY, _survey(config))
    if QUADRANTS in markdown:
        markdown = markdown.replace(QUADRANTS, _quadrants())
    return markdown
