# object-ownership - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/object-ownership/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this object ownership & least privilege</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Owner/Steward/Delegate 模式">
<action>Work on owner/steward/delegate 模式</action>
<template-output section="owners"/>
</step>

<step n="3" goal="Schema/Database 边界与跨域授权">
<action>Work on schema/database 边界与跨域授权</action>
<template-output section="boundaries"/>
</step>

<step n="4" goal="轮换/交接/弃用">
<action>Work on 轮换/交接/弃用</action>
<template-output section="rotation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
