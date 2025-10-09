# capacity-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/capacity-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this capacity & scaling plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="需求与峰值预测">
<action>Work on 需求与峰值预测</action>
<template-output section="demand"/>
</step>

<step n="3" goal="仓库分层/并发/自动策略">
<action>Work on 仓库分层/并发/自动策略</action>
<template-output section="warehouse"/>
</step>

<step n="4" goal="预算与资源监控">
<action>Work on 预算与资源监控</action>
<template-output section="budgets"/>
</step>

<step n="5" goal="压测/演练与回退">
<action>Work on 压测/演练与回退</action>
<template-output section="drills"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
