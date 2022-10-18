from layerx import datalake


class LayerxClient:
    """
    Python SDK of LayerX
    """

    def __init__(self, api_key: str, secret: str, layerx_url: str) -> None:
        _datalake_url = f'{layerx_url}/datalake'
        self.datalakeClient = datalake.DatalakeClient(api_key, secret, _datalake_url)

    def upload_modelrun_from_json(
            self,
            storage_base_path: str,
            model_id: str,
            file_path: str,
            annotation_geometry: str
    ):
        """
        Upload model run data from a json file
        """
        self.datalakeClient.upload_modelrun_from_json(
            storage_base_path,
            model_id,
            file_path,
            annotation_geometry
        )
