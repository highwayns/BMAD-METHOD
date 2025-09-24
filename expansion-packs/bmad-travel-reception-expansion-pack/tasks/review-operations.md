# task: review-operations

version: 1.0
role: itinerary-designer
purpose: 与运营/供应/运输/导游跨域评审行程的可执行性与风险。
inputs:

- 行程提案/资源锁定状态/释放曲线
- 高风险点（旺季/禁行/施工/天气）
  outputs:
- docs/itinerary/review-minutes-<project>.md
- risk/ops-review-actions-<project>.md
  steps:
- 逐日逐段过表：房配/车配/导游/票务
- 校验停卖/封控/时段与容量限制
- 形成整改与责任人/期限
  acceptance:
- P0 风险均有缓解方案和负责人
- 决议形成并回执
  checklists:
- travel-operations-checklist.md
