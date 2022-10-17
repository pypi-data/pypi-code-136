# General imports
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict
from distutils.version import StrictVersion
from functools import total_ordering


@total_ordering
class MacVersion(Enum):

    YOSEMITE = StrictVersion("10.10")

    EL_CAPITAN = StrictVersion("10.11")

    SIERRA = StrictVersion("10.12")

    HIGH_SIERRA = StrictVersion("10.13")

    MOJAVE = StrictVersion("10.14")

    CATALINA = StrictVersion("10.15")

    BIG_SUR = StrictVersion("11.0")

    MONTEREY = StrictVersion("12.0")

    VENTURA = StrictVersion("13.0")

    @staticmethod
    def from_version(version: str | StrictVersion):
        if version is None:
            raise ValueError("MacVersion: Can't identify none version number")

        if isinstance(version, str):
            version = StrictVersion(version)

        major_version = version.version[0]
        minor_version = version.version[1]

        if major_version < 11:
            truncated_version = StrictVersion(f"{major_version}.{minor_version}")
        else:
            truncated_version = StrictVersion(f"{major_version}.0")
        return MacVersion(truncated_version)

    @staticmethod
    def from_name(name: str) -> Optional['MacVersion']:
        if name is None:
            return None
        return MacVersion[name.upper()]

    def __lt__(self, other):
        return self.value < other.value


class VersionRange:

    def __init__(self, start: Optional[MacVersion] | Optional[StrictVersion] = None, end: Optional[MacVersion] | Optional[StrictVersion] = None):
        """
        A None start is taken to be the equivalent
        of "since the beginning of time"

        A None end is taken to be the equivalent of
        "currently supported"
        """

        if start is not None and not isinstance(start, StrictVersion) and not isinstance(start, MacVersion):
            raise ValueError(f"Unable to create a version range, passed in type for start was invalid [start={type(start)}], should have been a StrictVersion")

        if end is not None and not isinstance(end, StrictVersion) and not isinstance(start, MacVersion):
            raise ValueError(f"Unable to create a version range, passed in type for start was invalid [end={type(start)}], should have been a StrictVersion")

        self.start = start
        self.end = end

    def __str__(self):
        return f"VersionRange(start={self.start}, end={self.end})"

    def is_in_range(self, current_version: StrictVersion | MacVersion):
        # Infinite range case
        if self.start is None and self.end is None:
            return True

        if self.start is None and self.end is not None:
            return current_version <= self.end

        if self.start is not None and self.end is None:
            return self.start <= current_version

        # For somebody who likes to keep their books clean
        return self.start <= current_version <= self.end


@dataclass(frozen=True, order=True)
class DefaultSettings:
    name: str
    enabled: bool
    description: Optional[str]
    command: str
    start: Optional[MacVersion]
    end: Optional[MacVersion]
    check_command: Optional[str]
    expected_check_state: Optional[str]
    sudo: bool
    check_output: bool
    post_command: Optional[str]

    @staticmethod
    def from_dict(data: list[Dict]) -> list['DefaultSettings']:
        return [DefaultSettings.from_default_setting_dict(datum) for datum in data]

    @staticmethod
    def from_default_setting_dict(data: Dict) -> 'DefaultSettings':
        return DefaultSettings(
            name=data.get("name"),
            enabled=True if data.get("enabled") is None else data.get("enabled"),
            description=data.get("description"),
            command=data.get("command"),
            start=MacVersion.from_name(data.get("start")),
            end=MacVersion.from_name(data.get("end")),
            check_command=data.get("check_command"),
            expected_check_state=data.get("expected_check_state"),
            sudo=False if data.get("sudo") is None else data.get("sudo"),
            check_output=True if data.get("check_output") is None else data.get("check_output"),
            post_command=data.get("post_command"),
        )

    @property
    def version_range(self) -> VersionRange:
        return VersionRange(self.start, self.end)

    def should_run(self, current_version: StrictVersion | MacVersion) -> bool:
        if not self.enabled:
            return False

        if not self.version_range.is_in_range(current_version):
            return False

        if self.check_command is None:
            return True
        return True
