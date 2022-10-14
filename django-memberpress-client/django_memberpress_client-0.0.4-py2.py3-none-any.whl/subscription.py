# Python stuff
import json
import logging
from datetime import datetime

# our stuff
from memberpress_client.client import MemberpressAPIClient
from memberpress_client.constants import COMPLETE_SUBSCRIPTION_DICT
from memberpress_client.utils import str2datetime

logger = logging.getLogger(__name__)


class Subscription(MemberpressAPIClient):
    def __init__(self, subscription=None) -> None:
        super().__init__()
        self.init()
        if self.is_valid(subscription):
            self.json = subscription
        else:
            logger.warning("received an invalid subscription object: {o}".format(o=subscription))

    def init(self):
        super().init()

    @property
    def is_complete_dict(self) -> bool:
        """
        validate that response is a json dict containing at least
        the keys in qc_keys. These are the dict keys returned by the
        MemberPress REST api "/me" endpoint for a subscribed user.
        """
        qc_keys = COMPLETE_SUBSCRIPTION_DICT
        return self.is_valid_dict(self.json, qc_keys)

    @property
    def coupon(self) -> int:
        try:
            return int(self.json["coupon"])
        except Exception:
            return None

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
    def id(self) -> int:
        try:
            return int(self.json["id"])
        except Exception:
            return None

    @property
    def subscriber_id(self) -> str:
        return self.json.get("subscr_id", None)

    @property
    def gateway(self) -> str:
        return self.json.get("gateway", None)

    @property
    def price(self) -> float:
        try:
            return float(self.json["price"])
        except Exception:
            return None

    @property
    def period(self) -> int:
        try:
            return int(self.json["period"])
        except Exception:
            return None

    @property
    def period_type(self) -> str:
        return self.json.get("period_type", None)

    @property
    def limit_cycles(self) -> int:
        try:
            return int(self.json["limit_cycles"])
        except Exception:
            return None

    @property
    def limit_cycles_num(self) -> int:
        try:
            return int(self.json["limit_cycles_num"])
        except Exception:
            return None

    @property
    def limit_cycles_action(self) -> str:
        return self.json.get("limit_cycles_action", None)

    @property
    def limit_cycles_expires_after(self) -> int:
        try:
            return int(self.json["limit_cycles_expires_after"])
        except Exception:
            return None

    @property
    def limit_cycles_expires_type(self) -> str:
        return self.json.get("limit_cycles_expires_type", None)

    @property
    def prorated_trial(self) -> int:
        try:
            return int(self.json["prorated_trial"])
        except Exception:
            return None

    @property
    def trial(self) -> int:
        try:
            return int(self.json["trial"])
        except Exception:
            return None

    @property
    def trial_days(self) -> int:
        try:
            return int(self.json["trial_days"])
        except Exception:
            return None

    @property
    def trial_amount(self) -> float:
        try:
            return float(self.json["trial_amount"])
        except Exception:
            return None

    @property
    def trial_tax_amount(self) -> float:
        try:
            return float(self.json["trial_tax_amount"])
        except Exception:
            return None

    @property
    def trial_total(self) -> float:
        try:
            return float(self.json["trial_total"])
        except Exception:
            return None

    @property
    def status(self) -> str:
        return self.json.get("status", None)

    @property
    def created_at(self) -> datetime:
        date_str = self.json.get("created_at", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read created_at for id {id}".format(id=self.id))
            return None

    @property
    def total(self) -> float:
        try:
            return float(self.json["total"])
        except Exception:
            return None

    @property
    def tax_rate(self) -> float:
        try:
            return float(self.json["tax_rate"])
        except Exception:
            return None

    @property
    def tax_amount(self) -> float:
        try:
            return float(self.json["tax_amount"])
        except Exception:
            return None

    @property
    def tax_desc(self) -> str:
        return self.json.get("tax_desc", None)

    @property
    def tax_class(self) -> str:
        return self.json.get("tax_class", None)

    @property
    def cc_last4(self) -> int:
        try:
            return int(self.json["cc_last4"])
        except Exception:
            return None

    @property
    def cc_exp_month(self) -> int:
        try:
            return int(self.json["cc_exp_month"])
        except Exception:
            return None

    @property
    def cc_exp_year(self) -> int:
        try:
            return int(self.json["cc_exp_year"])
        except Exception:
            return None

    @property
    def token(self) -> str:
        return self.json.get("token", None)

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
