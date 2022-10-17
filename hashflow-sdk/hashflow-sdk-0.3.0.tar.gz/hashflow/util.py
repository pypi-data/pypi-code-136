from typing import TypedDict, Union

import eth_keys as eth_keys
from eth_account import Account
from enum import IntEnum
from eth_typing.evm import ChecksumAddress
from eth_typing.encoding import HexStr
from web3.types import Nonce, Wei


class RFQType(IntEnum):
    rfq_t = 0
    rfq_m = 1


class XChainMessageProtocol(IntEnum):
    layer_zero = 0
    wormhole = 1


class HTokenType(IntEnum):
    lp = 0
    x_chain = 1


class UnsignedRFQTQuoteStruct(TypedDict):
    pool: ChecksumAddress
    externalAccount: ChecksumAddress
    trader: ChecksumAddress
    effectiveTrader: ChecksumAddress
    baseToken: ChecksumAddress
    quoteToken: ChecksumAddress
    effectiveBaseTokenAmount: int
    maxBaseTokenAmount: int
    maxQuoteTokenAmount: int
    quoteExpiry: int
    nonce: int
    txid: str


class UnsignedRFQMQuoteStruct(TypedDict):
    pool: ChecksumAddress
    externalAccount: ChecksumAddress
    trader: ChecksumAddress
    baseToken: ChecksumAddress
    quoteToken: ChecksumAddress
    baseTokenAmount: int
    quoteTokenAmount: int
    quoteExpiry: int
    txid: str


class UnsignedXChainRFQTQuoteStruct(TypedDict):
    srcChainId: int
    dstChainId: int
    srcPool: ChecksumAddress
    dstPool: bytes
    srcExternalAccount: ChecksumAddress
    dstExternalAccount: bytes
    trader: ChecksumAddress
    baseToken: ChecksumAddress
    quoteToken: ChecksumAddress
    baseTokenAmount: int
    quoteTokenAmount: int
    quoteExpiry: int
    nonce: int
    txid: str


class UnsignedXChainRFQMQuoteStruct(TypedDict):
    srcChainId: int
    dstChainId: int
    srcPool: ChecksumAddress
    dstPool: bytes
    srcExternalAccount: ChecksumAddress
    dstExternalAccount: bytes
    trader: ChecksumAddress
    baseToken: ChecksumAddress
    quoteToken: ChecksumAddress
    baseTokenAmount: int
    quoteTokenAmount: int
    quoteExpiry: int
    txid: str


class RFQTQuote(UnsignedRFQTQuoteStruct):
    signature: bytes


class RFQMQuote(UnsignedRFQMQuoteStruct):
    makerSignature: bytes
    takerSignature: bytes


class XChainRFQTQuote(UnsignedXChainRFQTQuoteStruct):
    signature: bytes


class XChainRFQMQuote(UnsignedXChainRFQMQuoteStruct):
    makerSignature: bytes
    takerSignature: bytes


Options = TypedDict(
    "Options",
    {
        "from": ChecksumAddress,
        "nonce": Nonce,
        "to": ChecksumAddress,
        "value": Wei,
        "gas": Wei,
        "gasPrice": Wei,
        "maxFeePerGas": Wei,
        "maxPriorityFeePerGas": Wei,
        "data": Union[bytes, HexStr],
        "chainId": int,
        "type": Union[int, HexStr],
    },
    total=False,
)

NativeTokenDetails = TypedDict(
    "NativeTokenDetails",
    {
        "name": str,
        "symbol": str,
        "decimals": int,
    },
)

Deposit = TypedDict(
    "Deposit",
    {
        "pool": ChecksumAddress,
        "token": ChecksumAddress,
        "amount": Wei,
        "nonce": int,
        "signature": bytes,
    },
)

AuthorizedXChainPool = TypedDict(
    "AuthorizedXChainPool",
    {
        "chainId": int,
        "pool": bytes,
    },
)


def strip_hex_prefix(input: str) -> str:
    if input[0:2] == "0x":
        return input[2:]
    else:
        return input


def normalize_to_bytearray(input: str | bytearray) -> bytearray:
    if type(input) is str:
        return bytearray.fromhex(strip_hex_prefix(input))
    elif type(input) is bytearray:
        return input
    else:
        raise TypeError("input incorrect type")


def private_key_to_address(key: bytearray) -> ChecksumAddress:
    eth_keys_key = eth_keys.keys.PrivateKey(key)
    return eth_keys_key.public_key.to_checksum_address()


def sign_digest(digest: str, private_key: bytearray) -> str:
    result = Account.signHash(digest, private_key)
    return result["signature"].hex()
