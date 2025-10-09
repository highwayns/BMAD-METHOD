# contract-versioning - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/contract-versioning/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data contract versioning (semver/deprecation)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="语义化版本（主/次/修）">
<action>Work on 语义化版本（主/次/修）</action>
<template-output section="semver"/>
</step>

<step n="3" goal="弃用与迁移期">
<action>Work on 弃用与迁移期</action>
<template-output section="deprec"/>
</step>

<step n="4" goal="通知与证据">
<action>Work on 通知与证据</action>
<template-output section="comms"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
