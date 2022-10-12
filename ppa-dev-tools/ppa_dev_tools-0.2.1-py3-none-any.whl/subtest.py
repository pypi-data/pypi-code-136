#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# Copyright (C) 2022 Authors
#
# Released under GNU GPLv2 or later, read the file 'LICENSE.GPLv2+' for
# more information.
#
# Authors:
#   Bryce Harrington <bryce@canonical.com>

"""An individual DEP8 test run"""

from functools import cached_property


class Subtest:
    """
    A triggered autopkgtest can invoke multiple DEP8 tests, such as running
    checks on dependencies, the software's testsuite, and integration tests.
    Each of these is considered a "Subtest"
    """
    VALUES = {
        'PASS': "🟩",
        'SKIP': "🟧",
        'FAIL': "🟥",
        'BAD': "⛔",
        'UNKNOWN': "⚪"
    }

    def __init__(self, line):
        """Initializes a new Subtext object.

        :param str line: The subtest result summary from a test log.
        """
        if not line:
            raise ValueError("undefined line.")

        self._line = line

    def __repr__(self) -> str:
        """Machine-parsable unique representation of object.

        :rtype: str
        :returns: Official string representation of the object.
        """
        return (f'{self.__class__.__name__}('
                f'line={self._line!r})')

    def __str__(self) -> str:
        """Human-readable summary of the object.

        :rtype: str
        :returns: Printable summary of the object.
        """
        return f"{self.desc:25} {self.status:6} {self.status_icon}"

    @cached_property
    def desc(self) -> str:
        """The descriptive text for the given subtest.

        :rtype: str
        :returns: Descriptive text.
        """
        return next(iter(self._line.split()), '')

    @cached_property
    def status(self) -> str:
        """The success or failure of the given subtest.

        :rtype: str
        :returns: Status term in capitalized letters (PASS, FAIL, etc.)
        """
        for k in Subtest.VALUES:
            if f" {k}" in self._line:
                return k
        return 'UNKNOWN'

    @cached_property
    def status_icon(self) -> str:
        """Unicode symbol corresponding to subtest's status.

        :rtype: str
        :returns: Single unicode character matching the status.
        """
        return Subtest.VALUES[self.status]


if __name__ == "__main__":
    print("### Subtest class smoke test ###")
    print()

    print("Valid cases")
    print("-----------")
    print(Subtest('subtest-a   UNKNOWN'))
    print(Subtest('subtest-b   PASS'))
    print(Subtest('subtest-c   FAIL'))
    print(Subtest('subtest-d   FAIL non-zero exit status 123'))
    print(Subtest('subtest-e   SKIP'))
    print(Subtest('subtest-f   BAD'))
    print(Subtest('librust-clang-sys-dev:clang_10_0 FAIL non-zero exit status 101'))
    print()

    print("Invalid cases")
    print("-------------")
    print(Subtest('invalid subtest: invalid'))
    print(Subtest('bAd subtest: bAd'))
