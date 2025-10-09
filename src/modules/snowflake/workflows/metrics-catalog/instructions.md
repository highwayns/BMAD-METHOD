# metrics-catalog - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/metrics-catalog/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this metrics catalog (definitions/owners/queries)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="术语与口径（统一定义）">
<action>Work on 术语与口径（统一定义）</action>
<template-output section="glossary"/>
</step>

<step n="3" goal="指标清单（来源SQL/刷新/Owner/阈值）">
<action>Work on 指标清单（来源sql/刷新/owner/阈值）</action>
<template-output section="metrics"/>
</step>

<step n="4" goal="指标契约与变更记录">
<action>Work on 指标契约与变更记录</action>
<template-output section="contracts"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
