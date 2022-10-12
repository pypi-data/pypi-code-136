import base64
import json
import os, time
import pathlib
import subprocess

from kubernetes import client, config as kube_config
import requests
from urllib3.exceptions import InsecureRequestWarning

from jinja2 import Environment, FileSystemLoader
from k9.helm import helm_install, helm_repo_add, helm_repo_update, helm_exists, helm_uninstall
from k9.core import namespace_exists, set_default_namespace, create_namespace, abs_path, list_pods, wait_for_pod, \
    run_command, read_yaml, set_run_output, refresh_kubeconfig, get_secret, \
    create_app_databases, delete_app_database, secret_exists, create_secret, connect_to_cluster, shell, render_template
from k9.storage import storage_class_exists
from k9.apps import deployment_exists, create_deployment

from aws import cluster, cfm, cert, ec2, secret, iam, util, rds, region

SIMON_CHARTS = 'https://charts.simoncomputing.com'


# util for jinja'ing XML
def write_templated_config(name: str, env, params):
    if not isinstance(params, dict):
        params = vars(params)
    template = env.get_template(name)
    template_body = template.render(params)
    if not os.path.exists('./.output/config'):
        if not os.path.exists('./.output'):
            os.mkdir('./.output')
        os.mkdir('./.output/config')
    path = f'./.output/config/{name}'

    f = open(path, 'w+')
    f.write(template_body)
    f.close()
    return f'./.output/config/{name}'


def get_alb_controller_image_repo():
    """
    ALB Controller installation needs to get its image from the same region the cluster is deployed in.
    https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases

    :returns: ECR url for the current region to pass into helm value image.repo
    """
    current_region = region.get_default_region()

    repos = {
        'us-gov-east-1': '151742754352.dkr.ecr.us-gov-east-1.amazonaws.com/amazon/aws-load-balancer-controller',
        'us-gov-west-1': '013241004608.dkr.ecr.us-gov-west-1.amazonaws.com/amazon/aws-load-balancer-controller',
        'us-east-1': '602401143452.dkr.ecr.us-east-1.amazonaws.com/amazon/aws-load-balancer-controller'
    }

    if current_region not in repos:
        print('Using us-east-1 image for ALB Controller. If the install fails to ready, check '
              'https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases for your region and fix with'
              'the following command.')
        print('helm upgrade aws-load-balancer-controller --set image.repository=<REPO_WITHOUT_IMAGE_TAG> --reuse-values simoncomputing/aws-load-balancer-controller -n kube-system')

        # vast majority of regions can use the same as us-east-1 (all non-gov us regions)
        current_region = 'us-east-1'

    return repos[current_region]


def install_aws_load_balancer_controller(params: dict):
    """
    Installs the ALB controller helm chart and waits for the pods to ready.

    :param params: a dictionary containing the params to insert into the chart's values.yaml

    :returns: None on success. Error if install fails.
    """
    if not helm_exists('aws-load-balancer-controller', 'kube-system'):
        params['albRepoUrl'] = get_alb_controller_image_repo()
        namespace = 'kube-system'
        helm_install('simoncomputing/aws-load-balancer-controller', params,
                     values_path=abs_path('yaml/aws-load-balancer-controller-values.yml'), namespace=namespace,
                     debug=False)

        alb_pod = ''
        # get pod
        attempts = 0
        while attempts < 5:
            time.sleep(15)
            pods = list_pods(namespace)
            for p in pods:
                if p.get('name', '').find('aws-load-balancer-controller') != -1:
                    alb_pod = p.get('name', False)
                    break
            attempts += 1

        # wait for pod to be ready
        if not wait_for_pod(alb_pod, namespace, timeout=300):
            raise ValueError('aws-load-balancer-controller did not ready')


def install_aws_tools(params: dict):
    """
    Installs charts/deployments from/for AWS resources. These are a storage class corresponding to EBS volumes,
    EKS autoscaling parameters, and the ALB/ingress controller
    
    :param params: a dictionary containing the params to insert into the charts' values.yaml
    :return: True on success, exception if failure.
    """
    set_run_output(False)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_default_namespace('default')
    set_run_output(True)
    if not storage_class_exists('standard'):
        print('storage class: "standard" not found. Creating standard storage class...')
        set_run_output(False)
        result = run_command('kubectl', 'apply', '-f', abs_path('yaml/default-sc.yml'))
        set_run_output(True)
        errors = result.stderr
        if errors:
            print('An error was encountered when creating the standard storage class.')
            raise ValueError(errors)
        print('Standard storage class successfully created.')
        helm_install('simoncomputing/aws-storage', {}, release_name='aws-storage',
                     values_path=abs_path('yaml/aws-storage-values.yml'))
    set_default_namespace('kube-system')
    if not deployment_exists('cluster-autoscaler'):
        env = Environment(loader=FileSystemLoader(abs_path('yaml/autoscaler')), autoescape=True)
        run_command('kubectl', 'apply', '-f', abs_path('yaml/autoscaler/infra.yml'))
        auto_deploy = read_yaml(write_templated_config('deploy.yml', env, params))
        create_deployment(auto_deploy, 'kube-system')

    install_aws_load_balancer_controller(params)

    return True


def install_jenkins(params: dict, namespace='cicd'):
    """
    Installs Jenkins to the current kubernetes environment.

    :param params: a dictionary containing the params to insert into the jenkins chart's values.yaml
    :param namespace: the namespace to install jenkins in. defaults to cluster-tools
    :return: None on success, exception if failure.
    """

    if helm_exists('jenkins', namespace):
        return
    
    helm_params = {
        'clusterName': params.get('clusterName'),
        'baseDomain': params.get('baseDomain'),
        'certArn': params.get('certArn'),
    }
    install_aws_tools(helm_params)

    set_run_output(False)
    set_default_namespace(namespace)
    if not namespace_exists(namespace):
        create_namespace(namespace)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_run_output(True)

    # install chart
    helm_install('simoncomputing/jenkins', params, release_name='jenkins',
                 values_path=abs_path('yaml/jenkins-values.yml'), namespace=namespace)
    # get pod
    time.sleep(1)
    pods = list_pods(namespace)
    jenkins_pod = False
    for p in pods:
        if p.get('name', '').find('jenkins') != -1:
            jenkins_pod = p.get('name', False)
    # wait for pod to be ready
    if not wait_for_pod(jenkins_pod, namespace, timeout=300):
        if jenkins_pod:
            run_command('kubectl', 'describe', 'pod', jenkins_pod, '-n', namespace)
        raise RuntimeError('Jenkins pod did not ready within 5 minutes. '
                           'Please verify that your params are complete and correct.')


