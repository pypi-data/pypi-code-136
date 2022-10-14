import json
import os
import time
from typing import Type
from hexbytes import HexBytes

from eth_typing.evm import AnyAddress, ChecksumAddress, Address, Hash32, BlockNumber
from eth_typing.encoding import HexStr
from web3 import Web3
from web3.types import TxReceipt, ENS
from web3.contract import Contract

from hashflow.util import (
    UnsignedRFQMQuoteStruct,
    UnsignedRFQTQuoteStruct,
    UnsignedXChainRFQTQuoteStruct,
)
from hashflow.constants import ZERO_ADDRESS

# -----------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------


def create_hashflow_contract(web3: Web3, name: str, network_id: int) -> Type[Contract]:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    abi_file_path = os.path.join(this_folder, "abi/I{}.json".format(name))
    deployed_file_path = os.path.join(this_folder, "deployed.json")
    deployed_addresses = json.load(open(deployed_file_path, "r"))
    contract_address = deployed_addresses[name][str(network_id)]["address"]
    return web3.eth.contract(
        address=contract_address, abi=json.load(open(abi_file_path, "r"))
    )


def create_contract(
    web3: Web3, name: str, address: Address | ChecksumAddress | ENS
) -> Contract:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    abi_file_path = os.path.join(this_folder, "abi/{}.json".format(name))
    return web3.eth.contract(address=address, abi=json.load(open(abi_file_path, "r")))


def get_receipt(web3: Web3, tx_hash: Hash32 | HexBytes | HexStr) -> TxReceipt:
    return web3.eth.wait_for_transaction_receipt(tx_hash)


def hash_rfqt_quote(quote_data: UnsignedRFQTQuoteStruct, chain_id: int) -> str:
    """
    Generate the keccak hash of quote object.
    """
    return Web3.solidityKeccak(
        [
            "address",
            "address",
            "address",
            "address",
            "address",
            "address",
            "uint256",
            "uint256",
            "uint256",
            "uint256",
            "bytes32",
            "uint256",
        ],
        [
            quote_data["pool"],
            quote_data["trader"],
            quote_data["effectiveTrader"] or quote_data["trader"],
            quote_data["externalAccount"] or ZERO_ADDRESS,
            quote_data["baseToken"],
            quote_data["quoteToken"],
            quote_data["maxBaseTokenAmount"],
            quote_data["maxQuoteTokenAmount"],
            quote_data["nonce"],
            quote_data["quoteExpiry"],
            quote_data["txid"],
            chain_id,
        ],
    ).hex()


def hash_maker_rfqm_quote(quote_data: UnsignedRFQMQuoteStruct, chain_id: int) -> str:
    """
    Generate the keccak hash of quote object.
    """
    return Web3.solidityKeccak(
        [
            "address",
            "address",
            "address",
            "address",
            "uint256",
            "uint256",
            "uint256",
            "bytes32",
            "uint256",
        ],
        [
            quote_data["pool"],
            quote_data["externalAccount"],
            quote_data["baseToken"],
            quote_data["quoteToken"],
            quote_data["baseTokenAmount"],
            quote_data["quoteTokenAmount"],
            quote_data["quoteExpiry"],
            quote_data["txid"],
            chain_id,
        ],
    ).hex()


def hash_x_chain_rfqt_quote(quote_data: UnsignedXChainRFQTQuoteStruct) -> str:
    """
    Generate the keccak hash of quote object.
    """
    return Web3.solidityKeccak(
        [
            "uint16",
            "uint16",
            "address",
            "address",
            "address",
            "address",
            "address",
            "address",
            "address",
            "uint256",
            "uint256",
            "uint256",
            "uint256",
            "bytes32",
        ],
        [
            quote_data["srcChainId"],
            quote_data["dstChainId"],
            quote_data["trader"],
            quote_data["srcPool"],
            quote_data["dstPool"],
            quote_data["srcExternalAccount"] or ZERO_ADDRESS,
            quote_data["dstExternalAccount"] or ZERO_ADDRESS,
            quote_data["baseToken"],
            quote_data["quoteToken"],
            quote_data["baseTokenAmount"],
            quote_data["quoteTokenAmount"],
            quote_data["quoteExpiry"],
            quote_data["nonce"],
            quote_data["txid"],
        ],
    ).hex()


def get_wallet_balance(
    web3: Web3,
    account: AnyAddress,
    token: AnyAddress = ZERO_ADDRESS,
):
    """
    Gets the on-chain balance of a users wallet for some asset.
    """
    if Web3.toChecksumAddress(token) == Web3.toChecksumAddress(ZERO_ADDRESS):
        balance = web3.eth.get_balance(Web3.toChecksumAddress(account))
    else:
        contract = create_contract(web3, "IERC20", Web3.toChecksumAddress(token))
        balance = contract.functions.balanceOf(Web3.toChecksumAddress(account)).call()
    return balance


def get_block_number(web3: Web3) -> BlockNumber:
    """
    Gets the latest block number.
    """
    return web3.eth.get_block_number()


def set_expiry(expiry: int) -> int:
    """
    Sets the quote expiry time (in seconds).
    """
    result = int(time.time()) + expiry
    return result


def convert_to_decimals(
    web3: Web3, amount: int, token: Address | ChecksumAddress | None = None
):
    """
    Convert asset amount to decimals.
    """
    decimals = 18
    if token is not None:
        contract = create_contract(web3, "IERC20", token)
        decimals = contract.functions.decimals().call()

    return amount * (10**decimals)


def convert_from_decimals(
    web3: Web3, amount: int, token: Address | ChecksumAddress | None = None
):
    """
    Convert asset amount from decimals.
    """
    decimals = 18
    if token is not None:
        contract = create_contract(web3, "IERC20", token)
        decimals = contract.functions.decimals().call()

    return amount / (10**decimals)
