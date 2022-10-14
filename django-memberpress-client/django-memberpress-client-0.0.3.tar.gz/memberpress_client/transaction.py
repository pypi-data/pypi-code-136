# Python stuff
import json
import logging
from datetime import datetime

# our stuff
from memberpress_client.client import MemberpressAPIClient
from memberpress_client.constants import COMPLETE_TRANSACTION_DICT
from memberpress_client.utils import str2datetime

logger = logging.getLogger(__name__)


class Transaction(MemberpressAPIClient):
    _json = None

    def __init__(self, transaction=None) -> None:
        super().__init__()
        if self.is_valid(transaction):
            self._json = transaction

    def is_valid(self, value) -> bool:
        if type(value) != dict:
            return False
        return True

    @property
    def is_complete_dict(self) -> bool:
        """
        validate that response is a json dict containing at least
        the keys in qc_keys. These are the dict keys returned by the
        MemberPress REST api "/me" endpoint for a subscribed user.
        """
        qc_keys = COMPLETE_TRANSACTION_DICT
        return self.is_valid_dict(self.json, qc_keys)

    @property
    def json(self) -> json:
        return self._json

    @property
    def membership(self) -> int:
        try:
            return int(self.json["membership"])
        except Exception:
            return None

    @property
    def member(self) -> int:
        try:
            return int(self.json["member"])
        except Exception:
            return None

    @property
    def coupon(self) -> int:
        try:
            return int(self.json["coupon"])
        except Exception:
            return None

    @property
    def subscription(self) -> int:
        try:
            return int(self.json["subscription"])
        except Exception:
            return None

    @property
    def transaction(self) -> int:
        try:
            return int(self.json["transaction"])
        except Exception:
            return None

    @property
    def id(self) -> int:
        try:
            return int(self.json["id"])
        except Exception:
            return None

    @property
    def amount(self) -> float:
        try:
            return float(self.json["amount"])
        except Exception:
            return None

    @property
    def total(self) -> float:
        try:
            return float(self.json["total"])
        except Exception:
            return None

    @property
    def tax_amount(self) -> float:
        try:
            return float(self.json["tax_amount"])
        except Exception:
            return None

    @property
    def tax_rate(self) -> float:
        try:
            return float(self.json["tax_rate"])
        except Exception:
            return None

    @property
    def tax_desc(self) -> str:
        return self.json.get("tax_desc", None)

    @property
    def tax_class(self) -> str:
        return self.json.get("tax_class", None)

    @property
    def trans_num(self) -> str:
        return self.json.get("trans_num", None)

    @property
    def status(self) -> str:
        return self.json.get("status", None)

    @property
    def txn_type(self) -> str:
        return self.json.get("txn_type", None)

    @property
    def gateway(self) -> str:
        return self.json.get("gateway", None)

    @property
    def prorated(self) -> int:
        try:
            return int(self.json["prorated"])
        except Exception:
            return None

    @property
    def created_at(self) -> datetime:
        date_str = self.json.get("created_at", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read created_at for id {id}".format(id=self.id))
            return None

    @property
    def expires_at(self) -> datetime:
        date_str = self.json.get("expires_at", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read expires_at for id {id}".format(id=self.id))
            return None

    @property
    def corporate_account_id(self) -> int:
        try:
            return int(self.json["corporate_account_id"])
        except Exception:
            return None

    @property
    def parent_transaction_id(self) -> int:
        try:
            return int(self.json["parent_transaction_id"])
        except Exception:
            return None

    @property
    def tax_compound(self) -> int:
        try:
            return int(self.json["tax_compound"])
        except Exception:
            return None

    @property
    def tax_shipping(self) -> int:
        try:
            return int(self.json["tax_shipping"])
        except Exception:
            return None

    @property
    def response(self) -> str:
        return self.json.get("response", None)
