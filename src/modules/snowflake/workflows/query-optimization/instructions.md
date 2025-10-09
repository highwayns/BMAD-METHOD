# query-optimization - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/query-optimization/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this query optimization (hotspots/spill/cache)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="热点与大查询剖析（Profile/Spill）">
<action>Work on 热点与大查询剖析（profile/spill）</action>
<template-output section="hotspots"/>
</step>

<step n="3" goal="结果缓存/重用策略">
<action>Work on 结果缓存/重用策略</action>
<template-output section="cache"/>
</step>

<step n="4" goal="优化与收益评估">
<action>Work on 优化与收益评估</action>
<template-output section="remediation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
