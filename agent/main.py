from agent.runner import run_agent


def main():

    result = run_agent(
        incident_id="INC-001",
        service="payments",
    )

    print("\n==========================")
    print("FINAL INCIDENT RESULT")
    print("==========================")

    print(f"Incident ID: {result.incident_id}")
    print(f"Service: {result.service}")
    print(f"Completed: {result.completed}")
    print(f"Hypothesis: {result.hypothesis}")

    print("\nEvidence collected:")

    for evidence in result.evidence:
        print(evidence)


if __name__ == "__main__":
    main()
