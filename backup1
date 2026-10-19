# AI Infrastructure Incident Response Agent

A production-oriented AI infrastructure incident-response prototype that demonstrates how an LLM-based agent can investigate infrastructure incidents while keeping execution deterministic, observable, auditable, and protected by policy and human approval.

The project combines:

- AI agent reasoning
- structured tool calling
- Python infrastructure tooling
- Kubernetes diagnostics
- operational runbook retrieval
- Prometheus observability
- human-in-the-loop approvals
- Ansible automation
- optional AWX / Ansible Automation Platform execution
- CI/CD
- agent evaluation and testing

---

# Why This Project Exists

Infrastructure incidents often require an engineer to correlate information from several systems:

- service metrics
- application logs
- deployment history
- Kubernetes pod state
- Kubernetes events
- operational runbooks
- infrastructure configuration
- previous remediation procedures

A traditional script follows a predefined workflow.

An AI agent can instead decide what evidence it needs next based on the information already collected.

However, giving an LLM unrestricted infrastructure access is unsafe.

This project therefore follows one core principle:

> **The agent reasons. Deterministic tools execute. The model is never the security boundary.**

The agent may recommend a change, but high-risk infrastructure actions must pass through policy enforcement and human approval before execution.

---

# High-Level Architecture

```text
                         Incident
                            │
                            ▼
                    ┌───────────────┐
                    │ Decision      │
                    │ Engine        │
                    │ LLM/Fallback  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ AgentDecision │
                    │   Pydantic    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Policy Layer  │
                    └───────┬───────┘
                            │
                  ┌─────────┴─────────┐
                  │                   │
                  ▼                   ▼
              LOW RISK             HIGH RISK
                  │                   │
                  ▼                   ▼
          Allowlisted Tool       Approval Request
                  │                   │
                  ▼                   ▼
              Evidence              Human
                  │             Approve / Reject
                  │                   │
                  │              Approved
                  │                   │
                  │                   ▼
                  │          Execution Service
                  │             /          \
                  │          Local          AWX
                  │            │             │
                  │         Ansible       Ansible
                  │            │             │
                  └────────────┴─────┬───────┘
                                     │
                                     ▼
                                Remediation
                                     │
                                     ▼
                                 Verification
