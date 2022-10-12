# SPDX-License-Identifier: GPL-3.0-or-later

# Reading resources, mappings and other JSON documents from the filesystem.
#
# This file is part of Hydrilla&Haketilo
#
# Copyright (C) 2021, 2022 Wojtek Kosior
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
.....
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import enum
import typing as t
import dataclasses as dc

from pathlib import Path, PurePosixPath
from abc import ABC, abstractmethod

from immutables import Map

from . import versions, json_instances
from .url_patterns import parse_pattern, ParsedUrl, ParsedPattern
from .exceptions import HaketiloException
from .translations import smart_gettext as _


@dc.dataclass(frozen=True, unsafe_hash=True)
class ItemSpecifier:
    """...."""
    identifier: str

ItemSpecs = t.Tuple[ItemSpecifier, ...]

SpecifierObjs = t.Sequence[t.Mapping[str, t.Any]]

def make_item_specifiers_seq(spec_objs: SpecifierObjs) -> ItemSpecs:
    return tuple(ItemSpecifier(obj['identifier']) for obj in spec_objs)

def make_required_mappings(spec_objs: t.Any, schema_compat: int) -> ItemSpecs:
    if schema_compat < 2:
        return ()

    return make_item_specifiers_seq(spec_objs)

@dc.dataclass(frozen=True, unsafe_hash=True)
class FileSpecifier:
    """...."""
    name:   str
    sha256: str

FileSpecs = t.Tuple[FileSpecifier, ...]

def normalize_filename(name: str):
    """
    This function eliminated double slashes in file name and ensures it does not
    try to reference parent directories.
    """
    path = PurePosixPath(name)

    if '.' in path.parts or '..' in path.parts:
        msg = _('err.item_info.filename_invalid_{}').format(name)
        raise HaketiloException(msg)

    return str(path)

def make_file_specifiers_seq(spec_objs: SpecifierObjs) -> FileSpecs:
    return tuple(
        FileSpecifier(normalize_filename(obj['file']), obj['sha256'])
        for obj
        in spec_objs
    )

@dc.dataclass(frozen=True, unsafe_hash=True)
class GeneratedBy:
    """...."""
    name:    str
    version: t.Optional[str]

    @staticmethod
    def make(generated_by_obj: t.Optional[t.Mapping[str, t.Any]]) -> \
        t.Optional['GeneratedBy']:
        """...."""
        if generated_by_obj is None:
            return None

        return GeneratedBy(
            name    = generated_by_obj['name'],
            version = generated_by_obj.get('version')
        )


def make_eval_permission(perms_obj: t.Any, schema_compat: int) -> bool:
    if schema_compat < 2:
        return False

    return perms_obj.get('eval', False)


def make_cors_bypass_permission(perms_obj: t.Any, schema_compat: int) -> bool:
    if schema_compat < 2:
        return False

    return perms_obj.get('cors_bypass', False)


def make_version_constraint(
        ver:           t.Any,
        schema_compat: int,
        default:       versions.VerTuple
) -> versions.VerTuple:
    if schema_compat < 2 or ver is None:
        return default

    return versions.normalize(ver)


class Categorizable(Protocol):
    """...."""
    uuid:       t.Optional[str]
    identifier: str

@dc.dataclass(frozen=True, unsafe_hash=True)
class ItemIdentity:
    repo:           str
    repo_iteration: int
    version:        versions.VerTuple
    identifier:     str


