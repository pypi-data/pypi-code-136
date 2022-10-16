from datetime import date

from boatrace.models import StadiumTelCode
from boatrace.official.v1707.pages.pre_inspection_information_page.location import (
    create_event_entry_page_url,
)


def test_create_event_entry_page_url():
    assert (
        create_event_entry_page_url(StadiumTelCode.HEIWAJIMA, date(2022, 9, 15))
        == "https://boatrace.jp/owpc/pc/race/rankingmotor?jcd=04&hd=20220915"
    )
