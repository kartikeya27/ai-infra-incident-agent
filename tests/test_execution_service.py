import pytest

from agent.approvals import (
    APPROVALS,
    create_approval,
)

from agent.execution_service import (
    execute_approved_action,
)


def setup_function():

    APPROVALS.clear()


def test_unapproved_action_is_blocked():

    approval = create_approval(
        incident_id="TEST-001",
        action="restart_service",
        arguments={
            "service":
                "payments",

            "environment":
                "demo",
        },
        reason=(
            "Test remediation."
        ),
    )

    with pytest.raises(
        PermissionError
    ):

        execute_approved_action(
            approval.approval_id
        )
