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
```

---

# Core Design Principles

The project is designed around several production engineering principles:

- the LLM reasons, while deterministic tools execute
- infrastructure access is explicitly allowlisted
- read-only diagnostics are preferred by default
- unknown tools are rejected
- high-risk actions require additional controls
- human approval separates recommendation from execution
- agent execution is bounded
- every tool execution is observable
- incident conclusions should be grounded in collected evidence
- operational knowledge can be retrieved from runbooks
- secrets remain outside source control
- deterministic fallback mode allows the project to run without external LLM access

---

# Main Capabilities

The project includes:

- Python 3 agent execution loop
- deterministic fallback decision engine
- OpenAI LLM client integration
- Pydantic structured decisions
- explicit infrastructure tool allowlisting
- maximum execution-step limits
- risk-based policy classification
- synthetic incident metrics
- synthetic application logs
- deployment-history lookup
- operational runbook retrieval
- Kubernetes pod diagnostics
- Kubernetes event diagnostics
- correlation IDs
- structured logging
- tool latency tracking
- Prometheus metrics
- Dockerized Prometheus
- FastAPI human approval service
- Ansible infrastructure automation
- AWX REST API client
- GitHub Actions CI
- Jenkins pipeline
- deployment metadata generation
- agent evaluation
- unit testing

---

# Agent vs Traditional Automation

Traditional automation normally follows predefined steps:

```text
Step A
   │
   ▼
Step B
   │
   ▼
Step C
```

The infrastructure agent can instead choose the next diagnostic action based on evidence collected during previous steps.

Example:

```text
Incident
   │
   ▼
get_metrics
   │
   ▼
High error rate + high connection pool usage
   │
   ▼
get_logs
   │
   ▼
Database connection pool exhausted
   │
   ▼
search_runbooks
   │
   ▼
Database pool exhaustion runbook
   │
   ▼
get_recent_deployment
   │
   ▼
Recent deployment detected
   │
   ▼
Hypothesis
```

The architecture is therefore hybrid:

```text
LLM / Decision Engine
        │
        ▼
Reasoning
        │
        ▼
Deterministic Python Tools
        │
        ▼
Infrastructure Evidence
```

---

# Safety Model

The agent does **not** receive unrestricted shell, SSH, Kubernetes, or infrastructure access.

The model cannot directly execute arbitrary:

```text
shell commands
SSH commands
kubectl commands
Python code
Ansible commands
```

Infrastructure access is exposed through explicit Python tools.

Current diagnostic tools include:

```text
get_metrics
get_logs
get_recent_deployment
get_kubernetes_pods
search_runbooks
```

Higher-risk actions such as:

```text
restart_service
```

are classified separately.

The intended high-risk flow is:

```text
Agent Recommendation
        │
        ▼
Policy Classification
        │
        ▼
High Risk
        │
        ▼
Human Approval
        │
        ▼
Controlled Automation
        │
        ▼
Ansible / AWX
```

The model is treated as a reasoning component, not as the infrastructure security boundary.

---

# Repository Structure

```text
ai-infra-incident-agent/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── agent/
│   ├── __init__.py
│   ├── approvals.py
│   ├── awx_tools.py
│   ├── decision_engine.py
│   ├── evaluator.py
│   ├── kubernetes_tools.py
│   ├── llm_client.py
│   ├── main.py
│   ├── models.py
│   ├── observability.py
│   ├── policy.py
│   ├── prometheus_metrics.py
│   ├── prompts.py
│   ├── runner.py
│   ├── state.py
│   ├── tool_schemas.py
│   ├── tools.py
│   │
│   └── rag/
│       ├── __init__.py
│       ├── loader.py
│       ├── retriever.py
│       └── runbook_tool.py
│
├── ansible/
│   ├── inventory.ini
│   ├── restart_service.yml
│   └── site.yml
│
├── api/
│   ├── __init__.py
│   └── approval_server.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── incidents.json
│   ├── logs/
│   │   ├── orders.log
│   │   └── payments.log
│   └── metrics/
│       ├── orders.json
│       └── payments.json
│
├── docs/
│   └── architecture.md
│
├── examples/
│   ├── __init__.py
│   ├── evaluate_demo.py
│   └── production_demo.py
│
├── monitoring/
│   └── prometheus.yml
│
├── pipeline/
│   └── Jenkinsfile
│
├── runbooks/
│   ├── database_pool_exhaustion.md
│   └── deployment_regression.md
│
├── scripts/
│   └── create_deployment_metadata.py
│
├── tests/
│   ├── test_models.py
│   ├── test_policy.py
│   ├── test_runner.py
│   └── test_tools.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Prerequisites

