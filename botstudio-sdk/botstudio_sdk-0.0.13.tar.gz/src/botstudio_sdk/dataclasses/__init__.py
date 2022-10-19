from dataclasses import dataclass, field
from typing import Union, List, Text, Any, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# from actions.variable_names import IntentName


@dataclass(frozen=False)
class QuestionInfo:
    tracker: Union[Tracker, None]
    dispatcher: Union[CollectingDispatcher, None]
    slot_name: Union[Text, None]


@dataclass(frozen=False)
class ValidateInfo:
    """
    Dataclass used during slot validation

    info = ValidateInfo(
        value=value
        dispatcher=dispatcher,
        tracker=tracker,
        domain=domain,
    )
    """

    value: Union[Any, None]
    tracker: Union[Tracker, None]
    dispatcher: Union[CollectingDispatcher, None]
    domain: Union[DomainDict, None]


@dataclass(frozen=False)
class ExtractInfo:
    """
    Dataclass used during slot extraction

    info = ExtractInfo(
        dispatcher=dispatcher,
        tracker=tracker,
        domain=domain,
    )
    """

    tracker: Union[Tracker, None]
    dispatcher: Union[CollectingDispatcher, None]
    domain: Union[DomainDict, None]


# @dataclass(frozen=False)
# class MappingInfo:
#     query_agent: List = field(
#         default_factory=lambda: [
#             IntentName.change_agent,
#             # IntentName.give_name,
#         ]
#     )
#     query_service: List = field(
#         default_factory=lambda: [
#             IntentName.change_service,
#             IntentName.give_service,
#         ]
#     )
#     query_date: List = field(
#         default_factory=lambda: [
#             IntentName.change_date,
#             IntentName.give_data,
#
#         ]
#     )
#     query_time: List = field(
#         default_factory=lambda: [
#             IntentName.give_time,
#             IntentName.change_time,
#         ]
#     )
#
#     query_customer_phone: List = field(
#         default_factory=lambda: [
#             IntentName.give_phone_number,
#             IntentName.change_phone,
#         ]
#     )
#     query_customer_email: List = field(
#         default_factory=lambda: [
#             IntentName.give_email_address,
#             IntentName.change_email,
#         ]
#     )
#     query_customer_note: List = field(
#         default_factory=lambda: [IntentName.change_message],
#     )
#     stop_form: List = field(
#         default_factory=lambda: [
#             IntentName.stop,
#         ]
#     )
#     previous_question: List = field(
#         default_factory=lambda: [
#             IntentName.previous_question,
#         ]
#     )
#     ask_again: List = field(
#         default_factory=lambda: [
#             IntentName.affirm,
#         ]
#     )


@dataclass
class SlotInfo:
    value: Union[str, list]
    slot_name: str
    slot_order: list


@dataclass(frozen=False)
class QuotationInfo:
    bathroom_wall_sq_m: Optional[str]
    bathroom_wall_surface: Optional[str]
    bathroom_wall_finish: Optional[str]
    bathroom_ceiling_sq_m: Optional[str]
    bathroom_ceiling_surface: Optional[str]
    bathroom_ceiling_finish: Optional[str]
    customer_name: Optional[str]
    customer_email: Optional[str]
    customer_phone: Optional[str]
    customer_note: Optional[str]


@dataclass(frozen=False)
class PriceIndicatorEmailInfo:
    email_body: Optional[str]
    customer_email: Optional[str]
    customer_name: Optional[str]
