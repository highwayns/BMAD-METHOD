# oncall-setup - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/oncall-setup/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this oncall setup (roster/rotation/runbooks)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="排班与轮换/替班/假期">
<action>Work on 排班与轮换/替班/假期</action>
<template-output section="roster"/>
</step>

<step n="3" goal="角色（IC/Tech Lead/Comms/Recorder）">
<action>Work on 角色（ic/tech lead/comms/recorder）</action>
<template-output section="roles"/>
</step>

<step n="4" goal="Runbooks 链接与演练频率">
<action>Work on runbooks 链接与演练频率</action>
<template-output section="runbooks"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
