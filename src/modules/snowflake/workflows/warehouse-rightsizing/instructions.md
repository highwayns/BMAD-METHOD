# warehouse-rightsizing - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/warehouse-rightsizing/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this warehouse right-sizing & isolation</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="规格/并发/多集群策略">
<action>Work on 规格/并发/多集群策略</action>
<template-output section="sizing"/>
</step>

<step n="3" goal="工作负载隔离与优先级">
<action>Work on 工作负载隔离与优先级</action>
<template-output section="isolation"/>
</step>

<step n="4" goal="自动挂起与最小活跃">
<action>Work on 自动挂起与最小活跃</action>
<template-output section="autosuspend"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
