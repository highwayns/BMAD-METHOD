# task: training-plan

version: 1.0
role: guide-leader-manager
purpose: 制定并发布培训计划与考核。
inputs: [模块与目标, 排期与讲师]
outputs: [docs/guide/training-plan.md]
steps:

- 渲染 templates/guide-training-plan-tmpl.yaml
- 公告并收集签到/通过记录
  acceptance:
- 模块与考核清晰
- 记录可追溯
