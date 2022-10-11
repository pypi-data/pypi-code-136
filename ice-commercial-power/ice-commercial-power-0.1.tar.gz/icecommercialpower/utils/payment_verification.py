"""
Utilities to verify correctness of payments and transactions,
and whether they match each other.
"""
import logging
import math

from icecommercialpower.flutterwave import FwTransaction, FwTransactionStatus
from icecommercialpower.payments import Payment
from icecommercialpower.steamaco import Transaction


def payment_matches_flutterwave_tx(
    payment_in_db: Payment,
    flutterwave_transaction: FwTransaction,
    log_non_matching_fields=False,
) -> bool:
    """
    Compares payment in the DB to the transaction info from Flutterwave.
    Returns True if the payment in DB matches result from Flutterwave.
    """
    valid_id = flutterwave_transaction.tx_ref == payment_in_db.id
    valid_currency = flutterwave_transaction.currency == payment_in_db.currency
    valid_amount = (
        flutterwave_transaction.amount >= payment_in_db.amount
        or _equal_amounts(flutterwave_transaction.amount, payment_in_db.amount)
    )

    valid_settled_amount = True

    if flutterwave_transaction.status == FwTransactionStatus.SUCCESSFUL:
        if flutterwave_transaction.amount_settled is None:
            valid_settled_amount = False
        else:
            """ We don't want to compare the settled amount to the amount in the DB
            Because the settled amount varies depending on who pays transaction fee
            and aparently on flutterwave testmode transaction fee is always deducted
            from the amount paid which makes settled amount lesser than amount in DB.
            """
            #  The Change below was made to fix a bug which occurs on staging;
            # paid_amount = flutterwave_transaction.amount_settled
            paid_amount = flutterwave_transaction.charged_amount
            valid_settled_amount = (
                paid_amount >= payment_in_db.amount
                or _equal_amounts(paid_amount, payment_in_db.amount)
            )

    if log_non_matching_fields:
        if not valid_id:
            logging.error(
                "Id/Ref is not matching: db %s, Flutterwave %s",
                payment_in_db.id,
                flutterwave_transaction.tx_ref,
            )
        if not valid_currency:
            logging.error(
                "Currency is not matching: db %s, Flutterwave %s",
                payment_in_db.currency,
                flutterwave_transaction.currency,
            )
        if not valid_settled_amount:
            logging.error(
                "Settled amount is not valid: db %s, Flutterwave settled: %s, charged_amount: %s, amount: %s, app_fee: %s",  # pylint: disable=line-too-long
                payment_in_db.amount,
                flutterwave_transaction.amount_settled,
                flutterwave_transaction.charged_amount,
                flutterwave_transaction.amount,
                flutterwave_transaction.app_fee,
            )
        if not valid_amount:
            logging.error(
                "Amount is not matching: db %s, Flutterwave %s",
                payment_in_db.amount,
                flutterwave_transaction.amount,
            )

    return valid_id and valid_currency and valid_amount and valid_settled_amount


def is_paid_in_full(
    payment_in_db: Payment, flutterwave_transaction: FwTransaction
) -> bool:
    """
    Checks if flutterwave transaction was susscessful and
    compares payment in the DB to the transaction info from Flutterwave.
    Returns True if the payment was paid by the customer.
    """
    return (
        flutterwave_transaction.status == FwTransactionStatus.SUCCESSFUL
        and payment_matches_flutterwave_tx(payment_in_db, flutterwave_transaction)
    )


def payment_matches_steamaco_tx(
    payment_in_db: Payment,
    steamaco_tx: Transaction,
):
    """
    Compares payment in the DB to the transaction record in SteamaCo.
    Determines if this transaction corresponds to this payment.
    """
    return (
        payment_in_db.id == steamaco_tx.reference
        and payment_in_db.customer_id == steamaco_tx.customer_id
        and _equal_amounts(payment_in_db.amount, steamaco_tx.amount)
        and (payment_in_db.currency, steamaco_tx.currency)
        in {
            ("NGN", "NRN"),  # mapping between our currencies and SteamaCo currencies
        }
        and (
            payment_in_db.steamaco_id is None
            or payment_in_db.steamaco_id == steamaco_tx.id
        )
    )


# Amounts are floats, and we need an almost-equality check
# to avoid the (unlikely) floating point precision errors.
def _equal_amounts(amount1: float, amount2: float):
    return math.isclose(amount1, amount2, rel_tol=1e-12)
