# batch-scoring - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/batch-scoring/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this batch scoring (dynamic tables/tasks)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="动态表刷新/优先级/依赖">
<action>Work on 动态表刷新/优先级/依赖</action>
<template-output section="dt"/>
</step>

<step n="3" goal="调度/重试/隔离">
<action>Work on 调度/重试/隔离</action>
<template-output section="tasks"/>
</step>

<step n="4" goal="线上一致性与回填">
<action>Work on 线上一致性与回填</action>
<template-output section="accuracy"/>
</step>

<step n="5" goal="成本监控与优化">
<action>Work on 成本监控与优化</action>
<template-output section="costs"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
