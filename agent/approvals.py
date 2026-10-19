from dataclasses import (
    asdict,
    dataclass,
)

from datetime import (
    datetime,
    timezone,
)

import uuid


@dataclass
class ApprovalRequest:

    approval_id: str

    incident_id: str

    action: str

    arguments: dict

    reason: str

    created_at: str

    status: str = "pending"

    execution_status: (
        str | None
    ) = None

    execution_result: (
        dict | None
    ) = None


APPROVALS: dict[
    str,
    ApprovalRequest,
] = {}


def create_approval(
    incident_id: str,
    action: str,
    arguments: dict,
    reason: str,
) -> ApprovalRequest:

    approval_id = str(
        uuid.uuid4()
    )

    approval = ApprovalRequest(
        approval_id=
            approval_id,

        incident_id=
            incident_id,

        action=
            action,

        arguments=
            arguments,

        reason=
            reason,

        created_at=(
            datetime.now(
                timezone.utc
            ).isoformat()
        ),
    )

    APPROVALS[
        approval_id
    ] = approval

    return approval


def get_approval(
    approval_id: str,
) -> ApprovalRequest | None:

    return APPROVALS.get(
        approval_id
    )


def serialize_approval(
    approval: ApprovalRequest,
) -> dict:

    return asdict(
        approval
    )
