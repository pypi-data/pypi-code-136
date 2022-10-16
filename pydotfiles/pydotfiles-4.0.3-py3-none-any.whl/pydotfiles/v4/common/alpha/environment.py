# General imports
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict


class DevLanguage(Enum):
    python = "python"
    ruby = "ruby"
    golang = "golang"
    java = "java"
    rust = "rust"


@dataclass(frozen=True, order=True)
class VirtualEnvironment:
    version: str
    name: str

    @staticmethod
    def from_dict(data: Dict) -> 'VirtualEnvironment':
        return VirtualEnvironment(
            version=data.get("version"),
            name=data.get("name")
        )


@dataclass(frozen=True, order=True)
class Plugin:
    name: str
    virtual_environments: list[VirtualEnvironment]

    @staticmethod
    def from_dict(data: Dict) -> 'Plugin':
        virtual_environments = [VirtualEnvironment.from_dict(virtual_environment) for virtual_environment in data.get("virtual_environments")]
        return Plugin(
            name=data.get("name"),
            virtual_environments=virtual_environments
        )


@dataclass(frozen=True, order=True)
class EnvironmentManager:
    name: str
    plugins: list[Plugin]

    @staticmethod
    def from_dict(data: Optional[Dict]) -> Optional['EnvironmentManager']:
        if data is None:
            return None

        plugins = [] if data.get("plugins") is None else [Plugin.from_dict(plugin) for plugin in data.get("plugins")]
        return EnvironmentManager(
            name=data.get("name"),
            plugins=plugins
        )


@dataclass(frozen=True, order=True)
class Environment:
    language: DevLanguage
    versions: list[str]
    environment_manager: Optional[EnvironmentManager]

    @staticmethod
    def from_dict(data: list[Dict]) -> list['Environment']:
        return [Environment.from_environment_dict(datum) for datum in data]

    @staticmethod
    def from_environment_dict(data: Dict) -> 'Environment':
        return Environment(
            language=DevLanguage[data.get("language")],
            versions=data.get("versions"),
            environment_manager=EnvironmentManager.from_dict(data.get("environment_manager"))
        )
