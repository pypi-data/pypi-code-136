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

import pytest

from nqsdk.abstract.message import Message, SentMeta
from .impl import TestMessage, TestSentMeta


@pytest.fixture
def message() -> Message:
    return TestMessage()


@pytest.fixture
def sent_meta() -> SentMeta:
    return TestSentMeta()
