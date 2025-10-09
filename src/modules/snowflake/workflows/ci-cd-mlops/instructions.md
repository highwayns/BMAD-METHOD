# ci-cd-mlops - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ci-cd-mlops/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this ci/cd & mlops</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="仓库与分支策略（Trunk/PR/保护）">
<action>Work on 仓库与分支策略（trunk/pr/保护）</action>
<template-output section="repo"/>
</step>

<step n="3" goal="静态检查/单元/集成/契约/公平性测试">
<action>Work on 静态检查/单元/集成/契约/公平性测试</action>
<template-output section="checks"/>
</step>

<step n="4" goal="训练/评估/注册/发布流水线">
<action>Work on 训练/评估/注册/发布流水线</action>
<template-output section="pipelines"/>
</step>

<step n="5" goal="回退/蓝绿/灰度与审计">
<action>Work on 回退/蓝绿/灰度与审计</action>
<template-output section="rollbacks"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
