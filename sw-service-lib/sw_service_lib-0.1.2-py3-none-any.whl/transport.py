from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests
from gql.transport.requests import RequestsHTTPTransport
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import RequestException

from sw_service_lib.error import StrangeworksError


class StrangeworksTransport(RequestsHTTPTransport):
    """Transport layer with automatic token refresh."""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        svcs_path: str = "services",
        headers: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        retries: int = 0,
        **kvargs,
    ) -> None:
        self.services_url = urljoin(base_url, svcs_path)
        self.api_key = api_key
        self.auth_url = urljoin(base_url, "service/token")

        super().__init__(
            url=self.services_url,
            headers=headers,
            timeout=timeout,
            retries=retries,
        )
        self.auth_token: Optional[str] = None

    def _get_token(self) -> None:
        try:
            res = requests.post(self.auth_url, json={"key": self.api_key})
            if res.status_code != 200:
                raise StrangeworksError.forbidden_error(
                    "Unable to exchange api key for bearer token"
                )
            payload = res.json()
            self.auth_token = payload["accessToken"]
            if self.headers:
                self.headers["Authorization"] = self.auth_token
            else:
                self.headers = {"Authorization": self.auth_token}

        except RequestException:
            raise StrangeworksError.forbidden_error(
                "Unable to obtain bearer token using api key."
            )

    def connect(self):
        """Set up a session object.

        Creates a session object for the transport to use and configures retries and
        re-authentication.
        """
        if self.session is None:

            self.session = requests.Session()

            # set up retries.
            if self.retries > 0:
                adapter = HTTPAdapter(
                    max_retries=Retry(
                        total=self.retries,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504],
                        allowed_methods=None,
                    )
                )

                for prefix in "http://", "https://":
                    self.session.mount(prefix, adapter)

            # setup token refresh if expired.
            self.session.hooks["response"].append(self._reauthenticate)

        if self.auth_token is None:
            self._get_token()

    def _reauthenticate(self, res: requests.Response, **kwargs) -> requests.Response:
        """Reauthenticate to Strangeworks.

        Parameters
        ----------
        res : requests.Response
        **kwargs

        Returns
        -------
        : requests.Response
        """
        if res.status_code == requests.codes.unauthorized:
            seen_before_header = "X-SW-SDK-Re-Auth"
            # We've tried once before but no luck. Maybe they've changed their api_key?
            if res.request.headers.get(seen_before_header):
                raise StrangeworksError(
                    "Unable to re-authenticate your request. Utilize "
                    "strangeworks.authenticate(username, api_key) with your most up "
                    "to date credentials and try again."
                )
            self._get_token()
            # self.session.send just sends the prepared request, so we must manually
            # ensure that the new token is part of the header
            res.request.headers["Authorization"] = f"Bearer {self.auth_token}"
            res.request.headers[seen_before_header] = True
            return self.session.send(res.request)
