# task: validate-operations

version: 1.0
role: itinerary-designer
purpose: 行前最终验证（Rooming/Transport/Guide/Tickets）与发布闸门前置检查。
inputs:

- 最新 Rooming/Transport/Guide/Tickets 清单
- 异常/替代/回滚预案
  outputs:
- docs/itinerary/ops-validation-<project>.md
- qa/release-gate-precheck-<date>.md
  steps:
- 核对房单与连通/无障碍/过敏备注
- 校验排车/上客点/车流时序与司机名册
- 校验导游排班/禁排与升级矩阵
- 校验票务/时段/二维码与退改规则
  acceptance:
- 关键证据齐全（回执/截图/合同）
- 未解决阻塞项为0
  checklists:
- travel-operations-checklist.md
