from kubernetes import (
    client,
    config,
)
from kubernetes.config import (
    ConfigException,
)


def load_kubernetes_config() -> None:
    """
    Load Kubernetes credentials.

    When running inside Kubernetes:
        use the pod service account.

    When running locally:
        use ~/.kube/config.
    """

    try:

        config.load_incluster_config()

    except ConfigException:

        config.load_kube_config()


def get_kubernetes_pods(
    namespace: str = "default",
) -> list[dict]:

    load_kubernetes_config()

    api = client.CoreV1Api()

    pods = (
        api.list_namespaced_pod(
            namespace=namespace
        )
    )

    result = []

    for pod in pods.items:

        result.append({
            "name":
                pod.metadata.name,

            "namespace":
                pod.metadata.namespace,

            "phase":
                pod.status.phase,

            "pod_ip":
                pod.status.pod_ip,

            "node":
                pod.spec.node_name,
        })

    return result
