---
template_id: pm-asset/story
version: 1
purpose: 用户故事
fields:
  id: { type: string }
  as_a: { type: string }
  i_want: { type: text }
  so_that: { type: text }
  acceptance: { type: list, items: string }
outputs:
  - backlog/story-{{id}}.md
---

# Story {{id}}

- As a {{as_a}}, I want {{i_want}} so that {{so_that}}.
- Acceptance: {{acceptance}}
