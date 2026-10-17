from agent.runner import run_agent
from agent.evaluator import evaluate_agent


result = run_agent(
    incident_id="EVAL-001",
    service="payments",
)


evaluation = evaluate_agent(
    state=result,
    expected_tools=[
        "get_metrics",
        "get_logs",
        "get_recent_deployment",
    ],
    expected_keyword="deployment",
)


print("\n====================")
print("AGENT EVALUATION")
print("====================")

for key, value in evaluation.items():
    print(
        f"{key}: {value}"
    )
