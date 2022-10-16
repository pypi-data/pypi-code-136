from typing import Any, Dict, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from wepipe.pipeline.base_pipeline import BasePipelineConfig
from wepipe.destination.base_destination import BaseDestinationConfig
from wepipe.source.base_source import BaseSourceConfig


class WorkflowConfig(BaseModel):
    source_config: Optional[BaseSourceConfig]
    destination_config: Optional[BaseDestinationConfig]
    pipeline_config: Optional[BasePipelineConfig]
    time_in_seconds: Optional[int]

    class Config:
        arbitrary_types_allowed = True


class WorkflowState(BaseModel):
    source_state: Optional[Dict[str, Any]]
    destination_state: Optional[Dict[str, Any]]
    pipeline_state: Optional[Dict[str, Any]]

    class Config:
        arbitrary_types_allowed = True
        response_model_exclude_unset = True


class Workflow(BaseModel):
    id: str = str(uuid4())
    config: WorkflowConfig
    states: WorkflowState = Field(WorkflowState())

    class Config:
        arbitrary_types_allowed = True
        response_model_exclude_unset = True
