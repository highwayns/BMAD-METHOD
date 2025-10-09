# risk-assessment - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/risk-assessment/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this risk assessment (impact/probability/controls)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="风险矩阵与等级">
<action>Work on 风险矩阵与等级</action>
<template-output section="matrix"/>
</step>

<step n="3" goal="控制项（演练/监控/回退）">
<action>Work on 控制项（演练/监控/回退）</action>
<template-output section="controls"/>
</step>

<step n="4" goal="审批与签字">
<action>Work on 审批与签字</action>
<template-output section="approvals"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
