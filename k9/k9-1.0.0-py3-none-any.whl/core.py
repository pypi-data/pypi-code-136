from collections import namedtuple

from kubernetes import client, config as kube_config

from datetime import datetime, timezone

from aws import rds, secret
import os
import pprint
import subprocess
import time
import yaml
import json
from jinja2 import Environment, FileSystemLoader


default_namespace = None


###########################################################################
# Utility Functions
###########################################################################

CommandResult = namedtuple('CommandResult', 'args returncode stdout stderr')
output_on = True


def set_run_output(output_mode=True):
    """
    Sets flag to indicate whether outputs from the run_command should be printed
    to the console or not.
    :param output_mode: True if stdout should be printed to console.  Default is True
    """
    global output_on
    output_on = output_mode


def run_command(*params):
    """
    This is a helper function to make it easier to run shell commands in
    a consistent manner.

    Calls the subprocess.run() command with the following options:

    capture_output=True  Which provides **stdout** and **stderr**
    check=True           Which throws an exception if an error occurs.  The exception
    type `subprocess.CalledProcessError <https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError>`_

    :param params: a variable list of parameters
    :return: A named tuple version of `subprocess.CompletedProcess <https://docs.python.org/3/library/subprocess.html>`_
             that translates the stdout and stderr with str( 'utf-8')

    Example Call

    ::

        result = run_command('ls', '-la')
        print(f'result.args: {result.args}')
        print(f'result.returncode: {result.returncode}')
        print(f'result.stdout: {result.stdout}')
        print(f'result.stderr: {result.stderr}')


    """
    try:
        result = subprocess.run(params, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        raise e

    stdout = ""
    if result.stdout:
        stdout = str(result.stdout, 'utf-8')
        if output_on:
            print(stdout)

    stderr = ""
    if result.stderr:
        stderr = str(result.stderr, 'utf-8')

    return CommandResult(
        args=result.args,
        returncode=result.returncode,
        stdout=stdout,
        stderr=stderr
    )


def shell(command: str, silent: bool = False):
    """
    Calls run_command given a command as a single string. Optional silent flag will prevent printing for this
    command and set output_on to the state it was in before running the command.

    :param command: The command to run as a single string.
    :param silent: Optional. Set to True to turn off printing command output.

    """
    volume = output_on
    if silent:
        set_run_output(False)

    try:
        result = run_command(*command.split(' '))
    finally:
        if silent:
            set_run_output(volume)

    return result


def last_word(value: str):
    """
    Splits out the word after the last slash in a string.  K8
    objects are expressed in a path style name

    Example
    -------

    >>> last_word('pods/my-pod')
    'my-pod'
    """
    return value.split('/')[-1:][0]


def view_yaml(fn: str):
    """
    Dumps out yaml file in JSON format for easy viewing. This
    is useful when constructing the body of a request that matches a known yaml format.

    Example
    -------

    >>> view_yaml('tomcat-deploy-dev.yml')
    """
    file = None
    try:
        file = open(fn)
        pprint.pprint(yaml.safe_load(file))

    finally:
        if file is not None:
            file.close()


def read_yaml(fn: str):
    """
    Reads a YAML file and returns the resulting the object.

    Example
    -------

    >>> read_yaml('tomcat-deploy-dev.yml')

    """
    file = None
    try:
        file = open(fn)
        return yaml.safe_load(file)

    finally:
        if file is not None:
            file.close()


def get_age(creation_time: datetime):
    """
    Given a creation timestamp, return the difference in time from now.

    :param creation_time: The time we want to measure age from
    :return: timedelta - the amount of time since creation_time
    """
    now = datetime.now(timezone.utc)
    delta = now - creation_time

    if delta.days > 0:
        return f'{delta.days}d'

    hours = delta.seconds/3600

    seconds = delta.seconds % 3600

    minutes = seconds/60
    seconds = seconds % 60

    return '%02d:%02d:%02d' % (hours, minutes, seconds)


def abs_path(file: str):
    """
    Sets an absolute path relative to the **k9** package directory.

    Example::
        result = abs_path('myfile')

    Result::
        /Users/simon/git/k9/k9/myfile


    This is used primarily for building unit tests within the K9 package
    and is not expected to be useful to K9 library users.

    :param file: File or directory to attach absolute path with
    :return: absolute path to specified file or directory
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, file)


def refresh_kubeconfig():
    """
    Refreshes the configuration found in the kubeconfig. Useful for EKS (and similar systems) where the 'user' command generates a token.
    In EKS, that token is viable for 15 minutes, and we have some long tasks that, when combined, may go over that time limit.
    """
    if os.getenv('automated') == '1':
        kube_config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))
        try:
            os.environ["AWS_ACCESS_KEY_ID"] = os.environ['K9_ROLE_ID']
            os.environ["AWS_SECRET_ACCESS_KEY"] = os.environ['K9_ROLE_KEY']
            os.environ["AWS_SESSION_TOKEN"] = os.environ['K9_ROLE_TOKEN']
            assume_role = shell(f'aws sts assume-role --role-arn {os.environ["EKS_ACCESS_ROLE_ARN"]} --role-session-name jenkins-session',
                                silent=True)
            assume_role_dict = json.loads(assume_role.stdout)
            os.environ["AWS_ACCESS_KEY_ID"] = assume_role_dict["Credentials"]['AccessKeyId']
            os.environ["AWS_SECRET_ACCESS_KEY"] = assume_role_dict["Credentials"]['SecretAccessKey']
            os.environ["AWS_SESSION_TOKEN"] = assume_role_dict["Credentials"]['SessionToken']
        except subprocess.CalledProcessError as e:
            # failed to assume access role which means access role is still active
            print(e.stderr)
            set_run_output(True)
        except KeyError:
            # k9 role not set to env variable yet
            set_run_output(True)
        return

    if os.getenv('KUBERNETES_SERVICE_HOST') and not os.getenv('USE_INHABITED_CLUSTER', 'FALSE') == 'TRUE':
        # need to check if it's a) a worker and b) working for the cluster in kubectl
        kube_config.load_incluster_config()
    else:
        kube_config.load_kube_config()
    time.sleep(2)


current_cluster = None


def connect_to_cluster(cluster_name: str):
    """
    Switches to connect to another cluster if needed.

    :param cluster_name: The cluster to connect to.
    """
    global current_cluster
    if current_cluster == cluster_name:
        refresh_kubeconfig()
        return
    try:
        run_command("aws", "eks", "update-kubeconfig", "--name", f"{cluster_name}-cluster")
        refresh_kubeconfig()
        current_cluster = cluster_name
        print(f'Connected to {cluster_name}-cluster')
    except Exception as e:
        print(
            f'ERROR: An exception was encountered while attempting to connect to the cluster with name {cluster_name}. '
            f'Please verify that this cluster exists.')
        print(e)
        raise e


def render_template(template_path: str, file_name: str, params: dict):
    """
    Returns the Jinja formatted template given the directory, file name, and parameters.

    :param template_path: relative path from the k9 source directory. ex: yaml/access-role
    :param file_name: full file name of the template
    :param params: dictionary of key value pairs to insert into template

    :returns: The template body after being rendered.
    """
    env = Environment(loader=FileSystemLoader(abs_path(template_path)), autoescape=True)
    template = env.get_template(file_name)
    return template.render(params)


###########################################################################
# Namespaces
###########################################################################

def set_default_namespace(namespace: str = None):
    """
    Sets the default namespace for all functions that need namespace.

    Most of the functions in this library will require a namespace parameter.
    If the namespace is not provided, the default namespace you set will
    be used instead, simplifying the call.

    Typically, this should be one of the first calls you make when
    working with this library.

    :param: The name of the default namespace. If none, we use "default"
    """
    global default_namespace
    if namespace is None:
        namespace = 'default'
    default_namespace = namespace


def get_default_namespace():
    """
    Gets the default namespace set using set_default_namespace().

    :return: The default namespace's name
    """
    global default_namespace
    if default_namespace is None or default_namespace == '':
        raise RuntimeError("You must call set_default_namespace() first before using most of the K9 API functions.")

    return default_namespace


def default_namespace_exists():
    """
    Returns true if the default namespace exists.

    :return: True if the default namespace exists.
    """
    return namespace_exists(get_default_namespace())


def list_namespaces():
    """
    Retrieves a list of namespaces and associated status.  Returns same
    information as `kubectl get namespaces`

    :return: list of dictionaries with **name** and **status**
    """

    return [
        {
            'name': namespace.metadata.name,
            'status': namespace.status.phase,
            'age': get_age(namespace.metadata.creation_timestamp)
        }
        for namespace in client.CoreV1Api().list_namespace().items
    ]

def get_namespace(namespace: str = None):
    """
    Gets an object that holds detailed information about the supplied namespace.

    :param namespace: Namespace to retrieve.  If None, will use default namespace.
    :return: `V1Namespace <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Namespace.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.CoreV1Api().read_namespace(namespace)


def namespace_exists(namespace: str = None):
    """
    Determines if the specified namespace exists.

    :param namespace: The namespace to check for.  If None, then the default namespace is used.
    :return: bool - True if namespace exists
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_namespace(namespace)
        return result.status.phase == 'Active' and result.metadata.name == namespace

    except:
        return False


def create_namespace(namespace: str = None):
    """
    Creates the specified namespace.

    :param namespace: Specifies the namespace to create.  If None, then the default namespace is used.
    :return: `V1Namespace <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Namespace.md>`_
    """

    if namespace is None:
        namespace = get_default_namespace()

    body = \
        {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": namespace,
            }
        }

    return client.CoreV1Api().create_namespace(body)

def delete_namespace(namespace: str = None):
    """
    Deletes the specified namespace.

    :param namespace: Namespace to delete.  If None, the default namespace is used.
    :return: None if namespace doesn't exist, otherwise `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if not namespace_exists(namespace):
        return None

    client.CoreV1Api().delete_namespace(namespace)

    # wait for namespace to be gone
    try:
        while get_namespace(namespace) is not None:
            time.sleep(1)

    except client.rest.ApiException as e:
        # spec found here: https://github.com/kubernetes-client/python/blob/master/kubernetes/client/rest.py
        if "Not Found" not in e.reason:
            raise


###########################################################################
# Nodes
###########################################################################

def list_nodes():
    """
    Retrieve a list of nodes
    
    :return: Return a list of nodes - each node represented by a dictionary with **name**, **status**, **ip**, **label**, **reason**, and **start_time**
    """
    return [
        {
            'name': node.metadata.name,
            'status': node.status.phase,
            'info': node.status.node_info
        }
        for node in client.CoreV1Api().list_node().items
    ]

def get_node(name: str):
    """

    :param name: The name of the node
    :return: Return information related to the node
    """
    selector = 'metadata.name=' + name
    return [
        {
            'name': node.metadata.name,
            'status': node.status.phase,
            'info': node.status.node_info
        }

        for node in client.CoreV1Api().list_node(field_selector=selector).items
    ]


###########################################################################
# Pods
###########################################################################

def list_pods(namespace: str = None):
    """
    List all pods in a given namespace

    :param namespace: Namespace to search.  If None, uses the default namespace
    :return: Returns a list of pods - each pod represented by a dictionary with **name**, **status**, **ip**, **node**, **labels**, **reason**, and **start_time**
    """
    if namespace is None:
        namespace = get_default_namespace()

    pod_list = client.CoreV1Api().list_namespaced_pod(namespace)
    ret = []
    for pod in pod_list.items:
        ready = False
        if not pod.status.start_time:
          pod.status.start_time = datetime.now(timezone.utc)
        for cond in pod.status.conditions:
            if cond.type == 'Ready':
                ready = (cond.status == 'True')
                break
        ret.append({
              'name': pod.metadata.name,
              'status': pod.status.phase,
              'ready': ready,
              'ip': pod.status.pod_ip,
              'labels': pod.metadata.labels,
              'reason': pod.status.reason,
              'node': pod.spec.node_name,
              'age': get_age(pod.status.start_time)
        })
    return ret

def copy_to_pod(pod: str, host_fn: str, dest_fn: str, namespace: str = None):
    """
    Copies a file to the specified pod.
    
    Example::
        copy_to_pod('jenkins-12345', '.output/jenkins_config.xml', '/var/jenkins_home/some_config.xml')
    
    :param pod: The name of the pod you're copying the file into
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param host_fn: The filename, relative to the execution folder
    :param dest_fn: The desired location + filename on the pod.

    This function doesn't return anything if successful. It throws errors if the file does not exist on the host, the file already exists on the pod, or if the pod name is invalid.
    """
    try:
        if not namespace:
            namespace = get_default_namespace()
        run_command('kubectl', 'cp', host_fn, f'{namespace}/{pod}:{dest_fn}')
    except Exception as e:
        print(e)

def copy_from_pod(pod: str, host_fn: str, dest_fn: str, namespace: str = None):
    """
    This is used for copying a file from inside a pod to the host machine.
    
    Example::
        copy_from_pod('jenkins-12345', '/var/jenkins_home/some_config.xml', '.output/jenkins_config.xml')

    :param pod: The name of the pod you're copying the file from
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param host_fn: The location + filename on the pod.
    :param dest_fn: The destination file relative to the folder we're executing from.

    This function doesn't return anything if successful. It throws errors if the pod or file (on the pod) doesn't exist. This overwrites files on the host machine, unlike copy_to_pod()
    """
    try:
        if not namespace:
            namespace = get_default_namespace()
        run_command('kubectl', 'cp', f'{namespace}/{pod}:{host_fn}', dest_fn)
    except Exception as e:
        print(e)

def wait_for_pod(pod: str, namespace: str = None, interval: int = 10, timeout: int = 240):
    """
    Waits for a pod to be ready. Generally used when we need to use an API or get a file to/from the pod for configuration.

    Example::
        wait_for_pod('jenkins-asdf123')
    
    :param pod: The name of the pod we're waiting on
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param interval: How long to wait between checks (in seconds)
    :param timeout: How many seconds to wait (in total) before timing out the operation

    :return: If the pod is ready/running (True) or if it isn't ready by the timeout (False)
    """
    time.sleep(5)
    ready = False
    for i in range(timeout // interval + 1):
        pods = list_pods(namespace)
        for p in pods:
            if p['name'] == pod:
                ready = p['ready']
        if ready:
            return True
        if i <= timeout // interval:
            print(f'waiting for {pod} to be ready')
            time.sleep(interval)
    return False

def get_pod_logs(pod: str, container: str = None, tail: int = None, namespace: str = None):
    """
    Returns the logs of a pod.

    :param pod: The name of the pod with the logs you would like to read
    :param container: The name of the container in the pod you would like to read
    :param tail: The number of lines to show, starting from the most recent line. If none, all lines of the pod are returned.
    :param namespace: The namespace that pod is in. If None, the default namespace is used.
    """

    if namespace is None:
        namespace = get_default_namespace()

    if tail and tail < 1:
        tail = None
    
    pods = list_pods(namespace)
    pod_exists = False
    for p in pods:
        if p['name'] == pod:
            pod_exists = True
            break
    if not pod_exists:
        raise Exception("The pod you specified in get_pod_logs does not exist in the namespace you provided (or the default namespace, if you didn't provide one).")
    
    return client.CoreV1Api().read_namespaced_pod_log(name = pod, namespace = namespace, container = container, tail_lines = tail)


###########################################################################
# Secrets
###########################################################################

def list_secrets(namespace: str = None):
    """
    Lists secrets in a given namespace.

    :param namespace: Namespace you want to search.  If None, the default namespace is used.
    :return: A list of dictionaries with **name**, **type**, **data** (for number of entries), and **age**
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': secret.metadata.name,
            'type': secret.type,
            'data': len(secret.data),
            'age': get_age(secret.metadata.creation_timestamp)
        }
        for secret in client.CoreV1Api().list_namespaced_secret(namespace).items
    ]


def secret_exists(name: str, namespace: str = None):
    """
    Determines if a secret exists.

    :param name: Name of secret
    :param namespace: Namespace to search, if None, uses default namespace
    :return: True if specfied secret exists.
    """
    if namespace is None:
        namespace = get_default_namespace()

    try:
        result = get_secret(name, namespace)
        return result.metadata.name == name

    except:
        return False


def get_secret(name: str, namespace: str = None):
    """
    Gets a secret's metadata and value(s).

    :param name: Name of secret
    :param namespace: Namespace to search, if None, uses default namespace
    :return: None if not found, otherwise `V1Secret <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Secret.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.CoreV1Api().read_namespaced_secret(name, namespace)


def create_secret(name: str, secrets: dict, namespace: str = None):
    """
    Creates a secret.

    :param name: Name of secret
    :param secrets: Dictionary containing name value pairs of secrets
    :param namespace:
    :return: `V1Secret <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Secret.md>`_

    Example::

        # Note that you should not embed secrets in your source code, this is
        # simply to illustrate how the function call works.
        secret_name = "tomcat-dev"
        secrets = {
            'ds-url': 'https://some/url',
            'password': 'My1SecretPassword',
            'username': 'postgres'
        }

        # Test create_secret()
        result = create_secret(secret_name, secrets)

    Output::

        {'api_version': 'v1',
         'data': {'ds-url': 'aHR0cHM6Ly9zb21lL3VybA==',
                  'password': 'TXkxU2VjcmV0UGFzc3dvcmQ=',
                  'username': 'cG9zdGdyZXM='},
         'kind': 'Secret',
         'metadata': {'annotations': None,
                      'cluster_name': None,
                      'creation_timestamp': datetime.datetime(2019, 10, 17, 17, 20, 56, tzinfo=tzutc()),
                      'deletion_grace_period_seconds': None,
                      'deletion_timestamp': None,
                      'finalizers': None,
                      'generate_name': None,
                      'generation': None,
                      'initializers': None,
                      'labels': None,
                      'managed_fields': None,
                      'name': 'tomcat-dev',
                      'namespace': 'default',
                      'owner_references': None,
                      'resource_version': '2053051',
                      'self_link': '/api/v1/namespaces/default/secrets/tomcat-dev',
                      'uid': '7ab378c0-f102-11e9-a715-025000000001'},
         'string_data': None,
         'type': 'Opaque'}
    """
    if namespace is None:
        namespace = get_default_namespace()

    body = client.V1Secret()
    body.api_version = 'v1'
    body.kind = 'Secret'
    body.metadata = {'name': name}
    body.string_data = secrets
    body.type = 'Opaque'

    return client.CoreV1Api().create_namespaced_secret(namespace, body)


def delete_secret(name: str, namespace: str = None):
    """
    Delete specified secret.

    :param name: Name of secret to delete.
    :param namespace: Namespace to delete from.  If None, default namespace is used.
    :return: `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_ if secret exists, if not, None.
    """
    if namespace is None:
        namespace = get_default_namespace()

    if secret_exists(name, namespace):
        return client.CoreV1Api().delete_namespaced_secret(name, namespace)
    else:
        return None


###########################################################################
# Services
###########################################################################

def list_services(namespace: str = None):
    """
    Lists the services in the namespace.

    :param namespace: Namespace to list services from.  If None, default namespace will be used.
    :return: List of dictionaries with **name**, **type**, **cluster-ip**, **external-ips**, **ports**, and **age**
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': svc.metadata.name,
            'type': svc.spec.type,
            'cluster-ip': svc.spec.cluster_ip,
            'external-ips': svc.spec.external_i_ps,
            'ports': [
                f'{port.target_port}/{port.protocol}'
                for port in svc.spec.ports
            ],
            'age': get_age(svc.metadata.creation_timestamp)
        }
        for svc in client.CoreV1Api().list_namespaced_service(namespace).items
    ]


