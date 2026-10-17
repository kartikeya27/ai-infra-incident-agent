from dataclasses import dataclass, field


@dataclass
class AgentState:
    incident_id: str
    service: str
    evidence: list[dict] = field(default_factory=list)
    hypothesis: str | None = None
    completed: bool = False
