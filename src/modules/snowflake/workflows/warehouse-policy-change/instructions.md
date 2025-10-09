# warehouse-policy-change - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/warehouse-policy-change/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this warehouse/resource/quota policy change</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="隔离/并发/队列/限流">
<action>Work on 隔离/并发/队列/限流</action>
<template-output section="isolation"/>
</step>

<step n="3" goal="资源监控与预算">
<action>Work on 资源监控与预算</action>
<template-output section="monitors"/>
</step>

<step n="4" goal="演练与回退">
<action>Work on 演练与回退</action>
<template-output section="test"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
