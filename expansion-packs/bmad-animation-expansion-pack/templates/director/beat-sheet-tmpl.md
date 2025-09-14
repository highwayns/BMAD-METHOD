---
template_id: director/beat-sheet
version: 1
purpose: 节拍表（三幕或四幕）
fields:
  act: { type: string, example: 'Act I' }
  beats: { type: table, columns: [idx, beat, purpose, stakes, notes] }
outputs:
  - docs/beat-sheet-{{act}}.md
---

# Beat Sheet — {{act}}

| #   | Beat | Purpose | Stakes | Notes |
| --- | ---- | ------- | ------ | ----- |

{{beats}}
