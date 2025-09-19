# task: create-doc

version: 1.0
role: sales-account-manager
purpose: 基于 YAML 模板生成文档/表单。
inputs: [模板路径, 结构化数据, 交互式填充]
outputs: [docs/sales/*.md]
steps:

- 解析模板 meta/sections
- 若 elicit: true 则逐节问答收集字段
- 渲染并输出
  acceptance:
- 字段覆盖率≥95%
- 核心字段非空校验通过
