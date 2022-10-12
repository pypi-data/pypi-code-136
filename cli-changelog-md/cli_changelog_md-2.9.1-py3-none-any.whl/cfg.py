import configparser
import os
from pathlib import Path
from urllib.parse import urlparse

from cli_changelog_md.exception import GitLabLoginException
from cli_changelog_md.git import GitProject


class Config:
    HOME_DIR = os.path.join(str(Path.home()), '.changelog-md')
    PROFILE_PATH = os.path.join(HOME_DIR, 'changelog-md.cfg')

    def __init__(self, path, git_token=None):
        self.path = Path(path)

        self.config: configparser.ConfigParser = configparser.ConfigParser()
        self.config.read(path)

        self.git_project = GitProject(token=git_token if git_token else self._get_git_token())

        if not os.path.exists(Config.HOME_DIR):
            self.create_profile_path()

        if not os.path.exists(Config.PROFILE_PATH):
            self.create_empty_cfg()

    def add_gitlab_login(self, host, token):
        if not self.config.has_section("GITLAB"):
            self.config['GITLAB'] = {}
        self.config['GITLAB'].update({urlparse(host).hostname: token})

    @staticmethod
    def create_profile_path():
        os.mkdir(Config.HOME_DIR)

    @staticmethod
    def create_empty_cfg():
        with open(Config.PROFILE_PATH, 'w', encoding='UTF8'):
            pass

    @classmethod
    def load(cls, git_token: str = None, path: str = PROFILE_PATH):
        obj = cls(path=path, git_token=git_token)
        return obj

    def save_config(self):
        with open(Config.PROFILE_PATH, 'w') as configfile:
            self.config.write(configfile)

    def _get_git_token(self):
        if self.config.has_option(section="GITLAB", option=GitProject.git_host()):
            return self.config.get(section="GITLAB", option=GitProject.git_host())
        else:
            raise GitLabLoginException(
                f"You need login to git server {GitProject.git_project_url()}. Use git-login command!")
