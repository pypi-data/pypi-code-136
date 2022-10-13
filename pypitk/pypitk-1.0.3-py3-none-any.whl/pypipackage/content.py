from .commands import commands as _init_commands
from .templates import pyproject_toml as _pyproject_toml_template


class Content:

    def __init__(self, __config):
        self.config = __config

    @property
    def commands(self):
        return _init_commands(self.config)

    @property
    def _private_commands(self):
        return self.commands.private_commands

    @property
    def _public_commands(self):
        return self.commands.public_commands

    @property
    def pyproject_toml(self) -> str:
        result = _pyproject_toml_template
        for key, value in self.config.items():
            v = str(value).lower() if isinstance(value,bool) else value
            result = result.replace(f"*{key}*", v)
        return result

    @property
    def readme(self) -> str:
        name = str(self.config["package_name"]).title()
        description = str(self.config["package_description"])
        commands = "\n\n".join(self._public_commands)
        return f"## {name}\n\n## Description:\n#    {description}\n\n## Commands:\n\n{commands}\n"

    @property
    def private(self):
        commands = "\n\n".join(self._private_commands)
        return f"## Commands:\n\n {commands}"
