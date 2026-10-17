from agent.models import AgentDecision


def choose_action(
    service: str,
    evidence: list[dict]
) -> AgentDecision:
    """
    Decide which diagnostic action should run next.

    This first implementation is deterministic.
    Later it will be replaced by a real LLM.
    """

    tools_used = {
        item["tool"]
        for item in evidence
    }

    if "get_metrics" not in tools_used:
        return AgentDecision(
            action="get_metrics",
            arguments={
                "service": service
            },
            reason=(
                "I need current service health metrics "
                "before forming a hypothesis."
            ),
        )

    if "get_logs" not in tools_used:
        return AgentDecision(
            action="get_logs",
            arguments={
                "service": service
            },
            reason=(
                "The metrics have been collected. "
                "I now need logs to identify the failure mode."
            ),
        )

    if "get_recent_deployment" not in tools_used:
        return AgentDecision(
            action="get_recent_deployment",
            arguments={
                "service": service
            },
            reason=(
                "I need deployment history to determine "
                "whether the incident correlates with a recent release."
            ),
        )

    return AgentDecision(
        action="conclude",
        arguments={},
        reason=(
            "Metrics, logs, and deployment history provide "
            "enough evidence to form a hypothesis."
        ),
        hypothesis=(
            "A recent deployment may have introduced a "
            "database connection issue that is contributing "
            "to elevated latency and error rate."
        ),
    )
