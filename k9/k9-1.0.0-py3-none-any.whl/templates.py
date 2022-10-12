import os
import pathlib
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader
from aws import config, region

from k9.core import abs_path, render_template
from k9.deploy import read_app_config, read_yaml, get_caller_identity

DIR_PROJECT_TEMPLATE: str = 'yaml/project-templates'
CFM_DIR = 'yaml/cfm'
DEFAULTS_YML_NAME = 'defaults.yml'
CLUSTER_CONFIG = 'cluster-config.yml'


def get_cfm_templates(cwd: str):
    """
    Helper method to copy default CloudFormation files from atomic-cloud into the given directory.

    :param cwd: The directory to copy templates into
    """
    # search for provided cfm templates
    file_types = [CLUSTER_CONFIG, '00-cert.yml', '01-vpc.yml', '02-eks-cp.yml', '03-eks-workers.yml',
                  '04-rds.yml']
    for ft in file_types:
        found = False
        for file_name in os.listdir(cwd):
            if ft == file_name:
                found = True
                break

        if found:
            print(f'Found {ft} file in current working directory...')
        else:
            print(f'Copying {ft} default file into current working directory')
            file_path = os.path.join(cwd, ft)
            with open(file_path, 'w+') as file:
                # there is no cluster-config.yml template in atomic-cloud
                if ft == CLUSTER_CONFIG:
                    # must prompt user to render k9 template
                    cluster_name = input('Input clusterName: \n')
                    root_domain = input('Enter rootDomain. ex: "simoncomputing.com":\n')
                    params = {
                        'clusterName': cluster_name,
                        'isPrd': cluster_name == 'prd',
                        'isCicd': cluster_name == 'cicd',
                        'rootDomain': root_domain
                    }
                    contents = render_template(DIR_PROJECT_TEMPLATE, 'cluster-config-template.yml', params)
                else:
                    # get template file from atomic-cloud
                    contents = config.get_cfm_file(ft)
                file.write(contents)


def add_cluster_template(k9_dir: str, cluster_name: str, root_domain: str):
    """
    Creates a k9 subdirectory for a cluster and adds cluster-config.yml

    :param k9_dir: the k9 root directory
    :param cluster_name: the clusterName to create directory for. Used to fill out cluster-config.
    :param root_domain: the root domain for the cluster. Templated into baseDomain and validationDomain.
    """
    cluster_dir = os.path.join(k9_dir, cluster_name)
    pathlib.Path(cluster_dir).mkdir(parents=True, exist_ok=True)

    is_prd = cluster_name == 'prd'
    is_cicd = cluster_name == 'cicd'

    # get jinja formatted cluster-config
    params = {
        'clusterName': cluster_name,
        'isPrd': is_prd,
        'isCicd': is_cicd,
        'rootDomain': root_domain
    }
    template_body = render_template(DIR_PROJECT_TEMPLATE, 'cluster-config-template.yml', params)

    config_path = os.path.join(cluster_dir, CLUSTER_CONFIG)

    with open(config_path, 'w') as file:
        file.write(template_body)
    print(f'Created {cluster_name} cluster directory.')


def create_app_template(k9_dir: str, app_name: str, root_domain: str):
    """
    Creates a k9 subdirectory for an app and adds app-config.yml and k9-helm-values.yml.
    Creates empty 'values' directory.

    :param k9_dir:the k9 root directory
    :param app_name: the appName to create directory for. Used to fill out app-config.
    :param root_domain: Used to fill out app-config.
    """
    app_dir = os.path.join(k9_dir, f'apps/{app_name}')
    pathlib.Path(app_dir).mkdir(parents=True, exist_ok=True)

    # get jinja formatted cluster-config
    params = {
        'appName': app_name,
        'rootDomain': root_domain
    }
    templates_dir = abs_path(DIR_PROJECT_TEMPLATE)
    jinja_env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)

    files = ['app-config', 'k9-helm-values', 'helm-values']
    # render each template and write the output to the app directory
    for file_name in files:
        template = jinja_env.get_template(f'{file_name}-template.yml')
        template_body = template.render(params)
        file_path = os.path.join(app_dir, f'{file_name}.yml')

        with open(file_path, 'w') as file:
            file.write(template_body)

    # values directory
    values_dir = os.path.join(app_dir, 'values')
    pathlib.Path(values_dir).mkdir(parents=True, exist_ok=True)

