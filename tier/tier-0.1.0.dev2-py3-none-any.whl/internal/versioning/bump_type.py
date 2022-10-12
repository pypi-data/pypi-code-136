# std
from __future__ import annotations
from enum import Enum
from typing import Tuple

# internal
from tier.internal.errors import expect, TierVersionError


class BumpType(Enum):
    MAJOR = (4, 0)
    MINOR = (3, 0)
    PATCH = (2, 0)
    POST = (1, 0)

    RC = (0, 4)
    MAJOR_RC = (4, 4)
    MINOR_RC = (3, 4)
    PATCH_RC = (2, 4)

    B = (0, 3)
    MAJOR_B = (4, 3)
    MINOR_B = (3, 3)
    PATCH_B = (2, 3)

    A = (0, 2)
    MAJOR_A = (4, 2)
    MINOR_A = (3, 2)
    PATCH_A = (2, 2)

    DEV = (0, 1)
    MAJOR_DEV = (4, 1)
    MINOR_DEV = (3, 1)
    PATCH_DEV = (2, 1)

    NULL = (0, 0)

    def __add__(self, other: BumpType) -> BumpType:
        left, right = sorted((self, other))
        l, r = left.value, right.value
        t = (max(l[0], r[0]), max(l[1], r[1]))
        try:
            return self.from_tuple(t)
        except TierVersionError:
            pass
        return right

    def __eq__(self, other: BumpType) -> bool:
        return self.value == other.value

    def __lt__(self, other: BumpType) -> bool:
        return self.value < other.value

    def __gt__(self, other: BumpType) -> bool:
        return self.value > other.value

    @classmethod
    def expect(cls, condition: bool, msg: str):
        expect(condition, msg, TierVersionError)

    @classmethod
    def from_tuple(cls, t: Tuple[int, int]) -> BumpType:
        if t == BumpType.MAJOR.value:
            return BumpType.MAJOR
        elif t == BumpType.MINOR.value:
            return BumpType.MINOR
        elif t == BumpType.PATCH.value:
            return BumpType.PATCH
        elif t == BumpType.POST.value:
            return BumpType.POST
        elif t == BumpType.RC.value:
            return BumpType.RC
        elif t == BumpType.MAJOR_RC.value:
            return BumpType.MAJOR_RC
        elif t == BumpType.MINOR_RC.value:
            return BumpType.MINOR_RC
        elif t == BumpType.PATCH_RC.value:
            return BumpType.PATCH_RC
        elif t == BumpType.B.value:
            return BumpType.B
        elif t == BumpType.MAJOR_B.value:
            return BumpType.MAJOR_B
        elif t == BumpType.MINOR_B.value:
            return BumpType.MINOR_B
        elif t == BumpType.PATCH_B.value:
            return BumpType.PATCH_B
        elif t == BumpType.A.value:
            return BumpType.A
        elif t == BumpType.MAJOR_A.value:
            return BumpType.MAJOR_A
        elif t == BumpType.MINOR_A.value:
            return BumpType.MINOR_A
        elif t == BumpType.PATCH_A.value:
            return BumpType.PATCH_A
        elif t == BumpType.DEV.value:
            return BumpType.DEV
        elif t == BumpType.MAJOR_DEV.value:
            return BumpType.MAJOR_DEV
        elif t == BumpType.MINOR_DEV.value:
            return BumpType.MINOR_DEV
        elif t == BumpType.PATCH_DEV.value:
            return BumpType.PATCH_DEV
        elif t == BumpType.NULL.value:
            return BumpType.NULL
        else:
            raise TierVersionError(f'tuple {t} does not correspond to bump type')

    @classmethod
    def from_options(
            cls,
            major: bool = False,
            minor: bool = False,
            patch: bool = False,
            post: bool = False,
            rc: bool = False,
            beta: bool = False,
            alpha: bool = False,
            dev: bool = False,
    ) -> BumpType:
        bump_type = BumpType.NULL
        if major:
            bump_type += BumpType.MAJOR
        if minor:
            bump_type += BumpType.MINOR
        if patch:
            bump_type += BumpType.PATCH
        if post:
            bump_type += BumpType.POST
        if rc:
            bump_type += BumpType.RC
        if beta:
            bump_type += BumpType.B
        if alpha:
            bump_type += BumpType.A
        if dev:
            bump_type += BumpType.DEV
        return bump_type
