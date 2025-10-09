# selfservice-portal - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/selfservice-portal/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this developer self-service portal</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="服务目录（申请新仓库/新Schema/新流水线/临时访问）">
<action>Work on 服务目录（申请新仓库/新schema/新流水线/临时访问）</action>
<template-output section="catalog"/>
</step>

<step n="3" goal="表单/校验/审批流">
<action>Work on 表单/校验/审批流</action>
<template-output section="forms"/>
</step>

<step n="4" goal="自动化动作与证据留存">
<action>Work on 自动化动作与证据留存</action>
<template-output section="automation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