# mypy needs to be corrected:
# https://stackoverflow.com/questions/70999513/conflict-between-mix-ins-for-abstract-dataclasses/70999704#70999704
@dc.dataclass(frozen=True) # type: ignore[misc]
class ItemInfoBase(ABC, ItemIdentity, Categorizable):
    """...."""
    source_name:        str                     = dc.field(hash=False, compare=False)
    source_copyright:   FileSpecs               = dc.field(hash=False, compare=False)
    uuid:               t.Optional[str]         = dc.field(hash=False, compare=False)
    long_name:          str                     = dc.field(hash=False, compare=False)
    description:        str                     = dc.field(hash=False, compare=False)
    allows_eval:        bool                    = dc.field(hash=False, compare=False)
    allows_cors_bypass: bool                    = dc.field(hash=False, compare=False)
    min_haketilo_ver:   versions.VerTuple       = dc.field(hash=False, compare=False)
    max_haketilo_ver:   versions.VerTuple       = dc.field(hash=False, compare=False)
    required_mappings:  ItemSpecs               = dc.field(hash=False, compare=False)
    generated_by:       t.Optional[GeneratedBy] = dc.field(hash=False, compare=False)

    @property
    def version_string(self) -> str:
        return versions.version_string(self.version)

    @property
    def versioned_identifier(self) -> str:
        """...."""
        return f'{self.identifier}-{self.version_string}'

    @property
    def files(self) -> FileSpecs:
        return self.source_copyright

    @property
    def compatible(self) -> bool:
        return (self.min_haketilo_ver <= versions.haketilo_version and
                self.max_haketilo_ver >= versions.haketilo_version)

    @staticmethod
    def _get_base_init_kwargs(
            item_obj:       t.Mapping[str, t.Any],
            schema_compat:  int,
            repo:           str,
            repo_iteration: int
    ) -> t.Mapping[str, t.Any]:
        """...."""
        source_copyright = make_file_specifiers_seq(
            item_obj['source_copyright']
        )

        version = versions.normalize(item_obj['version'])

        perms_obj = item_obj.get('permissions', {})

        eval_perm        = make_eval_permission(perms_obj, schema_compat)
        cors_bypass_perm = make_cors_bypass_permission(perms_obj, schema_compat)

        min_haketilo_ver = make_version_constraint(
            ver           = item_obj.get('min_haketilo_version'),
            schema_compat = schema_compat,
            default       = versions.int_ver_min
        )
        max_haketilo_ver = make_version_constraint(
            ver           = item_obj.get('max_haketilo_version'),
            schema_compat = schema_compat,
            default       = versions.int_ver_max
        )

        required_mappings = make_required_mappings(
            item_obj.get('required_mappings', []),
            schema_compat
        )

        generated_by = GeneratedBy.make(item_obj.get('generated_by'))

        return Map(
            repo               = repo,
            repo_iteration     = repo_iteration,
            source_name        = item_obj['source_name'],
            source_copyright   = source_copyright,
            version            = version,
            identifier         = item_obj['identifier'],
            uuid               = item_obj.get('uuid'),
            long_name          = item_obj['long_name'],
            description        = item_obj['description'],
            allows_eval        = eval_perm,
            allows_cors_bypass = cors_bypass_perm,
            min_haketilo_ver   = min_haketilo_ver,
            max_haketilo_ver   = max_haketilo_ver,
            required_mappings  = required_mappings,
            generated_by       = generated_by
        )


AnyInfo = t.Union['ResourceInfo', 'MappingInfo']


class ItemType(enum.Enum):
    RESOURCE = 'resource'
    MAPPING  = 'mapping'

    @property
    def info_class(self) -> t.Type[AnyInfo]:
        if self == ItemType.RESOURCE:
            return ResourceInfo
        else:
            return MappingInfo

    @property
    def alt_name(self) -> str:
        if self == ItemType.RESOURCE:
            return 'library'
        else:
            return 'package'

    @property
    def alt_name_plural(self) -> str:
        if self == ItemType.RESOURCE:
            return 'libraries'
        else:
            return 'packages'

@dc.dataclass(frozen=True, unsafe_hash=True)
class CorrespondsToResourceDCMixin:
    type: t.ClassVar[ItemType] = ItemType.RESOURCE

@dc.dataclass(frozen=True, unsafe_hash=True)
class CorrespondsToMappingDCMixin:
    type: t.ClassVar[ItemType] = ItemType.MAPPING


