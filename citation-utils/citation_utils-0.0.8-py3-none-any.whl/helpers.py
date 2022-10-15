from typing import Iterator

from citation_report import Report
from dateutil.parser import parse

from .constructors import CitationType


def help_remove_docketed(
    dockets: list[CitationType],
    volpubpage_texts: list[str],
) -> list[str]:
    """Since Dockets contain `Report`s and each `Report` has a volpubpage; edit list of volpubpages to exclude volpubpages which are already included in dockets"""
    for docket in dockets:
        if docket.volpubpage:
            if docket.volpubpage in volpubpage_texts:
                volpubpage_texts.remove(docket.volpubpage)
    return volpubpage_texts


def help_clear_docket_reports(
    unique_texts: list[str],
    docketed_reports: list[CitationType],
    just_reports: list[Report],
) -> Iterator[Report]:
    """Given text get unique reports (through` volpubpages`) that are not contained in the existing list of dockets `ds`"""
    if volpubpages := help_remove_docketed(docketed_reports, unique_texts):
        for v in volpubpages:
            for report in just_reports:
                if report.volpubpage == v:
                    yield report


def filter_out_docket_reports(
    raw: str, dockets: list[CitationType], just_reports: list[Report]
) -> list[Report] | None:
    """If separate `Report`s are found; but these are already included in Docket models, remove/filter out these redundant `Report`s"""
    if u := Report.get_unique(raw):
        if x_reports := help_clear_docket_reports(u, dockets, just_reports):
            return list(x_reports)
    return None


def create_docket_string(serial: str, d: str) -> str | None:
    """
    >>> serial = 'G.R. No. 2335'
    >>> d = '5/1/2019'
    >>> create_docket_string(serial, d)
    'G.R. No. 2335, May 01, 2019'
    """
    return f'{serial}, {parse(d).date().strftime("%B %d, %Y")}'
