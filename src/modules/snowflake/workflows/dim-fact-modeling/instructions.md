# dim-fact-modeling - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dim-fact-modeling/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dimensional modeling (star/snowflake)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="事实表（粒度/度量/度量可加性）">
<action>Work on 事实表（粒度/度量/度量可加性）</action>
<template-output section="facts"/>
</step>

<step n="3" goal="维度（主键/层级/SCD）">
<action>Work on 维度（主键/层级/scd）</action>
<template-output section="dimensions"/>
</step>

<step n="4" goal="分区/聚簇/裁剪策略">
<action>Work on 分区/聚簇/裁剪策略</action>
<template-output section="partitions"/>
</step>

<step n="5" goal="跨域一致维度">
<action>Work on 跨域一致维度</action>
<template-output section="conformance"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
