# aiforscientists.eu (demo)

Source for a demo of aiforscientists.eu: recipes and skills for giving research tasks to agents.
It is a companion to [aiforscience.eu](https://aiforscience.eu), which collects best practices for agentic AI in science.
Each recipe links to the practices it follows.

This build is a demo.
Names and details are removed from all examples, and skill and repository links are placeholders.

## Development

```sh
uv sync
uv run mkdocs serve          # preview at http://127.0.0.1:8000
uv run mkdocs build --strict
```

Recipe pages are in `docs/recipes/NN-slug.md`.
`hooks/recipe_pages.py` builds each recipe's title, skills and related practices from the page's frontmatter.
The theme is copied from aiforscience.eu (`overrides/`, `docs/assets/css/home.css`).
