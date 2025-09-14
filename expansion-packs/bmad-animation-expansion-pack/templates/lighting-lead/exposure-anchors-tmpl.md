---
template_id: lighting-lead/exposure-anchors
version: 1
purpose: 曝光锚点/相机基线
fields:
  seq: { type: string }
  anchors:
    {
      type: table,
      columns: [shot, gray_nits, chrome_nits, key_ev, iso, shutter, tstop, wb_k, notes],
    }
  meters: { type: table, columns: [tool, calibration, date] }
outputs:
  - specs/exposure-anchors-{{seq}}.md
---

# Exposure Anchors — {{seq}}

{{anchors}}

- Meters: {{meters}}
