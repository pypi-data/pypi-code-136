from eth_typing.evm import AnyAddress, ChecksumAddress
from web3 import Web3

from hashflow.functions import (
    create_hashflow_contract,
)
from hashflow.executor import Executor
from hashflow.util import Options


class Tracker(object):
    def __init__(self, executor: Executor, network_id: int):
        self.executor = executor

        # initialize contracts
        self.contract = create_hashflow_contract(
            executor.web3, "HashflowTracker", network_id
        )

    def get_governance(self) -> ChecksumAddress:
        return self.executor.call(self.contract.functions.getGovernance())

    def get_pool_authorization(self, pool: AnyAddress) -> bool:
        return self.executor.call(
            self.contract.functions.getPoolAuthorization(Web3.toChecksumAddress(pool))
        )

    def register_pool(self, pool: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.registerPool(Web3.toChecksumAddress(pool)),
            options=options,
        )

    def update_governance(self, governance: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateGovernance(
                Web3.toChecksumAddress(governance)
            ),
            options=options,
        )

    def update_pool_authorization(
        self, pool: AnyAddress, status: bool, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updatePoolAuthorization(
                Web3.toChecksumAddress(pool), status
            ),
            options=options,
        )
