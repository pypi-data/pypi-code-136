# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (interface definition through abstract
# class).
#
# This file is part of Hydrilla&Haketilo.
#
# Copyright (C) 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

"""
This module defines API for keeping track of all settings, rules, mappings and
resources.
"""

import dataclasses as dc
import typing as t

from pathlib import Path
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

from immutables import Map

from ..exceptions import HaketiloException
from ..versions import VerTuple
from ..url_patterns import ParsedPattern
from .. import item_infos
from .simple_dependency_satisfying import ImpossibleSituation


class EnabledStatus(Enum):
    """
    ENABLED - User wished to always apply given mapping when it matches site's
        URL.

    DISABLED - User wished to never apply given mapping.

    NO_MARK - User has not configured given mapping.
    """
    ENABLED  = 'E'
    DISABLED = 'D'
    NO_MARK  = 'N'


class FrozenStatus(Enum):
    """
    EXACT_VERSION - User wished to always use the same version of a mapping.

    REPOSITORY - User wished to always use a version of the mapping from the
        same repository.

    NOT_FROZEN - User did not restrict updates of the mapping.
    """
    EXACT_VERSION = 'E'
    REPOSITORY    = 'R'
    NOT_FROZEN    = 'N'

    @staticmethod
    def make(letter: t.Optional[str]) -> t.Optional['FrozenStatus']:
        if letter is None:
            return None

        return FrozenStatus(letter)


class InstalledStatus(Enum):
    """
    INSTALLED - Mapping's all files are present and mapping data is not going to
        be automatically removed.

    NOT_INSTALLED - Some of the mapping's files might be absent. Mapping can be
        automatically removed if it is orphaned.

    FAILED_TO_INSTALL - Same as "NOT_INSTALLED" but we additionally know that
        the last automatic attempt to install mapping's files from repository
        was unsuccessful.
    """
    INSTALLED         = 'I'
    NOT_INSTALLED     = 'N'
    FAILED_TO_INSTALL = 'F'


class ActiveStatus(Enum):
    """
    REQUIRED - Mapping version got active to fulfill a requirement of some (this
        or another) explicitly enabled mapping.

    AUTO - Mapping version was activated automatically.

    NOT_ACTIVE - Mapping version is not currently being used.
    """
    REQUIRED   = 'R'
    AUTO       = 'A'
    NOT_ACTIVE = 'N'


@dc.dataclass(frozen=True, unsafe_hash=True)
class Ref:
    """...."""
    id: str

    def __post_init__(self):
        assert isinstance(self.id, str)


RefType = t.TypeVar('RefType', bound=Ref)

class Store(ABC, t.Generic[RefType]):
    @abstractmethod
    def get(self, id) -> RefType:
        ...


class RulePatternInvalid(HaketiloException):
    pass

@dc.dataclass(frozen=True)
class RuleDisplayInfo:
    ref:           'RuleRef'
    pattern:       str
    allow_scripts: bool

# mypy needs to be corrected:
# https://stackoverflow.com/questions/70999513/conflict-between-mix-ins-for-abstract-dataclasses/70999704#70999704
@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RuleRef(Ref):
    @abstractmethod
    def remove(self) -> None:
        ...

    @abstractmethod
    def update(
            self,
            *,
            pattern: t.Optional[str] = None,
            allow: t.Optional[bool] = None
    ) -> None:
        ...

    @abstractmethod
    def get_display_info(self) -> RuleDisplayInfo:
        ...

class RuleStore(Store[RuleRef]):
    @abstractmethod
    def get_display_infos(self, allow: t.Optional[bool] = None) \
        -> t.Sequence[RuleDisplayInfo]:
        ...

    @abstractmethod
    def add(self, pattern: str, allow: bool) -> RuleRef:
        ...


class RepoNameInvalid(HaketiloException):
    pass

class RepoNameTaken(HaketiloException):
    pass

class RepoUrlInvalid(HaketiloException):
    pass

class RepoCommunicationError(HaketiloException):
    pass

@dc.dataclass(frozen=True)
class FileInstallationError(HaketiloException):
    repo_id: str
    sha256:  str

@dc.dataclass(frozen=True)
class FileIntegrityError(FileInstallationError):
    invalid_sha256: str

@dc.dataclass(frozen=True)
class FileMissingError(FileInstallationError):
    pass

class RepoApiVersionUnsupported(HaketiloException):
    pass

@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RepoRef(Ref):
    """...."""
    @abstractmethod
    def remove(self) -> None:
        """...."""
        ...

    @abstractmethod
    def update(
            self,
            *,
            name: t.Optional[str] = None,
            url:  t.Optional[str] = None
    ) -> None:
        """...."""
        ...

    @abstractmethod
    def refresh(self) -> None:
        """...."""
        ...

    @abstractmethod
    def get_display_info(self) -> 'RepoDisplayInfo':
        ...

