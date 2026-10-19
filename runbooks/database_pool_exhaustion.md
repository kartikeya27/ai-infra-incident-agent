# Database Connection Pool Exhaustion

## Symptoms

- HTTP 5xx rate increases
- request latency increases
- connection pool utilization exceeds 90%
- requests time out waiting for a database connection

## Diagnostics

1. inspect pool utilization
2. inspect application logs
3. check recent deployments
4. check for leaked connections
5. compare request volume with pool size

## Safe Actions

- collect metrics
- inspect logs
- inspect deployment history

## Higher Risk Actions

- rollback deployment
- restart application
- modify pool configuration

These require approval.

## Verification

After remediation verify:

- error rate returns to baseline
- p95 latency decreases
- connection pool utilization decreases
- database saturation remains healthy
