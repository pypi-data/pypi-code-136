# Copyright (c) Qotto, 2022

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional

__all__ = [
    'Namespace',
    'Matching',
    'Application',
    'Permission',
    'Organization',
    'Authorization',
    'Role',
    'User',
    'Member',
    'Account',
]


class Matching(Enum):
    ALL = 'ALL'
    EXACT = 'EXACT'
    ASCENDANT = 'ASCENDANT'
    DESCENDANT = 'DESCENDANT'
    SAME_BRANCH = 'SAME_BRANCH'

    def __str__(self) -> str:
        return self.name


class Namespace:
    _nodes: list[str]

    def __init__(
            self,
            nodes: Union[str, list[str]],
    ) -> None:
        """
        >>> Namespace('a:::b  :c:d')
        a:b:c:d
        >>> Namespace(['a', '  b  ', 'c', '', '', 'd'])
        a:b:c:d
        >>> Namespace(['a:', 'b', 'c', 'd'])
        Traceback (most recent call last):
            ...
        ValueError: A node cannot contain colons ":".
        >>> Namespace(['a', 1, 'c', 'd'])
        Traceback (most recent call last):
            ...
        TypeError: A node must be a str.
        >>> Namespace('')
        Traceback (most recent call last):
            ...
        ValueError: Namespace must have at least one node.
        """
        if isinstance(nodes, str):
            nodes = list(filter(len, (v.strip().lower() for v in nodes.split(':'))))
        elif isinstance(nodes, list):
            if any(filter(lambda x: not isinstance(x, str), nodes)):
                raise TypeError("A node must be a str.")
            if any(filter(lambda x: ':' in str(x), nodes)):
                raise ValueError("A node cannot contain colons \":\".")
            nodes = list(filter(len, (v.strip().lower() for v in nodes)))
        if not nodes:
            raise ValueError("Namespace must have at least one node.")
        for node in nodes:
            if not node:
                raise ValueError("Namespace node must not be empty.")
        self._nodes = nodes

    @property
    def path(self) -> str:
        return ':'.join(self._nodes)

    @property
    def nodes(self) -> list[str]:
        return self._nodes.copy()

    def matches(self, other: Namespace, matching: Matching = Matching.ALL) -> bool:
        """
        Test is self is <matching> of other.
        """
        if matching == Matching.ALL:
            return True
        if matching == Matching.EXACT:
            return self == other
        if matching == Matching.ASCENDANT:
            return self >= other
        if matching == Matching.DESCENDANT:
            return self <= other
        if matching == Matching.SAME_BRANCH:
            return self <= other or self >= other
        raise ValueError(f"Unknown matching type {matching}.")

    def __eq__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) == len(other)
                and self.path == other.path)

    def __le__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) >= len(other)
                and Namespace(self._nodes[:len(other)]) == other)

    def __ge__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) <= len(other)
                and Namespace(other._nodes[:len(self)]) == self)

    def __lt__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) > len(other)
                and Namespace(self._nodes[:len(other)]) == other)

    def __gt__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) < len(other)
                and Namespace(other._nodes[:len(self)]) == self)

    def __len__(self) -> int:
        return len(self._nodes)

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return self.path


@dataclass
class Application:
    application_id: str
    name: str
    description: str


@dataclass
class Permission:
    application: Application
    permission_id: str
    name: str
    description: str


@dataclass
class Organization:
    organization_id: str
    name: str
    namespace: Namespace


@dataclass
class Authorization:
    authorization_id: str
    name: str
    description: str
    organization: Organization
    inheritance: bool
    matching: Matching


@dataclass
class Role:
    role_id: str
    name: str
    description: str
    organization: Organization
    inheritance: bool


@dataclass
class Identity:
    identity_id: str
    name: str
    provider_id: str
    email: str
    user: Optional[User]
    blocked: bool


@dataclass
class User:
    user_id: str
    name: str
    is_superuser: bool


@dataclass
class Member:
    member_id: str
    user: User
    organization: Organization


@dataclass
class Account:
    account_id: str
    application: Application
    user: User
    enabled: bool
    data: dict


@dataclass
class Cookie:
    name: str
    value: str
    domain: str
    max_age: int
    secure: bool
    http_only: bool

    def __str__(self):
        return f'Cookie"{self.name}={self.value}"'
