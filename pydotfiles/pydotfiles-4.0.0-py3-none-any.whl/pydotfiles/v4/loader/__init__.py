# General imports
from os import walk as os_walk
from os import path as os_path
from pathlib import Path
from typing import Dict
from json import load as json_load
from logging import getLogger

# 3rd party imports
from yaml import load as yaml_load
from yaml import YAMLError, Loader
from yaml.scanner import ScannerError

# Project imports
from pydotfiles.v4.common import Configuration
from pydotfiles.v4.common import PydotfilesError
from pydotfiles.v4.validator import validate

logger = getLogger(__name__)

##
# Publicly accessible methods
##


def load_configuration(directory: Path) -> list[Configuration]:
    # Generates a set of files that we need to validate from a tree structure
    potential_configuration_files = __load_potential_configuration_files(directory)
    loaded_potential_configs = {config_file: __load_data_from_file(config_file) for config_file in potential_configuration_files}
    return validate(loaded_potential_configs)

##
# Helper methods
##


def __load_potential_configuration_files(directory: Path) -> set[Path]:
    potential_configuration_files = set()

    exclude = {".git"}
    for path_prefix, directory_names, file_names in os_walk(directory, topdown=True):
        # We want to exclude certain directories from our loading walk. For more
        # information, see https://stackoverflow.com/a/19859907
        directory_names[:] = [d for d in directory_names if d not in exclude]
        for file_name_path in file_names:
            if file_name_path.endswith(".json") or file_name_path.endswith(".yaml") or file_name_path.endswith(".yml"):
                potential_configuration_files.add(Path(os_path.join(path_prefix, file_name_path)))

    # for file in initial_files_to_validate:
    #     print(f"files to potentially load from: {file}")
    return potential_configuration_files


def __load_data_from_file(config_file: Path) -> Dict:
    """
    Loads a configuration file
    """
    try:
        with config_file.open('r') as config_fd:
            if str(config_file).endswith("json"):
                return json_load(config_fd)
            elif str(config_file).endswith("yaml") or str(config_file).endswith("yml"):
                try:
                    return yaml_load(config_fd, Loader)
                except (YAMLError, ScannerError) as e:
                    load_error = PydotfilesError.due_to_yaml_error()
                    load_error.context_map['file'] = str(config_file)
                    load_error.context_map['error'] = e
                    raise load_error from e
            else:
                load_error = PydotfilesError.due_to_unsupported_config_filetype()
                load_error.context_map['file'] = str(config_file)
                raise load_error
    except PydotfilesError as e:
        logger.error(e.help_message)
