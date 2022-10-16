from .signature_verifier import SignatureVerifier
from .config import NearRpcConfig, NearConfig
from typing import Optional, Type, TypeVar
from aslabs.dependencies import ResolverABC, DependenciesABC
from .account import get_near_account, get_resilient_near_account
from near_api.account import Account

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