from typing import Any, List

from typing_extensions import Self

from infiniaml_idp_client._common.constants import IDP_URL
from infiniaml_idp_client.models import Project

from .credentials import AsyncTokenCredential
from .idp_client import IdpClient

__all__ = ("AccountManagementClient",)


class AccountManagementClient:
    def __init__(
        self,
        token_credential: AsyncTokenCredential,
        *,
        idp_url: str = IDP_URL,
    ) -> None:
        """Create an IDP AccountManagementClient

        Args:
            token_credential: A token credential instance used for authentication
        """
        self._idp_client = IdpClient(token_credential, idp_url)

    async def __aenter__(self) -> Self:
        await self._idp_client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._idp_client.__aexit__()

    async def list_projects(self) -> List[Project]:
        """List projects belonging to active account"""

        account = (await self._idp_client.get("/management/api/v1/accounts")).json()["accounts"][0]
        projects = (await self._idp_client.get(f"/management/api/v1/accounts/{account['id']}/projects")).json()
        return projects