def install_efk(params: dict, namespace: str = 'logging'):
    """
    Installs EFK to the current kubernetes environment.

    :param params: a dictionary containing the params to insert into the efk chart's values.yaml
    :param namespace: the namespace to install efk in. defaults to cluster-tools
    :return: None on success, exception if failure.
    """

    if helm_exists('efk', namespace):
        return

    set_run_output(False)
    set_default_namespace(namespace)
    if not namespace_exists(namespace):
        create_namespace(namespace)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_run_output(True)

    # install chart
    helm_install('simoncomputing/efk', params, release_name='efk', values_path=abs_path('yaml/efk-values.yml'),
                 namespace=namespace)
    # get pod
    attempts = 0
    while attempts < 5:
        time.sleep(20)
        pods = list_pods(namespace)
        elastic_pod = False
        for p in pods:
            if p.get('name', '').find('elasticsearch') != -1:
                elastic_pod = p.get('name', False)
                break
        attempts += 1
                
    # wait for pod to be ready
    if not elastic_pod or not wait_for_pod(elastic_pod, namespace, timeout=300):
        raise RuntimeError('Elastic pod did not ready. Please verify that your params are complete and correct.')

    for p in pods:
        if p.get('name', '').find('kibana') != -1:
            kibana_pod = p.get('name', False)
    # wait for pod to be ready
    if not wait_for_pod(kibana_pod, namespace, timeout=300):
        raise RuntimeError('Kibana pod did not ready within 5 minutes. '
                           'Please verify that your params are complete and correct.')


def get_kibana_session(base_domain):
    """
    Returns a request.Session() object with Kibana authorization and headers.

    :param base_domain: baseDomain from cluster-config

    :return: request.Session() object ready to be used for Kibana.
    """
    kibana_secret = get_secret('elasticsearch-master-es-elastic-user', 'logging')
    kibana_password = base64.decodebytes(bytes(kibana_secret.data['elastic'], 'ascii'))

    session = requests.Session()
    session.auth = ('elastic', kibana_password)
    session.headers['kbn-xsrf'] = 'true'
    session.headers['Host'] = f'kibana.{base_domain}'
    session.verify = False
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    return session


def kibana_import_object(session, dns_name: str, file_path: str, overwrite=False, create_new=False):
    """
    Makes an API call to Kibana to post an object.

    :param session: a requests.session object with auth and headers already set up
    :param dns_name: DNS name of the load balancer to route traffic to
    :param file_path: absolute path to the object being posted
    :param overwrite: Replace existing objects if there are conflicts.
    :param create_new: Generate new ids if True. Takes precedent over overwrite parameter.
    If not set and conflicts are found, raises error. Default is False.

    :returns: True if upload succeeds. False otherwise.
    """
    # route to load balancer
    kibana_url = f'https://{dns_name}'

    # wait for service to ready up
    retry = 6
    for _ in range(retry):
        resp = session.get(kibana_url)
        if resp.ok:
            break
        print('waiting for kibana to become available...')
        print(resp.raw)
        time.sleep(10)

    import_url = os.path.join(kibana_url, 'api/saved_objects/_import')

    if create_new:
        params = {
            'createNewCopies': create_new
        }
    else:
        params = {
            'overwrite': overwrite
        }

    with open(file_path, 'rb') as import_file:
        files = {'file': (file_path, import_file)}
        response = session.post(url=import_url, params=params, files=files)
        print(response.status_code)

    try:
        response_body = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Kibana upload failed')
        print(response.reason)
        print(str(e))
        return False

    if not response_body.get('success', False):
        print(response_body)
        return False
    else:
        print('Upload Success')
        return True


def kibana_import_objects(combined_file_path, session, dns_name: str, file_paths, overwrite=False, create_new=False):
    """
    Combines all given files into one combined.ndjson file and then calls kibana_import_object.
    Files are combined to allow references across files. create_new=True changes the ids in file provided. However,
    if the reference is within one file, kibana automatically handles changing the reference.

    :param combined_file_path: The file location to place the combined ndjson file.
    If the file exists, uploading is skipped.
    :param session: a requests.session object with auth and headers already set up
    :param dns_name: DNS name of the load balancer to route traffic to
    :param file_paths: absolute path to the objects being uploaded
    :param overwrite: Replace existing objects if there are conflicts.
    :param create_new: Generate new ids if True. Takes precedent over overwrite parameter.
    If not set and conflicts are found, raises error. Default is False.

    :returns: True if upload succeeds. False otherwise.
    """

    # do not create new dashboards if the combined file already exists, this will duplicate everything
    if os.path.exists(combined_file_path):
        return True

    with open(combined_file_path, 'w+') as output:
        for path in file_paths:
            with open(path, 'r') as input_file:
                output.write(input_file.read())
                output.write('\n')
    return kibana_import_object(session, dns_name, combined_file_path, overwrite, create_new)


def configure_kibana(base_domain: str, dns_name: str):
    """
    Adds the standard cluster dashboard to Kibana.

    :param dns_name: DNS name of the AWS load balancer

    :param base_domain: the baseDomain from the cluster-config. Used to create Kibana urls.

    :returns: True if all uploads succeed. False otherwise.
    """
    session = get_kibana_session(base_domain)

    # create cluster dashboard
    filepath = abs_path('yaml/kibana/cluster-dashboard.ndjson')
    return kibana_import_object(session, dns_name, filepath, overwrite=True)


