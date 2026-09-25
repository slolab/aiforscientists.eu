---
title: Define a problem as metrics and datasets, and let an agent search for methods
nav_title: "Let agents search for methods"
recipe_id: R-01
status: tried
stage: Analyze results
verifiability: Machine-checkable
autonomy: Works alone against a fixed benchmark
first_added: 2026-09-25
last_reviewed: 2026-09-25
skills: []
practices:
  - title: Evaluate tools before trust
    slug: 08-evaluate-tools-before-trust
    note: build the benchmark before the agent uses it.
  - title: Match the method to the task
    slug: 01-match-method-to-task
    note: an agent search only makes sense if there is a metric.
tags: [Analyze results, Machine-checkable]
---

<!-- RECIPE_TITLE -->

## Summary

Write the research question as a metric, several datasets and a baseline.
Then let an agent try methods: parameter sweeps, rewritten methods, or a search over code variants.
The benchmark scores each attempt, so the agent does not need to be told which method to use.
The quality of the problem definition limits the results more than the agent does.

## Steps

1. Pick a problem with data you already have.
2. Write the metric and the evaluation script before the agent starts.
3. Use at least three datasets, so that a result that only works on one of them is visible.
4. Run a baseline method, so each result can be compared with it.
5. Do not give the agent write access to the evaluation code.
6. Move to harder problems only when results on the first one are stable.

## How to check the output

The benchmark scores each result.
A person checks the benchmark itself: are the splits, metrics and seeds the ones written down in step 2?
Is the baseline result correct?
A result that improves only one dataset does not count.

## Examples

- Agents added methods to a public benchmark and found which method parameters matter most.
- One group plans to run its own code-search system instead of using an external provider.

## Known problems

- With one dataset, an agent improved a metric by changing random seeds and small parameters. See [What went wrong](failures.md#metric-hacking).
- An agent that can edit the evaluation code can change what is being measured.

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-09-25: Updated to match the first full draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
