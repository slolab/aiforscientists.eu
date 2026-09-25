---
title: What went wrong
---

# What went wrong

Errors reported with the recipes, with names and details removed.
Each entry says what happened, how it was found, and which recipe now prevents it.
[Report an error](../about/contribute.md).

## Changed cross-validation { #silent-cross-validation-change }

**What happened.** An agent that was restructuring an analysis changed the cross-validation scheme.
The paper's main result changed.

**How it was found.** The changed code looked correct.
A co-author found the change by reading the code carefully.

**Recipes that prevent it.** [Review methods, limit file access](09-review-methods-restrict-files.md), [Run experiments on fixed code](02-run-experiments-on-fixed-code.md).

## Metric improved by tuning seeds { #metric-hacking }

**What happened.** An automated optimization improved a metric by changing random seeds and small parameters.

**How it was found.** The improvement did not appear on other datasets.

**Recipes that prevent it.** [Let agents search for methods](01-search-for-methods.md), which requires at least three datasets per problem.

## Folders anyone could write to { #open-folders }

**What happened.** On a shared cluster, many group folders could be written to by any user, and none were backed up.
One wrong agent job could have deleted a group's data.

**How it was found.** A check of folder permissions on the cluster.

**Recipes that prevent it.** [Review methods, limit file access](09-review-methods-restrict-files.md).

## Signatures that reflected a confounder { #outdated-signatures }

**What happened.** Disease signatures extracted from older papers turned out to reflect a known confounder.

**How it was found.** The extracted table was checked against current knowledge.

**Recipes that prevent it.** [Extract and query the literature](04-extract-and-query-literature.md), step 4.

## Reviews and slides that look the same { #convergence }

**What happened.** A thesis review drafted by an agent was almost identical to another reviewer's review.
Students' slides are starting to look the same.

**How it was found.** The two reviewers compared their reviews.

**Recipes that prevent it.** [Writing, reviewing and teaching](08-writing-reviewing-teaching.md): write from your own bullet points.
