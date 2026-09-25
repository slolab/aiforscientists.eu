---
title: Review every method change, and limit what agents can write to
nav_title: "Review methods, limit file access"
recipe_id: R-09
status: tried
stage: Design
verifiability: Hard to verify
autonomy: Sandboxed; a second person reviews method changes
first_added: 2026-09-25
last_reviewed: 2026-09-25
skills:
  - name: public-data-qc
    does: downloads, deduplicates and checks public datasets, with a report for each step.
practices:
  - title: Govern agent autonomy and accountability
    slug: 04-govern-autonomy-and-accountability
    note: a sandbox and a list of allowed paths limit what the agent can do.
  - title: Evaluate tools before trust
    slug: 08-evaluate-tools-before-trust
    note: a second reviewer checks each method change.
tags: [Design, Hard to verify]
---

<!-- RECIPE_TITLE -->

## Summary

The hardest errors to catch are small changes to a method that still look correct.
A second risk is shared storage that was set up before agents existed and lets anyone write anywhere.

## Steps

1. Write the spec first, and keep pull requests small so a reviewer can read every change.
2. Ask a co-author to check any method an agent changed: data splits, metrics and seeds.
3. Run agents in a sandbox with a fixed list of paths they may write to.
4. Check which shared folders anyone can write to, and check that they are backed up.

## How to check the output

A second person reviews method changes.
File permissions and backups are checked at regular intervals.

## Examples

- An agent changed a cross-validation scheme, and a paper's main result changed with it.
  Only a co-author noticed.
- On one shared cluster, many group folders could be written to by any user, and none were backed up.

## Known problems

- Large pull requests contain changes that no reviewer reads in full.

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-09-25: First draft, from the first round-table.
