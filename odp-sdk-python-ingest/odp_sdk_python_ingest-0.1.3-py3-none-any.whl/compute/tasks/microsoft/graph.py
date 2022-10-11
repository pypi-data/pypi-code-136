import logging
from typing import Dict, Optional, Generator, Any, List, Tuple, Union

import requests

import msal
from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs

LOG = logging.getLogger(__name__)

__all__ = ["MsgListGroups", "MsgListUsers", "MsgListSignins", "MsgGetGroupMembers"]


class MsgBase:
    def __init__(self):
        self.scopes = ["https://graph.microsoft.com/.default"]

    def pre_run(self, credentials: Dict[str, str]) -> None:
        """

        Args:
            credentials: Credentials as a dict. Should include the following keys: `authority`, `client_id`, `client_credential`
        """
        self._app = msal.ConfidentialClientApplication(**credentials)

    def _get_access_token(self) -> str:

        # Check if token exists in cache
        result = self._app.acquire_token_silent(self.scopes, account=None)

        if not result:
            result = self._app.acquire_token_for_client(scopes=self.scopes)

        if not "access_token" in result:
            raise RuntimeError(
                "Failed to authenticate: {} (correlationId: {}) - {}".format(
                    result.get("error"),
                    result.get("correlation_id"),
                    result.get("error_description"),
                )
            )

        return result["access_token"]

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:

        token = self._get_access_token()

        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"

        return requests.request(method, url, headers=headers, **kwargs)

    def _get(self, url, **kwargs) -> requests.Response:
        return self._request("GET", url, **kwargs)

    def _post(self, url, **kwargs) -> requests.Response:
        return self._request("POST", url, **kwargs)

    def _paginate(self, method: str, url: str, **kwargs) -> Generator[Any, None, None]:

        skip_token = None

        while True:
            LOG.debug(f"skip_token={skip_token}")
            response = self._request(method, skip_token or url, **kwargs)

            response.raise_for_status()
            response = response.json()

            for row in response["value"]:
                yield row

            try:
                skip_token = response["@odata.nextLink"]
            except KeyError:
                break


class MsgListGroups(MsgBase, Task):
    def __init__(self, *args, **kwargs):
        MsgBase.__init__(self)

        Task.__init__(self, *args, nout=kwargs.pop("nout", True), **kwargs)

    def run(self, credentials: Dict[str, str]) -> List[Dict]:
        MsgBase.pre_run(self, credentials)

        ret = list(self._read_groups())
        LOG.info(f"Read {len(ret)} groups")

        return ret

    def _read_groups(self) -> Generator[Dict, None, None]:
        response = self._paginate(
            "GET", "https://graph.microsoft.com/v1.0/groups?$select=id,displayName"
        )

        for row in response:
            yield row


class MsgListUsers(MsgBase, Task):
    def __init__(self, *args, **kwargs):
        MsgBase.__init__(self)

        Task.__init__(self, *args, nout=kwargs.pop("nout", True), **kwargs)

    def run(self, credentials: Dict[str, str]) -> List[Dict]:
        MsgBase.pre_run(self, credentials)

        ret = list(self._read_users())
        LOG.info(f"Read {len(ret)} users")

        return ret

    def _read_users(self) -> Generator[Dict, None, None]:
        response = self._paginate("GET", "https://graph.microsoft.com/v1.0/users")

        for row in response:
            yield row


class MsgListSignins(MsgBase, Task):
    def __init__(self, *args, **kwargs):
        MsgBase.__init__(self)

        Task.__init__(self, *args, nout=kwargs.pop("nout", True), **kwargs)

    def run(self, credentials: Dict[str, str]) -> List[Dict]:
        MsgBase.pre_run(self, credentials)

        ret = list(self._read_signin_logs())
        LOG.info(f"Read {len(ret)} signin records")

        return ret

    def _read_signin_logs(self) -> Generator[Dict, None, None]:
        response = self._paginate(
            "GET", "https://graph.microsoft.com/v1.0/auditLogs/signIns"
        )

        for row in response:
            yield row


class MsgGetGroupMembers(MsgBase, Task):
    def __init__(self, group: Optional[Union[Dict, str]] = None, *args, **kwargs):
        MsgBase.__init__(self)
        Task.__init__(self, *args, nout=kwargs.pop("nout", True), **kwargs)

        self.group = group

    @defaults_from_attrs("group")
    def run(
        self, group: Union[Dict, str], credentials: Dict[str, str]
    ) -> List[Dict[str, str]]:
        MsgBase.pre_run(self, credentials)

        if isinstance(group, dict):
            group = group["id"]

        ret = list(self._get_group_members(group))
        LOG.info(f"The group with ID {group} has {len(ret)} members")

        return ret

    def _get_group_members(
        self, group_id: str
    ) -> Generator[Dict[str, str], None, None]:
        response = self._paginate(
            "GET", f"https://graph.microsoft.com/v1.0/groups/{group_id}/members"
        )

        for row in response:
            yield {"group_id": group_id, "user_id": row["id"]}
