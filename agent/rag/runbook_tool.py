from agent.rag.retriever import (
    search_runbooks,
)


def search_operational_runbooks(
    query: str,
) -> list[dict]:

    results = search_runbooks(
        query=query,
        limit=3,
    )

    return [
        {
            "source":
                item["source"],

            "score":
                item["score"],

            "content":
                item["content"][
                    :2000
                ],
        }

        for item
        in results
    ]
