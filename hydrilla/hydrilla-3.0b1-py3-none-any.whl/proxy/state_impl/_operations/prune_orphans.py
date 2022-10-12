# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (removal of packages that are not used).
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

from pathlib import Path


def _remove_item_versions(cursor: sqlite3.Cursor, with_installed: bool) -> None:
    cursor.execute(
        '''
        CREATE TEMPORARY TABLE __removed_versions(
                item_version_id INTEGER PRIMARY KEY
        );
        '''
    )

    condition = "iv.active != 'R'" if with_installed else "iv.installed != 'I'"

    cursor.execute(
        f'''
        INSERT INTO
                __removed_versions
        SELECT
                iv.item_version_id
        FROM
                     item_versions     AS iv
                JOIN orphan_iterations AS oi USING (repo_iteration_id)
        WHERE
                {condition};
        '''
    )

    cursor.execute(
        '''
        UPDATE
                mapping_statuses
        SET
                active_version_id = NULL
        WHERE
                active_version_id IN __removed_versions;
        '''
    )

    cursor.execute(
        '''
        DELETE FROM
                item_versions
        WHERE
                item_version_id IN __removed_versions;
        '''
    )

    cursor.execute('DROP TABLE __removed_versions;')

_remove_items_sql = '''
WITH removed_items AS (
        SELECT
                i.item_id
        FROM
                          items            AS i
                LEFT JOIN item_versions    AS iv USING (item_id)
                LEFT JOIN mapping_statuses AS ms USING (item_id)
        WHERE
                 iv.item_version_id IS NULL AND
                 (i.type = 'R' OR ms.enabled = 'N')
)
DELETE FROM
        items
WHERE
        item_id IN removed_items;
'''

_remove_files_sql = '''
WITH removed_files AS (
        SELECT
                f.file_id
        FROM
                          files     AS f
                LEFT JOIN file_uses AS fu USING (file_id)
        WHERE
                fu.file_use_id IS NULL
)
DELETE FROM
        files
WHERE
        file_id IN removed_files;
'''

_forget_files_data_sql = '''
WITH forgotten_files AS (
        SELECT
                f.file_id
        FROM
                          files         AS f
                     JOIN file_uses     AS fu
                        USING (file_id)
                LEFT JOIN item_versions AS iv
                        ON (fu.item_version_id = iv.item_version_id AND
                            iv.installed = 'I')
        GROUP BY
                f.file_id
        HAVING
                COUNT(iv.item_version_id) = 0
)
UPDATE
        files
SET
        data = NULL
WHERE
        file_id IN forgotten_files;
'''

_remove_repo_iterations_sql = '''
WITH removed_iterations AS (
        SELECT
                oi.repo_iteration_id
        FROM
                          orphan_iterations AS oi
                LEFT JOIN item_versions     AS iv USING (repo_iteration_id)
        WHERE
                iv.item_version_id IS NULL
)
DELETE FROM
        repo_iterations
WHERE
        repo_iteration_id IN removed_iterations;
'''

_remove_repos_sql = '''
WITH removed_repos AS (
        SELECT
                r.repo_id
        FROM
                          repos           AS r
                LEFT JOIN repo_iterations AS ri USING (repo_id)
        WHERE
                r.deleted AND ri.repo_iteration_id IS NULL AND r.repo_id != 1
)
DELETE FROM
        repos
WHERE
        repo_id IN removed_repos;
'''

def prune_orphans(cursor: sqlite3.Cursor, aggressive: bool = False) -> None:
    assert cursor.connection.in_transaction

    _remove_item_versions(cursor, with_installed=aggressive)
    cursor.execute(_remove_items_sql)
    cursor.execute(_remove_files_sql)
    cursor.execute(_forget_files_data_sql)
    cursor.execute(_remove_repo_iterations_sql)
    cursor.execute(_remove_repos_sql)
