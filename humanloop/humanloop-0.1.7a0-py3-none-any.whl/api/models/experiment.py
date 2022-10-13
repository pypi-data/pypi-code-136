import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .metric import BaseMetricResponse
from .model import ModelEndpoints, ModelProviders
from .utils import KeyValues


class TrialResponse(BaseModel):
    id: str = Field(
        title="Trial ID",
        description="Unique ID of trial to reference in subsequent log calls.",
    )
    model_config_id: str = Field(
        title="Model config ID",
        description="Unique ID of the model config associated to the trial.",
    )
    experiment_id: str = Field(
        title="Experiment",
        description="Unique ID of the experiment the trial belongs to.",
    )
    model_config_name: Optional[str] = Field(
        title="Model config name",
    )
    model: str = Field(
        title="Instance of model used",
        description="What instance of model was used for the generation?"
        "e.g. text-davinci-002. ",
    )
    prompt_template: Optional[str] = Field(
        title="Prompt template",
        description="Prompt template that incorporated your specified inputs to form "
        "your final request to the model.",
    )
    parameters: Optional[KeyValues] = Field(
        title="Model parameters",
        description="The hyper-parameter settings that along with your model source "
        "and prompt template (if provided) will uniquely determine a model"
        " configuration on Humanloop. For example, the temperature setting.",
    )
    provider: Optional[ModelProviders] = Field(
        title="Model provider",
        description="The company who is hosting the target model.",
    )
    endpoint: Optional[ModelEndpoints] = Field(
        title="Provider endpoint",
        description="Which of the providers model endpoints to use."
        "For example Complete or Edit. ",
    )


class ExperimentModelConfigResponse(BaseModel):
    mean: Optional[float]
    spread: Optional[float]
    trials_count: int
    active: bool
    id: str
    display_name: str
    model_name: str
    prompt_template: Optional[str]
    parameters: Optional[dict]
    provider: Optional[ModelProviders]
    endpoint: Optional[ModelEndpoints]
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ExperimentPositiveLabel(BaseModel):
    group: str
    label: str


class ExperimentResponse(BaseModel):
    id: str
    project_id: str
    name: str
    active: bool

    status: str  # TODO add sensible enum
    model_configs: Optional[List[ExperimentModelConfigResponse]]
    metric: BaseMetricResponse
    positive_labels: List[ExperimentPositiveLabel]

    created_at: datetime.datetime
    updated_at: datetime.datetime


class CreateExperimentRequest(BaseModel):
    name: str
    model_config_ids: Optional[List[str]]
    positive_labels: List[ExperimentPositiveLabel]


class UpdateExperimentRequest(BaseModel):
    name: Optional[str]
    active: Optional[bool]
    metric_id: Optional[str]
    positive_labels: Optional[List[ExperimentPositiveLabel]]
    config_ids_to_register: Optional[List[str]]
    config_ids_to_deregister: Optional[List[str]]
