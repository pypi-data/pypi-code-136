import os.path
import json
import pathlib
import time
from dataclasses import dataclass

import botocore.errorfactory

from k9.core import create_secret, delete_app_database, delete_secret, run_command, refresh_kubeconfig, \
    connect_to_cluster, render_template, abs_path, shell
from k9.helm import helm_repo_add, helm_repo_update, helm_exists, namespace_exists, create_namespace, helm_uninstall
from k9.jcasc import create_google_chat_credential
from aws import util, cert, cluster, secret as aws_secret, cfm, rds, region
import boto3


@dataclass
class _SecretTypes:
    app = 'Application secret'


SECRET_TYPES = _SecretTypes()
CFM_DIR = 'yaml/cfm'
VERSION_TEMPLATE = '{{Version}}'


def read_yaml(file_path: str):
    """
    Reads a yml file into a dict. Prints a nice error message and stop execution if file is not found.

    :param file_path: path to the yml file to open

    :return: dict representation of the yml
    """
    try:
        output = util.read_yaml(file_path)
    except FileNotFoundError as e:
        file = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        print(f'Error: {file} not found in {dir_name}')
        raise e
    return output


def read_app_config(app_dir: str, deleting: bool = False):
    """
    Read app-config.yml and return the contents.
    :param app_dir: the file path to the directory containing app-config.yml
    :param deleting: whether the deployment instance is being deleted

    :return: dict of the contents of app-config.yml
    """

    return _process_app_config(app_dir, False, deleting)


def read_prd_app_config(app_dir: str, deleting: bool = False):
    """
    Read app-config.yml and return the contents.
    :param app_dir: the file path to the directory containing app-config.yml
    :param deleting: whether the deployment instance is being deleted

    :return: dict of the contents of app-config.yml
    """

    return _process_app_config(app_dir, True, deleting)


def _process_app_config(app_dir: str, is_prd: bool, deleting: bool = False):
    """
        Helper method to read  and return the contents.
        :param app_dir: the file path to the directory containing app-config.yml or prd-app-config.yml
        :param deleting: whether the deployment instance is being deleted

        :return: dict of the contents of app-config.yml or prd-app-config.yml
        """
    config_path = os.path.join(app_dir, 'prd-app-config.yml') if is_prd else os.path.join(app_dir, 'app-config.yml')
    config = read_yaml(config_path)

    instances = []

    deployments = config['deployments']
    for cluster_dict in deployments:
        cluster_name = cluster_dict['clusterName']
        # each env might have multiple customers
        for env in cluster_dict['environments']:
            customers = env.get('customers', [])
            if len(customers) > 0:
                # create an instance object for each customer in the env
                for cust in customers:
                    inst = create_deployment_instance(config, cluster_name, env, cust, deleting)
                    instances.append(inst)
            else:
                inst = create_deployment_instance(app_config=config, cluster_name=cluster_name, env_dict=env,
                                                  deleting=deleting)
                instances.append(inst)

    config['appInstances'] = instances

    return config


def get_cert_urls(app_config: dict, include_ui: bool = True, include_service: bool = True):
    """
    Get unique certificate urls and alternate certificate urls for each deployment instance.
    Includes UI and Service urls unless told not to.
    If multiple deployment instances have the same urls, they will only be included once.

    :param app_config: The dictionary version of app-config.yml. Contains all environments to deploy to.
    :param include_ui: Whether to return urls for UI instances.
    :param include_service: Whether to return urls for service instances.

    :return: List of tuples. (cert_url, alt_cert_url)
    """
    cert_urls = []

    for instance in app_config['appInstances']:
        if include_ui:
            ui = (instance['uiCertUrl'], instance['altUiCertUrl'])
            if ui not in cert_urls:
                cert_urls.append(ui)
        if include_service:
            service = (instance['serviceCertUrl'], instance['altServiceCertUrl'])
            if service not in cert_urls:
                cert_urls.append(service)

    return cert_urls


def create_app_certs(app_config: dict, include_ui: bool = True, include_service: bool = True):
    """
    Creates certs for all deployments in an app-config.

    :param app_config: The dictionary version of app-config.yml. Contains all environments to deploy to.
    :param include_ui: Whether to create certs for UI instances.
    :param include_service: Whether to create certs for service instances.
    """

    urls = get_cert_urls(app_config, include_ui, include_service)
    request_urls = []
    alt_request_urls = []
    # find urls without certs
    for url_pair in urls:
        exists = cert.get_cert_arn(url_pair[0])
        if not exists:
            request_urls.append(url_pair[0])
            alt_request_urls.append(url_pair[1])

    if len(request_urls) == 0:
        print('All certificates exist already')
        return

    print('Going to request certs for', request_urls)
    client = cert.get_acm()

    # get the validation domain to send cert approval emails to.
    validation_domain = app_config['rootDomain']

    print(f'validation domain: {validation_domain}')
    option = input('Input "quit" to stop before requesting.\n'
                   'Input "skip" to skip making requests.\n'
                   'Input anything else to continue and request certificates with the above validation domain:\n')
    if option == 'quit':
        exit()
    if option == 'skip':
        return

    tags = {
        'appName': app_config['appName'],
        'createdWith': 'k9 cli'
    }
    aws_tags = [{'Key': k, 'Value': tags[k]} for k in tags]

    for i in range(len(request_urls)):
        url = request_urls[i]
        alt_url = alt_request_urls[i]
        response = client.request_certificate(DomainName=url, ValidationMethod='EMAIL', IdempotencyToken='k9',
                                              DomainValidationOptions=[
                                                  {'DomainName': url, 'ValidationDomain': validation_domain}, ],
                                              SubjectAlternativeNames=[alt_url],
                                              Tags=aws_tags)
        print(response)
        print(f'requested certificate for {url}')


