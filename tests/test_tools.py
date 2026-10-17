import pytest

from agent.tools import execute_tool


def test_get_metrics():

    result = execute_tool(
        "get_metrics",
        {
            "service": "payments"
        },
    )

    assert result["cpu"] == 91
    assert result["error_rate"] == 0.16


def test_invalid_tool_rejected():

    with pytest.raises(ValueError):

        execute_tool(
            "delete_database",
            {},
        )
