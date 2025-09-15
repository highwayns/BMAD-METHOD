# Dataset Audit

## Purpose

对数据集进行结构/字典/缺失/异常值/一致性/PII 暴露/版本追踪审计。

## Checks

- 架构与字典一致性、单位与编码（LOINC/SNOMED/OMOP）
- 缺失/异常分布，跨表键一致性
- PII/敏感字段暴露风险（遮蔽/脱敏/访问控制）
- 版本与沿袭（provenance/ETL 日志）

## Output

- `reports/dataset-audit.md`（问题项与修复建议）
