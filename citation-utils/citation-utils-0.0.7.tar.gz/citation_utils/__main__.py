import datetime
from enum import Enum
from typing import Iterator

from citation_report import Report
from pydantic import BaseModel
from slugify import slugify

from .constructors import CitationType, Docket, Style
from .helpers import filter_out_docket_reports


class DocketCategory(str, Enum):
    GR = Style.GR.value.short_category
    AM = Style.AM.value.short_category
    AC = Style.AC.value.short_category
    BM = Style.BM.value.short_category


class Citation(BaseModel):
    docket: str | None = None
    docket_category: DocketCategory | None = None
    docket_serial: str | None = None
    docket_date: datetime.date | None = None
    phil: str | None = None
    scra: str | None = None
    offg: str | None = None

    class Config:
        use_enum_values = True

    @property
    def slug(self) -> str | None:
        """If any of the possible values are present, convert this into a slug that can serve as a primary key."""
        els = [self.docket, self.scra, self.phil, self.offg]
        values = [el for el in els if el is not None]
        return slugify(" ".join(values)).strip() or None

    @classmethod
    def from_details(cls, data: dict):
        """Requires `docket`, `scra`, `phil` and `offg` keys set in the `data` dictionary. This enables creation of the Citation object from the originally scraped details.yaml"""
        if data.get("docket"):
            try:
                cite = next(cls.find_citations(data["docket"]))
            except StopIteration:
                cite = None
        return cls(
            docket=cite.docket if cite else None,
            docket_category=cite.docket_category if cite else None,
            docket_serial=cite.docket_serial if cite else None,
            docket_date=cite.docket_date if cite else None,
            phil=Report.extract_from_dict(data, "phil"),
            scra=Report.extract_from_dict(data, "scra"),
            offg=Report.extract_from_dict(data, "offg"),
        )

    @classmethod
    def get_styles(cls, raw: str) -> list[CitationType]:
        """Combine `Docket`s (which have `Reports`), and filtered `Report` models, if they exist."""
        if dockets := list(Style.extract(raw)):
            # each docket may have a report
            if reports := list(Report.extract(raw)):
                # duplicate reports now possible
                if undocketed := filter_out_docket_reports(
                    raw, dockets, reports
                ):
                    # ensures unique reports
                    return dockets + list(undocketed)
                return dockets + reports
            return dockets
        else:
            if reports := list(Report.extract(raw)):
                return reports
        return []

    @classmethod
    def find_citations(cls, text: str) -> Iterator["Citation"]:
        """Generate different docket / report types from the `text`."""
        for c in cls.get_styles(text):
            citation_data = {}
            if isinstance(c, Docket) and c.ids:
                citation_data = {
                    "docket": str(c),
                    "docket_category": c.short_category,
                    "docket_serial": c.first_id,
                    "docket_date": c.docket_date,
                }
            if isinstance(c, Report):
                citation_data |= {
                    "phil": c.phil,
                    "scra": c.scra,
                    "offg": c.offg,
                }
            yield cls(**citation_data)
