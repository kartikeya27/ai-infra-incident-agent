from agent.llm_client import (
    InfrastructureLLM,
)
from agent.models import (
    AgentArguments,
    AgentDecision,
)
from config.settings import (
    USE_REAL_LLM,
)


_llm = None


def make_arguments(
    service: str | None = None,
    namespace: str | None = None,
    query: str | None = None,
    environment: str | None = None,
) -> AgentArguments:

    return AgentArguments(
        service=service,
        namespace=namespace,
        query=query,
        environment=environment,
    )


def deterministic_decision(
    service: str,
    evidence: list[dict],
) -> AgentDecision:

    tools_used = {
        item["tool"]
        for item in evidence
    }

    if (
        "get_metrics"
        not in tools_used
    ):

        return AgentDecision(
            action="get_metrics",
            arguments=
                make_arguments(
                    service=service
                ),
            reason=(
                "Collect service metrics first."
            ),
            hypothesis=None,
        )

    if (
        "get_logs"
        not in tools_used
    ):

        return AgentDecision(
            action="get_logs",
            arguments=
                make_arguments(
                    service=service
                ),
            reason=(
                "Inspect service logs "
                "for the failure mode."
            ),
            hypothesis=None,
        )

    if (
        "search_runbooks"
        not in tools_used
    ):

        return AgentDecision(
            action="search_runbooks",
            arguments=
                make_arguments(
                    query=(
                        "database connection "
                        "pool exhausted"
                    )
                ),
            reason=(
                "Search operational runbooks "
                "for matching symptoms."
            ),
            hypothesis=None,
        )

    if (
        "get_recent_deployment"
        not in tools_used
    ):

        return AgentDecision(
            action=
                "get_recent_deployment",

            arguments=
                make_arguments(
                    service=service
                ),

            reason=(
                "Check whether a deployment "
                "occurred near the incident."
            ),

            hypothesis=None,
        )

    return AgentDecision(
        action="conclude",

        arguments=
            make_arguments(),

        reason=(
            "Enough evidence has "
            "been collected."
        ),

        hypothesis=(
            "A recent deployment may "
            "have introduced a database "
            "connection handling problem."
        ),
    )


def choose_action(
    service: str,
    evidence: list[dict],
) -> AgentDecision:

    global _llm

    if not USE_REAL_LLM:

        return deterministic_decision(
            service=service,
            evidence=evidence,
        )

    if _llm is None:

        _llm = InfrastructureLLM()

    return _llm.choose_action(
        service=service,
        evidence=evidence,
    )
