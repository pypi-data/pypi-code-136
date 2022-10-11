# based on
# - https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/
# - https://github.com/PretzelLogix/py-cat-api

from datetime import datetime
from getpass import getpass
from typing import Dict, List
from urllib.parse import urljoin
import uuid as uuid_pkg

from dynaconf.utils.boxing import DynaBox
import requests
import yaml

from . import logger
from .common import encode_token, get_token_from_file, is_valid_uuid, write_token_to_file
from .exceptions import (
    TimonApiException,
    TimonException,
    TimonLoginRequiredException,
    TimonTokenExpiredException
)
from .models import *
from .schemas import validate_content


class Client:
    def __init__(self, profile: DynaBox, token: Token = None):
        self.token = token
        self.profile = profile
        self.api_url = urljoin(self.profile.api_url, f"{self.profile.api_version}/")
        self.headers = {}

        logger.debug(f"profile = {self.profile.name}")
        logger.debug(f"api_url = {self.api_url}")

        if token:
            # refresh token expired
            if datetime.now().timestamp() - token.issue_timestamp > token.refresh_expires_in:
                raise TimonTokenExpiredException(f"Refresh token for {self.profile.name}")

            # refresh of token required
            elif datetime.now().timestamp() - token.issue_timestamp > token.expires_in:
                logger.debug(f"Token refresh required, refreshing token for {self.profile.name}")
                login_data = {
                    "organisation": token.organisation_id,
                    "project": token.project_id,
                    "refresh_token": token.refresh_token
                }
                result = self.post("auth/tokens", data=login_data)
                self.token = Token(**result.data)
                write_token_to_file(self.profile.name, self.token)

            # set authorization header
            encoded_token = encode_token(self.token)
            self.headers = {
                "Authorization": f"Bearer {encoded_token}"
            }

    def login(self) -> Token:
        password = self.profile.auth.get("password")
        if not password:
            self.profile.auth.password = getpass()
        login_data = {
            "organisation": self.profile.auth.organisation,
            "password": self.profile.auth.password,
            "project": self.profile.auth.project,
            "username": self.profile.auth.username
        }
        result = self.post("auth/tokens", data=login_data)

        self.token = Token(**result.data)
        write_token_to_file(self.profile.name, self.token)
        return self.token

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        url = urljoin(str(self.api_url), endpoint)

        log_line_pre = f"method={http_method}, url={url}, params={ep_params}"
        # log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))

        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            logger.debug(log_line_pre)
            response = requests.request(method=http_method, url=url, verify=self.profile.insecure,
                                        headers=self.headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            logger.error(str(e))
            raise TimonApiException("Request failed") from e

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200     # 200 to 299 is OK
        # log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            # logger.debug(log_line)
            return Result(status_code=response.status_code, headers=response.headers, message=response.reason, data=response.content)
        # logger.error(log_line)
        raise TimonApiException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params, data=data)

    def patch(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='PATCH', endpoint=endpoint, ep_params=ep_params, data=data)

    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)

    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)

    def fetch_data(self, url: str) -> bytes:
        # GET URL; catching, logging, and re-raising any exceptions
        http_method = 'GET'
        try:
            log_line = f"method={http_method}, url={url}"
            logger.debug(log_line)
            response = requests.request(method=http_method, url=url, verify=self.profile.insecure)
        except requests.exceptions.RequestException as e:
            logger.error(str(e))
            raise TimonApiException(str(e)) from e

        # If status_code in 200-299 range, return byte stream, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        log_line = f"success={is_success}, status_code={response.status_code}, message={response.reason}"
        logger.debug(log_line)
        if not is_success:
            raise TimonApiException(response.reason)

        return response.content


