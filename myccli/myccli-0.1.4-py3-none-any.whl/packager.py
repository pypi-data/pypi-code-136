import hashlib
import inspect
import os
import shutil
import tarfile
import tempfile
from dataclasses import dataclass
from typing import Optional

import toml

from myccli.platform import Platform, AWSLambdaPlatform, AWSECSPlatform
from myccli.poetry import PoetryDriver
import myc


@dataclass(unsafe_hash=True)
class PackagingConfig:
    root_dir: str
    """ The directory that contains the input that is to be packaged. """

    out_dir: str
    """ The directory to which packages are to be saved. """

    use_local_myc: bool = False
    """ If true, a local copy of the mycelium runtime package is stored together with the project. """

    myc_source_dir: Optional[str] = None
    """ If use_local_myc is true, this stores the path of the directory containing the mycelium package to copy. """


class Packager:
    def wrap_package(self, config: PackagingConfig):
        """ Packages a whole package. """
        raise NotImplementedError


class PackagerFactory:
    def __init__(self):
        self._by_cls = {}

    def create(self, cls, **kwargs):
        assert not kwargs  # TODO: support creation arguments (with proper memoization)
        assert issubclass(cls, Packager)

        existing = self._by_cls.get(cls)
        if existing is not None:
            return existing

        result = cls()
        self._by_cls[cls] = result
        return result

    def create_for_platform(self, platform: Platform):
        if isinstance(platform, AWSLambdaPlatform):
            return self.create(LambdaPackager)
        elif isinstance(platform, AWSECSPlatform):
            return self.create(ECSPackager)
        else:
            raise NotImplementedError


class LambdaPackager(Packager):
    """
    Packages applications to be deployed to AWS' lambda service.
    """
    def __init__(self):
        self._ready_full_packages = {}

    def _export_requirements(self, poetry: PoetryDriver):
        lines = poetry.export_requirements().splitlines()

        # remove editable mycelium package
        # TODO: maybe do something for any editable package
        lines = [x for x in lines if not x.startswith('myc @')]

        return '\n'.join(lines)

    def wrap_package(self, config: PackagingConfig):
        if config in self._ready_full_packages:
            # return already existing package if created in the past with same parameters
            return self._ready_full_packages[config]

        os.makedirs(config.out_dir, exist_ok=True)

        poetry = PoetryDriver(config.root_dir)

        # install dependencies in the target project's environment
        # TODO: maybe create new build environment?
        poetry.install_deps()
        build_env_path = poetry.env_path()

        # build sdist archive
        archive_path = poetry.build_sdist()
        sdist_name = poetry.root_sdist_dirname()

        # extract
        with tempfile.TemporaryDirectory() as tmpdir:
            # find root version
            with tarfile.open(archive_path) as f:
                f.extractall(path=tmpdir)

            # fix timestamps because tarfile omits them...
            for d, ds, fs in os.walk(tmpdir):
                for f in fs:
                    os.utime(os.path.join(d, f))

            # copy dependencies directly into zip
            base_dir = os.path.join(tmpdir, sdist_name)
            python_dirs = os.listdir(os.path.join(build_env_path, 'lib'))
            assert len(python_dirs) == 1
            site_packages_path = os.path.join(build_env_path, 'lib', python_dirs[0], 'site-packages')
            shutil.copytree(site_packages_path, base_dir, dirs_exist_ok=True)

            # add mycelium package directly into zip
            def ignore(_root, files):
                return [x for x in files if x.endswith('.pyc')]
            mycelium_path = os.path.dirname(inspect.getfile(myc))
            shutil.copytree(mycelium_path, os.path.join(base_dir, 'myc'), ignore=ignore)

            # repackage into .zip file with requirements.txt
            out_path = os.path.join(config.out_dir, sdist_name)
            shutil.make_archive(out_path, 'zip', base_dir)

            result = out_path + '.zip'
            self._ready_full_packages[config] = result
            return result


