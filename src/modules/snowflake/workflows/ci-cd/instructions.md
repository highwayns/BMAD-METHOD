# ci-cd - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ci-cd/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this ci/cd pipeline for ingestion/streaming</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="仓库/分支策略">
<action>Work on 仓库/分支策略</action>
<template-output section="repo"/>
</step>

<step n="3" goal="静态检查（SQL lint/安全扫描/规范）">
<action>Work on 静态检查（sql lint/安全扫描/规范）</action>
<template-output section="checks"/>
</step>

<step n="4" goal="构建/测试/部署/回退（蓝绿/灰度）">
<action>Work on 构建/测试/部署/回退（蓝绿/灰度）</action>
<template-output section="pipelines"/>
</step>

<step n="5" goal="密钥与参数/审计">
<action>Work on 密钥与参数/审计</action>
<template-output section="secrets"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
