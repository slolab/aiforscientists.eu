# aiforscientists.eu

Source for [aiforscientists.eu](https://aiforscientists.eu): recipes for giving research tasks to AI agents, with skill briefs that an agent can turn into a version for your own institute.

The site accompanies the Comment "Delegate what you can check: ten lessons on AI agents in research" (Theis, F. J. & Helmholtz Munich Computational Health Center), submitted for publication.
Recipe *N* follows point *N* of the Comment.
It is maintained alongside [aiforscience.eu](https://aiforscience.eu), a living record of best practices for agentic AI in science, and each recipe links to the practices it follows.

## Development

```sh
uv sync
uv run mkdocs serve          # preview at http://127.0.0.1:8000
uv run mkdocs build --strict # run before every PR
```

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Recipe pages are in `docs/recipes/NN-slug.md`, skill briefs in `docs/skills/<name>.md`.
Page structure, frontmatter and writing rules are in [CLAUDE.md](CLAUDE.md).

## Contributing

What to contribute and through which route: [aiforscientists.eu/about/contribute](https://aiforscientists.eu/about/contribute/).
How to work in this repository: [CONTRIBUTING.md](CONTRIBUTING.md).
Everyone taking part is covered by the [code of conduct](CODE_OF_CONDUCT.md).

## Editors

- Fabian J. Theis (Computational Health Center, Helmholtz Munich)
- Sebastian Lobentanzer (Computational Health Center, Helmholtz Munich)

## License

Site configuration and code: [MIT](LICENSE).
Written content under `docs/`, including skill briefs: [CC-BY-4.0](LICENSE-CONTENT).
