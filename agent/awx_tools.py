import requests

from config.settings import (
    AWX_JOB_TEMPLATE_ID,
    AWX_TOKEN,
    AWX_URL,
)


def _headers() -> dict:

    if not AWX_TOKEN:

        raise RuntimeError(
            "AWX_TOKEN is not configured."
        )

    return {
        "Authorization":
            f"Bearer {AWX_TOKEN}",

        "Content-Type":
            "application/json",
    }


def launch_awx_job(
    service: str,
    environment: str,
) -> dict:

    if not AWX_URL:

        raise RuntimeError(
            "AWX_URL is not configured."
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
        headers=_headers(),
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def get_awx_job_status(
    job_id: int,
) -> dict:

    url = (
        f"{AWX_URL}/api/v2/"
        f"jobs/{job_id}/"
    )

    response = requests.get(
        url,
        headers=_headers(),
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    return {
        "id":
            data.get("id"),

        "status":
            data.get("status"),

        "started":
            data.get("started"),

        "finished":
            data.get("finished"),
    }
