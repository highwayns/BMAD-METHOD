# testing-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/testing-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this testing plan (dbt tests/custom sql/contract tests)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="覆盖（唯一/非空/关系/断言）">
<action>Work on 覆盖（唯一/非空/关系/断言）</action>
<template-output section="coverage"/>
</step>

<step n="3" goal="样例数据与期望">
<action>Work on 样例数据与期望</action>
<template-output section="samples"/>
</step>

<step n="4" goal="CI 集成与报告">
<action>Work on ci 集成与报告</action>
<template-output section="automation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
