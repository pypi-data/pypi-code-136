import datetime
from enum import Enum
from typing import Iterator

from citation_report import Report, get_reports
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
        """Requires `orig_idx`, `docket`, and `date_prom` keys set in the `data` dictionary. This enables creation of the Citation object from the originally scraped details.yaml"""
        if data.get("docket"):
            try:
                cite = next(cls.find_citations(data["docket"]))
                cat = cite.docket_category
                idx = cite.docket_serial
                date = cite.docket_date
            except StopIteration:
                cite = None
                cat = None
                idx = None
                date = None

        if data.get("scra"):
            try:
                scra = next(get_reports(data["scra"])).scra
            except StopIteration:
                scra = None

        if data.get("phil"):
            try:
                phil = next(get_reports(data["phil"])).phil
            except StopIteration:
                phil = None

        if data.get("offg"):
            try:
                offg = next(get_reports(data["offg"])).offg
            except StopIteration:
                offg = None

        if any(i for i in [cite, scra, phil, offg]):
            return cls(
                docket_category=cat,
                docket_serial=idx,
                docket_date=date,
                phil=phil,
                scra=scra,
                offg=offg,
            )
        return None

    @classmethod
    def get_styles(cls, raw: str) -> list[CitationType]:
        """Combine `Docket`s (which have `Reports`), and filtered `Report` models, if they exist."""
        if dockets := list(
            Style.extract(raw)
        ):  # each docket may have a report
            if reports := list(
                get_reports(raw)
            ):  # duplicate reports now possible
                if undocketed := filter_out_docket_reports(
                    raw, dockets, reports
                ):
                    return dockets + list(undocketed)  # ensures unique reports
                return dockets + reports
            return dockets
        else:
            if reports := list(get_reports(raw)):
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
