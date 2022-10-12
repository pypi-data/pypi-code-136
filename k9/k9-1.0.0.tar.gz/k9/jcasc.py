import requests
import os

from k9.core import abs_path, render_template, \
    get_configmap, update_configmap, connect_to_cluster
from k9.cluster_init import _get_jenkins_password
from k9.helm import helm_exists

from aws import secret

JENKINS_PATH = 'yaml/jenkins'
JENKINS_DIR = abs_path(JENKINS_PATH)
JCASC_MAP_NAME = 'jenkins-jenkins-jcasc-config'


class JenkinsSession:

    session = None
    url = ''
    crumb = ''

    def __init__(self, url: str, password: str):
        """
        Sets up a Jenkins session

        :param url: Jenkins url to connect to.
        :param password: Admin password to Jenkins.
        """

        self.url = url
        self.session = requests.Session()
        self.session.auth = ("admin", password)

        crumb_url = os.path.join(self.url, 'crumbIssuer/api/json')
        response = self.session.get(crumb_url)
        self.crumb = response.json()['crumb']
        self.session.headers = {'Jenkins-Crumb': self.crumb}

    def post_script(self, script_name):
        """
        Executes a script in the yaml/jenkins directory on Jenkins.

        :param script_name: name of the script to execute
        """
        script_name += '.groovy'
        print(f'Executing {script_name}')
        script_path = os.path.join(JENKINS_DIR, script_name)
        with open(script_path, 'r') as file:
            data = {
                'script': file.read()
            }
        script_url = os.path.join(self.url, 'scriptText/')
        response = self.session.post(url=script_url, data=data)
        print(response.reason)
        return response

    def refresh_jcasc(self):
        """
        Sends a POST request to the JCasC endpoint that refreshes it. Must be called after updating the
        JCasC ConfigMap to let changes have an effect.
        """
        print('Refreshing jcasc...')
        refresh_url = os.path.join(self.url, 'configuration-as-code/reload')
        response = self.session.post(url=refresh_url)
        print(response.reason)
        return response


def create_jenkins_pipeline(app_config: dict, defaults: dict, is_service: bool):
    """
    Creates the Service or UI Multibranch pipeline job and credentials on Jenkins.

    :param app_config: The dictionary version of app-config.yml.
    :param defaults: The dictionary version of defaults.yml.
    :param is_service: True if creating service pipeline. False for UI.

    :returns: True if jcasc returns ok for final refresh. False otherwise.
    """
    # set up jenkins session
    cluster_name = defaults['jenkins']['clusterName']
    print('Connecting to cicd cluster defined in defaults.yml')
    connect_to_cluster(cluster_name)
    if not helm_exists('jenkins', 'cicd'):
        return False

    url = defaults['jenkins']['jenkinsUrl']
    jenkins_pass = _get_jenkins_password(cluster_name)
    try:
        session = JenkinsSession(url, jenkins_pass)
    except requests.exceptions.ConnectionError:
        print(f'Could not connect to jenkins at {url}. Skipping configuration. '
              f'You may try again when Jenkins is running.')
        return False

    # create git credentials
    deployment_type = 'serviceDeployment' if is_service else 'webDeployment'
    secret_name = app_config[deployment_type]['deployTokenSecret']
    git_token = secret.get_secret_value(secret_name, 'password')
    if git_token is None:
        print(f'Could not find AWS secret {secret_name}. The credential in Jenkins must be manually updated.'
              f'Or you may update the AWS secret and try again.')
    username = secret.get_secret_value(secret_name, 'username')
    if username is None:
        # gitlab requires any non-blank username, so it is safe to default a username if not given one
        username = 'jenkins'
    create_username_password_secret(secret_name, username, git_token)
    session.refresh_jcasc()

    # create multibranch pipeline job
    create_multibranch_pipeline_job(app_config, is_service=is_service)
    session.refresh_jcasc()

    # create extra secrets
    create_extra_credentials(app_config)
    final_response = session.refresh_jcasc()

    print('Finished creating pipeline.')
    return final_response.ok


def link_jenkins_sonarqube(cluster_name: str, base_domain: str, secret_name: str, secret: str):
    """
    Creates the "Jenkins user in SonarQube" token credential and updates the SonarQube tool in Jenkins.

    :param cluster_name: The name of the cluster that contains Jenkins.
    :param base_domain: The base domain.
    :param secret_name: The name of the secret.
    :param secret: The secret token

    :returns: True if jcasc returns ok for final refresh. False otherwise.
    """
    connect_to_cluster(cluster_name)
    # set up jenkins session
    if not helm_exists('jenkins', 'cicd'):
        return False

    url = f'https://jenkins.{base_domain}'
    jenkins_pass = _get_jenkins_password(cluster_name)
    try:
        session = JenkinsSession(url, jenkins_pass)
    except requests.exceptions.ConnectionError:
        print(f'Could not connect to jenkins at {url}. Skipping configuration. '
              f'You may try again when Jenkins is running.')
        return False

    # create sonar-jenkins credentials
    create_secret_text_secret(secret_name=secret_name, secret=secret)
    session.refresh_jcasc()

    # update sonarqube tool
    update_sonarqube_tool(base_domain=base_domain, secret_name=secret_name)
    final_response = session.refresh_jcasc()

    print('Finished linking Jenkins and SonarQube.')
    return final_response.ok


