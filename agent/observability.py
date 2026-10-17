import logging
import time
import uuid

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
    correlation_id = str(
        uuid.uuid4()
    )

    start = time.monotonic()

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

        result = execute_tool(
            tool_name,
            arguments,
        )

        latency_ms = (
            time.monotonic()
            - start
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

            "latency_ms":
                round(
                    latency_ms,
                    2,
                ),

            "result":
                result,
        }

    except Exception:

        logging.exception(
            "tool_failed "
            "incident=%s "
            "correlation=%s "
            "tool=%s",
            incident_id,
            correlation_id,
            tool_name,
        )

        raise
