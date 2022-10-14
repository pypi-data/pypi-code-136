# Python stuff
import json
import logging
from datetime import datetime

# our stuff
from memberpress_client.client import MemberpressAPIClient
from memberpress_client.constants import COMPLETE_MEMBERSHIP_DICT
from memberpress_client.utils import str2datetime

logger = logging.getLogger(__name__)


class Membership(MemberpressAPIClient):

    _json = None

    def __init__(self, membership=None) -> None:
        super().__init__()
        if self.is_valid(membership):
            self._json = membership

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
        qc_keys = COMPLETE_MEMBERSHIP_DICT
        return self.is_valid_dict(self.member, qc_keys)

    @property
    def json(self) -> json:
        return self._json

    @property
    def id(self) -> int:
        try:
            return int(self.json["id"])
        except Exception:
            return None

    @property
    def title(self) -> str:
        return self.json.get("title", None)

    @property
    def content(self) -> str:
        return self.json.get("content", None)

    @property
    def excerpt(self) -> str:
        return self.json.get("excerpt", None)

    @property
    def date(self) -> datetime:
        date_str = self.json.get("date", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read date for id {id}".format(id=self.id))
            return None

    @property
    def status(self) -> str:
        return self.json.get("status", None)

    @property
    def author(self) -> int:
        try:
            return int(self.json["author"])
        except Exception:
            return None

    @property
    def date_gmt(self) -> datetime:
        date_str = self.json.get("date_gmt", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read date_gmt for id {id}".format(id=self.id))
            return None

    @property
    def modified(self) -> datetime:
        date_str = self.json.get("modified", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read modified for id {id}".format(id=self.id))
            return None

    @property
    def modified_gmt(self) -> datetime:
        date_str = self.json.get("modified_gmt", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read modified_gmt for id {id}".format(id=self.id))
            return None

    @property
    def group(self) -> int:
        try:
            return int(self.json["group"])
        except Exception:
            return None

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
    def signup_button_text(self) -> str:
        return self.json.get("signup_button_text", None)

    @property
    def limit_cycles(self) -> bool:
        try:
            v = str(self.json.get("limit_cycles", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

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
    def trial_amount(self) -> int:
        try:
            return int(self.json["trial_amount"])
        except Exception:
            return None

    @property
    def trial_once(self) -> int:
        try:
            return int(self.json["trial_once"])
        except Exception:
            return None

    @property
    def group_order(self) -> int:
        try:
            return int(self.json["group_order"])
        except Exception:
            return None

    @property
    def is_highlighted(self) -> int:
        try:
            return int(self.json["is_highlighted"])
        except Exception:
            return None

    @property
    def plan_code(self) -> str:
        return self.json.get("plan_code", None)

    @property
    def pricing_title(self) -> str:
        return self.json.get("pricing_title", None)

    @property
    def pricing_show_price(self) -> bool:
        try:
            v = str(self.json.get("pricing_show_price", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def pricing_display(self) -> str:
        return self.json.get("pricing_display", None)

    @property
    def custom_price(self) -> str:
        return self.json.get("custom_price", None)

    @property
    def pricing_heading_txt(self) -> str:
        return self.json.get("pricing_heading_txt", None)

    @property
    def pricing_footer_txt(self) -> str:
        return self.json.get("pricing_footer_txt", None)

    @property
    def pricing_button_txt(self) -> str:
        return self.json.get("pricing_button_txt", None)

    @property
    def pricing_button_position(self) -> str:
        return self.json.get("pricing_button_position", None)

    @property
    def pricing_benefits(self) -> list:
        return self.json.get("pricing_benefits", None)

    @property
    def register_price_action(self) -> str:
        return self.json.get("register_price_action", None)

    @property
    def register_price(self) -> str:
        return self.json.get("register_price", None)

    @property
    def thank_you_page_enabled(self) -> bool:
        try:
            v = str(self.json.get("thank_you_page_enabled", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def thank_you_page_type(self) -> str:
        return self.json.get("thank_you_page_type", None)

    @property
    def thank_you_message(self) -> str:
        return self.json.get("thank_you_message", None)

    @property
    def thank_you_page_id(self) -> int:
        try:
            return int(self.json["thank_you_page_id"])
        except Exception:
            return None

    @property
    def custom_login_urls_enabled(self) -> int:
        try:
            return int(self.json["custom_login_urls_enabled"])
        except Exception:
            return None

    @property
    def custom_login_urls_default(self) -> str:
        return self.json.get("custom_login_urls_default", None)

    @property
    def custom_login_urls(self) -> list:
        return self.json.get("custom_login_urls", None)

    @property
    def expire_type(self) -> str:
        return self.json.get("expire_type", None)

    @property
    def expire_after(self) -> int:
        try:
            return int(self.json["expire_after"])
        except Exception:
            return None

    @property
    def expire_unit(self) -> str:
        return self.json.get("expire_unit", None)

    @property
    def expire_fixed(self) -> datetime:
        date_str = self.json.get("expire_fixed", "")
        try:
            return str2datetime(date_str)
        except Exception:
            logger.warning("Cannot read date_gmt for id {id}".format(id=self.id))
            return None

    @property
    def tax_exempt(self) -> bool:
        try:
            v = str(self.json.get("tax_exempt", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def tax_class(self) -> str:
        return self.json.get("tax_class", None)

    @property
    def allow_renewal(self) -> bool:
        try:
            v = str(self.json.get("allow_renewal", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def access_url(self) -> str:
        return self.json.get("access_url", None)

    @property
    def disable_address_fields(self) -> bool:
        try:
            v = str(self.json.get("disable_address_fields", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def simultaneous_subscriptions(self) -> bool:
        try:
            v = str(self.json.get("simultaneous_subscriptions", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def use_custom_template(self) -> bool:
        try:
            v = str(self.json.get("use_custom_template", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def custom_template(self) -> str:
        return self.json.get("custom_template", None)

    @property
    def customize_payment_methods(self) -> int:
        try:
            return int(self.json["customize_payment_methods"])
        except Exception:
            return None

    @property
    def custom_payment_methods(self) -> list:
        return self.json.get("custom_payment_methods", None)

    @property
    def customize_profile_fields(self) -> bool:
        try:
            v = str(self.json.get("customize_profile_fields", "false")).lower()
            return True if v == "true" else False
        except Exception:
            return False

    @property
    def custom_profile_fields(self) -> list:
        return self.json.get("custom_profile_fields", None)

    @property
    def cannot_purchase_message(self) -> str:
        return self.json.get("cannot_purchase_message", None)
