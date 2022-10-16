from near_api.signer import Signer, KeyPair
from near_api.account import Account
from near_api.providers import JsonProvider, JsonProviderError
from .config import NearConfig
from typing import TypeVar, Type
from requests import ReadTimeout

T = TypeVar("T")


class ResilientJsonProvider(JsonProvider):
    forced_timeout = 100
    max_retry_count = 5

    def send_tx_and_wait(self, signed_tx, timeout):
        retry_count = 0
        while True:
            try:
                return super().send_tx_and_wait(signed_tx, timeout)
            except JsonProviderError as e:
                result, *_ = e.args
                if result.get("name") == "HANDLER_ERROR" and result.get("cause", {}).get("name") == "TIMEOUT_ERROR":
                    retry_count += 1
                    if retry_count > 5:
                        raise
            except ReadTimeout:
                retry_count += 1
                if retry_count > self.max_retry_count:
                    raise


def get_near_account(config: NearConfig):
    return Account(
        JsonProvider(config.provider_url),
        Signer(config.account_id, KeyPair(config.private_key)),
        config.account_id
    )


def get_resilient_near_account(config: NearConfig):
    return Account(
        ResilientJsonProvider(config.provider_url),
        Signer(config.account_id, KeyPair(config.private_key)),
        config.account_id
    )
