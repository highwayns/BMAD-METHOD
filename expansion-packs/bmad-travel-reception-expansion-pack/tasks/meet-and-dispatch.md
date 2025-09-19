# task: meet-and-dispatch

version: 1.0
role: onsite-ops-lead
purpose: 组织集合、点名与分车/分组派发。
inputs: [团名/人数/语言, 集合点/时间/分车, 司机/车牌/导游]
outputs: [docs/onsite/meet-dispatch-YYYYMMDD.md]
steps:

- 渲染 templates/meet-dispatch-sheet-tmpl.yaml
- 执行 meet-greet-check 与 bus-boarding-check
  acceptance:
- 集合与分车顺畅
- 安全与无障碍覆盖
