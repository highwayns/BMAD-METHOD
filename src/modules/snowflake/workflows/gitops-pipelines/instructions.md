# gitops-pipelines - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/gitops-pipelines/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this gitops pipelines (plan/apply/verify/rollback)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="阶段与门禁（lint/test/plan/apply/verify）">
<action>Work on 阶段与门禁（lint/test/plan/apply/verify）</action>
<template-output section="stages"/>
</step>

<step n="3" goal="审批与签字/变更冻结">
<action>Work on 审批与签字/变更冻结</action>
<template-output section="approvals"/>
</step>

<step n="4" goal="回滚策略与演练">
<action>Work on 回滚策略与演练</action>
<template-output section="backout"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
