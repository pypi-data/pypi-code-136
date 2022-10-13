from typing import Optional

from humanloop.api.models.generate import GenerateRequest, GetModelConfigResponse
from humanloop.api.models.model import GenerateResponse
from humanloop.sdk.init import _get_client, _get_settings


def generate(**kwargs) -> GenerateResponse:
    """Generates an output from your provider foundation model and automatically
    logs the results for feedback later.

    The model configuration used depends on how the method was called. The
    following signatures are accepted:
    (Listed in decreasing priority. If multiple signatures are satisfied, the highest priority signature will be used.
    For example, if both model config parameters and an experiment ID is provided, the model config parameters will be
    used and the experiment ID will be ignored.)
        1. Model config parameters:
            The specific model configuration parameters will be used to link to an existing or create a new model
            configuration that will be used for this generation.
            E.g. generate(model="text-davinci-002", prompt_template="...", parameters={...}, ... )
        2. model_config_id:
            The ID of an existing model configuration to be used.
            E.g. generate(model_config_id="config_abcdef1234567")
        3. experiment_id:
            The ID of an existing experiment. A model configuration will be sampled from the experiment's list of
            active model configurations.
            E.g. generate(experiment_id="exp_abcdef1234567")
        4. project:
            A model configuration will be selected based on the projects deployment settings.
            E.g. generate(project="your-project-name-001")

    Note that all of the above signatures also require the following parameters:
        "project", "inputs", "source"
    """
    settings = _get_settings()
    client = _get_client()
    return client.generate(
        GenerateRequest.parse_obj(
            {**kwargs, "provider_api_keys": settings.provider_api_keys}
        )
    )


def get_model_config(
    experiment_id: Optional[str] = None,
    project_id: Optional[str] = None,
) -> GetModelConfigResponse:
    """Retrieves a model config to use to execute your model.

    One of "experiment_id" or "project_id" should be provided.
    If "experiment_id" is provided, a model configuration will be sampled
    from the experiment's list of active model configurations.
    If "project_id" is provided, a model configuration will be selected based
    on the projects deployment settings.
    """
    if experiment_id is None and project_id is None:
        raise ValueError("One of 'experiment_id' or 'project_id' should be specified.")
    if experiment_id is not None and project_id is not None:
        raise ValueError(
            "Only one of 'experiment_id' or 'project_id' should be specified."
        )
    client = _get_client()
    if project_id is not None:
        return client.get_model_config_from_project(
            project_id=project_id,
        )
    if experiment_id is not None:
        return client.get_model_config_from_experiment(
            experiment_id=experiment_id,
        )
