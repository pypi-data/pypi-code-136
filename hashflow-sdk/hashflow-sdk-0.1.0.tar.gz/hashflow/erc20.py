import os
import json

from eth_typing.evm import AnyAddress
from web3 import Web3

from hashflow.constants import MAX_SOLIDITY_UINT
from hashflow.executor import Executor
from hashflow.functions import create_contract
from hashflow.util import Options


class Token(object):
    def __init__(self, executor: Executor, address: AnyAddress):
        self.executor = executor
        self.contract = create_contract(
            executor.web3, "IERC20", Web3.toChecksumAddress(address)
        )

    def approve(
        self,
        spender: AnyAddress,
        amount: int = MAX_SOLIDITY_UINT,
        options: Options = {},
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.approve(
                Web3.toChecksumAddress(spender),
                amount,
            ),
            options=options,
        )

    def allowance(self, owner: AnyAddress, spender: AnyAddress) -> int:
        return self.executor.call(
            self.contract.functions.allowance(
                Web3.toChecksumAddress(owner),
                Web3.toChecksumAddress(spender),
            )
        )

    def balance_of(self, address: AnyAddress) -> int:
        return self.executor.call(
            self.contract.functions.balanceOf(
                Web3.toChecksumAddress(address),
            )
        )

    def decimals(self) -> int:
        return self.executor.call(self.contract.functions.decimals())

    def name(self) -> str:
        return self.executor.call(self.contract.functions.name())

    def symbol(self) -> str:
        return self.executor.call(self.contract.functions.symbol())

    def total_supply(self) -> int:
        return self.executor.call(self.contract.functions.totalSupply())


class ERC20(object):
    def __init__(self, executor: Executor, network_id: int):
        self.executor = executor
        this_folder = os.path.dirname(os.path.abspath(__file__))

        deployed_file_path = os.path.join(this_folder, "deployed.json")
        deployed_addresses = json.load(open(deployed_file_path, "r"))

        self.router_address = deployed_addresses["HashflowRouter"][str(network_id)][
            "address"
        ]

    def get_token(self, address: AnyAddress) -> Token:
        return Token(self.executor, address)

    # -----------------------------------------------------------
    # Transactions
    # -----------------------------------------------------------

    def set_maximum_hashflow_allowance(
        self, token: AnyAddress, options: Options = {}
    ) -> str:
        contract = Token(self.executor, token).contract
        return self.executor.send_transaction(
            method=contract.functions.approve(
                Web3.toChecksumAddress(self.router_address),
                MAX_SOLIDITY_UINT,
            ),
            options=options,
        )

    def unset_allowance(self, token: AnyAddress, options: Options = {}) -> str:
        contract = Token(self.executor, token).contract
        return self.executor.send_transaction(
            method=contract.functions.approve(
                Web3.toChecksumAddress(self.router_address), 0
            ),
            options=options,
        )

    def transfer(
        self,
        token: AnyAddress,
        receiver: AnyAddress,
        amount: int,
        options: Options = {},
    ) -> str:
        contract = Token(self.executor, token).contract
        return self.executor.send_transaction(
            method=contract.functions.transfer(
                Web3.toChecksumAddress(receiver),
                amount,
            ),
            options=options,
        )

    def transfer_from(
        self,
        token: AnyAddress,
        spender: AnyAddress,
        receiver: AnyAddress,
        amount: int,
        options: Options = {},
    ) -> str:
        contract = Token(self.executor, token).contract
        return self.executor.send_transaction(
            method=contract.functions.transferFrom(
                Web3.toChecksumAddress(spender),
                Web3.toChecksumAddress(receiver),
                amount,
            ),
            options=options,
        )