For the basic local demo you need:

- Git
- Python 3.11+
- pip
- Docker Desktop

For Kubernetes and infrastructure automation features, also install:

- kubectl
- kind
- Ansible

Optional:

- OpenAI API access
- AWX / Ansible Automation Platform

Verify:

```bash
git --version
python3 --version
docker --version
```

Optional:

```bash
kubectl version --client
kind version
ansible --version
```

On macOS:

```bash
brew install kubectl
brew install kind
brew install ansible
```

Docker Desktop should also be installed and running.

---

# Run the Project Locally

This section provides the complete setup for somebody cloning the repository for the first time.

---

## Step 1 — Clone the Repository

Using HTTPS:

```bash
git clone https://github.com/kartikeya27/ai-infra-incident-agent.git
```

Enter the repository:

```bash
cd ai-infra-incident-agent
```

Alternatively, using SSH:

```bash
git clone git@github.com:kartikeya27/ai-infra-incident-agent.git
cd ai-infra-incident-agent
```

Verify:

```bash
git status
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.
```

---

## Step 2 — Create the Python Virtual Environment

Create:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Verify:

```bash
which python3
```

Expected path should look similar to:

```text
.../ai-infra-incident-agent/.venv/bin/python3
```

Verify Python:

```bash
python3 --version
```

---

## Step 3 — Install Python Dependencies

Upgrade pip:

```bash
python3 -m pip install --upgrade pip
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Verify installed packages:

```bash
python3 -m pip list
```

---

## Step 4 — Create Local Environment Configuration

Copy:

```bash
cp .env.example .env
```

For the first local run, use deterministic mode.

Your `.env` should look similar to:

```text
OPENAI_API_KEY=
OPENAI_MODEL=
USE_REAL_LLM=false

AWX_URL=
AWX_TOKEN=
AWX_JOB_TEMPLATE_ID=0
```

Never commit `.env`.

Verify:

```bash
git check-ignore -v .env
```

You can also run:

```bash
git ls-files .env
```

This command should return nothing.

---

## Step 5 — Run Unit Tests

Run:

```bash
python3 -m pytest -v
```

Tests cover areas such as:

- structured decisions
- Pydantic validation
- invalid actions
- tool allowlisting
- policy behavior
- agent completion
- evidence collection

Do not continue with deployment changes if tests are failing.

---

## Step 6 — Run the Agent

Use deterministic mode:

```text
USE_REAL_LLM=false
```

Run:

```bash
python3 -m agent.main
```

The agent will investigate the synthetic `payments` incident.

A typical flow is:

```text
get_metrics
   │
   ▼
get_logs
   │
   ▼
search_runbooks
   │
   ▼
get_recent_deployment
   │
   ▼
conclude
```

At the end you should see:

```text
FINAL INCIDENT RESULT
```

along with:

- incident ID
- service
- completion status
- hypothesis
- collected evidence

---

# Deterministic Mode

Deterministic mode is the recommended first-time configuration.

Set:

```text
USE_REAL_LLM=false
```

Run:

```bash
python3 -m agent.main
```

Advantages:

- no API key required
- no API credits required
- predictable execution
- useful for CI
- useful for local development
- easier debugging

---

# Real LLM Mode

The project can also use a real OpenAI model as its decision engine.

Edit `.env`:

```text
OPENAI_API_KEY=your-private-api-key
OPENAI_MODEL=your-supported-model
USE_REAL_LLM=true
```

Then:

```bash
python3 -m agent.main
```

The LLM chooses the next diagnostic action based on accumulated evidence.

OpenAI API access and available API credits are required.

Never commit the real API key.

Before every Git push:

```bash
git grep -n "sk-"
```

This should return nothing.

---

# Synthetic Incident Data

The repository contains synthetic infrastructure incident data:

```text
data/
├── incidents.json
├── logs/
│   ├── orders.log
│   └── payments.log
└── metrics/
    ├── orders.json
    └── payments.json
