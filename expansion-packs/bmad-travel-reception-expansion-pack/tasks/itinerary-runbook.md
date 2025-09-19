# task: itinerary-runbook

version: 1.0
role: operations-director
purpose: 为具体团队/行程生成运行手册，保障落地与一致性。
inputs:

- 团队信息/路书/票务/餐饮/过敏
  outputs:
- docs/ops/runbook-<group>.md
  steps:
- create-doc → templates/itinerary-runbook-tmpl.yaml
- 现场抽检与回传照片/定位/签到
  acceptance:
- 日程要点/备选方案完整
- 抽检通过率≥95%
