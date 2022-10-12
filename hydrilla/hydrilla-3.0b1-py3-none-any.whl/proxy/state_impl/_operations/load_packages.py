# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (import of packages from disk files).
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

import io
import mimetypes
import sqlite3
import hashlib
import dataclasses as dc
import typing as t

from pathlib import Path, PurePosixPath

from .... import versions
from .... import item_infos
from ... import state
from .recompute_dependencies import _recompute_dependencies_no_state_update, \
    FileResolver
from .prune_orphans import prune_orphans

def make_repo_iteration(cursor: sqlite3.Cursor, repo_id: int) -> int:
    cursor.execute(
        '''
        SELECT
                next_iteration
        FROM
                repos
        WHERE
                repo_id = ?;
        ''',
        (repo_id,)
    )

    (next_iteration,), = cursor.fetchall()

    cursor.execute(
        '''
        INSERT INTO repo_iterations(repo_id, iteration)
        VALUES(?, ?);
        ''',
        (repo_id, next_iteration)
    )

    cursor.execute(
        '''
        SELECT
                repo_iteration_id
        FROM
                repo_iterations
        WHERE
                repo_id = ? AND iteration = ?;
        ''',
        (repo_id, next_iteration)
    )

    (repo_iteration_id,), = cursor.fetchall()

    cursor.execute(
        '''
        UPDATE
                repos
        SET
                next_iteration = ?,
                active_iteration_id = (
                        CASE
                        WHEN repo_id = 1 THEN NULL
                        ELSE ?
                        END
                ),
                last_refreshed = (
                        CASE
                        WHEN repo_id = 1 THEN NULL
                        ELSE STRFTIME('%s', 'NOW')
                        END
                )
        WHERE
                repo_id = ?;
        ''',
        (next_iteration + 1, repo_iteration_id, repo_id)
    )

    return repo_iteration_id

def get_or_make_item(cursor: sqlite3.Cursor, type: str, identifier: str) -> int:
    type_letter = {'resource': 'R', 'mapping': 'M'}[type]

    cursor.execute(
        '''
        INSERT OR IGNORE INTO items(type, identifier)
        VALUES(?, ?);
        ''',
        (type_letter, identifier)
    )

    cursor.execute(
        '''
        SELECT
                item_id
        FROM
                items
        WHERE
                type = ? AND identifier = ?;
        ''',
        (type_letter, identifier)
    )

    (item_id,), = cursor.fetchall()

    return item_id

def update_or_make_item_version(
        cursor:            sqlite3.Cursor,
        item_id:           int,
        version:           versions.VerTuple,
        installed:         str,
        repo_iteration_id: int,
        repo_id:           int,
        definition:        bytes
) -> int:
    ver_str = versions.version_string(version)

    definition_sha256 = hashlib.sha256(definition).digest().hex()

    cursor.execute(
        '''
        SELECT
                item_version_id
        FROM
                item_versions AS iv
                JOIN repo_iterations AS ri USING (repo_iteration_id)
                JOIN repos           AS r  USING (repo_id)
        WHERE
                r.repo_id = ? AND iv.definition_sha256 = ?;
        ''',
        (repo_id, definition_sha256)
    )

    rows = cursor.fetchall()

    if rows != []:
        (item_version_id,), = rows
        cursor.execute(
            '''
            UPDATE
                    item_versions
            SET
                    installed = (
                            CASE
                            WHEN installed = 'I' OR ? = 'I' THEN 'I'
                            ELSE 'N'
                            END
                    ),
                    repo_iteration_id = ?
            WHERE
                    item_version_id = ?;
            ''',
            (installed, repo_iteration_id, item_version_id)
        )

        return item_version_id

    cursor.execute(
        '''
        INSERT INTO item_versions(
                item_id,
                version,
                installed,
                repo_iteration_id,
                definition,
                definition_sha256
        )
        VALUES(?, ?, ?, ?, ?, ?);
        ''',
        (item_id, ver_str, installed, repo_iteration_id, definition,
         definition_sha256)
    )

    cursor.execute(
        '''
        SELECT
                item_version_id
        FROM
                item_versions
        WHERE
                item_id = ? AND version = ? AND repo_iteration_id = ?;
        ''',
        (item_id, ver_str, repo_iteration_id)
    )

    (item_version_id,), = cursor.fetchall()

    return item_version_id

def make_mapping_status(cursor: sqlite3.Cursor, item_id: int) -> None:
    cursor.execute(
        'INSERT OR IGNORE INTO mapping_statuses(item_id) VALUES(?);',
        (item_id,)
    )

def get_or_make_file(cursor: sqlite3.Cursor, sha256: str) -> int:
    cursor.execute('INSERT OR IGNORE INTO files(sha256) VALUES(?);', (sha256,))

    cursor.execute('SELECT file_id FROM files WHERE sha256 = ?;', (sha256,))

    (file_id,), = cursor.fetchall()

    return file_id

