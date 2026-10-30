# Contributing

What to contribute, and through which route, is on the site:
[aiforscientists.eu/about/contribute](https://aiforscientists.eu/about/contribute/).
Issue templates for adding an example, reporting an error, contributing a skill, proposing a recipe and disagreeing with one;
[Discussions](https://github.com/slolab/aiforscientists.eu/discussions) for anything open-ended;
the [AI for Science Google Group](https://groups.google.com/g/aiforscience) (aiforscience@googlegroups.com, subject starting with "aiforscientists") if you do not use GitHub.

This file covers working in the repository.

## Setup and checks

See [Development](README.md#development).
The strict build runs on every pull request ([`.github/workflows/ci.yaml`](.github/workflows/ci.yaml)).
Run it before you push:

```sh
uv run mkdocs build --strict   # fails on broken internal links
```

## Conventions

[CLAUDE.md](CLAUDE.md) is the source for recipe and skill frontmatter, page structure and the writing rules.
Follow it by hand or give it to an agent.

## Branches and pull requests

Branch off `main`, one topic per branch, and open a pull request.
Do not push to `main`: every push to `main` deploys the site.
The [pull request template](.github/pull_request_template.md) lists what a reviewer checks.

## Names and confidential material

Examples are published without names unless the contributor asks to be named.
Never commit personal data, patient data, confidential results, manuscripts under review, or institute-internal forms.
Manuscript drafts (`*.docx`, `*.pdf`) are ignored by git for this reason.

## Licensing your contribution

Opening a pull request offers the change under the repository's licences:
[MIT](LICENSE) for site configuration and code, [CC-BY-4.0](LICENSE-CONTENT) for content under `docs/`.
You keep copyright in what you write.
