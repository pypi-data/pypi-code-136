from typing import Any, Dict

from infiniaml_idp_client import IdpClient


def docs_path(project_id: int) -> str:
    return f"/api/v1/projects/{project_id}/docs"


def get_docs(idp_client: IdpClient, project_id: int) -> Dict[str, Any]:
    resp = idp_client.get(docs_path(project_id))
    return resp.json()
