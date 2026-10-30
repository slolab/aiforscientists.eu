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

## What group leaders accept without checking

In a survey at the Helmholtz Munich Computational Health Center, 36 of about 45 group leaders said which of 12 research steps they had given to agents in the previous three months, and for which steps they would accept the output without checking it again.

- Every respondent had given at least one step to agents.
  The most common were literature search (94%), writing (89%) and analysis (83%).
- Only 9% of all delegations came with a willingness to accept the output unchecked.
  64% of respondents would not accept unchecked output for any step.
- Nobody accepted unchecked analysis, experimental design or peer review.
- The least common were administration (53%), teaching (42%) and lab management (39%).
- The steps most often accepted unchecked were running computing jobs (17%) and literature search (14%).
  Both are quick to check.
- 31% had seen an agent error reach a shared result.
  For 8%, the error was caught only by a co-author or reviewer.
- The median respondent estimated saving 3 to 5 hours a week.
- 78% said that agents had changed which projects they start.
- The most common obstacle was time to learn (53%).

<!-- FIGURE: survey -->

These are self-reports from one centre with a computational focus.

## How much freedom to give an agent

<!-- FIGURE: quadrants -->

- **Delegate.** Start with the underused tasks. If the output is easy to check and agents are not doing the task yet, start there.
- **Add checks.** Before giving agents more freedom on a risky task, make its output checkable. Add tests, metrics and datasets until the output is easy to check.

## Three steps of freedom

1. Tasks that a script can check.
2. Running experiments on tested code that the agent cannot change.
3. Writing new code, with a person reviewing every change.

[Let checking cost set freedom](../recipes/06-let-checking-cost-decide.md) shows these steps in practice.
Some decisions stay with people even when checking is easy.
See [Where to draw the line](limits.md).
