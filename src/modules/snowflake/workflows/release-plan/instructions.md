# release-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/release-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this release plan (versioning/backwards-compatibility)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="版本策略（SemVer/变更说明）">
<action>Work on 版本策略（semver/变更说明）</action>
<template-output section="versions"/>
</step>

<step n="3" goal="兼容与弃用时间线">
<action>Work on 兼容与弃用时间线</action>
<template-output section="compatibility"/>
</step>

<step n="4" goal="回退/热修与沟通">
<action>Work on 回退/热修与沟通</action>
<template-output section="rollback"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
