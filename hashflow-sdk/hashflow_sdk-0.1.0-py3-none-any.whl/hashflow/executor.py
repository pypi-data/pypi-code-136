from typing import Any
from web3 import Web3
from web3.contract import ContractFunction
from web3.types import TxParams, Nonce, Wei
from eth_account.messages import SignableMessage

from hexbytes import HexBytes

import hashflow.constants as consts
import hashflow.util as utils
from hashflow.util import Options


class Executor(object):
    def __init__(self, jsonRpcUrl: str | None, private_key: str | bytearray):
        self.web3: Web3 = Web3(
            None if jsonRpcUrl is None else Web3.HTTPProvider(jsonRpcUrl)
        )
        self.private_key = utils.normalize_to_bytearray(private_key)
        self.public_address = utils.private_key_to_address(self.private_key)

    def get_nonce(self) -> Nonce:
        return self.web3.eth.get_transaction_count(self.public_address)

    def sign_message(self, message: SignableMessage) -> HexBytes:
        return self.web3.eth.account.sign_message(message, self.private_key).signature

    def send_transaction(self, method: ContractFunction, options: Options = {}) -> str:
        options_mod = options.copy()
        if "from" not in options_mod:
            options_mod["from"] = self.public_address
        if "value" not in options_mod:
            options_mod["value"] = Wei(0)
        if "gas" not in options_mod:
            try:
                options_mod["gas"] = Wei(
                    int(method.estimate_gas(options_mod) * consts.DEFAULT_GAS_MULTIPLIER)
                )
            except Exception:
                options_mod["gas"] = consts.DEFAULT_GAS_AMOUNT
        if "nonce" not in options_mod:
            options_mod["nonce"] = self.get_nonce()
        else:
            print('Setting nonce', options_mod["nonce"])

        if "maxFeePerGas" in options_mod or "maxPriorityFeePerGas" in options_mod:
            options_mod["type"] = 2

        tx: TxParams = method.build_transaction(options_mod)
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        return self.web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()

    def call(self, method: ContractFunction, options: Options = {}) -> Any:
        options_mod = options.copy()
        if "from" not in options_mod:
            options_mod["from"] = self.public_address
        return method.call(options_mod)