@dc.dataclass(frozen=True)
class RepoDisplayInfo:
    ref:               RepoRef
    is_local_semirepo: bool
    name:              str
    url:               str
    deleted:           bool
    last_refreshed:    t.Optional[datetime]
    resource_count:    int
    mapping_count:     int

class RepoStore(Store[RepoRef]):
    @abstractmethod
    def get_display_infos(self, include_deleted: bool = False) -> \
        t.Sequence[RepoDisplayInfo]:
        ...

    @abstractmethod
    def add(self, name: str, url: str) -> RepoRef:
        ...


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class RepoIterationRef(Ref):
    """...."""
    pass


@dc.dataclass(frozen=True)
class FileData:
    mime_type: str
    name:      str
    contents:  bytes


@dc.dataclass(frozen=True)
class MappingDisplayInfo(item_infos.CorrespondsToMappingDCMixin):
    ref:            'MappingRef'
    identifier:     str
    enabled:        EnabledStatus
    frozen:         t.Optional[FrozenStatus]
    active_version: t.Optional['MappingVersionDisplayInfo']

@dc.dataclass(frozen=True)
class RichMappingDisplayInfo(MappingDisplayInfo):
    all_versions: t.Sequence['MappingVersionDisplayInfo']

@dc.dataclass(frozen=True)
class MappingVersionDisplayInfo(item_infos.CorrespondsToMappingDCMixin):
    ref:             'MappingVersionRef'
    info:            item_infos.MappingInfo
    installed:       InstalledStatus
    active:          ActiveStatus
    is_orphan:       bool
    is_local:        bool

@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class MappingRef(Ref, item_infos.CorrespondsToMappingDCMixin):
    """...."""
    @abstractmethod
    def update_status(
            self,
            enabled: EnabledStatus,
            frozen:  t.Optional[FrozenStatus] = None
    ) -> None:
        ...

    @abstractmethod
    def get_display_info(self) -> RichMappingDisplayInfo:
        ...


class MappingStore(Store[MappingRef]):
    @abstractmethod
    def get_display_infos(self) -> t.Sequence[MappingDisplayInfo]:
        ...

    @abstractmethod
    def get_by_identifier(self, identifier: str) -> MappingRef:
        ...

@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class MappingVersionRef(Ref, item_infos.CorrespondsToMappingDCMixin):
    @abstractmethod
    def install(self) -> None:
        ...

    @abstractmethod
    def uninstall(self) -> t.Optional['MappingVersionRef']:
        ...

    @abstractmethod
    def ensure_depended_items_installed(self) -> None:
        ...

    @abstractmethod
    def update_mapping_status(
            self,
            enabled: EnabledStatus,
            frozen:  t.Optional[FrozenStatus] = None
    ) -> None:
        ...

    @abstractmethod
    def get_license_file(self, name: str) -> FileData:
        ...

    @abstractmethod
    def get_upstream_license_file_url(self, name: str) -> str:
        ...

    @abstractmethod
    def get_required_mapping(self, identifier: str) -> 'MappingVersionRef':
        ...

    @abstractmethod
    def get_payload_resource(self, pattern: str, identifier: str) \
        -> 'ResourceVersionRef':
        ...

    @abstractmethod
    def get_item_display_info(self) -> RichMappingDisplayInfo:
        ...

class MappingVersionStore(Store[MappingVersionRef]):
    pass


@dc.dataclass(frozen=True)
class ResourceDisplayInfo(item_infos.CorrespondsToResourceDCMixin):
    ref:            'ResourceRef'
    identifier:     str

@dc.dataclass(frozen=True)
class RichResourceDisplayInfo(ResourceDisplayInfo):
    all_versions: t.Sequence['ResourceVersionDisplayInfo']

@dc.dataclass(frozen=True)
class ResourceVersionDisplayInfo(item_infos.CorrespondsToResourceDCMixin):
    ref:             'ResourceVersionRef'
    info:            item_infos.ResourceInfo
    installed:       InstalledStatus
    active:          ActiveStatus
    is_orphan:       bool
    is_local:        bool

@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class ResourceRef(Ref, item_infos.CorrespondsToResourceDCMixin):
    @abstractmethod
    def get_display_info(self) -> RichResourceDisplayInfo:
        ...

class ResourceStore(Store[ResourceRef]):
    @abstractmethod
    def get_display_infos(self) -> t.Sequence[ResourceDisplayInfo]:
        ...

    @abstractmethod
    def get_by_identifier(self, identifier: str) -> ResourceRef:
        ...


