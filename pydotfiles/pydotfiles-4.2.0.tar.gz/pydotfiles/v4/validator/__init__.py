# General imports
from typing import Dict, Any
from pathlib import Path
from logging import getLogger

# Project imports
from pydotfiles.v4.common import get_configuration_version
from pydotfiles.v4.common import Configuration
from pydotfiles.v4.common.alpha import AlphaCore, AlphaDefaultSettings, DefaultSettings
from pydotfiles.v4.validator.alpha import AlphaValidator

logger = getLogger(__name__)

##
# Public methods
##


def validate(raw_data: Dict) -> list[Configuration]:

    validated_data = {file_path: file_data for file_path, file_data in raw_data.items() if __validate_configuration(file_path, file_data)}
    mapped_data = [Configuration(file_path, __map_data(file_data)) for file_path, file_data in validated_data.items()]
    joined_data = __join_dev_data(mapped_data)
    # We want to join our default data files in the OperatingSystem object with the AlphaDevEnvironment object
    # for mapped_datum in mapped_data:
    #     print(f"--------------------------\n")
    #     print(f"The data is: {mapped_datum}")
    #     print(f"The raw data is: {dumps(validated_data.get(mapped_datum.file_path), indent=4, sort_keys=True)}")
    #     print(f"--------------------------\n")
    logger.debug("All valid config files loaded")
    return joined_data

##
# Helper methods
##


def __validate_configuration(file_path: Path, file_data: Dict) -> bool:
    validator = get_validator(file_data)
    return validator.validate(file_path, file_data)


def get_validator(data: dict):
    """
    We only support alpha for now
    """
    return AlphaValidator()


def __map_data(validated_data: Dict) -> Any:
    configuration_version_type = get_configuration_version(validated_data.get("version"), validated_data.get("schema"))
    return configuration_version_type.from_dict(validated_data)


def __join_dev_data(data: list[Configuration]) -> list[Configuration]:
    os_map: Dict[Path, AlphaCore] = {}
    dev_env_map: Dict[Path, AlphaDefaultSettings] = {}

    for datum in data:
        if isinstance(datum.data, AlphaCore) and datum.data.os is not None and len(datum.data.os.default_settings_files) > 0:
            os_map[datum.file_path] = datum.data
        elif isinstance(datum.data, AlphaDefaultSettings):
            dev_env_map[datum.file_path] = datum.data

    final_join_dev_data: list[Configuration] = []
    for datum in data:
        if dev_env_map.get(datum.file_path) is not None:
            # Skips over this config since it's taken care of in os
            continue
        if os_map.get(datum.file_path) is None:
            final_join_dev_data.append(datum)
        else:
            # Now needs to reform the AlphaCore object with the corresponding AlphaDefaultSettings
            final_join_dev_data.append(__join_dev_datum(datum, dev_env_map))
    return final_join_dev_data


def __join_dev_datum(datum: Configuration, dev_env_map: Dict[Path, AlphaDefaultSettings]) -> Configuration:
    data: AlphaCore = datum.data

    raw_additional_data: list[AlphaDefaultSettings] = []
    for default_settings_file_path in data.os.default_settings_files:
        if dev_env_map.get(datum.file_path.parent.joinpath(default_settings_file_path)) is None:
            logger.error(f"Unable to map {data.os.default_settings_files} to a loaded-in default settings object")
        else:
            raw_additional_data.append(dev_env_map.get(datum.file_path.parent.joinpath(default_settings_file_path)))

    additional_data: list[DefaultSettings] = []
    for raw_additional_datum in raw_additional_data:
        for default_settings in raw_additional_datum.default_settings:
            additional_data.append(default_settings)

    return Configuration(file_path=datum.file_path, data=data.join_with_default_settings_data(additional_data))
