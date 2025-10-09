# comms-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/comms-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this communications plan (stakeholders/status page/eta)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="利益相关者与渠道">
<action>Work on 利益相关者与渠道</action>
<template-output section="stakeholders"/>
</step>

<step n="3" goal="更新频率（SEV1:15m/SEV2:30m/SEV3:60m）">
<action>Work on 更新频率（sev1:15m/sev2:30m/sev3:60m）</action>
<template-output section="cadence"/>
</step>

<step n="4" goal="模板（初报/更新/恢复/复盘）">
<action>Work on 模板（初报/更新/恢复/复盘）</action>
<template-output section="templates"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
