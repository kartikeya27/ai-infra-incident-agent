import pytest
from pydantic import ValidationError

from agent.models import AgentDecision


def test_valid_agent_decision():
    decision = AgentDecision(
        action="get_logs",
        arguments={"service": "payments"},
        reason="Need log evidence.",
    )

    assert decision.action == "get_logs"
    assert decision.arguments["service"] == "payments"


def test_invalid_agent_action():
    with pytest.raises(ValidationError):
        AgentDecision(
            action="delete_database",
            arguments={},
            reason="Invalid action",
        )
