"""Baseten

    isort:skip_file
"""

from truss.build import from_directory
from pathlib import Path
from single_source import get_version
import logging


from collections import defaultdict

from baseten import baseten_artifact
from baseten.baseten_deployed_model import BasetenDeployedModel, models_summary  # noqa: E402
from baseten.common.model_deployer import build_truss, deploy_truss, build_and_deploy_truss, pull_model
from baseten.common.util import setup_logger  # noqa: E402
from baseten.common import settings  # noqa: E402


__version__ = get_version(__name__, Path(__file__).parent.parent)


def version():
    return __version__


patched_modules = defaultdict(lambda: [])


logger = logging.getLogger(__name__)
setup_logger('baseten', logging.INFO)
if settings.DEBUG:
    setup_logger('baseten', logging.DEBUG)
logger.debug(f'Starting the client with the server URL set to {settings.API_URL_BASE}')

# The Baseten model ID that either a) the user initialized baseten with, or b) was created when deploying a model.
working_model_id = None

deploy = build_and_deploy_truss  # This allows the user to call baseten.deploy(model)
build_truss = build_truss
deploy_truss = deploy_truss
load_truss = from_directory
pull = pull_model


create_artifact = baseten_artifact.create_artifact

models_summary = models_summary


def set_log_level(level):
    setup_logger('baseten', level)


def init(baseten_model_id=None):
    """Initialize Baseten

    Args:
        baseten_model_id (str, optional): The BaseTen model id to initialize the client with.
        If not provided, a new Baseten model will be created at deploy() time.
    """
    global working_model_id
    working_model_id = baseten_model_id


def deployed_model_id(model_id: str) -> BasetenDeployedModel:
    """Returns a BasetenDeployedModel object for interacting with the model model_id.

    Args:
        model_id (str)

    Returns:
        BasetenDeployedModel
    """
    return BasetenDeployedModel(model_id=model_id)


def deployed_model_version_id(model_version_id: str) -> BasetenDeployedModel:
    """Returns a BasetenDeployedModel object for interacting with the model version model_version_id.

    Args:
        model_version_id (str)

    Returns:
        BasetenDeployedModel
    """
    return BasetenDeployedModel(model_version_id=model_version_id)


def deployed_artifact_id(artifact_id: str):
    """Returns a BasetenArtifact object for interacting with given the artifact_id

    Args:
        artifact_id (str)

    Returns:
        BasetenArtifact
    """
    return baseten_artifact.BasetenArtifact(artifact_id=artifact_id)


def login(api_key: str):
    """Set the API key for the client.

    Args:
        api_key (str)
    """
    settings.set_config_value('api', 'api_key', api_key)
    logger.info('API key set.')


def configure(server_url: str):
    """Sets the Server URL for the client

    Args:
        server_url (str): The base URL of the server
    """
    if settings.set_server_url(server_url):
        logger.info('Saved server URL.')
    else:
        logger.info('That is not a valid URL.')
