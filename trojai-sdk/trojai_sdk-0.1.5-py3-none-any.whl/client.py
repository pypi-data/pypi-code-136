import requests
from typing import Optional, List
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests import Session

from trojsdk.config.auth import TrojAuthConfig
from trojsdk.config.base import BaseTrojConfig

retry_strategy = Retry(
    total=2,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "PUT", "POST", "DELETE", "OPTIONS", "TRACE"],
)

retry_adapter = HTTPAdapter(max_retries=retry_strategy)
requests_retry = Session()
requests_retry.mount("https://", retry_adapter)
requests_retry.mount("http://", retry_adapter)

"""
Troj Client class handls all requests made to a passed endpoint
"""


class TrojClient:

    api_endpoint: str = None
    refresh_url: str = "https://troj.auth.ca-central-1.amazoncognito.com/oauth2/token"

    _auth_config: TrojAuthConfig = None

    _creds_id_token: str = None
    _creds_refresh_token: str = None
    _creds_api_key: str = None
    _secrets: dict = None

    def __init__(
        self,
        *,
        api_endpoint: str = "http://localhost:8080/api/v1",
        auth_config: TrojAuthConfig = None,
        **kwargs,
    ):
        if auth_config is not None:
            self.api_endpoint = auth_config.api_endpoint

            self._auth_config = auth_config

            self._creds_id_token = auth_config.auth_keys.id_token
            self._creds_refresh_token = auth_config.auth_keys.refresh_token
            self._creds_api_key = auth_config.auth_keys.api_key
            self._secrets = auth_config.secrets
        else:
            self.api_endpoint = api_endpoint

        requests_retry.hooks["response"].append(
            self.reauth
        )  # https://github.com/psf/requests/issues/4747 - Important for Retry vs urllib3

    def _get_creds_headers(self):
        """
        Get appropriate request headers for the currently set credentials.

        Raises:
            Exception: No credentials set.
        """
        if self._creds_id_token:
            return {
                "Authorization": f"Bearer {self._creds_id_token}",
                "x-api-key": f"{self._creds_api_key}",
            }
        else:
            raise Exception("No credentials set.")

    def set_credentials(
        self,
        *,
        id_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        api_key: Optional[str] = None,
        auth_config: Optional[TrojAuthConfig] = None,
    ):
        """
        Set credentials for the client.

        :param id_token (str, optional): Used by the client to authenticate the user.
        :param refresh_token (str, optional): Used to refresh the ID Token.
        :param api_key (str, optional): Used to gain access to API.

        Raises:
            Exception: Invalid credential combination provided.
        """

        # TODO: Change to require id_token and api_key together
        if id_token is not None:
            self._creds_id_token = id_token

        if refresh_token is not None:
            self._creds_refresh_token = refresh_token

        if api_key is not None:
            self._creds_api_key = api_key

        if auth_config is not None:
            self._auth_config = auth_config

    """
    This function is not called in all the pytest tests
    """

    def reauth(self, res, *args, **kwargs):
        """Hook to re-authenticate whenever authentication expires."""
        if res.status_code == requests.codes.forbidden:
            if res.request.headers.get("REATTEMPT"):
                res.raise_for_status()
            self.refresh_tokens()
            req = res.request
            req.headers["REATTEMPT"] = 1
            req = self.auth_inside_hook(req)
            res = requests_retry.send(req)
            return res

    """
    This function is not called in all the pytest tests
    """

    def auth_inside_hook(self, req):
        """Set the authentication token for the premade request during reauth attempts inside the retry hook."""
        req.headers["Authorization"] = f"Bearer {self._creds_id_token}"
        return req

    def refresh_tokens(self):
        payload = f"grant_type=refresh_token&client_id={self.cognito_client_id}&refresh_token={self._creds_refresh_token}"
        requests.utils.quote(payload)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.request(
            "POST", self.refresh_url, headers=headers, data=payload
        )
        self._creds_id_token = json.loads(response.text)["id_token"]

        return response

    def get_jobs(self):
        r = requests_retry.get(
            f"{self.api_endpoint}/jobs",
        )

    def post_job(
        self,
        config: BaseTrojConfig,
        docker_metadata: dict = None,
        use_auth_from_config: bool = False,
        use_api_endpoint_from_auth_config: bool = False,
    ):
        """
        When using different sources of authentication and api endpoints, keep in mind that the client's auth_config will remain the unchanged.
        Use client.set_credentials() to change auth_config context.

        :param config: Uses BaseTrojConfig (NLPTrojConfig, TabularTrojConfig, or VisionTrojConfig)
            The main configuration for the project.

        :param docker_metadata: A dictionary with the following two values;
            "docker_image_url": A Docker Hub image id for any engine type.
                Ex. value: "trojai/troj-engine-base-tabular:tabluar-shawn-latest"
            "docker_secret_name": The name of the environment secret containing the credentials for Docker Hub access. This is defined in the TrojAI helm repo in the _setup.sh_ script.

        :param use_auth_config_from_config: Use the api keys from the config's authentication values, and not from the client object.

        :param use_api_endpoint_from_auth_config: Use the endpoint from the config's auth value, and not from the client object.

        :return dict: Contains job_name under key "data", under key "job_name". (Dict within dict)
        """

        # Keep the project name and dataset name from the config, but set auth keys from client's TrojAuthConfig
        if not use_auth_from_config:
            proj_name = config.auth_config.project_name
            dset_name = config.auth_config.dataset_name

            config.auth_config = self._auth_config

            config.auth_config.project_name = proj_name
            config.auth_config.dataset_name = dset_name

        if use_api_endpoint_from_auth_config:
            api_endpoint = config.auth_config.api_endpoint
        else:
            api_endpoint = self.api_endpoint
            config.auth_config.api_endpoint = self.api_endpoint

        config = config.to_dict()

        if not docker_metadata:
            docker_metadata = {"docker_secret_name": "trojaicreds"}
            try:
                docker_choices_dict = {
                    "tabular": "trojai/troj-engine-base-tabular:tabluar-predev-latest",
                    "nlp": "trojai/troj-engine-base-nlp:nlp-predev-latest",
                    "vision": "trojai/troj-engine-base-cv:cv-predev-latest",
                }
                docker_metadata["docker_image_url"] = docker_choices_dict[
                    str(config.get("task_type")).lower()
                ]
            except Exception as e:
                raise Exception(
                    "Model type "
                    + str(config.get("task_type", "none"))
                    + " not found. Please select one of "
                    + str(list(docker_choices_dict))
                ) from e

        data = {"job_config": {"body": config}, "docker_metadata": docker_metadata}

        r = requests_retry.post(
            f"{api_endpoint}/jobs", headers=self._get_creds_headers(), json=data
        )
        self.raise_resp_exception_error(r)

        print("POST /jobs response:", r.json())

        return {"status_code": r.status_code, "data": r.json()}

    def get_job_status(self, job_id: str):
        """
        The job_id can be retrieved from the return value of client.post_job(), or from client.get_jobs().
        Set the client's auth with client.set_credentials() to provide context.
        """
        r = requests_retry.get(
            f"{self.api_endpoint}/jobs/{job_id}",
            headers=self._get_creds_headers(),
        )

        print("GET /jobs/job_id response:", r.json())
        self.raise_resp_exception_error(r)

        return {"status_code": r.status_code, "data": r.json()}

    def raise_resp_exception_error(self, resp):
        if not resp.ok:
            message = None
            try:
                r_body = resp.json()
                message = r_body.get("message") or r_body.get("msg")
            except:
                # If we failed for whatever reason (parsing body, etc.)
                # Just return the code
                if resp.status_code == 500:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)}"
                    )
                else:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)} | {resp.json()['detail']}"
                    )
            if message:
                raise Exception(f"Error: {message}")
            else:
                if resp.status_code == 500:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)}"
                    )
                else:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)} | {resp.json()['detail']}"
                    )
