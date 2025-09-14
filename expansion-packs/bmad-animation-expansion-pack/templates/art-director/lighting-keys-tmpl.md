---
template_id: art-director/lighting-keys
version: 1
purpose: Lighting Keys 说明
fields:
  seq: { type: string }
  keys: { type: table, columns: [shot, mood, key_light, fill, rim, notes] }
outputs:
  - lookdev/lighting-keys-{{seq}}.md
---

# Lighting Keys — {{seq}}

{{keys}}
