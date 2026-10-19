import time

from agent.prometheus_metrics import (
    start_metrics_server,
)
from agent.runner import (
    run_agent,
)


def main():

    print(
        "\nStarting Prometheus "
        "metrics server on port 8000..."
    )

    start_metrics_server(
        port=8001
    )

    print(
        "\nRunning infrastructure "
        "incident agent..."
    )

    result = run_agent(
        incident_id="INC-001",
        service="payments",
    )

    print(
        "\n=========================="
    )
    print(
        "FINAL AGENT RESULT"
    )
    print(
        "=========================="
    )

    print(
        f"Incident: "
        f"{result.incident_id}"
    )

    print(
        f"Service: "
        f"{result.service}"
    )

    print(
        f"Completed: "
        f"{result.completed}"
    )

    print(
        f"Hypothesis: "
        f"{result.hypothesis}"
    )

    print(
        "\nEvidence:"
    )

    for item in (
        result.evidence
    ):

        print(
            "\nTool:",
            item["tool"],
        )

        print(
            "Reason:",
            item["reason"],
        )

        print(
            "Result:",
            item["result"],
        )

    print(
        "\nPrometheus metrics:"
    )

    print(
        "http://localhost:8001/metrics"
    )

    print(
    "\nPrometheus metrics server is running."
    )

    print(
     "Press Ctrl+C to stop."
    )

    while True:
      time.sleep(60)

if __name__ == "__main__":
    main()
