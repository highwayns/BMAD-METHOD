# task: advanced-elicitation

version: 1.0
role: operations-director
purpose: 以 1–9 交互流程高效澄清用户需求与约束，形成可执行输入。
inputs:

- 用户意图/目标
- 业务边界（范围/地域/时段/预算）
- 关键约束（安全/合规/SLA/资源）
  outputs:
- elicitation-log.md
- structured-brief.json
  steps:
- 1 定义目标：确认“为什么做/成功标准”
- 2 利益相关者：谁签核/谁执行/谁受影响
- 3 资源与限制：人车房票/预算/时窗/合规
- 4 风险与备选：地震/台风/航班延误/超售
- 5 数据/口径：KPI/NPS/准点率/取消率
- 6 交付物：文档/表单/派单/报表
- 7 验收：DoD/签核关口
- 8 排期：里程碑/倒计时
- 9 行动：下一步编号清单
  acceptance:
- 形成结构化 brief（JSON/YAML）
- 列出缺失信息与待确认项
- 输出“编号选项”以便快速选择
