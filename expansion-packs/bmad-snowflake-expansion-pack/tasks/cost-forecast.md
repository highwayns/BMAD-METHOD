# Cost Forecast & FinOps Plan

inputs:

- data/sample-budgets.csv # dept,monthly_budget_credits,owner,thresholds
- current warehouse mix & schedules
  process:
- Map workloads→warehouses→credit rate→forecast by hour/day/week
- Simulate elasticity (auto-suspend/resume, concurrency scaling) scenarios
- Produce monthly forecast and alerts plan
  output:
- docs/finops/cost-forecast.md
