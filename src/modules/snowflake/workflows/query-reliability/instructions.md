# query-reliability - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/query-reliability/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this query reliability (hotspots/failures/cache)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="热点大查询/长尾分析（Profile/Spill）">
<action>Work on 热点大查询/长尾分析（profile/spill）</action>
<template-output section="hotspots"/>
</step>

<step n="3" goal="错误码/重试/回退">
<action>Work on 错误码/重试/回退</action>
<template-output section="failures"/>
</step>

<step n="4" goal="结果缓存命中/重用">
<action>Work on 结果缓存命中/重用</action>
<template-output section="cache"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