```

The payments example includes:

```text
CPU                     91%
Memory                  72%
Error rate              16%
P95 latency             890 ms
Connection pool usage   98%
```

The associated logs contain simulated database connection pool exhaustion.

This allows realistic incident investigation without using confidential production information.

---

# Operational Runbook Retrieval

Runbooks are stored under:

```text
runbooks/
├── database_pool_exhaustion.md
└── deployment_regression.md
```

Test retrieval:

```bash
python3 -c \
'from agent.rag.retriever import search_runbooks; print(search_runbooks("database connection pool exhausted"))'
```

A cleaner query:

```bash
python3 -c \
'from agent.rag.retriever import search_runbooks; results=search_runbooks("database connection pool exhausted"); print([(r["source"], r["score"]) for r in results])'
```

Expected result:

```text
database_pool_exhaustion.md
```

The current retriever uses lexical/token overlap.

Future versions can use:

- embeddings
- vector databases
- semantic similarity
- chunk-level retrieval

---

# Prometheus Observability

The project exports Prometheus metrics.

Metrics include:

```text
infra_agent_runs_total
infra_agent_tool_calls_total
infra_agent_tool_latency_seconds
infra_agent_steps
infra_agent_active_incidents
```

---

## Start the Production Demo

Run:

```bash
python3 -m examples.production_demo
```

The metrics endpoint is:

```text
http://localhost:8001/metrics
```

Leave this process running.

---

## Start Prometheus

Open another terminal.

Enter the repository:

```bash
cd ai-infra-incident-agent
```

Start:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

Open:

```text
http://localhost:9090
```

Check targets:

```text
http://localhost:9090/targets
```

Expected:

```text
infra-agent    UP
```

---

## Prometheus Queries

Basic query:

```text
infra_agent_tool_calls_total
```

Aggregate successful calls by tool:

```text
sum by (tool) (
  infra_agent_tool_calls_total{
    status="success"
  }
)
```

Agent runs:

```text
infra_agent_runs_total
```

Agent steps:

```text
infra_agent_steps
```

Active incidents:

```text
infra_agent_active_incidents
```

---

# Kubernetes Diagnostics

The project contains Kubernetes integration in:

```text
agent/kubernetes_tools.py
```

The client supports:

- local kubeconfig authentication
- in-cluster authentication
- pod discovery
- namespace
- pod phase
- pod IP
- node information
- restart count
- Kubernetes events

---

## Install kind

On macOS:

```bash
brew install kind
```

Verify:

```bash
kind version
```

---

## Create a Local Kubernetes Cluster

```bash
kind create cluster \
  --name incident-agent
```

Verify context:

```bash
kubectl config current-context
```

Expected:

```text
kind-incident-agent
```

Check nodes:

```bash
kubectl get nodes
```

Expected status:

```text
Ready
```

Check all pods:

```bash
kubectl get pods -A
```

---

## Test Kubernetes From Python

Run:

```bash
python3 -c \
'from agent.kubernetes_tools import get_kubernetes_pods; print(get_kubernetes_pods("default"))'
```

If no workloads exist in the default namespace:

```text
[]
```

is a valid response.

Test Kubernetes events:

```bash
python3 -c \
'from agent.kubernetes_tools import get_kubernetes_events; print(get_kubernetes_events("default"))'
```

---

## Delete the Local Cluster

When finished:

```bash
kind delete cluster \
  --name incident-agent
