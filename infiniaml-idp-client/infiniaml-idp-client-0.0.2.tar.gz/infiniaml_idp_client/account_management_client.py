from typing import Any, List

from typing_extensions import Self

from infiniaml_idp_client._common.constants import IDP_URL
from infiniaml_idp_client.models import Project

from .credentials import TokenCredential
from .idp_client import IdpClient

__all__ = ("AccountManagementClient",)


class AccountManagementClient:
    def __init__(
        self,
        token_credential: TokenCredential,
        *,
        idp_url: str = IDP_URL,
    ) -> None:
        """Create an IDP AccountManagementClient

        Args:
            token_credential: A token credential instance used for authentication
        """
        self._idp_client = IdpClient(token_credential, idp_url)

    def __enter__(self) -> Self:
        self._idp_client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._idp_client.__exit__()

    def list_projects(self) -> List[Project]:
        """List projects belonging to active account"""

        account = (self._idp_client.get("/management/api/v1/accounts")).json()["accounts"][0]
        projects = (self._idp_client.get(f"/management/api/v1/accounts/{account['id']}/projects")).json()
        return projects
