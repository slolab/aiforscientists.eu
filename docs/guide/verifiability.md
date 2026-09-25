---
title: Delegate by verifiability
---

# Delegate by verifiability

Give agents the work whose output is quick and cheap to check.
Every recipe on this site follows this rule.

Agents worked well when checking was cheap.
Examples: a GPU kernel must return the same numbers as the reference code, a reimbursement form must add up, and an agent that only runs fixed code cannot change it.
Agents caused problems when checking was expensive.
Examples: a cross-validation scheme changed without anyone noticing, a metric improved by tuning random seeds, and many hypotheses that sounded right but could not be tested quickly.

## Three levels of checking

| Level | What checks the output | Examples |
|---|---|---|
| <span class="afs-check afs-check--machine">Machine-checkable</span> | A test, a sum, or a comparison of numbers | Custom kernels, job monitoring, reimbursement forms, format checks |
| <span class="afs-check afs-check--expert">Expert-checkable</span> | A person with the right knowledge | Literature tables with sources, project prototypes, draft reviews |
| <span class="afs-check afs-check--hard">Hard to verify</span> | Nothing yet | New hypotheses, method changes inside an analysis |

Each recipe shows its level in the box "About this recipe".

## How much freedom to give an agent

<div class="afs-quadrants" markdown="0">
  <div class="afs-quadrant afs-quadrant--danger">
    <strong>Danger zone</strong>
    <p>Hard to check, high freedom. All reported errors happened here: changed methods, tuned seeds, open folders.</p>
  </div>
  <div class="afs-quadrant afs-quadrant--automate">
    <strong>Automate</strong>
    <p>Easy to check, high freedom. Custom kernels, experiments on fixed code, job monitoring, reimbursement forms.</p>
  </div>
  <div class="afs-quadrant afs-quadrant--human">
    <strong>Keep human</strong>
    <p>Hard to check, low freedom. New hypotheses, peer-review judgments, decisions about people.</p>
  </div>
  <div class="afs-quadrant afs-quadrant--underused">
    <strong>Underused</strong>
    <p>Easy to check, not yet given to agents. Most administration, literature tables, pre-submission checks.</p>
  </div>
</div>
<p class="afs-quadrants__axes">Left to right: harder to easier to check. Bottom to top: less to more freedom for the agent.</p>

- **Start with the underused tasks.** If the output is easy to check and agents are not doing the task yet, start there.
- **Make risky tasks checkable before giving agents more freedom.** Add tests, metrics and datasets until the output of a task is easy to check.

## Three steps of freedom

1. Tasks that a script can check.
2. Running experiments on tested code that the agent cannot change.
3. Writing new code, with a person reviewing every change.

[Run experiments on fixed code](../recipes/02-run-experiments-on-fixed-code.md) shows these steps in practice.
Some decisions stay with people even when checking is easy.
See [Where to draw the line](limits.md).