def create_google_chat_credential(defaults: dict, secret_name: str, secret: str):
    cluster_name = defaults['jenkins']['clusterName']
    connect_to_cluster(cluster_name)
    if not helm_exists('jenkins', 'cicd'):
        return False

    url = defaults['jenkins']['jenkinsUrl']
    jenkins_pass = _get_jenkins_password(cluster_name)
    try:
        session = JenkinsSession(url, jenkins_pass)
    except requests.exceptions.ConnectionError:
        print(f'Could not connect to jenkins at {url}. Skipping configuration. '
              f'You may try again when Jenkins is running.')
        return False
    
    create_secret_text_secret(secret_name=secret_name, secret=secret)
    final_response = session.refresh_jcasc()

    print('Finished creating Google Chat credential.')
    return final_response.ok


def update_sonarqube_tool(base_domain: str, secret_name: str):
    """
    Updates the SonarQube tool in Jenkins using the newly created secret

    :param base_domain: The base domain of the sonar site.
    :param secret_name: The name of the secret.
    """
    sonar_url = f'https://sonar.{base_domain}'
    params = {
        'secretName': secret_name,
        'sonarUrl': sonar_url
    }

    template_body = render_template(JENKINS_PATH, 'configure-sonarqube.yml', params)
    patch_jcasc_config_map('configure-sonarqube', template_body)


def get_jcasc_config_map():
    """
    Gets the JCasC ConfigMap from kubernetes.

    :returns: The ConfigMap for JCasC configuration.
    """
    config_map = get_configmap(name=JCASC_MAP_NAME, namespace='cicd')
    return config_map


def patch_jcasc_config_map(key_name: str, contents: str):
    """
    Edits the JCasC ConfigMap to add a new entry. This will create a new file in the jcasc_configs directory.

    :param key_name: Used to create the file name for the yaml contents. key_name.yaml
    :param contents: The yaml formatted JCasC contents to store in the file.
    """
    file_name = key_name + '.yaml'
    print(f'Adding {file_name} to JCasC')
    config_map = get_jcasc_config_map()
    config_map.data[file_name] = contents
    update_configmap(name=JCASC_MAP_NAME, body=config_map, namespace='cicd')


def create_username_password_secret(secret_name: str, username: str, password: str):
    """
    Creates a usernamePassword credential on Jenkins.

    :param secret_name: The unique id name of the secret.
    :param username: Username to store.
    :param password: Password to store
    """

    params = {
        'secretName': secret_name,
        'username': username,
        'password': password
    }

    template_body = render_template(JENKINS_PATH, 'credentials.yml', params)
    patch_jcasc_config_map(secret_name, template_body)


def create_secret_text_secret(secret_name: str, secret: str):
    """
    Creates a secret text credential on Jenkins.

    :param secret_name: The unique id name of the secret.
    :param secret: Secret to store
    """

    params = {
        'secretName': secret_name,
        'secret': secret
    }

    template_body = render_template(JENKINS_PATH, 'secret-text-credentials.yml', params)
    patch_jcasc_config_map(secret_name, template_body)


def create_multibranch_pipeline_job(app_config: dict, is_service: bool):
    """
    Creates a multibranch pipeline job on Jenkins

    :param app_config: app_config.yml dict.
    :param is_service: True if deploying service. False if UI.
    """
    deploy_type = 'service' if is_service else 'ui'

    deployment = 'serviceDeployment' if is_service else 'webDeployment'
    git_url = app_config[deployment]['repository']
    git_credential_name = app_config[deployment]['deployTokenSecret']

    app_name = app_config['appName']
    job_name = f'{app_name}-{deploy_type}'
    promote_path = 'jenkins/UpdateServiceVersion' if is_service else 'jenkins/UpdateUiVersion'

    folder_name = app_config['jenkins']['folderName']

    params = {
        'folderName': folder_name,
        'appName': app_name,
        'jobName': job_name,
        'repoUrl': git_url,
        'credentialsId': git_credential_name,
        'promotePath': promote_path,
        'deployType': deploy_type
    }

    template_body = render_template(JENKINS_PATH, 'multibranch-pipeline.yml', params)
    patch_jcasc_config_map(job_name, template_body)


def create_extra_credentials(app_config: dict):
    """
    Creates credentials in Jenkins if they are present in AWS.

    :param app_config: app_config.yml dict.
    """

    secrets_list = app_config['jenkins'].get('secrets', [])

    for item in secrets_list:
        secret_name = item['name']
        if secret.secret_exists(secret_name):
            print(f'Found AWS Secret: {secret_name}')
            username = secret.get_secret_value(secret_name, 'username')
            password = secret.get_secret_value(secret_name, 'password')
            create_username_password_secret(secret_name, username, password)
        else:
            print(f'{secret_name} does not exist. Skipping creating the jenkins credential. '
                  f'You may try again after creating the AWS secret.')
