from agent.state import AgentState
from agent.decision_engine import choose_action
from agent.observability import tracked_execute_tool


MAX_STEPS = 6


def run_agent(
    incident_id: str,
    service: str,
) -> AgentState:

    state = AgentState(
        incident_id=incident_id,
        service=service,
    )

    for step in range(MAX_STEPS):

        decision = choose_action(
            service=service,
            evidence=state.evidence,
        )

        print("\n-------------------------")
        print(f"Step {step + 1}")
        print("-------------------------")
        print(f"Action: {decision.action}")
        print(f"Reason: {decision.reason}")

        if decision.action == "conclude":
            state.hypothesis = decision.hypothesis
            state.completed = True
            break

        result = tracked_execute_tool(
            incident_id=incident_id,
            tool_name=decision.action,
            arguments=decision.arguments,
        )

        state.evidence.append({
            "step": step + 1,
            "tool": decision.action,
            "arguments": decision.arguments,
            "reason": decision.reason,
            "result": result,
        })

    return state
