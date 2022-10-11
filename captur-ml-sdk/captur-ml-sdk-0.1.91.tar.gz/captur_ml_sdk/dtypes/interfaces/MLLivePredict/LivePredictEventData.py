from pydantic import BaseModel, AnyUrl
from typing import Optional


class LivePredictEventData(BaseModel):
    request_id: str
    endpoint_id: str
    task_type: str
    model_type: str
    serving_input: str
    location: str
    image_url: AnyUrl
    image_id: str
    webhooks: str
