import base64
import configparser
import os
from urllib.parse import urlparse

from gitlab import Gitlab


class GitProject:
    def __init__(self, token):
        self.path = GitProject.git_path()
        self.parse = GitProject.git_url_parse()
        self.branch = GitProject.get_branch()
        self.host = GitProject.git_host()
        self.url = GitProject.git_project_url()
        self.git_url = GitProject.git_url()
        self.path_with_namespace = self._get_path_with_namespace()
        self.token = token

        self._gitlab_project = None
        self._client = None
        self._master_branch = None

    @property
    def master_branch(self):
        if self._master_branch is None:
            self._master_branch = self._get_master_branch()
        return self._master_branch

    @property
    def gitlab_client(self):
        if self._client is None:
            self._client = self._get_git_client()
        return self._client

    @property
    def gitlab_project(self):
        if self._gitlab_project is None:
            self._gitlab_project = self._get_gitlab_project()
        return self._gitlab_project

    @staticmethod
    def get_branch():
        if os.getenv("CI_MERGE_REQUEST_SOURCE_BRANCH_NAME"):
            return os.getenv("CI_MERGE_REQUEST_SOURCE_BRANCH_NAME")
        if os.getenv("CI_BUILD_REF_NAME"):
            return os.getenv("CI_BUILD_REF_NAME")
        return open(os.path.join(GitProject.git_path(), 'HEAD'), 'r').read().split('heads/')[-1].strip()

    @staticmethod
    def git_path():
        if os.getenv("CI_PROJECT_DIR"):
            current_path = os.getenv('CI_PROJECT_DIR')
        else:
            current_path = os.path.abspath(os.getcwd())
        return os.path.join(current_path, '.git')

    @staticmethod
    def git_url_parse():
        config_path = os.path.join(GitProject.git_path(), 'config')
        config = configparser.ConfigParser()
        config.read(config_path)
        base_url = config.get('remote "origin"', "url")
        url = base_url.split("@", maxsplit=1)[-1] if '@' in base_url else base_url
        schema = 'http' if 'http://' in url else 'https://'
        url = url.replace("https://", "").replace("http://", "").replace(":", "/").replace(".git", '')
        parse = urlparse(f'{schema}' + url)
        return parse

    @staticmethod
    def git_host():
        return GitProject.git_url_parse().hostname

    @staticmethod
    def git_url():
        parse = GitProject.git_url_parse()
        return f'{parse.scheme}://{parse.hostname}'

    @staticmethod
    def git_project_url():
        parse = GitProject.git_url_parse()
        return f'{parse.scheme}://{parse.hostname}{parse.path}'

    def _get_master_branch(self):
        return self.gitlab_project.default_branch

    def _get_git_client(self):
        return Gitlab(GitProject.git_url(), private_token=self.token)

    def _get_path_with_namespace(self):
        return self.parse.path.replace(".git", "")[1:]

    def _get_gitlab_project(self):
        return self.gitlab_client.projects.get(self.path_with_namespace)

    def _find_git_file_id(self, file_name, branch):
        result = []
        for item in self.gitlab_project.repository_tree(ref=branch):
            if item['name'] == file_name:
                return item['id']
        return result

    def get_git_file_text(self, file_name, branch):
        ci_info = self.gitlab_project.repository_blob(
            self._find_git_file_id(branch=branch, file_name=file_name), branch=branch)
        content = base64.b64decode(ci_info['content'])
        return content.decode('utf8')
