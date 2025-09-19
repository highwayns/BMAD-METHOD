# task: vendor-sourcing

version: 1.0
role: vendor-procurement-manager
purpose: 建立候选清单与寻源策略，锁定高价值供应。
inputs: [城市/类型/容量/季节, 准入条件, 候选与风险]
outputs: [docs/vendor/sourcing-<region>.md]
steps:

- 渲染 templates/vendor-sourcing-tmpl.yaml（逐节提问）
- 执行 due-diligence-check 与 sustainability-check（按需）
  acceptance:
- 候选覆盖关键档位与区域
- 风险与下一步明确
