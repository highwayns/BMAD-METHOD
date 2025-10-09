# sql-migration-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sql-migration-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this sql migration plan (ddl/dml/backfill)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="脚本/顺序/幂等/锁">
<action>Work on 脚本/顺序/幂等/锁</action>
<template-output section="scripts"/>
</step>

<step n="3" goal="回填/回算/一致性">
<action>Work on 回填/回算/一致性</action>
<template-output section="backfill"/>
</step>

<step n="4" goal="回退/验证/证据">
<action>Work on 回退/验证/证据</action>
<template-output section="rollback"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
