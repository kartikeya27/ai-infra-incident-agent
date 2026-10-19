import json

from openai import OpenAI

from agent.models import AgentDecision
from agent.prompts import AGENT_SYSTEM_PROMPT
from config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


class InfrastructureLLM:
    """
    Wrapper around the OpenAI Responses API.

    The LLM must return a structured AgentDecision.
    """

    def __init__(self):

        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        if not OPENAI_MODEL:
            raise ValueError(
                "OPENAI_MODEL is not configured."
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        self.model = OPENAI_MODEL

    def choose_action(
        self,
        service: str,
        evidence: list[dict],
    ) -> AgentDecision:

        context = {
            "service": service,
            "evidence": evidence,
        }

        response = self.client.responses.parse(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": AGENT_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": (
                        "Investigate this infrastructure incident.\n\n"
                        + json.dumps(
                            context,
                            indent=2,
                        )
                    ),
                },
            ],
            text_format=AgentDecision,
        )

        if response.output_parsed is None:
            raise RuntimeError(
                "Model did not produce a valid AgentDecision."
            )

        return response.output_parsed