def install_kibana_app_dashboards(app_dir: str):
    """
    Installs boilerplate Kibana dashboards for the given app.

    :param app_dir: The directory containing app_config.yml for the app.

    :returns: True if all uploads were successful. False otherwise.
    """
    from k9.deploy import read_app_config
    app_config = read_app_config(app_dir)
    app_name = app_config['appName']

    file_names = ['boiler-dashboard', 'boiler-error-dashboard', 'boiler-api-dashboard', 'boiler-performance-dashboard']
    output_file_paths = []
    pathlib.Path(f'{app_dir}/values/kibana').mkdir(parents=True, exist_ok=True)

    # create dashboard files from templates
    for file_name in file_names:
        # read boiler content
        input_path = abs_path(f'yaml/kibana/{file_name}.ndjson')
        with open(input_path, 'r') as boiler_file:
            boiler_content = boiler_file.read()

        # replace 'boiler' with app name
        output_content = boiler_content.replace('boiler', app_name)
        output_name = file_name.replace('boiler', app_name)
        output_path = f'{app_dir}/values/kibana/{output_name}.ndjson'

        # write the templated files to the vales/kibana directory
        output_file_paths.append(output_path)
        with open(output_path, 'w+') as output_file:
            output_file.write(output_content)
        print(f'Created {output_name}.ndjson')

    # files are written, upload to every cluster in app-config
    root_domain = app_config['rootDomain']
    success = True
    for deployment in app_config['deployments']:
        cluster_name = deployment['clusterName']
        connect_to_cluster(cluster_name)
        base_domain = f'{cluster_name}.{root_domain}'
        session = get_kibana_session(base_domain)
        lb = get_cluster_load_balancer(cluster_name)
        print(f'Uploading {app_name} dashboards to {cluster_name}-cluster.')
        combined_file_path = f'{app_dir}/values/kibana/{cluster_name}-combined.ndjson'
        success = success and kibana_import_objects(combined_file_path, session, lb['DNSName'],
                                                    output_file_paths, overwrite=False, create_new=True)

    print('Kibana dashboards installed.') if success else print('Kibana dashboards failed to install')
    return success


def install_sonarqube(params: dict, namespace: str = 'cicd'):
    """
    Installs SonarQube to the current kubernetes environment.

    :param params: a dictionary containing the params to insert into the sonarqube chart's values.yaml
    :param namespace: the namespace to install sonarqube in. defaults to cluster-tools
    :return: None on success, exception if failure.
    """

    if helm_exists('sonarqube', namespace):
        return

    # install chart
    # get pod
    # wait for pod to be ready
    set_run_output(False)
    set_default_namespace(namespace)
    if not namespace_exists(namespace):
        create_namespace(namespace)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_run_output(True)

    # install chart
    helm_install('simoncomputing/sonarqube', params, release_name='sonarqube',
                 values_path=abs_path('yaml/sonarqube-values.yml'), namespace=namespace)
    # get pod
    time.sleep(5)
    pods = list_pods(namespace)
    sonar_pod = False
    for p in pods:
        if p.get('name', '').find('sonarqube-sonarqube') != -1:
            sonar_pod = p.get('name', False)
    # wait for pod to be ready
    if not wait_for_pod(sonar_pod, namespace,
                        timeout=600):  # this one takes around 6 minutes, give or take. so much longer than the rest.
        raise RuntimeError('Sonar pod did not ready within 5 minutes. '
                           'Please verify that your params are complete and correct.')


def install_prometheus(params: dict, namespace: str = 'monitoring'):
    """
    Installs Prometheus to the current kubernetes environment.

    :param params: a dictionary containing the params to insert into the prometheus chart's values.yaml
    :param namespace: the namespace to install prometheus in. defaults to cluster-tools
    :return: None on success, exception if failure.
    """

    if helm_exists('prometheus', namespace):
        return

    # install chart
    # get pod
    # wait for pod to be ready
    set_run_output(False)
    set_default_namespace(namespace)
    if not namespace_exists(namespace):
        create_namespace(namespace)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_run_output(True)

    # install chart
    helm_install('simoncomputing/prometheus', params, release_name='prometheus',
                 values_path=abs_path('yaml/prometheus-values.yml'), namespace=namespace)
    # get pod
    time.sleep(1)
    pods = list_pods(namespace)
    prom_pod = False
    for p in pods:
        if p.get('name', '').find('prometheus') != -1:
            prom_pod = p.get('name', False)
    # wait for pod to be ready
    if not wait_for_pod(prom_pod, namespace, timeout=300):
        raise RuntimeError('Prometheus pod did not ready within 5 minutes. '
                           'Please verify that your params are complete and correct.')


def install_grafana(params: dict, namespace: str = 'monitoring'):
    """
    Installs grafana to the current kubernetes environment.

    :param params: a dictionary containing the params to insert into the grafana chart's values.yaml
    :param namespace: the namespace to install grafana in. defaults to cluster-tools
    :return: None on success, exception if failure.
    """

    if helm_exists('grafana', namespace):
        return

    # install chart
    # get pod
    # wait for pod to be ready
    set_run_output(False)
    set_default_namespace(namespace)
    if not namespace_exists(namespace):
        create_namespace(namespace)
    helm_repo_add('simoncomputing', SIMON_CHARTS)
    helm_repo_update()
    set_run_output(True)

    # install chart
    helm_install('simoncomputing/grafana', params, release_name='grafana',
                 values_path=abs_path('yaml/grafana-values.yml'), namespace=namespace)
    # get pod
    time.sleep(1)
    pods = list_pods(namespace)
    grafana_pod = False
    for p in pods:
        if p.get('name', '').find('grafana') != -1:
            grafana_pod = p.get('name', False)
    # wait for pod to be ready
    if not wait_for_pod(grafana_pod, namespace, timeout=300):
        raise RuntimeError('Grafana pod did not ready within 5 minutes. '
                           'Please verify that your params are complete and correct.')


