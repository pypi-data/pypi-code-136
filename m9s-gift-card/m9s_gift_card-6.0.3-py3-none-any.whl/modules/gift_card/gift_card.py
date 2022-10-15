# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from jinja2 import Environment, PackageLoader
from num2words import num2words
from sql import Table

from trytond.config import config
from trytond.exceptions import UserError
from trytond.i18n import gettext
from trytond.model import ModelSQL, ModelView, Unique, Workflow, fields
from trytond.pool import Pool
from trytond.pyson import Eval, If
from trytond.report import Report
from trytond.sendmail import SMTPDataManager, sendmail_transactional
from trytond.transaction import Transaction
from trytond.wizard import Button, StateTransition, StateView, Wizard

from nereid import render_email

_from = config.get('email', 'from', default='no-reply@localhost')


class GiftCard(Workflow, ModelSQL, ModelView):
    "Gift Card"
    __name__ = 'gift_card.gift_card'
    _rec_name = 'number'

    number = fields.Char(
        'Number', select=True, readonly=True, required=True,
        help='Number of the gift card'
    )
    origin = fields.Reference(
        'Origin', selection='get_origin', select=True,
        states={
            'readonly': Eval('state') != 'draft',
        }, depends=['state']
    )
    currency = fields.Many2One(
        'currency.currency', 'Currency', required=True,
        states={
            'readonly': Eval('state') != 'draft'
        }, depends=['state']
    )
    currency_digits = fields.Function(
        fields.Integer('Currency Digits'),
        'on_change_with_currency_digits'
    )
    amount = fields.Numeric(
        'Amount',
        digits=(16, Eval('currency_digits', 2)),
        states={
            'readonly': Eval('state') != 'draft'
        }, depends=['state', 'currency_digits'], required=True
    )

    amount_authorized = fields.Function(
        fields.Numeric(
            "Amount Authorized", digits=(16, Eval('currency_digits', 2)),
            depends=['currency_digits']
        ), 'get_amount'
    )
    amount_captured = fields.Function(
        fields.Numeric(
            "Amount Captured", digits=(16, Eval('currency_digits', 2)),
            depends=['currency_digits']
        ), 'get_amount'
    )

    amount_available = fields.Function(
        fields.Numeric(
            "Amount Available", digits=(16, Eval('currency_digits', 2)),
            depends=['currency_digits']
        ), 'get_amount'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('used', 'Used'),
    ], 'State', readonly=True, required=True)

    sale_line = fields.Many2One('sale.line', "Sale Line", readonly=True)

    sale = fields.Function(
        fields.Many2One('sale.sale', "Sale"), 'get_sale'
    )
    payment_transactions = fields.One2Many(
        "payment_gateway.transaction", "gift_card", "Payment Transactions",
        readonly=True
    )
    message = fields.Text("Message")
    recipient_email = fields.Char(
        "Recipient Email", states={
            'readonly': Eval('state') != 'draft'
        }
    )

    recipient_name = fields.Char(
        "Recipient Name", states={
            'readonly': Eval('state') != 'draft'
        }
    )

    is_email_sent = fields.Boolean("Is Email Sent ?", readonly=True)
    comment = fields.Text('Comment')

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().connection.cursor()
        model_data = Table('ir_model_data')

        # Migration from 6.0: Rename some ids to be more explicite
        if module_name == 'gift_card':
            for old_id, new_id in (
                    ('sequence_type_number', 'sequence_type_gift_card_number'),
                    ('sequence_number', 'sequence_gift_card_number'),
                    ('sequence_type_number_sequence_group_admin',
                        'sequence_type_gift_card_number_sequence_group_admin'),
                    ):
                cursor.execute(*model_data.select(model_data.id,
                        where=(model_data.fs_id == new_id)
                        & (model_data.module == module_name)))
                if cursor.fetchone():
                    continue
                cursor.execute(*model_data.update(
                        columns=[model_data.fs_id],
                        values=[new_id],
                        where=(model_data.fs_id == old_id)
                        & (model_data.module == module_name)))

        super().__register__(module_name)

    def get_sale(self, name):
        """
        Return sale for gift card using the origin and as fallback the
        sale line associated with it
        """
        Sale = Pool().get('sale.sale')

        if isinstance(self.origin, Sale):
            return self.origin.id
        return self.sale_line and self.sale_line.sale.id or None

    @staticmethod
    def default_currency():
        """
        Set currency of current company as default currency
        """
        Company = Pool().get('company.company')

        return Transaction().context.get('company') and \
            Company(Transaction().context.get('company')).currency.id or None

    def get_amount(self, name):
        """
        Returns authorized, captured and available amount for the gift card
        """
        PaymentTransaction = Pool().get('payment_gateway.transaction')

        if name == 'amount_authorized':
            return sum([t.amount for t in PaymentTransaction.search([
                ('state', '=', 'authorized'),
                ('gift_card', '=', self.id)
            ])])

        if name == 'amount_captured':
            return sum([t.amount for t in PaymentTransaction.search([
                ('state', 'in', ['completed', 'posted', 'done']),
                ('gift_card', '=', self.id)
            ])])

        if name == 'amount_available':
            return self.amount - sum([
                t.amount for t in PaymentTransaction.search([
                    ('state', 'in', ['authorized', 'completed','posted',
                                    'done']),
                    ('gift_card', '=', self.id)
                ])
            ])

    @staticmethod
    def default_state():
        return 'draft'

    @fields.depends('currency')
    def on_change_with_currency_digits(self, name=None):
        if self.currency:
            return self.currency.digits
        return 2

    @classmethod
    def __setup__(cls):
        super().__setup__()
        table = cls.__table__()
        cls._sql_constraints = [
            ('number_uniq', Unique(table, table.number),
             'The number of the gift card must be unique.')
        ]
        cls._transitions |= set((
            ('draft', 'active'),
            ('active', 'canceled'),
            ('draft', 'canceled'),
            ('canceled', 'draft'),
        ))
        cls._buttons.update({
            'cancel': {
                'invisible': ~Eval('state').in_(['draft', 'active']),
            },
            'draft': {
                'invisible': ~Eval('state').in_(['canceled']),
                'icon': If(
                    Eval('state') == 'cancel', 'tryton-clear',
                    'tryton-back'
                ),
            },
            'activate': {
                'invisible': Eval('state') != 'draft',
            }
        })

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('number'):
                values['number'] = cls.get_gift_card_number()
        return super().create(vlist)

    @classmethod
    def get_gift_card_number(cls):
        Configuration = Pool().get('gift_card.configuration')
        return Configuration(1).number_sequence.get()

    @classmethod
    def copy(cls, gift_cards, default=None):
        if default is None:
            default = {}
        default = default.copy()
        default['number'] = None
        default['sale_line'] = None
        default['state'] = cls.default_state()
        default['payment_transactions'] = None
        return super().copy(gift_cards, default=default)

    @classmethod
    @ModelView.button
    @Workflow.transition('active')
    def activate(cls, gift_cards):
        """
        Set gift cards to active state
        """
        for gift_card in gift_cards:
            if gift_card.recipient_email and not gift_card.is_email_sent:
                gift_card.send_gift_card_as_email()

    @classmethod
    @ModelView.button
    @Workflow.transition('draft')
    def draft(cls, gift_cards):
        """
        Set gift cards back to draft state
        """
        pass

    @classmethod
    @ModelView.button
    @Workflow.transition('canceled')
    def cancel(cls, gift_cards):
        """
        Cancel gift cards
        """
        pass

    @classmethod
    def get_origin(cls):
        return [
            (None, ''),
            ('sale.sale', 'Sale'),
        ]

    @classmethod
    def delete(cls, gift_cards):
        """
        It should not be possible to delete gift cards in active state
        """

        for gift_card in gift_cards:
            if gift_card.state == 'active':
                raise UserError(gettext("gift_card.deletion_not_allowed"))

        return super().delete(gift_cards)

    def _get_subject_for_email(self):
        """
        Returns the text to use as subject of email
        """
        return "Gift Card - %s" % self.number

    def _get_email_templates(self):
        """
        Returns a tuple of the form:

        (html_template, text_template)
        """
        env = Environment(loader=PackageLoader(
            'trytond.modules.gift_card', 'emails'
        ))
        return (
            env.get_template('gift_card_html.html'),
            env.get_template('gift_card_text.html')
        )

    def send_gift_card_as_email(self):
        """
        Send gift card as an attachment in the email
        """
        GiftCardReport = Pool().get('gift_card.gift_card', type='report')
        ModelData = Pool().get('ir.model.data')
        Group = Pool().get('res.group')

        group_id = ModelData.get_id(
            "gift_card", "gift_card_email_receivers"
        )
        bcc_emails = [user.email for user in [
                user for user in Group(group_id).users if user.email]]

        if not self.recipient_email:  # pragma: no cover
            return

        # Try to generate report twice
        # This is needed as sometimes `unoconv` fails to convert report to pdf
        for try_count in range(2):
            try:
                val = GiftCardReport.execute([self.id], {})
                break
            except:  # pragma: no cover
                if try_count == 0:
                    continue
                else:
                    return

        subject = self._get_subject_for_email()
        html_template, text_template = self._get_email_templates()

        recipients = [self.recipient_email] + bcc_emails
        email_gift_card = render_email(
            _from,
            recipients,
            subject,
            html_template=html_template,
            text_template=text_template,
            attachments={"%s.%s" % (val[3], val[0]): val[1]},
            card=self,
        )

        self.send_email(email_gift_card, to_addr=recipients)
        self.is_email_sent = True
        self.save()

    # TODO refactor this into common method, also used by
    # trytond_nereid/user.py
    def send_email(self, message, to_addr=None):
        """
        Generic method to call sendmail_transactional
        """
        datamanager = SMTPDataManager()
        Transaction().join(datamanager)

        if to_addr:
            sendmail_transactional(_from, to_addr, message,
                datamanager=datamanager)


