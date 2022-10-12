import configparser
import os
from pathlib import Path
from typing import List


class ConfigFiles:
    root_folder = os.getcwd()
    apps_folder = Path(__file__).parent.resolve()
    base_config_parser = configparser.ConfigParser()
    settings_name = "bfet"
    settings_file = "setup.cfg"
    default_file_namig = "test_*"
    default_class_naming = "Test*"
    default_function_namig = "test_*"

    default_files_to_include = "forms,views,managers,models,urls,admin"
    default_files_to_exclude = ""

    def __init__(self) -> None:
        try:
            self.base_config_parser.read(self.settings_file)
            self.config_parser = self.base_config_parser[self.settings_name]
        except KeyError:
            # TODO raise and exception or advice the user to create or allow the automatic creation
            # of the setup.cfg settings for bfet
            return
        else:
            self.files_to_include = self.get_files_to("include", self.default_files_to_include)
            self.file_namig = self.config_parser.get("file_namig", self.default_file_namig)
            self.class_naming = self.config_parser.get("class_naming", self.default_class_naming)
            self.function_namig = self.config_parser.get(
                "function_namig", self.default_function_namig
            )
            self.files_to_exclude = self.get_files_to("exclude", self.default_files_to_exclude)

    def get_files_to(self, what_to_do: str, default: str) -> List:
        files_to = self.config_parser.get(what_to_do, default)
        return [file.strip() for file in files_to.split(",")]

    def create_config_settings(self):
        if self.settings_file not in os.listdir(self.root_folder):
            with open(f"{self.root_folder}/{self.settings_file}", "w") as f:
                f.close()
        self.base_config_parser.read(self.settings_file)
        sections = self.base_config_parser.sections()
        if self.settings_name not in sections:
            self.base_config_parser[self.settings_name] = {
                # "django_settings_module": django_settings_module,
                # "django_local_apps": ",".join(django_local_apps)
                "file_namig": self.default_file_namig,
                "class_naming": self.default_class_naming,
                "function_namig": self.default_function_namig,
                "include": self.default_files_to_include,
                "exclude": self.default_files_to_exclude,
            }
            with open(self.settings_file, "w") as conf:
                self.base_config_parser.write(conf)