def delete_app_certs(app_dir: str, delete_ui: bool = True, delete_service: bool = True, is_prd: bool = False):
    """
    Deletes certs created for an app.

    :param app_dir: the file path to the directory containing app-config.yml
    :param delete_ui: Whether to delete certs for UI instances.
    :param delete_service: Whether to delete certs for service instances.
    :param is_prd: Whether the application is strictly for the production environment

    """
    app_config = read_prd_app_config(app_dir) if is_prd else read_app_config(app_dir)
    urls = get_cert_urls(app_config, include_ui=delete_ui, include_service=delete_service)

    for url in urls:
        cert.delete_cert(url[0])
        print(f'Deleted certificate: {url[0]}')


def get_caller_identity():
    """
    Calls sts get-caller-identity api

    :returns: Dict containing UserId, Account, and Arn.
    """
    sts_client = boto3.client('sts')
    return sts_client.get_caller_identity()


def create_ecr(app_name: str):
    """
    Creates an ECR for the given app name. Returns the url for the ECR.

    :param app_name: The name of the app to create the ECR for.

    :return: ECR URL
    """
    cluster.create_ecr(app_name)

    account_id = region.get_account_id()
    reg = region.get_default_region()
    url = f'{account_id}dkr.ecr.{reg}.amazonaws.com/{app_name}'
    print(f'ECR repo url: {url}')
    return url


def delete_ecr(app_name: str):
    """
    Empties an ECR of all images then deletes the stack

    :param app_name: The name of the app to create the ECR for.
    """
    ecr_name = app_name.lower()
    client = boto3.client('ecr')

    repos = client.describe_repositories()['repositories']

    registry_id = None
    for repo in repos:
        if repo['repositoryName'] == ecr_name:
            registry_id = repo['registryId']
            print(f'Found registry id: {registry_id}')
            break

    if registry_id is not None:
        # delete ecr with force=True to delete if images are still in it
        client.delete_repository(
            registryId=registry_id,
            repositoryName=ecr_name,
            force=True
        )
        print('Force deleted ECR')

    # delete stack now that ECR has no images in it
    cluster.delete_ecr(app_name)


def deploy_service(app_config: dict, app_dir: str):
    """
    Deploys the app to all environments given in app_config. Looks in the 'values' directory for values.yml files for
    each deployment. Each env deployment looks at the file name <env>-values.yml. ex: dvl-values.yml, prd-values.yml.
    Each values.yml file must have [chartName, namespace, releaseName, repoName, repoUrl] defined. <env>-values.yml
    files generated by k9 will have these filled in.

    :param app_config: The dictionary version of app-config.yml. Contains all environments to deploy to.
    :param app_dir: the file path to the directory containing app-config.yml
    """
    values_dir = os.path.join(app_dir, 'values')

    instances = app_config['appInstances']
    for instance in instances:
        instance_name = instance['appInstanceName']
        print(f'Deploying app instance: {instance_name}')
        cluster_name = instance['clusterName']
        connect_to_cluster(cluster_name)

        # get values.yml file name
        file_name = f'{instance_name}-values.yml'
        values_path = os.path.join(values_dir, file_name)
        if not os.path.exists(values_path):
            print(f'{values_path} not found. skipping {file_name} deployment.')
            continue

        values = read_yaml(values_path)

        k9_values = values['k9']

        repo_name = k9_values['repoName']
        chart_name = k9_values['chartName']
        namespace = k9_values['namespace']
        release_name = k9_values['releaseName']

        if not namespace_exists(namespace):
            create_namespace(namespace)

        if helm_exists(release_name, namespace):
            print(f'Release: {release_name} found in namespace: {namespace}. skipping {release_name} deployment.')
            continue

        helm_repo_add(repo_name, k9_values['repoUrl'])
        helm_repo_update()

        run_command('helm', 'install', '-n', namespace, '-f', values_path, release_name, f'{repo_name}/{chart_name}')

    print(f'\nAll {app_config["appName"]} deployments successful. You must manually configure DNS to point to the '
          f'AWS load balancers.')


def delete_all_service_deployments(app_dir: str, is_prd: bool = False):
    """
    Uninstalls all service deployments found in app-config.yml or prd-app-config.yml, dependent on if is_prd is set to True.
    Uses app-config.yml/prd-app-config.yml to find values.yml files to then run helm uninstall on the correct release
    in the correct namespace.
    """
    refresh_kubeconfig()
    app_config = read_prd_app_config(app_dir) if is_prd else read_app_config(app_dir)
    values_dir = os.path.join(app_dir, 'values')

    instances = app_config['appInstances']
    for instance in instances:
        instance_name = instance['appInstanceName']
        print(f'Deleting app instance: {instance_name}')
        cluster_name = instance['clusterName']
        connect_to_cluster(cluster_name)

        # get values.yml file name
        file_name = f'{instance_name}-values.yml'
        values_path = os.path.join(values_dir, file_name)
        if not os.path.exists(values_path):
            print(f'{values_path} not found. Skipping {instance_name} delete.')
            continue

        values = read_yaml(values_path)

        k9_values = values['k9']
        namespace = k9_values['namespace']
        release_name = k9_values['releaseName']

        if helm_exists(release_name, namespace):
            print(f'Release: {release_name} found in namespace: {namespace}. Deleting.')
            helm_uninstall(release_name, namespace)
        else:
            print(f'Release {release_name} not found.')


