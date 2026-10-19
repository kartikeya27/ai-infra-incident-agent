TOOL_DEFINITIONS = [
    {
        "name": "get_metrics",
        "description":
            "Retrieve health metrics for a service.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string"
                }
            },
            "required": [
                "service"
            ],
            "additionalProperties":
                False,
        },
    },

    {
        "name": "get_logs",
        "description":
            "Retrieve recent service logs.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string"
                }
            },
            "required": [
                "service"
            ],
            "additionalProperties":
                False,
        },
    },

    {
        "name":
            "get_recent_deployment",
        "description":
            "Retrieve recent deployment information.",
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string"
                }
            },
            "required": [
                "service"
            ],
            "additionalProperties":
                False,
        },
    },
]
