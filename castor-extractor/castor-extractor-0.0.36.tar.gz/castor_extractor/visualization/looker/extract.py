import logging
from typing import Iterable, Optional, Tuple

from ...logger import add_logging_file_handler
from ...utils import (
    SafeMode,
    current_timestamp,
    deep_serialize,
    get_output_filename,
    write_json,
    write_summary,
)
from .api import ApiClient, Credentials, explore_names_associated_to_dashboards
from .assets import LookerAsset
from .parameters import get_parameters

logger = logging.getLogger(__name__)


def _safe_mode(directory: str) -> SafeMode:
    add_logging_file_handler(directory)
    return SafeMode((Exception,), float("inf"))


def _client(
    base_url: str,
    client_id: str,
    client_secret: str,
    timeout: Optional[int],
    safe_mode: Optional[SafeMode],
) -> ApiClient:
    credentials = Credentials(
        base_url=base_url,
        client_id=client_id,
        client_secret=client_secret,
        timeout=timeout,
    )
    return ApiClient(credentials=credentials, safe_mode=safe_mode)


def iterate_all_data(
    client: ApiClient, all_looks: bool
) -> Iterable[Tuple[LookerAsset, list]]:
    """Iterate over the extracted Data From looker"""

    logger.info("Extracting users from Looker API")
    yield LookerAsset.USERS, deep_serialize(client.users())

    logger.info("Extracting folders from Looker API")
    yield LookerAsset.FOLDERS, deep_serialize(client.folders())

    logger.info("Extracting looks from Looker API")
    yield LookerAsset.LOOKS, deep_serialize(client.looks(all_looks))

    logger.info("Extracting dashboards from Looker API")
    dashboards = client.dashboards()
    yield LookerAsset.DASHBOARDS, deep_serialize(dashboards)

    logger.info("Extracting lookml models from Looker API")
    lookmls = client.lookml_models()
    yield LookerAsset.LOOKML_MODELS, deep_serialize(lookmls)

    logger.info("Extracting explores from Looker API")
    explore_names = explore_names_associated_to_dashboards(lookmls, dashboards)
    yield LookerAsset.EXPLORES, deep_serialize(client.explores(explore_names))

    logger.info("Extracting connections from Looker API")
    connections = client.connections()
    yield LookerAsset.CONNECTIONS, deep_serialize(connections)

    logger.info("Extracting projects from Looker API")
    projects = client.projects()
    yield LookerAsset.PROJECTS, deep_serialize(projects)


def extract_all(**kwargs) -> None:
    """
    Extract Data From looker and store it locally in files under the
    output_directory
    """
    parameters = get_parameters(**kwargs)
    output_directory = parameters.output_directory
    base_url = parameters.base_url

    is_safe_mode = parameters.is_safe_mode
    safe_mode = _safe_mode(output_directory) if is_safe_mode else None
    client = _client(
        base_url=base_url,
        client_id=parameters.client_id,
        client_secret=parameters.client_secret,
        timeout=parameters.timeout,
        safe_mode=safe_mode,
    )

    ts = current_timestamp()

    for key, data in iterate_all_data(client, parameters.all_looks):
        filename = get_output_filename(key.value, output_directory, ts)
        write_json(filename, data)

    write_summary(output_directory, ts, base_url=base_url)
