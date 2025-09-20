# Care Pathway & Order Sets Specification Task

## Purpose

将指南转化为本地化临床路径与医嘱集（含处方集/检验/影像/护理/宣教），实现“Evidence → Pathway → Order Set → EMR”。

## Steps

1. 选择疾病/场景（如 CAP、HF、Stroke、AMI、糖尿病等）。
2. 收集指南/专家共识/本地资源与限制，形成差异表。
3. 设计路径：入院判定→评估→治疗→复评→出院标准与随访。
4. 整理医嘱集：药品/剂量/途径/频次，检验/影像，护理医嘱与宣教。
5. 定义质控点与门槛、强制医嘱与提醒、权限与变更流程。
6. 生成文档并提交变更评审（与 EMR 变更控制对齐）。

## Output

模板 `templates/output/care-pathway-spec-tmpl.yaml`。
