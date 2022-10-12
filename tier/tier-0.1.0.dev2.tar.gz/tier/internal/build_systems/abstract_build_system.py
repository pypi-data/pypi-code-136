# std
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional as Opt, Union

# internal
from tier.internal.configs.abstract_config import SubConfig

# types
from tier.internal.types import Data

DependencyDef = Union[str, Dict[str, str]]
DependenciesDef = Dict[str, DependencyDef]


class AbstractBuildSystem(ABC):

    def __init__(self, config: SubConfig):
        self.config: SubConfig = config

    @abstractmethod
    def get_package_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_version(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def set_version(self, version: str):
        raise NotImplementedError

    @abstractmethod
    def get_dependencies(self, group_name: Opt[str] = None) -> DependenciesDef:
        raise NotImplementedError

    def get_dependency(self, dependency_name: str, group_name: Opt[str] = None) -> DependencyDef:
        return self.get_dependencies(group_name)[dependency_name]

    def get_dependency_objects(self, group_name: Opt[str] = None) -> List[Dependency]:
        return [Dependency(name, self, group_name) for name in self.get_dependencies(group_name)]

    def get_dependency_obj(self, dependency_name: str, group_name: Opt[str] = None) -> Dependency:
        return Dependency(dependency_name, self, group_name)

    @abstractmethod
    def set_dependency(self, dependency_name: str, dependency: DependencyDef, group_name: Opt[str] = None):
        raise NotImplementedError

    @abstractmethod
    def get_group_names(self) -> List[str]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def system_name(cls) -> str:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def build_backend(cls) -> str:
        raise NotImplementedError


class Dependency:

    def __init__(self, name: str, build_system: AbstractBuildSystem, group_name: Opt[str] = None):
        self.name = name
        self.build_system = build_system
        self.group_name = group_name

    def get(self) -> Data:
        return self.build_system.get_dependency(self.name, self.group_name)

    def set(self, value: Data):
        self.build_system.set_dependency(self.name, value, self.group_name)
