# performance-ops - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/performance-ops/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this performance ops (hotspot/spill/queue)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="热点与大查询分析（Profile/Spill）">
<action>Work on 热点与大查询分析（profile/spill）</action>
<template-output section="hotspots"/>
</step>

<step n="3" goal="仓库排队与并发">
<action>Work on 仓库排队与并发</action>
<template-output section="queues"/>
</step>

<step n="4" goal="MV/DT/SOS/结果缓存策略">
<action>Work on mv/dt/sos/结果缓存策略</action>
<template-output section="acceleration"/>
</step>

<step n="5" goal="优化/隔离/限流">
<action>Work on 优化/隔离/限流</action>
<template-output section="remediation"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
