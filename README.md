# AI Infrastructure Incident Response Agent

A production-oriented infrastructure AI agent prototype
that demonstrates how LLM-style reasoning can safely
interact with deterministic infrastructure tools.

## Problem

Infrastructure incidents often require engineers to
manually correlate information across:

- metrics
- logs
- deployment history
- configuration
- service health

This project demonstrates how an agent can dynamically
select diagnostic tools based on evidence collected
during an incident.

## Core Design Principle

The agent reasons.

Deterministic tools execute.

The model is never the security boundary.

## Architecture

Incident
→ Decision Engine
→ Structured AgentDecision
→ Policy Validation
→ Allowlisted Tool
→ Infrastructure Evidence
→ Agent State
→ Next Decision
→ Conclusion

## Features

- Python 3 agent loop
- Pydantic structured outputs
- allowlisted infrastructure tools
- maximum execution step limit
- risk-based approval policy
- correlation IDs
- tool latency tracking
- deterministic evaluation
- Ansible infrastructure automation
- GitHub Actions CI
- Jenkins pipeline
- deployment metadata handoff

## Agent vs Traditional Automation

Traditional automation follows predefined steps.

The agent chooses its next diagnostic action based on
the previous tool result.

Example:

Incident
→ metrics
→ abnormal error rate
→ logs
→ database connection error
→ deployment history
→ recent release
→ hypothesis

## Safety

Infrastructure safety is enforced through:

- typed model output
- explicit tool allowlist
- policy validation
- risk classification
- human approval for high-risk actions
- bounded execution steps
- deterministic tools
- audit logging

## Run Locally

Create a virtual environment:

```bash
python3 -m venv .venv
