# General imports
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum

# Project imports
from .os import OperatingSystem, OSName
from .action import ActionType
from .environment import Environment
from .default_settings import DefaultSettings
from .profiles import Profile


class Version(Enum):
    alpha = "alpha"


class Schema(Enum):
    core = "core"
    default_settings = "default_settings"
    developer_environments = "developer_environments"
    manifest = "manifest"


@dataclass(frozen=True, order=True)
class AlphaCommon:
    version: Version
    schema: Schema


@dataclass(frozen=True, order=True)
class AlphaCore(AlphaCommon):
    profile: str
    os: Optional[OperatingSystem]
    actions: list[ActionType]

    @staticmethod
    def from_dict(data: Dict) -> 'AlphaCore':
        return AlphaCore(
            version=data.get("version"),
            schema=data.get("schema"),
            profile=data.get("profile"),
            os=OperatingSystem.from_dict(data.get("os")),
            actions=ActionType.from_dict(data.get("actions", []))
        )

    def join_with_default_settings_data(self, additional_data: list[DefaultSettings]) -> 'AlphaCore':
        return AlphaCore(
            version=self.version,
            schema=self.schema,
            profile=self.profile,
            os=self.os.join_with_default_settings_data(additional_data),
            actions=self.actions,
        )


@dataclass(frozen=True, order=True)
class AlphaDefaultSettings(AlphaCommon):
    default_settings: list[DefaultSettings]

    @staticmethod
    def from_dict(data: Dict) -> 'AlphaDefaultSettings':
        return AlphaDefaultSettings(
            version=data.get("version"),
            schema=data.get("schema"),
            default_settings=DefaultSettings.from_dict(data.get("default_settings", []))
        )


@dataclass(frozen=True, order=True)
class AlphaDeveloperEnvironments(AlphaCommon):
    environments: list[Environment]
    profile: str

    @staticmethod
    def from_dict(data: Dict) -> 'AlphaDeveloperEnvironments':
        return AlphaDeveloperEnvironments(
            version=data.get("version"),
            schema=data.get("schema"),
            profile=data.get("profile"),
            environments=Environment.from_dict(data.get("environments", []))
        )


@dataclass(frozen=True, order=True)
class AlphaManifest(AlphaCommon):
    profiles: list[Profile]

    @staticmethod
    def from_dict(data: Dict) -> 'AlphaManifest':
        return AlphaManifest(
            version=data.get("version"),
            schema=data.get("schema"),
            profiles=Profile.from_dict(data.get("profiles"))
        )


def get_schema(schema: str) -> type:
    configuration_map: Dict[str, type] = {
        "core": AlphaCore,
        "default_settings": AlphaDefaultSettings,
        "developer_environments": AlphaDeveloperEnvironments,
        "manifest": AlphaManifest,
    }
    return configuration_map.get(schema)
