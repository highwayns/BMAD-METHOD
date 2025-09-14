---
template_id: anim-supervisor/animator-playbook
version: 1
purpose: 动画师作业手册/DoD
fields:
  version: { type: string }
  dod: { type: list, items: string }
  submission_rules: { type: list, items: string }
  review_cycle: { type: list, items: string }
outputs:
  - docs/animator-playbook-{{version}}.md
---

# Animator Playbook v{{version}}

- DoD: {{dod}}
- Submission: {{submission_rules}}
- Review Cycle: {{review_cycle}}
