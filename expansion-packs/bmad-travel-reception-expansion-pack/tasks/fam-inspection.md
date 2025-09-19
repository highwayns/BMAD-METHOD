# task: fam-inspection

version: 1.0
role: hotel-contracting-manager
purpose: 踩点/FAM 检查并沉淀体验与推荐级别。
inputs: [交通/房型/设施/清洁/周边]
outputs: [reports/fam-inspection-<hotel>.md]
steps:

- 渲染 templates/fam-inspection-report-tmpl.yaml
- 生成评分与推荐结论
  acceptance:
- 评分维度与证据齐全
- 建议可操作
