# dq-rulebook - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dq-rulebook/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data quality rulebook (null/unique/range/referential)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="规则（Null/Unique/Range/Referential）">
<action>Work on 规则（null/unique/range/referential）</action>
<template-output section="rules"/>
</step>

<step n="3" goal="阈值/例外/豁免与时限">
<action>Work on 阈值/例外/豁免与时限</action>
<template-output section="thresholds"/>
</step>

<step n="4" goal="Owner/修复/证据">
<action>Work on owner/修复/证据</action>
<template-output section="ownership"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