def create_grafana_post(session, upload_url: str, json: dict, keep_uid=False):
    """
    Sends a POST to the grafana API. Used to upload dashboards and notification channels

    :param session: a requests.session object with auth already set up
    :param upload_url: the exact API url to post to
    :param json: the json object being sent to the API
    :param keep_uid: If set, the uid found in the dashboard specification will be reused. Otherwise, a new one will be generated. Default: False

    :returns: True on Success, False on failure.
    """

    data = json.copy()
    if 'dashboard' in data:
        data['dashboard']['id'] = None
        if not keep_uid:
            data['dashboard']['uid'] = None
    else:
        data['id'] = None
        if not keep_uid:
            data['uid'] = None
    response_body = session.post(upload_url, json=data)
    print(response_body.status_code)

    if response_body.status_code == 412 or response_body.status_code == 409:
        print('Item already exists')
        return True
    elif response_body.status_code == 200:
        print('Upload Success')
        return True
    else:
        print('Upload Failed')
        print(response_body.reason)
        return False


def configure_grafana(base_domain: str, dns_name: str):
    """
    Adds dashboards and notification channels to Grafana.

    :param base_domain: the baseDomain from the cluster-config. Used to create urls.
    :param dns_name: DNS name of the AWS load balancer

    :returns: True if all uploads succeeded. False otherwise.
    """
    # get auth
    refresh_kubeconfig()
    credentials_secret = get_secret('grafana', namespace='monitoring')
    username = base64.decodebytes(bytes(credentials_secret.data['admin-user'], 'ascii'))
    password = base64.decodebytes(bytes(credentials_secret.data['admin-password'], 'ascii'))

    session = requests.Session()
    session.auth = (username, password)
    session.headers['Host'] = f'grafana.{base_domain}'
    session.verify = False
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    dashboards = ['pod-health', 'kubernetes-volume-usage-percentage',
                  # https://grafana.com/grafana/dashboards/1860-node-exporter-full/
                  'node-exporter-full',
                  # https://grafana.com/grafana/dashboards/3831-autoscaler/
                  'kubernetes-cluster-autoscaler',
                  ]
    grafana_path = abs_path('yaml/grafana')

    grafana_url = f'https://{dns_name}'

    # wait for service to ready up
    retry = 6
    for _ in range(retry):
        resp = session.get(grafana_url)
        if resp.ok:
            break
        print('waiting for grafana to become available...')
        print(resp.raw)
        time.sleep(10)

    dashboard_url = os.path.join(grafana_url, 'api/dashboards/db')
    notification_channel_url = os.path.join(grafana_url, 'api/alert-notifications')

    success = True

    for d in dashboards:
        with open(f'{grafana_path}/dashboards/{d}.json') as f:
            d_json = json.load(f)
        if d_json:
            data = {'dashboard': d_json}
            success = success and create_grafana_post(session, dashboard_url, data)
    # notis (this is what calls self healing lambdas, among other things)
    notis = ['google-chat-alert']
    for n in notis:
        with open(f'{grafana_path}/notification-channels/{n}.json') as f:
            n_json = json.load(f)
        if n_json:
            success = success and create_grafana_post(session, notification_channel_url, n_json, keep_uid=True)

    print('Created grafana notification channel: "Google Chat Alert". '
          'Update the Url to your google chat webhook to have notifications turned on.')
    return success


def create_logins_secret(cluster_name: str):
    """
    Puts Kibana, Grafana, Prometheus logins into an AWS secret

    :param cluster_name: the name of the cluster currently connected to. Used to name the secret.
    """

    secret_name = f'{cluster_name}-monitoring-logins-secret'

    if secret.secret_exists(secret_name):
        print(f'{secret_name} already exists')
        return True

    kibana_secret = get_secret('elasticsearch-master-es-elastic-user', 'logging')
    kibana_user = 'elastic'
    kibana_password = base64.b64decode(bytes(kibana_secret.data['elastic'], encoding='utf8')).decode('utf-8')

    grafana_secret = get_secret('grafana', namespace='monitoring')
    grafana_user = base64.b64decode(bytes(grafana_secret.data['admin-user'], encoding='utf8')).decode('utf-8')
    grafana_password = base64.b64decode(bytes(grafana_secret.data['admin-password'], encoding='utf8')).decode('utf-8')

    content = {
        'kibanaUser': kibana_user,
        'kibanaPassword': str(kibana_password),
        'grafanaUser': str(grafana_user),
        'grafanaPassword': str(grafana_password)
    }

    tags = {
        'clusterName': cluster_name,
        'createdWith': 'k9-create-cluster'
    }

    secret.create_secret(secret_name, f'Kibana and Grafana web login credentials for {cluster_name} cluster.',
                         kvp=content, tags=tags, )
    print(f'{secret_name} created. Use may now view the login credentials within that secret.')


def delete_logins_secret(cluster_name: str):
    """
    Deletes secret that holds standard app logins.

    :param cluster_name: the name of the cluster currently connected to. Used to name the secret.
    """
    secret_name = f'{cluster_name}-monitoring-logins-secret'

    if not secret.secret_exists(secret_name):
        print(f'{secret_name} does not exist, skipping delete')
        return True

    secret.delete_secret(secret_name, perma_delete=True)
    print(f'{secret_name} deleted')


def install_standard_apps(config):
    """
    Called by :func:`k9.cluster_init.create_cluster` after creating the cluster.
    Deploys standard kubernetes apps: EFK, Grafana, Prometheus.
    Also adds dashboards to Kibana and Grafana.

    :param config: config dictionary as read from your cluster-config file
    """

    print("Installing standard apps. If there are any errors, you may retry by running create cluster again.")

    cert_arn = cert.get_certificate(config['baseDomain'])[0]['CertificateArn']
    base_domain = config['baseDomain']
    helm_params = {
        'clusterName': config['clusterName'],
        'baseDomain': base_domain,
        'certArn': cert_arn,
    }

    install_aws_tools(helm_params)
    install_efk(helm_params)
    install_prometheus(helm_params)
    install_grafana(helm_params)

    create_logins_secret(config['clusterName'])


