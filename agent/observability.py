import logging
import time
import uuid

from agent.prometheus_metrics import (
    TOOL_CALLS,
    TOOL_LATENCY,
)
from agent.tools import execute_tool


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    ),
)


def tracked_execute_tool(
    incident_id: str,
    tool_name: str,
    arguments: dict,
):
    """
    Execute an allowlisted infrastructure tool
    and record:

    - correlation ID
    - execution latency
    - success/failure
    - Prometheus metrics
    - structured logs
    """

    correlation_id = str(
        uuid.uuid4()
    )

    start_time = time.monotonic()

    logging.info(
        "tool_start "
        "incident=%s "
        "correlation=%s "
        "tool=%s "
        "arguments=%s",
        incident_id,
        correlation_id,
        tool_name,
        arguments,
    )

    try:

        with TOOL_LATENCY.labels(
            tool=tool_name
        ).time():

            result = execute_tool(
                tool_name,
                arguments,
            )

        TOOL_CALLS.labels(
            tool=tool_name,
            status="success",
        ).inc()

        latency_ms = (
            time.monotonic()
            - start_time
        ) * 1000

        logging.info(
            "tool_success "
            "incident=%s "
            "correlation=%s "
            "tool=%s "
            "latency_ms=%.2f",
            incident_id,
            correlation_id,
            tool_name,
            latency_ms,
        )

        return {
            "correlation_id":
                correlation_id,

            "tool":
                tool_name,

            "status":
                "success",

            "latency_ms":
                round(
                    latency_ms,
                    2,
                ),

            "result":
                result,
        }

    except Exception as exc:

        TOOL_CALLS.labels(
            tool=tool_name,
            status="failure",
        ).inc()

        latency_ms = (
            time.monotonic()
            - start_time
        ) * 1000

        logging.exception(
            "tool_failed "
            "incident=%s "
            "correlation=%s "
            "tool=%s "
            "latency_ms=%.2f "
            "error=%s",
            incident_id,
            correlation_id,
            tool_name,
            latency_ms,
            str(exc),
        )

        raise
