from tonic_api.classes.httpclient import HttpClient
from tonic_api.services.workspaces import WorkspaceService
from tonic_api.classes.workspace import Workspace


class TonicApi:
    '''Wrapper class for invoking Tonic API
    
    Parameters
    ----------
    base_url : str
        The url to your Tonic instance. Do not include trailing backslashes
    api_key : str
        Your api token

    Examples
    --------
    >>> TonicApi("http://localhost:3000", "your_api_key")
    '''
    def __init__(self, base_url : str, api_key: str):
        client = HttpClient(base_url, api_key)
        self.workspace_service = WorkspaceService(client)

    def get_workspace(self, workspace_id : str) -> Workspace:
        '''Get instance of Workspace class with specified workspace_id.

        Parameters
        ----------
        workspace_id : str
            The id for your workspace

        Returns
        -------
        Workspace

        Examples
        --------
        >>> workspace = tonic.get_workspace("11529c2f-e9a7-6c12-4025-c2cdc0dcb6fa")
        '''
        return self.workspace_service.get_workspace(workspace_id)
