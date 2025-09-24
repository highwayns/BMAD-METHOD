# task: create-doc-travel-architecture

version: 1.0
role: itinerary-designer
purpose: 基于旅程架构（Day-by-Day/City-by-City/Resource Blocks）生成结构化文档与可复用片段。
inputs:

- 客户Brief/预算/人数/偏好/禁忌
- 行程结构（城市/天数/交通/房型/活动）
  outputs:
- docs/itinerary/travel-architecture-<project>.md
- docs/itinerary/day-by-day-<project>.md
  steps:
- 解析行程骨架（城市→天→段→资源）
- 关联价格与毛利目标，标记P0/P1体验
- 渲染模板并生成可复用片段（住宿/交通/活动）
  acceptance:
- 结构完整（城市/天/段/资源齐全）
- 与预算/毛利边界一致
  checklists:
- travel-operations-checklist.md
