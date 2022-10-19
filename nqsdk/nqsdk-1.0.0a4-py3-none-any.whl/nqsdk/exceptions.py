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

from typing import TYPE_CHECKING, Any, Dict, Optional

from nqsdk.mixins import SerializableMixin

if TYPE_CHECKING:  # pragma: no cover
    from .abstract.quotas import Quota
    from .callback import CallbackResponse


class BaseSentException(Exception, SerializableMixin):
    def as_dict(self) -> Dict[str, Any]:
        return {"exc": self.__class__.__name__, "message": str(self)}


class SentException(BaseSentException):
    pass


class DeliveryException(BaseSentException):
    pass


class AckException(BaseSentException):
    pass


class CallbackHandlingException(Exception, SerializableMixin):
    def __init__(self, *args, response: CallbackResponse):
        super().__init__(*args)
        self._response = response

    @property
    def response(self) -> CallbackResponse:
        return self._response

    def as_dict(self) -> Dict[str, Any]:
        return {"exc": self.__class__.__name__, "message": str(self)}


class ImproperlyConfigured(Exception):
    pass


class QuotaExceededException(Exception, SerializableMixin):
    def __init__(self, *args, quota: Quota = None):
        super().__init__(*args)
        self._quota = quota

    @property
    def quota(self) -> Optional[Quota]:
        return self._quota

    def as_dict(self) -> Dict[str, Any]:
        return {
            "exc": self.__class__.__name__,
            "message": str(self),
            "quota": self.quota.as_dict() if self.quota else None,
        }