@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class ResourceVersionRef(Ref, item_infos.CorrespondsToResourceDCMixin):
    @abstractmethod
    def install(self) -> None:
        ...

    @abstractmethod
    def uninstall(self) -> t.Optional['ResourceVersionRef']:
        ...

    @abstractmethod
    def get_license_file(self, name: str) -> FileData:
        ...

    @abstractmethod
    def get_resource_file(self, name: str) -> FileData:
        ...

    @abstractmethod
    def get_upstream_license_file_url(self, name: str) -> str:
        ...

    @abstractmethod
    def get_upstream_resource_file_url(self, name: str) -> str:
        ...

    @abstractmethod
    def get_dependency(self, identifier: str) -> 'ResourceVersionRef':
        ...

    @abstractmethod
    def get_item_display_info(self) -> RichResourceDisplayInfo:
        ...

class ResourceVersionStore(Store[ResourceVersionRef]):
    pass


@dc.dataclass(frozen=True)
class PayloadKey:
    """...."""
    ref: 'PayloadRef'

    mapping_identifier: str

    def __lt__(self, other: 'PayloadKey') -> bool:
        """...."""
        return self.mapping_identifier < other.mapping_identifier

@dc.dataclass(frozen=True)
class PayloadData:
    """...."""
    ref: 'PayloadRef'

    explicitly_enabled:    bool
    unique_token:          str
    pattern_path_segments: tuple[str, ...]
    eval_allowed:          bool
    cors_bypass_allowed:   bool
    global_secret:         bytes

@dc.dataclass(frozen=True)
class PayloadDisplayInfo:
    ref: 'PayloadRef'

    mapping_info: MappingVersionDisplayInfo
    pattern:      str
    has_problems: bool

@dc.dataclass(frozen=True, unsafe_hash=True) # type: ignore[misc]
class PayloadRef(Ref):
    """...."""
    @abstractmethod
    def get_data(self) -> PayloadData:
        """...."""
        ...

    @abstractmethod
    def has_problems(self) -> bool:
        ...

    @abstractmethod
    def get_display_info(self) -> PayloadDisplayInfo:
        ...

    @abstractmethod
    def ensure_items_installed(self) -> None:
        """...."""
        ...

    @abstractmethod
    def get_script_paths(self) \
        -> t.Iterable[t.Sequence[str]]:
        """...."""
        ...

    @abstractmethod
    def get_file_data(self, path: t.Sequence[str]) \
        -> t.Optional[FileData]:
        """...."""
        ...

class PayloadStore(Store[PayloadRef]):
    pass


class MappingUseMode(Enum):
    """
    AUTO - Apply mappings except for those explicitly disabled.

    WHEN_ENABLED - Only apply mappings explicitly marked as enabled. Don't apply
        unmarked nor explicitly disabled mappings.

    QUESTION - Automatically apply mappings that are explicitly enabled. Ask
        whether to enable unmarked mappings. Don't apply explicitly disabled
        ones.
    """
    AUTO         = 'A'
    WHEN_ENABLED = 'W'
    QUESTION     = 'Q'


@dc.dataclass(frozen=True)
class HaketiloGlobalSettings:
    """...."""
    mapping_use_mode:      MappingUseMode
    default_allow_scripts: bool
    advanced_user:         bool
    repo_refresh_seconds:  int


class MissingItemError(ValueError):
    """...."""
    pass


@dc.dataclass(frozen=True)
class OrphanItemsStats:
    mappings:  int
    resources: int


class HaketiloState(ABC):
    """...."""
    @abstractmethod
    def import_items(self, malcontent_path: Path) -> None:
        ...

    @abstractmethod
    def count_orphan_items(self) -> OrphanItemsStats:
        ...

    @abstractmethod
    def prune_orphan_items(self) -> None:
        ...

    @abstractmethod
    def rule_store(self) -> RuleStore:
        ...

    @abstractmethod
    def repo_store(self) -> RepoStore:
        """...."""
        ...

    @abstractmethod
    def mapping_store(self) -> MappingStore:
        ...

    @abstractmethod
    def mapping_version_store(self) -> MappingVersionStore:
        ...

    @abstractmethod
    def resource_store(self) -> ResourceStore:
        ...

    @abstractmethod
    def resource_version_store(self) -> ResourceVersionStore:
        ...

    @abstractmethod
    def payload_store(self) -> PayloadStore:
        ...

    @abstractmethod
    def get_secret(self) -> bytes:
        ...

    @abstractmethod
    def get_settings(self) -> HaketiloGlobalSettings:
        """...."""
        ...

    @abstractmethod
    def update_settings(
            self,
            *,
            mapping_use_mode:      t.Optional[MappingUseMode] = None,
            default_allow_scripts: t.Optional[bool]           = None,
            advanced_user:         t.Optional[bool]           = None,
            repo_refresh_seconds:  t.Optional[int]            = None
    ) -> None:
        """...."""
        ...
