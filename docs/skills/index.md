---
title: Skills
---

# Skills

A skill is a set of instructions, sometimes with scripts, that an agent loads for one task.
Each skill on this site belongs to a recipe.
The recipe says when to use the skill and how to check its output.

Most useful skills depend on local details: the institute's reimbursement form, the cluster's scheduler, the folders an agent may use.
A skill built for one campus does not run on another.
So this site publishes a **skill brief** for each skill.
The brief states what is general, and lists the questions only a local user can answer.

## Make your own version

1. Open a skill below and copy its brief.
2. Give the brief to your agent.
   If the agent has a skill-creation skill, such as Anthropic's `skill-creator`, it will use it.
3. The agent asks you the local questions, one at a time, and builds the skill.
4. The agent runs the skill once on the brief's test case.
   Check the result as the brief says.

If you built a version that others could use, [share it](../about/contribute.md#contribute-a-skill).
It is listed on the skill's page as a local version.

## List of skills

<!-- SKILL_TABLE -->

## What a brief contains

| Section | Content |
|---|---|
| Purpose | What the skill does, in one sentence. |
| Inputs | What the user gives the skill. |
| Output | What the skill returns. |
| Steps | What the skill does, in order. |
| Local details | Questions the agent asks the user before it writes the skill. Every institute-specific detail goes here. |
| Never | Rules the local version must keep, such as "never submit the form". |
| How to check the output | The check that runs every time the skill runs. |
| Test case | One case to run after the skill is built, with a known result. |

A brief contains no internal paths, names, credentials or institute forms.
It describes the form or system instead, so each institute can use its own.

## Status

| Status | Meaning |
|---|---|
| <span class="afs-badge afs-badge--brief">brief</span> | A brief is published. Build your own version from it. |
| <span class="afs-badge afs-badge--tried">tried</span> | At least one local version built from the brief is in regular use, and is listed on the skill's page. |
| <span class="afs-badge afs-badge--reproduced">reproduced</span> | Versions at two or more institutes are in regular use. |
