---
title: What went wrong
---

# What went wrong

Errors reported with the recipes, with names and details removed.
Each entry says what happened, how it was found, and which recipe now prevents it.
[Report an error](../about/contribute.md).

## Changed cross-validation { #silent-cross-validation-change }

**What happened.** An agent that had been asked to implement an analysis for a paper changed how the cross-validation was done.
The code ran, and the paper's result shifted slightly.

**How it was found.** A co-author noticed, much later.

**Recipes that prevent it.** [Pin down the method](08-pin-down-the-method.md), [Let checking cost set freedom](06-let-checking-cost-decide.md).

## Metric improved by tuning seeds { #metric-hacking }

**What happened.** An automated optimization improved a metric by changing random seeds and small parameters.

**How it was found.** The improvement did not appear on other datasets.

**Recipes that prevent it.** [Make problems checkable](07-checkable-problems.md), which requires at least three datasets per problem.

## Folders anyone could write to { #open-folders }

**What happened.** On a shared cluster, many group folders could be written to by any user, and the data were too large to back up.
One wrong agent job could have deleted a group's data.

**How it was found.** A check of folder permissions on the cluster.

**Recipes that prevent it.** [Establish guardrails](02-establish-guardrails.md).

## Agent read a folder before it was allowed to { #folder-instructions }

**What happened.** A user told an agent it could now look at a second folder.
The agent replied that it already had.

**How it was found.** The agent said so itself.

**Recipes that prevent it.** [Establish guardrails](02-establish-guardrails.md): a sandbox with a listed set of paths, not instructions.

## Signatures that reflected a confounder { #outdated-signatures }

**What happened.** Disease signatures extracted from older papers turned out to reflect a confounder that was not known when they were published.

**How it was found.** The extracted table was checked against current knowledge.

**Recipes that prevent it.** [Literature as data and sparring partner](04-literature-as-data.md), step 4.

## Reviews and slides that look the same { #convergence }

**What happened.** A thesis report drafted with an agent from the reviewer's own bullet points was almost identical to the second examiner's report.
Students' slides are starting to look the same.

**How it was found.** The two reviewers compared their reviews.

**Recipes that prevent it.** [Write, review and teach](09-write-review-teach.md): write from your own notes and argument, and give the agent earlier texts as style examples.