@dc.dataclass(frozen=True, unsafe_hash=True)
class ResourceInfo(ItemInfoBase, CorrespondsToResourceDCMixin):
    """...."""
    revision:     int       = dc.field(hash=False, compare=False)
    dependencies: ItemSpecs = dc.field(hash=False, compare=False)
    scripts:      FileSpecs = dc.field(hash=False, compare=False)

    @property
    def version_string(self) -> str:
        return f'{super().version_string}-{self.revision}'

    @property
    def files(self) -> FileSpecs:
        return tuple((*self.source_copyright, *self.scripts))

    @staticmethod
    def make(
            item_obj:       t.Mapping[str, t.Any],
            schema_compat:  int,
            repo:           str,
            repo_iteration: int
    ) -> 'ResourceInfo':
        """...."""
        base_init_kwargs = ItemInfoBase._get_base_init_kwargs(
            item_obj,
            schema_compat,
            repo,
            repo_iteration
        )

        dependencies = make_item_specifiers_seq(
            item_obj.get('dependencies', [])
        )

        scripts = make_file_specifiers_seq(
            item_obj.get('scripts', [])
        )

        return ResourceInfo(
            **base_init_kwargs,

            revision     = item_obj['revision'],
            dependencies = dependencies,
            scripts      = scripts
        )

    @staticmethod
    def load(
            instance_source: json_instances.InstanceSource,
            repo:            str = '<dummyrepo>',
            repo_iteration:  int = -1
    ) -> 'ResourceInfo':
        """...."""
        return _load_item_info(
            ResourceInfo,
            instance_source,
            repo,
            repo_iteration
        )

    def __lt__(self, other: 'ResourceInfo') -> bool:
        """...."""
        return (
            self.identifier,
            other.version,
            other.revision,
            self.repo,
            other.repo_iteration
        ) < (
            other.identifier,
            self.version,
            self.revision,
            other.repo,
            self.repo_iteration
        )

def make_payloads(payloads_obj: t.Mapping[str, t.Any]) \
    -> t.Mapping[ParsedPattern, ItemSpecifier]:
    """...."""
    mapping: t.List[t.Tuple[ParsedPattern, ItemSpecifier]] = []

    for pattern, spec_obj in payloads_obj.items():
        ref = ItemSpecifier(spec_obj['identifier'])
        mapping.extend((parsed, ref) for parsed in parse_pattern(pattern))

    return Map(mapping)

@dc.dataclass(frozen=True, unsafe_hash=True)
class MappingInfo(ItemInfoBase, CorrespondsToMappingDCMixin):
    """...."""
    payloads: t.Mapping[ParsedPattern, ItemSpecifier] = \
        dc.field(hash=False, compare=False)

    @staticmethod
    def make(
            item_obj:       t.Mapping[str, t.Any],
            schema_compat:  int,
            repo:           str,
            repo_iteration: int
    ) -> 'MappingInfo':
        """...."""
        base_init_kwargs = ItemInfoBase._get_base_init_kwargs(
            item_obj,
            schema_compat,
            repo,
            repo_iteration
        )

        return MappingInfo(
            **base_init_kwargs,

            payloads = make_payloads(item_obj.get('payloads', {}))
        )

    @staticmethod
    def load(
            instance_source: json_instances.InstanceSource,
            repo:            str = '<dummyrepo>',
            repo_iteration:  int = -1
    ) -> 'MappingInfo':
        """...."""
        return _load_item_info(
            MappingInfo,
            instance_source,
            repo,
            repo_iteration
        )

    def __lt__(self, other: 'MappingInfo') -> bool:
        """...."""
        return (
            self.identifier,
            other.version,
            self.repo,
            other.repo_iteration
        ) < (
            other.identifier,
            self.version,
            other.repo,
            self.repo_iteration
        )


LoadedType = t.TypeVar('LoadedType', ResourceInfo, MappingInfo)

def _load_item_info(
        info_type:       t.Type[LoadedType],
        instance_source: json_instances.InstanceSource,
        repo:            str,
        repo_iteration:  int
) -> LoadedType:
    """Read, validate and autocomplete a mapping/resource description."""
    instance = json_instances.read_instance(instance_source)

    schema_fmt = f'api_{info_type.type.value}_description-{{}}.schema.json'

    schema_compat = json_instances.validate_instance(instance, schema_fmt)

    # We know from successful validation that instance is a dict.
    return info_type.make(
        t.cast('t.Dict[str, t.Any]', instance),
        schema_compat,
        repo,
        repo_iteration
    )


