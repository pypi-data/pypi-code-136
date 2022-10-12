from kubernetes import client
from k9.core import get_default_namespace


###########################################################################
# Cron Jobs
###########################################################################

def list_cron_jobs(namespace: str = None):
    """
    List all cluster cron jobs
    :param namespace: Then namespace to list cron jobs from.  If None, uses the default namespace.
    :return: A list of dictionary items with **name** and **created**.
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': cj.metadata.name,
            'created': cj.metadata.creation_timestamp
        }
        for cj in client.BatchV1beta1Api().list_namespaced_cron_job(namespace).items
    ]


def create_cron_job(body: dict, namespace: str = None):
    """
    Create a cron job

    :param body: The cron job definition object.
    :param namespace: Then namespace to create cronjob in.  If None, uses the default namespace.
    :return: `V1beta1CronJob <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1beta1CronJob.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.BatchV1beta1Api().create_namespaced_cron_job(namespace, body)


def delete_cron_job(name: str, namespace: str = None):
    """
    Deletes the specified cron job

    :param name: Name of cron job
    :param namespace: Then namespace to delete cron job from.  If None, uses the default namespace.
    :return: None if cron job doesn't exist, `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if cron_job_exists(name, namespace):
        return client.BatchV1beta1Api().delete_namespaced_cron_job(name, namespace)
    else:
        return None


def get_cron_job(name: str, namespace: str = None):
    """
    Gets the specified cron job

    :param name: Name of cron job
    :param namespace: Then namespace to get cron job from.  If None, uses the default namespace.
    :return: `V1beta1CronJob <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1beta1CronJob.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.BatchV1beta1Api().read_namespaced_cron_job(name, namespace)


def cron_job_exists(name: str, namespace: str = None):
    """
    Checks for the cron job's existence.

    :param name: Name of cron job to look for.
    :param namespace: Then namespace to check for cron job.  If None, uses the default namespace.
    :return: True if specified cron job exists
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_cron_job(name, namespace)
        return result.metadata.name == name

    except:
        return False
