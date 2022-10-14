import os
import sys

from hexbytes import HexBytes
from eth_account.messages import encode_defunct

from hashflow.util import Deposit, HTokenType

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hashflow.client import Hashflow
from eth_typing.evm import HexAddress
from eth_typing.encoding import HexStr

from web3 import Web3
from web3.types import Wei

OWNER_ADDRESS = HexAddress(HexStr("0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266"))
OWNER_PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

ACCOUNT_ADDRESS = HexAddress(HexStr("0x9965507d1a55bcc2695c58ba16fb37d819b0a4dc"))
ACCOUNT_PRIVATE_KEY = (
    "0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba"
)
WETH = HexAddress(HexStr("0x0165878A594ca255338adfa4d48449f69242Eb8F"))
ETH = HexAddress(HexStr("0x0000000000000000000000000000000000000000"))

LOCALHOST_NETWORK_ID: int = 31337
LOCALHOST_NODE = "http://127.0.0.1:8545"

hashflow = Hashflow(
    private_key=ACCOUNT_PRIVATE_KEY,
    network_id=LOCALHOST_NETWORK_ID,
    jsonRpcUrl=LOCALHOST_NODE,
)

hashflow_owner = Hashflow(
    private_key=OWNER_PRIVATE_KEY,
    network_id=LOCALHOST_NETWORK_ID,
    jsonRpcUrl=LOCALHOST_NODE,
)

w3 = hashflow.executor.web3
factory_contract = hashflow.contracts.factory.contract


def test_private_pool_liquidity_gas0():
    event_hash = w3.keccak(text="CreatePool(address,address,bool)")
    tx_hash = hashflow.contracts.factory.create_pool(
        name="private testpool",
        signer=ACCOUNT_ADDRESS,
        options={"from": Web3.toChecksumAddress(ACCOUNT_ADDRESS)},
    )

    receipt = w3.eth.get_transaction_receipt(HexBytes(tx_hash))
    log = next(log for log in receipt["logs"] if event_hash in log["topics"])
    processed_log = factory_contract.events.CreatePool().processLog(log)
    priv_pool_address = processed_log["args"]["pool"]
    priv_pool = hashflow.pool.get_private_pool(priv_pool_address)
    priv_pool.list_asset(ETH)

    hashflow.contracts.router.add_liquidity_private_pool(
        priv_pool_address,
        ETH,
        Wei(10000000000000000000),
        options={
            "from": Web3.toChecksumAddress(ACCOUNT_ADDRESS),
            "gasPrice": w3.eth.gas_price,
        },
    )

    priv_pool.update_withdrawal_account([ACCOUNT_ADDRESS], True)
    priv_pool.remove_liquidity(
        ETH,
        ACCOUNT_ADDRESS,
        Wei(5000000000000000000),
        options={
            "from": Web3.toChecksumAddress(ACCOUNT_ADDRESS),
            "gasPrice": w3.eth.gas_price,
        },
    )

    reserves = priv_pool.get_reserves(ETH)
    assert reserves == 5000000000000000000


def test_private_pool_liquidity_gas2():
    event_hash = w3.keccak(text="CreatePool(address,address,bool)")
    tx_hash = hashflow.contracts.factory.create_pool(
        name="private testpool 2",
        signer=ACCOUNT_ADDRESS,
        options={"from": Web3.toChecksumAddress(ACCOUNT_ADDRESS)},
    )

    receipt = w3.eth.get_transaction_receipt(HexBytes(tx_hash))
    log = next(log for log in receipt["logs"] if event_hash in log["topics"])
    processed_log = factory_contract.events.CreatePool().processLog(log)

    priv_pool_address = processed_log["args"]["pool"]
    priv_pool = hashflow.pool.get_private_pool(priv_pool_address)
    tx_hash_list_asset = priv_pool.list_asset(ETH)

    w3.eth.get_transaction_receipt(HexBytes(tx_hash_list_asset))

    hashflow.contracts.router.add_liquidity_private_pool(
        priv_pool_address,
        ETH,
        Wei(10000000000000000000),
        options={
            "from": Web3.toChecksumAddress(ACCOUNT_ADDRESS),
            "maxFeePerGas": Wei(80000000),
            "maxPriorityFeePerGas": Wei(20000000),
        },
    )

    priv_pool.update_withdrawal_account([ACCOUNT_ADDRESS], True)
    priv_pool.remove_liquidity(
        ETH,
        ACCOUNT_ADDRESS,
        Wei(5000000000000000000),
        options={
            "from": Web3.toChecksumAddress(ACCOUNT_ADDRESS),
            "maxFeePerGas": Wei(80000000),
            "maxPriorityFeePerGas": Wei(20000000),
        },
    )

    reserves = priv_pool.get_reserves(ETH)
    assert reserves == 5000000000000000000


def test_public_pool_liquidity():
    event_hash = w3.keccak(text="CreatePool(address,address,bool)")
    tx_hash = hashflow.contracts.factory.create_pool(
        name="public testpool",
        signer=ACCOUNT_ADDRESS,
        symbol="TTT",
        isPrivate=False,
        options={"from": Web3.toChecksumAddress(ACCOUNT_ADDRESS)},
    )
    receipt = w3.eth.get_transaction_receipt(HexBytes(tx_hash))
    log = next(log for log in receipt["logs"] if event_hash in log["topics"])
    processed_log = factory_contract.events.CreatePool().processLog(log)

    pub_pool_address = processed_log["args"]["pool"]
    pub_pool = hashflow.pool.get_public_pool(pub_pool_address)
    pub_pool.list_asset(ETH, 400000000000000000000)

    amount = Wei(40000000000000000000)
    chain_id = hashflow.contracts.chain_id
    nonce = hashflow.contracts.router.executor.get_nonce()
    depositHash = Web3.solidityKeccak(
        ["address", "address", "address", "uint256", "uint256", "uint256"],
        [
            Web3.toChecksumAddress(ACCOUNT_ADDRESS),
            Web3.toChecksumAddress(pub_pool_address),
            Web3.toChecksumAddress(ETH),
            amount,
            nonce,
            chain_id,
        ],
    )
    signedDeposit = hashflow.executor.sign_message(
        encode_defunct(primitive=depositHash)
    )

    hashflow.contracts.router.add_liquidity_public_pool(
        deposit=Deposit(
            pool=Web3.toChecksumAddress(pub_pool_address),
            token=Web3.toChecksumAddress(ETH),
            amount=amount,
            nonce=nonce,
            signature=signedDeposit,
        ),
        options={"from": Web3.toChecksumAddress(ACCOUNT_ADDRESS)},
    )

    reserves = pub_pool.get_reserves(ETH)
    assert reserves == 40000000000000000000

    h_token_address = pub_pool.h_tokens(HTokenType.lp, ETH)
    h_token = hashflow.erc20.get_token(h_token_address)
    h_token.approve(hashflow.erc20.router_address)
    h_token_exchange_rate = 0.02

    amount_wei = 20000000000000000000
    amount = int(amount_wei / h_token_exchange_rate)

    hashflow.contracts.router.remove_liquidity_public_pool(
        pub_pool_address,
        ETH,
        amount,
        options={"from": Web3.toChecksumAddress(ACCOUNT_ADDRESS)},
    )

    post_reserves = pub_pool.get_reserves(ETH)
    assert (reserves - post_reserves) == amount_wei
