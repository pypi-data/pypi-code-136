from typing import List
from ..classes.httpclient import HttpClient

class ModelService:
    def __init__(self, client: HttpClient):
        self.client = client

    def get_trained_model(self, job_id: str):
        return self.client.http_get("/api/modeltraining/models/" + job_id)
    
    def get_most_recent_trained_model(self, model_id: str):
        return self.client.http_get(
            "/api/modeltraining/most_recent_trained_model/" + model_id
        )
    
    def get_most_recent_trained_model_old(self, workspace_id: str, model_id: str):
        params = {"workspaceId": workspace_id, "modelId": model_id}
        return self.client.http_get(
            "/api/modeltraining/most_recent_trained_model_old", params=params
        )

    def sample(self, model_training_id: str, num_rows: int):
        params = {"numRows": num_rows} if num_rows is not None else {}
        return self.client.http_get(
            "/api/modeltraining/sample/" + model_training_id, params=params
        )
    
    def conditional_sample(self, model_training_id: str, conditions_list: List[dict]):
        return self.client.http_post(
            "/api/modeltraining/sample_sequences_conditionally/" + model_training_id,
            data=conditions_list
        )

    def sample_source(self, workspace_id, query, num_rows):
        data = {"workspaceId": workspace_id, "query": query, "numRows": num_rows}
        return self.client.http_post("/api/model/get_preview_raw", data=data)

    def get_schema(self, workspace_id, query):
        data = {"workspaceId": workspace_id, "query": query}
        return self.client.http_post("/api/model/get_schema_of_query", data=data)
    
    def get_job_status(self, job_id: str):
        return self.client.http_get("/api/job/" + job_id)
    
    def start_training(self, workspace_id: str, model_id: str):
        params = {"workspaceId": workspace_id, "modelId": model_id}
        return self.client.http_post(
            "/api/modeltraining/train", params=params
        )