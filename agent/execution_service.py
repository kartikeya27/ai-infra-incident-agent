import subprocess

from agent.approvals import (
    get_approval,
)

from agent.awx_tools import (
    launch_awx_job,
)

from config.settings import (
    EXECUTION_BACKEND,
)


ALLOWED_REMEDIATIONS = {
    "restart_service",
}


def execute_approved_action(
    approval_id: str,
) -> dict:

    approval = get_approval(
        approval_id
    )

    if approval is None:

        raise ValueError(
            "Approval not found."
        )

    if approval.status != "approved":

        raise PermissionError(
            "Action has not been approved."
        )

    if (
        approval.action
        not in ALLOWED_REMEDIATIONS
    ):

        raise PermissionError(
            "Action is not an allowed "
            "remediation."
        )

    if (
        approval.execution_status
        == "completed"
    ):

        return (
            approval.execution_result
            or {}
        )

    service = (
        approval.arguments.get(
            "service",
            "payments",
        )
    )

    environment = (
        approval.arguments.get(
            "environment",
            "demo",
        )
    )

    approval.execution_status = (
        "running"
    )

    try:

        if (
            EXECUTION_BACKEND
            == "awx"
        ):

            result = launch_awx_job(
                service=service,
                environment=environment,
            )

            output = {
                "backend":
                    "awx",

                "job_id":
                    result.get("job"),

                "status":
                    "launched",

                "raw":
                    result,
            }

        else:

            command = [
                "ansible-playbook",
                "-i",
                "ansible/inventory.ini",
                "ansible/restart_service.yml",
                "-e",
                f"service_name={service}",
            ]

            process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
            )

            if (
                process.returncode
                != 0
            ):

                raise RuntimeError(
                    process.stderr
                )

            output = {
                "backend":
                    "local",

                "status":
                    "completed",

                "stdout":
                    process.stdout,
            }

        approval.execution_status = (
            "completed"
        )

        approval.execution_result = (
            output
        )

        return output

    except Exception as exc:

        approval.execution_status = (
            "failed"
        )

        approval.execution_result = {
            "error":
                str(exc)
        }

        raise
