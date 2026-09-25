---
title: Skills
---

# Skills

A skill is a set of instructions, sometimes with scripts, that an agent loads for one task.
Each skill on this site belongs to a recipe.
The recipe says when to use the skill and how to check its output.
Anyone can contribute a skill, and skills are reviewed in the same way as recipes.

!!! note "Demo"
    The source links on this page are placeholders.
    No skill has been published yet.

## List of skills

| Skill | Recipe | Output check |
|---|---|---|
| [`travel-reimbursement`](#travel-reimbursement) | [Fill in admin forms](recipes/07-fill-in-admin-forms.md) | <span class="afs-check afs-check--machine">Machine-checkable</span> |
| [`pre-submission-check`](#pre-submission-check) | [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md) | <span class="afs-check afs-check--machine">Machine-checkable</span> |
| [`slide-library`](#slide-library) | [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`lab-meeting-digest`](#lab-meeting-digest) | [Schedule recurring lab tasks](recipes/06-schedule-lab-tasks.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`job-babysitter`](#job-babysitter) | [Run experiments on fixed code](recipes/02-run-experiments-on-fixed-code.md) | <span class="afs-check afs-check--machine">Machine-checkable</span> |
| [`teach-me`](#teach-me) | [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`lecture-visualization`](#lecture-visualization) | [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`public-data-qc`](#public-data-qc) | [Review methods, limit file access](recipes/09-review-methods-restrict-files.md) | <span class="afs-check afs-check--machine">Machine-checkable</span> |
| [`literature-to-table`](#literature-to-table) | [Extract and query the literature](recipes/04-extract-and-query-literature.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`grill-me`](#grill-me) | [Test projects before assigning them](recipes/03-test-projects-before-assigning.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |
| [`package-to-skill`](#package-to-skill) | [Pairing and shared skills](recipes/10-pairing-and-shared-skills.md) | <span class="afs-check afs-check--expert">Expert-checkable</span> |

### `travel-reimbursement` { #travel-reimbursement }

Fills in the travel reimbursement form from a folder of invoices and tickets.

- **Recipe:** [Fill in admin forms](recipes/07-fill-in-admin-forms.md)
- **How to check it:** The totals match the receipts. A person signs and submits the form.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#travel-reimbursement" title="Placeholder link">repository link</a>

### `pre-submission-check` { #pre-submission-check }

Checks a manuscript against the journal's author guidelines and lists what is missing.

- **Recipe:** [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md)
- **How to check it:** Each item names the guideline it comes from.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#pre-submission-check" title="Placeholder link">repository link</a>

### `slide-library` { #slide-library }

Finds slides from earlier talks for reuse in a new one, and lists what it used.

- **Recipe:** [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md)
- **How to check it:** The speaker checks the slide order.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#slide-library" title="Placeholder link">repository link</a>

### `lab-meeting-digest` { #lab-meeting-digest }

Reads the week's project updates and posts a summary on the morning before lab meeting.

- **Recipe:** [Schedule recurring lab tasks](recipes/06-schedule-lab-tasks.md)
- **How to check it:** The group leader reads it before the meeting.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#lab-meeting-digest" title="Placeholder link">repository link</a>

### `job-babysitter` { #job-babysitter }

Watches cluster jobs, resubmits failed runs up to a set limit, and logs each change.

- **Recipe:** [Run experiments on fixed code](recipes/02-run-experiments-on-fixed-code.md)
- **How to check it:** The log lists each resubmission and its cause.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#job-babysitter" title="Placeholder link">repository link</a>

### `teach-me` { #teach-me }

Turns a topic or paper into an interactive tutorial with questions.

- **Recipe:** [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md)
- **How to check it:** The teacher works through it once.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#teach-me" title="Placeholder link">repository link</a>

### `lecture-visualization` { #lecture-visualization }

Builds interactive HTML visualizations for teaching.

- **Recipe:** [Writing, reviewing and teaching](recipes/08-writing-reviewing-teaching.md)
- **How to check it:** The lecturer checks the model behind each plot.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#lecture-visualization" title="Placeholder link">repository link</a>

### `public-data-qc` { #public-data-qc }

Downloads, deduplicates and checks public datasets, with a report for each step.

- **Recipe:** [Review methods, limit file access](recipes/09-review-methods-restrict-files.md)
- **How to check it:** Checksums and counts for each step.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#public-data-qc" title="Placeholder link">repository link</a>

### `literature-to-table` { #literature-to-table }

Extracts values from papers into a table, with the source and page for every value.

- **Recipe:** [Extract and query the literature](recipes/04-extract-and-query-literature.md)
- **How to check it:** A person checks a random sample of rows.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#literature-to-table" title="Placeholder link">repository link</a>

### `grill-me` { #grill-me }

Asks questions about a project description until its assumptions, data and success criteria are written down.

- **Recipe:** [Test projects before assigning them](recipes/03-test-projects-before-assigning.md)
- **How to check it:** The group leader decides whether to assign the project.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#grill-me" title="Placeholder link">repository link</a>

### `package-to-skill` { #package-to-skill }

Turns the documentation of a software package into a skill an agent can load.

- **Recipe:** [Pairing and shared skills](recipes/10-pairing-and-shared-skills.md)
- **How to check it:** The package maintainer reviews the skill.
- **Status:** planned
- **Source:** <a class="afs-placeholder" href="#package-to-skill" title="Placeholder link">repository link</a>

## What a published skill contains

- The instructions the agent loads, as plain text.
- A README that names the recipe, how to check the output, and the tools the skill was tested with.
- One worked example, with no personal data.
- A licence.

Before a skill is published, internal paths, names, credentials and institute-specific forms are removed.
The skill describes the form it fills in instead of including it, so each institute can use its own form.
