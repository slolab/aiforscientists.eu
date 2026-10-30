---
title: Let the cost of checking decide how much freedom an agent gets
nav_title: "Let checking cost set freedom"
recipe_icon: scale-balance
try: "Start with tasks a machine can check, such as tests that must pass or numbers that must match."
recipe_id: R-06
status: tried
stage: Implement with agents
verifiability: Machine-checkable
autonomy: Works alone; cannot change the code
first_added: 2026-09-25
last_reviewed: 2026-10-30
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
tags: [Implement with agents, Machine-checkable]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

The freedom an agent gets should depend less on how hard a task is and more on how cheaply its output can be checked.
The clearest successes came where checking was nearly free.
Analysis, experimental design and writing are much harder to check, so agents get less freedom there: they draft, and people check almost everything.

Give agents more freedom in three steps:

1. Tasks that a script can check.
2. Running experiments on tested code that the agent cannot change.
3. Writing new code, with a person reviewing every change.

Move to the next step only when the current one works.

## Steps

1. Tag a release of tested code and give the agent read-only access to it.
2. Let the agent start GPU experiments, collect the results and keep a log of each run.
3. Let an agent watch cluster jobs, read the logs of runs that crashed, fix trivial errors, resubmit, and log each change.
   Set a limit on the number of resubmissions.
4. For code that is rewritten to run faster, such as GPU kernels for large training runs, let the agent test and refine it in a loop.
   Each version must return the same numbers as the reference code.

## How to check the output

In the first two steps a script does the check: the code is unchanged, the rewritten code returns the same numbers, and the run log lists each resubmission and its cause.
In the third step a person reviews each change before it is merged.

## Examples

- One group lets agents run thousands of experiments on fixed code.
  Within those limits, the agent found better model settings than the group had found by hand.
- With an agent monitoring its cluster jobs, one group went from tens of runs to hundreds.
- In protein language model training, an agent implements about ten published methods a day.
  A benchmark scores each one, and a person decides which to keep.

## Known problems

- An agent that resubmits jobs can use up a shared quota.
  Set a limit on the number of runs.
- When agents move from running code to writing it, they can change a method without anyone noticing.
  See [What went wrong](failures.md#silent-cross-validation-change) and [recipe 8](08-pin-down-the-method.md).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: Renumbered to follow point 6 of the submitted Comment (formerly "Run experiments on fixed code").
- 2026-10-28: Updated to match the presubmission draft of the Comment.
- 2026-09-25: Updated to match the first full draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