class GiftCardReport(Report):
    __name__ = 'gift_card.gift_card'

    @classmethod
    def get_context(cls, records, header, data):
        """
        Update localcontext to add num2words
        """
        context = super().get_context(records, header, data)

        context['num2words'] = lambda *args, **kargs: num2words(
            *args, **kargs)
        context['company'] = context['user'].company
        return context


class GiftCardRedeemStart(ModelView):
    "Gift Card Redeem Start View"
    __name__ = 'gift_card.redeem.start'

    description = fields.Text('Description', required=True)
    gateway = fields.Many2One(
        'payment_gateway.gateway', 'Gateway', required=True,
        domain=[
            ('method', '=', 'gift_card'),
        ]
    )
    gift_card = fields.Many2One(
        'gift_card.gift_card', 'Gift Card', readonly=True
    )
    party = fields.Many2One('party.party', 'Party', required=True)
    amount = fields.Numeric('Amount', digits=(16, 2), required=True)
    address = fields.Many2One(
        'party.address', 'Billing Address', required=True,
        domain=[('party', '=', Eval('party'))],
        depends=['party']
    )
    currency = fields.Many2One('currency.currency', 'Currency', required=True)
    currency_digits = fields.Function(
        fields.Integer('Currency Digits'),
        'on_change_with_currency_digits'
    )

    @staticmethod
    def default_currency():
        """
        Set currency of current company as default currency
        """
        Company = Pool().get('company.company')

        company_id = Transaction().context.get('company') or None
        if company_id:
            return Company(company_id).currency.id

    @fields.depends('currency')
    def on_change_with_currency_digits(self, name=None):
        if self.currency:
            return self.currency.digits
        return 2

    @fields.depends('party')
    def on_change_with_address(self, name=None):
        if self.party:
            return self.party.address_get('invoice')
        return None

    @fields.depends('gift_card', 'amount')
    def on_change_gift_card(self):
        self.set_available_amount(self.gift_card, self.amount)

    @fields.depends('gift_card', 'amount')
    def on_change_amount(self):
        self.set_available_amount(self.gift_card, self.amount)

    def set_available_amount(self, gift_card, amount):
        if gift_card:
            if amount > gift_card.amount_available:
                self.amount = gift_card.amount_available


