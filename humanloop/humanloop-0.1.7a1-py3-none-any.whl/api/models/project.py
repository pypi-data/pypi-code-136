import datetime
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

from humanloop.api.models.experiment import ExperimentResponse
from humanloop.api.models.model_config import ProjectModelConfigResponse


class ProjectResponse(BaseModel):
    id: str = Field(title="Project ID", description="Project ID")
    internal_id: int = Field(
        title="Internal project ID",
        description="Project ID for internal Humanloop use.",
    )
    name: str = Field(title="Project name", description="Unique project name.")
    active_experiment: Optional[ExperimentResponse] = Field(
        title="Active experiment",
        description="Experiment that has been set as the project's active deployment. "
        "At most one of active_experiment and active_model_config can be set.",
    )
    active_model_config: Optional[ProjectModelConfigResponse] = Field(
        title="Active model configuration",
        description="Model configuration that has been set as the project's active deployment. "
        "At most one of active_experiment and active_model_config can be set.",
    )

    created_at: datetime.datetime
    updated_at: datetime.datetime


class CreateProjectRequest(BaseModel):
    name: str


class UpdateProjectRequest(BaseModel):
    active_experiment_id: Optional[str] = Field(
        title="Active experiment ID",
        description="ID for an experiment to set as the project's active deployment. "
        "Starts with 'exp_'. "
        "At most one of active_experiment_id and active_model_config_id can be set.",
    )
    active_model_config_id: Optional[str] = Field(
        title="Active model configuration ID",
        description="ID for a model configuration to set as the project's active deployment. "
        "Starts with 'config_'. "
        "At most one of active_experiment_id and active_model_config_id can be set.",
    )


class CategoricalFeedbackGroup(BaseModel):
    name: str
    labels: List[str]
    type: Literal["categorical"]


class TextFeedbackGroup(BaseModel):
    name: str
    type: Literal["text"]


class FeedbackSchema(BaseModel):
    groups: List[Union[TextFeedbackGroup, CategoricalFeedbackGroup]]
