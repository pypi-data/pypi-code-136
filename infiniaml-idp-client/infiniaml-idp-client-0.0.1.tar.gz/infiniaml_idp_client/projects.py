from typing import List

from infiniaml_idp_client._common.constants import IDP_URL
from infiniaml_idp_client.models import Project

from .credentials import AccessKeyCredentials
from .idp_client import IdpClient

__all__ = ("list_projects",)


def list_projects(creds: AccessKeyCredentials, *, idp_url: str = IDP_URL) -> List[Project]:
    with IdpClient(creds, idp_url=idp_url) as client:
        account = (client.get("/management/api/v1/accounts")).json()["accounts"][0]
        projects = (client.get(f"/management/api/v1/accounts/{account['id']}/projects")).json()
    return projects
