# Design Domain & Semantic Model Task

docOutputLocation: docs/architecture/domain-semantic-model.md

## Purpose

定义领域边界、公共维度与指标字典，建立 Bronze→Silver→Gold 的语义一致性。

## Inputs

- templates/logical-data-model-tmpl.md
- data/lakehouse-architect-kb.md

## Steps

1. 分解业务域 → 主题域/子域/上下游依赖
2. 定义统一维度/度量（语义层），约束命名与粒度
3. 绘制层次数据流（Mermaid/PUML），标注SLO与回滚域
4. 产出领域模型与指标字典

## Outputs

- docs/architecture/domain-semantic-model.md
- diagrams/domain/\*.puml
