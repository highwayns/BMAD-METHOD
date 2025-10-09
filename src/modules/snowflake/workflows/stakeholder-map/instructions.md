# stakeholder-map - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/stakeholder-map/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this stakeholder map & raci</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="干系人地图">
<action>Work on 干系人地图</action>
<template-output section="map"/>
</step>

<step n="3" goal="RACI 矩阵">
<action>Work on raci 矩阵</action>
<template-output section="raci"/>
</step>

<step n="4" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
