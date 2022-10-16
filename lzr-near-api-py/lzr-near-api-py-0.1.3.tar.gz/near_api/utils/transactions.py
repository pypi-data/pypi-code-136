import time
import logging

from near_api import transactions
from near_api.providers import JsonProviderError


def tx_retry_with_cool_off(callback, receiver_id: str,
                           actions: list['transactions.Action'],
                           delay: int = 0.5, nonce_max_retry: int = 8,
                           cool_of_factor=1.5):
    delay_time = delay
    for i in range(nonce_max_retry):
        try:
            result = callback(receiver_id, actions)
            return result
        except JsonProviderError as err:
            time.sleep(delay_time)
            delay_time *= cool_of_factor
    return None
