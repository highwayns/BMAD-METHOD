# warehouse-ops - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/warehouse-ops/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this warehouse operations (queues/scaling/policies)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="规格/并发扩展/自动挂起">
<action>Work on 规格/并发扩展/自动挂起</action>
<template-output section="sizing"/>
</step>

<step n="3" goal="资源监控与信用触发">
<action>Work on 资源监控与信用触发</action>
<template-output section="policies"/>
</step>

<step n="4" goal="工作负载隔离与优先级">
<action>Work on 工作负载隔离与优先级</action>
<template-output section="isolation"/>
</step>

<step n="5" goal="日程（工作日/离峰）">
<action>Work on 日程（工作日/离峰）</action>
<template-output section="schedules"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
