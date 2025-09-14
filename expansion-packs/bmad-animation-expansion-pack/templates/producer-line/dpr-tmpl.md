---
template_id: producer-line/dpr
version: 1
purpose: 日制作报告（DPR）
fields:
  date: { type: date }
  seq_range: { type: string, example: 'SEQ010-SEQ030' }
  completed_shots: { type: list, items: string }
  pending_shots: { type: list, items: string }
  rework_shots: { type: list, items: string }
  dailies_pass_rate: { type: number, example: 0.78 }
  blockers_top: { type: list, items: string }
  timesheet_filled_pct: { type: number }
  notes: { type: text }
outputs:
  - reports/dpr-{{date}}.md
---

# DPR {{date}}

- 序列范围：{{seq_range}}
- 通过镜头：{{completed_shots}}
- 待处理镜头：{{pending_shots}}
- 返工镜头：{{rework_shots}}
- Dailies 通过率：{{dailies_pass_rate}}
- 阻塞TOP：{{blockers_top}}
- 工时回填率：{{timesheet_filled_pct}}
- 备注：{{notes}}
