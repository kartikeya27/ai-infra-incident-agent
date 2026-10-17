from typing import Any


def get_metrics(service: str) -> dict[str, Any]:
    mock_data = {
        "payments": {
            "cpu": 91,
            "memory": 72,
            "error_rate": 0.16,
            "p95_latency_ms": 890,
        },
        "orders": {
            "cpu": 45,
            "memory": 62,
            "error_rate": 0.21,
            "p95_latency_ms": 420,
        },
    }

    return mock_data.get(
        service,
        {
            "cpu": 0,
            "memory": 0,
            "error_rate": 0,
            "p95_latency_ms": 0,
        },
    )


def get_logs(service: str) -> list[str]:

    logs = {
        "payments": [
            "ERROR database connection pool exhausted",
            "WARN request latency above threshold",
        ],
        "orders": [
            "ERROR upstream inventory service timeout",
            "WARN retry attempt 3",
        ],
    }

    return logs.get(service, [])


def get_recent_deployment(service: str) -> dict:

    deployments = {
        "payments": {
            "version": "v2.8.1",
            "deployed_minutes_ago": 12,
        },
        "orders": {
            "version": "v5.2.0",
            "deployed_minutes_ago": 1440,
        },
    }

    return deployments.get(service, {})
