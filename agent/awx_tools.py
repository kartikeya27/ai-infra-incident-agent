import requests

from config.settings import (
    AWX_JOB_TEMPLATE_ID,
    AWX_TOKEN,
    AWX_URL,
)


def launch_awx_job(
    service: str,
    environment: str,
) -> dict:
    """
    Launch a preconfigured AWX job template.

    This is NOT unrestricted shell execution.

    The agent can only trigger a known,
    controlled AWX template.
    """

    if not AWX_URL:

        raise RuntimeError(
            "AWX_URL is not configured."
        )

    if not AWX_TOKEN:

        raise RuntimeError(
            "AWX_TOKEN is not configured."
        )

    if (
        AWX_JOB_TEMPLATE_ID
        <= 0
    ):

        raise RuntimeError(
            "AWX_JOB_TEMPLATE_ID "
            "is not configured."
        )

    url = (
        f"{AWX_URL}/api/v2/"
        f"job_templates/"
        f"{AWX_JOB_TEMPLATE_ID}/"
        "launch/"
    )

    headers = {
        "Authorization":
            f"Bearer {AWX_TOKEN}",

        "Content-Type":
            "application/json",
    }

    payload = {
        "extra_vars": {
            "service":
                service,

            "environment":
                environment,
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
