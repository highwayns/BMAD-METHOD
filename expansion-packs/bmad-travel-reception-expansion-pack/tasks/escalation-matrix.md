# task: escalation-matrix

version: 1.0
role: onsite-ops-lead
purpose: 建立事件分级的升级与支援矩阵。
inputs: [事件类型/等级, 联系人/电话, 值班/备份]
outputs: [docs/onsite/escalation-matrix.md]
steps:

- 渲染 templates/escalation-matrix-tmpl.yaml
- 广而告之并演练
  acceptance:
- 线路清晰/可联通
- 演练通过
