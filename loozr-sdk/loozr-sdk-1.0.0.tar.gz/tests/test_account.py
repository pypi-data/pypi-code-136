import unittest
import time

from loozr_sdk.accounts import NearClient, new_lzr_account, AccountHelper, \
    StorageBalance
from loozr_sdk.utils.account import LZR_MIXER_ACCOUNT_ID
from loozr_sdk.utils.constants import ACCOUNT_INIT_BALANCE

from loozr_sdk.utils.format import get_account_id_from_name, yocto_format


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.lzr = NearClient()

    def test_check_account(self):
        account_id = get_account_id_from_name(
            'test_user1-%s' % int(time.time() * 10_000))

        self.lzr.account.create_account(account_id,
                                        self.lzr.account.signer.public_key,
                                        ACCOUNT_INIT_BALANCE)

    def test_create_account_func(self):
        account_name = 'test_user2-%s' % int(time.time() * 10_000)

        new_account = new_lzr_account(self.lzr.account, account_name)
        self.assertEqual(new_account[0].state['amount'],
                         str(ACCOUNT_INIT_BALANCE))

    def test_account_id_by_name(self) -> None:
        account_name = 'test_user'
        account_id = get_account_id_from_name(account_name)
        self.assertEqual(account_id, f'test_user.{LZR_MIXER_ACCOUNT_ID}')

    def test_fund_transfer(self):
        account_name = 'test_user2-%s' % int(time.time() * 10_000)
        new_account = new_lzr_account(self.lzr.account, account_name)[0]

        account_helper = AccountHelper(self.lzr.account)
        storage_balance = account_helper.check_storage_balance(
            new_account.account_id)

        if StorageBalance.is_storage_enough(storage_balance):
            account_helper.transfer_ft(yocto_format(5), new_account.account_id)
        else:
            storage_required = StorageBalance.storage_required(storage_balance)
            account_helper.buy_storage(new_account.account_id,
                                       storage_required)
            account_helper.transfer_ft(yocto_format(5), new_account.account_id)
