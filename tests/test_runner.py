from agent.runner import run_agent


def test_agent_completes():

    result = run_agent(
        incident_id="TEST-001",
        service="payments",
    )

    assert result.completed is True

    assert result.hypothesis is not None

    assert len(
        result.evidence
    ) == 4

    tools_used = [
        item["tool"]
        for item in result.evidence
    ]

    assert (
        "get_metrics"
        in tools_used
    )

    assert (
        "get_logs"
        in tools_used
    )

    assert (
        "search_runbooks"
        in tools_used
    )

    assert (
        "get_recent_deployment"
        in tools_used
    )
