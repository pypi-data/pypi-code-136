import os
import subprocess

import toml


class NotPoetryProjectError(Exception):
    pass


class PoetryDriver:
    def __init__(self, work_dir: str):
        self._work_dir = work_dir
        self._project_toml = self._load_toml()

    def _load_toml(self):
        toml_path = os.path.join(self._work_dir, 'pyproject.toml')
        if not os.path.exists(toml_path):
            raise NotPoetryProjectError('pyproject.toml not found')

        with open(toml_path) as f:
            result = toml.load(f)

        if 'tool' not in result or 'poetry' not in result['tool']:
            raise NotPoetryProjectError('pyproject.toml is not configured with poetry')

        return result

    def root_sdist_dirname(self) -> str:
        """ Returns the name of the top-level directory of an sdist archive for this project. """
        name = self._project_toml['tool']['poetry']['name']
        version = self._project_toml['tool']['poetry']['version']
        return f'{name}-{version}'

    def build_sdist(self):
        """
        Builds the project in the configured working directory.
        Returns the path of the resulting sdist .tar.gz archive.
        """
        subprocess.check_call(
            'poetry build --format=sdist',
            cwd=self._work_dir, shell=True, stdout=subprocess.DEVNULL
        )

        # find resulting .tar.gz archive
        dist_folder = os.path.join(self._work_dir, 'dist')
        project_name = self._project_toml['tool']['poetry']['name']
        archives = [entry for entry in os.listdir(dist_folder) if
                    entry.endswith('.tar.gz') and entry.startswith(project_name)]
        assert len(archives) == 1, 'More than one archive created during build process'
        return os.path.join(dist_folder, archives[0])

    def export_requirements(self):
        """ Creates a requirements.txt file from a poetry project. """
        return subprocess.check_output(
            'poetry export --without-hashes --format=requirements.txt',
            cwd=self._work_dir, shell=True, encoding='utf-8'
        )

    def env_path(self):
        return subprocess.check_output('poetry env info -p', cwd=self._work_dir, shell=True, encoding='utf-8').strip()

    def install_deps(self):
        return subprocess.check_call(
            'poetry install --no-root',
            cwd=self._work_dir, shell=True, encoding='utf-8',
            stdout=subprocess.DEVNULL
        )
