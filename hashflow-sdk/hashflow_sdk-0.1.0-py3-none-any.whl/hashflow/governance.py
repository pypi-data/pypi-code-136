from eth_typing.evm import AnyAddress, HexAddress
from web3 import Web3

from hashflow.executor import Executor
from hashflow.functions import create_hashflow_contract
from hashflow.util import NativeTokenDetails, Options


class Governance(object):
    def __init__(
        self,
        executor: Executor,
        network_id: int,
    ):
        self.executor = executor

        # initialize contracts
        self.contract = create_hashflow_contract(
            executor.web3, "HashflowGovernance", network_id
        )

    def authorized_router(self, router: AnyAddress) -> bool:
        return self.executor.call(
            self.contract.functions.authorizedRouter(Web3.toChecksumAddress(router)),
        )

    def factory(self) -> HexAddress:
        return self.executor.call(
            self.contract.functions.factory(),
        )

    def get_native_token_details(self) -> NativeTokenDetails:
        return self.executor.call(
            self.contract.functions.getNativeTokenDetails(),
        )

    def percent_withdraw_limit(self) -> int:
        return self.executor.call(
            self.contract.functions.percentWithdrawLimit(),
        )

    def router(self) -> HexAddress:
        return self.executor.call(
            self.contract.functions.router(),
        )

    def update_factory(self, factory: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateFactory(
                Web3.toChecksumAddress(factory)
            ),
            options=options,
        )

    def update_percent_withdrawal_limit(
        self, percent_withdrawal_limit: int, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updatePercentWithdrawLimit(
                percent_withdrawal_limit
            ),
            options=options,
        )

    def update_router(self, router: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateRouter(Web3.toChecksumAddress(router)),
            options=options,
        )

    def update_router_auth_status(
        self, router: AnyAddress, authorization: bool, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateRouterAuthStatus(
                Web3.toChecksumAddress(router),
                authorization,
            ),
            options=options,
        )

    def update_withdraw_period(
        self, withdraw_period: int, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateWithdrawPeriod(withdraw_period),
            options=options,
        )

    def update_x_chain_ua(self, x_chain_ua: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateXChainUa(
                Web3.toChecksumAddress(x_chain_ua)
            ),
            options=options,
        )

    def withdraw_period(self) -> int:
        return self.executor.call(self.contract.functions.withdrawPeriod())

    def x_chain_ua(self) -> HexAddress:
        return self.executor.call(self.contract.functions.xChainUa())
