import logging
from typing import List

import requests
from requests import HTTPError
from uplink import (
    Body,
    Consumer,
    delete,
    get,
    json,
    patch,
    post,
    response_handler,
    returns,
)
from uplink.auth import ApiTokenHeader

from humanloop.api.models.experiment import (
    CreateExperimentRequest,
    ExperimentResponse,
    TrialResponse,
)
from humanloop.api.models.feedback import ListFeedbackResponse
from humanloop.api.models.generate import GenerateRequest, GetModelConfigResponse
from humanloop.api.models.log import (
    ListFeedbackRequest,
    ListLogRequest,
    ListLogResponse,
)
from humanloop.api.models.metric import (
    CreateMetricRequest,
    MetricResponse,
    UpdateMetricRequest,
)
from humanloop.api.models.model import (
    GenerateResponse,
    ModelConfig,
    ModelConfigResponse,
    ModelGenerate,
)
from humanloop.api.models.project import (
    CreateProjectRequest,
    FeedbackSchema,
    ProjectResponse,
    UpdateProjectRequest,
)
from humanloop.api.models.user import UserResponse

logger = logging.getLogger(__file__)


def raise_for_status(response: requests.Response):
    """Checks whether the response was successful."""
    try:
        response.raise_for_status()
        return response
    except HTTPError as e:
        # Attempt to log JSON error response.
        try:
            logger.error(f"Request to {e.request.url} failed with {e.response.json()}")
        except Exception:
            pass
        raise e


@response_handler(raise_for_status)
class Humanloop(Consumer):
    """Python Client for the Humanloop API"""

    @returns.json()
    @get()
    def health_check(self):
        """Health check"""
        pass

    @returns.json()
    @get("/users/me")
    def read_me(self) -> UserResponse:
        """Validate user exists with valid password and return access token"""
        pass

    @json
    @returns.json
    @post("/v1/logs")
    def log(
        self,
        request: Body(type=ListLogRequest),
    ) -> ListLogResponse:
        """Log a datapoint to your Humanloop project."""

    @json
    @returns.json
    @post("/v1/feedback")
    def feedback(
        self, feedback: Body(type=ListFeedbackRequest)
    ) -> ListFeedbackResponse:
        """Add feedback to an existing logged datapoint."""

    @json
    @returns.json
    @post("/v1/model-configs")
    def register(self, model_config: Body(type=ModelConfig)) -> ModelConfigResponse:
        """Register a model config to a project and optionally add it to an
        experiment.

        If the project provided does not exist, a new project will be created
        automatically.
        If an experiment name is provided, the specified experiment must already
        exist. Otherwise, an error will be raised.

        If the model config is the first to be associated to the project, it will
        be set as the active model config.
        """

    @json
    @returns.json
    @get("/v1/experiments/{experiment_id}/model-config")
    def get_model_config_from_experiment(
        self, experiment_id: str
    ) -> GetModelConfigResponse:
        """Retrieves a model config to use to execute your model.

        A model configuration will be sampled from the experiment's list of active
        model configurations.
        """

    @json
    @returns.json
    @get("/v1/projects/{project_id}/model-config")
    def get_model_config_from_project(self, project_id: str) -> GetModelConfigResponse:
        """Retrieves a model config to use to execute your model.

        A model configuration will be selected based on the project's
        active model config/experiment settings.
        """

    # TODO: Remove as replaced by get model config from experiment and get model config from project.
    @json
    @returns.json
    @post("/experiments/{experiment_id}/trial")
    def trial_old(self, experiment_id: str) -> TrialResponse:
        """Manually generate a trial for a given experiment."""

    @json
    @returns.json
    @post("/models/generate")
    def generate_old(self, request: Body(type=ModelGenerate)) -> GenerateResponse:
        """Generate output from a provider model and log the response for feedback"""

    @returns.json
    @get("/v1/projects/{project_id}")
    def get_project(self, project_id: str) -> ProjectResponse:
        """Get the project with the given ID"""

    @json
    @returns.json
    @post("/v1/projects")
    def create_project(
        self, request: Body(type=CreateProjectRequest)
    ) -> ProjectResponse:
        """Create a project with the given name"""

    @json
    @returns.json
    @post("/v1/projects/{project_id}/feedback-schema")
    def add_feedback_labels_and_groups(
        self, project_id: str, schema: Body(type=FeedbackSchema)
    ) -> FeedbackSchema:
        """Add the specified feedback groups and labels"""

    @json
    @returns.json
    @post("/v1/projects/{project_id}/metrics")
    def create_metric(
        self, project_id: str, metric: Body(type=CreateMetricRequest)
    ) -> MetricResponse:
        """Create a new metric and associate it to a project."""

    @returns.json
    @get("/v1/projects/{project_id}/metrics")
    def get_metrics(self, project_id: str) -> List[MetricResponse]:
        """Get an array of existing metrics for a given project"""

    @json
    @returns.json
    @patch("/v1/projects/{project_id}/metrics/{metric_id}")
    def update_metric(
        self, project_id: str, metric_id: str, request: Body(type=UpdateMetricRequest)
    ) -> MetricResponse:
        """Update a specific metric."""

    @returns.json
    @delete("/v1/projects/{project_id}/metrics/{metric_id}")
    def delete_metric(self, project_id: str, metric_id: str) -> MetricResponse:
        """Delete a specific metric."""

    @json
    @returns.json
    @get("/v1/projects/{project_id}/experiments")
    def get_experiments(self, project_id: str) -> List[ExperimentResponse]:
        """Get an array of experiments associated to your project"""

    @json
    @returns.json
    @post("/v1/projects/{project_id}/experiments")
    def create_experiment(
        self, project_id: str, experiment: Body(type=CreateExperimentRequest)
    ) -> ExperimentResponse:
        """Create an experiment for your project.

        You can optionally specify IDs of your project's model configs to include
        in the experiment, along with a specific metric to optimise.
        """

    @json
    @returns.json
    @patch("/v1/projects/{project_id}")
    def update_project(
        self, project_id: str, update: Body(type=UpdateProjectRequest)
    ) -> ProjectResponse:
        """Update the specified project"""

    @returns.json
    @delete("/v1/projects/{project_id}/active-model-config")
    def remove_project_active_model_config(self, project_id: str) -> ProjectResponse:
        """Remove the project's active model config, if set."""

    @returns.json
    @delete("/v1/projects/{project_id}/active-experiment")
    def remove_project_active_experiment(self, project_id: str) -> ProjectResponse:
        """Remove the project's active experiment, if set."""

    @json
    @returns.json
    @post("/v1/generate")
    def generate(self, request: Body(type=GenerateRequest)) -> GenerateResponse:
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
                E.g. { "model: "text-davinci-002", "prompt_template", "parameters", ... }
            2. model_config_id:
                The ID of an existing model configuration to be used.
                E.g. { "model_config_id": "config_abcdef1234567" }
            3. experiment_id:
                The ID of an existing experiment. A model configuration will be sampled from the experiment's list of
                active model configurations.
                E.g. { "experiment_id": "exp_abcdef1234567" }
            4. project:
                A model configuration will be selected based on the projects deployment settings.
                E.g. { "project": "your-project-name-001" }

        Note that all of the above signatures also require the following parameters:
            { "project", "inputs", "source", "provider_api_keys" }
        """


def get_humanloop_client(api_key: str, base_url: str) -> Humanloop:
    return Humanloop(base_url=base_url, auth=ApiTokenHeader("X-API-KEY", api_key))
