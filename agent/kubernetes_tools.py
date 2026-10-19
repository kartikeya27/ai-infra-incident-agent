from kubernetes import (
    client,
    config,
)

from kubernetes.config import (
    ConfigException,
)


def load_kubernetes_config() -> None:
    """
    Load Kubernetes authentication.

    Inside Kubernetes:
        service-account credentials are used.

    Local development:
        ~/.kube/config is used.
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

    pods = api.list_namespaced_pod(
        namespace=namespace
    )

    results = []

    for pod in pods.items:

        restart_count = sum(
            status.restart_count
            for status
            in (
                pod.status.container_statuses
                or []
            )
        )

        results.append({
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

            "restart_count":
                restart_count,
        })

    return results


def get_kubernetes_events(
    namespace: str = "default",
) -> list[dict]:

    load_kubernetes_config()

    api = client.CoreV1Api()

    events = api.list_namespaced_event(
        namespace=namespace
    )

    results = []

    for event in events.items:

        results.append({
            "type":
                event.type,

            "reason":
                event.reason,

            "message":
                event.message,

            "object":
                event.involved_object.name,
        })

    return results
