from fastapi import (
    FastAPI,
    HTTPException,
)
from pydantic import BaseModel

from agent.approvals import (
    APPROVALS,
    create_approval,
    get_approval,
    serialize_approval,
)


app = FastAPI(
    title=(
        "Infrastructure Agent "
        "Approval API"
    )
)


class NewApproval(BaseModel):

    incident_id: str

    action: str

    arguments: dict

    reason: str


@app.post("/approvals")
def create_new_approval(
    request: NewApproval,
):

    approval = create_approval(
        incident_id=
            request.incident_id,

        action=
            request.action,

        arguments=
            request.arguments,

        reason=
            request.reason,
    )

    return serialize_approval(
        approval
    )


@app.get("/approvals")
def list_approvals():

    return [
        serialize_approval(
            approval
        )
        for approval
        in APPROVALS.values()
    ]


@app.get(
    "/approvals/{approval_id}"
)
def get_one_approval(
    approval_id: str,
):

    approval = get_approval(
        approval_id
    )

    if not approval:

        raise HTTPException(
            status_code=404,
            detail=(
                "Approval not found"
            ),
        )

    return serialize_approval(
        approval
    )


@app.post(
    "/approvals/{approval_id}/approve"
)
def approve(
    approval_id: str,
):

    approval = get_approval(
        approval_id
    )

    if not approval:

        raise HTTPException(
            status_code=404,
            detail=(
                "Approval not found"
            ),
        )

    approval.status = "approved"

    return serialize_approval(
        approval
    )


@app.post(
    "/approvals/{approval_id}/reject"
)
def reject(
    approval_id: str,
):

    approval = get_approval(
        approval_id
    )

    if not approval:

        raise HTTPException(
            status_code=404,
            detail=(
                "Approval not found"
            ),
        )

    approval.status = "rejected"

    return serialize_approval(
        approval
    )
