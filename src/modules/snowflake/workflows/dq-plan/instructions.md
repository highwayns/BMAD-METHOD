# dq-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dq-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data quality plan (rules + tests)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="规则（完整性/唯一性/范围/关联）">
<action>Work on 规则（完整性/唯一性/范围/关联）</action>
<template-output section="rules"/>
</step>

<step n="3" goal="测试（dbt tests/自定义SQL/合约测试）">
<action>Work on 测试（dbt tests/自定义sql/合约测试）</action>
<template-output section="tests"/>
</step>

<step n="4" goal="阈值与失败处置（隔离/重跑/告警）">
<action>Work on 阈值与失败处置（隔离/重跑/告警）</action>
<template-output section="threshold"/>
</step>

<step n="5" goal="采样/审计表与示例数据">
<action>Work on 采样/审计表与示例数据</action>
<template-output section="sampling"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