```

---

# Human Approval API

The project includes a FastAPI approval service:

```text
api/approval_server.py
```

Start it:

```bash
python3 -m uvicorn \
  api.approval_server:app \
  --reload \
  --port 8081
```

Open:

```text
http://localhost:8081/docs
```

Swagger UI allows you to test the API interactively.

Current operations include:

```text
POST /approvals

GET /approvals

GET /approvals/{approval_id}

POST /approvals/{approval_id}/approve

POST /approvals/{approval_id}/reject
```

---

## Example Approval Request

Use:

```text
POST /approvals
```

Body:

```json
{
  "incident_id": "INC-001",
  "action": "restart_service",
  "arguments": {
    "service": "payments",
    "environment": "demo"
  },
  "reason": "Controlled remediation requested after incident diagnosis."
}
```

The API creates a pending approval request.

Approval data is currently stored in memory.

Restarting the FastAPI process clears those approval records.

---

# Ansible Infrastructure Automation

The repository contains:

```text
ansible/
├── inventory.ini
├── restart_service.yml
└── site.yml
```

---

## Validate Main Playbook

```bash
ansible-playbook \
  -i ansible/inventory.ini \
  ansible/site.yml \
  --syntax-check
```

---

## Validate Remediation Playbook

```bash
ansible-playbook \
  -i ansible/inventory.ini \
  ansible/restart_service.yml \
  --syntax-check
```

---

## Run Main Playbook

```bash
ansible-playbook \
  -i ansible/inventory.ini \
  ansible/site.yml
```

Run it again:

```bash
ansible-playbook \
  -i ansible/inventory.ini \
  ansible/site.yml
```

The second execution can be used to demonstrate idempotent behavior.

---

# AWX / Ansible Automation Platform

The repository contains an AWX API client:

```text
agent/awx_tools.py
```

Example AWX configuration:

```text
AWX_URL=https://your-awx-server
AWX_TOKEN=your-private-token
AWX_JOB_TEMPLATE_ID=123
```

These values belong only in `.env`.

Never commit AWX credentials.

The intended architecture is:

```text
AI Agent
   │
   ▼
Policy
   │
   ▼
Human Approval
   │
   ▼
AWX API
   │
   ▼
Approved Job Template
   │
   ▼
Ansible
   │
   ▼
Infrastructure
```

---

# Agent Evaluation

Run:

```bash
python3 -m examples.evaluate_demo
```

The evaluation layer can measure:

- expected tool selection
- number of tools used
- unnecessary tool calls
- agent completion
- hypothesis matching
- investigation steps

---

# Deployment Metadata

Generate:

```bash
python3 scripts/create_deployment_metadata.py
```

The metadata can include:

```text
application
Git commit
build number
environment
artifact
Ansible playbook
```

This demonstrates CI-to-deployment handoff information.

---

# CI/CD

GitHub Actions configuration:

```text
.github/workflows/ci.yml
```

Jenkins pipeline:

```text
pipeline/Jenkinsfile
```

CI validates areas such as:

- dependency installation
- Python tests
- Ansible syntax
- build/package behavior

---

# Recommended First-Time Demo Sequence

The following sequence is recommended for somebody cloning this repository for the first time.

---

## Terminal 1 — Clone and Set Up the Project

```bash
git clone \
  https://github.com/kartikeya27/ai-infra-incident-agent.git
```

Enter:

```bash
cd ai-infra-incident-agent
```

Create the Python environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install --upgrade pip
```

```bash
python3 -m pip install \
  -r requirements.txt
```

Create configuration:

```bash
cp .env.example .env
```

Use:

```text
OPENAI_API_KEY=
OPENAI_MODEL=
USE_REAL_LLM=false

AWX_URL=
AWX_TOKEN=
AWX_JOB_TEMPLATE_ID=0
```

Run tests:

```bash
python3 -m pytest -v
```

Run the agent:

```bash
python3 -m agent.main
```

Start the Prometheus-enabled demo:

```bash
python3 -m examples.production_demo
```

