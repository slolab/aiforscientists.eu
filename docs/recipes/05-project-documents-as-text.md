---
title: Keep project documents as plain text in the repository
nav_title: "Keep project documents as text"
recipe_id: R-05
status: tried
stage: Design
verifiability: Expert-checkable
autonomy: Proposes changes as pull requests
first_added: 2026-09-25
last_reviewed: 2026-09-25
skills:
  - name: package-to-skill
    does: turns the documentation of a software package into a skill an agent can load.
practices:
  - title: Write documentation and data for agents
    slug: 05-documentation-and-data-for-agents
    note: the same rule, applied to a lab.
tags: [Design, Expert-checkable]
---

<!-- RECIPE_TITLE -->

## Summary

An agent can only use information it can read.
It cannot read slides, chat threads, or what people remember.
Keep specs, notes and designs as plain text in the repository where the agent works.

## Steps

1. Add a `docs/` folder to every repository, with specs, meeting notes, transcripts and links to related repositories.
2. Write model assumptions and experimental designs in Markdown.
3. Let people and agents propose changes to them as pull requests.
4. Choose tools that store content as Markdown and can be used from the command line.

## How to check the output

A person reviews each pull request that changes a design or an assumption.

## Examples

- One lab moved its notes to a tool that stores everything as Markdown and works from the command line.
- Another lab gives tasks to its cluster agent only through issues in its code repository, and reviews every pull request the agent opens.

## Known problems

- If nobody updates the `docs/` folder, the agent works from an old plan.
  Date the notes, and delete what is no longer true.

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-09-25: First draft, from the first round-table.
