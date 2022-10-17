import logging
import os
import socket

import yaml
from jsonschema import validate

DEFAULT_CONFIG_PATH = f"{os.environ['HOME']}/.blam/agent.yml"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
CALCULATED_DEFAULTS = {
    "name": socket.gethostname(),
    "working_dir": os.getcwd(),
}


class AgentConf(dict):
    def __init__(self, **kwargs):
        self._validate_params(kwargs)
        super().__init__(**kwargs)

    def _validate_params(self, params):
        with open(f"{SCRIPT_DIR}/resources/agent.schema.yml") as f:
            self.conf_schema = yaml.safe_load(f)
        validate(params, self.conf_schema)

    def _get_value(self, prop, env_var=None):
        if env_var is not None and os.getenv(env_var) is not None:
            return os.getenv(env_var)
        return self.get(prop, self.get_default(prop))

    def get_default(self, prop):
        if (
            prop in self.conf_schema["properties"]
            and "default" in self.conf_schema["properties"][prop]
        ):
            return self.conf_schema["properties"][prop].get("default")
        elif prop in CALCULATED_DEFAULTS:
            return CALCULATED_DEFAULTS[prop]
        else:
            return None

    @property
    def name(self):
        return self._get_value("name")

    @property
    def working_dir(self):
        return self._get_value("working_dir", "AGENT_WORKING_DIR")

    @property
    def action_ids(self):
        return self._get_value("action_ids")

    @property
    def commands(self):
        return self._get_value("commands")

    @property
    def poll_interval(self):
        return self._get_value("poll_interval")

    @property
    def queue(self):
        return self._get_value("queue")

    def show_config(self):
        def format_array(arr):
            if len(arr):
                formatted_array = "\n"
                for item in arr:
                    formatted_array += f"        - {item} \n"
                return formatted_array
            else:
                return "[]"

        logging.info(
            f"""
Agent configuration:
    Name: {self.name}
    Working directory: {self.working_dir}
    Poll Interval: {self.poll_interval}
    Action IDs: {format_array(self.action_ids)}
    Commands: {format_array(self.commands)}
        """
        )

    def to_file(self, path=DEFAULT_CONFIG_PATH):
        with open(path, "w") as f:
            yaml.safe_dump(dict(self), f)

    @staticmethod
    def from_file(path=DEFAULT_CONFIG_PATH):
        with open(path) as f:
            conf = yaml.safe_load(f)
        return AgentConf(**conf)

    @staticmethod
    def interactive_create(write=False, config_path=DEFAULT_CONFIG_PATH):
        conf = AgentConf()
        for key in conf.conf_schema["properties"].keys():
            if conf.conf_schema["properties"][key].get("type") == "array":
                input_val = input(
                    f"{key} (seperate with commas if entering multiple): "
                )
                input_val = input_val.split(",")
            else:
                input_val = input(f"{key} [{conf.get_default(key)}]: ")
                if (
                    conf.conf_schema["properties"][key].get("type")
                    == "integer"
                ):
                    input_val = int(input_val)

            conf[key] = input_val if input_val else conf.get_default(key)
        if write:
            conf.to_file(config_path)
        return conf