Leave this terminal running.

---

## Terminal 2 — Start Prometheus

Enter the repository:

```bash
cd ai-infra-incident-agent
```

Start Prometheus:

```bash
docker compose up -d
```

Check containers:

```bash
docker compose ps
```

Open:

```text
http://localhost:9090
```

Check:

```text
http://localhost:9090/targets
```

Run query:

```text
infra_agent_tool_calls_total
```

---

## Terminal 3 — Start Approval API

Enter:

```bash
cd ai-infra-incident-agent
```

Activate environment:

```bash
source .venv/bin/activate
```

Start API:

```bash
python3 -m uvicorn \
  api.approval_server:app \
  --reload \
  --port 8081
```

Open:

```text
http://localhost:8081/docs
```

From Swagger you can:

- create approval requests
- list requests
- inspect a request
- approve a request
- reject a request

---

## Terminal 4 — Optional Kubernetes Demo

Create cluster:

```bash
kind create cluster \
  --name incident-agent
```

Check nodes:

```bash
kubectl get nodes
```

Check pods:

```bash
kubectl get pods -A
```

Test Python integration:

```bash
python3 -c \
'from agent.kubernetes_tools import get_kubernetes_pods; print(get_kubernetes_pods("default"))'
```

Test events:

```bash
python3 -c \
'from agent.kubernetes_tools import get_kubernetes_events; print(get_kubernetes_events("default"))'
```

When finished:

```bash
kind delete cluster \
  --name incident-agent
```

---

# Git Development Workflow

For non-trivial changes, use a feature branch.

---

## Step 1 — Switch to Main

```bash
git checkout main
```

---

## Step 2 — Pull Latest Main

```bash
git pull origin main
```

---

## Step 3 — Create a Feature Branch

Example:

```bash
git checkout -b \
  feature/policy-k8s-remediation
```

Verify:

```bash
git branch
```

Expected:

```text
* feature/policy-k8s-remediation
  main
```

---

## Step 4 — Make Your Changes

Edit the required project files.

Then run:

```bash
python3 -m pytest -v
```

---

## Step 5 — Check Git Status

```bash
git status
```

Review all changed and untracked files.

---

## Step 6 — Check for Exposed Secrets

Check for OpenAI-style keys:

```bash
git grep -n "sk-"
```

This should return nothing.

Verify `.env` is not tracked:

```bash
git ls-files .env
```

This should return nothing.

Check ignore rule:

```bash
git check-ignore -v .env
```

---

## Step 7 — Stage Changes

To stage everything:

```bash
git add .
```

Or stage individual files:

```bash
git add README.md
```

```bash
git add agent/
```

```bash
git add tests/
```

---

## Step 8 — Review Staged Changes

```bash
git diff --cached
```

Make sure the commit does not contain:

```text
.env
API keys
AWX tokens
SSH keys
cloud credentials
service-account credentials
```

---

## Step 9 — Commit

Example:

```bash
git commit \
  -m "Add infrastructure agent improvements"
```

---

## Step 10 — Push the Feature Branch

```bash
git push \
  -u origin \
  feature/policy-k8s-remediation
```

---

# Merge Feature Branch Into Main

The recommended method is a GitHub Pull Request.

---

## Step 1 — Push Feature Branch

```bash
git push \
  -u origin \
  feature/policy-k8s-remediation
```

---

## Step 2 — Open the Repository

Open:

```text
https://github.com/kartikeya27/ai-infra-incident-agent
```

GitHub should display:

```text
Compare & pull request
```

Click it.

---

## Step 3 — Confirm Pull Request Direction

Verify:

```text
base: main
compare: feature/policy-k8s-remediation
```

Meaning:

```text
feature/policy-k8s-remediation
             │
             ▼
            main
```

---

## Step 4 — Review Files

Click:

```text
Files changed
```

Review:

- Python files
- README
- tests
- Ansible files
- Kubernetes-related changes
- workflow changes
- configuration
- no secrets

---

## Step 5 — Create Pull Request

