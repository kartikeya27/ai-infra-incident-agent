from agent.approvals import (
    create_approval,
)

from agent.policy import (
    requires_approval,
)


def propose_remediation(
    incident_id: str,
    action: str,
    arguments: dict,
    reason: str,
) -> dict:

    if not requires_approval(
        action
    ):

        return {
            "status":
                "authorized",

            "action":
                action,

            "arguments":
                arguments,
        }

    approval = create_approval(
        incident_id=
            incident_id,

        action=
            action,

        arguments=
            arguments,

        reason=
            reason,
    )

    return {
        "status":
            "awaiting_approval",

        "approval_id":
            approval.approval_id,

        "action":
            action,

        "arguments":
            arguments,
    }
