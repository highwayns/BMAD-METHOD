# data-inventory - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/data-inventory/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data inventory & classification (snowflake)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="对象清单（库/模式/表/列）与来源">
<action>Work on 对象清单（库/模式/表/列）与来源</action>
<template-output section="inventory"/>
</step>

<step n="3" goal="Owner/Steward/处理者/控制者">
<action>Work on owner/steward/处理者/控制者</action>
<template-output section="owners"/>
</step>

<step n="4" goal="机密级别与标签（PII/PHI/财务等）">
<action>Work on 机密级别与标签（pii/phi/财务等）</action>
<template-output section="classification"/>
</step>

<step n="5" goal="最小化与必要性说明">
<action>Work on 最小化与必要性说明</action>
<template-output section="minimization"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
