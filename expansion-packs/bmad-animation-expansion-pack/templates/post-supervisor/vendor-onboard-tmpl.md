---
template_id: post-supervisor/vendor-onboard
version: 1
purpose: 供应商入驻
fields:
  name: { type: string }
  contacts: { type: table, columns: [dept, person, email, phone] }
  security: { type: list, items: string }
  deliverables: { type: list, items: string }
outputs:
  - vendor/vendor-onboard-{{name}}.md
---

# Vendor Onboard — {{name}}

{{contacts}}

- Security: {{security}}
- Deliverables: {{deliverables}}
