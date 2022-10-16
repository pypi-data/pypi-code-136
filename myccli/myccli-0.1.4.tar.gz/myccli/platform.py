from dataclasses import dataclass
from typing import List, Optional

from myc.endpoint import Endpoint, PlatformKind, GeneralFunctionEndpoint, AWSLambdaFunctionEndpoint
from myc.ledger import LedgerPlatformsEntry


@dataclass
class Platform:
    logical_id: str

    @property
    def kind(self) -> PlatformKind:
        raise NotImplementedError

    def make_ledger_entry(self, endpoint_id: str) -> LedgerPlatformsEntry:
        return LedgerPlatformsEntry(
            endpoint_id=endpoint_id,
            platform_kind=self.kind,
            logical_id=self.logical_id,
        )


@dataclass
class AWSLambdaPlatform(Platform):
    @property
    def kind(self) -> PlatformKind:
        return PlatformKind.AWS_LAMBDA


@dataclass
class AWSECSPlatform(Platform):
    @property
    def kind(self) -> PlatformKind:
        return PlatformKind.AWS_ECS


class PlatformMapping:
    def __init__(self):
        self._endpoint_map = {}

    def set_endpoint_platform(self, endpoint: Endpoint, platform: Platform):
        self._endpoint_map[endpoint] = platform

    def get_endpoint_platform(self, endpoint: Endpoint) -> Optional[Platform]:
        return self._endpoint_map.get(endpoint)

    def count_unique(self, platform_cls: type):
        """
        Counts the number of platforms of a given type uniquely identifiable by their logical IDs.
        """
        assert issubclass(platform_cls, Platform)
        return len(set(p.logical_id for p in self._endpoint_map.values() if isinstance(p, platform_cls)))


class PlatformSelector:
    """
    Responsible for managing the process of assigning endpoints a platform to
    be deployed on.
    """
    def __init__(self, endpoints: List[Endpoint]):
        self._endpoints = endpoints

    def select(self) -> PlatformMapping:
        result = PlatformMapping()

        for endpoint in self._endpoints:
            logical_id = endpoint.service.name

            # if endpoint.platform_hint == PlatformKind.AWS_LAMBDA:
            platform = AWSLambdaPlatform(logical_id)
            # else:
            #     platform = AWSECSPlatform(logical_id)

            result.set_endpoint_platform(endpoint, platform)

        return result