def service_exists(name: str, namespace: str = None):
    """
    Checks existence of specified service.

    :param name: Name of service.
    :param namespace: Namespace to get service from.  If None, will use default namespace.
    :return: True if service exists.
    """
    if namespace is None:
        namespace = get_default_namespace()
    try:
        result = get_service(name, namespace)

        return result.metadata.name == name
    except:

        return False

def get_service(name: str, namespace: str = None):
    """
    Retrieves details on the specified service.

    :param name: Name of service to get.
    :param namespace: Namespace to get service from.  If None, will use default namespace.
    :return: `V1Service <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.CoreV1Api().read_namespaced_service(name, namespace)

def create_service(body: dict, namespace: str = None):
    """
    Creates a service based on definition provided by **body**.

    :param body:  Service description: https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md
    :param namespace: Namespace to create service in.  If None, will use default namespace.
    :return: `V1Service <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md>`_

    You'll most likely create a YAML file to describe your service and read that in.  You can use
    read_yaml() to generate the body as follows:

    Example::

        result = create_service(read_yaml('my-service.yaml'))

    Sample YAML file::

        apiVersion: v1
        kind: Service
        metadata:
          name: tomcat-svc-dev
          labels:
                svc: tomcat
                env: dev
        spec:
          type: ClusterIP
          ports:
          - port: 8080
            targetPort: 8080
            protocol: TCP
          selector:
                app: tomcat
                env: dev
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.CoreV1Api().create_namespaced_service(namespace=namespace, body=body)


