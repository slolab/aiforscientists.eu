---
title: Prototype an idea before you hand it to a student
nav_title: "Prototype before assigning"
recipe_icon: lightbulb-on-outline
try: "Ask an agent to grill the project plan and build a minimal prototype on data you already have."
recipe_id: R-05
status: tried
stage: Think with agents
verifiability: Expert-checkable
autonomy: Drafts; a person decides
first_added: 2026-09-25
last_reviewed: 2026-10-30
skills:
  - name: grill-me
    does: asks questions about a project description until its assumptions, data and success criteria are written down.
practices:
  - title: Match the method to the task
    slug: 01-match-method-to-task
    note: the prototype shows whether the project can work.
tags: [Think with agents, Expert-checkable]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

Before giving a project to a student, ask an agent to question the project description and build a small prototype on data the group already has.
If the prototype shows no result, the project is not ready.
The check is quick, and it can save a student months on a project that the data cannot support.
It also filters the many plausible ideas that agents produce.

## Steps

1. Write the project description as you would for a student.
2. Ask the agent to "grill me on it": what is assumed, which data will be used, and what counts as success.
3. Revise the description.
4. Ask the agent for a small prototype on existing data.
5. If the prototype finds nothing on existing data, do not assign the project yet.

## How to check the output

The group leader reads the prototype code and results, as for a rotation student's work.
The group leader checks that the result is real.
Code quality does not matter at this stage.

## Examples

- One group leader now tests every student project this way.
- Another asked an agent whether an old exponential-time algorithm could now be solved.
  It could not. The answer took days instead of months.

## Known problems

- The check works only when suitable data exist.
  A quick prototype can miss what a careful study would find.
- A prototype can look good and still use test data for training.
  Check the data split first.
- If every project arrives already tested, students miss the early exploratory work.
  See [Where to draw the line](../guide/limits.md#students-learning).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: Renumbered to follow point 5 of the submitted Comment (formerly "Test projects before assigning them").
- 2026-10-28: Updated to match the presubmission draft of the Comment.
- 2026-09-25: Updated to match the first full draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
