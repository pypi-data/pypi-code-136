import abc
from typing import Dict, Optional, Union

from pydantic import BaseModel, Field

from humanloop.api.models.model import ModelProviders
from humanloop.api.models.model_config import (
    ModelEndpoint,
    ModelProvider,
    ProjectModelConfigResponse,
)
from humanloop.api.models.utils import KeyValues, RootBaseModel


class OptionalProviderApiKeys(BaseModel, abc.ABC):
    provider_api_keys: Optional[Dict[ModelProviders, str]] = Field(
        # Marked as Optional to allow initialization without this. This is added by the SDK method.
        title="Provider API Keys",
        description="API keys required by each provider to make API calls. "
        "These API keys are not stored by Humanloop.",
    )


class BaseGenerate(OptionalProviderApiKeys, abc.ABC):
    project: str = Field(
        title="Project name",
        description="Unique project name. The model configuration will be "
        "added to the project if necessary.",
    )
    inputs: KeyValues = Field(
        title="Model input data",
        description="List of name, value pairs for the inputs used by your prompt "
        "template, or directly by your model.",
    )
    source: Optional[str] = Field(
        title="Source",
        description="What was source of the model used for this generation?"
        "e.g. website-landing-page",
    )
    metadata: Optional[KeyValues] = Field(
        title="Metadata",
        description="Any additional metadata that you would like to log for reference.",
    )


class ProjectGenerate(BaseGenerate):
    project: str = Field(
        title="Project name",
        description="Unique project name. This project must already have an active deployment configured.",
    )


class ExperimentGenerate(BaseGenerate):
    experiment_id: str = Field(
        title="ID of experiment",
        description="If an experiment ID is provided a model configuration will be "
        "sampled from the experiments active model configurations.",
    )


class ModelConfigGenerate(BaseGenerate):
    model_config_id: str = Field(
        title="ID of a model config",
        description="The model configuration specified will be used to create a generation.",
    )


class RawGenerate(BaseGenerate):
    model: str = Field(
        title="Model instance used",
        description="What model instance was used for the generation? "
        "e.g. text-davinci-002.",
    )
    parameters: Optional[KeyValues] = Field(
        title="Model parameters",
        description="Provider-specific hyperparameter settings that along with "
        "your model and prompt template (if provided) will uniquely determine a model"
        " configuration on Humanloop. For example, the temperature setting.",
    )
    prompt_template: str = Field(
        title="Prompt template",
        description="Prompt template that incorporated your specified inputs to form "
        "your final request to the model. "
        "NB: Input variables within the prompt template should be specified "
        "with syntax: {{INPUT_NAME}}."
        "This is used only if an existing experiment_id or model_config_id "
        "are not provided.",
    )
    provider: Optional[ModelProvider] = Field(
        title="Model provider",
        description="The company who is hosting the target model.",
        default=ModelProviders.openai,
    )
    endpoint: Optional[ModelEndpoint] = Field(
        title="Provider endpoint",
        description="Which of the providers model endpoints to use. "
        "For example Complete or Edit.",
        default=ModelEndpoint.complete,
    )


class GenerateRequest(RootBaseModel):
    # Used as Pydantic request body type for uplink client
    __root__: Union[
        RawGenerate, ModelConfigGenerate, ExperimentGenerate, ProjectGenerate
    ]


class GetModelConfigResponse(ProjectModelConfigResponse):
    """A selected model configuration.

    If the model configuration was selected in the context of an experiment,
    the response will include a trial_id to associate a subsequent log() call.
    """

    trial_id: Optional[str] = Field(
        title="Trial ID",
        description="ID of trial to reference in subsequent log calls.",
    )
