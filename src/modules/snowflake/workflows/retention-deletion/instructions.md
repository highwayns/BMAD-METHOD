# retention-deletion - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/retention-deletion/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this retention & deletion (time travel/fail-safe/legal hold)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="TT/Fail-safe/归档与法律留置">
<action>Work on tt/fail-safe/归档与法律留置</action>
<template-output section="retention"/>
</step>

<step n="3" goal="删除/去标识/回收流程">
<action>Work on 删除/去标识/回收流程</action>
<template-output section="deletion"/>
</step>

<step n="4" goal="验证与证据留存">
<action>Work on 验证与证据留存</action>
<template-output section="verification"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
