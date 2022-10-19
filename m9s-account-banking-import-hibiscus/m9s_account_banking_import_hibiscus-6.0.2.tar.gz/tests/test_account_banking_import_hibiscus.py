# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest

from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountBankingImportHibiscusTestCase(ModuleTestCase):
    'Test Account Banking Import Hibiscus module'
    module = 'account_banking_import_hibiscus'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountBankingImportHibiscusTestCase))
    return suite
