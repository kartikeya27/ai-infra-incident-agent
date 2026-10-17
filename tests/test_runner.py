from agent.runner import run_agent


def test_agent_completes():

    result = run_agent(
        incident_id="TEST-001",
        service="payments",
    )

    assert result.completed is True
    assert result.hypothesis is not None
    assert len(result.evidence) == 3
