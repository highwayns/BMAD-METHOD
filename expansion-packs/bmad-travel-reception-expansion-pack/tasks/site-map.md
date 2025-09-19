# task: site-map

version: 1.0
role: onsite-ops-lead
purpose: 输出现场点位与容量说明，支持分区调度。
inputs: [点位/坐标/照片, 功能/容量/注意]
outputs: [docs/onsite/site-map-<venue>.md]
steps:

- 渲染 templates/site-map-points-tmpl.yaml
- 与 crowd-control 方案联动
  acceptance:
- 点位齐全/容量可用
- 风险提示清晰
