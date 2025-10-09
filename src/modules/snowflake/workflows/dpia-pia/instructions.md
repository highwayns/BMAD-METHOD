# dpia-pia - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dpia-pia/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dpia/pia (risk assessment & mitigations)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="风险识别（数据类型/主体/规模/自动化）">
<action>Work on 风险识别（数据类型/主体/规模/自动化）</action>
<template-output section="risks"/>
</step>

<step n="3" goal="缓解措施（技术/组织）">
<action>Work on 缓解措施（技术/组织）</action>
<template-output section="mitigations"/>
</step>

<step n="4" goal="DPO/法务评审与记录">
<action>Work on dpo/法务评审与记录</action>
<template-output section="review"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
