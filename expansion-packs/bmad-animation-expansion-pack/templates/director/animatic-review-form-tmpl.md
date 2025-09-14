---
template_id: director/animatic-review-form
version: 1
purpose: Animatic 评审记录
fields:
  cut: { type: string }
  timing_notes: { type: list, items: string }
  continuity_notes: { type: list, items: string }
  audio_notes: { type: list, items: string }
  actions: { type: table, columns: [who, what, due, priority] }
outputs:
  - reviews/animatic-review-{{cut}}.md
---

# Animatic Review — {{cut}}

## Timing

- {{timing_notes}}

## Continuity

- {{continuity_notes}}

## Audio

- {{audio_notes}}

## Actions

- {{actions}}