Suggested title:

```text
Add infrastructure agent policy and remediation improvements
```

Suggested description:

```text
This pull request improves the AI infrastructure incident-response agent.

Changes include:

- infrastructure agent improvements
- policy and safety improvements
- Kubernetes diagnostics
- observability
- documentation
- local execution instructions
- tests
- CI validation
```

Click:

```text
Create pull request
```

---

## Step 6 — Wait for GitHub Actions

Wait for CI checks to finish.

Do **not** merge if CI is failing.

If a test fails:

```bash
git checkout \
  feature/policy-k8s-remediation
```

Make the fix.

Then:

```bash
git add .
```

```bash
git commit \
  -m "Fix CI issue"
```

```bash
git push
```

The Pull Request will update automatically.

---

## Step 7 — Merge the Pull Request

After all checks pass, click:

```text
Merge pull request
```

Recommended strategy:

```text
Squash and merge
```

Then click:

```text
Confirm squash and merge
```

---

## Step 8 — Update Local Main

Return to your terminal.

Switch:

```bash
git checkout main
```

Pull:

```bash
git pull origin main
```

---

## Step 9 — Verify Main

```bash
git status
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

Run:

```bash
python3 -m pytest -v
```

---

## Step 10 — Delete Local Feature Branch

```bash
git branch \
  -d feature/policy-k8s-remediation
```

If you used squash merge and Git reports that the branch was not fully merged:

```bash
git branch \
  -D feature/policy-k8s-remediation
```

---

## Step 11 — Delete Remote Feature Branch

If GitHub did not delete it automatically:

```bash
git push origin \
  --delete feature/policy-k8s-remediation
```

---

# How to Update README.md in Git

If you are replacing the current repository README with this file:

---

## Step 1 — Enter the Repository

```bash
cd ~/ai-infra-incident-agent
```

---

## Step 2 — Back Up the Existing README

```bash
cp README.md \
  README.md.backup
```

---

## Step 3 — Replace README.md

If your downloaded file is:

```text
~/Downloads/README.md
```

run:

```bash
cp ~/Downloads/README.md \
  ./README.md
```

---

## Step 4 — Verify the README

```bash
head -50 README.md
```

---

## Step 5 — Review the Difference

```bash
git diff README.md
```

---

## Step 6 — Check Git Status

```bash
git status
```

---

## Step 7 — Check for Secrets

```bash
git grep -n "sk-"
```

Verify `.env` is not tracked:

```bash
git ls-files .env
```

---

## Step 8 — Stage README

```bash
git add README.md
```

---

## Step 9 — Review Staged README

```bash
git diff \
  --cached \
  README.md
```

---

## Step 10 — Commit README

```bash
git commit \
  -m "Update README with complete local setup and Git workflow"
```

---

## Step 11 — Push README

If you are on `main`:

```bash
git push origin main
```

If you are on the feature branch:

```bash
git push \
  -u origin \
  feature/policy-k8s-remediation
```

---

# Merge Conflict Resolution

If Git reports a merge conflict:

```bash
git status
```

A conflicted file may contain:

```text
<<<<<<< HEAD

main branch content

=======

feature branch content

>>>>>>> feature/policy-k8s-remediation
```

Edit the file.

Keep the desired final content.

Remove these markers:

```text
<<<<<<<
=======
>>>>>>>
```

Stage the resolved file:

```bash
git add <resolved-file>
```

Complete merge:

```bash
git commit
```

Run tests:

```bash
python3 -m pytest -v
```

Push:

```bash
git push origin main
```

To abandon a local merge:

```bash
git merge --abort
```

---

# Before Every Git Push

Always run:

```bash
git status
```

Check OpenAI secrets:

```bash
git grep -n "sk-"
```

Verify `.env` is not tracked:

```bash
git ls-files .env
```

Review staged changes:

```bash
git diff --cached
```

Do not commit:

```text
.env
OpenAI API keys
AWX tokens
AWS credentials
private SSH keys
Kubernetes service-account credentials
other production secrets
```

---

# Stop Local Services

Stop Prometheus:

```bash
docker compose down
```

Stop FastAPI:

```text
Ctrl+C
```

Stop production demo:

```text
Ctrl+C
```

Delete Kubernetes cluster:

```bash
kind delete cluster \
  --name incident-agent