class Timon:
    def __init__(self, profile: DynaBox):
        self.profile = profile
        token = get_token_from_file(profile.name)
        if not token:
            raise TimonLoginRequiredException

        self.client = Client(profile=profile, token=token)

        if not self.profile.insecure:
            requests.packages.urllib3.disable_warnings()

        # organisation = profile.auth.organisation
        # if is_valid_uuid(organisation):
        #     self.organisation_id = organisation
        # else:
        #     self.organisation_id = self.get_organisation_id(organisation)

        # project = profile.auth.project
        # if is_valid_uuid(project):
        #     self.project_id = project
        # else:
        #     self.project_id = self.get_project_id(self.organisation_id, project)

        self.organisation_id = token.organisation_id
        self.project_id = token.project_id

        logger.debug(f"organisation = {self.organisation_id}")
        logger.debug(f"project = {self.project_id}")

    # blueprints

    def get_blueprint_id(self, blueprint: str, project: str = None) -> uuid_pkg.UUID:
        if is_valid_uuid(blueprint):
            return blueprint

        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"blueprints/{project_id}", ep_params={"q": blueprint})
        blueprint = Blueprint(**result.data[0])
        return blueprint.id

    def delete_blueprint(self, blueprint: str, project: str = None) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        blueprint_id = self.get_blueprint_id(blueprint, project_id)
        result = self.client.delete(f"blueprints/{project_id}/{blueprint_id}")
        return result

    def get_blueprint(self, blueprint: str, project: str) -> Blueprint:
        project_id = self.get_project_id(self.organisation_id, project)
        blueprint_id = self.get_blueprint_id(blueprint, project_id)
        result = self.client.get(f"blueprints/{project_id}/{blueprint_id}")
        blueprint = Blueprint(**result.data)
        return blueprint

    def get_blueprints(self, project: str) -> Blueprint:
        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"blueprints/{project_id}")
        blueprints = [Blueprint(**blueprint) for blueprint in result.data]
        return blueprints

    def update_blueprint(self, blueprint: str, project: str) -> Blueprint:
        project_id = self.get_project_id(self.organisation_id, project)
        blueprint_id = self.get_blueprint_id(blueprint, project_id)
        self.client.post(f"blueprints/{project_id}/{blueprint_id}/update")

    def import_blueprint(self,
                         name: str,
                         repository: str,
                         repository_path: str,
                         repository_server: str,
                         repository_key: str,
                         project: str) -> uuid_pkg.UUID:
        project_id = self.get_project_id(self.organisation_id, project)
        blueprint = BlueprintBase(
            repository=repository,
            repository_path=repository_path,
            repository_server=repository_server,
            name=name
        )
        data = blueprint.dict()
        if repository_key:
            data["repository_key"] = repository_key
        result = self.client.post(f"blueprints/{project_id}", data=data)
        blueprint = Blueprint(**result.data)
        return blueprint

    # deployments

    def create_deployment(self, name: str, template: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        template_id = self.get_template_id(template)
        deployment = DeploymentBase(
            name=name,
            template_id=str(template_id)
        )
        result = self.client.post(f"deployments/{project_id}", data=deployment.dict())
        deployment = Deployment(**result.data)
        return deployment

    def destroy_deployment(self, name: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(name)
        result = self.client.post(f"deployments/{project_id}/{deployment_id}/destroy")
        return result

    def reconcile_deployment(self, name: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(name)
        result = self.client.post(f"deployments/{project_id}/{deployment_id}/reconcile")
        return result

    def get_deployment_id(self, deployment: str, project: str = None) -> uuid_pkg.UUID:
        if is_valid_uuid(deployment):
            return deployment

        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"deployments/{project_id}", ep_params={"q": deployment})
        deployment = Deployment(**result.data[0])
        return deployment.id

    def delete_deployment(self, deployment: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(deployment, project_id)
        result = self.client.delete(f"deployments/{project_id}/{deployment_id}")
        return result

    def get_deployment(self, deployment: str, project: str) -> Deployment:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(deployment, project_id)
        result = self.client.get(f"deployments/{project_id}/{deployment_id}")
        deployment = Deployment(**result.data)
        return deployment

    def get_deployments(self, project: str) -> List[Deployment]:
        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"deployments/{project_id}")
        deployments = [Deployment(**deployment) for deployment in result.data]
        return deployments

    def get_deployment_outputs(self, deployment: str, output: str, project: str) -> Dict:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(deployment, project_id)
        result = self.client.get(f"deployments/{project_id}/{deployment_id}/outputs")
        return result.data

    def get_deployment_log(self, deployment: str, log_id: uuid_pkg.UUID, project: str) -> LogWithValue:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(deployment, project_id)
        result = self.client.get(f"logs/{project_id}/{deployment_id}/{log_id}")
        log = LogWithValue(**result.data)
        return log

    def get_deployment_logs(self, deployment: str, project: str, log_filter: str = None) -> List[Log]:
        project_id = self.get_project_id(self.organisation_id, project)
        deployment_id = self.get_deployment_id(deployment, project_id)
        result = self.client.get(f"logs/{project_id}/{deployment_id}", ep_params={"q": log_filter})
        logs = [Log(**log) for log in result.data]
        return logs

    # environments

    def get_environment_id(self, environment: str, project: str = None) -> uuid_pkg.UUID:
        if is_valid_uuid(environment):
            return environment

        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"environments/{project_id}", ep_params={"q": environment})
        environment = Environment(**result.data[0])
        return environment.id

    def delete_environment(self, environment: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        environment_id = self.get_environment_id(environment, project_id)
        result = self.client.delete(f"environments/{project_id}/{environment_id}")
        return result

    def get_environment(self, environment: str, project: str) -> Environment:
        project_id = self.get_project_id(self.organisation_id, project)
        environment_id = self.get_environment_id(environment, project_id)
        result = self.client.get(f"environments/{project_id}/{environment_id}")
        environment = Environment(**result.data)
        return environment

    def get_environments(self, project: str) -> Environment:
        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"environments/{project_id}")
        environments = [Environment(**environment) for environment in result.data]
        return environments

    def update_environment(self, environment: str, project: str) -> Blueprint:
        project_id = self.get_project_id(self.organisation_id, project)
        environment_id = self.get_environment_id(environment, project_id)
        self.client.post(f"environments/{project_id}/{environment_id}/update")

    def import_environment(self,
                           name: str,
                           repository: str,
                           repository_path: str,
                           repository_server: str,
                           repository_key: str,
                           project: str) -> uuid_pkg.UUID:
        project_id = self.get_project_id(self.organisation_id, project)
        environment = EnvironmentBase(
            repository=repository,
            repository_path=repository_path,
            repository_server=repository_server,
            name=name
        )
        data = environment.dict()
        if repository_key:
            data["repository_key"] = repository_key
        result = self.client.post(f"environments/{project_id}", data=data)
        environment = Environment(**result.data)
        return environment

    # templates

    def get_template_id(self, template: str, project: str = None) -> uuid_pkg.UUID:
        if is_valid_uuid(template):
            return template

        project_id = self.get_project_id(self.organisation_id, project)

        result = self.client.get(f"templates/{project_id}", ep_params={"q": template})
        template = Template(**result.data[0])
        return template.id

    def delete_template(self, template: str, project: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        template_id = self.get_template_id(template, project_id)
        result = self.client.delete(f"templates/{project_id}/{template_id}")
        return result

    def get_template(self, template: str, project: str) -> TemplateWithInputs:
        project_id = self.get_project_id(self.organisation_id, project)
        template_id = self.get_template_id(template, project_id)
        result = self.client.get(f"templates/{project_id}/{template_id}")
        template = TemplateWithInputs(**result.data)
        return template

    def get_templates(self, project: str) -> Template:
        project_id = self.get_project_id(self.organisation_id, project)
        result = self.client.get(f"templates/{project_id}")
        templates = [Template(**template) for template in result.data]
        return templates

    def import_template(self, path: str, name: str, project: str) -> Template:
        project_id = self.get_project_id(self.organisation_id, project)

        logger.debug(f"Validating template {path}")
        try:
            with open(path) as fp:
                validate_content(fp.read(), "template")
        except Exception as e:
            raise TimonException(f"Template {path} is not valid:\n{e}")

        with open(path) as fp:
            data = yaml.safe_load(fp)

        if name not in data:
            raise TimonException(f"Template {name} not found in {path}")

        template_data = data[name]

        if "environment_version" in template_data:
            environment_version = template_data["environment_version"]
        else:
            environment_version = None

        if "environment" in template_data:
            if type(template_data["environment"]) == dict:
                try:
                    environment_data = template_data["environment"]
                    environment_id = self.get_environment_id(environment_data["name"])
                except TimonApiException:
                    repository_key = None
                    if "repository_key" in environment_data:
                        repository_key = environment_data["repository_key"]
                        if type(repository_key) == dict:
                            if repository_key["type"] == "file":
                                with open(v["path"]) as fp:
                                    repository_key = fp.read()
                    environment = self.import_environment(
                        environment_data["name"],
                        environment_data["repository"],
                        "environments",
                        environment_data["repository_server"],
                        repository_key,
                        project=project_id
                    )
                    environment_id = environment.id
            else:
                environment_id = self.get_environment_id(template_data["environment"])
        else:
            environment_id = None

        if "blueprint_version" in template_data:
            blueprint_version = template_data["blueprint_version"]
        else:
            blueprint_version = None

        if "blueprint" in template_data:
            if type(template_data["blueprint"]) == dict:
                try:
                    blueprint_data = template_data["blueprint"]
                    blueprint_id = self.get_blueprint_id(blueprint_data["name"])
                except TimonApiException:
                    repository_key = None
                    if "repository_key" in blueprint_data:
                        repository_key = blueprint_data["repository_key"]
                        if type(repository_key) == dict:
                            if repository_key["type"] == "file":
                                with open(v["path"]) as fp:
                                    repository_key = fp.read()
                    blueprint = self.import_blueprint(
                        blueprint_data["name"],
                        blueprint_data["repository"],
                        "blueprints",
                        blueprint_data["repository_server"],
                        repository_key,
                        project=project_id
                    )
                    blueprint_id = blueprint.id
            else:
                blueprint_id = self.get_blueprint_id(template_data["blueprint"])
        else:
            blueprint_id = None

        if "inputs" in template_data:
            inputs = template_data["inputs"]
        else:
            inputs = {}

        # prepare inputs
        for k, v in inputs.items():
            if type(v) == dict:
                if v["type"] == "file":
                    with open(v["path"]) as fp:
                        v = fp.read()
                        inputs[k] = v
        template = TemplateWithInputsBase(
            blueprint_id=str(blueprint_id),
            blueprint_version=blueprint_version,
            environment_id=str(environment_id),
            environment_version=environment_version,
            inputs=yaml.dump(inputs),
            name=name
        )
        result = self.client.post(f"templates/{project_id}", data=template.dict())
        template = Template(**result.data)
        return template

    # projects

    def get_project_id(self, organisation_id, project: str = None) -> uuid_pkg.UUID:
        if not project:
            return self.project_id

        if is_valid_uuid(project):
            return project

        result = self.client.get(f"projects/{organisation_id}", ep_params={"q": project})
        project = Project(**result.data[0])
        return project.id

    def create_project(self, project: str, organisation: str) -> Project:
        organisation_id = self.get_organisation_id(organisation)
        project_data = {
            "name": project
        }
        result = self.client.post(f"projects/{organisation_id}", data=project_data)
        project = Project(**result.data)
        return project

    def delete_project(self, project: str, organisation: str) -> Result:
        project_id = self.get_project_id(self.organisation_id, project)
        organisation_id = self.get_organisation_id(organisation)
        result = self.client.delete(f"projects/{organisation_id}/{project_id}")
        return result

    def get_project(self, project: str, organisation: str) -> Project:
        project_id = self.get_project_id(self.organisation_id, project)
        organisation_id = self.get_organisation_id(organisation)
        result = self.client.get(f"projects/{organisation_id}/{project_id}")
        project = Project(**result.data)
        return project

    def get_projects(self, organisation: str) -> List[Project]:
        organisation_id = self.get_organisation_id(organisation)
        result = self.client.get(f"projects/{organisation_id}")
        projects = [Project(**project) for project in result.data]
        return projects

    # other

    def get_organisation_id(self, organisation: str = None) -> uuid_pkg.UUID:
        if not organisation:
            return self.organisation_id

        if is_valid_uuid(organisation):
            return organisation

        result = self.client.get("organisations", ep_params={"q": organisation})
        organisation = Organisation(**result.data[0])
        return organisation.id


def get_client(profile: DynaBox) -> Timon:
    return Timon(profile)


def get_http_client(profile: DynaBox) -> Client:
    return Client(profile)
