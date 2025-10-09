# slislos-contract - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/slislos-contract/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this sli/slo contract</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="SLI 定义（正确性/完整性/新鲜度/一致性/可用性）">
<action>Work on sli 定义（正确性/完整性/新鲜度/一致性/可用性）</action>
<template-output section="slis"/>
</step>

<step n="3" goal="目标与告警阈值">
<action>Work on 目标与告警阈值</action>
<template-output section="targets"/>
</step>

<step n="4" goal="值班/升级路径/沟通渠道">
<action>Work on 值班/升级路径/沟通渠道</action>
<template-output section="ownership"/>
</step>

<step n="5" goal="度量方法与数据源（Account Usage/Information Schema）">
<action>Work on 度量方法与数据源（account usage/information schema）</action>
<template-output section="measurement"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
