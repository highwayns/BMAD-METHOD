# hyperparam-tuning - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/hyperparam-tuning/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this hyperparameter tuning</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="搜索空间与策略">
<action>Work on 搜索空间与策略</action>
<template-output section="search"/>
</step>

<step n="3" goal="预算/并发/中止与早停">
<action>Work on 预算/并发/中止与早停</action>
<template-output section="budget"/>
</step>

<step n="4" goal="实验记录与选择标准">
<action>Work on 实验记录与选择标准</action>
<template-output section="tracking"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