def configure_standard_apps(base_domain, dns_name: str):
    """
    Called as part of install_standard_apps after DNS routing is complete.
    Adds canned dashboards to standard apps.

    :param base_domain: the baseDomain from the cluster-config. Used to create urls.
    :param dns_name: DNS name of the AWS load balancer
    """
    refresh_kubeconfig()
    print('Adding Kibana Dashboards')
    kibana_success = configure_kibana(base_domain, dns_name)

    print('Adding Grafana Dashboards')
    grafana_success = configure_grafana(base_domain, dns_name)

    return kibana_success and grafana_success


def create_access_role(cluster_name: str):
    """
    Finds the EKS access role and configures aws-auth on the kubernetes cluster to allow the role access.
    Creates a ClusterRole and ClusterRoleBinding for the user created in aws-auth.

    :param cluster_name: clusterName creating the role for, used to find the AWS role.

    :return: True on success, False if unable to access ConfigMaps, exception if other failure.
    """
    # match the name format in atomic-cloud cfm template
    role = iam.get_role(f'{cluster_name}-eks-access-role')
    role_arn = role['Arn']

    # add access role to aws_auth configmap
    add_arn_to_aws_auth(role_arn)

    # create ClusterRole and CLusterRoleBinding
    cr_body = util.read_yaml(abs_path('yaml/access-role/access-ClusterRole.yml'))
    try:
        client.RbacAuthorizationV1Api().create_cluster_role(cr_body)
    except client.exceptions.ApiException:
        print('ClusterRole already exists')

    crb_body = util.read_yaml(abs_path('yaml/access-role/access-ClusterRoleBinding.yml'))
    try:
        client.RbacAuthorizationV1Api().create_cluster_role_binding(crb_body)
    except client.exceptions.ApiException:
        print('ClusterRoleBinding already exists')

    print(f'{cluster_name}-eks-access-role created and configured. '
          f'Manually add users to the trust policy to allow them to assume the role.')
    return True


def add_arn_to_aws_auth(role_arn: str):
    """
    Adds the IAM entity arn to the current cluster's aws-auth ConfigMap. The arn is associated to a kubernetes user
    named eks-access-role-user.
    """
    # build addition to aws-auth
    jinja_env = Environment(loader=FileSystemLoader(abs_path('yaml/access-role')), autoescape=True)
    template = jinja_env.get_template('aws-auth-entry.yml')
    template_body = template.render({'roleArn': role_arn})

    # find aws-auth and patch in new entry
    core = client.CoreV1Api()
    try:
        map_list = core.list_namespaced_config_map('kube-system')
    except client.exceptions.ApiException as e:
        if e.reason == 'Forbidden':
            print('The current AWS principle (role/user) does not have access to ConfigMaps')
            print('Cannot configure aws-auth configmap')
            return False
        raise e

    aws_auth = None
    for m in map_list.items:
        if m.metadata.name == 'aws-auth':
            aws_auth = m
            break

    if role_arn not in aws_auth.data['mapRoles']:
        new_body = aws_auth.data['mapRoles'] + '\n' + template_body
        aws_auth.data['mapRoles'] = new_body
        core.patch_namespaced_config_map(name='aws-auth', namespace='kube-system', body=aws_auth)
        print('patched aws-auth')
    else:
        print('aws-auth already patched')


def configure_access_to_cluster(cluster_name: str):
    """
    Adds the current IAM entity to a cluster. Current IAM entity must be able to assume the cluster's eks-access-role.
    See https://k9.docs.simoncomputing.com/eks_access_role.html for information on assuming an access role.

    :param cluster_name: The cluster to configure access to.

    :return: True on success, False otherwise.
    """
    # match the name format in atomic-cloud cfm template
    role = iam.get_role(f'{cluster_name}-eks-access-role')
    role_arn = role['Arn']

    from k9.deploy import get_caller_identity
    my_arn = get_caller_identity()['Arn']

    # assume access role
    try:
        shell(f'aws sts assume-role --role-arn {role_arn} --role-session-name configure-access', silent=True)
    except subprocess.CalledProcessError as e:
        if 'AccessDenied' in str(e.stderr):
            print(f'\nThe current IAM entity does not have permissions to assume {role_arn}. '
                  f'See https://k9.docs.simoncomputing.com/eks_access_role.html for information on assuming a cluster '
                  f'access role.')
        return False
    shell(f'aws eks update-kubeconfig --name {cluster_name}-cluster --role-arn {role_arn}', silent=True)
    kube_config.load_kube_config()
    add_arn_to_aws_auth(my_arn)

    # un-assume access role
    connect_to_cluster(cluster_name)
    return True


def _get_rds_instance_name(cluster_name: str):
    '''
    Helper function to be used by create_cicd() to get rds instance name for cicd
    '''
    databases = rds.list_db_instances(eks_cluster_name=cluster_name)
    rds_instance_name = None
    if len(databases) == 0:
        raise ValueError(f'The cluster with name {cluster_name} does not have any associated RDS instances.')
    elif len(databases) == 1:
        rds_instance_name = databases[0]['DBInstanceIdentifier']
    else:
        for database in databases:
            if util.get_tag_value(database, 'default', 'TagList') == 'True':
                rds_instance_name = database['DBInstanceIdentifier']
                break
        if not rds_instance_name:
            raise ValueError(f'There was no RDS instance that was found with a default tag.')

    return rds_instance_name


def _get_jenkins_password(cluster_name: str):
    '''
    Helper function to be used by create_cicd() to get Jenkins password if defined in secret manager.
    Otherwise, it will random generated and put to a secret manager.

    :param cluster_name
    :return Jenkins password
    '''
    secret_name = cluster_name + '-jenkins-password'
    jenkins_tags = {
        "clusterName": cluster_name,
        "type": 'Jenkins login'
    }
    try:
        if not secret.secret_exists_by_tags(tags=jenkins_tags):
            if not secret.secret_exists(name=secret_name):
                password = util.generate_random_password()
                tags = {
                    'Name': secret_name,
                    'clusterName': cluster_name,
                    'type': 'Jenkins login'
                }
                secret.create_secret(name=secret_name,
                                     description=f"Jenkins web login credentials for the {cluster_name} cluster.",
                                     kvp={'username': 'admin', 'password': password}, tags=tags)
                resulting_secret = secret.get_secret_value(name=secret_name)
                secret.wait_for_secret(name=secret_name, value=resulting_secret)
                return password
            else:
                return secret.get_secret_value(name=secret_name, key='password')
        else:
            return secret.get_secrets_by_tags(tags=jenkins_tags, desired_key='password')[0]
    except Exception as e:
        print(
            f'ERROR: An error occurred while attempting to create/retrieve the Jenkins login secret for the cluster {cluster_name}.')
        print(e)
        raise e


