# task: ab-test-plan

version: 1.0
role: content-branding
purpose: A/B 实验计划（样本/功效）。
outputs: [docs/exp/ab-test-plan.md]
steps:

- 渲染 templates/ab-test-plan-tmpl.yaml
  acceptance:
- 统计功效达标