CategorizedInfoType = t.TypeVar(
    'CategorizedInfoType',
    ResourceInfo,
    MappingInfo
)

CategorizedType = t.TypeVar(
    'CategorizedType',
    bound=Categorizable
)

CategorizedUpdater = t.Callable[
    [t.Optional[CategorizedType]],
    t.Optional[CategorizedType]
]

CategoryKeyType = t.TypeVar('CategoryKeyType', bound=t.Hashable)

@dc.dataclass(frozen=True) # type: ignore[misc]
class CategorizedItemInfo(
        ABC,
        Categorizable,
        t.Generic[CategorizedInfoType, CategorizedType, CategoryKeyType]
):
    """...."""
    SelfType = t.TypeVar(
        'SelfType',
        bound = 'CategorizedItemInfo[CategorizedInfoType, CategorizedType, CategoryKeyType]'
    )

    uuid:         t.Optional[str]                       = None
    identifier:   str                                   = '<dummy>'
    items:        Map[CategoryKeyType, CategorizedType] = Map()
    _initialized: bool                                  = False

    def _update(
            self:   'SelfType',
            key:     CategoryKeyType,
            updater: CategorizedUpdater
    ) -> 'SelfType':
        """...... Perform sanity checks for uuid."""
        uuid = self.uuid

        items = self.items.mutate()

        updated = updater(items.get(key))
        if updated is None:
            items.pop(key, None)

            identifier = self.identifier
        else:
            items[key] = updated

            identifier = updated.identifier
            if self._initialized:
                assert identifier == self.identifier

            if uuid is not None:
                if updated.uuid is not None and uuid != updated.uuid:
                    raise HaketiloException(_('uuid_mismatch_{identifier}')
                                            .format(identifier=identifier))
            else:
                uuid = updated.uuid

        return dc.replace(
            self,
            identifier   = identifier,
            uuid         = uuid,
            items        = items.finish(),
            _initialized = self._initialized or updated is not None
        )

    @abstractmethod
    def register(self: 'SelfType', info: CategorizedInfoType) -> 'SelfType':
        ...

    @abstractmethod
    def get_all(self: 'SelfType') -> t.Sequence[CategorizedInfoType]:
        ...

    def is_empty(self) -> bool:
        return len(self.items) == 0


class VersionedItemInfo(
        CategorizedItemInfo[
            CategorizedInfoType,
            CategorizedInfoType,
            versions.VerTuple
        ],
        t.Generic[CategorizedInfoType]
):
    """Stores data of multiple versions of given resource/mapping."""
    SelfType = t.TypeVar(
        'SelfType',
        bound = 'VersionedItemInfo[CategorizedInfoType]'
    )

    def register(self: 'SelfType', item_info: CategorizedInfoType) \
        -> 'SelfType':
        """
        Make item info queryable by version. Perform sanity checks for uuid.
        """
        return self._update(item_info.version, lambda old_info: item_info)

    @property
    def newest_version(self) -> versions.VerTuple:
        """...."""
        assert not self.is_empty()

        return self.versions()[-1]

    @property
    def newest_info(self) -> CategorizedInfoType:
        """Find and return info of the newest version of item."""
        return self.items[self.newest_version]

    def versions(self, reverse: bool = False) -> t.Sequence[versions.VerTuple]:
        return sorted(self.items.keys(), reverse=reverse)

    def get_by_ver(self, ver: t.Sequence[int]) \
        -> t.Optional[CategorizedInfoType]:
        """
        Find and return info of the specified version of the item (or None if
        absent).
        """
        return self.items.get(versions.normalize(ver))

    def get_all(self, reverse_versions: bool = False) \
        -> t.Sequence[CategorizedInfoType]:
        """
        Generate item info for all its versions, from oldest to newest unless
        the opposite is requested.
        """
        versions = self.versions(reverse=reverse_versions)
        return [self.items[ver] for ver in versions]

