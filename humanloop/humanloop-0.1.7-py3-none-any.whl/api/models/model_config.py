import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ModelProvider(str, Enum):
    """Supported model providers."""

    openai = "OpenAI"
    mock = "Mock"


class ModelEndpoint(str, Enum):
    """Supported model provider endpoints."""

    complete = "Complete"
    edit = "Edit"


class ProjectModelConfigResponse(BaseModel):
    id: str
    display_name: str
    model_name: str
    prompt_template: Optional[str]
    parameters: Optional[dict]
    provider: Optional[ModelProvider]
    endpoint: Optional[ModelEndpoint]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Optional[str]
    last_used: datetime.datetime


class GetModelConfigResponse(ProjectModelConfigResponse):
    """A selected model configuration.

    If the model configuration was selected in the context of an experiment,
    the response will include a trial_id to associate a subsequent log() call.
    """

    trial_id: Optional[str] = Field(
        title="Trial ID",
        description="ID of trial to reference in subsequent log calls.",
    )
