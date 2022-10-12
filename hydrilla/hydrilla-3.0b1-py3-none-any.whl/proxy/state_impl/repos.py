# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (RepoRef and RepoStore subtypes).
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
This module provides an interface to interact with repositories configured
inside Haketilo.
"""

import re
import json
import tempfile
import sqlite3
import typing as t
import dataclasses as dc

from urllib.parse import urlparse, urljoin
from datetime import datetime
from pathlib import Path

import requests

from ... import json_instances
from ... import item_infos
from ... import versions
from .. import state as st
from .. import simple_dependency_satisfying as sds
from . import base


repo_name_regex = re.compile(r'''
^
(?:
  []a-zA-Z0-9()<>^&$.!,?@#|;:%"'*{}[/_=+-]+ # allowed non-whitespace characters

  (?: # optional additional words separated by single spaces
    [ ]
    []a-zA-Z0-9()<>^&$.!,?@#|;:%"'*{}[/_=+-]+
  )*
)
$
''', re.VERBOSE)

def sanitize_repo_name(name: str) -> str:
    name = name.strip()

    if repo_name_regex.match(name) is None:
        raise st.RepoNameInvalid()

    return name


def sanitize_repo_url(url: str) -> str:
    try:
        parsed = urlparse(url)
    except:
        raise st.RepoUrlInvalid()

    if parsed.scheme not in ('http', 'https'):
        raise st.RepoUrlInvalid()

    if url[-1] != '/':
        url = url + '/'

    return url


def ensure_repo_not_deleted(cursor: sqlite3.Cursor, repo_id: str) -> None:
    cursor.execute(
        'SELECT deleted FROM repos WHERE repo_id = ?;',
        (repo_id,)
    )

    rows = cursor.fetchall()

    if rows == []:
        raise st.MissingItemError()

    (deleted,), = rows

    if deleted:
        raise st.MissingItemError()


def sync_remote_repo_definitions(repo_url: str, dest: Path) -> None:
    try:
        list_all_response = requests.get(urljoin(repo_url, 'list_all'))
        assert list_all_response.ok

        list_instance = list_all_response.json()
    except:
        raise st.RepoCommunicationError()

    try:
        json_instances.validate_instance(
            list_instance,
            'api_package_list-{}.schema.json'
        )
    except json_instances.UnknownSchemaError:
        raise st.RepoApiVersionUnsupported()
    except:
        raise st.RepoCommunicationError()

    ref: dict[str, t.Any]

    for item_type_name in ('resource', 'mapping'):
        for ref in list_instance[item_type_name + 's']:
            ver = versions.version_string(versions.normalize(ref['version']))
            item_rel_path = f'{item_type_name}/{ref["identifier"]}/{ver}'

            try:
                item_response = requests.get(urljoin(repo_url, item_rel_path))
                assert item_response.ok
            except:
                raise st.RepoCommunicationError()

            item_path = dest / item_rel_path
            item_path.parent.mkdir(parents=True, exist_ok=True)
            item_path.write_bytes(item_response.content)


def make_repo_display_info(
        ref:            st.RepoRef,
        name:           str,
        url:            str,
        deleted:        bool,
        last_refreshed: t.Optional[int],
        resource_count: int,
        mapping_count:  int
) -> st.RepoDisplayInfo:
        last_refreshed_converted: t.Optional[datetime] = None
        if last_refreshed is not None:
            last_refreshed_converted = datetime.fromtimestamp(last_refreshed)

        return st.RepoDisplayInfo(
            ref               = ref,
            is_local_semirepo = ref.id == '1',
            name              = name,
            url               = url,
            deleted           = deleted,
            last_refreshed    = last_refreshed_converted,
            resource_count    = resource_count,
            mapping_count     = mapping_count
        )


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteRepoRef(st.RepoRef):
    """...."""
    state: base.HaketiloStateWithFields = dc.field(hash=False, compare=False)

    def remove(self) -> None:
        with self.state.cursor(transaction=True) as cursor:
            ensure_repo_not_deleted(cursor, self.id)

            cursor.execute(
                '''
                UPDATE
                        repos
                SET
                        deleted             = TRUE,
                        url                 = '',
                        active_iteration_id = NULL,
                        last_refreshed      = NULL
                WHERE
                        repo_id = ?;
                ''',
                (self.id,)
            )

            self.state.soft_prune_orphan_items()
            self.state.recompute_dependencies()

    def update(
            self,
            *,
            name: t.Optional[str] = None,
            url:  t.Optional[str] = None
    ) -> None:
        if name is not None:
            if name.isspace():
                raise st.RepoNameInvalid()

            name = sanitize_repo_name(name)

        if url is not None:
            if url.isspace():
                raise st.RepoUrlInvalid()

            url = sanitize_repo_url(url)

        if name is None and url is None:
            return

        with self.state.cursor(transaction=True) as cursor:
            ensure_repo_not_deleted(cursor, self.id)

            if url is not None:
                cursor.execute(
                    'UPDATE repos SET url = ? WHERE repo_id = ?;',
                    (url, self.id)
                )

            if name is not None:
                try:
                    cursor.execute(
                        'UPDATE repos SET name = ? WHERE repo_id = ?;',
                        (name, self.id)
                    )
                except sqlite3.IntegrityError:
                    raise st.RepoNameTaken()

                self.state.rebuild_structures(rules=False)

    def refresh(self) -> None:
        with self.state.cursor(transaction=True) as cursor:
            ensure_repo_not_deleted(cursor, self.id)

            cursor.execute(
                'SELECT url FROM repos WHERE repo_id = ?;',
                (self.id,)
            )

            (repo_url,), = cursor.fetchall()

            with tempfile.TemporaryDirectory() as tmpdir_str:
                tmpdir = Path(tmpdir_str)
                sync_remote_repo_definitions(repo_url, tmpdir)
                self.state.import_items(tmpdir, int(self.id))

    def get_display_info(self) -> st.RepoDisplayInfo:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        name, url, deleted, last_refreshed,
                        resource_count, mapping_count
                FROM
                        repo_display_infos
                WHERE
                        repo_id = ?;
                ''',
                (self.id,)
            )

            rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        row, = rows

        return make_repo_display_info(self, *row)


@dc.dataclass(frozen=True)
class ConcreteRepoStore(st.RepoStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.RepoRef:
        return ConcreteRepoRef(str(int(id)), self.state)

    def add(self, name: str, url: str) -> st.RepoRef:
        name = name.strip()
        if repo_name_regex.match(name) is None:
            raise st.RepoNameInvalid()

        url = sanitize_repo_url(url)

        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                '''
                SELECT
                        COUNT(repo_id)
                FROM
                        repos
                WHERE
                        NOT deleted AND name = ?;
                ''',
                (name,)
            )
            (name_taken,), = cursor.fetchall()

            if name_taken:
                raise st.RepoNameTaken()

            cursor.execute(
                '''
                INSERT INTO repos(name, url)
                VALUES (?, ?)
                ON CONFLICT (name)
                DO UPDATE SET
                        name           = excluded.name,
                        url            = excluded.url,
                        deleted        = FALSE,
                        last_refreshed = NULL;
                ''',
                (name, url)
            )

            cursor.execute('SELECT repo_id FROM repos WHERE name = ?;', (name,))

            (repo_id,), = cursor.fetchall()

            return ConcreteRepoRef(str(repo_id), self.state)

    def get_display_infos(self, include_deleted: bool = False) \
        -> t.Sequence[st.RepoDisplayInfo]:
        with self.state.cursor() as cursor:
            condition: str = 'TRUE'
            if include_deleted:
                condition = 'COALESCE(deleted = FALSE, TRUE)'

            cursor.execute(
                f'''
                SELECT
                        repo_id, name, url, deleted, last_refreshed,
                        resource_count, mapping_count
                FROM
                        repo_display_infos
                WHERE
                        {condition}
                ORDER BY
                        repo_id != 1, name;
                '''
            )

            all_rows = cursor.fetchall()

        assert len(all_rows) > 0 and all_rows[0][0] == 1

        result = []
        for row in all_rows:
            repo_id, *rest = row

            ref = ConcreteRepoRef(str(repo_id), self.state)

            result.append(make_repo_display_info(ref, *rest))

        return result
