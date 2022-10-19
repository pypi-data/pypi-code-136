# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import os
import sys

from decimal import Decimal

import requests

from trytond.config import config
from trytond.exceptions import UserError
from trytond.i18n import gettext
from trytond.model import fields
from trytond.modules.account_banking_import.utils import str2date
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Bool, Eval, Not
from trytond.rpc import RPC

HIBISCUS_URI = config.get('hibiscus', 'uri')
HIBISCUS_USER = config.get('hibiscus', 'user')
HIBISCUS_PASSWORD = config.get('hibiscus', 'password')
HIBISCUS_VERIFY = config.getboolean('hibiscus', 'verify')


class BankingImportConfiguration(metaclass=PoolMeta):
    __name__ = 'banking.import.configuration'

    hibiscus_account = fields.Selection('selection_accounts',
        'Hibiscus Bank Account', states={
            'required': Eval('import_method') == 'hibiscus',
            'invisible': Eval('import_method') != 'hibiscus',
            'readonly': Not(Bool(Eval('active'))),
            }, depends=['import_method', 'active'])
    paypal = fields.Boolean('Internal balance check',
        help='Activate this box if you want to use internal '
        'balance control instead of the balances provided '
        'by Hibiscus, e.g. if the Hibiscus account is a '
        'Paypal account provided by the hibiscus.mashup-Plugin '
        '(Richter).')

    @classmethod
    def __setup__(cls):
        super(BankingImportConfiguration, cls).__setup__()
        method = ('hibiscus', 'Hibiscus')
        if method not in cls.import_method.selection:
            cls.import_method.selection.append(method)
        cls.__rpc__.update({'selection_accounts': RPC(False)})

    @staticmethod
    def default_paypal():
        return False

    @classmethod
    def validate(cls, configurations):
        super().validate(configurations)
        cls.check_entry_date(configurations)

    @classmethod
    def check_entry_date(cls, configurations):
        for configuration in configurations:
            if (configuration.import_method == 'hibiscus'
                    and configuration.entry_date != 'date'):
                raise UserError(gettext(
                    'account_banking_import_hibiscus.msg_wrong_entry_date'))

    @classmethod
    def get_hibiscus_request(cls, method):
        if not HIBISCUS_URI:
            raise UserError(gettext(
                    'account_banking_import_hibiscus.missing_configuration'))
        rest_uri = os.path.join(HIBISCUS_URI, 'webadmin/rest/hibiscus/',
            method)
        response = requests.get(rest_uri,
            auth=(HIBISCUS_USER, HIBISCUS_PASSWORD), verify=HIBISCUS_VERIFY)
        if response.status_code == 401:
            raise UserError(gettext(
                    'account_banking_import_hibiscus.unauthorized'))
        elif response.status_code != 200:
            raise UserError(gettext(
                    'account_banking_import_hibiscus.connection_failed',
                    response.status_code))
        return response.json()

    @classmethod
    def selection_accounts(cls):
        accounts = []
        # Do not call the hibiscus server under unit testing
        if 'unittest' not in sys.modules:
            accounts = cls.get_hibiscus_request('konto/list')
        selection = []
        for account in accounts:
            selection.append((account['id'],
                    ', '.join([account['bezeichnung'], account['iban'],
                        account['bic']])))
        return selection

    def get_transactions_hibiscus(self):
        '''
        Import the transactions of the configured account from Hibiscus

        We rely on the correctness of the sequence of hibiscus IDs and the
        correct balance provided by Hibiscus.
        '''
        pool = Pool()
        ImportLine = pool.get('banking.import.line')
        Date = pool.get('ir.date')
        today = Date.today()

        last_line = ImportLine.search([
                ('bank_import_config', '=', self.id),
                ], order=[('hibiscus_id', 'DESC')], limit=1)
        if last_line:
            hibiscus_id, date = last_line[0].hibiscus_id, last_line[0].date
            delta = today - date
            # get one day in the past to be sure to overlap
            days = delta.days + 1
        else:
            hibiscus_id = -1
            days = 9999

        params = 'konto/%s/umsaetze/days/%s' % (self.hibiscus_account, days)
        transactions = self.__class__.get_hibiscus_request(params)
        lines = []
        # hibiscus returns the newest entry first
        for transaction in reversed(transactions):
            if int(transaction['id']) > int(hibiscus_id):
                purpose = ''
                for key in ('zweck', 'zweck2', 'zweck3'):
                    if key in transaction:
                        purpose += transaction[key] + '\n'
                date = transaction['datum']
                valuta_date = transaction['valuta']
                try:
                    date = str2date(date, format='%Y-%m-%d')
                except:
                    raise UserError(gettext(
                            'account_banking_import_hibiscus.invalid_date',
                            date, hibiscus_id))
                try:
                    valuta_date = str2date(valuta_date, format='%Y-%m-%d')
                except:
                    raise UserError(gettext(
                            'account_banking_import_hibiscus.invalid_date',
                            valuta_date, hibiscus_id))
                line = {
                    'bank_import_config': self,
                    'date': date,
                    'valuta_date': valuta_date,
                    'contra_name': transaction.get('empfaenger_name', None),
                    'contra_account': transaction.get('empfaenger_konto', None),
                    'contra_bank_code': transaction.get('empfaenger_blz', None),
                    'amount': Decimal(transaction['betrag']),
                    'purpose': purpose,
                    # The PayPal plugin provides sometimes weird balances
                    # exceeding the digits of the field
                    'balance': self.journal.currency.round(
                        Decimal(transaction['saldo'])),
                    'kind': transaction['art'],
                    'customer_ref': transaction['customerref'],
                    'code': transaction.get('gvcode', None),
                    'addkey': transaction.get('addkey', None),
                    'primanota': transaction.get('primanota', None),
                    'hibiscus_id': transaction['id'],
                    }
                lines.append(line)
        if lines:
            # Recalculate line balances for PayPal accounts (#2904).
            # The Richter hibiscus.mashup writes wrong balances.
            # Sadly the upstream of the Richter plugin is uncommunicative and
            # the plugin is closed source. So we have to recalculate the
            # balances on our own to get reliable results.
            if self.paypal:
                last_line = ImportLine.search([
                        ('bank_import_config', '=', self.id),
                        ], order=[('id', 'DESC')], limit=1)
                if last_line:
                    balance = last_line[0].balance
                else:
                    balance = Decimal('0.0')
                for line in lines:
                    balance += line['amount']
                    line['balance'] = balance
            ImportLine.create(lines)


class BankingImportLine(metaclass=PoolMeta):
    __name__ = 'banking.import.line'

    hibiscus_id = fields.Integer('Hibiscus ID', readonly=True)


class BankingImportRuleInformation(metaclass=PoolMeta):
    __name__ = 'banking.import.rule.information'

    @classmethod
    def key_selection_excludes(cls):
        return super().key_selection_excludes() + ['hibiscus_id']
