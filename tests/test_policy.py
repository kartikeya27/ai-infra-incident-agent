from agent.policy import (
    get_risk_level,
    requires_approval,
)


def test_metrics_are_low_risk():

    assert (
        requires_approval(
            "get_metrics"
        )
        is False
    )


def test_logs_are_low_risk():

    assert (
        requires_approval(
            "get_logs"
        )
        is False
    )


def test_kubernetes_pods_are_low_risk():

    assert (
        requires_approval(
            "get_kubernetes_pods"
        )
        is False
    )


def test_kubernetes_events_are_low_risk():

    assert (
        requires_approval(
            "get_kubernetes_events"
        )
        is False
    )


def test_runbook_search_is_low_risk():

    assert (
        requires_approval(
            "search_runbooks"
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


def test_unknown_action_requires_approval():

    assert (
        requires_approval(
            "unknown_action"
        )
        is True
    )


def test_restart_is_high_risk():

    assert (
        get_risk_level(
            "restart_service"
        )
        == "high"
    )
