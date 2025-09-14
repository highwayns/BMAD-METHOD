---
template_id: rigging-lead/muscle-sim-bridge
version: 1
purpose: 肌肉/CFX 接口
fields:
  asset: { type: string }
  attachments: { type: table, columns: [region, locator, type, notes] }
  caches: { type: table, columns: [stage, format, path_token] }
outputs:
  - cfx/muscle-bridge-{{asset}}.md
---

# Muscle/CFX Bridge — {{asset}}

{{attachments}}
{{caches}}
