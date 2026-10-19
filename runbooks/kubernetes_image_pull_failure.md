# Kubernetes Image Pull Failure

## Symptoms

- pod enters ImagePullBackOff
- pod enters ErrImagePull
- desired replicas are unavailable
- application becomes unreachable

## Diagnostics

1. inspect pod status
2. inspect Kubernetes events
3. verify container image
4. verify image tag
5. verify registry credentials
6. inspect recent deployment changes

## Safe Actions

- inspect pods
- inspect Kubernetes events
- inspect deployment history

## High Risk Actions

- modify deployment
- rollback release
- restart workload

These require human approval.

## Verification

After remediation verify:

- pods are Running
- desired replicas equal available replicas
- restart count remains stable
- application endpoint responds successfully