def deploy_ui(app_config: dict, app_dir: str = None):
    """
        Create s3 hosting for UI app for all environments given in app_config.
        For each env deployment, certificate for UI will be requested. Upon approval, an S3 bucket and CloudFront
        will be created.

        :param app_config: The dictionary version of app-config.yml. Contains all environments to deploy to.
        :param app_dir: Directory containing app-config.yml and values directory, only used for govcloud deployments.
    """

    if 'gov' in region.get_default_region():
        return deploy_gov_ui(app_config, app_dir)

    validation_domain = app_config['rootDomain']
    instances = app_config['appInstances']
    app_name = app_config['appName'].lower()

    # for ui, create s3_hosting per environment, not per customer
    hosted_envs = []
    for instance in instances:
        env = instance['env']
        if env in hosted_envs:
            continue

        cluster_name = instance['clusterName']
        ui_cert_url = instance['uiCertUrl'].lower()
        print(f'Creating S3 hosting for cluster: {cluster_name}, appName: {app_name}, environment: {env}, '
              f'uiCert: {ui_cert_url}')
        cfm.set_template_path(cfm.TEMPLATE_DIR)
        s3_hosting = cluster.create_s3_hosting(cluster_name, app_name, ui_cert_url, env, validation_domain)
        print(f'Environment: {env}, '
              f'Distribution: {cluster._get_output(s3_hosting, "Distribution")}, '
              f'CloudfrontUrl: {cluster._get_output(s3_hosting, "CloudfrontUrl")}, '
              f'Bucket: {cluster._get_output(s3_hosting, "Bucket")}')
        hosted_envs.append(env)

    # create S3 bucket for builds process
    # use www instead of appName if webSite is True
    web_site = app_config.get('webSite', False)
    build_bucket_name = get_build_bucket_name(web_site, app_name, validation_domain)
    create_s3_if_not_exist(build_bucket_name)


def get_build_bucket_name(web_site: bool, app_name: str, validation_domain: str):
    corrected_app_name = 'www' if web_site else app_name
    return f'{corrected_app_name}.{validation_domain}-builds'


def deploy_gov_ui(app_config: dict, app_dir: str):
    """
    Create s3 hosting for UI app for all environments given in app_config.
    For each env deployment, certificate for UI will be requested.
    An S3 bucket will be created for each environment.
    A kubernetes deployment will be installed so that traffic can be routed from a load balancer to the S3 buckets.

    :param app_config: The dictionary version of app-config.yml. Contains all environments to deploy to.
    :param app_dir: Directory containing app-config.yml and values directory. Used to find the 'values' directory.
    """

    validation_domain = app_config['rootDomain']
    instances = app_config['appInstances']
    app_name = app_config['appName'].lower()

    helm_repo_add('simoncomputing', 'https://charts.simoncomputing.com/')
    helm_repo_update()

    # for ui, create s3_gov_hosting per environment, not per customer
    hosted_envs = []
    for instance in instances:
        env = instance['env']
        if env in hosted_envs:
            continue
        hosted_envs.append(env)

        cluster_name = instance['clusterName']
        connect_to_cluster(cluster_name)
        ui_cert_url = instance['uiCertUrl'].lower()

        # get list of hostnames
        host_names = get_instance_host_names(instance)

        # create bucket and certificate
        cfm.set_template_path(cfm.TEMPLATE_DIR)
        hosting = cluster.create_s3_gov_hosting(cluster_name, app_name, ui_cert_url, env)
        bucket_name = cfm.get_output(hosting, 'Bucket')

        ui_cert_url = ui_cert_url.replace('*.', '')
        safe_app_name = app_name.replace('.', '-')
        cert_stack = cluster.create_certificate(instance['clusterName'], ui_cert_url,
                                                validation_domain, f'{safe_app_name}-{env}')

        # create values.yml files
        cert_arn = cfm.get_output(cert_stack, 'OutputCertificate')
        deployment_name = f'{instance["env"]}-{app_name}-ui'
        namespace = deployment_name
        params = {
            'certArn': cert_arn,
            'instance': instance,
            'deploymentName': deployment_name,
            'bucketUrl': get_static_site_url(bucket_name),
            'hostNames': host_names,
        }
        from k9.templates import create_gov_ui_values
        values_file_path = create_gov_ui_values(params, app_dir)
        print(values_file_path, namespace)

        # deploy if needed
        refresh_kubeconfig()
        if not namespace_exists(namespace):
            create_namespace(namespace)

        if helm_exists(deployment_name, namespace):
            print(f'Release: {deployment_name} found in namespace: {namespace}. running helm upgrade.')
            run_command('helm', 'upgrade', deployment_name, 'simoncomputing/nginx-s3',
                        '-n', namespace, '-f', values_file_path)
        else:
            print(f'Deploying {deployment_name}..')
            run_command('helm', 'install', '-n', namespace, '-f', values_file_path,
                        deployment_name, 'simoncomputing/nginx-s3')

    # create S3 bucket for builds process
    # use www instead of appName if webSite is True
    web_site = app_config.get('webSite', False)
    build_bucket_name = get_build_bucket_name(web_site, app_name, validation_domain)
    create_s3_if_not_exist(build_bucket_name)


