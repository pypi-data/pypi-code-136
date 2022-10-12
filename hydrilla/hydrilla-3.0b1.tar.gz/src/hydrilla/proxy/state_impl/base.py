# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (definition of fields of a class that
# will implement HaketiloState).
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
This module defines fields that will later be part of a concrete HaketiloState
subtype.
"""

import sqlite3
import threading
import secrets
import dataclasses as dc
import typing as t

from pathlib import Path
from contextlib import contextmanager
from abc import abstractmethod

from ... import url_patterns
from ... import pattern_tree
from .. import simple_dependency_satisfying as sds
from .. import state as st
from .. import policies


@contextmanager
def temporary_ids_tables(
        cursor: sqlite3.Cursor,
        tables: t.Iterable[tuple[str, t.Iterable[int]]]
) -> t.Iterator[None]:
    created: set[str] = set()

    try:
        for name, ids in tables:
            cursor.execute(
                f'CREATE TEMPORARY TABLE "{name}"(id INTEGER PRIMARY KEY);'
            )
            created.add(name)

            for id in ids:
                cursor.execute(f'INSERT INTO "{name}" VALUES(?);', (id,))

        yield
    finally:
        for name in created:
            cursor.execute(f'DROP TABLE "{name}";')


@dc.dataclass(frozen=True)
class PolicyTree(pattern_tree.PatternTree[policies.PolicyFactory]):
    SelfType = t.TypeVar('SelfType', bound='PolicyTree')

    def register_payload(
            self:        'SelfType',
            pattern:     url_patterns.ParsedPattern,
            payload_key: st.PayloadKey,
            token:       str
    ) -> 'SelfType':
        payload_policy_factory = policies.PayloadPolicyFactory(
            builtin     = False,
            payload_key = payload_key
        )

        policy_tree = self.register(pattern, payload_policy_factory)

        resource_policy_factory = policies.PayloadResourcePolicyFactory(
            builtin     = False,
            payload_key = payload_key
        )

        policy_tree = policy_tree.register(
            pattern.path_append(token, '***'),
            resource_policy_factory
        )

        return policy_tree

def mark_failed_file_installs(
        cursor:      sqlite3.Cursor,
        file_sha256: str,
        repo_id:     int
) -> None:
    cursor.execute(
        '''
        WITH failed_items AS (
                SELECT DISTINCT
                        item_version_id
                FROM
                             files               AS f
                        JOIN file_uses           AS fu USING (file_id)
                        JOIN item_versions_extra AS ive USING (item_version_id)
                WHERE
                        f.sha256 = ? AND f.data IS NULL AND ive.repo_id = ?
        )
        UPDATE
                item_versions
        SET
                installed = 'F'
        WHERE
                item_version_id IN failed_items;
        ''',
        (file_sha256, repo_id)
    )

NoLockArg = t.Union[t.Sequence[int], t.Literal['all_mappings_unlocked']]

PayloadsData = t.Mapping[st.PayloadRef, st.PayloadData]

# mypy needs to be corrected:
# https://stackoverflow.com/questions/70999513/conflict-between-mix-ins-for-abstract-dataclasses/70999704#70999704
@dc.dataclass # type: ignore[misc]
class HaketiloStateWithFields(st.HaketiloState):
    """...."""
    store_dir:      Path
    connection:     sqlite3.Connection
    settings:       st.HaketiloGlobalSettings
    current_cursor: t.Optional[sqlite3.Cursor] = None

    secret: bytes = dc.field(default_factory=(lambda: secrets.token_bytes(16)))

    policy_tree:   PolicyTree   = PolicyTree()
    payloads_data: PayloadsData = dc.field(default_factory=dict)

    lock: threading.RLock = dc.field(default_factory=threading.RLock)

    @contextmanager
    def cursor(self, transaction: bool = False) \
        -> t.Iterator[sqlite3.Cursor]:
        with self.lock:
            start_transaction = \
                transaction and not self.connection.in_transaction

            if self.current_cursor is not None:
                yield self.current_cursor
                return

            try:
                self.current_cursor = self.connection.cursor()

                if start_transaction:
                    self.current_cursor.execute('BEGIN TRANSACTION;')

                try:
                    yield self.current_cursor

                    if start_transaction:
                        assert self.connection.in_transaction
                        self.current_cursor.execute('COMMIT TRANSACTION;')
                except:
                    if start_transaction:
                        self.current_cursor.execute('ROLLBACK TRANSACTION;')
                    raise
            except st.FileInstallationError as ex:
                if start_transaction:
                    assert self.current_cursor is not None
                    mark_failed_file_installs(
                        cursor      = self.current_cursor,
                        file_sha256 = ex.sha256,
                        repo_id     = int(ex.repo_id)
                    )
                raise
            finally:
                self.current_cursor = None

    def select_policy(self, url: url_patterns.ParsedUrl) -> policies.Policy:
        """...."""
        with self.lock:
            policy_tree = self.policy_tree

        try:
            best_priority: int                         = 0
            best_policy:   t.Optional[policies.Policy] = None

            for factories_set in policy_tree.search(url):
                for stored_factory in sorted(factories_set):
                    factory = stored_factory.item

                    policy = factory.make_policy(self)

                    if policy.priority > best_priority:
                        best_priority = policy.priority
                        best_policy   = policy
        except Exception as e:
            return policies.ErrorBlockPolicy(
                builtin = True,
                error   = e
            )

        if best_policy is not None:
            return best_policy

        if self.get_settings().default_allow_scripts:
            return policies.FallbackAllowPolicy()
        else:
            return policies.FallbackBlockPolicy()

    @abstractmethod
    def import_items(self, malcontent_path: Path, repo_id: int = 1) -> None:
        ...

    @abstractmethod
    def soft_prune_orphan_items(self) -> None:
        ...

    @abstractmethod
    def recompute_dependencies(
            self,
            unlocked_required_mappings: NoLockArg = []
    ) -> None:
        ...

    @abstractmethod
    def pull_missing_files(self) -> None:
        """
        This function checks which packages marked as installed are missing
        files in the database. It attempts to restore integrity by downloading
        the files from their respective repositories.
        """
        ...

    @abstractmethod
    def rebuild_structures(self, *, payloads: bool = True, rules: bool = True) \
        -> None:
        """
        Recreation of data structures as done after every recomputation of
        dependencies as well as at startup.
        """
        ...