def delete_service(name: str, namespace: str = None):
    """
    Deletes the specified service.  This function will check whether the service exists before attempting the delete.

    :param name: Name of service to delete
    :param namespace: Namespace to delete from.  If None, default namespace is used.
    :return: None if service doesn't exist, otherwise `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if service_exists(name, namespace):
        return client.CoreV1Api().delete_namespaced_service(name, namespace)
    else:
        return None


###########################################################################
# Service Accounts
###########################################################################

def list_service_accounts(namespace: str = None):
    """
    Lists service accounts in a namespace.

    :param namespace: The namespace to list accounts from. If None, we use the default namespace.
    :return: A list of every service account in the namespace.

    Example Output::
    
        [
          {
            'name': 'elastic-sa',
            'age': 123456789
          },
          {
            'name': 'fluent-sa',
            'age': 123456999
          }
        ]
    """
    if namespace is None:
        namespace = get_default_namespace()

    result = client.CoreV1Api().list_namespaced_service_account(namespace)

    return [
        {
            'name': sa.metadata.name,
            'age': get_age(sa.metadata.creation_timestamp)
        }
        for sa in result.items
    ]


def create_service_account(name: str, namespace: str = None):
    """
    Create a service account.

    :param name: Name of service account.
    :param namespace: namespace to create service account in.  If None, create service account in default namespace
    :return: `V1ServiceAccount <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ServiceAccount.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    body =\
        { 'apiVersion': 'v1',
          'kind': 'ServiceAccount',
          'metadata' : { 'name': name }
        }

    return client.CoreV1Api().create_namespaced_service_account(namespace, body)

def get_service_account(name: str, namespace: str = None):
    """
    Get details of specified service account

    :param name: Name of service account to retrieve.
    :param namespace: Namespace to retrieve service account from. If None, retrieve from default namespace.
    :return: `V1ServiceAccount <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ServiceAccount.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return client.CoreV1Api().read_namespaced_service_account(name, namespace)


