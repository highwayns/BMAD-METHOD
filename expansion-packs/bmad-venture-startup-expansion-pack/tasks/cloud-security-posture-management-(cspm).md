# Cloud Security Posture Management (CSPM)

## Purpose

云安全与配置基线/漂移/门禁。

## Inputs

- 云账户/项目/策略/扫描结果
- templates/cspm-ruleset-and-guardrails-tmpl.yaml
- checklists/cspm-and-cloud-misconfig-qa.md
- data/cloud-misconfig-patterns.md

## Outputs

- CSPM基线与例外库。

## Steps

1. 身份与网络边界/分段/私有化
2. 存储加密/公开访问/快照与KMS
3. 安全组/防火墙/端口与最小暴露
4. 漂移检测/自动修复/变更门
5. 月度审计与例外复核
