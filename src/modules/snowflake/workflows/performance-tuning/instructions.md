# performance-tuning - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/performance-tuning/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this sql performance tuning plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Query Profile 分析（Stage/Scan/Join/Spill）">
<action>Work on query profile 分析（stage/scan/join/spill）</action>
<template-output section="profiling"/>
</step>

<step n="3" goal="分区/聚簇/裁剪策略">
<action>Work on 分区/聚簇/裁剪策略</action>
<template-output section="pruning"/>
</step>

<step n="4" goal="SOS/MV/DT 加速策略">
<action>Work on sos/mv/dt 加速策略</action>
<template-output section="acceleration"/>
</step>

<step n="5" goal="仓库规格/并发/自动挂起">
<action>Work on 仓库规格/并发/自动挂起</action>
<template-output section="warehouse"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
