import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hashflow.client import Hashflow
from eth_typing.evm import HexAddress
from eth_typing.encoding import HexStr
from web3 import Web3

OPERATIONS_ADDRESS = HexAddress(HexStr("0x70997970c51812dc3a010c7d01b50e0d17dc79c8"))
OPERATIONS_PRIVATE_KEY = (
    "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d"
)

SIGNER_ADDRESS = HexAddress(HexStr("0x90f79bf6eb2c4f870365e785982e1f101e93b906"))
SIGNER_PRIVATE_KEY = (
    "0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6"
)

ACCOUNT_TWO_ADDRESS = HexAddress(HexStr("0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc"))
ACCOUNT_TWO_PRIVATE_KEY = (
    "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a"
)

LOCALHOST_NETWORK_ID: int = 31337
LOCALHOST_NODE = "http://127.0.0.1:8545"

hashflow = Hashflow(
    private_key=OPERATIONS_PRIVATE_KEY,
    network_id=LOCALHOST_NETWORK_ID,
    jsonRpcUrl=LOCALHOST_NODE,
)

hashflow2 = Hashflow(
    private_key=ACCOUNT_TWO_PRIVATE_KEY,
    network_id=LOCALHOST_NETWORK_ID,
    jsonRpcUrl=LOCALHOST_NODE,
)

w3 = hashflow.executor.web3
factory_contract = hashflow.contracts.factory.contract


def test_private_pool_creation():
    event_filter = factory_contract.events.CreatePool().createFilter(fromBlock="latest")
    hashflow.contracts.factory.create_pool(name="testpool1", signer=SIGNER_ADDRESS)

    event = event_filter.get_new_entries()
    pool = event[0]["args"]["pool"]
    assert type(pool) == str
    assert len(pool) == 42


def test_public_pool_creation():
    event_filter = factory_contract.events.CreatePool().createFilter(fromBlock="latest")
    hashflow2.contracts.factory.create_pool(
        name="testpool2",
        signer=SIGNER_ADDRESS,
        symbol="TST",
        isPrivate=False,
        options={"from": Web3.toChecksumAddress(ACCOUNT_TWO_ADDRESS)},
    )

    event = event_filter.get_new_entries()
    pool = event[0]["args"]["pool"]
    assert type(pool) == str
    assert len(pool) == 42
