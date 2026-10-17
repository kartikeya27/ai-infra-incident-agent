import json
import os
import subprocess


def get_git_commit() -> str:

    return subprocess.check_output(
        [
            "git",
            "rev-parse",
            "--short",
            "HEAD",
        ],
        text=True,
    ).strip()


metadata = {
    "application":
        "ai-infra-incident-agent",

    "git_commit":
        get_git_commit(),

    "build_number":
        os.getenv(
            "BUILD_NUMBER",
            "local",
        ),

    "environment":
        os.getenv(
            "DEPLOY_ENV",
            "development",
        ),

    "artifact":
        os.getenv(
            "ARTIFACT_NAME",
            "incident-agent-local.tar.gz",
        ),

    "ansible_playbook":
        "ansible/site.yml",
}


with open(
    "deployment.json",
    "w",
    encoding="utf-8",
) as file:

    json.dump(
        metadata,
        file,
        indent=2,
    )


print(
    json.dumps(
        metadata,
        indent=2,
    )
)
