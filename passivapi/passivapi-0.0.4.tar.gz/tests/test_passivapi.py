import pytest
import requests_mock

from passivapi.passivapi import PassivApi


def test_login():
    with requests_mock.Mocker() as m:
        mock_token = {
            "token_type": "Bearer",
            "access_token": "9f44b3cd-c8a8-4e8b-af7b-01234567890a",
            "expires_in": 26002376,
        }
        m.post("https://www.passivliving.com/oauth/token", json=mock_token)
        PassivApi("some_user", "some_password")


def test_get_heating():
    with requests_mock.Mocker() as m:
        mock_token = {
            "token_type": "Bearer",
            "access_token": "9f44b3cd-c8a8-4e8b-af7b-01234567890a",
            "expires_in": 26002376,
        }
        m.post("https://www.passivliving.com/oauth/token", json=mock_token)

        mock_heating = {"foo": "bar"}
        m.get(
            "https://www.passivliving.com/api/consumer/v/1/users/some_user/home/capabilities/heating",
            json=mock_heating,
        )

        p = PassivApi("some_user", "some_password")

        h = p.get_heating()

        assert h == mock_heating
