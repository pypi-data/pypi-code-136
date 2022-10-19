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
from decimal import Decimal
from typing import Dict, Union
from unittest import mock

import pytest
from requests import Response

from nqsdk.abstract.message import Message, SentMeta
from nqsdk.dummy.provider import DummyProvider
from nqsdk.enums import CallbackUrl
from nqsdk.exceptions import SentException


class TestDummyRequests:
    @staticmethod
    def get_response(code: int = 200) -> Response:
        resp = Response()
        resp.status_code = code

        return resp

    @pytest.mark.parametrize(
        "callback_urls", [{}, {CallbackUrl.ACK: "https://example.com/callback/{attempt_uid}"}]
    )
    @pytest.mark.parametrize("auth_token", [None, uuid.uuid4().hex])
    @pytest.mark.parametrize(
        "config",
        [
            {
                "send_url": "https://example.com/send",
            },
        ],
    )
    def test_send(
        self,
        config: Dict,
        message: Message,
        auth_token: str,
        callback_urls: Dict[Union[CallbackUrl, str], str],
    ):
        if auth_token:
            config["auth_token"] = auth_token

        kwargs = {
            "method": "post",
            "url": config["send_url"],
            "json": {
                "recipient_id": message.get_recipient_id(),
                "signature": message.get_signature(),
                "content": message.get_content(),
            },
        }
        if "auth_token" in config:
            kwargs["headers"] = {"Authorization": config["auth_token"]}
        if CallbackUrl.ACK in callback_urls:
            kwargs["json"]["callback_url"] = callback_urls[CallbackUrl.ACK].format(
                attempt_uid=message.attempt_uid
            )

        with mock.patch("requests.request", return_value=self.get_response()) as mocked:
            provider = DummyProvider(config=config, callback_urls=callback_urls)
            provider.send(message=message)

            mocked.assert_called_once_with(**kwargs)

    def test_send_exception(self, message: Message):
        with mock.patch(
            "nqsdk.dummy.provider.DummyProvider.send", side_effect=SentException("Sending error.")
        ) as mocked:
            provider = DummyProvider(config={}, callback_urls={})

            with pytest.raises(SentException) as exc_info:
                provider.send(message=message)

            exc = exc_info.value

            assert exc.as_dict()["exc"] == "SentException"
            assert exc.as_dict()["message"] == "Sending error."

        mocked.assert_called_once()

    @pytest.mark.parametrize("method", ["get", "post"])
    @pytest.mark.parametrize("auth_token", [None, uuid.uuid4().hex])
    @pytest.mark.parametrize(
        "key,config",
        [
            [
                "delivery",
                {
                    "delivery_check_url": "https://example.com/delivery",
                },
            ],
            [
                "ack",
                {
                    "ack_check_url": "https://example.org/ack",
                },
            ],
        ],
    )
    def test_check(self, method: str, key: str, config: Dict, sent_meta: SentMeta, auth_token: str):
        config[f"{key}_check_method"] = method
        if auth_token:
            config["auth_token"] = auth_token

        kwargs = {
            "method": method,
            "url": config[f"{key}_check_url"],
        }
        if "auth_token" in config:
            kwargs["headers"] = {"Authorization": config["auth_token"]}

        params_key = "params" if method == "get" else "json"
        kwargs[params_key] = {"message_id": sent_meta.ext_id}

        with mock.patch("requests.request", return_value=self.get_response()) as mocked:
            provider = DummyProvider(config=config, callback_urls={})
            func = getattr(provider, f"check_{key}")
            result = func(meta=sent_meta)

            mocked.assert_called_once_with(**kwargs)
            assert result.ext_id
            assert result.attempt_uid

            if key == "ack":
                assert result.dt_ack
                dt = result.dt_ack
            else:
                assert result.dt_delivered
                dt = result.dt_delivered

            assert dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None

    @pytest.mark.parametrize("method", ["get", "post"])
    @pytest.mark.parametrize("auth_token", [None, uuid.uuid4().hex])
    @pytest.mark.parametrize(
        "config",
        [
            {
                "health_check_url": "https://example.com/health",
            },
        ],
    )
    def test_check_health(self, method: str, config: Dict, auth_token):
        config["health_check_method"] = method
        if auth_token:
            config["auth_token"] = auth_token

        kwargs = {
            "method": method,
            "url": config["health_check_url"],
        }
        if "auth_token" in config:
            kwargs["headers"] = {"Authorization": config["auth_token"]}

        with mock.patch("requests.request", return_value=self.get_response()) as mocked:
            provider = DummyProvider(config=config, callback_urls={})
            result = provider.check_health()

            mocked.assert_called_once_with(**kwargs)
            assert result is True

    @pytest.mark.parametrize("method", ["get", "post"])
    @pytest.mark.parametrize("auth_token", [None, uuid.uuid4().hex])
    @pytest.mark.parametrize(
        "config",
        [
            {
                "balance_get_url": "https://example.com/balance",
            },
        ],
    )
    def test_get_balance(self, method: str, config: Dict, auth_token):
        config["balance_get_method"] = method
        if auth_token:
            config["auth_token"] = auth_token

        kwargs = {
            "method": method,
            "url": config["balance_get_url"],
        }
        if "auth_token" in config:
            kwargs["headers"] = {"Authorization": config["auth_token"]}

        with mock.patch("requests.request", return_value=self.get_response()) as mocked:
            provider = DummyProvider(config=config, callback_urls={})
            result = provider.get_balance()

            mocked.assert_called_once_with(**kwargs)
            assert isinstance(result, Decimal)
            assert result >= Decimal("1.0")
