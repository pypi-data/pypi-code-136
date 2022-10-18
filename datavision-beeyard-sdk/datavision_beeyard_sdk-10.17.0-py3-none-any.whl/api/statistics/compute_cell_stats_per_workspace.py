from ...client import AuthenticatedClient
import json


def cell_count(workspace_id: str, *, client: AuthenticatedClient):
    url = "{}/api/v1/workspaces/{workspaceId}/cells/stats".format(
        client.base_url, workspaceId=workspace_id
    )
    response = client.get(url, headers=client.token_headers)
    return json.loads(response.content.decode("utf-8"))
