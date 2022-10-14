import os
from pathlib import Path
from typing import Type

from web3 import Web3
from web3.contract import Contract

from encrypticoin_etalon.utility.compile import compile_freeze_solidity_contract


def load_etalon_contract_cls(w3: Web3, force: bool = False, require_frozen: bool = False) -> Type[Contract]:
    """
    To get an actual contract instance, create it with its address.
    """
    abi, bytecode = compile_freeze_solidity_contract(
        Path(os.path.dirname(os.path.abspath(__file__)), "BEP20EtalonToken.sol"),
        force=force,
        require_frozen=require_frozen,
    )
    return w3.eth.contract(abi=abi, bytecode=bytecode)