def get_instance_host_names(instance: dict):
    """
    Helper function for deploy_gov_ui to get the list of hostnames for a nginx deployment.

    :param instance: The instance to get hostNames for.

    :returns: an array of urls
    """
    host_names = []
    if instance['envCustomers'] is None:
        host_names.append(instance['altUiCertUrl'])
    else:
        env = instance['env']
        app_name = instance['appName']
        root_domain = instance['rootDomain']
        for cust in instance['envCustomers']:
            # prd urls don't include env in url
            if env == 'prd':
                host_names.append(f'{cust}.{app_name}.{root_domain}')
            else:
                host_names.append(f'{cust}.{app_name}.{env}.{root_domain}')
    return host_names


def get_static_site_url(bucket_name: str):
    """
    Creates the static site url given a bucket name and the current region.
    https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints
    Some regions use s3-website.<region> and some use s3-website-<region>.

    :param bucket_name: The bucket to find the url for.

    :returns: The static site url.
    """
    region_name = region.get_default_region()

    dash_regions = ['us-east-1', 'us-west-1', 'us-west-2', 'ap-southeast-1', 'ap-southeast-2',
                    'ap-northeast-1', 'eu-west-1', 'sa-east-1', 'us-gov-west-1']

    use_dash = region_name in dash_regions
    connector = '-' if use_dash else '.'

    return f'{bucket_name}.s3-website{connector}{region_name}.amazonaws.com'


def create_s3_if_not_exist(bucket_name: str):
    s3_client = boto3.client('s3')
    if s3_exists(bucket_name):
        print(f'{bucket_name} already existed')
        return

    region_name = region.get_default_region()
    # region is required in non us-east-1 region, but throws an error if included in us-east-1 region
    if region_name != 'us-east-1':
        s3_client.create_bucket(
            Bucket=bucket_name,
            ACL='private',
            CreateBucketConfiguration={'LocationConstraint': region.get_default_region()}
        )
    else:
        s3_client.create_bucket(
            Bucket=bucket_name,
            ACL='private',
        )
    # This will set the public block settings
    s3_client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    print(f'bucket {bucket_name} created')

    # wait for client to return it exists consistently
    waiter = s3_client.get_waiter('bucket_exists')
    count = 0
    while count < 5:
        try:
            waiter.wait(Bucket=bucket_name)
            count += 1
        except botocore.errorfactory.ClientError:
            count = 0


def s3_exists(bucket_name: str):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except s3_client.exceptions.ClientError:
        return False


def empty_and_delete_bucket(bucket_name: str):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).objects.all().delete()
        boto3.client('s3').delete_bucket(
            Bucket=bucket_name
        )
        # wait for client to return it doesn't exist consistently
        success = 0
        while success < 5:
            time.sleep(2)
            if s3_exists(bucket_name):
                success = 0
            else:
                success += 1
    except Exception as e:
        print(f'Cannot delete {bucket_name}: {e}')


def create_deployment_instance(app_config: dict, cluster_name: str, env_dict: dict, customer: str = None,
                               deleting: bool = None):
    """
    Creates a deployment instance object that contains all information needed for that instance of a deployment.
    Names are formatted to a standard naming convention.

    :param app_config: app_config.yml dict. Used to get appName and rootDomain.
    :param cluster_name: the cluster this deployment instance will be in
    :param env_dict: The env object for this instance.
    :param customer: optional. The single customer for this instance.

    :return: a dictionary object with all the key value pairs needed to deploy an instance.
    keys: ['appName', 'clusterName', 'env', 'customer', 'appInstanceName', 'appSecret', 'springActiveProfile',
    'updateTag', 'useBlueGreen', 'rdsInstance', 'dbName', 'dbSchema','namespace',
    'uiUrl', 'uiCertUrl', 'altUiCertUrl', 'serviceUrl', 'serviceCertUrl', 'altServiceCertUrl']

    ::

        The actual URL the UI or service will use. Prepends customer if present.
        uiUrl: cust.appName.env.root_domain or appName.env.root_domain
        serviceUrl: cust.appName-service.env.root_domain or appName-service.env.root_domain

        These do not change if customer is present
        uiCertUrl: *.appName.env.root_domain
        altUiCertUrl: appName.env.root_domain
        serviceCertUrl: *.appName-service.env.root_domain
        altServiceCertUrl: appName-service.env.root_domain

    """
    env = env_dict['env']
    specified_rds_instance = env_dict.get('rdsInstance', None)
    app_name = app_config['appName'].lower()
    web_site = app_config.get('webSite', False)
    root_domain = app_config['rootDomain']

    app_instance_name = f'{env}-{app_name}'
    if customer:
        app_instance_name += f'-{customer}'

    # get secret name if listed, otherwise generate it
    app_secret = env_dict.get('appSecret', None)
    if app_secret is None:
        app_secret = f'{app_instance_name}-secret'
    generated_app_secret = f'{app_instance_name}-secret'

    active_profile = env_dict.get('springActiveProfile', None)
    if active_profile is None:
        raise KeyError(f'Environment {env} is missing the springActiveProfile key in app-config.yml')

    update_tag = env_dict.get('updateTag', env)
    use_blue_green = env_dict.get('useBlueGreen', None)

    rds_instance = f'{cluster_name}-{env}'
    if specified_rds_instance and ensure_specified_rds_instance_exists(cluster_name, specified_rds_instance):
        rds_instance_name = specified_rds_instance
    elif deleting:
        rds_instance_name = None
    else:
        try:
            rds_instance_dict = rds.find_default_rds_instance(cluster_name)
            rds_instance_name = rds_instance_dict.get('DBInstanceIdentifier')
        except ValueError:
            # no rds instance found, leave empty
            rds_instance_name = ''
    database_name = f'{env}_{app_name}'
    db_schema_name = f'{env}_{app_name}_{customer}' if customer else f'{env}_{app_name}'
    namespace = app_instance_name

    # don't include prd in url
    # base url to derive all other urls from
    # if webSite was set to true, use www instead of the appName
    url = f'www.{env}.{root_domain}' if web_site else f'{app_name}.{env}.{root_domain}'
    if env == 'prd':
        url = f'www.{root_domain}' if web_site else f'{app_name}.{root_domain}'

    ui_cert_url = f'*.{url}'
    alt_ui_cert_url = url
    ui_url = url
    if customer:
        ui_url = f'{customer}.' + ui_url

    # service urls are all the same as ui except appName should be appName-service
    service_cert_url = ui_cert_url.replace(app_name, f'{app_name}-service')
    alt_service_url = alt_ui_cert_url.replace(app_name, f'{app_name}-service')
    service_url = ui_url.replace(app_name, f'{app_name}-service')

    # list of all customers in this env
    env_customers = env_dict.get('customers', None)

    instance = {
        'appName': app_name,
        'rootDomain': root_domain,
        'clusterName': cluster_name,
        'env': env,
        'customer': customer,
        'envCustomers': env_customers,
        'appInstanceName': app_instance_name,
        'appSecret': app_secret,
        'generatedAppSecret': generated_app_secret,
        'springActiveProfile': active_profile,
        'updateTag': update_tag,
        'useBlueGreen': use_blue_green,
        'rdsInstance': rds_instance,
        'rdsInstanceName': rds_instance_name,
        'dbName': database_name,
        'dbSchema': db_schema_name,
        'namespace': namespace,
        'uiUrl': ui_url,
        'uiCertUrl': ui_cert_url,
        'altUiCertUrl': alt_ui_cert_url,
        'serviceUrl': service_url,
        'serviceCertUrl': service_cert_url,
        'altServiceCertUrl': alt_service_url
    }

    return instance


