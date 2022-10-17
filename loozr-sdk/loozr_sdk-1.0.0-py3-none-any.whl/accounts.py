from typing import Union
import json

from near_api.providers import JsonProvider
from near_api.signer import Signer, KeyPair
from near_api.account import Account

from loozr_sdk.utils.account import (LZR_MIXER_ACCOUNT_ID,
                                     LZR_MIXER_SECRET_KEY,
                                     LZR_FACTORY_MIXER_ACCOUNT_ID,
                                     LZR_FACTORY_MIXER_SECRET_KEY)
from loozr_sdk.utils.format import get_account_id_from_name
from loozr_sdk.utils.rpc import RPC_NODES
from loozr_sdk.utils.constants import ACCOUNT_INIT_BALANCE, \
    MINIMUM_STORAGE_BALANCE


class StorageBalance:
    def __init__(self, options: Union[dict, None]):
        if options:
            self.available_balance = int(options['available'])
            self.total_balance = int(options['total'])
        self.available_balance = 0
        self.total_balance = 0

    @staticmethod
    def is_storage_enough(storage: 'StorageBalance') -> bool:
        return storage.available_balance >= MINIMUM_STORAGE_BALANCE

    @staticmethod
    def storage_required(storage: 'StorageBalance') -> int:
        return MINIMUM_STORAGE_BALANCE - storage.available_balance


class ClientOptions:
    ACCOUNT_ID = ''
    SECRET_KEY = ''
    RPC_NODE = ''

    def __init__(self, account_id: str, secret_key: str,
                 rpc_node: str = 'testnet'):
        self.ACCOUNT_ID = account_id
        self.SECRET_KEY = secret_key

        if rpc_node not in RPC_NODES.keys():
            self.RPC_NODE = RPC_NODES['testnet']

        self.RPC_NODE = RPC_NODES[rpc_node]

    def __str__(self):
        return f'{self.RPC_NODE} - {self.ACCOUNT_ID}'


class NearClient:
    def __init__(self, options: ClientOptions = ClientOptions(
        LZR_MIXER_ACCOUNT_ID, LZR_MIXER_SECRET_KEY)
                 ) -> None:
        self.provider = JsonProvider(options.RPC_NODE)
        self.signer = Signer(options.ACCOUNT_ID, KeyPair(options.SECRET_KEY))
        self.account = Account(self.provider, self.signer, options.ACCOUNT_ID)


class FactoryClient(NearClient):
    def __init__(self):
        options = ClientOptions(LZR_FACTORY_MIXER_ACCOUNT_ID,
                                LZR_FACTORY_MIXER_SECRET_KEY)
        super().__init__(options=options)


class CoinRouterClient(NearClient):
    def __init__(self, contract_account_id: str):
        options = ClientOptions(contract_account_id,
                                LZR_FACTORY_MIXER_SECRET_KEY)
        super().__init__(options=options)


class AccountHelper:
    def __init__(self, account: Account):
        self.account = account

    def check_account(self, account_id):
        """Gets account details of `account_id` from
        the near blockchain or throw a JsonProviderError
        if account does not exist"""
        res = self.account.provider.get_account(account_id)
        return res

    def check_storage_balance(
            self,
            account_id: str,
            contract_id: str = LZR_MIXER_ACCOUNT_ID) -> StorageBalance:
        """
        Checks for the current storage balance of `account_id` on `contract_id`
        Parameters

        ----------
        account_id
        contract_id

        Returns
        -------
        An instance of `StorageBalance` containing the `account_id`
        storage balance
        """
        method = 'storage_balance_of'
        args = json.dumps({"account_id": account_id}).encode('utf8')
        response = self.account.provider.view_call(contract_id, method, args)
        result = json.loads("".join(map(chr, response['result'])))
        return StorageBalance(result)

    def buy_storage(self, account_id: str, amount: int,
                    contract_id: str = LZR_MIXER_ACCOUNT_ID) -> None:
        """
        Purchases storage of `amount` from `contract_id`.

        Parameters
        ----------
        account_id
        amount
        contract_id

        Returns
        -------
        """
        method = 'storage_deposit'
        args = {"account_id": account_id, "registration_only": True}
        self.account.function_call(contract_id, method, args, amount=amount)

    def transfer_ft(self, amount: Union[str, int], recipient: str,
                    contract_id: str = LZR_MIXER_ACCOUNT_ID):
        """
        Transfers coin from the current account to `recipient`
        account in `contract_id`

        The recipient account is first validated to confirm if it
        exists on the near blockchain before
        carrying out the transaction

        Parameters
        ----------
        amount: the amount of tokens to transfer
        recipient: near account to receive the token
        contract_id: ft contract to interact with

        Returns
        -------
        dict containing transaction result
        """
        self.check_account(recipient)
        method = 'ft_transfer'
        args = {"receiver_id": recipient, "amount": str(amount)}
        self.account.function_call(contract_id, method, args, amount=1)


def new_lzr_account(account: Account, user_account_name: str,
                    initial_balance=ACCOUNT_INIT_BALANCE):
    account_id = get_account_id_from_name(user_account_name)
    result = account.create_account(account_id, account.signer.public_key,
                                    initial_balance)
    signer = Signer(account_id, account.signer.key_pair)
    new_user_account = Account(account.provider, signer, account_id)
    return new_user_account, result
