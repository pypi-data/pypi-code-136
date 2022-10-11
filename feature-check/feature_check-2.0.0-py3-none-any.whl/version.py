# Copyright (c) 2018, 2019, 2021  Peter Pentchev <roam@ringlet.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""Version string parsing for the feature-check Python library."""

from __future__ import annotations

from typing import Any, NamedTuple, Optional, TypeVar


class VersionComponent(NamedTuple):
    """Represent a single version component: a numerical part and a freeform string one."""

    num: Optional[int]
    rest: str

    def __str__(self) -> str:
        """Provide a string representation of the version component."""
        return (str(self.num) if self.num is not None else "") + self.rest

    def __cmp__(self, other: Any) -> int:
        """Compare two components, return None if they are equal."""
        # pylint: disable=too-many-return-statements,too-many-branches
        if not isinstance(other, VersionComponent):
            raise NotImplementedError("Only comparisons to VersionComponent supported")

        if self.num is not None:
            if other.num is not None:
                if self.num < other.num:
                    return -1
                if self.num > other.num:
                    return 1

                if self.rest is not None:
                    if other.rest is not None:
                        if self.rest < other.rest:
                            return -1
                        if self.rest > other.rest:
                            return 1
                        return 0

                    return 1

                if other.rest is not None:
                    return -1

                return 0

            return 1

        if other.num is not None:
            return -1

        if self.rest is not None:
            if other.rest is not None:
                if self.rest < other.rest:
                    return -1
                if self.rest > other.rest:
                    return 1
                return 0

            return -1

        return 0

    def __lt__(self, other: Any) -> bool:
        """Check whether this version component is less than the other one."""
        return self.__cmp__(other) < 0

    def __le__(self, other: Any) -> bool:
        """Check whether this version component is less than or equal to the other one."""
        return self.__cmp__(other) <= 0

    def __eq__(self, other: Any) -> bool:
        """Check whether this version component is equal to the other one."""
        return self.__cmp__(other) == 0

    def __ne__(self, other: Any) -> bool:
        """Check whether this version component is not equal to the other one."""
        return self.__cmp__(other) != 0

    def __ge__(self, other: Any) -> bool:
        """Check whether this version component is greater than or equal to the other one."""
        return self.__cmp__(other) >= 0

    def __gt__(self, other: Any) -> bool:
        """Check whether this version component is greater than the other one."""
        return self.__cmp__(other) > 0


class Version(NamedTuple):
    """A version string: many components, possibly other attributes."""

    value: str
    components: list[VersionComponent]


T = TypeVar("T")


def _version_compare_split_empty(
    spl_a: list[VersionComponent], spl_b: list[VersionComponent]
) -> int | None:
    """Check if any of the split version numbers is empty."""
    if not spl_a:
        if not spl_b:
            return 0
        if spl_b[0].num is None:
            return 1
        return -1
    if not spl_b:
        if spl_a[0].num is None:
            return -1
        return 1

    return None


def _version_compare_split(
    spl_a: list[VersionComponent], spl_b: list[VersionComponent]
) -> int:
    """Compare two version numbers already split into component lists.

    Returns -1, 0, or 1 for the first version being less than, equal to,
    or greater than the second one.
    """
    res = _version_compare_split_empty(spl_a, spl_b)
    if res is not None:
        return res

    (comp_a, comp_b) = (spl_a.pop(0), spl_b.pop(0))
    res = comp_a.__cmp__(comp_b)
    if res != 0:
        return res

    return _version_compare_split(spl_a, spl_b)


def version_compare(ver_a: Version, ver_b: Version) -> int:
    """Compare two version strings.

    Returns -1, 0, or 1 for the first version being less than, equal to,
    or greater than the second one.
    """
    return _version_compare_split(ver_a.components, ver_b.components)