VersionedResourceInfo = VersionedItemInfo[ResourceInfo]
VersionedMappingInfo  = VersionedItemInfo[MappingInfo]

VersionedItemInfoMap     = Map[str, VersionedItemInfo]
VersionedResourceInfoMap = Map[str, VersionedResourceInfo]
VersionedMappingInfoMap  = Map[str, VersionedMappingInfo]

def register_in_versioned_map(
        map:  Map[str, VersionedItemInfo[CategorizedInfoType]],
        info: CategorizedInfoType
) -> Map[str, VersionedItemInfo[CategorizedInfoType]]:
    versioned_info = map.get(info.identifier, VersionedItemInfo())

    return map.set(info.identifier, versioned_info.register(info))


class MultirepoItemInfo(
        CategorizedItemInfo[
            CategorizedInfoType,
            VersionedItemInfo[CategorizedInfoType],
            t.Tuple[str, int]
        ],
        t.Generic[CategorizedInfoType]
):
    """
    Stores data of multiple versions of given resource/mapping that may come
    from multiple repositories.
    """
    SelfType = t.TypeVar(
        'SelfType',
        bound = 'MultirepoItemInfo[CategorizedInfoType]'
    )

    def register(self: 'SelfType', item_info: CategorizedInfoType) \
        -> 'SelfType':
        """
        Make item info queryable by repo and version. Perform sanity checks for
        uuid.
        """
        def update(
                versioned: t.Optional[VersionedItemInfo[CategorizedInfoType]]
        ) -> VersionedItemInfo[CategorizedInfoType]:
            if versioned is None:
                versioned = VersionedItemInfo()
            return versioned.register(item_info)

        return self._update((item_info.repo, item_info.repo_iteration), update)

    @property
    def default_info(self) -> CategorizedInfoType:
        """
        Find and return info of one of the available options for the newest
        version of item.
        """
        assert not self.is_empty()

        return self.get_all(reverse_repos=True)[-1]

    def options(self, reverse: bool = False) -> t.Sequence[t.Tuple[str, int]]:
        return sorted(
            self.items.keys(),
            key     = (lambda tuple: (tuple[0], 1 - tuple[1])),
            reverse = reverse
        )

    def get_all(
            self,
            reverse_versions: bool = False,
            reverse_repos:    bool = False
    ) -> t.Sequence[CategorizedInfoType]:
        """
        Generate item info for all its versions and options, from oldest to
        newest version and from.
        """
        all_versions: t.Set[versions.VerTuple] = set()
        for versioned in self.items.values():
            all_versions.update(versioned.versions())

        result = []

        for version in sorted(all_versions, reverse=reverse_versions):
            for option in self.options(reverse=reverse_repos):
                info = self.items[option].get_by_ver(version)
                if info is not None:
                    result.append(info)

        return result

MultirepoResourceInfo = MultirepoItemInfo[ResourceInfo]
MultirepoMappingInfo  = MultirepoItemInfo[MappingInfo]


MultirepoItemInfoMap     = Map[str, MultirepoItemInfo]
MultirepoResourceInfoMap = Map[str, MultirepoResourceInfo]
MultirepoMappingInfoMap  = Map[str, MultirepoMappingInfo]

def register_in_multirepo_map(
        map:  Map[str, MultirepoItemInfo[CategorizedInfoType]],
        info: CategorizedInfoType
) -> Map[str, MultirepoItemInfo[CategorizedInfoType]]:
    multirepo_info = map.get(info.identifier, MultirepoItemInfo())

    return map.set(info.identifier, multirepo_info.register(info))


def all_map_infos(
    map: Map[str, CategorizedItemInfo[CategorizedInfoType, t.Any, t.Any]]
) -> t.Iterator[CategorizedInfoType]:
    for versioned_info in map.values():
        for item_info in versioned_info.get_all():
            yield item_info
