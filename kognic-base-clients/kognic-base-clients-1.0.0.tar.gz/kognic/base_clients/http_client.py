"""Client for communicating with the Kognic platform."""
import logging
import urllib.parse
from typing import Optional, Union

import requests
from kognic.auth.requests.auth_session import RequestsAuthSession

from kognic.base_clients import __version__
from kognic.base_clients.models import PaginatedResponse
from kognic.base_clients.util import filter_none

from humps import decamelize

log = logging.getLogger(__name__)

ENVELOPED_JSON_TAG = "data"


class HttpClient:
    """Http Client dealing with auth and communication with API."""

    def __init__(self, auth, host: str, auth_host: str, client_organization_id: int = None, timeout: int = 60):
        """
        :param auth: auth credentials, see https://pypi.org/project/kognic-auth
        :param host: override for api url
        :param auth_host: override for authentication url
        :param client_organization_id: Overrides your users organization id. Only works with an Kognic user.
        :param max_upload_retry_attempts: Max number of attempts to retry uploading a file to GCS.
        :param max_upload_retry_wait_time:  Max with time before retrying an upload to GCS.
        """

        self.host = host
        self._auth_req_session = RequestsAuthSession(host=auth_host, auth=auth)
        self.headers = {
            "Accept-Encoding": "gzip",
            "Accept": "application/json",
            "User-Agent": f"kognic-{decamelize(self.__class__.__name__)}/{__version__}"
        }
        self.dryrun_header = {"X-Dryrun": ""}
        self.timeout = timeout

        if client_organization_id is not None:
            self.headers["X-Organization-Id"] = str(client_organization_id)
            log.warning(
                f"WARNING: You will now act as if you are part of organization: {client_organization_id}. "
                f"This will not work unless you are an Kognic user."
            )

    @property
    def session(self):
        return self._auth_req_session.session

    @staticmethod
    def _raise_on_error(resp: requests.Response) -> requests.Response:
        try:
            resp.raise_for_status()
        except requests.HTTPError as exception:
            if exception.response is not None and exception.response.status_code == 400:
                try:
                    message = exception.response.json()["message"]
                except ValueError:
                    message = exception.response.text
                raise RuntimeError(message) from exception

            raise exception from None
        return resp

    @staticmethod
    def _unwrap_enveloped_json(js: dict) -> Union[dict, list, PaginatedResponse]:
        if isinstance(js, list):
            return js
        elif js is not None and js.get('metadata') is not None:
            return PaginatedResponse.from_json(js)
        elif js is not None and js.get(ENVELOPED_JSON_TAG) is not None:
            return js[ENVELOPED_JSON_TAG]
        return js

    def get(self, endpoint, **kwargs) -> dict:
        r"""Sends a GET request. Returns :class:`dict` object.

        :param endpoint: endpoint to be appended to `client.host`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: dict
        """

        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)
        url = urllib.parse.urljoin(self.host, endpoint)
        resp = self.session.get(url, **kwargs)
        return self._unwrap_enveloped_json(self._raise_on_error(resp).json())

    def post(self, endpoint, data=None, json=None, dryrun=False, discard_response=False, **kwargs) -> Optional[dict]:
        r"""Sends a POST request. Returns :class:`dict` object.

        :param endpoint: endpoint to be appended to `client.host`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: dict
        """

        if dryrun:
            headers = {**self.headers, **self.dryrun_header}
        else:
            headers = {**self.headers}

        kwargs.setdefault("headers", headers)
        kwargs.setdefault("timeout", self.timeout)
        resp = self.session.post(f"{self.host}/{endpoint}", data, filter_none(json), **kwargs)
        if discard_response:
            self._raise_on_error(resp)
            return None
        else:
            return self._unwrap_enveloped_json(self._raise_on_error(resp).json())

    def put(self, endpoint, data, **kwargs) -> dict:
        r"""Sends a PUT request. Returns :class:`dict` object.

        :param endpoint: endpoint to be appended to `client.host`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: dict
        """
        kwargs.setdefault("headers", self.headers)
        kwargs.setdefault("timeout", self.timeout)
        resp = self.session.put(f"{self.host}/{endpoint}", filter_none(data), **kwargs)
        return self._unwrap_enveloped_json(self._raise_on_error(resp).json())