def service_account_exists(name: str, namespace: str = None):
    """
    Checks for existence of service account

    :param name: Name of service account to look for.
    :param namespace: Namespace to look in.  If None, look in default namespace.
    :return: True if specified account exists.
    """
    if namespace is None:
        namespace = get_default_namespace()

    try:
        result = get_service_account(name, namespace)
        return result.metadata.name == name

    except:
        return False


def delete_service_account(name: str, namespace: str = None):
    """
    Delete specified service account.

    :param name: Name of service account to delete.
    :param namespace: Namespace to delete from.  If None, delete from default namespace.
    :return: None if service account doesn't exists, otherwise returns `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if service_account_exists(name, namespace):
        return client.CoreV1Api().delete_namespaced_service_account(name, namespace)
    else:
        return None


###########################################################################
# ConfigMaps
###########################################################################

def create_configmap(body: dict, namespace: str = None):
    """
    Creates a new configmap.

    :param body: the body to create the configmap with
    :param namespace: the namespace to create in. If not supplied, we use the default namespace.
    """
    if namespace is None:
        namespace = get_default_namespace()
    return client.CoreV1Api().create_namespaced_config_map(namespace, body)


def list_configmap(namespace: str = None):
    """
    Lists configmaps present in the namespace.

    :param namespace: the namespace to search in. If not supplied, we use the default namespace.
    :return: a list of configmaps
    """
    if namespace is None:
        namespace = get_default_namespace()
    return client.CoreV1Api().list_namespaced_config_map(namespace).items


def get_configmap(name: str, namespace: str = None):
    """
    Gets a configmap with the supplied name.
    
    :param name: the name of the configmap we're searching for
    :param namespace: the namespace to search in. If not supplied, we use the default namespace.
    :return: the requested configmap. Returns False if the configmap does not exist.
    """
    if namespace is None:
        namespace = get_default_namespace()
    try:
        return client.CoreV1Api().read_namespaced_config_map(name, namespace)
    except:
        return False


def delete_configmap(name: str, namespace: str = None):
    """
    Deletes a configmap with the supplied name.

    :param name: the name of the configmap we're deleting
    :param namespace: the namespace to delete the configmap from. If not supplied, we use the default namespace.
    :return: if the configmap isn't found, we return False. Otherwise, we return the status object generated by k8s upon deletion.
    """
    if namespace is None:
        namespace = get_default_namespace()
    if get_configmap(name, namespace):
        return client.CoreV1Api().delete_namespaced_config_map(name, namespace)
    return False


def update_configmap(name: str, body: dict, namespace: str = None):
    """
    Patches a configmap with the supplied name.

    :param name: the name of the configmap we're patching.
    :param body: the new body of the configmap.
    :param namespace: the namespace to patch the configmap in. If not supplied, we use the default namespace.
    """
    if namespace is None:
        namespace = get_default_namespace()
    if get_configmap(name, namespace):
        return client.CoreV1Api().patch_namespaced_config_map(name, namespace, body)


###########################################################################
# AWS Auth - Use on EKS for IAM authentication
###########################################################################

def add_aws_auth_user(iam_user: str, kube_user: str, groups: list = []):
    """
    Adds a user to the aws_auth configmap. Attaches the provided username and groups to their iam user.

    :param iam_user: the iam user arn to allow access to the cluster.
    :param kube_user: the kubernetes username to associate with the iam user (for role binding purposes).
    :param groups: the groups to add the user to. Fine to leave empty if you're giving someone limited access just through role + binding.
    :return: the updated aws-auth configmap
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapUsers', '[]'))
    auth_yaml.append({
      'userarn': iam_user,
      'username': kube_user,
      'groups': groups
    })

    output = yaml.dump(auth_yaml)
    auth.data['mapUsers'] = output
    return update_configmap('aws-auth', auth ,'kube-system')


