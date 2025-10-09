# metric-spec - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/metric-spec/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this metric specifications (definitions & provenance)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="术语与口径（反例/边界）">
<action>Work on 术语与口径（反例/边界）</action>
<template-output section="glossary"/>
</step>

<step n="3" goal="计算公式与示例">
<action>Work on 计算公式与示例</action>
<template-output section="formula"/>
</step>

<step n="4" goal="维度适用性与汇总逻辑">
<action>Work on 维度适用性与汇总逻辑</action>
<template-output section="dimensions"/>
</step>

<step n="5" goal="溯源（来源表/字段/转换）">
<action>Work on 溯源（来源表/字段/转换）</action>
<template-output section="lineage"/>
</step>

<step n="6" goal="校验规则与期望范围">
<action>Work on 校验规则与期望范围</action>
<template-output section="validation"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
