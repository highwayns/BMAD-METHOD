# Author Data Contract

docOutputLocation: docs/contracts/[domain]-[entity]-contract.yaml

## Purpose

产出首版契约（Schema/键/枚举/时间线/阈值/质量规则/隐私）。

## Inputs

- templates/data-contract-tmpl.yaml
- templates/contract-readme-tmpl.md

## Steps

- 定义字段/键/时间戳/延迟容忍度/质量规则/权限
- 生成 README 并链接到语义字典与 KPI

## Outputs

- contracts/\*.yaml
- docs/contracts/\*.md
