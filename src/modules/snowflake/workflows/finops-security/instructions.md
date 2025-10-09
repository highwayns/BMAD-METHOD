# finops-security - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/finops-security/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this finops for security (cost of controls)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="控制项成本评估（SOS/MV/掩码/行策略）">
<action>Work on 控制项成本评估（sos/mv/掩码/行策略）</action>
<template-output section="cost_of_controls"/>
</step>

<step n="3" goal="预算/监控与阈值动作">
<action>Work on 预算/监控与阈值动作</action>
<template-output section="budgets"/>
</step>

<step n="4" goal="周/月复盘与优化">
<action>Work on 周/月复盘与优化</action>
<template-output section="reviews"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