class ECSPackager(Packager):
    DOCKERFILE_TEMPLATE = r"""
FROM python:3.10

# install poetry
RUN apt-get update -y && \
    curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

# copy project files
WORKDIR /app
COPY . /app

# add uvicorn and install project dependencies
RUN poetry add uvicorn[standard] && \
    poetry install

ENTRYPOINT ["/root/.local/bin/poetry", "run", "--"]
    """

    def __init__(self):
        self._ready_full_packages = {}

    def _split_name_version(self, s: str):
        if '>=' in s:
            arg = '>='
        elif '<=' in s:
            arg = '<='
        elif '<' in s:
            arg = '<'
        else:
            raise NotImplementedError

        name, _, ver = s.partition(arg)
        return name.strip(), arg + ver.strip().strip('\'')

    def _get_pyproject_dependencies(self, proj, exclude=None):
        if 'tool' in proj and 'poetry' in proj['tool']:
            return proj['tool']['poetry']['dependencies']

        if 'dependencies' in proj['project']:
            deps = proj['project']['dependencies']
            assert isinstance(deps, list)
            result = dict(self._split_name_version(s) for s in deps)
            if exclude is not None:
                result = {k: v for k, v in result.items() if k not in exclude}

            return result

        raise NotImplementedError

    def _copy_poetry_dependencies(self, dst, src, exclude=None):
        dst_deps = dst['tool']['poetry']['dependencies']
        src_deps = self._get_pyproject_dependencies(src, exclude=exclude)
        for dep, version in src_deps.items():
            if dep not in dst_deps:
                dst_deps[dep] = version

    @staticmethod
    def _load_poetry_toml(project_path: str):
        this_pyproject_path = os.path.join(project_path, 'pyproject.toml')
        with open(this_pyproject_path, 'r') as f:
            return toml.load(f)

    def _remove_local_package(self, dst_project_path: str, package_name: str):
        this_pyproject = self._load_poetry_toml(dst_project_path)

        this_deps = this_pyproject['tool']['poetry']['dependencies']
        if package_name in this_deps:
            del this_deps[package_name]

        dev_deps = this_pyproject\
            .get('tool', {})\
            .get('poetry', {})\
            .get('group', {})\
            .get('dev', {})\
            .get('dependencies', {})
        if package_name in dev_deps:
            del dev_deps[package_name]

        with open(os.path.join(dst_project_path, 'pyproject.toml'), 'w') as f:
            toml.dump(this_pyproject, f)

    def _copy_local_package(self, dst_project_path: str, package_name: str, package_path: str, exclude_deps=None):
        """
        Copies a package and stores it locally in the target project's directory.
        :param dst_project_path: Where to copy the package into.
        :param package_name: The name of the package to copy.
        :param package_path: The path of the package to copy.
        """
        shutil.copytree(package_path, os.path.join(dst_project_path, package_name))

        this_pyproject = self._load_poetry_toml(dst_project_path)
        other_pyproject = self._load_poetry_toml(os.path.dirname(package_path))

        this_deps = this_pyproject['tool']['poetry']['dependencies']
        if package_name in this_deps:
            del this_deps[package_name]
        self._copy_poetry_dependencies(this_pyproject, other_pyproject, exclude=exclude_deps)

        with open(os.path.join(dst_project_path, 'pyproject.toml'), 'w') as f:
            toml.dump(this_pyproject, f)

    def _setup_mycelium_base(self, project_path: str):
        mycelium_path = os.path.dirname(inspect.getfile(myc))
        self._copy_local_package(project_path, 'myc', mycelium_path)

    def wrap_package(self, config: PackagingConfig):
        if config in self._ready_full_packages:
            return self._ready_full_packages[config]

        # create working directory
        work_hash = hashlib.sha1(config.root_dir.encode('utf-8')).hexdigest()[:8]
        work_dir = os.path.join(config.out_dir, os.path.basename(config.root_dir) + '-ecs-' + work_hash)
        if os.path.exists(work_dir):
            shutil.rmtree(work_dir)

        # copy source files
        def ignore(root, files):
            if root == config.root_dir:
                return ['poetry.lock', '.mycelium']

            if '.mycelium' == os.path.basename(root) or '/.mycelium/' in os.path.dirname(root):
                print('IG', files)
                return files

            return []
        shutil.copytree(config.root_dir, work_dir, ignore=ignore)

        # modify pyproject.toml and remove mycelium package from dependency list
        if config.use_local_myc:
            self._setup_mycelium_base(work_dir)

        self._remove_local_package(work_dir, 'myccli')

        # # FIXME: remove this (DEBUG)
        # self._copy_local_package(work_dir, 'uvicorn', '/home/jacob/Code/uvicorn/uvicorn', exclude_deps=['typing-extensions;python_version'])

        # create dockerfile
        with open(os.path.join(work_dir, 'Dockerfile'), 'w') as f:
            f.write(self.DOCKERFILE_TEMPLATE)

        self._ready_full_packages[config] = work_dir
        return work_dir