def add_aws_auth_role(iam_role: str, kube_user: str, groups: list = []):
    """
    Adds a role to the aws_auth configmap. Attaches the provided username and groups to their iam role.

    :param iam_role: the iam role arn to allow access to the cluster.
    :param kube_user: the kubernetes username to associate with the iam role (for role binding purposes).
    :param groups: the groups to add the role to. Fine to leave empty if you're giving someone limited access just through role + binding.
    :return: the updated aws-auth configmap
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapRoles', '[]'))
    auth_yaml.append({
      'rolearn': iam_role,
      'username': kube_user,
      'groups': groups
    })

    output = yaml.dump(auth_yaml)
    auth.data['mapRoles'] = output
    return update_configmap('aws-auth', auth ,'kube-system')


def get_aws_auth_user(iam_user: str = None, kube_user: str = None):
    """
    Returns the entry in aws-auth for the supplied iam user or kube username. If you give both, we search for the iam user!

    return format:
    {
      'userarn': 'arn::asdf',
      'username': 'k8s-username',
      'groups': ['system:masters', 'whatever']
    }

    :param iam_user: the iam user arn we're looking for
    :param kube_user: the kubernetes username associated with the iam user we're looking for
    :return: the userarn, username, and groups associated with the supplied user/username (as a dict)
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapUsers', '[]'))
    for m in auth_yaml:
        if (iam_user and m.get('userarn', False) == iam_user) or (kube_user and m.get('username', False) == kube_user):
            return m
    return False


