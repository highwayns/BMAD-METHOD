# task: medical-preexisting

version: 1.0
role: visa-insurance-specialist
purpose: 收集既往病史材料，明确除外与扩展方案。
inputs: [诊断/用药/住院史, 医师证明/体检报告]
outputs: [docs/insurance/preexisting-<traveler>.md]
steps:

- 渲染 templates/medical-preexisting-disclosure-tmpl.yaml
- 执行 preexisting-exclusion-check 清单
  acceptance:
- 告知完整
- 除外/扩展已确认
