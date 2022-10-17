import os
from getpass import getpass

import yaml

DEFAULT_CONFIG_PATH = f"{os.environ['HOME']}/.blam/config.yml"
DEFAULT_BASE_URL = "https://api.blam.jaguar-ai.com"


class SdkConfig:
    def __init__(self, username, password, base_url=DEFAULT_BASE_URL):
        self.username = username
        self.password = password
        self.base_url = base_url

    def to_file(self, config_path=DEFAULT_CONFIG_PATH):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as f:
            yaml.dump(self.__dict__, f)

    @staticmethod
    def from_file(config_path=DEFAULT_CONFIG_PATH):
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return SdkConfig(
            config["username"], config["password"], config["base_url"]
        )

    @staticmethod
    def interactive_create(write=False, config_path=DEFAULT_CONFIG_PATH):
        username = input("Username: ")
        password = getpass("Password: ")
        config = SdkConfig(username, password)
        if write:
            config.to_file(config_path)
        return config
