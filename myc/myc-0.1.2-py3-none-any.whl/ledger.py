import functools
import json
import os
from dataclasses import dataclass
from typing import Optional

import boto3

from myc.endpoint import Endpoint, PlatformKind

_LEDGER_CACHE = None


@dataclass
class LedgerPlatformsEntry:
    """
    An entry that describes the platform/runtime and logical entity an endpoint is deployed on.
    """
    endpoint_id: str
    platform_kind: PlatformKind
    logical_id: str

    def to_dict(self) -> dict:
        return {
            'endpoint_id': self.endpoint_id,
            'platform_kind': self.platform_kind.value,
            'logical_id': self.logical_id
        }

    @staticmethod
    def from_dict(obj: dict) -> 'LedgerPlatformsEntry':
        return LedgerPlatformsEntry(
            endpoint_id=obj['endpoint_id'],
            platform_kind=PlatformKind(obj['platform_kind']),
            logical_id=obj['logical_id'],
        )


@dataclass
class LedgerPostEntry:
    """
    An entry that describes the physical address of an endpoint and the protocol required
    to be able to talk to it, in addition to platform information.
    """
    platform_entry: LedgerPlatformsEntry
    protocol: str
    extra: Optional[dict]

    def to_dict(self) -> dict:
        return {
            'platform_entry': self.platform_entry.to_dict(),
            'protocol': self.protocol,
            'extra': self.extra,
        }

    @staticmethod
    def from_dict(obj: dict) -> 'LedgerPostEntry':
        return LedgerPostEntry(
            platform_entry=LedgerPlatformsEntry.from_dict(obj['platform_entry']),
            protocol=obj['protocol'],
            extra=obj['extra'],
        )


class LedgerObject:
    pass


class LedgerPost(LedgerObject):
    def __init__(self):
        self._entries = {}

    def add_entry(self, entry: LedgerPostEntry):
        self._entries[entry.platform_entry.endpoint_id] = entry

    def find_entry(self, endpoint_id: str) -> Optional[LedgerPostEntry]:
        return self._entries.get(endpoint_id)

    @staticmethod
    def from_dict(value: dict) -> 'LedgerPost':
        post = LedgerPost()
        for endpoint_id, value in value.items():
            post.add_entry(LedgerPostEntry.from_dict(value))

        return post


class LedgerPlatforms(LedgerObject):
    def __init__(self):
        self._entries = {}

    def get_platform(self, endpoint_id: str) -> Optional[PlatformKind]:
        return self._entries.get(endpoint_id)

    @staticmethod
    def from_dict(value: dict) -> 'LedgerPlatforms':
        platforms = LedgerPlatforms()

        for endpoint_id, value in value.items():
            platforms._entries[endpoint_id] = LedgerPlatformsEntry(
                endpoint_id=endpoint_id,
                platform_kind=PlatformKind(value['kind']),
                logical_id=value['logical_id'],
            )

        return platforms


class Ledger:
    def get_platforms(self) -> LedgerPlatforms:
        raise NotImplementedError

    def get_post(self) -> LedgerPost:
        raise NotImplementedError


class S3Ledger(Ledger):
    LEDGER_BUCKET_ENV_VAR = 'MYC_LEDGER_BUCKET__'
    LEDGER_POST_KEY = 'post.json'
    LEDGER_PLATFORMS_KEY = 'platforms.json'

    def __init__(self, bucket_name: str):
        self._bucket_name = bucket_name

    def _read_json_object(self, key: str) -> dict:
        s3 = boto3.resource('s3')
        obj = s3.Object(self._bucket_name, key)
        body = json.loads(obj.get()['Body'].read().decode('utf-8'))
        return body

    @functools.cache
    def get_platforms(self) -> LedgerPlatforms:
        platforms_body = self._read_json_object(S3Ledger.LEDGER_PLATFORMS_KEY)
        return LedgerPlatforms.from_dict(platforms_body)

    @functools.cache
    def get_post(self) -> LedgerPost:
        post_body = self._read_json_object(S3Ledger.LEDGER_POST_KEY)
        return LedgerPost.from_dict(post_body)


def read_ledger() -> Ledger:
    return read_ledger_from_s3()


def read_ledger_from_s3() -> S3Ledger:
    return S3Ledger(os.environ[S3Ledger.LEDGER_BUCKET_ENV_VAR])


def get_ledger() -> Ledger:
    """
    Memoized version of read_ledger().
    Use this function to utilize caching.
    """
    global _LEDGER_CACHE
    if _LEDGER_CACHE is None:
        _LEDGER_CACHE = read_ledger()

    return _LEDGER_CACHE
