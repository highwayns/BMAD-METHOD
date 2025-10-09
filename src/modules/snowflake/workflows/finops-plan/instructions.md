# finops-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/finops-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this finops cost optimization plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="预算/资源监控与触发">
<action>Work on 预算/资源监控与触发</action>
<template-output section="budgets"/>
</step>

<step n="3" goal="调度（离峰降配/停用）">
<action>Work on 调度（离峰降配/停用）</action>
<template-output section="schedules"/>
</step>

<step n="4" goal="周/月复盘与优化">
<action>Work on 周/月复盘与优化</action>
<template-output section="reviews"/>
</step>

<step n="5" goal="计费标签与归属">
<action>Work on 计费标签与归属</action>
<template-output section="tagging"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete undefined output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
