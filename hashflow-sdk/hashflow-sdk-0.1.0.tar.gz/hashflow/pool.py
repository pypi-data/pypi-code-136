from typing import List, Tuple

from eth_typing.evm import AnyAddress, ChecksumAddress, HexAddress
from web3 import Web3

from hashflow.executor import Executor
from hashflow.functions import create_contract
from hashflow.util import (
    AuthorizedXChainPool,
    Deposit,
    HTokenType,
    Options,
    RFQMQuote,
    RFQTQuote,
    XChainMessageProtocol,
    XChainRFQMQuote,
    XChainRFQTQuote,
    normalize_to_bytearray,
)


class HashflowPool(object):
    def __init__(self, executor: Executor, address: AnyAddress):
        self.executor = executor
        self.contract = create_contract(
            self.executor.web3, "IHashflowPool", Web3.toChecksumAddress(address)
        )

    def authorized_routers(self, router: AnyAddress) -> bool:
        """
        Determine if router is authorized
        """
        return self.executor.call(
            self.contract.functions.authorizedRouters(Web3.toChecksumAddress(router))
        )

    def fill_x_chain(
        self,
        external_account: AnyAddress,
        txid: str,
        trader: AnyAddress,
        quote_token: AnyAddress,
        quote_token_amount: int,
        protocol: XChainMessageProtocol,
        options: Options,
    ) -> Tuple[HexAddress, int]:
        return self.executor.call(
            method=self.contract.functions.fillXChain(
                Web3.toChecksumAddress(external_account),
                normalize_to_bytearray(txid),
                Web3.toChecksumAddress(trader),
                Web3.toChecksumAddress(quote_token),
                quote_token_amount,
                protocol,
            ),
            options=options,
        )

    def get_reserves(self, token: AnyAddress) -> int:
        """
        Query pool's reserves for an asset.
        For eth, set token address to ZERO_ADDRESS
        """
        return self.executor.call(
            self.contract.functions.getReserves(Web3.toChecksumAddress(token))
        )

    def governance(self) -> ChecksumAddress:
        """
        Query governance contract address.
        """
        return self.executor.call(self.contract.functions.governance())

    def h_tokens(self, h_token_type: HTokenType, token: AnyAddress) -> ChecksumAddress:
        """
        Query a token's hToken address associated with the pool.
        """
        return self.executor.call(
            self.contract.functions.hTokens(h_token_type, Web3.toChecksumAddress(token))
        )

    def killswitch_operations(self, enabled: bool, options: Options = {}) -> str:
        """
        Disable/enable killswitch operations
        """
        return self.executor.send_transaction(
            method=self.contract.functions.killswitchOperations(enabled)
        )

    def migrate_router_authorization(
        self, new_router: AnyAddress, old_router: AnyAddress, options: Options = {}
    ) -> str:
        """
        Migrate router authorization for the pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.migrateRouterAuthorization(
                Web3.toChecksumAddress(new_router), Web3.toChecksumAddress(old_router)
            ),
            options=options,
        )

    def name(self) -> str:
        """
        Get pool name
        """
        return self.executor.call(self.contract.functions.name())

    def nonces(self, trader: AnyAddress) -> int:
        """
        Get pool nonce
        """
        return self.executor.call(
            self.contract.functions.nonces(Web3.toChecksumAddress(trader))
        )

    def operations(self) -> ChecksumAddress:
        """
        Quote pool operations (owner of the pool)
        """
        return self.executor.call(self.contract.functions.operations())

    def redeem_x_chain_tokens(
        self, token: AnyAddress, amount: int, options: Options = {}
    ) -> str:
        """
        Redeem x chain tokens that were generated due to insufficient liquidity during X-chain transfers
        """
        return self.executor.send_transaction(
            method=self.contract.functions.redeemXChainTokens(
                Web3.toChecksumAddress(token),
                amount,
            ),
            options=options,
        )

    def signer_configuration(self) -> Tuple[ChecksumAddress, bool]:
        """
        Query  signer configured for the pool
        """
        return self.executor.call(self.contract.functions.signerConfiguration())

    def symbol(self) -> str:
        """
        Query pool symbol
        """
        return self.executor.call(self.contract.functions.symbol())

    def trade(
        self,
        quote: RFQTQuote,
    ) -> bool:
        """
        Check if an RFQ-T trade will execute correctly
        """
        return self.executor.call(self.contract.functions.trade(quote))

    def trade_rfq_m(self, quote: RFQMQuote) -> bool:
        """
        Check if an RFQ-M trade will execute correctly
        """
        return self.executor.call(self.contract.functions.tradeRFQm(quote))

    def trade_x_chain(self, quote: XChainRFQTQuote) -> bool:
        """
        Check if a cross-chain RFQ-T trade will execute correctly
        """
        return self.executor.call(self.contract.functions.tradeXChain(quote))

    def trade_x_chain_rfq_m(self, quote: XChainRFQMQuote) -> bool:
        """
        Check if a cross-chain RFQ-M trade will execute correctly
        """
        return self.executor.call(self.contract.functions.tradeXChainRFQm(quote))

    def update_router_permissions(
        self,
        router: AnyAddress,
        authorized: bool,
        options: Options = {},
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateRouterPermissions(
                Web3.toChecksumAddress(router),
                authorized,
            ),
            options=options,
        )

    def update_signer(self, signer: AnyAddress, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateSigner(
                Web3.toChecksumAddress(signer),
            ),
            options=options,
        )

    def update_withdrawal_account(
        self,
        withdrawal_accounts: List[AnyAddress],
        authorized: bool,
        options: Options = {},
    ) -> str:
        """
        Pool owners can authorize/unauthorize whitelist addresses that be used to withdraw
        funds
        """
        checksum_accounts: List[ChecksumAddress] = []
        for account in withdrawal_accounts:
            checksum_accounts.append(Web3.toChecksumAddress(account))

        return self.executor.send_transaction(
            method=self.contract.functions.updateWithdrawalAccount(
                checksum_accounts,
                authorized,
            ),
            options=options,
        )

    def update_x_chain_pool_authorization(
        self,
        pools: List[AuthorizedXChainPool],
        protocols: List[XChainMessageProtocol],
        authorized: bool,
        options: Options,
    ) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateXChainPoolAuthorization(
                pools,
                protocols,
                authorized,
            ),
            options=options,
        )

    def update_x_chain_ua(self) -> None:
        return self.executor.call(self.contract.functions.updateXChainUa())


class HashflowPrivatePool(HashflowPool):
    def __init__(self, executor: Executor, address: AnyAddress):
        self.executor = executor
        self.contract = create_contract(
            self.executor.web3, "IHashflowPrivatePool", Web3.toChecksumAddress(address)
        )

    def add_liquidity(
        self,
        token: AnyAddress,
        liquidity_provider: AnyAddress,
        deposit_amount: int,
        options: Options = {},
    ) -> str:
        """
        Add liquidity to private pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.addLiquidity(
                Web3.toChecksumAddress(token),
                Web3.toChecksumAddress(liquidity_provider),
                deposit_amount,
            ),
            options=options,
        )

    def initialize(
        self,
        name: str,
        symbol: str,
        signer: AnyAddress,
        operations: AnyAddress,
        h_token_impl: AnyAddress,
        governance: AnyAddress,
        router: AnyAddress,
        options: Options = {},
    ) -> str:
        """
        Initialize new private pool with all key parameters
        """
        return self.executor.send_transaction(
            method=self.contract.functions.initialize(
                name,
                symbol,
                Web3.toChecksumAddress(signer),
                Web3.toChecksumAddress(operations),
                Web3.toChecksumAddress(h_token_impl),
                Web3.toChecksumAddress(governance),
                Web3.toChecksumAddress(router),
            ),
            options=options,
        )

    def list_asset(self, token: AnyAddress, options: Options = {}) -> str:
        """
        List new asset on pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.listAsset(
                Web3.toChecksumAddress(token),
            ),
            options=options,
        )

    def remove_liquidity(
        self,
        token: AnyAddress,
        recipient: AnyAddress,
        amount: int,
        options: Options = {},
    ) -> str:
        """
        Remove liquidity from private pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.removeLiquidity(
                Web3.toChecksumAddress(token),
                Web3.toChecksumAddress(recipient),
                amount,
            ),
            options=options,
        )


