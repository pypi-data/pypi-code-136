import json
import logging
from io import IOBase
from typing import IO, Any, Iterable, Mapping, Tuple, Union
from urllib.parse import urljoin

import requests
from requests.models import Response

from .abstract_service_connexion import AbstractServiceConnexion
from .exceptions import NetworkError, UnauthorizedError


def reset_body(body):
    if "files" in body and isinstance(body["files"], dict):
        logging.debug("Seeking buffered readers to zero")
        for key, value in body["files"].items():
            if isinstance(value, IOBase):
                try:
                    value.seek(0)
                except Exception:
                    pass


def wrapped_request(f):
    def decorated(self, *args, regenerate_jwt=True, **kwargs):
        try:
            resp: Response = f(self, *args, **kwargs)
        except UnauthorizedError as e:
            raise e
        except Exception as e:
            raise NetworkError(
                f"Something went wrong while executing a request '{f.__name__}'. Error: {e}"
            )

        if resp.status_code == 401:
            if regenerate_jwt:
                logging.info(f"Regenerating connection token to {self.host}...")
                self._jwt, self._expires_in = self.generate_jwt()
                reset_body(kwargs)
                return decorated(self, *args, regenerate_jwt=False, **kwargs)
            else:
                raise UnauthorizedError("You are not authorized to do this: regeneration of connection token failed.")

        return resp

    return decorated


class JwtServiceConnexion(AbstractServiceConnexion):
    def __init__(
        self,
        host: str,
        jwt_identifier_data: dict,
        authorization_key: str = "Bearer",
        login_path: str = "/login",
    ) -> None:
        """JwtServiceConnexion may be used to handle a JwtAuthentication connexion with a service.
        You need to give a dict `jwt_identifier_data` that will be sent to the host to ensures validity of your request.
        This data will depend on service contacted. For example for a Deployment / Jwt request on Oracle, this will be :
        {
            "api_token" : <user_api_token>,
            "deployment_id" : <deployment_id>
        }
        """
        self.jwt_identifier_data = jwt_identifier_data
        self.login_path = login_path
        self.authorization_key = authorization_key
        self.host = host
        self.session = requests.Session()
        self._jwt, self._expires_in = None, None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            self.session.close()

    @property
    def jwt(self) -> str:
        if self._jwt is None:
            self._jwt, self._expires_in = self.generate_jwt()
        return self._jwt

    def generate_jwt(self):
        url = urljoin(self.host, self.login_path)
        try:
            response = self.session.post(
                url=url, data=json.dumps(self.jwt_identifier_data)
            )
        except Exception as e:
            raise NetworkError(
                f"Server is not responding, please check your host. Exception: {e}"
            )

        if response.status_code != 200:
            raise UnauthorizedError("Unauthorized attempt to connect.")

        try:
            data = response.json()
            return data["jwt"], data["expires"]
        except Exception:
            raise UnauthorizedError(
                "Cannot parse response from external service. Please contact support."
            )

    def _build_headers(self):
        return {"Authorization": f"{self.authorization_key} {self.jwt}"}

    @wrapped_request
    def get(self, path: str, params: dict = None, stream=False):
        url = urljoin(self.host, path)
        return self.session.get(
            url=url,
            headers=self._build_headers(),
            params=params,
            stream=stream,
        )

    @wrapped_request
    def xget(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        stream=False
    ):
        url = urljoin(self.host, path)
        return self.session.request(
            method="XGET",
            url=url,
            data=data,
            headers=self._build_headers(),
            params=params,
            stream=stream,
        )

    @wrapped_request
    def post(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        files: Any = None
    ):
        url = urljoin(self.host, path)
        return self.session.post(
            url=url,
            data=data,
            headers=self._build_headers(),
            params=params,
            files=files,
        )

    @wrapped_request
    def patch(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None
    ):
        url = urljoin(self.host, path)
        return self.session.patch(
            url=url, data=data, headers=self._build_headers(), params=params
        )

    @wrapped_request
    def put(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None
    ):
        url = urljoin(self.host, path)
        return self.session.put(
            url=url, data=data, headers=self._build_headers(), params=params
        )

    @wrapped_request
    def delete(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None
    ):
        url = urljoin(self.host, path)
        return self.session.delete(
            url=url, data=data, headers=self._build_headers(), params=params
        )
