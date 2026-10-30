"""MkDocs hook: render skill pages and their briefs from frontmatter.

Each skill lives in docs/skills/<name>.md, and its content lives only in the
page's frontmatter. Most skills depend on local details (the institute's forms,
the cluster's scheduler, the folders an agent may use), so the site publishes a
brief instead of one institute's skill. The brief separates what is general
from the questions only a local user can answer, and is written to be handed
to a skill-creation tool, which asks those questions and builds a local
version.

- `<!-- SKILL_PAGE -->` on a skill page becomes the page body, including the
  brief as one copyable block.
- `<!-- SKILL_TABLE -->` on docs/skills/index.md becomes the list of skills.
- Each brief is also written to site/skills/<name>/brief.md, so an agent can
  fetch it by URL.
"""

import re
from pathlib import Path

import yaml

PAGE = "<!-- SKILL_PAGE -->"
TABLE = "<!-- SKILL_TABLE -->"
SKILL_PAGE = re.compile(r"skills/(?!index\.md$)[^/]+\.md$")
SITE = "https://aiforscientists.eu"

CHECK_LABELS = {
    "machine": "Machine-checkable",
    "expert": "Expert-checkable",
    "hard": "Hard to verify",
}

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def _recipe_title(docs_dir, recipe):
    meta = _load_meta(docs_dir / "recipes" / f"{recipe}.md")
    return meta.get("nav_title") or meta.get("title") or recipe


def _check_badge(level):
    return (
        f'<span class="afs-check afs-check--{level}">{CHECK_LABELS[level]}</span>'
    )


def _bullets(items):
    return "\n".join(f"- {item}" for item in items)


def _numbered(items):
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))


def _brief(meta, recipe_title):
    """The text a reader copies and gives to a skill-creation tool."""
    name = meta["skill"]
    return "\n".join(
        [
            f"# Skill brief: {name}",
            "",
            f"Source: {SITE}/skills/{name}/",
            f"Recipe: {recipe_title} ({SITE}/recipes/{meta['recipe']}/)",
            "",
            "Build a skill for my own setting from this brief.",
            "If you have a skill-creation skill or tool, use it.",
            'Before you write anything, ask me each question under "Local details", one at a time.',
            "Do not guess an answer; if I do not know one, leave a marked TODO in the skill.",
            'Keep every rule under "Never" in the skill you write.',
            'Write the check under "How to check the output" into the skill, so that it runs every time.',
            'Then run the skill once on the test case and show me the result.',
            "",
            "## Purpose",
            "",
            meta["does"],
            "",
            "## Inputs",
            "",
            _bullets(meta["inputs"]),
            "",
            "## Output",
            "",
            _bullets(meta["outputs"]),
            "",
            "## Steps",
            "",
            _numbered(meta["steps"]),
            "",
            "## Local details",
            "",
            _numbered(meta["local"]),
            "",
            "## Never",
            "",
            _bullets(meta["never"]),
            "",
            "## How to check the output",
            "",
            meta["check"],
            "",
            "## Test case",
            "",
            meta["test"],
        ]
    )


def _render_page(meta, docs_dir):
    recipe_title = _recipe_title(docs_dir, meta["recipe"])
    status = meta.get("status", "brief")
    lines = [
        f"# `{meta['skill']}`",
        "",
        meta["does"],
        "",
        f"- **Recipe:** [{recipe_title}](../recipes/{meta['recipe']}.md)",
        f"- **Output check:** {_check_badge(meta['check_level'])} {meta['check']}",
        f'- **Status:** <span class="afs-badge afs-badge--{status}">{status}</span>',
        "",
        "## Make your own version",
        "",
        "This skill depends on local details, so the site publishes a brief instead of one institute's skill.",
        "Copy the brief and give it to your agent.",
        "If your agent has a skill-creation skill, such as Anthropic's `skill-creator`, it will use it.",
        'The agent asks you the questions under "Local details", builds the skill, and runs it once on the test case.',
        "",
        f"An agent that can read web pages can also fetch the brief itself from <{SITE}/skills/{meta['skill']}/brief.md>.",
        "",
        '<div class="afs-brief" markdown>',
        "",
        "```markdown",
        _brief(meta, recipe_title),
        "```",
        "",
        "</div>",
        "",
        "## Local details",
        "",
        "Your version needs answers to these questions:",
        "",
        _numbered(meta["local"]),
        "",
        "## Never",
        "",
        _bullets(meta["never"]),
        "",
    ]
    examples = meta.get("versions") or []
    lines += ["## Local versions", ""]
    if examples:
        lines.append("Versions built from this brief, shared by their authors:")
        lines.append("")
        lines += [f"- [{v['who']}]({v['url']}): {v['note']}" for v in examples]
    else:
        lines.append("No local version is published yet.")
        lines.append(
            "If you built one, [share it](../about/contribute.md#contribute-a-skill) "
            "as an example for others."
        )
    return "\n".join(lines)


def _render_table(docs_dir):
    rows = [
        "| Skill | What it does | Recipe | Output check |",
        "|---|---|---|---|",
    ]
    for path in sorted((docs_dir / "skills").glob("*.md")):
        if path.name == "index.md":
            continue
        meta = _load_meta(path)
        recipe_title = _recipe_title(docs_dir, meta["recipe"])
        rows.append(
            f"| [`{meta['skill']}`]({path.name}) | {meta['does']} "
            f"| [{recipe_title}](../recipes/{meta['recipe']}.md) "
            f"| {_check_badge(meta['check_level'])} |"
        )
    return "\n".join(rows)


# Briefs collected in on_page_markdown, written in on_post_build. Cleared per
# build so `mkdocs serve` rebuilds do not keep stale briefs.
_BRIEFS = {}


def on_config(config):
    _BRIEFS.clear()
    return config


def on_page_markdown(markdown, page, config, files):
    docs_dir = Path(config["docs_dir"])
    if SKILL_PAGE.match(page.file.src_uri):
        meta = page.meta
        _BRIEFS[meta["skill"]] = _brief(
            meta, _recipe_title(docs_dir, meta["recipe"])
        )
        return markdown.replace(PAGE, _render_page(meta, docs_dir))
    if TABLE in markdown:
        return markdown.replace(TABLE, _render_table(docs_dir))
    return markdown


def on_post_build(config):
    site_dir = Path(config["site_dir"])
    for name, brief in _BRIEFS.items():
        out = site_dir / "skills" / name / "brief.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(brief + "\n", encoding="utf-8")
