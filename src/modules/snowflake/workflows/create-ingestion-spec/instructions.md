# Ingestion Spec (Sources/Contracts/SLO) - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/create-ingestion-spec/workflow.yaml</critical>

<workflow>

<step n="1" goal="Review and Finalize">
<action>Review complete workflow output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
