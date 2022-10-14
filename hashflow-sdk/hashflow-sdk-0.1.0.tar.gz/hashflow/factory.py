import os
import json

from eth_typing.evm import AnyAddress
from web3 import Web3

from hashflow.util import Options
from hashflow.executor import Executor
from hashflow.functions import create_hashflow_contract


class Factory(object):
    def __init__(self, executor: Executor, network_id: int):
        self.executor = executor

        # initialize contracts
        self.contract = create_hashflow_contract(
            executor.web3, "HashflowFactory", network_id
        )
        this_folder = os.path.dirname(os.path.abspath(__file__))

        deployed_file_path = os.path.join(this_folder, "deployed.json")
        deployed_addresses = json.load(open(deployed_file_path, "r"))
        self.router_address = deployed_addresses["HashflowRouter"][str(network_id)][
            "address"
        ]
        self.governance_address = deployed_addresses["HashflowGovernance"][
            str(network_id)
        ]["address"]

    def all_pools_length(self) -> int:
        """
        Get number of pools
        """
        return self.executor.call(method=self.contract.functions.allPoolsLength())

    def create_pool(
        self,
        name: str,
        signer: AnyAddress,
        symbol: str = "",
        isPrivate: bool = True,
        options: Options = {},
    ) -> str:
        """
        Allows market makers to create a pool.
        """
        return self.executor.send_transaction(
            method=self.contract.functions.createPool(
                name,
                symbol,
                Web3.toChecksumAddress(signer),
                isPrivate,
            ),
            options=options,
        )

    def update_governance(self, governance: AnyAddress, options: Options = {}) -> str:
        """
        Updates governance contract
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updateGovernance(
                Web3.toChecksumAddress(governance)
            ),
            options=options,
        )

    def update_h_token_impl(
        self, h_token_impl: AnyAddress, options: Options = {}
    ) -> str:
        """
        Updates hToken contract
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updateHTokenImpl(
                Web3.toChecksumAddress(h_token_impl)
            ),
            options=options,
        )

    def update_private_pool_impl(
        self, private_pool_impl: AnyAddress, options: Options = {}
    ) -> str:
        """
        Updates hToken contract
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updatePrivatePoolImpl(
                Web3.toChecksumAddress(private_pool_impl)
            ),
            options=options,
        )

    def update_public_pool_impl(
        self, public_pool_impl: AnyAddress, options: Options = {}
    ) -> str:
        """
        Updates hToken contract
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updatePublicPoolImpl(
                Web3.toChecksumAddress(public_pool_impl)
            ),
            options=options,
        )
