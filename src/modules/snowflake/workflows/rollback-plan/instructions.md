# rollback-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/rollback-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this rollback plan (triggers/steps/verification)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="触发器（阈值/窗口/SLO）">
<action>Work on 触发器（阈值/窗口/slo）</action>
<template-output section="triggers"/>
</step>

<step n="3" goal="步骤/Owner/自动化">
<action>Work on 步骤/owner/自动化</action>
<template-output section="steps"/>
</step>

<step n="4" goal="验证与回滚后的监控">
<action>Work on 验证与回滚后的监控</action>
<template-output section="verify"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
