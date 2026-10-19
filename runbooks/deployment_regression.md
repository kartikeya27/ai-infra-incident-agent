# Deployment Regression

## Symptoms

- error rate rises after deployment
- latency changes after release
- errors appear only on the new version

## Diagnostics

1. retrieve recent deployment
2. compare deployment time with incident start
3. inspect logs for new errors
4. compare pre-deployment metrics

## Remediation

If evidence supports the deployment hypothesis:

1. prepare rollback
2. request approval
3. execute controlled rollback
4. verify service health
