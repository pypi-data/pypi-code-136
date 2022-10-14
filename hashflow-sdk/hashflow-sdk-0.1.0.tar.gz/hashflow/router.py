from typing import List
from eth_typing.evm import AnyAddress
from web3 import Web3
from web3.types import Wei

from hashflow.constants import ZERO_ADDRESS
from hashflow.functions import (
    create_hashflow_contract,
)
from hashflow.executor import Executor
from hashflow.util import (
    Deposit,
    Options,
    RFQMQuote,
    RFQTQuote,
    XChainMessageProtocol,
    XChainRFQMQuote,
    XChainRFQTQuote,
)


class Router(object):
    def __init__(self, executor: Executor, network_id: int):
        self.executor = executor

        # initialize contracts
        self.contract = create_hashflow_contract(
            executor.web3, "HashflowRouter", network_id
        )

    def add_liquidity_private_pool(
        self,
        pool: AnyAddress,
        token: AnyAddress,
        amount: Wei,
        options: Options = {},
    ) -> str:
        """
        Add liquidity into private pool.
        """

        if token == ZERO_ADDRESS:
            options["value"] = amount

        return self.executor.send_transaction(
            method=self.contract.functions.addLiquidityPrivatePool(
                Web3.toChecksumAddress(pool),
                Web3.toChecksumAddress(token),
                amount,
            ),
            options=options,
        )

    def add_liquidity_public_pool(
        self,
        deposit: Deposit,
        options: Options = {},
    ) -> str:
        """
        Add liquidity into public pool.
        """
        if deposit["token"] == ZERO_ADDRESS:
            options["value"] = deposit["amount"]

        return self.executor.send_transaction(
            method=self.contract.functions.addLiquidityPublicPool(
                [
                    deposit["pool"],
                    deposit["token"],
                    deposit["amount"],
                    deposit["nonce"],
                    deposit["signature"],
                ]
            ),
            options=options,
        )

    def is_pool_authorized(self, pool: AnyAddress) -> bool:
        """
        Get pool authorization state for router
        """
        return self.executor.call(
            self.contract.functions.isPoolAuthorized(
                Web3.toChecksumAddress(pool),
            )
        )

    def killswitch_pool(
        self, pool: AnyAddress, enabled: bool, options: Options = {}
    ) -> str:
        """
        Set pool killswitch state
        """
        return self.executor.send_transaction(
            method=self.contract.functions.killswitchPool(
                Web3.toChecksumAddress(pool),
                enabled,
            ),
            options=options,
        )

    def migrate_pool_authorization(
        self, migrationRouter: AnyAddress, options: Options = {}
    ) -> str:
        """
        Migrate the pool's authorized router
        """
        return self.executor.send_transaction(
            method=self.contract.functions.migratePoolAuthorization(
                Web3.toChecksumAddress(migrationRouter),
            ),
            options=options,
        )

    def remove_liquidity_public_pool(
        self,
        pool: AnyAddress,
        token: AnyAddress,
        burn_amount: int,
        options: Options = {},
    ) -> str:
        """
        Remove liquidity from public pool.
        """
        return self.executor.send_transaction(
            method=self.contract.functions.removeLiquidityPublicPool(
                Web3.toChecksumAddress(pool),
                Web3.toChecksumAddress(token),
                burn_amount,
            ),
            options=options,
        )

    def remove_liquidity_public_pool_with_permit(
        self,
        pool: AnyAddress,
        token: AnyAddress,
        burn_amount: int,
        deadline: int,
        v: int,
        r: bytes,
        s: bytes,
        approved_max: bool,
        options: Options = {},
    ) -> str:
        """
        Remove liquidity from public pool.
        """
        return self.executor.send_transaction(
            method=self.contract.functions.removeLiquidityPublicPoolWithPermit(
                Web3.toChecksumAddress(pool),
                Web3.toChecksumAddress(token),
                burn_amount,
                deadline,
                v,
                r,
                s,
                approved_max,
            ),
            options=options,
        )

    def trade_multi_hop(self, quotes: List[RFQTQuote], options: Options = {}) -> str:
        """
        Trade RFQ-t multi hop
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeMultiHop(quotes),
            options=options,
        )

    def trade_rfq_m(self, quote: RFQMQuote, options: Options = {}) -> str:
        """
        Trade single-hop RFQ-m
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeRFQm(quote),
            options=options,
        )

    def trade_rfq_m_with_permit(
        self,
        quote: RFQMQuote,
        deadline: int,
        v: int,
        r: bytes,
        s: bytes,
        approve_max: bool,
        options: Options = {},
    ) -> str:
        """
        Trade single-hop RFQ-m with permit
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeRFQmWithPermit(
                quote,
                deadline,
                v,
                r,
                s,
                approve_max,
            ),
            options=options,
        )

    def trade_single_hop(self, quote: RFQTQuote, options: Options = {}) -> str:
        """
        Trade RFQ-t single hop
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeSingleHop(quote),
            options=options,
        )

    def trade_x_chain(
        self,
        quote: XChainRFQTQuote,
        protocol: XChainMessageProtocol,
        options: Options = {},
    ) -> str:
        """
        Trade RFQ-t cross chain
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeXChain(
                quote,
                protocol,
            ),
            options=options,
        )

    def trade_x_chain_rfq_m(
        self,
        quote: XChainRFQMQuote,
        protocol: XChainMessageProtocol,
        options: Options = {},
    ) -> str:
        """
        Trade RFQ-m cross chain
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeXChainRFQm(
                quote,
                protocol,
            ),
            options=options,
        )

    def trade_x_chain_rfq_m_with_permit(
        self,
        quote: XChainRFQMQuote,
        protocol: XChainMessageProtocol,
        deadline: int,
        v: int,
        r: bytes,
        s: bytes,
        approve_max: bool,
        options: Options = {},
    ) -> str:
        """
        Trade RFQ-m cross chain with permit
        """
        return self.executor.send_transaction(
            method=self.contract.functions.tradeXChainRFQmWithPermit(
                quote,
                protocol,
                deadline,
                v,
                r,
                s,
                approve_max,
            ),
            options=options,
        )

    def update_governance(self, governance: AnyAddress, options: Options = {}) -> str:
        """
        Update governance contract
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updateGovernance(
                Web3.toChecksumAddress(governance),
            ),
            options=options,
        )

    def update_migration_router_status(
        self, router: AnyAddress, status: bool, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateMigrationRouterStatus(
                Web3.toChecksumAddress(router),
                status,
            ),
            options=options,
        )

    def update_pool_authorization(
        self, pool: AnyAddress, authorized: bool, options: Options = {}
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updatePoolAuthorization(
                Web3.toChecksumAddress(pool),
                authorized,
            ),
            options=options,
        )

    def update_x_chain_ua(self, x_chain_ua: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateXChainUa(
                Web3.toChecksumAddress(x_chain_ua)
            ),
            options=options,
        )
