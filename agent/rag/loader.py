from pathlib import Path


RUNBOOK_DIR = Path(
    "runbooks"
)


def load_runbooks() -> list[dict]:

    documents = []

    for path in (
        RUNBOOK_DIR.glob(
            "*.md"
        )
    ):

        documents.append({
            "source":
                path.name,

            "content":
                path.read_text(
                    encoding="utf-8"
                ),
        })

    return documents
