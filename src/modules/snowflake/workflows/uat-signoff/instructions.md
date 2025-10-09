# uat-signoff - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/uat-signoff/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this uat sign-off (evidence/approvals)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="场景/样本/验收标准">
<action>Work on 场景/样本/验收标准</action>
<template-output section="scope"/>
</step>

<step n="3" goal="审批与签字/记录">
<action>Work on 审批与签字/记录</action>
<template-output section="approvals"/>
</step>

<step n="4" goal="缺陷与例外/关闭条件">
<action>Work on 缺陷与例外/关闭条件</action>
<template-output section="issues"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
