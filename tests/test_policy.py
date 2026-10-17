from agent.policy import requires_approval


def test_logs_are_low_risk():

    assert (
        requires_approval(
            "get_logs"
        )
        is False
    )


def test_restart_requires_approval():

    assert (
        requires_approval(
            "restart_service"
        )
        is True
    )
