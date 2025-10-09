# slo-workshop - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/slo-workshop/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this slo definition workshop</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="SLI（可用性/延迟/失败率/新鲜度/成本）">
<action>Work on sli（可用性/延迟/失败率/新鲜度/成本）</action>
<template-output section="slis"/>
</step>

<step n="3" goal="目标与误差预算">
<action>Work on 目标与误差预算</action>
<template-output section="objectives"/>
</step>

<step n="4" goal="风险与应对/降级策略">
<action>Work on 风险与应对/降级策略</action>
<template-output section="risks"/>
</step>

<step n="5" goal="Owner/升级路径/沟通机制">
<action>Work on owner/升级路径/沟通机制</action>
<template-output section="owners"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete undefined output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
