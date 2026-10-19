from prometheus_client import (
    Counter,
    Gauge,
    Histogram,
    start_http_server,
)


AGENT_RUNS = Counter(
    "infra_agent_runs_total",
    "Total infrastructure agent runs",
    [
        "service",
        "status",
    ],
)


TOOL_CALLS = Counter(
    "infra_agent_tool_calls_total",
    "Total infrastructure tool calls",
    [
        "tool",
        "status",
    ],
)


TOOL_LATENCY = Histogram(
    "infra_agent_tool_latency_seconds",
    "Infrastructure tool execution latency",
    [
        "tool",
    ],
)


AGENT_STEPS = Histogram(
    "infra_agent_steps",
    "Number of reasoning steps per incident",
)


ACTIVE_INCIDENTS = Gauge(
    "infra_agent_active_incidents",
    "Number of incidents currently being investigated",
)


def start_metrics_server(
    port: int = 8000,
) -> None:
    """
    Start the Prometheus HTTP endpoint.

    Example:
        http://localhost:8000/metrics
    """

    start_http_server(port)
