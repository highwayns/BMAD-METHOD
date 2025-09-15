# Review Research Operations (PI)

## Purpose

对研究运营（资金-方案-数据-QA/QC-论文-IP-安全）进行分段评审，形成整改项与优先级。

## Steps

1. 收集：读取 `templates/data/*.csv` 与已生成文档（plan/protocol/DMP/SAP/QAQC 等）。
2. 体检：按《research-operations-checklist》逐段打分（0/1/2）。
3. 输出：形成问题单（owner/impact/due）与里程碑建议。

## Output

- `reports/ops-review.md`（得分雷达、优先改进 Top-N、风险看板）
