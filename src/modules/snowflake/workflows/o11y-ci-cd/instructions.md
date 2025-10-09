# o11y-ci-cd - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/o11y-ci-cd/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this observability ci/cd (dashboards/rules as code)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="目录结构/模板/约定">
<action>Work on 目录结构/模板/约定</action>
<template-output section="repo"/>
</step>

<step n="3" goal="指标/规则单元与回归测试">
<action>Work on 指标/规则单元与回归测试</action>
<template-output section="tests"/>
</step>

<step n="4" goal="变更门禁/发布/回滚">
<action>Work on 变更门禁/发布/回滚</action>
<template-output section="pipelines"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