def get_aws_auth_role(iam_role: str = None, kube_user: str = None):
    """
    Returns the entry in aws-auth for the supplied iam role or kube username. If you give both, we search for the iam role!

    return format:
    {
      'rolearn': 'arn::asdf',
      'username': 'k8s-username',
      'groups': ['system:masters', 'whatever']
    }

    :param iam_role: the iam role arn we're looking for
    :param kube_user: the kubernetes username associated with the iam user we're looking for
    :return: the rolearn, username, and groups associated with the supplied role/username (as a dict)
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapRoles', '[]'))
    for m in auth_yaml:
        if (iam_role and m.get('rolearn', False) == iam_role) or (kube_user and m.get('username', False) == kube_user):
            return m
    return False


def delete_aws_auth_user(iam_user: str = None):
    """
    Deletes an IAM user from aws-auth.

    :param iam_user: the iam user arn to remove from aws-auth.
    :return: the aws-auth configmap post-removal
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapUsers', '[]'))
    for m in auth_yaml:
        if iam_user == m.get('userarn', False):
            auth_yaml.remove(m)
            if len(auth_yaml) == 0:
                auth.data['mapUsers'] = None
            else:
                auth.data['mapUsers'] = yaml.dump(auth_yaml)
            return update_configmap('aws-auth', auth, 'kube-system')
    return False


