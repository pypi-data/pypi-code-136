# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy data and configuration (RuleRef and RuleStore subtypes).
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
This module provides an interface to interact with script allowing/blocking
rules configured inside Haketilo.
"""

import sqlite3
import typing as t
import dataclasses as dc

from ... import url_patterns
from .. import state as st
from . import base


def ensure_rule_not_deleted(cursor: sqlite3.Cursor, rule_id: str) -> None:
    cursor.execute('SELECT COUNT(*) from rules where rule_id = ?;', (rule_id,))

    (rule_present,), = cursor.fetchall()

    if not rule_present:
        raise st.MissingItemError()

def sanitize_rule_pattern(pattern: str) -> str:
    pattern = pattern.strip()

    try:
        assert pattern
        return url_patterns.normalize_pattern(pattern)
    except:
        raise st.RulePatternInvalid()


@dc.dataclass(frozen=True, unsafe_hash=True)
class ConcreteRuleRef(st.RuleRef):
    state: base.HaketiloStateWithFields = dc.field(hash=False, compare=False)

    def remove(self) -> None:
        with self.state.cursor(transaction=True) as cursor:
            ensure_rule_not_deleted(cursor, self.id)

            cursor.execute('DELETE FROM rules WHERE rule_id = ?;', self.id)

            self.state.rebuild_structures(payloads=False)

    def update(
            self,
            *,
            pattern: t.Optional[str]  = None,
            allow:   t.Optional[bool] = None
    ) -> None:
        if pattern is not None:
            pattern = sanitize_rule_pattern(pattern)

        if pattern is None and allow is None:
            return

        with self.state.cursor(transaction=True) as cursor:
            ensure_rule_not_deleted(cursor, self.id)

            if allow is not None:
                cursor.execute(
                    'UPDATE rules SET allow_scripts = ? WHERE rule_id = ?;',
                    (allow, self.id)
                )

            if pattern is not None:
                cursor.execute(
                    'DELETE FROM rules WHERE pattern = ? AND rule_id != ?;',
                    (pattern, self.id)
                )

                cursor.execute(
                    'UPDATE rules SET pattern = ? WHERE rule_id = ?;',
                    (pattern, self.id)
                )

            self.state.rebuild_structures(payloads=False)

    def get_display_info(self) -> st.RuleDisplayInfo:
        with self.state.cursor() as cursor:
            cursor.execute(
                'SELECT pattern, allow_scripts FROM rules WHERE rule_id = ?;',
                (self.id,)
            )

            rows = cursor.fetchall()

        if rows == []:
            raise st.MissingItemError()

        (pattern, allow), = rows

        return st.RuleDisplayInfo(self, pattern, allow)


@dc.dataclass(frozen=True)
class ConcreteRuleStore(st.RuleStore):
    state: base.HaketiloStateWithFields

    def get(self, id: str) -> st.RuleRef:
        return ConcreteRuleRef(str(int(id)), self.state)

    def add(self, pattern: str, allow: bool) -> st.RuleRef:
        pattern = sanitize_rule_pattern(pattern)

        with self.state.cursor(transaction=True) as cursor:
            cursor.execute(
                '''
                INSERT INTO rules(pattern, allow_scripts)
                VALUES (?, ?)
                ON CONFLICT (pattern)
                DO UPDATE SET allow_scripts = excluded.allow_scripts;
                ''',
                (pattern, allow)
            )

            cursor.execute(
                'SELECT rule_id FROM rules WHERE pattern = ?;',
                (pattern,)
            )

            (rule_id,), = cursor.fetchall()

            return ConcreteRuleRef(str(rule_id), self.state)

    def get_display_infos(self, allow: t.Optional[bool] = None) \
        -> t.Sequence[st.RuleDisplayInfo]:
        with self.state.cursor() as cursor:
            cursor.execute(
                '''
                SELECT
                        rule_id, pattern, allow_scripts
                FROM
                        rules
                WHERE
                        COALESCE(allow_scripts = ?, TRUE)
                ORDER BY
                        pattern;
                ''',
                (allow,)
            )

            rows = cursor.fetchall()

        result = []
        for rule_id, pattern, allow_scripts in rows:
            ref = ConcreteRuleRef(str(rule_id), self.state)

            result.append(st.RuleDisplayInfo(ref, pattern, allow_scripts))

        return result
