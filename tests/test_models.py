import pytest

from pydantic import ValidationError

from agent.models import (
    AgentArguments,
    AgentDecision,
)


def test_valid_agent_decision():

    decision = AgentDecision(
        action="get_logs",
        arguments=AgentArguments(
            service="payments"
        ),
        reason="Need log evidence.",
        hypothesis=None,
    )

    assert (
        decision.action
        == "get_logs"
    )

    assert (
        decision.arguments.service
        == "payments"
    )


def test_conclude_decision():

    decision = AgentDecision(
        action="conclude",
        arguments=AgentArguments(),
        reason=(
            "Enough evidence exists."
        ),
        hypothesis=(
            "Recent deployment may be related."
        ),
    )

    assert (
        decision.action
        == "conclude"
    )

    assert (
        decision.arguments.service
        is None
    )


def test_invalid_agent_action():

    with pytest.raises(
        ValidationError
    ):

        AgentDecision(
            action="delete_database",
            arguments=AgentArguments(
                service="payments"
            ),
            reason="Invalid action.",
            hypothesis=None,
        )


def test_extra_argument_rejected():

    with pytest.raises(
        ValidationError
    ):

        AgentArguments(
            service="payments",
            dangerous_command="rm -rf /",
        )
