# std
from __future__ import annotations
import re
from typing import Optional as Opt

# internal
from tier.internal.errors import expect, TierVersionError
from tier.internal.versioning.bump_type import BumpType


class Version:
    PATTERN_MAJOR_MINOR_PATCH = r'(?P<major>\d+)\.(?P<minor>\d+).(?P<patch>\d+)'
    PATTERN_OTHERS = r'(\.dev(?P<dev>\d+))|(a(?P<a>\d+))|(b(?P<b>\d+))|(rc(?P<rc>\d+))|(\.post(?P<post>\d+))'
    PATTERN = re.compile(f'^{PATTERN_MAJOR_MINOR_PATCH}({PATTERN_OTHERS})?$')

    def __init__(
            self,
            major: int = 0,
            minor: int = 0,
            patch: int = 0,
            post: Opt[int] = None,
            rc: Opt[int] = None,
            b: Opt[int] = None,
            a: Opt[int] = None,
            dev: Opt[int] = None,
    ):
        self.expect(
            sum(map(lambda x: x is not None, (post, rc, b, a, dev))) <= 1,
            'Only one dev-, pre-, or post-release number can be provided.',
            )
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if patch is not None:
            self.patch = patch
        self.post = post
        self.rc = rc
        self.b = b
        self.a = a
        self.dev = dev
        self.expect(self.major is not None, 'major number is required')
        self.expect(self.minor is not None, 'minor number is required')
        self.expect(self.patch is not None, 'patch number is required')

    def __repr__(self) -> str:
        return self.str()

    def __str__(self) -> str:
        return self.str()

    def __eq__(self, other: Version) -> bool:
        return str(self) == str(other)

    def __lt__(self, other: Version):
        return self.sorting_tuple() < other.sorting_tuple()

    @property
    def is_post_release(self) -> bool:
        return self.post is not None

    @property
    def is_pre_release(self) -> bool:
        return (
                self.rc is not None
                or self.b is not None
                or self.a is not None
                or self.dev is not None
        )

    @property
    def is_release(self) -> bool:
        return not (self.is_pre_release or self.is_post_release)

    def repr(self) -> str:
        return self.str()

    def str(self) -> str:
        s = f'{self.major}.{self.minor}.{self.patch}'
        if self.dev is not None:
            return f'{s}.dev{self.dev}'
        if self.a is not None:
            return f'{s}.a{self.a}'
        if self.b is not None:
            return f'{s}.b{self.b}'
        if self.rc is not None:
            return f'{s}.rc{self.rc}'
        if self.post is not None:
            return f'{s}.post{self.post}'
        return s

    def sorting_tuple(self):
        return (
            self.major,
            self.minor,
            self.patch,
            self.post or -1,
            0 if self.is_pre_release else 1,
            self.rc or -1,
            self.b or -1,
            self.a or -1,
            self.dev or -1,
        )

    def bump(self, bump_type: BumpType) -> Version:
        if bump_type == BumpType.MAJOR:
            return self.bump_major()
        elif bump_type == BumpType.MINOR:
            return self.bump_minor()
        elif bump_type == BumpType.PATCH:
            return self.bump_patch()
        elif bump_type == BumpType.POST:
            return self.bump_post()
        elif bump_type == BumpType.RC:
            return self.bump_rc()
        elif bump_type == BumpType.MAJOR_RC:
            return self.bump_major().bump_rc()
        elif bump_type == BumpType.MINOR_RC:
            return self.bump_minor().bump_rc()
        elif bump_type == BumpType.PATCH_RC:
            return self.bump_patch().bump_rc()
        elif bump_type == BumpType.B:
            return self.bump_b()
        elif bump_type == BumpType.MAJOR_B:
            return self.bump_major().bump_b()
        elif bump_type == BumpType.MINOR_B:
            return self.bump_minor().bump_b()
        elif bump_type == BumpType.PATCH_B:
            return self.bump_patch().bump_b()
        elif bump_type == BumpType.A:
            return self.bump_a()
        elif bump_type == BumpType.MAJOR_A:
            return self.bump_major().bump_a()
        elif bump_type == BumpType.MINOR_A:
            return self.bump_minor().bump_a()
        elif bump_type == BumpType.PATCH_A:
            return self.bump_patch().bump_a()
        elif bump_type == BumpType.DEV:
            return self.bump_dev()
        elif bump_type == BumpType.MAJOR_DEV:
            return self.bump_major().bump_dev()
        elif bump_type == BumpType.MINOR_DEV:
            return self.bump_minor().bump_dev()
        elif bump_type == BumpType.PATCH_DEV:
            return self.bump_patch().bump_dev()
        else:
            return self

    def bump_major(self) -> Version:
        return Version(self.major + 1, 0, 0)

    def bump_minor(self) -> Version:
        return Version(self.major, self.minor + 1, 0)

    def bump_patch(self) -> Version:
        return Version(self.major, self.minor, self.patch + 1)

    def bump_post(self) -> Version:
        return Version(self.major, self.minor, self.patch, (-1 if self.post is None else self.post) + 1)

    def bump_rc(self) -> Version:
        return Version(self.major, self.minor, self.patch, rc=(-1 if self.rc is None else self.rc) + 1)

    def bump_b(self) -> Version:
        return Version(self.major, self.minor, self.patch, b=(-1 if self.b is None else self.b) + 1)

    def bump_a(self) -> Version:
        return Version(self.major, self.minor, self.patch, a=(-1 if self.a is None else self.a) + 1)

    def bump_dev(self) -> Version:
        return Version(self.major, self.minor, self.patch, dev=(-1 if self.dev is None else self.dev) + 1)

    @classmethod
    def from_str(cls, s: str) -> Version:
        cls.expect(cls.validate(s), f'Invalid version string {s}')
        m = cls.PATTERN.match(s)
        d = {k: int(v) for k, v in m.groupdict().items() if v is not None}
        return Version(**d)

    @classmethod
    def expect(cls, condition: bool, msg: str):
        expect(condition, msg, TierVersionError)

    @classmethod
    def validate(cls, s: str) -> bool:
        m = cls.PATTERN.match(s)
        return bool(m)
