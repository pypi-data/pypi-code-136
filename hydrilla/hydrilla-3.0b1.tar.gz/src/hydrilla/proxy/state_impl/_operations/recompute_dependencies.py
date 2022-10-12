# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (update of dependency tree in the db).
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
....
"""

import sqlite3
import typing as t

from .... import item_infos
from ... import simple_dependency_satisfying as sds
from .. import base
from .pull_missing_files import pull_missing_files, FileResolver, \
    DummyFileResolver


AnyInfoVar = t.TypeVar(
    'AnyInfoVar',
    item_infos.ResourceInfo,
    item_infos.MappingInfo
)

def _get_infos_of_type(cursor: sqlite3.Cursor, info_type: t.Type[AnyInfoVar],) \
    -> t.Mapping[int, AnyInfoVar]:
    join_mapping_statuses = 'JOIN mapping_statuses AS ms USING (item_id)'
    condition = "i.type = 'M' AND ms.enabled != 'D'"
    if info_type is item_infos.ResourceInfo:
        join_mapping_statuses = ''
        condition = "i.type = 'R'"

    cursor.execute(
        f'''
        SELECT
                ive.item_version_id,
                ive.definition,
                ive.repo,
                ive.repo_iteration
        FROM
                     item_versions_extra AS ive
                JOIN items               AS i  USING (item_id)
                {join_mapping_statuses}
        WHERE
                {condition};
        '''
    )

    result: dict[int, AnyInfoVar] = {}

    for item_version_id, definition, repo_name, repo_iteration \
        in cursor.fetchall():
        info = info_type.load(definition, repo_name, repo_iteration)
        if info.compatible:
            result[item_version_id] = info

    return result

def _get_current_required_state(
        cursor:                     sqlite3.Cursor,
        unlocked_required_mappings: t.Sequence[int]
) -> tuple[list[sds.MappingRequirement], list[sds.ResourceVersionRequirement]]:
    # For mappings explicitly enabled by the user (+ all mappings they
    # recursively depend on) let's make sure that their exact same versions will
    # be enabled after the change. Make exception for mappings specified by the
    # caller.
    # The mappings to make exception for are passed by their item_id's. First,
    # we compute a set of their corresponding item_version_id's.
    with base.temporary_ids_tables(
            cursor = cursor,
            tables = [
                ('__work_ids_0',   unlocked_required_mappings),
                ('__work_ids_1',   []),
                ('__unlocked_ids', [])
            ]
    ):
        cursor.execute(
            '''
            INSERT INTO
                    __work_ids_1
            SELECT
                    item_version_id
            FROM
                    item_versions
            WHERE
                    item_id IN __work_ids_0;
            '''
        )

        # Recursively update the our unlocked ids collection with all mapping
        # version ids that are required by mapping versions already referenced
        # there.
        work_tab = '__work_ids_1'
        next_tab = '__work_ids_0'

        while True:
            cursor.execute(f'SELECT COUNT(*) FROM {work_tab};')

            (count,), = cursor.fetchall()

            if count == 0:
                break

            cursor.execute(f'DELETE FROM {next_tab};')

            cursor.execute(
                f'''
                INSERT INTO
                        {next_tab}
                SELECT
                        item_version_id
                FROM
                             item_versions              AS iv
                        JOIN items                      AS i
                                USING (item_id)
                        JOIN mapping_statuses           AS ms
                                USING (item_id)
                        JOIN resolved_required_mappings AS rrm
                                ON iv.item_version_id = rrm.required_mapping_id
                WHERE
                        ms.enabled != 'E'                      AND
                        rrm.requiring_mapping_id IN {work_tab} AND
                        rrm.requiring_mapping_id NOT IN __unlocked_ids;
                '''
            )

            cursor.execute(
                f'''
                INSERT OR IGNORE INTO
                        __unlocked_ids
                SELECT
                        id
                FROM
                        {work_tab};
                '''
            )

            work_tab, next_tab = next_tab, work_tab

        # Describe all required mappings using requirement objects.
        cursor.execute(
            '''
            SELECT
                    ive.definition, ive.repo, ive.repo_iteration
            FROM
                         item_versions_extra AS ive
                    JOIN items               AS i USING (item_id)
            WHERE
                    i.type = 'M'                              AND
                    ive.item_version_id NOT IN __unlocked_ids AND
                    ive.active = 'R';
            ''',
        )

        rows = cursor.fetchall()

        mapping_requirements: list[sds.MappingRequirement] = []

        for definition, repo, iteration in rows:
            mapping_info = \
                item_infos.MappingInfo.load(definition, repo, iteration)
            mapping_req = sds.MappingVersionRequirement(
                identifier   = mapping_info.identifier,
                version_info = mapping_info
            )
            mapping_requirements.append(mapping_req)

        # Describe all required resources using requirement objects.
        cursor.execute(
            '''
            SELECT
                    i_m.identifier,
                    ive_r.definition, ive_r.repo, ive_r.repo_iteration
            FROM
                         resolved_depended_resources AS rdd
                    JOIN item_versions_extra         AS ive_r
                            ON rdd.resource_item_id = ive_r.item_version_id
                    JOIN payloads                    AS p
                            USING (payload_id)
                    JOIN item_versions               AS iv_m
                            ON p.mapping_item_id = iv_m.item_version_id
                    JOIN items                       AS i_m
                            ON iv_m.item_id = i_m.item_id
            WHERE
                    iv_m.item_version_id NOT IN __unlocked_ids AND
                    iv_m.active = 'R';
            ''',
        )

        rows = cursor.fetchall()

        resource_requirements: list[sds.ResourceVersionRequirement] = []

        for mapping_identifier, definition, repo, iteration in rows:
            resource_info = \
                item_infos.ResourceInfo.load(definition, repo, iteration)
            resource_req = sds.ResourceVersionRequirement(
                mapping_identifier = mapping_identifier,
                version_info       = resource_info
            )
            resource_requirements.append(resource_req)

    return (mapping_requirements, resource_requirements)

def _mark_version_installed(cursor: sqlite3.Cursor, version_id: int) -> None:
    cursor.execute(
        '''
        UPDATE
                item_versions
        SET
                installed = 'I'
        WHERE
                item_version_id = ?;
        ''',
        (version_id,)
    )

def _recompute_dependencies_no_state_update_no_pull_files(
        cursor:                     sqlite3.Cursor,
        unlocked_required_mappings: base.NoLockArg = [],
) -> None:
    cursor.execute('DELETE FROM payloads;')

    ids_to_resources = _get_infos_of_type(cursor, item_infos.ResourceInfo)
    ids_to_mappings  = _get_infos_of_type(cursor, item_infos.MappingInfo)

    resources_to_ids = dict((info, id) for id, info in ids_to_resources.items())
    mappings_to_ids  = dict((info, id) for id, info in ids_to_mappings.items())

    if unlocked_required_mappings != 'all_mappings_unlocked':
        mapping_reqs, resource_reqs = _get_current_required_state(
            cursor                     = cursor,
            unlocked_required_mappings = unlocked_required_mappings
        )
    else:
        mapping_reqs, resource_reqs = [], []

    cursor.execute(
        '''
        SELECT
                i.identifier
        FROM
                     mapping_statuses AS ms
                JOIN items            AS i  USING(item_id)
        WHERE
                ms.enabled = 'E' AND ms.frozen = 'N';
        '''
    )

    for mapping_identifier, in cursor.fetchall():
        mapping_reqs.append(sds.MappingRequirement(mapping_identifier))

    cursor.execute(
        '''
        SELECT
                active_version_id, frozen
        FROM
                mapping_statuses
        WHERE
                enabled = 'E' AND frozen IN ('R', 'E');
        '''
    )

    for active_version_id, frozen in cursor.fetchall():
        info = ids_to_mappings[active_version_id]

        requirement: sds.MappingRequirement

        if frozen == 'R':
            requirement = sds.MappingRepoRequirement(info.identifier, info.repo)
        else:
            requirement = sds.MappingVersionRequirement(info.identifier, info)

        mapping_reqs.append(requirement)

    mapping_choices = sds.compute_payloads(
        resources             = ids_to_resources.values(),
        mappings              = ids_to_mappings.values(),
        mapping_requirements  = mapping_reqs,
        resource_requirements = resource_reqs
    )

    cursor.execute(
        '''
        UPDATE
                mapping_statuses
        SET
                active_version_id = NULL
        WHERE
                enabled != 'E';
        '''
    )

    cursor.execute("UPDATE item_versions SET active = 'N';")

    cursor.execute('DELETE FROM payloads;')

    cursor.execute('DELETE FROM resolved_required_mappings;')

    for choice in mapping_choices.values():
        mapping_ver_id = mappings_to_ids[choice.info]

        if choice.required:
            _mark_version_installed(cursor, mapping_ver_id)

        cursor.execute(
            '''
            SELECT
                    item_id
            FROM
                    item_versions
            WHERE
                    item_version_id = ?;
            ''',
            (mapping_ver_id,)
        )

        (mapping_item_id,), = cursor.fetchall()

        cursor.execute(
            '''
            UPDATE
                    mapping_statuses
            SET
                    active_version_id = ?
            WHERE
                    item_id = ?;
            ''',
            (mapping_ver_id, mapping_item_id)
        )

        cursor.execute(
            '''
            UPDATE
                    item_versions
            SET
                    active = ?
            WHERE
                    item_version_id = ?;
            ''',
            ('R' if choice.required else 'A', mapping_ver_id)
        )

        for depended_mapping_info in choice.mapping_dependencies:
            cursor.execute(
                '''
                INSERT INTO resolved_required_mappings(
                        requiring_mapping_id,
                        required_mapping_id
                )
                VALUES (?, ?);
                ''',
                (mapping_ver_id, mappings_to_ids[depended_mapping_info])
            )

        for num, (pattern, payload) in enumerate(choice.payloads.items()):
            cursor.execute(
                '''
                INSERT INTO payloads(
                        mapping_item_id,
                        pattern,
                        eval_allowed,
                        cors_bypass_allowed
                )
                VALUES (?, ?, ?, ?);
                ''',
                (
                    mapping_ver_id,
                    pattern.orig_url,
                    payload.allows_eval,
                    payload.allows_cors_bypass
                )
            )

            cursor.execute(
                '''
                SELECT
                        payload_id
                FROM
                        payloads
                WHERE
                        mapping_item_id = ? AND pattern = ?;
                ''',
                (mapping_ver_id, pattern.orig_url)
            )

            (payload_id,), = cursor.fetchall()

            for res_num, resource_info in enumerate(payload.resources):
                resource_ver_id = resources_to_ids[resource_info]

                if choice.required:
                    _mark_version_installed(cursor, resource_ver_id)

                cursor.execute(
                    '''
                    INSERT INTO resolved_depended_resources(
                            payload_id,
                            resource_item_id,
                            idx
                    )
                    VALUES(?, ?, ?);
                    ''',
                    (payload_id, resource_ver_id, res_num)
                )

                new_status = 'R' if choice.required else 'A'

                cursor.execute(
                    '''
                    UPDATE
                            item_versions
                    SET
                            active = (
                                    CASE
                                    WHEN active = 'R' OR ? = 'R' THEN 'R'
                                    WHEN active = 'A' OR ? = 'A' THEN 'A'
                                    ELSE 'N'
                                    END
                            )
                    WHERE
                            item_version_id = ?;
                    ''',
                    (new_status, new_status, resource_ver_id)
                )


def _recompute_dependencies_no_state_update(
        cursor:                     sqlite3.Cursor,
        unlocked_required_mappings: base.NoLockArg = [],
        semirepo_file_resolver:     FileResolver   = DummyFileResolver()
) -> None:
    _recompute_dependencies_no_state_update_no_pull_files(
        cursor                     = cursor,
        unlocked_required_mappings = unlocked_required_mappings
    )

    pull_missing_files(cursor, semirepo_file_resolver)
