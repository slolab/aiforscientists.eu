---
title: lecture-visualization
skill: lecture-visualization
status: brief
comments: true
recipe: 09-write-review-teach
check_level: expert
does: Builds small interactive web pages that let students explore the algorithms discussed in a lecture.
inputs:
- The algorithm or model, with its equations or reference code.
- What students should be able to change and observe.
outputs:
- A single web page that runs in a browser without a server.
- A short note on the model behind each plot.
steps:
- Implement the algorithm from the reference.
- Test it against known values.
- Build the page with controls for the parameters students should change.
- Write the note on the model behind each plot.
local:
- Where will the pages be hosted (course platform, static site)?
- Which libraries are allowed?
- Which accessibility rules apply?
never:
- Never load scripts from sources the course platform does not allow.
- Never collect data from students.
check: The lecturer checks the model behind each plot against the reference values.
test: Gradient descent on a two-dimensional function, with step size as a control.
---

<!-- SKILL_PAGE -->
