def evaluate_agent(
    state,
    expected_tools: list[str],
    expected_keyword: str,
) -> dict:

    tools_used = [
        item["tool"]
        for item in state.evidence
    ]

    matched_tools = [
        tool
        for tool in expected_tools
        if tool in tools_used
    ]

    tool_selection_score = (
        len(matched_tools)
        / len(expected_tools)
    )

    hypothesis = (
        state.hypothesis
        or ""
    )

    hypothesis_correct = (
        expected_keyword.lower()
        in hypothesis.lower()
    )

    return {
        "tools_used":
            tools_used,

        "tool_selection_score":
            round(
                tool_selection_score,
                2,
            ),

        "hypothesis_correct":
            hypothesis_correct,

        "completed":
            state.completed,

        "steps":
            len(state.evidence),
    }
