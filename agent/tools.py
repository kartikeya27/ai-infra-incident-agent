import json
from pathlib import Path
from typing import Any

from agent.kubernetes_tools import (
    get_kubernetes_pods,
)
from agent.rag.runbook_tool import (
    search_operational_runbooks,
)


DATA_DIR = Path(
    "data"
)


def get_metrics(
    service: str,
) -> dict[str, Any]:

    path = (
        DATA_DIR
        / "metrics"
        / f"{service}.json"
    )

    if not path.exists():

        return {}

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def get_logs(
    service: str,
) -> list[str]:

    path = (
        DATA_DIR
        / "logs"
        / f"{service}.log"
    )

    if not path.exists():

        return []

    return (
        path.read_text(
            encoding="utf-8"
        )
        .splitlines()
    )


def get_recent_deployment(
    service: str,
) -> dict:

    deployments = {
        "payments": {
            "version":
                "v2.8.1",

            "deployed_minutes_ago":
                12,
        },

        "orders": {
            "version":
                "v5.2.0",

            "deployed_minutes_ago":
                1440,
        },
    }

    return deployments.get(
        service,
        {},
    )


ALLOWED_TOOLS = {
    "get_metrics":
        get_metrics,

    "get_logs":
        get_logs,

    "get_recent_deployment":
        get_recent_deployment,

    "get_kubernetes_pods":
        get_kubernetes_pods,

    "search_runbooks":
        search_operational_runbooks,
}


def execute_tool(
    name: str,
    arguments: dict,
):

    if name not in ALLOWED_TOOLS:

        raise ValueError(
            f"Tool '{name}' "
            "is not authorized"
        )

    return ALLOWED_TOOLS[
        name
    ](
        **arguments
    )