def _get_rds_hostname(rds_instance_name: str, cluster_name: str):
    '''
    Helper function to get rds hostname of the rds instance through secret manager
    '''
    rds_secret_name = rds_instance_name + "-credentials"
    rds_tags = {
        "rdsInstance": rds_instance_name,
        "secretType": "RDS login credentials",
        "clusterName": cluster_name
    }
    if not secret.secret_exists_by_tags(tags=rds_tags):
        if not secret.secret_exists(rds_secret_name):
            raise Exception(f'Password secret for cluster with clusterName {cluster_name} does not exist.')
        return secret.get_secret_value(name=rds_secret_name, key='host')
    else:
        return secret.get_secrets_by_tags(tags=rds_tags, desired_key='host')[0]


def _get_sonar_credential(sonar_db_info: dict, cluster_name: str):
    env = sonar_db_info['deployments'][0]['environments'][0]['env']
    app_name = sonar_db_info['appName']
    database_name = env + "_" + app_name
    master_secret_name = env + "-" + app_name + "-master"
    master_tags = {
        "databaseName": database_name,
        "appName": app_name,
        "secretType": "Application database user credentials",
        "clusterName": cluster_name,
        "userType": "Master",
        "env": env
    }

    if not secret.secret_exists_by_tags(tags=master_tags):
        if not secret.secret_exists(master_secret_name):
            raise Exception(f'Password secret for cluster with clusterName {cluster_name} does not exist.')
        sonar_user = secret.get_secret_value(name=master_secret_name, key='username')
        sonar_password = secret.get_secret_value(name=master_secret_name, key='password')
    else:
        sonar_user = secret.get_secrets_by_tags(tags=master_tags, desired_key='username')[0]
        sonar_password = secret.get_secrets_by_tags(tags=master_tags, desired_key='password')[0]

    sonar_credential = {
        'user': sonar_user,
        'password': sonar_password
    }
    return sonar_credential


def create_cicd(config):
    """
    Called by :func:`k9.cluster_init.create_cluster` if creating a cicd cluster.
    Deploys cicd apps: Jenkins and SonarQube

    """
    cluster_name = config.get('clusterName')
    if not cluster_name:
        print(f'ERROR: The cluster-config.yml does not contain a clusterName.')
        raise ValueError('The cluster-config.yml does not contain a clusterName.')
    
    connect_to_cluster(cluster_name)
    
    base_domain = config.get('baseDomain')
    if not base_domain:
        print(f'ERROR: The cluster-config.yml does not contain a baseDomain.')
        raise ValueError('The cluster-config.yml does not contain a baseDomain.')

    certificate = '*.' + base_domain
    cert_arn = cert.get_cert_arn(domain=certificate)
    if not cert_arn:
        print(f'ERROR: The certificate {certificate} does not exist.')
        raise ValueError(f'The certificate {certificate} does not exist.')

    jenkins_password = _get_jenkins_password(cluster_name)
    jenkins_user = secret.get_secret_value(f'{cluster_name}-jenkins-password', 'username')
    
    if not namespace_exists(namespace='cicd'):
        create_namespace(namespace='cicd')
    
    try:
        run_command('kubectl', 'apply', '-f', abs_path('yaml/jenkins-pvc.yml'), '-n', 'cicd')
    except Exception as e:
        print(f'An error occurred while attempting to create the persistent volume claim for Jenkins.')
        raise e
    
    secret_dict = {
        'jenkins-admin-password': jenkins_password,
        'jenkins-admin-user': jenkins_user,
    }
    if not secret_exists('jenkins', 'cicd'):
        create_secret('jenkins', secret_dict, 'cicd')
    
    jenkins_params = {
        'clusterName': cluster_name,
        'baseDomain': base_domain,
        'certArn': cert_arn
    }

    try:
        print('Installing Jenkins...')
        install_jenkins(jenkins_params, namespace='cicd')
    except Exception as e:
        print('An error occurred while attempting to create Jenkins.')
        print(e)
        raise e
    print('Jenkins has been installed.')

    # SonarQube
    rds_instance_name = _get_rds_instance_name(cluster_name)
    rds_hostname = _get_rds_hostname(rds_instance_name, cluster_name)

    app_database_info = {
        "appName": "sonar",
        "deployments": [{
            "clusterName": cluster_name,
            "environments": [{
                "env": "cicd",
                "rdsInstance": rds_instance_name
            }]
        }]
    }
    total_no_action, total_successful, total_failure = create_app_databases(app_config=app_database_info)
    if len(total_no_action) > 0 or len(total_successful) != 1 or len(total_failure) > 0:
        raise Exception(f'Creation of application database for SonarQube was unsuccessful.')
    env = app_database_info['deployments'][0]['environments'][0]['env']
    app_name = app_database_info['appName']
    database_name = env + "_" + app_name
    sonar_credential = _get_sonar_credential(app_database_info, cluster_name)
    sonar_user = sonar_credential['user']
    sonar_password = sonar_credential['password']

    sonar_params = {
        'clusterName': cluster_name,
        'baseDomain': base_domain,
        'certArn': cert_arn,
        'sonarServerHost': rds_hostname,
        'sonarDb': database_name,
        'sonarUser': sonar_user
    }
    connect_to_cluster(cluster_name)
    if not secret_exists('sonar-password', 'cicd'):
        set_default_namespace('cicd')
        create_secret('sonar-password', {'postgresql-password': sonar_password}, 'cicd')
    try:
        print('Installing SonarQube...')
        install_sonarqube(sonar_params, namespace='cicd')
    except Exception as e:
        print('An error occurred while attempting to create SonarQube.')
        print(e)
        raise e
    print('SonarQube has been installed.')
    run_command('kubectl', 'get', 'ing', '-n', 'cicd')
    print('DNS Routing must be done manually now. Run the "k9 link cicd" command when you can access the hosts printed above.')

    print('cicd deployed')


