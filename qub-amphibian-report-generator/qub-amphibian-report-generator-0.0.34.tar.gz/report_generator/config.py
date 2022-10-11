"""Module to load configuration data.

Functions:
    load_config:    Loads the configuration file
"""
import yaml


def load_config() -> dict:
    """Load data from config file.

    Loads data from the config.yaml file. If the
    file is not found a None value is returned.

    Returns:
        config (dict):      dict with config data in key,
                            value pairs.
    """
    config = None
    try:
        with open("config.yaml", "r", encoding="utf-8") as file:
            config = yaml.load(file, Loader=yaml.loader.SafeLoader)
        return config
    except FileNotFoundError:
        return config


def dump_config(settings: dict) -> None:
    """Dumps config settings to config file.

    Puts the contents of the settings dict into the settings
    config file.

    Args:
        settings (dict):    a dict containing config data in key,
                            value pairs.

    """
    with open("config.yaml", "w", encoding="utf-8") as file:
        yaml.dump(settings, file)