def ensure_specified_rds_instance_exists(cluster_name: str, specified_rds_instance: str):
    db_instances: list = rds.list_db_instances(eks_cluster_name=cluster_name)
    rds_instance_exists = specified_rds_instance in list(
        map(lambda inst: inst.get('DBInstanceIdentifier'), db_instances))
    if not rds_instance_exists:
        raise KeyError(
            f'An RDS instance with name {specified_rds_instance} is not associated with cluster with name {cluster_name}.')
    return True


def prepare_kubernetes_resources(app_config: dict):
    """
    Creates kubernetes namespaces and turns AWS secrets into kubernetes secrets. If an AWS secret does not exist before
    calling, an empty one is created. Also adds standard information to each deployment's secret.

    :param app_config: app_config.yml dict.
    """

    # create empty AWS secrets if needed
    create_app_aws_secrets(app_config)

    # add information to each secret
    add_standard_info_to_aws_secrets(app_config)

    app_name = app_config['appName']
    app_instances = app_config["appInstances"]
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        customer = app_instance['customer']
        namespace = app_instance['namespace']
        app_secret = app_instance['appSecret'] if customer is None else app_instance['generatedAppSecret']

        connect_to_cluster(cluster_name)

        # create k8s namespace if not exist
        create_kubernetes_namespace(cluster_name, namespace)

        # create k8s secret or update
        try:
            delete_secret(name=app_secret, namespace=namespace)
            secret = get_app_secret_values(cluster_name, app_name, env, customer, app_secret)
            secret_json = json.loads(secret)
            create_secret(name=app_secret, secrets=secret_json, namespace=namespace)
        except Exception as e:
            print(
                f'ERROR: An error was encountered while attempting to create a kubernetes secret with name {app_secret}'
                f' in the namespace with name {namespace} for the cluster with name {cluster_name}.')
            print(e)
            raise e


def create_kubernetes_namespace(cluster_name: str, namespace: str):
    connect_to_cluster(cluster_name)

    try:
        if not namespace_exists(namespace=namespace):
            create_namespace(namespace=namespace)
        else:
            print(f'Namespace {namespace} already exists. Skipping.')
    except Exception as e:
        print(
            f'ERROR: An error was encountered while attempting to create a namespace with name {namespace} '
            f'in the cluster with name {cluster_name}')
        print(e)
        raise e


def get_app_secret_values(cluster_name: str, app_name: str, env: str, customer: str, app_secret_name: str):
    """
    Get secret values for the application to be defined in kubernetes secret.

    :param cluster_name
    :param app_name
    :param env
    :param customer
    :param app_secret_name

    :return secret key-value pairs

    """
    tags = {
        "clusterName": cluster_name,
        "appName": app_name,
        "env": env,
        "secretType": SECRET_TYPES.app
    }
    if customer and customer != "None":
        tags["customer"] = customer

    if aws_secret.secret_exists_by_tags(tags=tags) != True:
        print(
            f'Primary search for the application secret for the application in cluster {cluster_name} with app name '
            f'{app_name}, env {env}, and customer {customer} failed. Attempting secondary search.')

        if not aws_secret.secret_exists(name=app_secret_name):
            raise ValueError(
                f'The application secret for application in cluster {cluster_name} with app name {app_name}, env {env}, '
                f'and for customer {customer} was not found.')
        print('Secondary search successfully retrieved application secret.')
        return aws_secret.get_secret_value(name=app_secret_name)
    else:
        return aws_secret.get_secrets_by_tags(tags=tags)[0]


