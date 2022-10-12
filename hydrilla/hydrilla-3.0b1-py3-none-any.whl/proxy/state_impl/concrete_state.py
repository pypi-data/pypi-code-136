# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (instantiatable HaketiloState subtype).
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
This module contains logic for keeping track of all settings, rules, mappings
and resources.
"""

import sqlite3
import secrets
import typing as t
import dataclasses as dc

from pathlib import Path

from ...exceptions import HaketiloException
from ...translations import smart_gettext as _
from ... import url_patterns
from ... import item_infos
from .. import state as st
from .. import policies
from .. import simple_dependency_satisfying as sds
from . import base
from . import rules
from . import items
from . import repos
from . import payloads
from . import _operations


here = Path(__file__).resolve().parent


def _prepare_database(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    try:
        cursor.execute(
            '''
            SELECT
                    COUNT(name)
            FROM
                    sqlite_master
            WHERE
                    name = 'general' AND type = 'table';
            '''
        )

        (db_initialized,), = cursor.fetchall()

        if not db_initialized:
            cursor.executescript((here / 'tables.sql').read_text())
        else:
            cursor.execute(
                '''
                SELECT
                        haketilo_version
                FROM
                        general;
                '''
            )

            (db_haketilo_version,) = cursor.fetchone()
            if db_haketilo_version != '3.0b1':
                raise HaketiloException(_('err.proxy.unknown_db_schema'))

        cursor.execute('PRAGMA FOREIGN_KEYS;')
        if cursor.fetchall() == []:
            raise HaketiloException(_('err.proxy.no_sqlite_foreign_keys'))

        cursor.execute('PRAGMA FOREIGN_KEYS=ON;')
    finally:
        cursor.close()


def load_settings(cursor: sqlite3.Cursor) -> st.HaketiloGlobalSettings:
    cursor.execute(
        '''
        SELECT
                default_allow_scripts,
                advanced_user,
                repo_refresh_seconds,
                mapping_use_mode
        FROM
                general
        '''
    )

    (default_allow_scripts, advanced_user, repo_refresh_seconds,
     mapping_use_mode), = cursor.fetchall()

    return st.HaketiloGlobalSettings(
        default_allow_scripts = default_allow_scripts,
        advanced_user         = advanced_user,
        repo_refresh_seconds  = repo_refresh_seconds,
        mapping_use_mode      = st.MappingUseMode(mapping_use_mode)
    )

@dc.dataclass
class ConcreteHaketiloState(base.HaketiloStateWithFields):
    def __post_init__(self) -> None:
        self.rebuild_structures()

    def import_items(self, malcontent_path: Path, repo_id: int = 1) -> None:
        with self.cursor(transaction=(repo_id == 1)) as cursor:
            # This method without the repo_id argument exposed is part of the
            # state API. As such, calls with repo_id = 1 (imports of local
            # semirepo packages) create a new transaction. Calls with different
            # values of repo_id are assumed to originate from within the state
            # implementation code and expect an existing transaction. Here, we
            # verify the transaction is indeed present.
            assert self.connection.in_transaction

            _operations._load_packages_no_state_update(
                cursor          = cursor,
                malcontent_path = malcontent_path,
                repo_id         = repo_id
            )

            self.rebuild_structures(rules=False)

    def count_orphan_items(self) -> st.OrphanItemsStats:
        with self.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        COALESCE(SUM(i.type = 'M'), 0),
                        COALESCE(SUM(i.type = 'R'), 0)
                FROM
                             item_versions     AS iv
                        JOIN items             AS i  USING (item_id)
                        JOIN orphan_iterations AS oi USING (repo_iteration_id)
                WHERE
                        iv.active != 'R';
                '''
            )

            (orphan_mappings, orphan_resources), = cursor.fetchall()

        return st.OrphanItemsStats(orphan_mappings, orphan_resources)

    def prune_orphan_items(self) -> None:
        with self.cursor(transaction=True) as cursor:
            _operations.prune_orphans(cursor, aggressive=True)

            self.recompute_dependencies()

    def soft_prune_orphan_items(self) -> None:
        with self.cursor() as cursor:
            assert self.connection.in_transaction

            _operations.prune_orphans(cursor)

    def recompute_dependencies(
            self,
            unlocked_required_mappings: base.NoLockArg = []
    ) -> None:
        with self.cursor() as cursor:
            assert self.connection.in_transaction

            _operations._recompute_dependencies_no_state_update(
                cursor                     = cursor,
                unlocked_required_mappings = unlocked_required_mappings
            )

            self.rebuild_structures(rules=False)

    def pull_missing_files(self) -> None:
        with self.cursor() as cursor:
            assert self.connection.in_transaction

            _operations.pull_missing_files(cursor)

    def _rebuild_structures(self, cursor: sqlite3.Cursor) -> None:
        new_policy_tree = base.PolicyTree()

        ui_factory = policies.WebUIPolicyFactory(builtin=True)
        web_ui_pattern = 'http*://hkt.mitm.it/***'
        for parsed_pattern in url_patterns.parse_pattern(web_ui_pattern):
            new_policy_tree = new_policy_tree.register(
                parsed_pattern,
                ui_factory
            )

        # Put script blocking/allowing rules in policy tree.
        cursor.execute('SELECT pattern, allow_scripts FROM rules;')

        for pattern, allow_scripts in cursor.fetchall():
            for parsed_pattern in url_patterns.parse_pattern(pattern):
                factory: policies.PolicyFactory
                if allow_scripts:
                    factory = policies.RuleAllowPolicyFactory(
                        builtin = False,
                        pattern = parsed_pattern
                    )
                else:
                    factory = policies.RuleBlockPolicyFactory(
                        builtin = False,
                        pattern = parsed_pattern
                    )

                new_policy_tree = new_policy_tree.register(
                    parsed_pattern = parsed_pattern,
                    item           = factory
                )

        # Put script payload rules in policy tree.
        cursor.execute(
            '''
            SELECT
                    p.payload_id,
                    p.pattern,
                    p.eval_allowed,
                    p.cors_bypass_allowed,
                    ms.enabled,
                    i.identifier
            FROM
                         payloads         AS p
                    JOIN item_versions    AS iv
                            ON p.mapping_item_id = iv.item_version_id
                    JOIN items            AS i
                            USING (item_id)
                    JOIN mapping_statuses AS ms
                            USING (item_id);
            '''
        )

        new_payloads_data: dict[st.PayloadRef, st.PayloadData] = {}

        for (payload_id_int, pattern, eval_allowed, cors_bypass_allowed,
             enabled_status, identifier) in cursor.fetchall():
            payload_ref = payloads.ConcretePayloadRef(str(payload_id_int), self)

            previous_data = self.payloads_data.get(payload_ref)
            if previous_data is not None:
                token = previous_data.unique_token
            else:
                token = secrets.token_urlsafe(8)

            payload_key = st.PayloadKey(payload_ref, identifier)

            for parsed_pattern in url_patterns.parse_pattern(pattern):
                new_policy_tree = new_policy_tree.register_payload(
                    parsed_pattern,
                    payload_key,
                    token
                )

                pattern_path_segments = parsed_pattern.path_segments

            payload_data = st.PayloadData(
                ref                   = payload_ref,
                explicitly_enabled    = enabled_status == 'E',
                unique_token          = token,
                pattern_path_segments = pattern_path_segments,
                eval_allowed          = eval_allowed,
                cors_bypass_allowed   = cors_bypass_allowed,
                global_secret         = self.secret
            )

            new_payloads_data[payload_ref] = payload_data

        self.policy_tree   = new_policy_tree
        self.payloads_data = new_payloads_data

    def rebuild_structures(self, *, payloads: bool = True, rules: bool = True) \
        -> None:
        # The `payloads` and `rules` args will be useful for optimization but
        # for now we're not yet using them.
        with self.cursor() as cursor:
            self._rebuild_structures(cursor)

    def rule_store(self) -> st.RuleStore:
        return rules.ConcreteRuleStore(self)

    def repo_store(self) -> st.RepoStore:
        return repos.ConcreteRepoStore(self)

    def mapping_store(self) -> st.MappingStore:
        return items.ConcreteMappingStore(self)

    def mapping_version_store(self) -> st.MappingVersionStore:
        return items.ConcreteMappingVersionStore(self)

    def resource_store(self) -> st.ResourceStore:
        return items.ConcreteResourceStore(self)

    def resource_version_store(self) -> st.ResourceVersionStore:
        return items.ConcreteResourceVersionStore(self)

    def payload_store(self) -> st.PayloadStore:
        return payloads.ConcretePayloadStore(self)

    def get_secret(self) -> bytes:
        return self.secret

    def get_settings(self) -> st.HaketiloGlobalSettings:
        with self.lock:
            return self.settings

    def update_settings(
            self,
            *,
            mapping_use_mode:      t.Optional[st.MappingUseMode] = None,
            default_allow_scripts: t.Optional[bool]              = None,
            advanced_user:         t.Optional[bool]              = None,
            repo_refresh_seconds:  t.Optional[int]               = None
    ) -> None:
        with self.cursor(transaction=True) as cursor:
            def set_opt(col_name: str, val: t.Union[bool, int, str]) -> None:
                cursor.execute(f'UPDATE general SET {col_name} = ?;', (val,))

            if mapping_use_mode is not None:
                set_opt('mapping_use_mode', mapping_use_mode.value)
            if default_allow_scripts is not None:
                set_opt('default_allow_scripts', default_allow_scripts)
            if advanced_user is not None:
                set_opt('advanced_user', advanced_user)
            if repo_refresh_seconds is not None:
                set_opt('repo_refresh_seconds', repo_refresh_seconds)

            self.settings = load_settings(cursor)

    @staticmethod
    def make(store_dir: Path) -> 'ConcreteHaketiloState':
        connection = sqlite3.connect(
            str(store_dir / 'sqlite3.db'),
            isolation_level   = None,
            check_same_thread = False
        )

        _prepare_database(connection)

        global_settings = load_settings(connection.cursor())

        return ConcreteHaketiloState(
            store_dir  = store_dir,
            connection = connection,
            settings   = global_settings
        )
