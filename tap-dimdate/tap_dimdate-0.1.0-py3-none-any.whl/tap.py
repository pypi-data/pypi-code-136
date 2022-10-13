"""DimDate tap class."""

from typing import List
from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_dimdate.streams import (
    CalendarStream
)


class TapDimDate(Tap):

    name = "tap-dimdate"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateType,
            required=True,
            default="2022-01-01",
            description="The earliest record date to sync"
        ),
        th.Property(
            "end_date",
            th.DateType,
            required=True,
            default="2022-12-31",
            description="The latest record date to sync"
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [CalendarStream(tap=self)]


if __name__ == "__main__":
    TapDimDate.cli()