def create_prd_app_template(app_dir: str):
    """
    This is used when the production environment is on a different account than the
    non-production environments.
    Adds prd-app-config.yml to the application directory

    :param app_dir: The directory containing app_config.yml
    """
    app_config = read_app_config(app_dir)
    app_name = app_config['appName']
    root_domain = app_config['rootDomain']

    params = {
        'appName': app_name,
        'rootDomain': root_domain
    }

    contents = render_template(DIR_PROJECT_TEMPLATE, 'prd-app-config-template.yml', params)

    output_path = os.path.join(app_dir, 'prd-app-config.yml')
    with open(output_path, 'w+') as file:
        file.write(contents)

def create_app_defaults(apps_dir: str):
    """
    Creates defaults.yml file in k9/apps

    :param apps_dir: The directory to place defaults.yml in
    """
    file_path = abs_path('yaml/project-templates/defaults-template.yml')
    with open(file_path, 'r') as file:
        contents = file.read()

        write_file_path = os.path.join(apps_dir, DEFAULTS_YML_NAME)
        with open(write_file_path, 'w') as write_file:
            write_file.write(contents)


def create_project_template(parent_dir: str):
    """
    Sets up the k9 directory when starting to use k9.

    :param parent_dir: path of the parent directory above k9/
    """
    k9_dir = os.path.join(parent_dir, 'k9')

    root_domain = input('Enter rootDomain. ex: "simoncomputing.com":\n')

    # cluster directories
    add_cluster_template(k9_dir, 'prd', root_domain)
    add_cluster_template(k9_dir, 'np', root_domain)
    while True:
        cluster_name = input('Enter a clusterName or empty line to finish creating cluster directories:\n')
        if cluster_name == '':
            break
        add_cluster_template(k9_dir, cluster_name, root_domain)

    # app directories
    app_name_entered = False
    while True:
        app_name = input('Enter appName or an empty line to finish:\n')
        if app_name == '':
            break
        app_name_entered = True
        create_app_template(k9_dir, app_name, root_domain)

    if not app_name_entered:
        print('The application name was not entered, so the apps folder will not be created. '
              'To create this folder, rerun and enter the appName.')
    else:
        create_app_defaults(os.path.join(k9_dir, 'apps'))

    print('K9 project template complete')


def combine_helm_files(app_dir: str):
    """
    Takes in a base dictionary helm values file and adds a k9: section with information from k9-helm-values.yml.

    :param app_dir: the directory containing k9-helm-values.yml and helm-values.yml

    :return: A dictionary that is the combination of the base_dict and the k9 section.
    """
    # read yml files
    k9_helm_path = os.path.join(app_dir, 'k9-helm-values.yml')
    helm_path = os.path.join(app_dir, 'helm-values.yml')
    k9_helm_values = read_yaml(k9_helm_path)
    helm_values = read_yaml(helm_path)

    if helm_values is None:
        # handle empty file
        helm_values = {}

    # add k9 values to a k9 section in the original helm values file
    helm_values['k9'] = {}
    for key, val in k9_helm_values.items():
        helm_values['k9'][key] = val

    return helm_values


def read_blue_green_template(instance: dict, defaults):
    """
    Reads the blue-green template and fills it with proper values for the given deploy instance.

    :param instance: dict object containing information about a particular deployment instance.
    :param defaults: defaults.yml dict

    :return: blue-green file content
    """

    # certs must be requested beforehand, find them even if they are not approved yet
    service_cert_arn = None
    client = region.get_acm()
    certs = client.list_certificates().get('CertificateSummaryList')
    for c in certs:
        if c['DomainName'] == instance['serviceCertUrl']:
            service_cert_arn = c['CertificateArn']
    if service_cert_arn is None:
        print('WARNING: certificate ARN not found')

    account_id = get_caller_identity().get('Account')

    # check if useBlueGreen was specified in app-config.yml for this instance
    if instance['useBlueGreen'] is not None:
        use_blue_green = instance['useBlueGreen']
    else:
        # not found, so read defaults.yml to find the cluster's default value
        use_blue_green = False
        defaults_clusters = defaults['clusters']
        for cluster in defaults_clusters:
            if cluster['clusterName'] == instance['clusterName']:
                use_blue_green = cluster['useBlueGreen']
    
    app_secret_name = instance['appSecret'] if instance['customer'] is None else instance['generatedAppSecret']

    # params defined in blue-green-template.yml
    params = {
        'instance': instance,
        'appSecretName': app_secret_name,
        'serviceCertArn': service_cert_arn,
        'AWSAccount': account_id,
        'dbSecretName': f"{instance['dbSchema'].replace('_','-')}-owner",
        'useBlueGreen': use_blue_green,
        'region': region.get_default_region(),
        'fips': ''  # set to '-fips' to use fips endpoint
    }

    template = render_template(DIR_PROJECT_TEMPLATE, 'blue-green-template.yml', params)
    return template


