from __future__ import annotations

import json
import logging
import time
from datetime import timezone
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from urllib.parse import urljoin

import requests
import socketio
from dateutil import parser
from dateutil.tz import tzlocal
from packaging import version
from pydantic import parse_obj_as

from servicefoundry.internal.util import request_handling, upload_packaged_code
from servicefoundry.io.output_callback import OutputCallBack
from servicefoundry.lib.config_utils import _get_profile
from servicefoundry.lib.const import DEFAULT_PROFILE_NAME, REFRESH_ACCESS_TOKEN_IN_SEC
from servicefoundry.lib.exceptions import ConfigurationException
from servicefoundry.lib.model.session import ServiceFoundrySession
from servicefoundry.lib.session_factory import get_session
from servicefoundry.v2.lib.models import (
    AppDeploymentStatusResponse,
    BuildResponse,
    Deployment,
    DeploymentFqnResponse,
)
from servicefoundry.version import __version__

DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE = "DEPLOYMENT_LOGS"
BUILD_LOGS_SUBSCRIBE_MESSAGE = "logs"

if TYPE_CHECKING:
    from servicefoundry.auto_gen.models import Application

logger = logging.getLogger(__name__)

VERSION_PREFIX = "v1"


def _get_or_throw(definition, key, error_message):
    if key not in definition:
        raise ConfigurationException(error_message)
    return definition[key]


