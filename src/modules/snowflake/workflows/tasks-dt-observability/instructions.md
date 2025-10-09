# tasks-dt-observability - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/tasks-dt-observability/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this streams/tasks/dynamic tables observability</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="拓扑/依赖/优先级">
<action>Work on 拓扑/依赖/优先级</action>
<template-output section="topology"/>
</step>

<step n="3" goal="SLA/重试/死信/补偿">
<action>Work on sla/重试/死信/补偿</action>
<template-output section="sla"/>
</step>

<step n="4" goal="历史失败与趋势">
<action>Work on 历史失败与趋势</action>
<template-output section="history"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
