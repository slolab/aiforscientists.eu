---
title: Pin down the method before the agent starts, and watch for drift
nav_title: "Pin down the method"
recipe_icon: pin-outline
try: "Write the specification, including the evaluation, before any code, and have a second person read the evaluation code."
recipe_id: R-08
status: tried
stage: Implement with agents
verifiability: Hard to verify
autonomy: Implements a written specification in small steps; a second person reviews the evaluation
first_added: 2026-09-25
last_reviewed: 2026-10-30
skills:
  - name: public-data-qc
    does: downloads, deduplicates and checks public datasets, with a report for each step.
practices:
  - title: Evaluate tools before trust
    slug: 08-evaluate-tools-before-trust
    note: a second reviewer checks each method change.
tags: [Implement with agents, Hard to verify]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

The hardest errors to catch are small changes to a method that still look correct.
An agent asked to implement a plan can deliver something close to, but not exactly, what was planned.
Such deviations are easy to miss in evaluation code, and they can change results considerably if they accumulate.
Familiar engineering habits, such as test-driven development, help when they are applied more strictly.

## Steps

1. Work out a written specification with the agent before any code exists.
   Include the evaluation protocol: data splits, metrics and seeds.
2. Discuss the specification with colleagues.
3. Write the tests before the code.
4. Let the agent implement in steps small enough to read.
   When an agent changes too much at once, nobody can follow what happened, which creates technical and cognitive debt.
5. Ask someone other than the person who prompted the agent to review the evaluation code.

## How to check the output

A second person compares the evaluation code with the written specification.
Tests written before the code must pass.
Each change is small enough to read in full.

## Examples

- An agent asked to implement an analysis for a paper changed how the cross-validation was done.
  The code ran, the paper's result shifted slightly, and an attentive co-author noticed only much later.
  It was one of several cases where an agent delivered something close to, but not exactly, what was planned.
- Groups that build software with agents now write the specification with the agent first, and include the evaluation protocol in it.

## Known problems

- Large pull requests contain changes that no reviewer reads in full.
- The person who prompted the agent tends to read the code as what they asked for, not as what it does.
- In the centre's survey, 31% of group leaders had seen an agent error reach a shared result.

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: Renumbered to follow point 8 of the submitted Comment (formerly "Review methods, limit file access").
  The sandbox and folder-permission steps moved to [recipe 2](02-establish-guardrails.md).
- 2026-10-28: Updated to match the presubmission draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
