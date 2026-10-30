---
title: slide-library
skill: slide-library
status: brief
comments: true
recipe: 01-make-materials-accessible
check_level: expert
does: Indexes earlier slide decks and drafts a new talk from an abstract by reusing existing slides.
inputs:
- A folder of earlier slide decks.
- 'For a new talk: an abstract or outline, and the length of the talk.'
outputs:
- 'An index with one line per slide: deck, slide number, and a short description.'
- 'A build order for the new talk: which slide from which deck, in which order, and which slides are new.'
steps:
- Read every deck and write a one-line description of each slide.
- Store the index as plain text next to the decks.
- For a new talk, match the outline to the index.
- Propose a build order and mark the gaps that need new slides.
local:
- Where are your slide decks stored, and in which format?
- Which decks must not be reused, for example confidential or unpublished results?
- 'How should the new deck be assembled: by the agent, or by you from the build order?'
never:
- Never reuse unpublished data in a talk unless the user marks it as cleared.
- Never overwrite an earlier deck.
check: The speaker reads the build order and checks the slide order and the story.
test: Rebuild a talk you gave recently from its abstract, and compare the build order with the real deck.
---

<!-- SKILL_PAGE -->
