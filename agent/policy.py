RISK_LEVELS = {
    "get_metrics": "low",
    "get_logs": "low",
    "get_recent_deployment": "low",
    "restart_service": "high",
}


def get_risk_level(
    action: str
) -> str:

    return RISK_LEVELS.get(
        action,
        "unknown",
    )


def requires_approval(
    action: str
) -> bool:

    risk = get_risk_level(
        action
    )

    return risk in {
        "high",
        "unknown",
    }


def authorize_action(
    action: str,
    approved: bool = False
) -> bool:

    if not requires_approval(action):
        return True

    return approved
