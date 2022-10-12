from aws import rds, region, cluster
from jinja2 import Environment, FileSystemLoader
from k9 import deploy
from os import path

MODULE_DIR = path.abspath(path.dirname(__file__))
TEMPLATE_DIR = path.join(MODULE_DIR, 'factsheet')


def generate_application_factsheet(app_config: dict, is_service: bool, is_prd: bool, output_dir: str = '.'):
    '''
    Create factsheet for an application.

    :param app_config: The app configuration as a dict
    :param is_service: Whether the factsheet is being generated for the service
    :param is_prd: Whether the factsheet is being generated just for production deployment
    :param output_dir: The target directory for the factsheet file. Defaults to current working directory
    :return: the name of the file that has been created
    '''
    app_name = app_config['appName']
    factsheet_type = 'service' if is_service else 'ui'

    if is_prd:
        print(f'Generating prd {factsheet_type} application factsheet for {app_name}...')
    else:
        print(f'Generating {factsheet_type} application factsheet for {app_name}...')

    # validate input
    assert app_config, 'generate_application_factsheet() requires app_config'
    assert path.isdir(output_dir), 'generate_application_factsheet() requires a valid output_dir'

    params = _get_application_template_params(app_config, is_service)

    # apply params to template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), lstrip_blocks=True, trim_blocks=True, autoescape=True)

    if is_prd:
        factsheet_file = 'prd-service-app-factsheet.md' if is_service else 'prd-ui-app-factsheet.md'
    else:
        factsheet_file = 'service-app-factsheet.md' if is_service else 'ui-app-factsheet.md'
    template = env.get_template(factsheet_file)

    if is_prd:
        filename = f'prd-{app_name}-service-factsheet.md' if is_service else f'prd-{app_name}-ui-factsheet.md'
    else:
        filename = f'{app_name}-service-factsheet.md' if is_service else f'{app_name}-ui-factsheet.md'
    template.stream(params).dump(path.join(output_dir, filename))

    return filename


def _get_application_template_params(app_config: dict, is_service: bool):
    params = {}

    # Basic Info
    app_name = app_config['appName']
    params['appName'] = app_name
    params['account'] = region.get_account_id()
    account_aliases = region.get_iam().list_account_aliases()['AccountAliases']
    params['accountAlias'] = account_aliases[0] if account_aliases else None
    params['region'] = region.get_session_region()
    is_govcloud = 'gov' in region.get_session_region()
    params['govCloud'] = is_govcloud
    params['awsLink'] = 'amazonaws-us-gov.com' if is_govcloud else 'aws.amazon.com'

    app_instances = app_config['appInstances']
    root_domain = app_config['rootDomain']
    web_site = app_config.get('webSite', False)

    if is_service:
        _get_service_application_template_params(params, app_instances, app_name)
    else:
        _get_ui_application_template_params(params, app_instances, app_name, is_govcloud, root_domain, web_site)

    return params


def _get_service_application_template_params(params: dict, app_instances: dict, app_name: str):
    service_deployment_infos = []
    _get_service_deployment_information(params, app_instances, service_deployment_infos)

    # RDS instance information
    rds_instance_infos = []
    env_list = []
    _get_service_rds_information(params, app_instances, env_list, rds_instance_infos)

    # Database information
    database_infos = []
    _get_service_database_information(params, app_instances, database_infos)

    params['ecr'] = app_name
    params['servicePromotion'] = f'{app_name}-service-promotion'


def _get_service_deployment_information(params: dict, app_instances: dict, service_deployment_infos: list):
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        customer = app_instance['customer']
        service_url = app_instance['serviceUrl']
        app_secret = app_instance['appSecret'] if customer is None else app_instance['generatedAppSecret']
        spring_active_profile = app_instance['springActiveProfile']
        info = {
            'clusterName': cluster_name,
            'env': env,
            'customer': customer,
            'serviceUrl': service_url,
            'appSecret': app_secret,
            'springActiveProfile': spring_active_profile,
        }
        service_deployment_infos.append(info)
    params['serviceDeploymentInformation'] = service_deployment_infos


