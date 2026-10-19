from agent.decision_engine import (
    choose_action,
)

from agent.observability import (
    tracked_execute_tool,
)

from agent.policy import (
    requires_approval,
)

from agent.prometheus_metrics import (
    ACTIVE_INCIDENTS,
    AGENT_RUNS,
    AGENT_STEPS,
)

from agent.remediation import (
    propose_remediation,
)

from agent.state import (
    AgentState,
)


MAX_STEPS = 8


def run_agent(
    incident_id: str,
    service: str,
) -> AgentState:

    state = AgentState(
        incident_id=
            incident_id,

        service=
            service,
    )

    ACTIVE_INCIDENTS.inc()

    final_status = (
        "incomplete"
    )

    executed_steps = 0

    try:

        for step in range(
            MAX_STEPS
        ):

            decision = choose_action(
                service=
                    service,

                evidence=
                    state.evidence,
            )

            executed_steps = (
                step + 1
            )

            print(
                "\n-------------------------"
            )

            print(
                f"Step {step + 1}"
            )

            print(
                "-------------------------"
            )

            print(
                f"Action: "
                f"{decision.action}"
            )

            print(
                f"Reason: "
                f"{decision.reason}"
            )

            if (
                decision.action
                == "conclude"
            ):

                state.hypothesis = (
                    decision.hypothesis
                )

                state.completed = True

                final_status = (
                    "success"
                )

                break

            arguments = (
                decision.arguments.model_dump(
                    exclude_none=True
                )
            )

            #
            # HIGH-RISK ACTION
            #
            if requires_approval(
                decision.action
            ):

                remediation = (
                    propose_remediation(
                        incident_id=
                            incident_id,

                        action=
                            decision.action,

                        arguments=
                            arguments,

                        reason=
                            decision.reason,
                    )
                )

                state.pending_approval_id = (
                    remediation.get(
                        "approval_id"
                    )
                )

                state.remediation_status = (
                    remediation[
                        "status"
                    ]
                )

                state.evidence.append({
                    "step":
                        step + 1,

                    "tool":
                        decision.action,

                    "arguments":
                        arguments,

                    "reason":
                        decision.reason,

                    "result":
                        remediation,
                })

                final_status = (
                    "awaiting_approval"
                )

                break

            #
            # LOW-RISK TOOL
            #
            result = (
                tracked_execute_tool(
                    incident_id=
                        incident_id,

                    tool_name=
                        decision.action,

                    arguments=
                        arguments,
                )
            )

            state.evidence.append({
                "step":
                    step + 1,

                "tool":
                    decision.action,

                "arguments":
                    arguments,

                "reason":
                    decision.reason,

                "result":
                    result,
            })

        AGENT_STEPS.observe(
            executed_steps
        )

        AGENT_RUNS.labels(
            service=
                service,

            status=
                final_status,
        ).inc()

        return state

    except Exception:

        AGENT_RUNS.labels(
            service=
                service,

            status=
                "failure",
        ).inc()

        raise

    finally:

        ACTIVE_INCIDENTS.dec()
