# task: quality-audit

version: 1.0
role: operations-director
purpose: 执行质量抽检并形成复盘与纠正措施。
inputs:

- 抽检范围/样本/证据
  outputs:
- reports/quality-audit-YYYYMMDD.md
  steps:
- create-doc → templates/quality-audit-report-tmpl.yaml
- 形成整改闭环与跟踪指标
  acceptance:
- 抽检记录可追溯
- 纠正措施有负责人与期限