def delete_ui_by_env(app_config: dict, app_instance: dict, keep_certs: bool = False):
    """
    Delete S3 hosting for the application on a specified environment.

    :param app_config
    :param app_instance
    :param keep_certs

    """
    if 'gov' in region.get_default_region():
        return delete_gov_ui_by_env(app_config, app_instance, keep_certs)

    cluster_name = app_instance['clusterName']
    app_name = app_config['appName'].lower()
    env = app_instance['env']
    cert_url = app_instance['uiCertUrl']
    print(f'Deleting UI for application {app_name} on environment {env}')

    # empty bucket before deleting
    hosting = cfm.find_stack(StackType=cluster.STACK_TYPES.s3_hosting, clusterName=cluster_name, appName=app_name,
                             envName=env)
    if hosting:
        # empty bucket before deleting
        bucket = cfm.get_output(hosting, 'Bucket')
        s3 = boto3.resource('s3')
        s3.Bucket(bucket).objects.all().delete()

    cluster.delete_s3_hosting(cluster_name, app_name, env)
    delete_ui_cert(app_name, env, cert_url, keep_certs)


def delete_gov_ui_by_env(app_config: dict, app_instance: dict, keep_certs: bool = False):
    cluster_name = app_instance['clusterName']
    app_name = app_config['appName'].lower()
    env = app_instance['env']
    cert_url = app_instance['uiCertUrl']
    print(f'Deleting UI for application {app_name} on environment {env}')

    # empty bucket before deleting
    hosting = cfm.find_stack(StackType=cluster.STACK_TYPES.s3_gov_hosting, clusterName=cluster_name, appName=app_name,
                             envName=env)
    if hosting:
        # empty bucket before deleting
        bucket = cfm.get_output(hosting, 'Bucket')
        s3 = boto3.resource('s3')
        s3.Bucket(bucket).objects.all().delete()

    cluster.delete_s3_gov_hosting(cluster_name, app_name, env)
    deployment_name = f'{app_instance["env"]}-{app_name}-ui'
    connect_to_cluster(cluster_name)
    if helm_exists(deployment_name, deployment_name):
        helm_uninstall(deployment_name, deployment_name)
    delete_ui_cert(app_name, env, cert_url, keep_certs)


def delete_ui_cert(app_name: str, env: str, cert_url: str, keep_certs: bool = False):
    """
    Delete the certificate used for the S3 hosting.
    If the cloudFormation stack appName-env-00-cert exists, delete the stack.
    If not, delete cert by domain.

    :param app_name
    :param env
    :param cert_url
    :param keep_certs
    """
    if keep_certs:
        return

    stack_name = f'{app_name}-{env}-00-cert'
    if cfm.get_stack(stack_name) is not None:
        cfm.delete_stack(stack_name)
    else:
        cert.delete_cert(cert_url.lower())


def delete_all_ui_hosting(app_config: dict, keep_certs: bool = False):
    """
    Delete S3 hosting for the application on all environments

    :param app_config
    :param keep_certs

    """
    instances = app_config['appInstances']

    # for ui, create s3_hosting per environment, not per customer
    hosted_envs = []
    for instance in instances:
        env = instance['env']
        if env in hosted_envs:
            continue

        delete_ui_by_env(app_config, instance, keep_certs)
        hosted_envs.append(env)

    # delete builds s3 bucket
    app_name = app_config['appName'].lower()
    root_domain = app_config['rootDomain']
    web_site = app_config.get('webSite', False)
    build_bucket_name = get_build_bucket_name(web_site, app_name, root_domain)
    empty_and_delete_bucket(build_bucket_name)


def delete_ui(app_config: dict, env_name: str = None, keep_certs: bool = False):
    """
    Delete UI hosting with either all environments or by specified environment.
    Cert will not be deleted if keep_certs is specified

    :param app_config
    :param env_name
    :param keep_certs

    """
    if env_name is None:
        delete_all_ui_hosting(app_config, keep_certs)
    else:
        # find app_instance that match the specified env
        instances = app_config['appInstances']
        app_instance = None
        for instance in instances:
            if instance['env'] == env_name:
                app_instance = instance
                break

        if app_instance is None:
            print(f'Cannot find configuration for environment {env_name} in appConfig')
        else:
            delete_ui_by_env(app_config, app_instance, keep_certs)


def create_app_aws_secrets(app_config: dict, values: dict = None):
    """
    Useful for creating all AWS secrets that deploy service expects to find. Creates a secret for each deployment
    unless one already exists.

    :param app_config: app_config.yml dict.
    :param values: (Optional) Values to place into each secret.
    """
    if values is None:
        values = {}

    description = 'Application secret created by k9. Values here will be used to create a secret in kubernetes ' \
                  'by the deploy service command.'

    app_name = app_config['appName']
    deployments = app_config['appInstances']
    for app_instance in deployments:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        secret_name = app_instance['appSecret']
        customer = app_instance['customer']
        if customer:
            generated_secret_name = app_instance['generatedAppSecret']
            if not aws_secret.secret_exists(generated_secret_name):
                generated_tags = {
                    "clusterName": cluster_name,
                    "appName": app_name,
                    "env": env,
                    "customer": customer,
                    "secretType": SECRET_TYPES.app
                }
                generated_secret_string = json.dumps(values)
                aws_secret.create_secret(name=generated_secret_name, string=generated_secret_string,
                                         tags=generated_tags, description=description)
                print(f'Created deployment secret {generated_secret_name}')
        elif not aws_secret.secret_exists(secret_name):
            secret_string = json.dumps(values)
            tags = {
                "clusterName": cluster_name,
                "appName": app_name,
                "env": env,
                "secretType": SECRET_TYPES.app
            }
            aws_secret.create_secret(name=secret_name, string=secret_string, tags=tags, description=description)
            print(f'Created deployment secret {secret_name}')


