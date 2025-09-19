# task: incident-report

version: 1.0
role: operations-director
purpose: 对事故进行分级处置、取证与根因分析并沉淀报告。
inputs:

- 事故基本信息/时间线/取证材料
  outputs:
- reports/incident-YYYYMMDD-HHMM.md
  steps:
- 立即执行 safety-incident-playbook
- create-doc → templates/incident-report-tmpl.yaml
- 48小时内提交复盘与改进行动
  acceptance:
- 首轮响应≤30分钟
- 证据充分/根因与预防措施明确