def configure_sonar_for_linking(config):
    """
    Configures the sonar site to update the default admin's password, to create a Jenkins admin, and to create a user token for the Jenkins user
    Note: this should be run only after the create_cicd function has been run and DNS routing has been completed.

    :param config: The cluster-config of the cluster used for cicd in dict form
    :return: The user token used to link Jenkins and SonarQube
    """
    cluster_name = config.get('clusterName')
    if not cluster_name:
        raise ValueError('ERROR: The cluster-config.yml does not contain a clusterName.')
    
    connect_to_cluster(cluster_name)
    
    base_domain = config.get('baseDomain')
    if not base_domain:
        raise ValueError('ERROR: The cluster-config.yml does not contain a baseDomain.')
    
    if not helm_exists('jenkins', 'cicd') or not helm_exists('sonarqube', 'cicd'):
        raise ValueError('ERROR: Jenkins or SonarQube has not been installed. Please run the k9 create cicd command before running this.')
    
    sonar_url = f"https://sonar.{base_domain}"
    admin_login, admin_password = update_default_sonar_user_password(sonar_url=sonar_url, cluster_name=cluster_name)
    create_jenkins_user_in_sonar(sonar_url=sonar_url, admin_login=admin_login, admin_password=admin_password)
    user_token = create_jenkins_user_token(sonar_url=sonar_url, admin_login=admin_login, admin_password=admin_password)
    return user_token


def update_default_sonar_user_password(sonar_url: str, cluster_name: str):
    """
    Updates the SonarQube default admin's password. Returns an error if sonar site is unreachable.
    Note: this should be run only after the create_cicd function has been run and DNS routing has been completed.

    :param sonar_url: The url of the SonarQube site
    :return: The updated credentials for the default admin
    """
    sonar_default_login = secret.get_secret_value('default-sonarqube-credentials', 'login')
    sonar_default_password = secret.get_secret_value('default-sonarqube-credentials', 'password')
    login_data = {
        'login': sonar_default_login,
        'password': sonar_default_password
    }
    print('Connecting to SonarQube...')
    login_response = requests.post(f'{sonar_url}/api/authentication/login', data = login_data)
    print("Updating SonarQube administrator's password from default...")
    sonar_jenkins_user_tags = {
        'clusterName': cluster_name,
        'secretType': 'Admin user in SonarQube credentials'
    }
    if login_response.status_code == 200:
        jenkins_user_in_sonar_secret = f"{cluster_name}-sonar-web-login-credentials"
        if not secret.secret_exists_by_tags(tags=sonar_jenkins_user_tags):
            password = util.generate_random_password()
            sonar_jenkins_user_tags['Name'] = jenkins_user_in_sonar_secret
            secret.create_secret(name=jenkins_user_in_sonar_secret,
                                    description=f"SonarQube web login credentials for the {cluster_name} cluster.",
                                    kvp={'login': sonar_default_login, 'password': password}, tags=sonar_jenkins_user_tags)
            resulting_secret = secret.get_secret_value(name=jenkins_user_in_sonar_secret)
            secret.wait_for_secret(name=jenkins_user_in_sonar_secret, value=resulting_secret)
            admin_login = secret.get_secret_value(jenkins_user_in_sonar_secret, 'login')
            admin_password = secret.get_secret_value(jenkins_user_in_sonar_secret, 'password')
        else:
            admin_login = secret.get_secrets_by_tags(tags=sonar_jenkins_user_tags, desired_key='login')[0]
            admin_password = secret.get_secrets_by_tags(tags=sonar_jenkins_user_tags, desired_key='password')[0]
        changed_password_data = {
            'login': admin_login,
            'password': admin_password,
            'previousPassword': sonar_default_password,
        }
        change_password_response = requests.post(f'{sonar_url}/api/users/change_password', data = changed_password_data, auth = (sonar_default_login, sonar_default_password))
        if (change_password_response.status_code >= 400):
            print("WARNING: Sonar administrator's password was not successfully updated. This will need to be done manually.")
            admin_login = sonar_default_login
            admin_password = sonar_default_password
        else:
            print("Sonar administrator's password was successfully updated.")
    elif login_response.status_code == 401:
        print("Sonar administrator's password has already been updated.")
        admin_login = secret.get_secrets_by_tags(tags=sonar_jenkins_user_tags, desired_key='login')[0]
        admin_password = secret.get_secrets_by_tags(tags=sonar_jenkins_user_tags, desired_key='password')[0]
    else:
        raise ValueError(f'ERROR: Could not connect to the sonar site at {sonar_url}. Please ensure that you have completed DNS routing and are able to access this site.')
    return admin_login, admin_password


def create_jenkins_user_in_sonar(sonar_url: str, admin_login: str, admin_password: str):
    """
    Creates the Jenkins user and assigns administrator privileges to it.
    Note: this should be run only after the create_cicd function has been run and DNS routing has been completed.

    :param sonar_url: The url of the SonarQube site
    :param admin_login: The login for the default admin user
    :param admin_password: The password for the default admin user
    """
    print('Creating Jenkins user...')
    users_response = requests.get(f'{sonar_url}/api/users/search', params={'ps': 500}, auth = (admin_login, admin_password))
    users: list = users_response.json().get('users')
    jenkins_user = list(filter(lambda usr: usr.get('login') == 'jenkins', users))
    if not jenkins_user:
        jenkins_user_params = {
            'login': 'jenkins',
            'name': 'Jenkins',
            'password': util.generate_random_password()
        }
        create_user_response = requests.post(f'{sonar_url}/api/users/create', data=jenkins_user_params, auth = (admin_login, admin_password))
        if (create_user_response.status_code >= 400):
            raise ValueError("ERROR: Jenkins user in SonarQube was unable to be created.")
        else:
            print('Jenkins user created successfully.')
    else:
        print('Jenkins user already created.')
    print('Adding user as an administrator...')
    group_params = {
        'login': 'jenkins',
        'name': 'sonar-administrators'
    }
    add_user_to_group_response = requests.post(f'{sonar_url}/api/user_groups/add_user', data=group_params, auth = (admin_login, admin_password))
    if (add_user_to_group_response.status_code >= 400):
        raise ValueError("ERROR: Jenkins user was not able to be added as an administrator.")
    else:
        print('Jenkins user was added as an administrator successfully.')


