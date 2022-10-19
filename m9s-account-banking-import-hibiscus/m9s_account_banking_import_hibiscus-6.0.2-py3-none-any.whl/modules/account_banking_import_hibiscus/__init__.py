# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool

from . import banking_import

__all__ = ['register']


def register():
    Pool.register(
        banking_import.BankingImportConfiguration,
        banking_import.BankingImportLine,
        banking_import.BankingImportRuleInformation,
        module='account_banking_import_hibiscus', type_='model')
