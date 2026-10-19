import re

from agent.rag.loader import (
    load_runbooks,
)


def tokenize(
    text: str,
) -> set[str]:

    return set(
        re.findall(
            r"[a-zA-Z0-9]+",
            text.lower(),
        )
    )


def search_runbooks(
    query: str,
    limit: int = 3,
) -> list[dict]:

    query_tokens = tokenize(
        query
    )

    scored = []

    for document in (
        load_runbooks()
    ):

        document_tokens = (
            tokenize(
                document[
                    "content"
                ]
            )
        )

        score = len(
            query_tokens
            & document_tokens
        )

        if score > 0:

            scored.append({
                "source":
                    document[
                        "source"
                    ],

                "score":
                    score,

                "content":
                    document[
                        "content"
                    ],
            })

    scored.sort(
        key=lambda item:
            item["score"],
        reverse=True,
    )

    return scored[:limit]
