import configparser
import shutil
import yaml
import os
from typing import Dict


def copy_config_files_to_output(config_dir: str, output_dir: str):
    shutil.copy(config_dir, output_dir)


def load_yaml(filename) -> Dict:
    with open(filename) as f:
        return yaml.safe_load(f)


def load_cfg_config(config_dir: str, filename: str) -> configparser.RawConfigParser:
    config = configparser.RawConfigParser()
    config.read(os.path.join(config_dir, filename))
    return config