class HashflowPublicPool(HashflowPool):
    def __init__(self, executor: Executor, address: AnyAddress):
        self.executor = executor
        self.contract = create_contract(
            self.executor.web3, "IHashflowPublicPool", Web3.toChecksumAddress(address)
        )

    def add_liquidity(self, deposit: Deposit, options: Options = {}) -> str:
        """
        Deposit liquidity to public pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.addLiquidity(deposit),
            options=options,
        )

    def asset_details(
        self, token: AnyAddress
    ) -> Tuple[int, int, int, int, ChecksumAddress, ChecksumAddress, bool]:
        """
        Get details for a pool asset
        """
        return self.executor.call(
            self.contract.functions.assetDetails(
                Web3.toChecksumAddress(token),
            )
        )

    def deposit_yield(
        self, token: AnyAddress, amount: int, options: Options = {}
    ) -> str:
        """
        Pay out yield into the pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.depositYield(
                Web3.toChecksumAddress(token),
                amount,
            ),
            options=options,
        )

    def initialize(
        self,
        name: str,
        symbol: str,
        signer: AnyAddress,
        operations: AnyAddress,
        h_token_impl: AnyAddress,
        governance: AnyAddress,
        router: AnyAddress,
        options: Options = {},
    ) -> str:
        """
        Initialize new public pool with all key parameters
        """
        return self.executor.send_transaction(
            method=self.contract.functions.initialize(
                name,
                symbol,
                Web3.toChecksumAddress(signer),
                Web3.toChecksumAddress(operations),
                Web3.toChecksumAddress(h_token_impl),
                Web3.toChecksumAddress(governance),
                Web3.toChecksumAddress(router),
            ),
            options=options,
        )

    def list_asset(self, token: AnyAddress, cap: int, options: Options = {}) -> str:
        """
        List new asset on pool with cap
        """
        return self.executor.send_transaction(
            method=self.contract.functions.listAsset(
                Web3.toChecksumAddress(token),
                cap,
            ),
            options=options,
        )

    def migrate_mode(self) -> bool:
        """
        Checks whether the pool is currently being migrated
        """
        return self.executor.call(self.contract.functions.migrateMode())

    def remove_liquidity(
        self,
        token: AnyAddress,
        liquidity_provider: AnyAddress,
        burn_amount: int,
        options: Options = {},
    ) -> str:
        """
        Remove liquidity from private pool
        """
        return self.executor.send_transaction(
            method=self.contract.functions.removeLiquidity(
                Web3.toChecksumAddress(token),
                Web3.toChecksumAddress(liquidity_provider),
                burn_amount,
            ),
            options=options,
        )

    def transfer_assets(
        self,
        token: AnyAddress,
        recipient: AnyAddress,
        amount: int,
        options: Options = {},
    ) -> str:
        """
        Withdraw assets for rebalancing
        """
        return self.executor.send_transaction(
            method=self.contract.functions.transferAssets(
                Web3.toChecksumAddress(token), Web3.toChecksumAddress(recipient), amount
            ),
            options=options,
        )

    def update_cap(self, token: AnyAddress, cap: int, options: Options = {}) -> str:
        """
        Update an asset's cap.
        """
        return self.executor.send_transaction(
            method=self.contract.functions.updateCap(
                Web3.toChecksumAddress(token), cap
            ),
            options=options,
        )

    def update_migrate_mode(self, migration_mode: bool, options: Options = {}) -> str:
        return self.executor.send_transaction(
            method=self.contract.functions.updateMigrateMode(migration_mode),
            options=options,
        )


class Pool(object):
    def __init__(self, executor: Executor):
        self.executor = executor

    def get_public_pool(self, address: AnyAddress) -> HashflowPublicPool:
        return HashflowPublicPool(self.executor, address)

    def get_private_pool(self, address: AnyAddress) -> HashflowPrivatePool:
        return HashflowPrivatePool(self.executor, address)
