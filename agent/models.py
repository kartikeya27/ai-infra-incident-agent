from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
)


class AgentArguments(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    service: str | None = None

    namespace: str | None = None

    query: str | None = None

    environment: str | None = None


class AgentDecision(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    action: Literal[
        "get_metrics",
        "get_logs",
        "get_recent_deployment",
        "get_kubernetes_pods",
        "get_kubernetes_events",
        "search_runbooks",
        "restart_service",
        "conclude",
    ]

    arguments: AgentArguments

    reason: str

    hypothesis: str | None = None
