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

import uuid
from typing import Dict

import pytest

from nqsdk.dummy.provider import DummyProvider
from nqsdk.exceptions import ImproperlyConfigured


class TestDummyConfig:
    @pytest.mark.parametrize(
        "config",
        [
            {
                "auth_token": uuid.uuid4().hex,
                "send_url": "https://example.com/send",
                "delivery_check_url": "https://example.com/delivery",
                "delivery_check_method": "post",
            },
            {
                "send_url": "https://example.com/send",
            },
        ],
    )
    def test_config_valid(self, config: Dict):
        provider = DummyProvider(
            config=config, callback_url="https://example.com/callback/{attempt_uid}"
        )

        assert provider.config == config

    @pytest.mark.parametrize(
        "config,key",
        [
            [
                {
                    "auth_token": 1,
                },
                "auth_token",
            ],
            [
                {
                    "send_url": "ftp://example.com/send",
                },
                "send_url",
            ],
        ],
    )
    def test_config_invalid(self, config: Dict, key: str):
        with pytest.raises(ImproperlyConfigured) as exc_info:
            DummyProvider(config=config)

        exc = exc_info.value

        assert key in str(exc)

    def test_config_empty(self):
        provider = DummyProvider(config={})

        assert provider.config == {}

    @pytest.mark.parametrize(
        "callback_url",
        [
            "https://example.com/callback",
            "https://example.com/callback/{uid}",
            "https://example.com/callback/attempt_uid",
        ],
    )
    def test_callback_url_invalid(self, callback_url: str):
        with pytest.raises(ImproperlyConfigured) as exc_info:
            DummyProvider(config={}, callback_url=callback_url)

        exc = exc_info.value

        assert "Invalid callback URL" in str(exc)
