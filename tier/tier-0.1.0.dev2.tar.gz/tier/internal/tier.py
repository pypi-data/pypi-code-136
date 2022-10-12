# std
from functools import lru_cache
import os
from typing import List, Optional as Opt

# internal
from tier.internal.commit_analyzer import CommitAnalyzer
from tier.internal.decorators import tag_implies_commit
from tier.internal.dependency_graph import DependencyGraph
from tier.internal.errors import expect, TierException
from tier.internal.git.git import Git
from tier.internal.logging import log
from tier.internal.configs.pyproject import PyProject
from tier.internal.versioning.bump_type import BumpType
from tier.internal.versioning.version import Version


class Tier:

    def __init__(self, dirpath: Opt[str] = None):
        self.dirpath = dirpath or os.getcwd()
        self.graph = DependencyGraph.create(self.dirpath)

    @lru_cache
    def projects(self) -> List[PyProject]:
        return [v.data for v in self.graph.depth_first_search()]

    def is_initialized(self) -> bool:
        return all(self.is_project_initialized(project) for project in self.projects())

    def initialize(self, commit: bool, tag: bool, commit_id: Opt[str] = None):
        for project in self.projects():
            log.info(f'Initializing {project.get_build_system().get_package_name()}')
            self.initialize_project(project=project, commit=commit, tag=tag, commit_id=commit_id)

    def bump(
            self,
            commit: bool = False,
            tag: bool = False,
            major: bool = False,
            minor: bool = False,
            patch: bool = False,
            post: bool = False,
            rc: bool = False,
            beta: bool = False,
            alpha: bool = False,
            dev: bool = False,
    ):
        for project in self.projects():
            log.info(f'Bumping {project.get_build_system().get_package_name()}')
            self.bump_project_from_options(
                project=project,
                commit=commit,
                tag=tag,
                major=major,
                minor=minor,
                patch=patch,
                post=post,
                rc=rc,
                beta=beta,
                alpha=alpha,
                dev=dev,
            )

    def update(
            self,
            commit: bool = False,
            tag: bool = False,
    ):
        for project in self.projects():
            log.info(f'Updating {project.get_build_system().get_package_name()}')
            self.sync_project(project=project, commit=commit)
            self.update_project(
                project=project,
                commit=commit,
                tag=tag,
            )

    def develop(self):
        project: PyProject
        for project in self.projects():
            self.develop_project(project)

    def develop_project(self, project: PyProject):
        self.develop_project_group(project)
        for group_name in project.get_build_system().get_group_names():
            self.develop_project_group(project, group_name)

    def develop_project_group(self, project: PyProject, group_name: Opt[str] = None):
        bs = project.get_build_system()
        package_name = bs.get_package_name()
        for dependency_name in self.graph.get_internal_dependency_names(package_name, group_name):
            dependency_project = self.graph.get_project(dependency_name)
            relpath = os.path.relpath(start=project.dirpath, path=dependency_project.dirpath)
            develop_dependency = {'develop': True, 'path': relpath}
            project.get_build_system().set_dependency(dependency_name, develop_dependency, group_name)

    def sync(self, commit: bool = False):
        project: PyProject
        for project in self.projects():
            self.sync_project(project, commit)

    def sync_project(self, project: PyProject, commit: bool = False):
        git = Git(project.dirpath)
        package_name = project.get_build_system().get_package_name()

        self.sync_project_group(project)
        for group_name in project.get_build_system().get_group_names():
            self.sync_project_group(project, group_name)

        if commit:
            git.check('add', project.filepath)
            if git.is_staged_changes(project.filepath):
                git.check('commit', '-m', f'patch({package_name}): sync internal dependencies')

    def sync_project_group(
            self,
            project: PyProject,
            group_name: Opt[str] = None,
            commit: bool = False,
    ):
        git = Git(project.dirpath)
        package_name = project.get_build_system().get_package_name()

        dependency_projects = self.graph.get_internal_dependency_projects(package_name, group_name)
        for dependency_project in dependency_projects:
            dependency_name = dependency_project.get_build_system().get_package_name()
            dependency_version = dependency_project.get_build_system().get_version()
            project.get_build_system().set_dependency(dependency_name, dependency_version, group_name)

        if commit:
            git.check('add', project.filepath)
            if git.is_staged_changes(project.filepath):
                git.check('commit', '-m', f'patch({package_name}): sync internal dependencies')

    @staticmethod
    def is_project_initialized(project: PyProject) -> bool:
        return project.exists() and project['tool.tier.commit-id'] is not None

    @staticmethod
    @tag_implies_commit
    def initialize_project(project: PyProject, commit: bool, tag: bool, commit_id: Opt[str] = None):
        git = Git(project.dirpath)
        commit_id = commit_id or git.latest_commit_id('.')
        log.info(f'Initializing Tier tool in {project.filepath} with commit id {commit_id}')
        Tier.set_project_commit_id(project, commit_id)

        bs = project.get_build_system()
        package_name = bs.get_package_name()

        if commit:
            git.check('add', project.filepath)
            if git.is_staged_changes(project.filepath):
                git.check('commit', '-m', f'chore({package_name}): initialize tier')

        if tag:
            git.check('tag', '-a', f'{package_name}-{bs.get_version()}', '-m', '""')

    @staticmethod
    def get_project_commit_id(project: PyProject) -> str:
        expect(Tier.is_project_initialized(project), 'Tier tool has not been initialized.')
        return project['tool.tier.commit-id']

    @staticmethod
    def set_project_commit_id(project: PyProject, commit_id: str):
        project['tool.tier.commit-id'] = commit_id

    @staticmethod
    def bump_project_from_options(
            project: PyProject,
            commit: bool = False,
            tag: bool = False,
            major: bool = False,
            minor: bool = False,
            patch: bool = False,
            post: bool = False,
            rc: bool = False,
            beta: bool = False,
            alpha: bool = False,
            dev: bool = False,
    ):
        expect(Tier.is_project_initialized(project), 'Tier tool has not been initialized.')
        if tag:
            commit = True

        log.debug(f'{commit = }')
        log.debug(f'{tag = }')

        bump_type = BumpType.from_options(
            major=major,
            minor=minor,
            patch=patch,
            post=post,
            rc=rc,
            beta=beta,
            alpha=alpha,
            dev=dev,
        )
        Tier.bump_project(project=project, bump_type=bump_type, commit=commit, tag=tag)

    @staticmethod
    @tag_implies_commit
    def bump_project(
            *,
            project: PyProject,
            bump_type: BumpType,
            commit: bool = False,
            tag: bool = False,
    ):
        log.debug(f'Bump type: {bump_type}')
        if bump_type is BumpType.NULL:
            return

        bs = project.get_build_system()
        git = Git(project.dirpath)

        current = Version.from_str(bs.get_version())
        log.info(f'Current version: {current}')

        bumped = current.bump(bump_type)
        log.info(f'Bumped version: {bumped}')

        bs.set_version(bumped.str())

        Tier.set_project_commit_id(project, git.latest_commit_id('.'))

        package_name = bs.get_package_name()
        if commit:
            git.check('add', project.filepath)
            if git.is_staged_changes(project.filepath):
                git.check('commit', '-m', f'chore({package_name}): release {bumped}')

        if tag:
            git.check('tag', '-a', f'{package_name}-{bumped}', '-m', '""')

    @staticmethod
    def update_project(
            project: PyProject,
            commit: bool = False,
            tag: bool = False,
    ):
        git = Git(project.dirpath)
        previous_commit_id = Tier.get_project_commit_id(project)

        commits = git.commits(previous_commit_id, path=project.dirpath)
        analyzer = CommitAnalyzer()
        bump_type = analyzer.analyze_commits(*commits)
        Tier.bump_project(project=project, bump_type=bump_type, commit=commit, tag=tag)
