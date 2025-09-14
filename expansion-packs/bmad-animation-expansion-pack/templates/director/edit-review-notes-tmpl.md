---
template_id: director/edit-review-notes
version: 1
purpose: 剪辑评审记录
fields:
  cut: { type: string }
  rhythm_notes: { type: list, items: string }
  transition_notes: { type: list, items: string }
  insert_requests: { type: list, items: string }
  actions: { type: table, columns: [who, what, due, priority] }
outputs:
  - reviews/edit-notes-{{cut}}.md
---

# Edit Review — {{cut}}

## Rhythm

- {{rhythm_notes}}

## Transitions

- {{transition_notes}}

## Inserts

- {{insert_requests}}

## Actions

- {{actions}}
