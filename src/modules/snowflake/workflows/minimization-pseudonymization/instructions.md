# minimization-pseudonymization - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/minimization-pseudonymization/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data minimization & (pseudo/de-)identification</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="取样/聚合/泛化/扰动/差分隐私">
<action>Work on 取样/聚合/泛化/扰动/差分隐私</action>
<template-output section="strategies"/>
</step>

<step n="3" goal="重新识别风险评估（k-匿名、l-多样性、t-接近度）">
<action>Work on 重新识别风险评估（k-匿名、l-多样性、t-接近度）</action>
<template-output section="risk"/>
</step>

<step n="4" goal="可用性与偏差评估">
<action>Work on 可用性与偏差评估</action>
<template-output section="utility"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