class ServiceFoundryServiceClient:
    def __init__(
        self,
        session: Optional[ServiceFoundrySession],
    ):
        self.session = session
        self.host = None
        if self.session:
            self.host = self.session.profile.server_config.api_server

    @classmethod
    def get_client(
        cls, auth_required: bool = True, profile_name: str = DEFAULT_PROFILE_NAME
    ) -> "ServiceFoundryServiceClient":
        # Would be ok to prefer auth token from API instead of local session file
        if auth_required:
            session = get_session(profile_name=profile_name)
            instance = cls(session=session)
        else:
            # TODO (chiragjn): All usages should be made to handle session=None
            instance = cls(session=None)
            # Try to get this inside __init__, maybe profile shouldn't live inside session?
            instance.host = _get_profile(
                name=DEFAULT_PROFILE_NAME
            ).server_config.api_server

        if __version__ != "0.0.0":
            # "0.0.0" indicates dev version
            min_cli_version = cls._get_min_cli_version_requirement(instance.host)
            if version.parse(__version__) < version.parse(min_cli_version):
                raise Exception(
                    "You are using an outdated version of `servicefoundry`.\n"
                    f"Execute `pip install servicefoundry>={min_cli_version}` to install the supported version.",
                )
        else:
            logger.debug("Ignoring minimum cli version check")
        return instance

    @staticmethod
    @lru_cache(maxsize=3)
    def _get_min_cli_version_requirement(host: str) -> str:
        url = f"{host}/v1/min-cli-version"
        res = requests.get(url)
        res = request_handling(res)
        return res["minVersion"]

    def check_and_refresh_session(self):
        decoded = self.session.decode()
        expiry_second = decoded["exp"]
        if expiry_second - time.time() < REFRESH_ACCESS_TOKEN_IN_SEC:
            logger.info(
                f"Going to refresh the access token {expiry_second - time.time()}."
            )
            self.session.refresh_access_token()

    def _get_header(self):
        return {"Authorization": f"Bearer {self.session.access_token}"}

    def list_workspace(self):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_workspace(self, cluster_id, name):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.post(
            url,
            json={"name": name, "clusterId": cluster_id},
            headers=self._get_header(),
        )
        return request_handling(res)

    def remove_workspace(self, workspace_id, force=False):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace/{workspace_id}"
        force = json.dumps(
            force
        )  # this dumb conversion is required because `params` just casts as str
        res = requests.delete(url, headers=self._get_header(), params={"force": force})
        return request_handling(res)

    def get_workspace_by_name(self, workspace_name, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(
            url,
            headers=self._get_header(),
            params={"name": workspace_name, "clusterId": cluster_id},
        )
        return request_handling(res)

    def get_workspace(self, workspace_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace/{workspace_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_workspace_by_fqn(self, workspace_fqn: str) -> List[Dict[str, Any]]:
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(
            url,
            headers=self._get_header(),
            params={"fqn": workspace_fqn},
        )
        return request_handling(res)

    def list_deployments(self, workspace_id: str = None):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/deployment"
        params = {}
        if workspace_id:
            params["workspaceId"] = workspace_id
        res = requests.get(url=url, params=params, headers=self._get_header())
        return request_handling(res)

    def create_cluster(
        self, name, region, aws_account_id, cluster_name, ca_data, server_url
    ):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster"
        res = requests.post(
            url,
            json={
                "id": name,
                "region": region,
                "authData": {
                    "awsAccountID": aws_account_id,
                    "clusterName": cluster_name,
                    "caData": ca_data,
                    "serverUrl": server_url,
                },
            },
            headers=self._get_header(),
        )
        return request_handling(res)

    def list_cluster(self):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_cluster(self, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster/{cluster_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def remove_cluster(self, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster/{cluster_id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_presigned_url(self, space_name, service_name, env):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/deployment/code-upload-url"
        res = requests.post(
            url,
            json={
                "workspaceFqn": space_name,
                "serviceName": service_name,
                "stage": env,
            },
            headers=self._get_header(),
        )
        return request_handling(res)

    def upload_code_package(
        self, workspace_fqn: str, component_name: str, package_local_path: str
    ) -> str:
        http_response = self.get_presigned_url(
            space_name=workspace_fqn, service_name=component_name, env="default"
        )
        upload_packaged_code(metadata=http_response, package_file=package_local_path)

        return http_response["uri"]

    def deploy_application(
        self, workspace_id: str, application: Application
    ) -> Deployment:
        data = {
            "workspaceId": workspace_id,
            "name": application.name,
            "manifest": application.dict(exclude_none=True),
        }
        url = f"{self.host}/{VERSION_PREFIX}/deployment"
        deploy_response = requests.post(url, json=data, headers=self._get_header())
        response = request_handling(deploy_response)
        return Deployment.parse_obj(response["deployment"])

    def create_secret_group(self, name):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/secret-group/"
        res = requests.post(url, headers=self._get_header(), json={"name": name})
        return request_handling(res)

    def delete_secret_group(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_secret_group(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/{id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_secret(self, secret_group_id, key, value):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/"
        res = requests.post(
            url,
            headers=self._get_header(),
            json={"secretGroupId": secret_group_id, "key": key, "value": value},
        )
        return request_handling(res)

    def delete_secret(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_secret(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/{id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_secrets_in_group(self, secret_group_id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/list-by-secret-group/{secret_group_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_secret_groups(self):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/findAll"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def _get_log_print_line(self, log: dict):
        time_str = log["time"]
        time_obj = parser.parse(time_str)
        if not time_obj.tzinfo:
            time_obj = time_obj.replace(tzinfo=timezone.utc)
        local_time = time_obj.astimezone(tzlocal())
        local_time_str = local_time.isoformat()
        return f'[{local_time_str}] {log["log"].strip()}'

    def _tail_logs(
        self,
        tail_logs_url: str,
        query_dict: dict,
        # NOTE: Rather making this printer callback an argument,
        # we should have global printer callback
        # which will be initialized based on the running env (cli, lib, notebook)
        subscribe_message: str,
        socketio_path: str = "socket.io",
        callback=OutputCallBack(),
        wait=False,
    ):
        self.check_and_refresh_session()
        sio = socketio.Client(request_timeout=60)
        callback.print_line("Waiting for the task to start...")

        @sio.on(subscribe_message)
        def logs(data):
            try:
                _log = json.loads(data)
                callback.print_line(self._get_log_print_line(_log["body"]))
            except Exception:
                pass

        sio.connect(
            tail_logs_url,
            transports="websocket",
            headers=self._get_header(),
            socketio_path=socketio_path,
        )

        # TODO: We should have have a timeout here. `emit` does
        # not support timeout. Explore `sio.call`.

        sio.emit(
            subscribe_message,
            json.dumps(query_dict),
        )
        if wait:
            sio.wait()

    def poll_deployment_statuses(
        self, application_id: str, deployment_id: str, poll_after_secs: int = 5
    ) -> List[AppDeploymentStatusResponse]:
        while True:
            self.check_and_refresh_session()
            url = f"{self.host}/{VERSION_PREFIX}/app/{application_id}/deployments/{deployment_id}/statuses"
            res = requests.get(url, headers=self._get_header())
            res = request_handling(res)
            yield parse_obj_as(List[AppDeploymentStatusResponse], res)
            time.sleep(poll_after_secs)

    def get_deployment_build_response(
        self, application_id: str, deployment_id: str
    ) -> List[BuildResponse]:
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/app/{application_id}/deployments/{deployment_id}/builds"
        res = requests.get(url, headers=self._get_header())
        res = request_handling(res)
        return parse_obj_as(List[BuildResponse], res)

    def tail_build_logs(
        self, build_response: BuildResponse, callback=OutputCallBack(), wait=False
    ):
        tail_logs_obj = json.loads(build_response.tailLogsUrl)
        self._tail_logs(
            tail_logs_url=tail_logs_obj["uri"],
            socketio_path=tail_logs_obj["path"],
            query_dict={
                "pipelineRunName": build_response.name,
                "startTs": build_response.logsStartTs,
            },
            callback=callback,
            wait=wait,
            subscribe_message=BUILD_LOGS_SUBSCRIBE_MESSAGE,
        )

    def tail_logs_for_deployment(
        self,
        workspace_id: str,
        application_id: str,
        deployment_id: str,
        start_ts: int,
        limit: int,
        callback=OutputCallBack(),
        wait=True,
    ):
        self._tail_logs(
            tail_logs_url=urljoin(
                self.host, f"/?type={DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE}"
            ),
            query_dict={
                "workspaceId": workspace_id,
                "startTs": start_ts,
                "limit": limit,
                "getLogsQuery": {
                    "applicationId": application_id,
                    "deploymentId": deployment_id,
                },
            },
            callback=callback,
            wait=wait,
            subscribe_message=DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE,
        )

    def fetch_deployment_logs(
        self,
        workspace_id: str,
        application_id: str,
        deployment_id: str,
        end_ts: Optional[int],
        limit: Optional[int],
        start_ts: Optional[int],
        callback=OutputCallBack(),
    ):
        data = {
            "getLogsQuery": {
                "applicationId": application_id,
                "deploymentId": deployment_id,
            }
        }
        if start_ts:
            data["startTs"] = start_ts
        if end_ts:
            data["endTs"] = end_ts
        if limit:
            data["limit"] = limit

        url = f"{self.host}/{VERSION_PREFIX}/logs/{workspace_id}"
        self.check_and_refresh_session()
        res = requests.post(url=url, json=data, headers=self._get_header())
        logs_list = request_handling(res)
        for log in logs_list["logs"]:
            callback.print_line(self._get_log_print_line(log))

    def get_authorization_for_resource(self, resource_type, resource_id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize/{resource_type}/{resource_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_authorization(self, resource_id, resource_type, user_id, role):
        # @TODO instead of user_id pass emailID. Need to be done once API is available on auth.
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize"
        res = requests.post(
            url,
            headers=self._get_header(),
            json={
                "resourceId": resource_id,
                "resourceType": resource_type,
                "userName": user_id,
                "userType": "USER",
                "role": role,
            },
        )
        return request_handling(res)

    def delete_authorization(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def update_authorization(self, id, role):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize"
        res = requests.patch(
            url, headers=self._get_header(), json={"id": id, "role": role}
        )
        return request_handling(res)

    @staticmethod
    def get_tenant_info(api_server_host: str, tenant_hostname: str):
        res = requests.get(
            url=f"{api_server_host}/{VERSION_PREFIX}/tenant-id",
            params={"hostName": tenant_hostname},
        )
        return request_handling(res)

    def get_deployment_info_by_fqn(self, deployment_fqn: str) -> DeploymentFqnResponse:
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/fqn/deployment"
        res = requests.get(
            url, headers=self._get_header(), params={"fqn": deployment_fqn}
        )
        res = request_handling(res)
        return DeploymentFqnResponse(**res)
