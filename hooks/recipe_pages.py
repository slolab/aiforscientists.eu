"""MkDocs hook: keep recipe titles, skills and related practices spelled once.

Each recipe's title, skills and links to aiforscience.eu practices live only in
the recipe page's frontmatter. This hook renders them into the page body:

- `<!-- RECIPE_TITLE -->` becomes a "Recipe N" kicker plus the title as H1.
- `<!-- RECIPE_SKILLS -->` becomes the `## Skills` list from `skills:`.
- `<!-- RECIPE_PRACTICES -->` becomes the `## Related practices` list from
  `practices:`.
- Each recipe's sidebar label comes from its frontmatter `nav_title`.
"""

import re
from pathlib import Path

import yaml

TITLE = "<!-- RECIPE_TITLE -->"
SKILLS = "<!-- RECIPE_SKILLS -->"
PRACTICES = "<!-- RECIPE_PRACTICES -->"
RECIPE_PAGE = re.compile(r"recipes/(\d\d)-.*\.md$")
PRACTICE_BASE = "https://aiforscience.eu/best-practices/"

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def _render_skills(skills):
    lines = ["## Skills", ""]
    if not skills:
        lines.append("No skill yet. [Contribute one](../about/contribute.md).")
    for skill in skills:
        lines.append(
            f'- [`{skill["name"]}`](../skills.md#{skill["name"]}): {skill["does"]}'
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
    match = RECIPE_PAGE.match(page.file.src_uri)
    if not match:
        return markdown
    meta = page.meta
    kicker = f'<p class="afs-bp-kicker">Recipe {int(match.group(1))}</p>'
    markdown = markdown.replace(TITLE, f'{kicker}\n\n# {meta.get("title", "")}')
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
