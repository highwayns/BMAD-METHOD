# privacy-by-design-review - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/privacy-by-design-review/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this privacy-by-design review (change gate)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="范围（新数据/新模型/新共享/新地域）">
<action>Work on 范围（新数据/新模型/新共享/新地域）</action>
<template-output section="scope"/>
</step>

<step n="3" goal="门禁清单与签字">
<action>Work on 门禁清单与签字</action>
<template-output section="checklist"/>
</step>

<step n="4" goal="决策（批准/整改/拒绝）与证据">
<action>Work on 决策（批准/整改/拒绝）与证据</action>
<template-output section="outcomes"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
