---
template_id: fx-supervisor/particle-design
version: 1
purpose: 粒子/群集方案
fields:
  asset: { type: string }
  emitter: { type: table, columns: [shape, rate, speed, jitter, notes] }
  forces: { type: table, columns: [type, amp, noise, follow, notes] }
outputs:
  - plans/particle-{{asset}}.md
---

# Particle Design — {{asset}}

## Emitter

{{emitter}}

## Forces

{{forces}}
