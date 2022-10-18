from dataclasses import field
from dataclasses_json import config
from .utils import str_to_date_datetime, date_datetime_to_str


def DATE_FIELD():
    return field(
        metadata=config(
            encoder=date_datetime_to_str,
            decoder=str_to_date_datetime,
        )
    )
