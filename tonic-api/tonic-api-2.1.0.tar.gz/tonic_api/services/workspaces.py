from ..classes.workspace import Workspace
from ..classes.model import Model


class WorkspaceService:
    def __init__(self, client):
        self.client = client

    def get_workspace(self, workspace_id):
        workspace = self.client.http_get("/api/workspace/" + workspace_id)
        return Workspace(
            workspace["id"],
            workspace["workspaceName"],
            [Model(id, model) for (id, model) in workspace["models"].items()],
            self.client,
        )
