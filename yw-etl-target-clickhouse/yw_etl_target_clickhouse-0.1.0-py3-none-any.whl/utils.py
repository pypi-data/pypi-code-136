import logging.config
from pathlib import Path


# Conf Keys
class Conf:
    SYNC_WORKING_DIRECTORY = "sync.working_directory"


class Env:
    SYNC_WORKING_DIRECTORY = "TARGET_CLICKHOUSE_HOME"


# Logger
def _get_logger():
    logging_conf_file = Path(__file__).parent / 'logging.conf'
    logging.config.fileConfig(logging_conf_file)
    return logging.getLogger()


targetlog = _get_logger()
