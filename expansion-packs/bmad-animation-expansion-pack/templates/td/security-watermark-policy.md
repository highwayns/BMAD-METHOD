---
template_id: td/security-watermark-policy
version: 1
purpose: 安全与水印策略
fields:
  access_levels: { type: list, items: string }
  watermark_rules: { type: table, columns: [audience, text, opacity, ttl_days] }
  audit: { type: list, items: string }
outputs:
  - security/watermark-policy.md
---

# Security & Watermark Policy

- Access: {{access_levels}}
- Rules:
  {{watermark_rules}}
- Audit:
  {{audit}}
