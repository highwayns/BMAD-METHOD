# finops-guardrails - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/finops-guardrails/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this finops guardrails (budgets/resource monitors)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="预算/阈值/动作">
<action>Work on 预算/阈值/动作</action>
<template-output section="budgets"/>
</step>

<step n="3" goal="资源监控与冻结策略">
<action>Work on 资源监控与冻结策略</action>
<template-output section="monitors"/>
</step>

<step n="4" goal="离峰降配与停用">
<action>Work on 离峰降配与停用</action>
<template-output section="schedules"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
