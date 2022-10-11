from enum import Enum
from typing import List, Optional, Tuple, Set

from ._wallet_contract import SendModeEnum
from ._wallet_contract import WalletContract
from ._wallet_contract_v2 import WalletV2ContractR1, WalletV2ContractR2
from ._wallet_contract_v3 import WalletV3ContractR1, WalletV3ContractR2
from ._wallet_contract_v4 import WalletV4ContractR1, WalletV4ContractR2
from ...crypto import mnemonic_new, mnemonic_to_wallet_key, mnemonic_is_valid
from ...crypto.exceptions import InvalidMnemonicsError


class WalletVersionEnum(str, Enum):
    v2r1 = 'v2r1'
    v2r2 = 'v2r2'
    v3r1 = 'v3r1'
    v3r2 = 'v3r2'
    v4r1 = 'v4r1'
    v4r2 = 'v4r2'

    @classmethod
    def with_subwallet_id(cls) -> Set[str]:
        return {cls.v3r1.value, cls.v3r2.value, cls.v4r1.value, cls.v4r2.value}


class Wallets:
    default_version = WalletVersionEnum.v3r2
    ALL = {
        WalletVersionEnum.v2r1: WalletV2ContractR1,
        WalletVersionEnum.v2r2: WalletV2ContractR2,
        WalletVersionEnum.v3r1: WalletV3ContractR1,
        WalletVersionEnum.v3r2: WalletV3ContractR2,
        WalletVersionEnum.v4r1: WalletV4ContractR1,
        WalletVersionEnum.v4r2: WalletV4ContractR2,
    }

    @classmethod
    def create(cls, version: WalletVersionEnum, workchain: int,
               subwallet_id: Optional[int] = None, password: Optional[str] = None) -> Tuple[
        List[str], bytes, bytes, WalletContract]:
        """
        :rtype: (List[str](mnemonics), bytes(public_key), bytes(private_key), WalletContract(wallet))
        """
        mnemonics = mnemonic_new(password=password)
        pub_k, priv_k = mnemonic_to_wallet_key(mnemonics)
        wallet = cls.ALL[version](
            public_key=pub_k, private_key=priv_k, wc=workchain, subwallet_id=subwallet_id)

        return mnemonics, pub_k, priv_k, wallet

    @classmethod
    def from_mnemonics(cls, mnemonics: List[str], version: WalletVersionEnum = default_version,
                       workchain: int = 0, subwallet_id: Optional[int] = None) -> Tuple[
        List[str], bytes, bytes, WalletContract]:
        """
        :rtype: (List[str](mnemonics), bytes(public_key), bytes(private_key), WalletContract(wallet))
        """
        if not mnemonic_is_valid(mnemonics):
            raise InvalidMnemonicsError()

        pub_k, priv_k = mnemonic_to_wallet_key(mnemonics)
        wallet = cls.ALL[version](
            public_key=pub_k, private_key=priv_k, wc=workchain, subwallet_id=subwallet_id)

        return mnemonics, pub_k, priv_k, wallet

    @classmethod
    def to_addr_pk(cls, mnemonics: List[str], version: WalletVersionEnum = default_version,
                   workchain: int = 0, subwallet_id: Optional[int] = None) -> Tuple[bytes, bytes]:
        """
        :rtype: (bytes(addr), bytes(pk)
        """
        _mnemonics, _pub_k, priv_k, wallet = cls.from_mnemonics(
            mnemonics, version, workchain, subwallet_id)

        return wallet.address.to_buffer(), priv_k[:32]


__all__ = [
    'WalletV2ContractR1',
    'WalletV2ContractR2',
    'WalletV3ContractR1',
    'WalletV3ContractR2',
    'WalletV4ContractR1',
    'WalletV4ContractR2',
    'WalletContract',
    'SendModeEnum',
    'WalletVersionEnum',
    'Wallets',
]