def make_file_use(
        cursor:          sqlite3.Cursor,
        item_version_id: int,
        file_id:         int,
        name:            str,
        type:            str,
        mime_type:       str,
        idx:             int
) -> None:
    cursor.execute(
        '''
        INSERT OR IGNORE INTO file_uses(
                item_version_id,
                file_id,
                name,
                type,
                mime_type,
                idx
        )
        VALUES(?, ?, ?, ?, ?, ?);
        ''',
        (item_version_id, file_id, name, type, mime_type, idx)
    )

@dc.dataclass(frozen=True)
class _FileInfo:
    id:        int
    extension: str

def _add_item(
        cursor:                sqlite3.Cursor,
        info:                  item_infos.AnyInfo,
        definition:            bytes,
        repo_iteration_id:     int,
        repo_id:               int
) -> None:
    item_id = get_or_make_item(cursor, info.type.value, info.identifier)

    if isinstance(info, item_infos.MappingInfo):
        make_mapping_status(cursor, item_id)

    item_version_id = update_or_make_item_version(
        cursor            = cursor,
        item_id           = item_id,
        version           = info.version,
        installed         = 'I' if repo_id == 1 else 'N',
        repo_iteration_id = repo_iteration_id,
        repo_id           = repo_id,
        definition        = definition
    )

    file_infos = {}

    file_specifiers = [*info.source_copyright]
    if isinstance(info, item_infos.ResourceInfo):
        file_specifiers.extend(info.scripts)

    for file_spec in file_specifiers:
        file_id = get_or_make_file(cursor, file_spec.sha256)

        suffix = PurePosixPath(file_spec.name).suffix

        file_infos[file_spec.sha256] = _FileInfo(file_id, suffix)

    for idx, file_spec in enumerate(info.source_copyright):
        file_info = file_infos[file_spec.sha256]

        mime = mimetypes.types_map.get(file_info.extension)
        if mime is None:
            mime = mimetypes.common_types.get(file_info.extension)
        if mime is None:
            mime = 'application/octet-stream'
        if mime is None and file_info.extension == '.spdx':
            # We don't know of any estabilished mime type for tag-value SPDX
            # reports. Let's use the following for now.
            mime = 'text/spdx'

        make_file_use(
            cursor,
            item_version_id = item_version_id,
            file_id         = file_info.id,
            name            = file_spec.name,
            type            = 'L',
            mime_type       = mime,
            idx             = idx
        )

    if isinstance(info, item_infos.MappingInfo):
        return

    for idx, file_spec in enumerate(info.scripts):
        file_info = file_infos[file_spec.sha256]
        make_file_use(
            cursor,
            item_version_id = item_version_id,
            file_id         = file_info.id,
            name            = file_spec.name,
            type            = 'W',
            mime_type       = 'application/javascript',
            idx             = idx
        )

AnyInfoVar = t.TypeVar(
    'AnyInfoVar',
    item_infos.ResourceInfo,
    item_infos.MappingInfo
)

def _read_items(malcontent_path: Path, info_class: t.Type[AnyInfoVar]) \
    -> t.Iterator[tuple[AnyInfoVar, bytes]]:
    item_type_path = malcontent_path / info_class.type.value
    if not item_type_path.is_dir():
        return

    for item_path in item_type_path.iterdir():
        if not item_path.is_dir():
            continue

        for item_version_path in item_path.iterdir():
            definition = item_version_path.read_bytes()
            item_info = info_class.load(definition)

            assert item_info.identifier == item_path.name
            assert versions.version_string(item_info.version) == \
                item_version_path.name

            yield item_info, definition

@dc.dataclass(frozen=True)
class MalcontentFileResolver(FileResolver):
    malcontent_dir_path: Path

    def by_sha256(self, sha256: str) -> bytes:
        file_path = self.malcontent_dir_path / 'file' / 'sha256' / sha256
        if not file_path.is_file():
             raise state.FileMissingError(repo_id='1', sha256=sha256)

        return file_path.read_bytes()

def _load_packages_no_state_update(
        cursor:                sqlite3.Cursor,
        malcontent_path:       Path,
        repo_id:               int
) -> int:
    assert cursor.connection.in_transaction

    repo_iteration_id = make_repo_iteration(cursor, repo_id)

    for type in [item_infos.ItemType.RESOURCE, item_infos.ItemType.MAPPING]:
        info: item_infos.AnyInfo
        for info, definition in _read_items( # type: ignore
                malcontent_path,
                type.info_class
        ):
            _add_item(
                cursor            = cursor,
                info              = info,
                definition        = definition,
                repo_iteration_id = repo_iteration_id,
                repo_id           = repo_id
            )

    if repo_id != 1:
        # In case of local semirepo (repo_id = 1) all packages from previous
        # iteration are already orphans and can be assumed to be in a pruned
        # state no matter what.
        prune_orphans(cursor)

    _recompute_dependencies_no_state_update(
        cursor                     = cursor,
        unlocked_required_mappings = [],
        semirepo_file_resolver     = MalcontentFileResolver(malcontent_path)
    )

    return repo_iteration_id
