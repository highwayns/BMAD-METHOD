# task: travel-advisory-log

version: 1.0
role: risk-safety-manager
purpose: 记录旅行通告/预警并评估影响。
inputs: [来源/时间/内容/影响]
outputs: [docs/risk/advisory-log-<period>.md]
steps:

- 渲染 templates/travel-advisory-log-tmpl.yaml
- 与运营/导游/客户更新口径
  acceptance:
- 通告及时
- 口径一致
