from typing import Any, Literal
from pydantic import BaseModel, Field


class AgentDecision(BaseModel):
    action: Literal[
        "get_metrics",
        "get_logs",
        "get_recent_deployment",
        "conclude",
    ]

    arguments: dict[str, Any] = Field(
        default_factory=dict
    )

    reason: str

    hypothesis: str | None = None
