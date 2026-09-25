---
title: Let agents run experiments on code they cannot change
nav_title: "Run experiments on fixed code"
recipe_id: R-02
status: tried
stage: Run
verifiability: Machine-checkable
autonomy: Works alone; cannot change the code
first_added: 2026-09-25
last_reviewed: 2026-09-25
skills:
  - name: job-babysitter
    does: watches cluster jobs, resubmits failed runs, and logs each change.
practices:
  - title: Govern agent autonomy and accountability
    slug: 04-govern-autonomy-and-accountability
    note: read-only code limits what the agent can do.
  - title: State human-in-the-loop requirements
    slug: 09-human-in-the-loop
    note: each of the three levels below has a different human check.
tags: [Run, Machine-checkable]
---

<!-- RECIPE_TITLE -->

## Summary

Give agents more freedom in three steps:

1. Tasks that a script can check.
2. Running experiments on tested code that the agent cannot change.
3. Writing new code, with a person reviewing every change.

Move to the next step only when the current one works.

## Steps

1. Tag a release of tested code and give the agent read-only access to it.
2. Let the agent start GPU experiments, collect the results and keep a log of each run.
3. For large training runs, let the agent write custom GPU kernels.
   Test each kernel by checking that it returns the same numbers as the reference code.

## How to check the output

In the first two steps a script does the check: the code is unchanged, the kernel returns the same numbers, and the run log is complete.
In the third step a person reviews each change before it is merged.

## Examples

- A hyperparameter search by an agent, on fixed code, found better settings than students and group leaders had chosen.
- In protein language model training, an agent implements about ten published methods a day.
  A benchmark scores each one, and a person decides which to keep.

## Known problems

- When agents move from running code to writing it, they can change a method without anyone noticing.
  See [What went wrong](failures.md#silent-cross-validation-change).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-09-25: First draft, from the first round-table.