def _get_service_rds_information(params: dict, app_instances: dict, env_list: list, rds_instance_infos: list):
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        if env in env_list:
            continue
        env_list.append(env)
        rds_instance_identifier = app_instance['rdsInstanceName']

        if rds_instance_identifier == None or rds_instance_identifier == '':
            continue
        else:
            rds_instance = rds.get_db_instance(rds_instance_identifier)
            instance_endpoint = rds_instance['Endpoint']['Address'] + ':' + str(rds_instance['Endpoint']['Port'])
            rds_instance_login_credential = f'{rds_instance_identifier}-credentials'
            info = {
                'clusterName': cluster_name,
                'env': env,
                'rdsInstanceIdentifier': rds_instance_identifier,
                'rdsInstanceEndpoint': instance_endpoint,
                'rdsInstanceLoginCredential': rds_instance_login_credential,
            }
            rds_instance_infos.append(info)

    params['rdsInstanceInformation'] = rds_instance_infos


def _get_service_database_information(params: dict, app_instances: dict, database_infos: list):
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        customer = app_instance['customer']
        database_name = app_instance['dbName']
        database_schema = app_instance['dbSchema']
        app_instance_name = app_instance['appInstanceName']
        database_users = [f'{app_instance_name}-owner', f'{app_instance_name}-master', f'{app_instance_name}-readonly']
        info = {
            'clusterName': cluster_name,
            'env': env,
            'customer': customer,
            'databaseName': database_name,
            'databaseSchema': database_schema,
            'databaseUsers': database_users
        }
        database_infos.append(info)
    params['databaseInformation'] = database_infos


def _get_ui_application_template_params(params: dict, app_instances: dict, app_name: str, is_govcloud: bool,
                                        root_domain: str, web_site: bool):
    # UI deployment information
    ui_deployment_info = []
    _get_ui_deployment_information(params, app_instances, ui_deployment_info)

    # UI buckets and cloudfront
    ui_other = []
    hosted_envs = []
    _get_ui_buckets_and_cloudfront(params, app_instances, app_name, is_govcloud, ui_other, hosted_envs)
    params['buildsBucket'] = deploy.get_build_bucket_name(web_site, app_name, root_domain)

    # VPC Endpoint
    vpc_endpoints = []
    _get_ui_vpc_endpoints(params, app_instances, is_govcloud, vpc_endpoints)

    params['uiPromotion'] = f'{app_name}-ui-promotion'


def _get_ui_deployment_information(params: dict, app_instances: dict, ui_deployment_info: list):
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        customer = app_instance['customer']
        ui_url = app_instance['uiUrl']
        info = {
            'clusterName': cluster_name,
            'env': env,
            'customer': customer,
            'uiUrl': ui_url,
        }
        ui_deployment_info.append(info)
    params['uiDeploymentInformation'] = ui_deployment_info


def _get_ui_buckets_and_cloudfront(params: dict, app_instances: dict, app_name: str, is_govcloud: bool,
                                   ui_other: list, hosted_envs: list):
    for app_instance in app_instances:
        cluster_name = app_instance['clusterName']
        env = app_instance['env']
        if env in hosted_envs:
            continue
        hosted_envs.append(env)
        if is_govcloud:
            stack = cluster.get_s3_gov_hosting(cluster_name=cluster_name, app_name=app_name, env_name=env)
            s3_bucket = cluster._get_output(stack, "Bucket")
            cloudfront_distribution = 'N/A'
        else:
            stack = cluster.get_s3_hosting(cluster_name=cluster_name, app_name=app_name, env_name=env)
            if stack is None:
                continue
            else:
                s3_bucket = cluster._get_output(stack, "Bucket")
                cloudfront_distribution = cluster._get_output(stack, "Distribution")
        info = {
            'clusterName': cluster_name,
            'env': env,
            's3Bucket': s3_bucket,
            'cloudfrontDistribution': cloudfront_distribution,
        }
        ui_other.append(info)
    params['uiOther'] = ui_other


def _get_ui_vpc_endpoints(params: dict, app_instances: dict, is_govcloud: bool, vpc_endpoints: list):
    if is_govcloud:
        hosted_clusters = []
        for app_instance in app_instances:
            cluster_name = app_instance['clusterName']
            if cluster_name in hosted_clusters:
                continue
            stack = cluster.get_vpc_endpoint(cluster_name)
            vpc_endpoint = cluster._get_output(stack, "VpcEndpoint")
            info = {
                'clusterName': cluster_name,
                'vpcEndpoint': vpc_endpoint,
            }
            vpc_endpoints.append(info)
    params['vpcEndpoint'] = vpc_endpoints