def create_jenkins_user_token(sonar_url: str, admin_login: str, admin_password: str):
    """
    Creates a user token for the Jenkins user.
    Note: this should be run only after the create_cicd function has been run and DNS routing has been completed.

    :param sonar_url: The url of the SonarQube site
    :param admin_login: The login for the default admin user
    :param admin_password: The password for the default admin user
    """
    print('Creating user token...')
    token_exists_response = requests.get(f'{sonar_url}/api/user_tokens/search', params = {'login': 'jenkins'}, auth = (admin_login, admin_password))
    token_exists: list = token_exists_response.json().get('userTokens')
    if token_exists:
        raise ValueError('ERROR: The Jenkins user already has a user token. Please manually delete all tokens before continuing.')
    token_params = {
        'login': 'jenkins',
        'name': 'sonar-jenkins-user-token'
    }
    add_token_response = requests.post(f'{sonar_url}/api/user_tokens/generate', data=token_params, auth = (admin_login, admin_password))
    if (add_token_response.status_code >= 400):
        raise ValueError("ERROR: Jenkins user token was not able to be created.")
    return add_token_response.json().get('token')


def delete_cicd(config: dict):
    """
    Deletes resources created by create_cicd and removes Jenkins and Sonar deployments.

    :param config: cluster-config.yml
    """
    cluster_name = config['clusterName']

    connect_to_cluster(cluster_name)

    # delete AWS secrets
    jenkins_secret = cluster_name + '-jenkins-password'
    secret.delete_secret(jenkins_secret, perma_delete=True)

    sonar_secret = cluster_name + '-cluster-sonar-password'
    secret.delete_secret(sonar_secret, perma_delete=True)

    jenkins_user_in_sonar_secret = f"{cluster_name}-sonar-web-login-credentials"
    secret.delete_secret(jenkins_user_in_sonar_secret, perma_delete=True)

    if helm_exists('jenkins', 'cicd'):
        helm_uninstall('jenkins', 'cicd')
    if helm_exists('sonarqube', 'cicd'):
        helm_uninstall('sonarqube', 'cicd')

    # delete sonar db
    rds_instance_name = _get_rds_instance_name(cluster_name)
    delete_app_database(cluster_name, 'sonar', 'cicd', rds_instance_name)
    print('Jenkins and Sonar uninstalled.')


def create_cluster(config, cwd: str):
    """
    Called by create cluster cli. Does all cluster setup including CloudFormation stacks, installing standard apps,
    configuring standard apps, and create an access role for the cluster.

    :param config: config dictionary as read from your cluster-config file
    :param cwd: the current working directory that contains all the cfm template files
    """
    cfm.set_template_path(cwd)
    cluster.create_cluster(config)
    print('Cluster created.')

    # configure kubectl
    cluster_name = config['clusterName']
    connect_to_cluster(cluster_name)

    print('Creating EKS access role...')
    create_access_role(cluster_name)
    print('\nEKS access role created.\n')

    print('Installing standard apps...')
    install_standard_apps(config)
    print('\nAll standard apps deployed successfully.\n')

    print('Configuring standard apps...')
    lb = get_cluster_load_balancer(cluster_name)
    if lb is None:
        print('Cluster load balancer not found. Cannot configure standard apps.')
        return
    configure_standard_apps(base_domain=config['baseDomain'], dns_name=lb['DNSName'])
    print('\nStandard apps configured.\n')
    print(f'Route *.{config["baseDomain"]} to {lb["DNSName"]}\n')


def delete_volumes(cluster_name: str):
    """
    Deletes all ELB volumes created as part of the Kubernetes cluster.

    :param cluster_name: The name of the cluster to delete all volumes within.
        (appends '-cluster' to find the ControlPlane)
    """
    refresh_kubeconfig()
    client = ec2.get_ec2()

    # find volumes with the tag identifying them as part of this cluster
    response = client.describe_volumes(
        Filters=[
            {
                'Name': f'tag:kubernetes.io/cluster/{cluster_name}-cluster',
                'Values': ['owned',]
            }
        ]
    )

    for v in response['Volumes']:
        volume_id = v['VolumeId']
        print(f'Deleting volume: {volume_id}')
        # detach and then delete
        try:
            ec2.get_ec2().detach_volume(VolumeId=volume_id, Force=True)
        except Exception as e:
            # if volume already detached, continue to delete
            if 'IncorrectState' in str(e) or 'InvalidAttachment.NotFound' in str(e):
                print('Volume already detached')
            else:
                raise e
        try:
            response = ec2.get_ec2().delete_volume(VolumeId=volume_id)
            print(response)
        except Exception as e:
            # root volumes are removed with eks worker nodes
            if 'root' in str(e):
                print('Not deleting root volume, that will be cleaned later')
            elif 'currently attached' in str(e):
                print(str(e))
                print(f'{volume_id} may be left behind after delete cluster finishes. Check manually in AWS console.')
            else:
                raise e


def get_cluster_load_balancer(cluster_name: str):
    """
    Gets the load balancer for a vpc name clusterName-01-vpc.

    :param cluster_name: The cluster to find the load balancer for.

    :returns: Load balancer object if found. None otherwise.
    """
    try:
        vpc_id = cfm.get_output(cluster_name + '-01-vpc', 'VPC')
    except TypeError:
        return None

    load_balancers = region.get_elbv2().describe_load_balancers()
    for lb in load_balancers['LoadBalancers']:
        if lb['VpcId'] == vpc_id:
            return lb


