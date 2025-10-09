# data-quality-observability - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/data-quality-observability/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data quality & freshness observability</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="质量规则/上下界/样本">
<action>Work on 质量规则/上下界/样本</action>
<template-output section="rules"/>
</step>

<step n="3" goal="新鲜度 SLI 与回填">
<action>Work on 新鲜度 sli 与回填</action>
<template-output section="freshness"/>
</step>

<step n="4" goal="质量事件的血缘传播">
<action>Work on 质量事件的血缘传播</action>
<template-output section="lineage"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