def delete_aws_auth_role(iam_role: str = None):
    """
    Deletes an IAM role from aws-auth

    :param iam_role: the iam role arn to remove from aws-auth.
    :return: the aws-auth configmap post-removal
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapRoles', '[]'))
    for m in auth_yaml:
        if iam_role == m.get('rolearn', False):
            auth_yaml.remove(m)
            if len(auth_yaml) == 0:
                auth.data['mapRoles'] = None
            else:
                auth.data['mapRoles'] = yaml.dump(auth_yaml)
            return update_configmap('aws-auth', auth, 'kube-system')
    return False


def update_aws_auth_user(iam_user: str, kube_user: str = None, groups: list = []):
    """
    Changes the groups and/or kube user associated with a given iam user.

    :param iam_user: the user whose permissions we are modifying
    :param kube_user: if supplied, the user's kubernetes user association will be changed to this new username
    :param groups: if supplied, the user's groups will be replaced with this list 
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapUsers', '[]'))
    for m in auth_yaml:
        if iam_user == m.get('userarn', False):
            auth_yaml.remove(m)
            if not kube_user:
                kube_user = m.get('username')
            if not groups:
                groups = m.get('groups')
            auth_yaml.append({
              'userarn': iam_user,
              'username': kube_user,
              'groups': groups
            })
            auth.data['mapUsers'] = yaml.dump(auth_yaml)
            return update_configmap('aws-auth', auth, 'kube-system')
    return False


