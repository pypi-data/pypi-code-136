# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (PayloadRef subtype).
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
This module provides an interface to interact with payloads inside Haketilo.
"""

import sqlite3
import dataclasses as dc
import typing as t

from ... import item_infos
from .. import state as st
from . import base
from . import items


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcretePayloadRef(st.PayloadRef):
    state: base.HaketiloStateWithFields = dc.field(hash=False, compare=False)

    def get_data(self) -> st.PayloadData:
        try:
            return self.state.payloads_data[self]
        except KeyError:
            raise st.MissingItemError()

    def has_problems(self) -> bool:
        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                '''
                SELECT
                        iv.installed == 'F'
                FROM
                             payloads      AS p
                        JOIN item_versions AS iv
                                ON p.mapping_item_id = iv.item_version_id
                WHERE
                        p.payload_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (mapping_install_failed,), = rows
            if mapping_install_failed:
                return True

            cursor.execute(
                '''
                SELECT
                        COUNT(*) > 0
                FROM
                             payloads                    AS p
                        JOIN resolved_depended_resources AS rdd
                                USING (payload_id)
                        JOIN item_versions AS iv
                                ON rdd.resource_item_id = iv.item_version_id
                WHERE
                        p.payload_id = ? AND iv.installed = 'F';
                ''',
                (self.id,)
            )

            (resource_install_failed,), = cursor.fetchall()
            if resource_install_failed:
                return True

        return False

    def get_display_info(self) -> st.PayloadDisplayInfo:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        p.pattern,
                        ive.item_version_id,
                        ive.definition,
                        ive.repo,
                        ive.repo_iteration,
                        ive.installed,
                        ive.active,
                        ive.is_orphan,
                        ive.is_local
                FROM
                             payloads            AS p
                        JOIN item_versions_extra AS ive
                                ON p.mapping_item_id = ive.item_version_id
                WHERE
                        p.payload_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (pattern_str, mapping_version_id, definition, repo, repo_iteration,
             installed_status, active_status, is_orphan, is_local), = rows

            has_problems = self.has_problems()

        mapping_version_ref = items.ConcreteMappingVersionRef(
            id = str(mapping_version_id),
            state = self.state
        )

        mapping_version_info = item_infos.MappingInfo.load(
            definition,
            repo,
            repo_iteration
        )

        mapping_version_display_info = st.MappingVersionDisplayInfo(
            ref       = mapping_version_ref,
            info      = mapping_version_info,
            installed = st.InstalledStatus(installed_status),
            active    = st.ActiveStatus(active_status),
            is_orphan = is_orphan,
            is_local  = is_local
        )

        return st.PayloadDisplayInfo(
            ref          = self,
            mapping_info = mapping_version_display_info,
            pattern      = pattern_str,
            has_problems = has_problems
        )

    def ensure_items_installed(self) -> None:
        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                'SELECT mapping_item_id FROM payloads WHERE payload_id = ?;',
                (self.id,)
            )

            rows = cursor.fetchall()

            if rows == []:
                raise st.MissingItemError()

            (mapping_version_id,), = rows

            mapping_version_ref = items.ConcreteMappingVersionRef(
                id    = str(mapping_version_id),
                state = self.state
            )

            mapping_version_ref.ensure_depended_items_installed()

    def get_script_paths(self) \
        -> t.Iterable[t.Sequence[str]]:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        i.identifier, fu.name
                FROM
                                  payloads                    AS p
                        LEFT JOIN resolved_depended_resources AS rdd
                                USING (payload_id)
                        LEFT JOIN item_versions               AS iv
                                ON rdd.resource_item_id = iv.item_version_id
                        LEFT JOIN items                       AS i
                                USING (item_id)
                        LEFT JOIN file_uses                   AS fu
                                USING (item_version_id)
                WHERE
                        fu.type = 'W'    AND
                        p.payload_id = ? AND
                        (fu.idx IS NOT NULL OR rdd.idx IS NULL)
                ORDER BY
                        rdd.idx, fu.idx;
                ''',
                (self.id,)
            )

            paths: list[t.Sequence[str]] = []
            for resource_identifier, file_name in cursor.fetchall():
                if resource_identifier is None:
                    # payload found but it had no script files
                    return ()

                paths.append((resource_identifier, *file_name.split('/')))

        if paths == []:
            # payload not found
            raise st.MissingItemError()

        return paths

    def get_file_data(self, path: t.Sequence[str]) \
        -> t.Optional[st.FileData]:
        if len(path) == 0:
            raise st.MissingItemError()

        resource_identifier, *file_name_segments = path

        file_name = '/'.join(file_name_segments)

        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        f.data, fu.mime_type
                FROM
                             payloads                    AS p
                        JOIN resolved_depended_resources AS rdd
                                USING (payload_id)
                        JOIN item_versions               AS iv
                                ON rdd.resource_item_id = iv.item_version_id
                        JOIN items                       AS i
                                USING (item_id)
                        JOIN file_uses                   AS fu
                                USING (item_version_id)
                        JOIN files                       AS f
                                USING (file_id)
                WHERE
                        p.payload_id = ? AND
                        i.identifier = ? AND
                        fu.name = ?      AND
                        fu.type = 'W';
                ''',
                (self.id, resource_identifier, file_name)
            )

            result = cursor.fetchall()

        if result == []:
            return None

        (data, mime_type), = result

        return st.FileData(mime_type=mime_type, name=file_name, contents=data)


@dc.dataclass(frozen=True)
class ConcretePayloadStore(st.PayloadStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.PayloadRef:
        return ConcretePayloadRef(str(int(id)), self.state)
