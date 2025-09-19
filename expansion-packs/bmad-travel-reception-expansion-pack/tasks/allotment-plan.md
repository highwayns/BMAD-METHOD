# task: allotment-plan

version: 1.0
role: hotel-contracting-manager
purpose: 规划与管理配额/房券与停卖，建立预警机制。
inputs: [配额日历, 释放期/回收期, 停卖/封馆信息]
outputs: [docs/hotel/allotment-plan-<hotel>-<YYYY>.md]
steps:

- 渲染 templates/allotment-plan-tmpl.yaml
- 配额阈值与告警落地
  acceptance:
- 配额/控制规则明确
- 阈值与预警可用
