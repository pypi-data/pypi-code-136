"""Logging configuration

This module contains functions for setup logging with yaml file.
"""
import importlib.resources as pkg_resources
import logging
import logging.config
import os

import yaml
from tcd_pipeline import config as local_config


def config_logging(
  default_config: str = 'logging.yaml',
  default_level: int = logging.INFO,
  env_key: str = 'LOG_CFG') -> None:
    """Setup logging configuration from config file or dictionary file

    Ref https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19

    By default, this module will be loading resources/logging.yaml
    to config logging.

    This can be overwrite by environment variable LOG_CFG
    to config file (*.yaml)

    Parameters
    ----------
    default_config : str, optional
      Default internal yaml logging configuration. Default is logging.yaml
    default_level : int
      Default log level. Default value is "logging.INFO"
    env_key : str
      Environment variable name to logging configuration file (yaml)

    Returns
    -------
    None
    """

    # path = default_path
    # LOG_CFG is provided. Use user-defined configuration file
    path = os.getenv(env_key, None)
    if path:
        if os.path.exists(path):
            with open(path, 'rt', encoding="UTF-8") as config_file:
                try:
                    config = yaml.safe_load(config_file.read())
                    logging.config.dictConfig(config)
                except IOError as err:
                    print(err)
                    print(f"""Error in provided logging configuration [{path}].
                      Using default configs""")
                    logging.basicConfig(level=default_level)
        else:
            logging.basicConfig(level=default_level)
            print(f"""Failed to load configuration file {path}.
              Using default configs""")

    # LOG_CFG is not provided. Use default in package tcd_config.logging.yaml.
    else:
        try:
            pkg_resources.open_text(local_config, default_config)
            config = yaml.safe_load(pkg_resources.open_text(
              local_config, default_config))
            logging.config.dictConfig(config)
        except IOError as err:
            print(err)
            print(f"""Error in default configuration [{default_config}].
              Using default configs""")
            logging.basicConfig(level=default_level)

    return None
