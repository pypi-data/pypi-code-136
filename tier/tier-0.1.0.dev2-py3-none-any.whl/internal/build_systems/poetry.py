# std
from __future__ import annotations
from typing import List, Optional as Opt

# internal
from tier.internal.build_systems.abstract_build_system import (
    AbstractBuildSystem,
    DependencyDef,
    DependenciesDef,
)


class Poetry(AbstractBuildSystem):

    def get_package_name(self) -> str:
        return self.config.get('tool.poetry.name')

    def get_version(self) -> str:
        return self.config.get('tool.poetry.version')

    def set_version(self, version: str):
        self.config.set('tool.poetry.version', version)

    def get_dependencies(self, group_name: Opt[str] = None) -> DependenciesDef:
        if group_name:
            return self.get_group_dependencies(group_name)
        else:
            return self.config.get('tool.poetry.dependencies', {})

    def set_dependency(
            self,
            dependency_name: str,
            dependency: DependencyDef,
            group_name: Opt[str] = None,
    ):
        if group_name:
            self.set_group_dependency(group_name, dependency_name, dependency)
        else:
            self.config.set(f'tool.poetry.dependencies.{dependency_name}', dependency)

    def get_group_names(self) -> List[str]:
        return list(self.config.get('tool.poetry.group', {}).keys())

    def get_group_dependencies(self, group_name: str) -> DependenciesDef:
        return self.config.get(['tool', 'poetry', 'group', group_name, 'dependencies'], {})

    def set_group_dependency(self, group_name: str, dependency_name: str, dependency: DependencyDef):
        self.config.set(['tool', 'poetry', 'group', group_name, 'dependencies', dependency_name], dependency)

    @classmethod
    def system_name(cls) -> str:
        return 'poetry'

    @classmethod
    def build_backend(cls) -> str:
        return 'poetry.core.masonry.api'
