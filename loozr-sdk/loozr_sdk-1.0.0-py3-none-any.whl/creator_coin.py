import json
from typing import Union

from near_api.account import Account

from loozr_sdk.accounts import FactoryClient, CoinRouterClient, AccountHelper
from loozr_sdk.utils.account import LZR_MIXER_ACCOUNT_ID
from loozr_sdk.utils.constants import (
    CONTRACT_ATTACHED_GAS, CONTRACT_INITIAL_BALANCE, RESERVE_RATIO, SLOPE,
    CONTRACT_PNG_DATA)
from loozr_sdk.utils.exceptions import InsufficientFundsError
from loozr_sdk.utils.format import balance_format, yocto_format


def create_coin(coin_name: str,
                initial_contract_balance=CONTRACT_INITIAL_BALANCE):
    """Takes `coin_name` as account_id without the domain, eg:
    instead of `myname.near` coin_name == `myname` and
    deploy a creator coin on the account.

    `account_id` should be non-existent at the time
    of making this call since the factory contract
    will create the account before deploying the contract.

    Parameters
    ----------
    coin_name
    initial_contract_balance
    """
    factory_account = FactoryClient()
    factory_contract_id = factory_account.account.account_id
    method = 'create'
    args = {"owner_id": factory_contract_id, "name": coin_name,
            "image_icon_data": CONTRACT_PNG_DATA,
            "base_token_contract_id": LZR_MIXER_ACCOUNT_ID}

    factory_account.account.function_call(
        factory_contract_id,
        method,
        args,
        gas=CONTRACT_ATTACHED_GAS,
        amount=initial_contract_balance)


class CreatorCoinRouter(CoinRouterClient):
    def __init__(self, contract_account_id: str):
        super().__init__(contract_account_id)

    @staticmethod
    def _calc_polynomial_mint(buy_amount_in_near: int,
                              current_supply_in_near: int) -> int:
        # amounts should be in base 10 for calculation to be done
        buy_amount = balance_format(buy_amount_in_near)
        current_supply = balance_format(current_supply_in_near)
        rate = 3  # (increase rate + 1, where increase rate: n = 2)

        # This is the formula:
        # (((((3 * p) / m) + (x ^ 3)) ^ r) - x)
        #
        # Constants
        # "3" here is n + 1, n is the rate of price increase
        # p = buy_amount
        # m = SLOPE
        # x = current_supply
        # r = RESERVE_RATIO
        result = pow(((rate * buy_amount) / SLOPE) +
                     pow(current_supply, 3), RESERVE_RATIO) - current_supply
        return yocto_format(result)

    @staticmethod
    def _calc_bancor_mint(
            buy_amount_in_near: int, reserve_balance_in_near: int,
            current_supply_in_near: int) -> Union[int, float]:
        buy_amount = balance_format(buy_amount_in_near)
        current_supply = balance_format(current_supply_in_near)
        reserve_balance = balance_format(reserve_balance_in_near)
        # This is the formula:
        # x * ((1 + p / rb) ^ (r) - 1)
        #
        # Constants
        # p = buy_amount
        # rb = reserve_balance
        # x = current_supply
        # r = RESERVE_RATIO
        result = current_supply * (
                pow(1 + (buy_amount / reserve_balance), RESERVE_RATIO) - 1)
        return yocto_format(result)

    def calc_purchase_return(
            self, buy_amount: Union[str, int]) -> Union[int, float]:
        """
        This method calculates the amount of creator coin to be minted for
        `buy_amount` of loozr

        Parameters
        ----------
        buy_amount

        Returns
        -------
        int
        """
        reserve_balance = self.reserve_balance()
        current_supply = self.total_supply()

        if reserve_balance == 0:
            return self._calc_polynomial_mint(int(buy_amount), current_supply)
        return self._calc_bancor_mint(int(buy_amount), reserve_balance,
                                      current_supply)

    def calc_sale_return(self, coin_to_sell: Union[str, int]) -> int:
        """
        This method calculates the return in loozr of the creator to be sold
        (`sale_amount`)

        Parameters
        ----------
        coin_to_sell

        Returns
        -------

        """
        reserve_balance = balance_format(self.reserve_balance())
        current_supply = balance_format(self.total_supply())

        # This is the formula:
        # rb * (1 - (1 - p / x) ^ (1 / r))
        #
        # Constants
        # p = coin_to_sell
        # rb = reserve_balance
        # x = current_supply
        # r = RESERVE_RATIO
        result = reserve_balance * (
                1 - pow((1 - (coin_to_sell / current_supply)),
                        (1 / RESERVE_RATIO)))
        return yocto_format(result)

    def buy_token(self, account: Account, amount: int, founder_id: str,
                  founder_percent: int):
        """Sends loozr to creator coin contract in exchange for creator coin.

        `amount` is first transferred from `account_id` to the
        creator coin contract before calling the minting function.
        This is to make sure there is always loozr in the reserve to
        compute the bonding curve functions

        Parameters
        ----------
        founder_percent
        founder_id
        amount: Amount in loozr to send in exchange for creator coin
        account: Account sending the transaction
        """
        method = 'ft_mint'
        args = {"account_id": account.account_id, "amount": str(amount),
                "founder_id": founder_id,
                "founder_percent": str(founder_percent)}

        transfer_done = False

        # Todo: put the transfer and mint function call in a batch call so if
        #  one fails both with be reverted
        account_helper_provider = AccountHelper(account)
        account_helper_provider.transfer_ft(str(amount),
                                            self.account.account_id,
                                            LZR_MIXER_ACCOUNT_ID)
        transfer_done = True
        try:
            res = self.account.function_call(
                self.account.account_id, method, args)
            return res
        except Exception as err:
            # refunding user the amount sent upon failure after transfer is
            # successful

            if transfer_done:
                account_helper_provider = AccountHelper(self.account)
                account_helper_provider.transfer_ft(str(amount),
                                                    account.account_id,
                                                    LZR_MIXER_ACCOUNT_ID)
            raise err

    def sell_token(self, account_id: str, amount: int):
        """
        Sells creator coin in exchange for loozr

        Parameters
        ----------
        account_id: receiver of the loozr token
        amount: amount of creator coin to sell

        Returns
        -------
        """
        method = 'ft_burn'
        amount_to_burn = self.calc_sale_return(amount)
        args = {"account_id": account_id, "sell_amount": str(
            amount), "return_value": amount_to_burn}
        if self.balance_of(account_id) < amount:
            raise InsufficientFundsError('Coin in balance not enough to sell.')
        res = self.account.function_call(
            self.account.account_id, method, args, amount=1)
        return res

    def reserve_balance(self):
        method = 'reserve_balance'
        args = json.dumps({}).encode('utf8')

        res = self.account.provider.view_call(
            self.account.account_id, method, args)
        balance = json.loads("".join(map(chr, res['result'])))
        return balance

    def total_supply(self):
        method = 'ft_total_supply'
        args = json.dumps({}).encode('utf8')

        res = self.account.provider.view_call(
            self.account.account_id, method, args)
        total_supply = json.loads("".join(map(chr, res['result'])))
        return total_supply

    def balance_of(self, account_id: str):
        method = 'ft_balance_of'
        args = json.dumps({"account_id": account_id}).encode('utf8')

        res = self.account.provider.view_call(
            self.account.account_id, method, args)
        balance = json.loads("".join(map(chr, res['result'])))
        return balance