def update_aws_auth_role(iam_role: str, kube_user: str = None, groups: list = []):
    """
    Changes the groups and/or kube user associated with a given iam role.

    :param iam_role: the role whose permissions we are modifying
    :param kube_user: if supplied, the role's kubernetes user association will be changed to this new username
    :param groups: if supplied, the role's groups will be replaced with this list 
    """
    auth = get_configmap('aws-auth', 'kube-system')
    auth_yaml = yaml.safe_load(auth.data.get('mapRoles', '[]'))
    for m in auth_yaml:
        if iam_role == m.get('rolearn', False):
            auth_yaml.remove(m)
            if not kube_user:
                kube_user = m.get('username')
            if not groups:
                groups = m.get('groups')
            auth_yaml.append({
              'rolearn': iam_role,
              'username': kube_user,
              'groups': groups
            })
            auth.data['mapRoles'] = yaml.dump(auth_yaml)
            return update_configmap('aws-auth', auth, 'kube-system')
    return False

###########################################################################
# Application Databases
###########################################################################


def create_app_databases(app_config: dict):
    '''
    Create application databases based on the app-config.yml file in the path.

    :param app_config: config dictionary as read from your app-config.yml file

    :return: A tuple containing 3 lists of database names and a list of lambda delete waiting functions.
    The first corresponds to those that had no action performed on them.
    The second corresponds to those that were created/deleted successfully.
    The third corresponds to those that encountered errors when attempting to create/delete.
    The fourth is a list of waiting functions to call when done executing to make sure the lambdas are deleted.
    '''

    if not app_config:
        raise ValueError('The application configuration is required.')
    app_name = app_config.get('appName', None)
    if not app_name:
        raise ValueError('The appName is required.')
    deployments = app_config.get('deployments', [])
    total_no_action, total_successful, total_failure = [], [], []
    for cluster in deployments:
        cluster_name = cluster['clusterName']
        environments = cluster['environments']
        database_infos = []
        for environment in environments:
            env = environment.get('env', '')
            if not env:
                raise ValueError('The env key is required for each deployment.')
            customers = environment.get('customers',[])
            schemas = list(map(lambda c, environ=env: (environ + '_' + app_name + '_' + c) , customers))
            schemas = list(dict.fromkeys(schemas)) # remove duplicates
            database_name = env + "_" + app_name
            rds_instance = environment.get('rdsInstance', '')
            data = {
                'function': 'create',
                'database': database_name.replace('-', '_'),
                'env': env,
                'appName': app_name,
            }
            if len(schemas) > 0:
                data['schemas'] = schemas
            if rds_instance != '':
                data['rdsInstance'] = rds_instance
            database_infos.append(data)
        no_action, success, failure = rds.create_lambda(cluster_name=cluster_name, database_infos=database_infos)
        total_no_action.extend(no_action)
        total_successful.extend(success)
        total_failure.extend(failure)
    return total_no_action, total_successful, total_failure


def delete_app_database(cluster_name: str, app_name: str, env: str, rds_instance: str = None):
    '''
    Delete an application database on a cluster's RDS instance.
    Delete is idempotent. A normal return simply indicates that the database now does not exist, regardless if it existed before

    :param cluster_name: The cluster name
    :param app_name: The application name
    :param env: The associated environment
    :param rds_instance: The RDS instance to use for the lambda (optional - helpful when there is more than one RDS instance for a cluster)
    '''
    if not cluster_name or not env or not app_name:
        raise ValueError('All parameters except rds_instance are required')
    database_name = env + "_" + app_name
    tags = {
        'clusterName': cluster_name,
        'databaseName': database_name,
        'env': env,
        'appName': app_name,
        'userType': 'Master',
        'secretType': 'Application database user credentials'
    }
    if secret.secret_exists_by_tags(tags=tags) != True:
        # We consider "inconclusive" to be false. This list of tags is the most specific we can get, and the function will always return a result unless the tags in the secrets are manually modified.
        # If owner secret doesn't exist we can't access the database (RDS instance can be accessed by the master user, but it can only drop users. The database needs to be dropped first).
        print(f'Password secret for the owner user of app database {database_name} does not exist.')
        return None, None, None
    data = {
        'function': 'delete',
        'database': database_name.replace('-', '_'),
        'env': env,
        'appName': app_name
    }
    if rds_instance:
        data['rds_instance'] = rds_instance
    try:
        no_action, successful, failure = rds.create_lambda(cluster_name=cluster_name, database_infos=[data])
    except Exception as e:
        print(f'App database with name {database_name} was not deleted.')
        print(e)
        raise e
    return no_action, successful, failure