```

Deactivate Python environment:

```bash
deactivate
```

---

# Troubleshooting

## ModuleNotFoundError

Activate the environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install \
  -r requirements.txt
```

---

## Prometheus Shows No Data

First check:

```text
http://localhost:8001/metrics
```

Then:

```text
http://localhost:9090/targets
```

The target should show:

```text
UP
```

---

## Kubernetes Reports No Current Context

Create:

```bash
kind create cluster \
  --name incident-agent
```

Verify:

```bash
kubectl config current-context
```

```bash
kubectl get nodes
```

---

## OpenAI API Credits Are Unavailable

Use:

```text
USE_REAL_LLM=false
```

Then:

```bash
python3 -m agent.main
```

The project can continue running with the deterministic fallback.

---

## GitHub Push Protection Blocks a Secret

Do **not** bypass push protection.

Remove the secret from the commit.

Rotate the exposed credential.

Check:

```bash
git grep -n "sk-"
```

If necessary, inspect Git history and rewrite the affected local commit before pushing again.

---

# Current Project Status

## Implemented

- Python agent loop
- deterministic fallback mode
- structured Pydantic decisions
- OpenAI client integration
- explicit diagnostic tool allowlisting
- synthetic incident metrics
- synthetic logs
- deployment history lookup
- lexical runbook retrieval
- Kubernetes diagnostic client
- structured logging
- correlation IDs
- Prometheus instrumentation
- Dockerized Prometheus
- approval API
- Ansible playbooks
- AWX API client
- GitHub Actions
- Jenkins pipeline
- agent tests
- evaluation logic

---

## Environment Dependent

The following require additional local or external infrastructure:

- real OpenAI API execution
- local Kubernetes cluster
- AWX end-to-end execution
- external monitoring systems

---

## Planned Improvements

- integrate policy enforcement directly into the runner
- complete end-to-end approval-to-execution workflow
- controlled local Ansible execution after approval
- complete AWX remediation workflow
- persistent approval storage
- Kubernetes demo workload
- Kubernetes failure simulation
- Kubernetes events in the main agent tool allowlist
- vector/embedding RAG
- Grafana dashboard
- Kubernetes RBAC
- AWX job-status monitoring
- post-remediation health verification
- larger incident evaluation datasets
- OpenTelemetry tracing
- Kubernetes deployment of the agent

---

# Security Rules

Never commit:

```text
.env
OpenAI API keys
AWX tokens
cloud credentials
private SSH keys
Kubernetes credentials
service-account credentials
```

`.env.example` must only contain placeholders.

Example:

```text
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL=your-model-name
USE_REAL_LLM=false

AWX_URL=http://localhost:8080
AWX_TOKEN=replace-me
AWX_JOB_TEMPLATE_ID=1
```

Before every push:

```bash
git status
```

```bash
git grep -n "sk-"
```

```bash
git ls-files .env
```

```bash
git diff --cached
```

---

# Design Goals

1. AI reasons over infrastructure evidence rather than receiving unrestricted machine access.
2. Deterministic software performs infrastructure operations.
3. Read-only diagnostics are preferred by default.
4. High-risk operations require additional authorization.
5. Human approval separates recommendation from execution.
6. Infrastructure activity should be observable.
7. Every diagnostic tool invocation should be auditable.
8. Incident conclusions should be grounded in collected evidence.
9. Operational knowledge should be accessible through runbooks.
10. Controlled automation should be preferred over unrestricted remote execution.
11. The application should remain usable without an external LLM.
12. Infrastructure safety controls should live outside the model.

---

# Author

**Kartikeya Bhatt**

GitHub Repository:

```text
https://github.com/kartikeya27/ai-infra-incident-agent
```
