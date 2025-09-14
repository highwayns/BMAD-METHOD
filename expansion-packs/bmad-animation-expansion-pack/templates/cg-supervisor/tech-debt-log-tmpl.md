---
template_id: cg-supervisor/tech-debt-log
version: 1
purpose: 技术债台账
fields:
  items: { type: table, columns: [area, issue, impact, payoff, plan, owner, due] }
outputs:
  - techdebt/tech-debt-log.md
---

# Tech Debt

{{items}}
