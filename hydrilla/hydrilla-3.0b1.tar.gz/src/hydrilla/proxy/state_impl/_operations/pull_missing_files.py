# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (download of package files).
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
import hashlib

from abc import ABC, abstractmethod
from pathlib import Path
from urllib.parse import urljoin

import requests

from ... import state


class FileResolver(ABC):
    @abstractmethod
    def by_sha256(self, sha256: str) -> bytes:
        ...

class DummyFileResolver(FileResolver):
    def by_sha256(self, sha256: str) -> bytes:
        raise NotImplementedError()

def pull_missing_files(
        cursor:                 sqlite3.Cursor,
        semirepo_file_resolver: FileResolver = DummyFileResolver()
) -> None:
    cursor.execute(
        '''
        SELECT DISTINCT
                f.file_id, f.sha256,
                r.repo_id, r.url
        FROM
                     repos           AS R
                JOIN repo_iterations AS ri USING (repo_id)
                JOIN item_versions   AS iv USING (repo_iteration_id)
                JOIN file_uses       AS fu USING (item_version_id)
                JOIN files           AS f  USING (file_id)
        WHERE
                iv.installed = 'I' AND f.data IS NULL;
        '''
    )

    rows = cursor.fetchall()

    for file_id, sha256, repo_id, repo_url in rows:
        if repo_id == 1:
            file_bytes = semirepo_file_resolver.by_sha256(sha256)
        else:
            try:
                url = urljoin(repo_url, f'file/sha256/{sha256}')
                response = requests.get(url)

                assert response.ok

                file_bytes = response.content
            except:
                raise state.FileMissingError(
                    repo_id = str(repo_id),
                    sha256  = sha256
                )

        computed_sha256 = hashlib.sha256(file_bytes).digest().hex()
        if computed_sha256 != sha256:
            raise state.FileIntegrityError(
                repo_id        = str(repo_id),
                sha256         = sha256,
                invalid_sha256 = computed_sha256
            )

        cursor.execute(
            '''
            UPDATE
                    files
            SET
                    data = ?
            WHERE
                    file_id = ?;
            ''',
            (file_bytes, file_id)
        )
