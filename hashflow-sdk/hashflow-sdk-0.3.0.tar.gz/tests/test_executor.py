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

ACCT1_ADDRESS = HexAddress(HexStr("0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266"))
ACCT1_PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

ACCT2_ADDRESS = HexAddress(HexStr("0x70997970C51812dc3A010C7d01b50e0d17dc79C8"))
ACCT2_PRIVATE_KEY = "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"

ACCOUNT_ADDRESS = HexAddress(HexStr("0x9965507d1a55bcc2695c58ba16fb37d819b0a4dc"))
ACCOUNT_PRIVATE_KEY = (
    "0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba"
)
WETH = HexAddress(HexStr("0x5FbDB2315678afecb367f032d93F642f64180aa3"))
ETH = HexAddress(HexStr("0x0000000000000000000000000000000000000000"))

LOCALHOST_NETWORK_ID: int = 31337
LOCALHOST_NODE = "http://127.0.0.1:8545"

hashflow = Hashflow(
    private_key=ACCT1_PRIVATE_KEY,
    chain_id=LOCALHOST_NETWORK_ID,
    rpc_url=LOCALHOST_NODE,
)


w3 = hashflow.executor.web3


def test_send_native_token():
  eth_to_send = 1000000000000000000

  balance_acct2_before = w3.eth.getBalance(
    Web3.toChecksumAddress(ACCT2_ADDRESS)
  )

  tx_hash = hashflow.executor.send_native_token(
    ACCT2_ADDRESS,
    eth_to_send
  )

  balance_acct2_after = w3.eth.getBalance(
    Web3.toChecksumAddress(ACCT2_ADDRESS)
  )

  assert (balance_acct2_before + eth_to_send) == balance_acct2_after