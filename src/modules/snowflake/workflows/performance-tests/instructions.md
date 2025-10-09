# performance-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/performance-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this performance tests (queue/spill/throughput)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="并发/队列/热点">
<action>Work on 并发/队列/热点</action>
<template-output section="load"/>
</step>

<step n="3" goal="溢写/缓存/资源">
<action>Work on 溢写/缓存/资源</action>
<template-output section="spill"/>
</step>

<step n="4" goal="门槛/告警与回退">
<action>Work on 门槛/告警与回退</action>
<template-output section="thresholds"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
