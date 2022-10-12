# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (ResourceStore and MappingStore
# implementations).
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
This module provides an interface to interact with mappings, and resources
inside Haketilo.
"""

import sqlite3
import typing as t
import dataclasses as dc

from contextlib import contextmanager
from urllib.parse import urljoin

from ... import item_infos
from .. import state as st
from . import base


def _get_item_id(cursor: sqlite3.Cursor, item_type: str, identifier: str) \
    -> str:
    cursor.execute(
        'SELECT item_id FROM items WHERE identifier = ? AND type = ?;',
        (identifier, item_type)
    )

    rows = cursor.fetchall()

    if rows == []:
        raise st.MissingItemError()

    (item_id,), = rows

    return str(item_id)


def _get_parent_item_id(cursor: sqlite3.Cursor, version_id: str) -> str:
    cursor.execute(
        '''
        SELECT
                item_id
        FROM
                item_versions
        WHERE
                item_version_id = ?;
        ''',
        (version_id,)
    )

    rows = cursor.fetchall()
    if rows == []:
        raise st.MissingItemError()

    (item_id,), = rows

    return str(item_id)


def _set_installed_status(cursor: sqlite3.Cursor, id: str, new_status: str) \
    -> None:
    cursor.execute(
         'UPDATE item_versions SET installed = ? WHERE item_version_id = ?;',
        (new_status, id)
    )

def _get_statuses(cursor: sqlite3.Cursor, id: str) -> tuple[str, str]:
    cursor.execute(
        '''
        SELECT
                installed, active
        FROM
                item_versions
        WHERE
                item_version_id = ?;
        ''',
        (id,)
    )

    rows = cursor.fetchall()

    if rows == []:
        raise st.MissingItemError()

    (installed_status, active_status), = rows

    return installed_status, active_status

VersionRefVar = t.TypeVar(
    'VersionRefVar',
    'ConcreteResourceVersionRef',
    'ConcreteMappingVersionRef'
)

def _install_version(ref: VersionRefVar) -> None:
    with ref.state.cursor(transaction=True) as cursor:
        installed_status, _ = _get_statuses(cursor, ref.id)

        if installed_status == 'I':
            return

        _set_installed_status(cursor, ref.id, 'I')

        ref.state.pull_missing_files()

def _uninstall_version(ref: VersionRefVar) -> t.Optional[VersionRefVar]:
    with ref.state.cursor(transaction=True) as cursor:
        installed_status, active_status = _get_statuses(cursor, ref.id)

        if installed_status == 'N':
            return ref

        if active_status == 'R':
            return ref

        _set_installed_status(cursor, ref.id, 'N')

        ref.state.soft_prune_orphan_items()

        if active_status != 'N':
            ref.state.recompute_dependencies()

        cursor.execute(
            'SELECT COUNT(*) FROM item_versions WHERE item_version_id = ?;',
            (ref.id,)
        )

        (version_still_present,), = cursor.fetchall()
        return ref if version_still_present else None


def _get_file(ref: VersionRefVar, name: str, file_type: str = 'L') \
    -> st.FileData:
    with ref.state.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                    f.data, fu.mime_type
            FROM
                         item_versions AS iv
                    JOIN items         AS i  USING (item_id)
                    JOIN file_uses     AS fu USING (item_version_id)
                    JOIN files         AS f  USING (file_id)
            WHERE
                    (iv.item_version_id = ? AND iv.installed = 'I') AND
                    i.type = ?                                      AND
                    (fu.name = ? AND fu.type = ?)                   AND
                    f.data IS NOT NULL;
            ''',
            (ref.id, ref.type.value[0].upper(), name, file_type)
        )

        rows = cursor.fetchall()

    if rows == []:
        raise st.MissingItemError()

    (data, mime_type), = rows

    return st.FileData(mime_type, name, data)


def _get_upstream_file_url(
        ref:       VersionRefVar,
        name:      str,
        file_type: str = 'L'
) -> str:
    with ref.state.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                    f.sha256, r.url
            FROM
                         item_versions   AS iv
                    JOIN repo_iterations AS ri USING(repo_iteration_id)
                    JOIN repos           AS r  USING(repo_id)
                    JOIN file_uses       AS fu USING(item_version_id)
                    JOIN files           AS f  USING(file_id)
            WHERE
                    iv.item_version_id = ?        AND
                    (fu.name = ? AND fu.type = ?) AND
                    r.url IS NOT NULL;
            ''',
            (ref.id, name, file_type)
        )

        rows = cursor.fetchall()

    if rows == []:
        raise st.MissingItemError()

    (sha256, repo_url), = rows

    return urljoin(repo_url, f'file/sha256/{sha256}')


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteMappingRef(st.MappingRef):
    state: base.HaketiloStateWithFields = dc.field(hash=False, compare=False)

    def _get_status_data(self, cursor: sqlite3.Cursor) \
        -> tuple[str, str, int]:
        cursor.execute(
            '''
            SELECT
                    ms.enabled, ms.frozen, ms.active_version_id
            FROM
                    mapping_statuses
            WHERE
                    item_id = ?;
            ''',
            (self.id,)
        )

        rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        (enabled_status, frozen_status, active_version_id), = rows

        return (enabled_status, frozen_status, active_version_id)


    def update_status(
            self,
            enabled:                st.EnabledStatus,
            frozen:                 t.Optional[st.FrozenStatus] = None,
            version_id_to_activate: t.Optional[str]             = None
    ) -> None:
        assert frozen is None or enabled == st.EnabledStatus.ENABLED
        assert version_id_to_activate is None or \
            frozen != st.FrozenStatus.NOT_FROZEN

        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                '''
                SELECT
                        enabled, frozen, active_version_id
                FROM
                        mapping_statuses
                WHERE
                        item_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (old_enabled_status, old_frozen_status,
             old_active_version_id), = rows

            if enabled.value == old_enabled_status and frozen is None:
                return

            new_enabled_status = enabled.value

            new_frozen_status = None if frozen is None else frozen.value

            if version_id_to_activate is not None:
                new_active_version_id = version_id_to_activate
            elif enabled == st.EnabledStatus.ENABLED and \
                 old_active_version_id is not None:
                new_active_version_id = str(old_active_version_id)
            else:
                new_active_version_id = None

            cursor.execute(
                '''
                UPDATE
                        mapping_statuses
                SET
                        enabled           = ?,
                        frozen            = ?,
                        active_version_id = ?
                WHERE
                        item_id = ?;
                ''', (
                    new_enabled_status,
                    new_frozen_status,
                    new_active_version_id,
                    self.id
                ))

            if enabled == st.EnabledStatus.ENABLED:
                if old_enabled_status == 'E'                           and \
                   new_active_version_id == str(old_active_version_id) and \
                   (new_frozen_status == 'E' or
                    old_frozen_status == 'N' or
                    new_frozen_status == old_frozen_status):
                    return
            else:
                if old_active_version_id is None and old_enabled_status != 'D':
                    return

            self.state.recompute_dependencies([int(self.id)])

    def get_display_info(self) -> st.RichMappingDisplayInfo:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        i.identifier,
                        ms.enabled, ms.frozen
                FROM
                             items            AS i
                        JOIN mapping_statuses AS ms USING (item_id)
                WHERE
                        item_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (identifier, enabled_status, frozen_status), = rows

            cursor.execute(
                '''
                SELECT
                        item_version_id,
                        definition,
                        repo,
                        repo_iteration,
                        installed,
                        active,
                        is_orphan,
                        is_local
                FROM
                        item_versions_extra
                WHERE
                        item_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

        version_infos = []

        active_info: t.Optional[st.MappingVersionDisplayInfo] = None

        for (item_version_id, definition, repo, repo_iteration,
             installed_status, active_status, is_orphan, is_local) in rows:
            ref = ConcreteMappingVersionRef(str(item_version_id), self.state)

            item_info = item_infos.MappingInfo.load(
                definition,
                repo,
                repo_iteration
            )

            version_display_info = st.MappingVersionDisplayInfo(
                ref             = ref,
                info            = item_info,
                installed       = st.InstalledStatus(installed_status),
                active          = st.ActiveStatus(active_status),
                is_orphan       = is_orphan,
                is_local        = is_local
            )

            version_infos.append(version_display_info)

            if active_status in ('R', 'A'):
                active_info = version_display_info

        return st.RichMappingDisplayInfo(
            ref            = self,
            identifier     = identifier,
            enabled        = st.EnabledStatus(enabled_status),
            frozen         = st.FrozenStatus.make(frozen_status),
            active_version = active_info,
            all_versions   = sorted(version_infos, key=(lambda vi: vi.info))
        )


@dc.dataclass(frozen=True)
class ConcreteMappingStore(st.MappingStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.MappingRef:
        return ConcreteMappingRef(str(int(id)), self.state)

    def get_display_infos(self) -> t.Sequence[st.MappingDisplayInfo]:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                WITH available_item_ids AS (
                        SELECT DISTINCT item_id FROM item_versions
                )
                SELECT
                        i.item_id,
                        i.identifier,
                        ive.item_version_id,
                        ive.definition,
                        ive.repo,
                        ive.repo_iteration,
                        ive.installed,
                        ive.active,
                        ive.is_orphan,
                        ive.is_local,
                        ms.enabled,
                        ms.frozen
                FROM
                                  items                 AS i
                        JOIN      mapping_statuses      AS ms
                                USING (item_id)
                        LEFT JOIN item_versions_extra   AS ive
                                ON ms.active_version_id = ive.item_version_id
                WHERE
                        i.item_id IN available_item_ids;
                '''
            )

            rows = cursor.fetchall()

        result = []

        for (item_id, identifier, item_version_id, definition, repo,
             repo_iteration, installed_status, active_status, is_orphan,
             is_local, enabled_status, frozen_status) in rows:
            ref = ConcreteMappingRef(str(item_id), self.state)

            active_version: t.Optional[st.MappingVersionDisplayInfo] = None

            if item_version_id is not None:
                active_version_ref = ConcreteMappingVersionRef(
                    id    = str(item_version_id),
                    state = self.state
                )

                active_version_info = item_infos.MappingInfo.load(
                    definition,
                    repo,
                    repo_iteration
                )

                active_version = st.MappingVersionDisplayInfo(
                    ref             = active_version_ref,
                    info            = active_version_info,
                    installed       = st.InstalledStatus(installed_status),
                    active          = st.ActiveStatus(active_status),
                    is_orphan       = is_orphan,
                    is_local        = is_local
                )

            display_info = st.MappingDisplayInfo(
                ref            = ref,
                identifier     = identifier,
                enabled        = st.EnabledStatus(enabled_status),
                frozen         = st.FrozenStatus.make(frozen_status),
                active_version = active_version
            )

            result.append(display_info)

        return sorted(result, key=(lambda di: di.identifier))

    def get_by_identifier(self, identifier: str) -> st.MappingRef:
        with self.state.cursor() as cursor:
            item_id = _get_item_id(cursor, 'M', identifier)

        return ConcreteMappingRef(item_id, self.state)


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteMappingVersionRef(st.MappingVersionRef):
    state: base.HaketiloStateWithFields

    def install(self) -> None:
        return _install_version(self)

    def uninstall(self) -> t.Optional['ConcreteMappingVersionRef']:
        return _uninstall_version(self)

    def ensure_depended_items_installed(self) -> None:
        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                '''
                UPDATE
                        item_versions
                SET
                        installed = 'I'
                WHERE
                        item_version_id = ?;
                ''',
                (self.id,)
            )

            cursor.execute(
                '''
                WITH depended_resource_ids AS (
                        SELECT
                                rdd.resource_item_id
                        FROM
                                     payloads                    AS p
                                JOIN resolved_depended_resources AS rdd
                                        USING (payload_id)
                        WHERE
                                p.mapping_item_id = ?
                )
                UPDATE
                        item_versions
                SET
                        installed = 'I'
                WHERE
                        item_version_id IN depended_resource_ids;
                ''',
                (self.id,)
            )

            self.state.pull_missing_files()

    @contextmanager
    def _mapping_ref(self) -> t.Iterator[ConcreteMappingRef]:
        with self.state.cursor(transaction=True) as cursor:
            mapping_id = _get_parent_item_id(cursor, self.id)
            yield ConcreteMappingRef(mapping_id, self.state)

    def update_mapping_status(
            self,
            enabled: st.EnabledStatus,
            frozen:  t.Optional[st.FrozenStatus] = None
    ) -> None:
        with self._mapping_ref() as mapping_ref:
            id_to_pass: t.Optional[str] = self.id
            if enabled.value != 'E' or frozen is None or frozen.value == 'N':
                id_to_pass = None

            mapping_ref.update_status(enabled, frozen, id_to_pass)

    def get_license_file(self, name: str) -> st.FileData:
        return _get_file(self, name, 'L')

    def get_upstream_license_file_url(self, name: str) -> str:
        return _get_upstream_file_url(self, name, 'L')

    def get_required_mapping(self, identifier: str) \
        -> 'ConcreteMappingVersionRef':
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        iv2.item_version_id
                FROM
                             item_versions              AS iv1
                        JOIN resolved_required_mappings AS rrm
                                ON iv1.item_version_id =
                                   rrm.requiring_mapping_id
                        JOIN item_versions              AS iv2
                                ON rrm.required_mapping_id =
                                   iv2.item_version_id
                        JOIN items                      AS i
                                ON iv2.item_id = i.item_id
                WHERE
                        iv1.item_version_id = ? AND
                        i.identifier = ?;
                ''',
                (self.id, identifier)
            )

            rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        (required_id,), = rows

        return ConcreteMappingVersionRef(str(required_id), self.state)

    def get_payload_resource(self, pattern: str, identifier: str) \
        -> 'ConcreteResourceVersionRef':
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        iv.item_version_id
                FROM
                             payloads                    AS p
                        JOIN resolved_depended_resources AS rdd
                                USING(payload_id)
                        JOIN item_versions               AS iv
                                ON rdd.resource_item_id = iv.item_version_id
                        JOIN items                       AS i
                                USING (item_id)
                WHERE
                        (p.mapping_item_id = ? AND p.pattern = ?) AND
                        i.identifier = ?;
                ''',
                (self.id, pattern, identifier)
            )

            rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        (resource_ver_id,), = rows

        return ConcreteResourceVersionRef(str(resource_ver_id), self.state)

    def get_item_display_info(self) -> st.RichMappingDisplayInfo:
        with self._mapping_ref() as mapping_ref:
            return mapping_ref.get_display_info()


@dc.dataclass(frozen=True)
class ConcreteMappingVersionStore(st.MappingVersionStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.MappingVersionRef:
        return ConcreteMappingVersionRef(str(int(id)), self.state)


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteResourceRef(st.ResourceRef):
    state: base.HaketiloStateWithFields = dc.field(hash=False, compare=False)

    def get_display_info(self) -> st.RichResourceDisplayInfo:
        with self.state.cursor() as cursor:
            cursor.execute(
                'SELECT identifier FROM items WHERE item_id = ?;',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (identifier,), = rows

            cursor.execute(
                '''
                SELECT
                        item_version_id,
                        definition,
                        repo,
                        repo_iteration,
                        installed,
                        active,
                        is_orphan,
                        is_local
                FROM
                        item_versions_extra
                WHERE
                        item_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

        version_infos = []

        for (item_version_id, definition, repo, repo_iteration,
             installed_status, active_status, is_orphan, is_local) in rows:
            ref = ConcreteResourceVersionRef(str(item_version_id), self.state)

            item_info = item_infos.ResourceInfo.load(
                definition,
                repo,
                repo_iteration
            )

            display_info = st.ResourceVersionDisplayInfo(
                ref             = ref,
                info            = item_info,
                installed       = st.InstalledStatus(installed_status),
                active          = st.ActiveStatus(active_status),
                is_orphan       = is_orphan,
                is_local        = is_local
            )

            version_infos.append(display_info)

        return st.RichResourceDisplayInfo(
            ref            = self,
            identifier     = identifier,
            all_versions   = sorted(version_infos, key=(lambda vi: vi.info))
        )


@dc.dataclass(frozen=True)
class ConcreteResourceStore(st.ResourceStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.ResourceRef:
        return ConcreteResourceRef(str(int(id)), self.state)

    def get_display_infos(self) -> t.Sequence[st.ResourceDisplayInfo]:
        with self.state.cursor() as cursor:
            cursor.execute(
                "SELECT item_id, identifier FROM items WHERE type = 'R';"
            )

            rows = cursor.fetchall()

        result = []

        for item_id, identifier in rows:
            ref = ConcreteResourceRef(str(item_id), self.state)

            result.append(st.ResourceDisplayInfo(ref, identifier))

        return sorted(result, key=(lambda di: di.identifier))

    def get_by_identifier(self, identifier: str) -> st.ResourceRef:
        with self.state.cursor() as cursor:
            item_id = _get_item_id(cursor, 'R', identifier)

        return ConcreteResourceRef(item_id, self.state)


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteResourceVersionRef(st.ResourceVersionRef):
    state: base.HaketiloStateWithFields

    def install(self) -> None:
        return _install_version(self)

    def uninstall(self) -> t.Optional['ConcreteResourceVersionRef']:
        return _uninstall_version(self)

    def get_license_file(self, name: str) -> st.FileData:
        return _get_file(self, name, 'L')

    def get_resource_file(self, name: str) -> st.FileData:
        return _get_file(self, name, 'W')

    def get_upstream_license_file_url(self, name: str) -> str:
        return _get_upstream_file_url(self, name, 'L')

    def get_upstream_resource_file_url(self, name: str) -> str:
        return _get_upstream_file_url(self, name, 'W')

    def get_dependency(self, identifier: str) -> st.ResourceVersionRef:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        iv.item_version_id
                FROM
                             resolved_depended_resources AS rdd1
                        JOIN payloads                    AS p
                                ON rdd1.payload_id = p.payload_id
                        JOIN resolved_depended_resources AS rdd2
                                ON p.payload_id = rdd2.payload_id
                        JOIN item_versions               AS iv
                                ON rdd2.resource_item_id = iv.item_version_id
                        JOIN items                       AS i
                                USING (item_id)
                WHERE
                        rdd1.resource_item_id = ? AND i.identifier = ?;
                ''',
                (self.id, identifier)
            )

            rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        (dep_id,), = rows

        return ConcreteResourceVersionRef(str(dep_id), self.state)

    def get_item_display_info(self) -> st.RichResourceDisplayInfo:
        with self.state.cursor() as cursor:
            resource_id = _get_parent_item_id(cursor, self.id)
            resource_ref = ConcreteResourceRef(resource_id, self.state)
            return resource_ref.get_display_info()


@dc.dataclass(frozen=True)
class ConcreteResourceVersionStore(st.ResourceVersionStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.ResourceVersionRef:
        return ConcreteResourceVersionRef(str(int(id)), self.state)
