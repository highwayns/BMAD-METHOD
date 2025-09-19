# task: lead-intake

version: 1.0
role: sales-account-manager
purpose: 以 1–9 交互流程澄清客户需求并形成结构化 brief。
inputs: [客户信息, 预算/时窗, 合规约束(APPI), 成功标准]
outputs: [docs/sales/lead-brief.md]
steps:

- 读取 templates/lead-intake-tmpl.yaml 并逐节提问
- 形成 brief 与缺口清单
- 提供编号选项：进入 proposal-quote 或暂存
  acceptance:
- 核心字段齐全且有决策时点
- 数据隐私条款确认
