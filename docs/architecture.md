# Architecture

```text
                ┌──────────────┐
                │   Incident   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Agent Runner │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Decision     │
                │ Engine       │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │AgentDecision │
                │  Pydantic    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │Policy Layer  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │Allowlisted   │
                │Tools         │
                └──────┬───────┘
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
       Metrics       Logs      Deployments
          │            │             │
          └────────────┼─────────────┘
                       │
                       ▼
                ┌──────────────┐
                │Agent State   │
                │Evidence      │
                └──────┬───────┘
                       │
                       ▼
                  Next Decision
