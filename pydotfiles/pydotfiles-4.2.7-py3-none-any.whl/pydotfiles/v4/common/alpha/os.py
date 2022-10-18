# General imports
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict
from pathlib import Path

from .default_settings import DefaultSettings


class OSName(Enum):
    macos = "macos"
    linux = "linux"


class Shell(Enum):
    bash = "bash"
    zsh = "zsh"

    @staticmethod
    def get(name: Optional[str]) -> Optional['Shell']:
        if name is None:
            return None
        return Shell[name]


class PackageManager(Enum):
    brew = "brew"
    yum = "yum"
    apt = "apt"

    @staticmethod
    def get(name: Optional[str]) -> Optional['PackageManager']:
        if name is None:
            return None
        return PackageManager[name]


@dataclass(frozen=True, order=True)
class OperatingSystem:
    name: OSName
    shell: Optional[Shell]
    package_manager: Optional[PackageManager]
    packages: list[str]
    applications: list[str]
    default_dock: list[str]
    default_settings_files: list[Path]
    default_settings_data: list[DefaultSettings]

    @staticmethod
    def from_dict(data: Optional[Dict]) -> Optional['OperatingSystem']:
        if data is None:
            return None

        if data.get("default_settings_files") is None:
            default_settings_files = []
        else:
            default_settings_files = [Path(default_setting_file) for default_setting_file in data.get("default_settings_files")]

        return OperatingSystem(
            name=OSName[data.get("name")],
            shell=Shell.get(data.get("shell")),
            package_manager=PackageManager.get(data.get("package_manager")),
            packages=data.get("packages", []),
            applications=data.get("applications", []),
            default_dock=data.get("default_dock", []),
            default_settings_files=default_settings_files,
            default_settings_data=[],
        )

    def join_with_default_settings_data(self, additional_data: list[DefaultSettings]) -> 'OperatingSystem':
        return OperatingSystem(
            name=self.name,
            shell=self.shell,
            package_manager=self.package_manager,
            packages=self.packages,
            applications=self.applications,
            default_dock=self.default_dock,
            default_settings_files=self.default_settings_files,
            default_settings_data=additional_data,
        )

    def to_dict(self) -> Dict:
        return {
            "name": self.name.value,
            "shell": None if self.shell is None else self.shell.value,
            "package_manager": None if self.package_manager is None else self.package_manager.value,
            "packages": self.packages,
            "applications": self.applications,
            "default_dock": self.default_dock,
            "default_settings_files": [str(default_settings_file) for default_settings_file in self.default_settings_files],
        }
