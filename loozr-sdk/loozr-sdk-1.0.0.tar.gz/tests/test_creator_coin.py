import unittest
import time

from loozr_sdk.creator_coin import create_coin, CreatorCoinRouter
from loozr_sdk.utils.format import yocto_format


class CoinTest(unittest.TestCase):
    def test_create_coin(self):
        coin_name = 'my_coin_%s' % int(time.time() * 10_000)
        create_coin(coin_name)

    def test_purchase_curve_func(self):
        current_supply = yocto_format(155.344952441)
        reserve_balance = yocto_format(3748.798188566)
        buy_amount = yocto_format(0.000001206)
        purchase_return = CreatorCoinRouter._calc_polynomial_mint(
            buy_amount, current_supply)
        self.assertEqual(purchase_return, yocto_format(1.6658304957672954e-8))

        bancor_purchase_return = CreatorCoinRouter._calc_bancor_mint(
            buy_amount, reserve_balance, current_supply)
        self.assertEqual(bancor_purchase_return,
                         yocto_format(1.665832953286128e-8))
