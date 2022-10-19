# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

try:
    from trytond.modules.account_banking_import_hibiscus.tests.test_account_banking_import_hibiscus import (
        suite)
except ImportError:
    from .test_account_banking_import_hibiscus import suite

__all__ = ['suite']
