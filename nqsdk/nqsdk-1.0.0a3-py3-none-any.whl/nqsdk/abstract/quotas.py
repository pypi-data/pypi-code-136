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
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:  # pragma: no cover
    from nqsdk.enums import QuotaIdentityType, QuotaType


class Quota(ABC):
    @classmethod
    @abstractmethod
    def quota_type(cls) -> QuotaType:
        pass


class ProviderQuota(Quota, ABC):
    @classmethod
    def quota_type(cls) -> QuotaType:
        return QuotaType.PROVIDER

    @classmethod
    @abstractmethod
    def identity_type(cls) -> QuotaIdentityType:
        pass


class ProviderStaticQuota(ProviderQuota, ABC):
    @property
    @abstractmethod
    def limit(self) -> int:
        """How many requests are allowed per time frame."""

    @property
    @abstractmethod
    def frame(self) -> int:
        """Time frame in seconds."""


class ProviderDynamicQuota(ProviderQuota, ABC):
    @property
    @abstractmethod
    def delay(self) -> Optional[int]:
        """How many seconds we need to wait before the next request."""

    @property
    @abstractmethod
    def until(self) -> Optional[datetime]:
        """Date & time in the future when we're allowed send the next request."""
