---
title: package-to-skill
skill: package-to-skill
status: brief
comments: true
recipe: 03-learn-from-peers
check_level: expert
does: Turns the documentation of a software package into a skill an agent can load.
inputs:
- The package's documentation and examples.
- The tasks users most often do with the package.
outputs:
- A skill with the instructions for the common tasks, and one worked example.
steps:
- Read the documentation and examples.
- List the common tasks.
- Write instructions for each task, with the functions to call.
- Add one worked example that runs.
local:
- Which package, and which version?
- Which tasks do your users do most?
- Who maintains the package and can review the skill?
never:
- Never document functions that do not exist in the stated version.
check: The package maintainer reviews the skill, and the worked example runs.
test: A package you maintain. Ask a new user to do one task with the skill.
---

<!-- SKILL_PAGE -->