class GiftCardRedeemDone(ModelView):
    "Gift Card Redeem Done View"
    __name__ = 'gift_card.redeem.end'

    done_msg = fields.Text('Redemption Complete', readonly=True)


class GiftCardRedeemWizard(Wizard):
    "Gift Card Redeem Wizard"
    __name__ = 'gift_card.redeem.wizard'

    start = StateView(
        'gift_card.redeem.start',
        'gift_card.redeem_start_view_form',
        [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button(
                'Redeem', 'redeem',
                'tryton-ok', default=True
            )
        ]
    )
    redeem = StateTransition()
    done = StateView(
        'gift_card.redeem.end',
        'gift_card.redeem_done_view_form',
        [
            Button('OK', 'end', 'tryton-ok')
        ]
    )

    def default_start(self, data):
        """
        Initial state of redeem wizard.
        """
        Gateway = Pool().get('payment_gateway.gateway')
        GiftCard = Pool().get('gift_card.gift_card')

        try:
            gift_card_id, = Transaction().context.get('active_ids')
        except ValueError:
            raise UserError(
                gettext('gift_card.multiple_giftcards'))

        gift_card = GiftCard(gift_card_id)

        self.check_giftcard_state(gift_card)

        res = {
            'gift_card': gift_card.id,
            'amount': gift_card.amount_available,
        }
        try:
            gateway, = Gateway.search([
                ('method', '=', 'gift_card'),
                ('active', '=', True),
            ])
            res.update({'gateway': gateway.id})
        except ValueError:
            pass

        return res

    def transition_redeem(self):
        """
        Transition where PaymentTransaction is created and associated
        with current gift card.
        """
        PaymentTransaction = Pool().get('payment_gateway.transaction')
        Date = Pool().get('ir.date')

        receivable = self.start.party.account_receivable_used
        transaction, = PaymentTransaction.create([{
            'description': self.start.description,
            'date': Date.today(),
            'party': self.start.party.id,
            'address': self.start.address,
            'amount': self.start.amount,
            'currency': self.start.currency.id,
            'gateway': self.start.gateway.id,
            'gift_card': self.start.gift_card.id,
            'credit_account': receivable.id if receivable else None,
        }])
        PaymentTransaction.capture([transaction])
        PaymentTransaction.post([transaction])

        return 'done'

    def default_done(self, data):
        """
        Returns a message with relevant details.
        """
        currency_code = self.start.gift_card.currency.code
        done_msg = gettext('gift_card.redeem_done_message',
            amount=self.start.amount,
            captured=self.start.gift_card.amount_captured,
            remaining=self.start.gift_card.amount_available,
            code=currency_code)
        print(done_msg)
        return {'done_msg': done_msg}

    def check_giftcard_state(self, gift_card):
        """
        Checks that the gift card is in active state, else throws error.
        """
        if gift_card.state == 'used':
            raise UserError(gettext('gift_card.gift_card_redeemed'))
        elif gift_card.state != 'active':
            raise UserError(gettext('gift_card.gift_card_inactive'))