def generate_jwt_key():
    """
    Generates a jwt secret key of 40 alphanumeric characters.

    :returns: jwt secret key
    """
    s3_client = region.get_secret()
    try:
        response = s3_client.get_random_password(
            PasswordLength=40,
            ExcludeCharacters="",
            ExcludeNumbers=False,
            ExcludePunctuation=True,
            ExcludeUppercase=False,
            ExcludeLowercase=False,
            IncludeSpace=False,
            RequireEachIncludedType=True
        )
        return response['RandomPassword']
    except Exception as e:
        print('Failed to generate jwt secret key')
        raise e


def add_standard_info_to_aws_secrets(app_config: dict):
    """
    Adds information to each AWS secret that is standard for every deployment.

    Keys added:

    ds-url: Access url for the database
    ds-schema: Schema to use when accessing the database

    :param app_config: app_config.yml dict.
    """
    deployments = app_config['appInstances']
    for app_instance in deployments:
        cluster_name = app_instance['clusterName']
        secret_name = app_instance['appSecret'] if app_instance['customer'] is None else app_instance[
            'generatedAppSecret']
        db_name = app_instance['dbName']

        # find the rds instance for this deployment
        instances = rds.list_db_instances(eks_cluster_name=cluster_name)
        if len(instances) < 1:
            print(f'No db instance found for {cluster_name}. Skipping editing {secret_name}.')
            continue
        instance = instances[0]

        # generate ds-url
        address = instance['Endpoint']['Address']
        url = f'{address}:5432/{db_name}'

        # do not change the jwt-key if it already exists
        jwt_key = aws_secret.get_secret_value(secret_name, 'jwt-key')
        if jwt_key is None:
            jwt_key = generate_jwt_key()

        values = {
            'ds-url': url,
            'ds-schema': app_instance['dbSchema'],
            'jwt-key': jwt_key,
            'password-reset-url': 'user/reset-password'
        }

        aws_secret.update_secret(secret_name, kvp=values, overwrite_json=False)


def delete_app_aws_secrets(app_config: dict):
    """
    Deletes the AWS secrets for each deployment instance if they exist.

    :param app_config: app_config.yml dict.
    """
    deployments = app_config['appInstances']
    for app_instance in deployments:
        secret_name = app_instance['appSecret'] if app_instance['customer'] is None else app_instance[
            'generatedAppSecret']
        result = aws_secret.delete_secret(secret_name, perma_delete=True)
        if result:
            print(f'Deleted secret {secret_name}')


def delete_service_application_databases(app_config: dict):
    deployments = app_config['deployments']
    app_name = app_config['appName']

    for deployment in deployments:
        cluster_name = deployment['clusterName']
        environments = deployment['environments']
        db_instances = rds.list_db_instances(eks_cluster_name=cluster_name)
        if not db_instances:
            continue
        for environment in environments:
            env = environment['env']
            rds_instance = environment.get('rdsInstance', None)
            delete_app_database(cluster_name=cluster_name, app_name=app_name, env=env, rds_instance=rds_instance)

    print(f'{app_name} service databases deleted.')


def create_promote_ui_stack(app_dir: str):
    """
    Creates a CloudFormation stack with an AWS Automation Document for manually calling a lambda function to
    promote a specific UI build to a SAT or PRD environment.
    The CloudFormation file is placed in the 'values' directory.

    :param app_dir: directory containing app config and 'values' directory
    """
    app_config = read_app_config(app_dir)
    ui_dir = os.path.join(CFM_DIR, 'promote-ui')

    # read lambda code
    script_path = os.path.join(ui_dir, 'promote-ui.py')
    with open(abs_path(script_path)) as f:
        script = f.read()

    app_name = app_config['appName'].lower()
    safe_app_name = app_name.replace('.', '-')
    web_site = app_config.get('webSite', False)
    root_domain = app_config['rootDomain']

    sat_bucket = f'www.sat.{root_domain}' if web_site else f'{app_name}.sat.{root_domain}'
    prd_bucket = f'www.{root_domain}' if web_site else f'{app_name}.{root_domain}'
    builds_bucket = f'{prd_bucket}-builds'

    params = {
        'appName': app_name,
        'script': script,
        'buildsBucket': builds_bucket,
        'satBucket': sat_bucket,
        'prdBucket': prd_bucket,
        'region': region.get_default_region(),
        'lambdaLayer': create_aws_cli_lambda_layer(),
        # leave "{{Version}}" and "{{TargetEnv}}" in template after render
        'Version': VERSION_TEMPLATE,
        'TargetEnv': '{{TargetEnv}}'
    }

    # render template and write to 'values' dir
    template_body = render_template(ui_dir, 'promote-ui-template.yml', params)
    values_path = os.path.join(app_dir, 'values')
    pathlib.Path(values_path).mkdir(parents=True, exist_ok=True)
    file_name = 'promote-ui.yml'
    file_path = os.path.join(values_path, file_name)
    with open(file_path, 'w') as file:
        file.write(template_body)

    # create stack
    params = {
        # becomes {app_name}-promote-ui
        'stackName': f'{safe_app_name}',
        # leave "{{Version}}" and "{{TargetEnv}}" in template after render
        'Version': VERSION_TEMPLATE,
        'TargetEnv': '{{TargetEnv}}'
    }
    tags = {
        'appName': app_name,
        'StackType': 'promote-ui'
    }
    cfm.set_template_path(values_path)
    return cfm.create_stack(template_name='promote-ui', params=params, capabilities=['CAPABILITY_NAMED_IAM'], tags=tags)


