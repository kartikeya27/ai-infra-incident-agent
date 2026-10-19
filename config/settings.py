import os

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "",
)


OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "",
)


USE_REAL_LLM = (
    os.getenv(
        "USE_REAL_LLM",
        "false",
    ).lower()
    == "true"
)


AWX_URL = os.getenv(
    "AWX_URL",
    "",
)


AWX_TOKEN = os.getenv(
    "AWX_TOKEN",
    "",
)


AWX_JOB_TEMPLATE_ID = int(
    os.getenv(
        "AWX_JOB_TEMPLATE_ID",
        "0",
    )
)


EXECUTION_BACKEND = os.getenv(
    "EXECUTION_BACKEND",
    "local",
).lower()
