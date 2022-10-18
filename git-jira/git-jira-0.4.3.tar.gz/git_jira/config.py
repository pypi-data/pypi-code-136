from pathlib import Path
import yaml
from git_jira.utils import singleton
CONFIG_FILE_PATH = Path(Path.home() / ".git-jira" / "config.yaml")


@singleton
class Config(object):
    def __init__(self, path=CONFIG_FILE_PATH):
        self.path = path

    def __getattr__(self, attr):
        self.load()
        return self.config.get(attr)

    def str_content(self, config):
        return yaml.dump(config, sort_keys=False)

    def load(self):
        """
        Load the CONFIG_FILE as a dictionary
        """
        if self.file_exists():
            with open(self.path, "r") as stream:
                config = yaml.safe_load(stream)
            self.config = config
        else:
            raise Exception("No config file found. Run git jira configure to generate.")

    def file_exists(self):
        """
        Test if the CONFIG_FILE_PATH exists
        """
        path = Path(self.path)
        return path.is_file()

    def change(self, new_config):
        self.config = new_config
        self.write()

    def write(self):
        """
        Write the config dictionary as a yaml in CONFIG_FILE_PATH
        """
        self.path.parent.mkdir(exist_ok=True, parents=True)
        with open(self.path, "w") as f:
            f.write(self.str_content(self.config))
        f.close()