def create_aws_cli_lambda_layer():
    """
    Creates a lambda layer for using the aws cli inside of lambda functions.

    :return: ARN of the aws-cli and the version ARN:version'
    """
    layer_name = 'aws-cli-layer'
    client = region.get_lambda()

    # find existing layer
    layers = client.list_layers(
        CompatibleRuntime='python3.8'
    ).get('Layers', [])

    for layer in layers:
        if layer['LayerName'] == layer_name:
            print(f'Found lambda layer: {layer_name}')
            return f'{layer["LayerArn"]}:{layer["LatestMatchingVersion"]["Version"]}'

    # create layer
    print('Reading and uploading aws cli zipfile...')
    zip_path = abs_path(os.path.join(CFM_DIR, 'promote-ui', 'awscli-lambda-layer.zip'))
    with open(zip_path, 'rb') as file:
        zip_file = file.read()
    response = client.publish_layer_version(
        LayerName=layer_name,
        Description='Lambda Layer for using the awscli in python3.8 lambdas.',
        Content={
            'ZipFile': zip_file
        },
        CompatibleRuntimes=[
            'python3.8',
        ],
    )
    print(f'Created lambda layer: {layer_name}')
    return f'{response["LayerArn"]}:{response["Version"]}'


def delete_promote_ui_stack(app_name):
    """
    Deletes the promote_ui stack for an app.

    :param app_name: The app to delete the promote-ui stack for.
    """
    stack = cfm.find_stack(StackType='promote-ui', appName=app_name.lower())
    if stack:
        cfm.delete_stack(stack.get('StackName'))


def create_promote_service_stack(app_dir):
    """
    Creates a CloudFormation stack with an AWS Automation Document for manually calling a lambda function to
    promote a specific service build. Users may apply 'test', 'blue', 'green', or 'prd' tags.
    The CloudFormation file is placed in the 'values' directory.

    :param app_dir: directory containing app config and 'values' directory
    """
    app_config = read_app_config(app_dir)
    service_dir = os.path.join(CFM_DIR, 'promote-service')

    app_name = app_config['appName'].lower()

    # read lambda code
    script_path = os.path.join(service_dir, 'promote-service.py')
    with open(abs_path(script_path)) as f:
        script = f.read()

    params = {
        'appName': app_name,
        'region': region.get_default_region(),
        'script': script,
        # leave "{{Version}}" and "{{Tag}}" in template after render
        'Version': VERSION_TEMPLATE,
        'Tag': '{{Tag}}'
    }

    # render template and write to 'values' dir
    template_body = render_template(service_dir, 'promote-service-template.yml', params)
    values_path = os.path.join(app_dir, 'values')
    pathlib.Path(values_path).mkdir(parents=True, exist_ok=True)
    file_name = 'promote-service.yml'
    file_path = os.path.join(values_path, file_name)
    with open(file_path, 'w') as file:
        file.write(template_body)

    # create stack
    params = {
        # becomes {app_name}-promote-service
        'stackName': f'{app_name}',
        # leave "{{Version}}" and "{{TargetEnv}}" in template after render
        'Version': VERSION_TEMPLATE,
        'Tag': '{{Tag}}'
    }
    tags = {
        'appName': app_name,
        'StackType': 'promote-service'
    }
    cfm.set_template_path(values_path)
    return cfm.create_stack(template_name='promote-service', params=params,
                            capabilities=['CAPABILITY_NAMED_IAM'], tags=tags)


def delete_promote_service_stack(app_name):
    """
    Deletes the promote-service stack for an app.

    :param app_name: The app to delete the promote-service stack for.
    """
    stack = cfm.find_stack(StackType='promote-service', appName=app_name.lower())
    if stack:
        cfm.delete_stack(stack.get('StackName'))


def set_up_google_chat(app_config: dict, defaults: dict):
    app_name = app_config['appName']
    secret_name = f'{app_name}-google-chat-cred'
    if not aws_secret.secret_exists(name=secret_name):
        print(f'No Google Chat credential found for application {app_name}. Skipping...')
        return False
    hook_url = aws_secret.get_secret_value(secret_name, 'url')
    return create_google_chat_credential(defaults, secret_name, hook_url)


def create_ecr_sync_cron_job(app_dir: str):
    """
    Creates a cron job for copying ECR images from nonprod to prod account ECR.

    :param app_dir: Directory containing ecr-sync-values.yml
    """
    from k9.templates import read_ecr_sync_values
    values = read_ecr_sync_values(app_dir)
    # generate cron job spec
    contents = render_template('yaml/ecr-sync', 'ecr-sync-cj-template.yml', values)
    cronjob_path = os.path.join(app_dir, 'values', 'ecr-sync-cj.yml')
    with open(cronjob_path, 'w+') as file:
        file.write(contents)

    # apply file to cluster
    connect_to_cluster(values['clusterName'])
    ns = values['namespace']
    if not namespace_exists(ns):
        create_namespace(ns)
    shell(f'kubectl apply -f {cronjob_path} -n {ns}')


def delete_ecr_sync_cron_job(app_dir: str):
    """
    Deletes cron job created by create_ecr_sync_cron_job.

    :param app_dir: Directory containing ecr-sync-values.yml
    """
    from k9.templates import read_ecr_sync_values
    values = read_ecr_sync_values(app_dir)

    connect_to_cluster(values['clusterName'])
    ns = values['namespace']
    shell(f'kubectl delete cronjob ecr-sync -n {ns}')
