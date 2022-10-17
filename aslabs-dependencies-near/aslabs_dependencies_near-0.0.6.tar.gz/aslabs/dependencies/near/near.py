from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
from aslabs.near.config import NearRpcConfig, NearConfig
from aslabs.near.account import get_near_account, get_resilient_near_account, Account
from aslabs.near.signature_verifier import SignatureVerifier


T = TypeVar("T")


class SignatureVerifierResolver(ResolverABC):
    def __call__(self, deps: DependenciesABC) -> T:
        config = deps.get(NearRpcConfig)
        return SignatureVerifier(config.provider_url)

    @property
    def resolved_type(self) -> Type[T]:
        return SignatureVerifier


class NearAccountResolver(ResolverABC):
    def __init__(self):
        self._account = None

    def __call__(self, deps: DependenciesABC) -> T:
        if self._account is None:
            self._account = get_near_account(deps.get(NearConfig))
        return self._account

    @property
    def resolved_type(self) -> Type[T]:
        return Account


class ResilientNearAccountResolver(ResolverABC):
    def __init__(self):
        self._account = None

    def __call__(self, deps: DependenciesABC) -> T:
        if self._account is None:
            self._account = get_resilient_near_account(deps.get(NearConfig))
        return self._account

    @property
    def resolved_type(self) -> Type[T]:
        return Account
