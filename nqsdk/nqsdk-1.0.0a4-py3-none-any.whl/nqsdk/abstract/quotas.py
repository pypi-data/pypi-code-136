"""
Copyright (c) 2022 Inqana Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict

from nqsdk.mixins import SerializableMixin

if TYPE_CHECKING:  # pragma: no cover
    from nqsdk.enums import QuotaIdentityType, QuotaType


class Quota(SerializableMixin, ABC):
    def as_dict(self) -> Dict[str, Any]:
        return {
            "quota_type": self.quota_type().value,
        }

    @classmethod
    @abstractmethod
    def quota_type(cls) -> QuotaType:
        pass


class ProviderQuota(Quota, ABC):
    def as_dict(self) -> Dict[str, Any]:
        dump = super().as_dict()
        dump.update(
            {
                "identity_type": self.identity_type().value,
            }
        )

        return dump

    @classmethod
    def quota_type(cls) -> QuotaType:
        return QuotaType.PROVIDER

    @classmethod
    @abstractmethod
    def identity_type(cls) -> QuotaIdentityType:
        pass


class ProviderStaticQuota(ProviderQuota, ABC):
    def as_dict(self) -> Dict[str, Any]:
        dump = super().as_dict()
        dump.update(
            {
                "limit": self.limit,
                "frame": self.frame,
            }
        )

        return dump

    @property
    @abstractmethod
    def limit(self) -> int:
        """How many requests are allowed per time frame."""

    @property
    @abstractmethod
    def frame(self) -> int:
        """Time frame in seconds."""


class ProviderDynamicDelayQuota(ProviderQuota, ABC):
    def as_dict(self) -> Dict[str, Any]:
        dump = super().as_dict()
        dump.update(
            {
                "delay": self.delay,
            }
        )

        return dump

    @property
    @abstractmethod
    def delay(self) -> int:
        """How many seconds we need to wait before the next request."""


class ProviderDynamicUntilQuota(ProviderQuota, ABC):
    def as_dict(self) -> Dict[str, Any]:
        dump = super().as_dict()
        dump.update(
            {
                "until": self.until.strftime("%Y-%m-%dT%H-%M-%s"),
            }
        )

        return dump

    @property
    @abstractmethod
    def until(self) -> datetime:
        """Date & time in the future when we're allowed send the next request."""
