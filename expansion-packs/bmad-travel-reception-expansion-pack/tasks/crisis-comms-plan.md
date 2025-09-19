# task: crisis-comms-plan

version: 1.0
role: risk-safety-manager
purpose: 定义危机沟通对象/频率/发言人与Q&A。
inputs: [内部/客户/媒体/监管, 发言人/频次/Q&A]
outputs: [docs/risk/crisis-comms.md]
steps:

- 渲染 templates/crisis-comms-plan-tmpl.yaml
- 执行 crisis-comms-check 清单
  acceptance:
- 渠道与口径一致
- 法律审阅完成