def generate_helm_values_files(app_dir: str, defaults: dict):
    """
    Generates a helm values.yml for each deployment in app-config.yml. Copies the helm_values contents. Adds
    a k9 section for helm install information. Adds a section for blue-green deployment information.

    :param app_dir: the app directory. Should contain app-config.yml, k9-helm-values.yml, and helm-values.yml.
    :param defaults: defaults.yml dict
    """
    app_config = read_app_config(app_dir)
    helm_values = combine_helm_files(app_dir)

    # make sure values dir exists
    values_dir = os.path.join(app_dir, 'values')
    pathlib.Path(values_dir).mkdir(parents=True, exist_ok=True)

    # create values file for each instance
    instances = app_config['appInstances']
    for instance in instances:
        instance_name = instance['appInstanceName']
        namespace = instance['namespace']

        helm_values['k9']['namespace'] = namespace
        helm_values['k9']['releaseName'] = namespace
        file_content = yaml.dump(helm_values, default_flow_style=False)
        file_content += '\n' + read_blue_green_template(instance, defaults)

        # get values.yml file name
        file_name = f'{instance_name}-values.yml'
        values_path = os.path.join(values_dir, file_name)

        if os.path.exists(values_path):
            print(f'{file_name} exists. Skipping creation.')
            continue

        with open(values_path, 'w') as file:
            file.write(file_content)
        print(f'created {file_name}')


def create_gov_ui_values(params: dict, app_dir: str):
    """
    Creates a values.yml file for the helm deployment for a govcloud ui.

    :param params: the parameters to pass to the template.
    :param app_dir: the directory containing the 'values' directory to place the rendered template in.

    :returns: The values file name.

    """
    template = render_template(DIR_PROJECT_TEMPLATE, 'ui-routing-values-template.yml', params)

    values_dir = os.path.join(app_dir, 'values')
    pathlib.Path(values_dir).mkdir(parents=True, exist_ok=True)

    # get values.yml file name
    instance_name = params['deploymentName']
    file_name = f'{instance_name}-values.yml'
    values_path = os.path.join(values_dir, file_name)

    if os.path.exists(values_path):
        print(f'{file_name} exists. Skipping creation.')
        return values_path

    with open(values_path, 'w') as file:
        file.write(template)
    print(f'created {file_name}')
    return values_path


def read_app_defaults(apps_dir: str):
    """
    Reads defaults.yml into a dictionary.

    :params apps_dir: full file path to the k9/apps directory.

    :returns: defaults.yml as a dictionary
    """
    file_path = os.path.join(apps_dir, DEFAULTS_YML_NAME)
    return read_yaml(file_path)


def write_app_defaults(apps_dir: str, dict_content: dict):
    """
    Creates defaults.yml file from a dictionary

    :params apps_dir: Full file path to the k9/apps directory.
    :params dict_content: The dictionary version of what to write in defaults.yml
    """
    file_content = yaml.dump(dict_content, default_flow_style=False)
    file_path = os.path.join(apps_dir, DEFAULTS_YML_NAME)
    with open(file_path, 'w') as file:
        file.write(file_content)
    print('Edited defaults.yml successfully')


def get_cfm_file(file_name: str, cwd: str):
    """
    Copies a file from the k9/yaml/cfm directory to the provided directory

    :params file_name: the file name in k9/yaml/cfm
    :params cwd: the target directory
    """
    cfm_dir = abs_path(CFM_DIR)
    source_file_path = os.path.join(cfm_dir, file_name)
    target_file_path = os.path.join(cwd, file_name)

    shutil.copy(source_file_path, target_file_path)


def create_ecr_sync_values(app_dir: str, cluster_name: str = 'None'):
    """
    Creates the ecr-sync-values.yml file for "k9 create ecr-sync"

    :param app_dir: The directory containing app_config.yml
    :param cluster_name: Optional. Adds the clusterName to the generated values file.
    """
    app_config = read_app_config(app_dir)
    app_name = app_config['appName']

    params = {
        'appName': app_name.lower(),
        'region': region.get_default_region(),
        'account': get_caller_identity().get('Account'),
        'clusterName': cluster_name or ''
    }

    contents = render_template('yaml/ecr-sync', 'ecr-sync-values-template.yml', params)

    output_path = os.path.join(app_dir, 'ecr-sync-values.yml')
    with open(output_path, 'w+') as file:
        file.write(contents)


def read_ecr_sync_values(app_dir: str):
    """
    Reads ecr-sync-values.yml into a dictionary.

    :param app_dir: The directory containing ecr-sync-values.yml

    :returns: dictionary of ecr-sync values
    """
    file_path = os.path.join(app_dir, 'ecr-sync-values.yml')
    return read_yaml(file_path)
