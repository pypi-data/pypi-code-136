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

import random
import uuid
from dataclasses import dataclass, field
from datetime import datetime

import pytz
from faker import Faker

from nqsdk.abstract.message import Message, SentMeta
from nqsdk.dummy.provider import DummyProvider

fake = Faker()


@dataclass
class TestMessage(Message):
    _attempt_uid: str = field(default_factory=lambda: str(uuid.uuid4().hex))
    _recipient_id: str = field(default_factory=fake.email)
    _content: str = field(default_factory=fake.text)
    _channel: str = field(default_factory=lambda: random.choice(DummyProvider.get_channels()).label)

    @property
    def channel(self) -> str:
        return self._channel

    @property
    def attempt_uid(self) -> str:
        return self._attempt_uid

    def get_recipient_id(self) -> str:
        return self._recipient_id

    def get_content(self) -> str:
        return self._content


@dataclass
class TestSentMeta(SentMeta):
    _attempt_uid: str = field(default_factory=lambda: str(uuid.uuid4().hex))
    _ext_id: str = field(default_factory=lambda: str(uuid.uuid4().hex))
    _dt_sent: datetime = field(default_factory=lambda: datetime.now(tz=pytz.timezone("UTC")))

    @property
    def attempt_uid(self) -> str:
        return self._attempt_uid

    @property
    def ext_id(self) -> str:
        return self._ext_id

    @property
    def dt_sent(self) -> datetime:
        return self._dt_sent
