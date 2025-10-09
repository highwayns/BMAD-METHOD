# backup-retention - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/backup-retention/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this backup & retention (time travel/fail-safe)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="保留策略（表/Stage/文件）">
<action>Work on 保留策略（表/stage/文件）</action>
<template-output section="policies"/>
</step>

<step n="3" goal="恢复演练与验证">
<action>Work on 恢复演练与验证</action>
<template-output section="recovery"/>
</step>

<step n="4" goal="自动化与审计">
<action>Work on 自动化与审计</action>
<template-output section="automation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
