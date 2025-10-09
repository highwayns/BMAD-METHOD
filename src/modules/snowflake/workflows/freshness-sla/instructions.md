# freshness-sla - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/freshness-sla/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this freshness slas (target_lag/latency/availability)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="目标延迟（TARGET_LAG）">
<action>Work on 目标延迟（target_lag）</action>
<template-output section="target_lag"/>
</step>

<step n="3" goal="可用性/缺口与回填">
<action>Work on 可用性/缺口与回填</action>
<template-output section="availability"/>
</step>

<step n="4" goal="监控与告警/证据">
<action>Work on 监控与告警/证据</action>
<template-output section="monitoring"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
