from pathlib import Path
from typing import Iterable
from singer_sdk.streams import Stream
from datetime import date, datetime

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class CalendarStream(Stream):

    name = "calendar"
    primary_keys = ["date_key"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "calendar.json"

    def get_records(self, context):
        start_date = datetime.strptime(self.config.get("start_date"), "%Y-%m-%d").date()
        end_date = datetime.strptime(self.config.get("end_date"), "%Y-%m-%d").date()
        return generate_calendar(start_date, end_date)


def generate_calendar(start_date, end_date):
    dates = (date.fromordinal(ordinal) for ordinal in range(start_date.toordinal(), end_date.toordinal()+1))
    for d in dates:
        week = d.isocalendar()[1]
        quarter = (d.month-1)//3 + 1
        yield {
        "date_key": int(d.strftime("%Y%m%d")),
        "date": d.strftime("%Y-%m-%d"),
        "weekday_name": d.strftime("%A"),
        "weekday_name3": d.strftime("%a"),
        "month_name": d.strftime("%B"),
        "month_name3": d.strftime("%b"),
        "year_week": f"{d.year}W{week}",
        "year_month": d.strftime("%Y-%m"),
        "year_quarter": f"{d.year}Q{quarter}",
        "year": d.year,
        "day_of_week": d.weekday()+1,
        "day_of_month": d.day,       
        "day_of_quarter": None,
        "day_of_year": d.timetuple().tm_yday,
        "week_of_month": None,
        "week_of_quarter": None,
        "week_of_year": week,
        "month_of_year": d.month,
        "month_of_quarter": None,
        "quarter_of_year": quarter
    }        