# SPDX-License-Identifier: AGPL-3.0-or-later

# Processing of repository packages.
#
# This file is part of Hydrilla
#
# Copyright (C) 2021, 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

import logging
import dataclasses as dc
import typing as t

from pathlib import Path

from immutables import Map

from ..translations import smart_gettext as _
from ..exceptions import HaketiloException
from .. import versions
from .. import item_infos
from .. import pattern_tree


MappingTree = pattern_tree.PatternTree[item_infos.MappingInfo]

# VersionedType = t.TypeVar(
#     'VersionedType',
#     item_infos.ResourceInfo,
#     item_infos.MappingInfo
# )

class Malcontent:
    """
    Represent a directory with files that can be loaded and served by Hydrilla.
    """
    def __init__(
            self,
            malcontent_dir_path: Path,
            werror: bool,
            verify_files: bool
    ):
        """
        When an instance of Malcontent is constructed, it searches
        malcontent_dir_path for serveable site-modifying packages and loads
        them into its data structures.
        """
        self.werror:       bool = werror
        self.verify_files: bool = verify_files

        self.resource_infos: item_infos.VersionedResourceInfoMap = Map()
        self.mapping_infos:  item_infos.VersionedMappingInfoMap  = Map()

        self.mapping_tree: MappingTree = MappingTree()

        self.malcontent_dir_path = malcontent_dir_path

        if not self.malcontent_dir_path.is_dir():
            fmt = _('err.server.malcontent_path_not_dir_{}')
            raise HaketiloException(fmt.format(malcontent_dir_path))

        for type in [item_infos.ItemType.RESOURCE, item_infos.ItemType.MAPPING]:
            type_path = self.malcontent_dir_path / type.value
            if not type_path.is_dir():
                continue

            for subpath in type_path.iterdir():
                if not subpath.is_dir():
                    continue

                for ver_file in subpath.iterdir():
                    try:
                        self._load_item(type, ver_file)
                    except:
                        if self.werror:
                            raise

                        fmt = _('err.server.couldnt_load_item_from_{}')
                        logging.error(fmt.format(ver_file), exc_info=True)

        self._report_missing()
        self._finalize()

    def _check_package_files(self, info: item_infos.AnyInfo) -> None:
        by_sha256_dir = self.malcontent_dir_path / 'file' / 'sha256'

        for file_spec in info.files:
            if (by_sha256_dir / file_spec.sha256).is_file():
                continue

            fmt = _('err.server.no_file_{required_by}_{ver}_{file}_{sha256}')
            msg = fmt.format(
                required_by = info.identifier,
                ver         = versions.version_string(info.version),
                file        = file_spec.name,
                sha256      = file_spec.sha256
            )
            if (self.werror):
                raise HaketiloException(msg)
            else:
                logging.error(msg)

    def _load_item(self, type: item_infos.ItemType, ver_file: Path) \
        -> None:
        """
        Reads, validates and autocompletes serveable mapping/resource
        definition, then registers information from it in data structures.
        """
        version    = versions.parse(ver_file.name)
        identifier = ver_file.parent.name

        item_info = type.info_class.load(ver_file)

        if item_info.identifier != identifier:
            fmt = _('err.server.item_{item}_in_file_{file}')
            msg = fmt.format({'item': item_info.identifier, 'file': ver_file})
            raise HaketiloException(msg)

        if item_info.version != version:
            ver_str = versions.version_string(item_info.version)
            fmt = _('item_version_{ver}_in_file_{file}')
            msg = fmt.format({'ver': ver_str, 'file': ver_file})
            raise HaketiloException(msg)

        if self.verify_files:
            self._check_package_files(item_info)

        if isinstance(item_info, item_infos.ResourceInfo):
            self.resource_infos = item_infos.register_in_versioned_map(
                map  = self.resource_infos,
                info = item_info
            )
        else:
            self.mapping_infos = item_infos.register_in_versioned_map(
                map  = self.mapping_infos,
                info = item_info
            )

    def _report_missing(self) -> None:
        """
        Use logger to print information about items that are referenced but
        were not loaded.
        """
        def report_missing_dependency(
                info: item_infos.ResourceInfo,
                dep: str
        ) -> None:
            msg = _('err.server.no_dep_{resource}_{ver}_{dep}')\
                .format(dep=dep, resource=info.identifier,
                        ver=versions.version_string(info.version))
            logging.error(msg)

        for resource_info in item_infos.all_map_infos(self.resource_infos):
            for dep_specifier in resource_info.dependencies:
                identifier = dep_specifier.identifier
                if identifier not in self.resource_infos:
                    report_missing_dependency(resource_info, identifier)

        def report_missing_payload(
                info: item_infos.MappingInfo,
                payload: str
        ) -> None:
            msg = _('err.server.no_payload_{mapping}_{ver}_{payload}')\
                .format(mapping=info.identifier, payload=payload,
                        ver=versions.version_string(info.version))
            logging.error(msg)

        for mapping_info in item_infos.all_map_infos(self.mapping_infos):
            for resource_specifier in mapping_info.payloads.values():
                identifier = resource_specifier.identifier
                if identifier not in self.resource_infos:
                    report_missing_payload(mapping_info, identifier)

        def report_missing_mapping(
                info: item_infos.AnyInfo,
                required: str
        ) -> None:
            msg = _('err.server.no_mapping_{required_by}_{ver}_{required}')\
                .format(required_by=info.identifier, required=required,
                        ver=versions.version_string(info.version))
            logging.error(msg)

        infos: t.Iterable[item_infos.AnyInfo] = (
            *item_infos.all_map_infos(self.mapping_infos),
            *item_infos.all_map_infos(self.resource_infos)
        )
        for item_info in infos:
            for mapping_specifier in item_info.required_mappings:
                identifier = mapping_specifier.identifier
                if identifier not in self.mapping_infos:
                    report_missing_mapping(item_info, identifier)

    def _finalize(self):
        """
        Initialize structures needed to serve queries. Called once after all
        data gets loaded.
        """
        for info in item_infos.all_map_infos(self.mapping_infos):
            for pattern in info.payloads:
                try:
                    self.mapping_tree = \
                        self.mapping_tree.register(pattern, info)
                except:
                    if self.werror:
                        raise
                    msg = _('server.err.couldnt_register_{mapping}_{ver}_{pattern}')\
                        .format(mapping=info.identifier, pattern=pattern,
                                ver=util.version_string(info.version))
                    logging.error(msg)

    def query(self, url: str) -> t.Sequence[item_infos.MappingInfo]:
        """
        Return a list of registered mappings that match url.

        If multiple versions of a mapping are applicable, only the most recent
        is included in the result.
        """
        collected: t.Dict[str, item_infos.MappingInfo] = {}
        for result_set in self.mapping_tree.search(url):
            for wrapped_mapping_info in result_set:
                info = wrapped_mapping_info.item
                previous = collected.get(info.identifier)
                if previous and previous.version > info.version:
                    continue

                collected[info.identifier] = info

        return list(collected.values())

    def get_all_resources(self) -> t.Sequence[item_infos.ResourceInfo]:
        return tuple(item_infos.all_map_infos(self.resource_infos))

    def get_all_mappings(self) -> t.Sequence[item_infos.MappingInfo]:
        return tuple(item_infos.all_map_infos(self.mapping_infos))
