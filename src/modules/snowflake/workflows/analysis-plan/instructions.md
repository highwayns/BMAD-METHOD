# analysis-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/analysis-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this analysis plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="关键问题与假设">
<action>Work on 关键问题与假设</action>
<template-output section="questions"/>
</step>

<step n="3" goal="方法（分群/因果/时间序列）">
<action>Work on 方法（分群/因果/时间序列）</action>
<template-output section="methods"/>
</step>

<step n="4" goal="数据与采样（偏倚/缺失）">
<action>Work on 数据与采样（偏倚/缺失）</action>
<template-output section="data"/>
</step>

<step n="5" goal="预期输出与受众">
<action>Work on 预期输出与受众</action>
<template-output section="outputs"/>
</step>

<step n="6" goal="风险/局限与伦理">
<action>Work on 风险/局限与伦理</action>
<template-output section="risks"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
