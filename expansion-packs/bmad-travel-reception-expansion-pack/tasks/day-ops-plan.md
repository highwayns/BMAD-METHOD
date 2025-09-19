# task: day-ops-plan

version: 1.0
role: onsite-ops-lead
purpose: 形成当日现场运营方案（布局/人力/风险）并对齐KPI。
inputs: [日期/场地/时段, 布局/动线, 人员分工, 风险与编号方案]
outputs: [docs/onsite/day-ops-plan-YYYYMMDD.md]
steps:

- 渲染 templates/day-ops-plan-tmpl.yaml（逐节提问）
- 执行 pre-open-check 清单
  acceptance:
- 布局/动线/人员/风险完整
- KPI 与触发阈值明确
