from __future__ import absolute_import

import aia
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

import json
import os
import yaml
import logging
import requests
from typing import List, Dict


class AoaClient(object):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)

        self.project_id = kwargs.get("project_id")
        self.ssl_verify = True
        self.aoa_url = None
        self.auth_mode = "oauth"
        self.__auth_user = None
        self.__auth_pass = None
        self.__credentials = None

        self.__client_id = None
        self.__client_secret = None
        self.__token_url = None
        self.__refresh_token = None

        self.__parse_aoa_config(**kwargs)

        if self.auth_mode == "oauth":
            self.__create_oauth_session_refresh_token()

        elif self.auth_mode == "oauth-cc":
            self.__create_oauth_session_client_credentials()

    def __parse_yaml(self, yaml_path: str):
        with open(yaml_path, "r") as handle:
            conf = yaml.safe_load(handle)
        self.__parse_kwargs(**conf)

    def __parse_kwargs(self, **kwargs):
        self.aoa_url = kwargs.get("aoa_url", self.aoa_url)
        self.ssl_verify = kwargs.get("ssl_verify", self.ssl_verify)
        self.auth_mode = kwargs.get("auth_mode", self.auth_mode)

        if self.auth_mode == "oauth":
            self.__client_id = kwargs.get("auth_client_id", self.__client_id)
            self.__client_secret = kwargs.get("auth_client_secret", self.__client_secret)
            self.__token_url = kwargs.get("auth_client_token_url", self.__token_url)
            self.__refresh_token = kwargs.get("auth_client_refresh_token", self.__refresh_token)

        elif self.auth_mode == "oauth-cc":
            self.__client_id = kwargs.get("auth_client_id", self.__client_id)
            self.__client_secret = kwargs.get("auth_client_secret", self.__client_secret)
            self.__token_url = kwargs.get("auth_client_token_url", self.__token_url)

        else:
            raise Exception(f"Auth mode: {self.auth_mode} not supported.")

        if "verify_connection" in kwargs:
            self.verify_aoa_connection = kwargs["verify_connection"]

    def __parse_env_variables(self):
        self.aoa_url = os.environ.get("AOA_URL", self.aoa_url)
        self.ssl_verify = os.environ.get("AOA_SSL_VERIFY", str(self.ssl_verify)).lower() == "true"
        self.auth_mode = os.environ.get("AOA_API_AUTH_MODE", self.auth_mode)

        if self.auth_mode == "oauth":
            self.__client_id = os.environ.get("AOA_API_AUTH_CLIENT_ID", self.__client_id)
            self.__client_secret = os.environ.get("AOA_API_AUTH_CLIENT_SECRET", self.__client_secret)
            self.__token_url = os.environ.get("AOA_API_AUTH_TOKEN_URL", self.__token_url)
            self.__refresh_token = os.environ.get("AOA_API_AUTH_REFRESH_TOKEN",
                                                  self.__refresh_token)

        elif self.auth_mode == "oauth-cc":
            self.__client_id = os.environ.get("AOA_API_AUTH_CLIENT_ID", self.__client_id)
            self.__client_secret = os.environ.get("AOA_API_AUTH_CLIENT_SECRET", self.__client_secret)
            self.__token_url = os.environ.get("AOA_API_AUTH_TOKEN_URL", self.__token_url)

        else:
            raise Exception(f"Auth mode: {self.auth_mode} not supported.")

    def __parse_aoa_config(self, **kwargs):
        if "config_file" in kwargs:
            self.__parse_yaml(kwargs['config_file'])
        else:
            from pathlib import Path
            config_file = "{}/.aoa/config.yaml".format(Path.home())
            if os.path.isfile(config_file):
                self.__parse_yaml(config_file)

        self.__parse_env_variables()
        self.__parse_kwargs(**kwargs)

    def __validate_url(self):
        if not self.aoa_url:
            raise ValueError("ModelOps endpoint not configured. "
                             "Try (re)copy the CLI configuration from ModelOps UI -> Session Details -> CLI Config.")

    def set_project_id(self, project_id: str):
        """
        set project id

        Parameters:
           project_id (str): project id(uuid)
        """
        self.project_id = project_id

    def get_current_project(self):
        """
        get project id

        Return:
           project_id (str): project id(uuid)
        """
        return self.project_id

    def select_header_accept(self, accepts: List[str]):
        """
        converts list of header into a string

        Return:
            (str): request header
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]
        return ', '.join(accepts)

    def get_request(self, path, header_params: Dict[str, str], query_params: Dict[str, str]):
        """
        wrapper for get request

        Parameters:
           path (str): url
           header_params (dict): header parameters
           query_params (dict): query parameters

        Returns:
            dict for resources, str for errors, None for 404
        Raise:
            raises HTTPError in case of error status code other than 404
        """

        self.__validate_url()

        resp = self.session.get(
            url=self.__strip_url(self.aoa_url) + path,
            headers=header_params,
            params=query_params
        )

        if resp.status_code == 404:
            return None

        return self.__validate_and_extract_body(resp)

    def post_request(self, path, header_params: Dict[str, str], query_params: Dict[str, str], body: Dict[str, str]):
        """
        wrapper for post request

        Parameters:
           path (str): url
           header_params (dict): header parameters
           query_params (dict): query parameters
           body (dict): request body

        Returns:
            dict for resources, str for errors
        Raise:
            raises HTTPError in case of error status code
        """

        self.__validate_url()

        resp = self.session.post(
            url=self.__strip_url(self.aoa_url) + path,
            headers=header_params,
            params=query_params,
            data=json.dumps(body)
        )

        return self.__validate_and_extract_body(resp)

    def put_request(self, path, header_params: Dict[str, str], query_params: Dict[str, str], body: Dict[str, str]):
        """
        wrapper for put request

        Parameters:
           path (str): url
           header_params (dict): header parameters
           query_params (dict): query parameters
           body (dict): request body

        Returns:
            dict for resources, str for errors
        Raise:
            raises HTTPError in case of error status code
        """

        self.__validate_url()

        resp = self.session.put(
            url=self.__strip_url(self.aoa_url) + path,
            headers=header_params,
            params=query_params,
            data=json.dumps(body)
        )

        return self.__validate_and_extract_body(resp)

    def delete_request(self, path, header_params: Dict[str, str], query_params: Dict[str, str], body: Dict[str, str]):
        """
        wrapper for delete request
        Parameters:
           path (str): url
           header_params (dict): header parameters
           query_params (dict): query parameters
           body (dict): request body
        Returns:
            dict for resources, str for errors
        Raise:
            raises HTTPError in case of error status code
        """

        self.__validate_url()

        resp = self.session.delete(
            url=self.__strip_url(self.aoa_url) + path,
            headers=header_params,
            params=query_params,
            data=json.dumps(body)
        )

        return self.__validate_and_extract_body(resp)

    def __validate_and_extract_body(self, resp):
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if resp.text:
                raise requests.exceptions.HTTPError(f"Error Message: {resp.text}")
            else:
                raise err

        try:
            return resp.json()
        except ValueError:
            return resp.text

    def __strip_url(self, url):
        return url.rstrip('/')

    def __create_oauth_session_refresh_token(self):
        self.logger.debug("Configuring oauth with refresh token")

        if self.__client_id is None or self.__client_secret is None or self.__token_url is None or self.__refresh_token is None:
            raise Exception("Missing CLI configuration.\n" +
                            "Please (re)copy the CLI configuration from " +
                            "ModelOps UI -> Session Details -> CLI Config\n")

        self.session = OAuth2Session(client_id=self.__client_id)
        self.__set_session_tls()
        self.session.refresh_token(token_url=self.__token_url,
                                   refresh_token=self.__refresh_token,
                                   auth=HTTPBasicAuth(self.__client_id, self.__client_secret))

    def __create_oauth_session_client_credentials(self):
        self.logger.debug("Configuring oauth with client credentials grant")

        if self.__client_id is None or self.__client_secret is None or self.__token_url is None:
            raise Exception("AOA_API_AUTH_CLIENT_ID, AOA_API_AUTH_CLIENT_SECRET, "
                            "AOA_API_AUTH_TOKEN_URL must be defined "
                            "with AOA_API_AUTH_MODE of 'oauth-cc (client-credentials)'")

        from requests_oauthlib import OAuth2Session
        from requests.auth import HTTPBasicAuth
        from oauthlib.oauth2 import BackendApplicationClient

        self.session = OAuth2Session(client=BackendApplicationClient(client_id=self.__client_id))
        self.__set_session_tls()
        self.session.fetch_token(token_url=self.__token_url,
                                 auth=HTTPBasicAuth(self.__client_id, self.__client_secret))

    def __set_session_tls(self):
        self.session.verify = self.ssl_verify
        if self.ssl_verify:
            self.__chase_tls_cert_chain()
        else:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning

            self.logger.warning("Certificate validation disabled. Adding certificate verification is strongly advised")
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def __chase_tls_cert_chain(self):
        if self.aoa_url.startswith("https") and not (
                "REQUESTS_CA_BUNDLE" in os.environ or "CURL_CA_BUNDLE" in os.environ):

            try:
                requests.get(f"{self.aoa_url}/admin/info")
            except requests.exceptions.SSLError:
                from aia import AIASession
                from tempfile import NamedTemporaryFile

                self.logger.debug("Attempting certificate chain chasing via aia")

                # unless, debug logging enabled,
                # change logging level for aia to warning as it prints debug at info level
                if logging.root.level > logging.DEBUG:
                    logging.getLogger("aia").setLevel(logging.WARNING)

                try:
                    aia_session = AIASession()

                    ca_data = aia_session.cadata_from_url(self.aoa_url)
                    with NamedTemporaryFile("w", delete=False) as pem_file:
                        pem_file.write(ca_data)
                        pem_file.flush()

                    self.session.verify = pem_file.name
                except aia.InvalidCAError:
                    raise Exception("Attempted to find trusted root certificate via AIA chasing but not found.\n"
                                    "Please configure REQUESTS_CA_BUNDLE or CURL_CA_BUNDLE.\n"
                                    "Alternatively, to ignore TLS validation (not advised), set AOA_SSL_VERIFY=false")
