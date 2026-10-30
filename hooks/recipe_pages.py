"""MkDocs hook: keep recipe titles, skills and related practices spelled once.

Each recipe's title, skills and links to aiforscience.eu practices live only in
the recipe page's frontmatter. This hook renders them into the page body:

- `<!-- RECIPE_TITLE -->` becomes a "Recipe N" kicker with the recipe's icon,
  the title as H1, and the `try:` line as "Try this first".
- `<!-- RECIPE_GRID -->` (on the recipes overview) becomes one card per recipe,
  grouped by `stage`, each with icon, title and `try:` line.
- `<!-- RECIPE_SKILLS -->` becomes the `## Skills` list from `skills:`.
- `<!-- RECIPE_PRACTICES -->` becomes the `## Related practices` list from
  `practices:`.
- Each recipe's sidebar label comes from its frontmatter `nav_title`.
"""

import re
from pathlib import Path

import material
import yaml

TITLE = "<!-- RECIPE_TITLE -->"
SKILLS = "<!-- RECIPE_SKILLS -->"
PRACTICES = "<!-- RECIPE_PRACTICES -->"
GRID = "<!-- RECIPE_GRID -->"
STAGES = ["Prepare for agents", "Think with agents", "Implement with agents"]
RECIPE_PAGE = re.compile(r"recipes/(\d\d)-.*\.md$")
PRACTICE_BASE = "https://aiforscience.eu/best-practices/"

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def _icon(config, name):
    """Inline SVG of a Material Design icon bundled with the theme."""
    if not name:
        return ""
    icons = Path(material.__file__).parent / "templates/.icons/material"
    path = icons / f"{name}.svg"
    svg = path.read_text(encoding="utf-8")
    return svg.replace("<svg ", '<svg aria-hidden="true" ', 1)


def _render_grid(config):
    docs_dir = Path(config["docs_dir"])
    recipes = []
    for path in sorted((docs_dir / "recipes").glob("[0-9][0-9]-*.md")):
        meta = _load_meta(path)
        recipes.append((int(path.name[:2]), path.name, meta))
    out = []
    for stage in STAGES:
        out.append(f"## {stage}\n")
        out.append('<div class="afs-recipe-grid" markdown="0">')
        for num, name, meta in recipes:
            if meta.get("stage") != stage:
                continue
            href = name[:-3] + "/"
            out.append(
                f'<a class="afs-recipe-card" href="{href}">'
                f'<span class="afs-recipe-card__icon">{_icon(config, meta.get("recipe_icon"))}</span>'
                f'<span class="afs-recipe-card__num">Recipe {num}</span>'
                f'<span class="afs-recipe-card__title">{meta.get("title", "")}</span>'
                f'<span class="afs-recipe-card__try"><strong>Try this:</strong> {meta.get("try", "")}</span>'
                "</a>"
            )
        out.append("</div>\n")
    return "\n".join(out)


def _render_skills(skills):
    lines = ["## Skills", ""]
    if not skills:
        lines.append("No skill yet. [Contribute one](../about/contribute.md#contribute-a-skill).")
    else:
        lines += [
            "Each skill page has a brief. Give it to your agent to build a version for your own institute.",
            "",
        ]
    for skill in skills:
        lines.append(
            f'- [`{skill["name"]}`](../skills/{skill["name"]}.md): {skill["does"]}'
        )
    return "\n".join(lines)


def _render_practices(practices):
    lines = [
        "## Related practices",
        "",
        "Best practices on [aiforscience.eu](https://aiforscience.eu) that this recipe follows:",
        "",
    ]
    for practice in practices:
        lines.append(
            f'- [{practice["title"]}]({PRACTICE_BASE}{practice["slug"]}/): '
            f'{practice["note"]}'
        )
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    if GRID in markdown:
        return markdown.replace(GRID, _render_grid(config))
    match = RECIPE_PAGE.match(page.file.src_uri)
    if not match:
        return markdown
    meta = page.meta
    icon = _icon(config, meta.get("recipe_icon"))
    kicker = (
        f'<p class="afs-bp-kicker afs-recipe-kicker">'
        f'<span class="afs-recipe-kicker__icon">{icon}</span>'
        f"Recipe {int(match.group(1))}</p>"
    )
    title = f'{kicker}\n\n# {meta.get("title", "")}'
    if meta.get("try"):
        title += (
            f'\n\n<p class="afs-try"><strong>Try this first.</strong> {meta["try"]}</p>'
        )
    markdown = markdown.replace(TITLE, title)
    markdown = markdown.replace(SKILLS, _render_skills(meta.get("skills") or []))
    markdown = markdown.replace(
        PRACTICES, _render_practices(meta.get("practices") or [])
    )
    return markdown


def on_nav(nav, config, files):
    docs_dir = Path(config["docs_dir"])
    for page in nav.pages:
        if RECIPE_PAGE.match(page.file.src_uri):
            label = _load_meta(docs_dir / page.file.src_uri).get("nav_title")
            if label:
                page.title = label
    return nav
