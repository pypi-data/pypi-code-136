from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, datetime
import json
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from benchling_api_client.v2.alpha.models.boolean_app_config_item_type import BooleanAppConfigItemType
from benchling_api_client.v2.alpha.models.date_app_config_item_type import DateAppConfigItemType
from benchling_api_client.v2.alpha.models.datetime_app_config_item_type import DatetimeAppConfigItemType
from benchling_api_client.v2.alpha.models.float_app_config_item_type import FloatAppConfigItemType
from benchling_api_client.v2.alpha.models.generic_app_config_item_type import GenericAppConfigItemType
from benchling_api_client.v2.alpha.models.integer_app_config_item_type import IntegerAppConfigItemType
from benchling_api_client.v2.alpha.models.json_app_config_item_type import JsonAppConfigItemType
from benchling_api_client.v2.alpha.models.secure_text_app_config_item_type import SecureTextAppConfigItemType
from typing_extensions import Literal

JsonType = Union[Dict[str, Any], List[Any], str, int, float, bool]
ScalarType = TypeVar("ScalarType", bool, date, datetime, float, int, JsonType, str)
# JsonType support requires object to be unioned. Currently we do it inline.
ScalarModelType = Union[bool, date, datetime, float, int, str]
# Enum values cannot be used in literals, so copy the strings
ScalarConfigItemType = Literal[
    "boolean",  # BooleanAppConfigItemType.BOOLEAN,
    "date",  # DateAppConfigItemType.DATE,
    "datetime",  # DatetimeAppConfigItemType.DATETIME,
    "float",  # FloatAppConfigItemType.FLOAT,
    "text",  # GenericAppConfigItemType.TEXT,
    "integer",  # IntegerAppConfigItemType.INTEGER,
    "json",  # JsonAppConfigItemType.JSON,
    "secure_text",  # SecureTextAppConfigItemType.SECURE_TEXT,
]


class ScalarDefinition(ABC, Generic[ScalarType]):
    """
    Scalar definition.

    Map how ScalarConfigTypes values can be converted into corresponding Python types.
    """

    @classmethod
    def init(cls):
        """Init."""
        return cls()

    @abstractmethod
    def from_str(self, value: Optional[str]) -> Optional[ScalarType]:
        """
        From string.

        Given an optional string value of scalar configuration, produce an Optional instance of the
        specific ScalarType. For instance, converting str to int.

        Used when coercing Python types from string values in API responses.
        """
        pass


class BoolScalar(ScalarDefinition[bool]):
    """
    Bool Scalar.

    Turn a Boolean-like string value into bool. Any permutation of "true" - case insensitive - is interpreted
    as True. Any other non-empty string is False.
    """

    def from_str(self, value: Optional[str]) -> Optional[bool]:
        """Convert optional str to optional bool."""
        # Though the spec declares str, this is actually being sent in JSON as a real Boolean
        # So runtime check defensively
        if value is not None:
            if isinstance(value, bool):
                return value
            if value.lower() == "true":
                return True
            return False
        return None


class DateScalar(ScalarDefinition[date]):
    """
    Date Scalar.

    Turn an ISO formatted date like YYYY-MM-dd into a date.
    """

    def from_str(self, value: Optional[str]) -> Optional[date]:
        """Convert optional str to optional date."""
        return date.fromisoformat(value) if value is not None else None


class DateTimeScalar(ScalarDefinition[datetime]):
    """
    Date Time Scalar.

    Turn a date time string into datetime.
    """

    def from_str(self, value: Optional[str]) -> Optional[datetime]:
        """Convert optional str to optional datetime."""
        return datetime.strptime(value, self.expected_format()) if value is not None else None

    @staticmethod
    def expected_format() -> str:
        """Return the expected date mask for parsing string to datetime."""
        return "%Y-%m-%d %H:%M:%S %p"


class FloatScalar(ScalarDefinition[float]):
    """
    Float Scalar.

    Turn a string into float. Assumes the string, if not empty, is a valid floating point.
    """

    def from_str(self, value: Optional[str]) -> Optional[float]:
        """Convert optional str to optional float."""
        return float(value) if value is not None else None


class IntScalar(ScalarDefinition[int]):
    """
    Int Scalar.

    Turn a string into int. Assumes the string, if not empty, is a valid integer.
    """

    def from_str(self, value: Optional[str]) -> Optional[int]:
        """Convert optional str to optional int."""
        return int(value) if value is not None else None


class JsonScalar(ScalarDefinition[JsonType]):
    """
    Json Scalar.

    Turn a string into JSON. Assumes the string is a valid JSON string.
    """

    def from_str(self, value: Optional[str]) -> Optional[JsonType]:
        """Convert optional str to optional JsonType."""
        return json.loads(value) if value is not None else None


class TextScalar(ScalarDefinition[str]):
    """
    Text Scalar.

    Text is already a string, so no conversion is performed.
    """

    def from_str(self, value: Optional[str]) -> Optional[str]:
        """Convert optional str to optional str. Implemented to appease ScalarDefinition contract."""
        return value


class SecureTextScalar(TextScalar):
    """
    Secure Text Scalar.

    Text is already a string, so no conversion is performed.
    """

    pass


# Maps scalar types from the API into typed Python SDK scalar definitions
DEFAULT_SCALAR_DEFINITIONS: Dict[ScalarConfigItemType, ScalarDefinition] = {
    BooleanAppConfigItemType.BOOLEAN.value: BoolScalar.init(),
    DateAppConfigItemType.DATE.value: DateScalar.init(),
    DatetimeAppConfigItemType.DATETIME.value: DateTimeScalar.init(),
    FloatAppConfigItemType.FLOAT.value: FloatScalar.init(),
    IntegerAppConfigItemType.INTEGER.value: IntScalar.init(),
    JsonAppConfigItemType.JSON.value: JsonScalar.init(),
    SecureTextAppConfigItemType.SECURE_TEXT.value: SecureTextScalar.init(),
    GenericAppConfigItemType.TEXT.value: TextScalar.init(),
}
